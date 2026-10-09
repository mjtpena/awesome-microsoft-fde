"""The evaluation gate: score retrieval and answers separately, fail the build below the bar.

    python evals/run_evals.py                      # offline: local BM25 + extractive answers
    python evals/run_evals.py --retriever azure --answerer llm --judge

Retrieval and answer quality are scored separately on purpose. When a number
drops you need to know which half broke: the week-6 incident was a retrieval
fault that looked like a model fault.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

from harbourline.answering import Answer, ExtractiveAnswerer, LlmAnswerer, format_passages
from harbourline.corpus import Passage, load_passages
from harbourline.retrieval import AzureSearchRetriever, LocalRetriever

HERE = Path(__file__).resolve().parent


@dataclass
class CaseResult:
    id: str
    category: str
    retrieved: list[str]
    answer: str
    citations: list[str]
    refused: bool
    retrieval_hit: bool | None = None  # None: case has no expected documents
    forbidden_doc_retrieved: bool = False
    refusal_correct: bool | None = None  # None: case isn't a must-refuse case
    citation_correct: bool | None = None  # None: case should be refused
    fact_match: bool | None = None
    forbidden_content: bool = False
    faithful: bool | None = None  # only with --judge
    problems: list[str] = field(default_factory=list)


def score_case(case: dict, passages: list[Passage], answer: Answer) -> CaseResult:
    """Score one golden case. Pure function: no I/O, so it is unit-tested directly."""
    retrieved = list(dict.fromkeys(p.doc_id for p in passages))
    r = CaseResult(case["id"], case["category"], retrieved, answer.text, answer.citations, answer.refused)
    expected = set(case.get("expected_doc_ids", []))
    forbidden_docs = set(case.get("forbidden_doc_ids", []))
    text = answer.text.casefold()

    # Retrieval half: did the right documents come back, and did any forbidden ones?
    if expected:
        r.retrieval_hit = bool(expected & set(retrieved))
    r.forbidden_doc_retrieved = bool(forbidden_docs & set(retrieved))

    # Answer half.
    if case.get("should_refuse"):
        r.refusal_correct = answer.refused
    else:
        cited = set(answer.citations)
        r.citation_correct = not answer.refused and bool(cited & expected) and cited <= set(retrieved)
        r.fact_match = not answer.refused and all(k.casefold() in text for k in case.get("expected_keywords", []))
    r.forbidden_content = any(k.casefold() in text for k in case.get("forbidden_keywords", [])) or bool(
        forbidden_docs & set(answer.citations)
    )

    for name in ("retrieval_hit", "refusal_correct", "citation_correct", "fact_match"):
        if getattr(r, name) is False:
            r.problems.append(name)
    for name in ("forbidden_doc_retrieved", "forbidden_content"):
        if getattr(r, name):
            r.problems.append(name)
    return r


def _rate(values: list[bool | None]) -> float | None:
    scored = [v for v in values if v is not None]
    return round(sum(scored) / len(scored), 4) if scored else None


def summarise(results: list[CaseResult]) -> dict:
    return {
        "retrieval_hit_rate_at_k": _rate([r.retrieval_hit for r in results]),
        "forbidden_doc_retrieved": sum(r.forbidden_doc_retrieved for r in results),
        "citation_accuracy": _rate([r.citation_correct for r in results]),
        "fact_match": _rate([r.fact_match for r in results]),
        "refusal_accuracy": _rate([r.refusal_correct for r in results]),
        "forbidden_content": sum(r.forbidden_content for r in results),
        "faithfulness": _rate([r.faithful for r in results]),
    }


def gate(summary: dict, thresholds: dict) -> list[tuple[str, object, str, bool]]:
    """Compare each metric with its threshold. Returns (metric, value, bar, passed) rows."""
    rows = []
    for name, bar in thresholds.items():
        if name.startswith("_"):
            continue
        if name.endswith("_max"):
            value = summary[name[: -len("_max")]]
            rows.append((name[: -len("_max")], value, f"<= {bar}", value <= bar))
        elif summary.get(name) is not None:  # e.g. faithfulness is only scored with --judge
            rows.append((name, summary[name], f">= {bar}", summary[name] >= bar))
    return rows


class LlmJudge:
    """Optional faithfulness check: does every claim in the answer appear in the cited passages?"""

    PROMPT = (
        "You grade a policy assistant. Reply with exactly PASS if every statement in the ANSWER "
        "is supported by the PASSAGES, otherwise reply with exactly FAIL."
    )

    def __init__(self, gateway_url: str, model: str):
        import asyncio

        from agent_framework import Agent
        from agent_framework.openai import OpenAIChatCompletionClient
        from azure.identity import DefaultAzureCredential

        client = OpenAIChatCompletionClient(model=model, base_url=gateway_url, credential=DefaultAzureCredential())
        self._agent = Agent(client=client, instructions=self.PROMPT, name="harbourline-judge")
        self._run = asyncio.run

    def faithful(self, answer: str, passages: list[Passage]) -> bool:
        response = self._run(self._agent.run(f"PASSAGES:\n{format_passages(passages)}\n\nANSWER:\n{answer}"))
        return response.text.strip().upper().startswith("PASS")


def _mark(value: bool | None, good: bool = True) -> str:
    if value is None:
        return "-"
    return "ok" if value == good else "FAIL"


def print_report(results: list[CaseResult], rows: list[tuple[str, object, str, bool]]) -> None:
    header = ("case", 16), ("category", 19), ("retrieval", 10), ("leak-doc", 9), ("refusal", 8), ("citation", 9), ("facts", 6)
    print(" ".join(f"{name:<{width}}" for name, width in header) + " leak-text")
    for r in results:
        print(
            f"{r.id:<16} {r.category:<19} {_mark(r.retrieval_hit):<10} {_mark(r.forbidden_doc_retrieved, False):<9} "
            f"{_mark(r.refusal_correct):<8} {_mark(r.citation_correct):<9} {_mark(r.fact_match):<6} "
            f"{_mark(r.forbidden_content, False):<9}"
        )
    print()
    print(f"{'metric':<26} {'value':>7}  {'bar':<8} result")
    for name, value, bar, passed in rows:
        print(f"{name:<26} {value!s:>7}  {bar:<8} {'pass' if passed else 'FAIL'}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--retriever", choices=["local", "azure"], default="local")
    parser.add_argument("--answerer", choices=["extractive", "llm"], default="extractive")
    parser.add_argument("--judge", action="store_true", help="also grade faithfulness with the model (needs Azure)")
    parser.add_argument("-k", type=int, default=5)
    parser.add_argument("--golden", type=Path, default=HERE / "golden.jsonl")
    parser.add_argument("--thresholds", type=Path, default=HERE / "thresholds.json")
    parser.add_argument("--out", type=Path, default=HERE / "results.json")
    args = parser.parse_args(argv)

    if args.retriever == "local":
        retriever = LocalRetriever(load_passages()[0])
    else:
        retriever = AzureSearchRetriever(os.environ["AZURE_SEARCH_ENDPOINT"], os.environ["AZURE_SEARCH_INDEX"])
    if args.answerer == "extractive":
        answerer = ExtractiveAnswerer()
    else:
        answerer = LlmAnswerer(os.environ["HARBOURLINE_GATEWAY_URL"], os.environ["HARBOURLINE_MODEL"])
    judge = LlmJudge(os.environ["HARBOURLINE_GATEWAY_URL"], os.environ["HARBOURLINE_MODEL"]) if args.judge else None

    cases = [json.loads(line) for line in args.golden.read_text(encoding="utf-8").splitlines() if line.strip()]
    results = []
    for case in cases:
        passages = retriever.search(case["question"], case["user_groups"], k=args.k)
        answer = answerer.answer(case["question"], passages)
        result = score_case(case, passages, answer)
        if judge and not answer.refused:
            result.faithful = judge.faithful(answer.text, passages)
        results.append(result)

    summary = summarise(results)
    rows = gate(summary, json.loads(args.thresholds.read_text(encoding="utf-8")))
    print_report(results, rows)
    passed = all(ok for *_, ok in rows)
    args.out.write_text(
        json.dumps(
            {"config": {"retriever": args.retriever, "answerer": args.answerer, "judge": args.judge, "k": args.k},
             "summary": summary, "passed": passed, "cases": [asdict(r) for r in results]},
            indent=2, ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    print(f"\n{'PASSED' if passed else 'FAILED'}: {len(cases)} cases, results in {args.out}")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
