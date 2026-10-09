"""The scorer is code that gates releases, so it gets tests too."""

from harbourline.answering import Answer
from harbourline.corpus import Passage
from run_evals import gate, score_case, summarise


def passage(doc_id):
    return Passage(f"{doc_id}--s", doc_id, "t", "s", "text", ("all-staff",))


CASE = {
    "id": "c1", "category": "common", "question": "q",
    "expected_doc_ids": ["motor-excess-policy"], "expected_keywords": ["£95"],
    "should_refuse": False, "forbidden_doc_ids": ["motor-excess-policy-v2"], "forbidden_keywords": ["£75"],
}
REFUSE = {"id": "r1", "category": "must-refuse", "question": "q", "should_refuse": True,
          "forbidden_doc_ids": ["pricing-motor-rate-review-draft"], "forbidden_keywords": ["7.5%"]}


def test_good_answer_passes_everything():
    r = score_case(CASE, [passage("motor-excess-policy")], Answer("£95 [motor-excess-policy]", ["motor-excess-policy"]))
    assert r.retrieval_hit and r.citation_correct and r.fact_match
    assert not r.forbidden_content and not r.forbidden_doc_retrieved and r.problems == []


def test_retrieval_and_answer_are_scored_separately():
    # Right document retrieved, wrong fact in the answer: retrieval passes, answer fails.
    r = score_case(CASE, [passage("motor-excess-policy")], Answer("£75 [motor-excess-policy]", ["motor-excess-policy"]))
    assert r.retrieval_hit is True
    assert r.fact_match is False
    assert r.forbidden_content is True


def test_wrong_citation_fails_citation_check():
    r = score_case(CASE, [passage("motor-excess-policy"), passage("motor-total-loss")],
                   Answer("£95 [motor-total-loss]", ["motor-total-loss"]))
    assert r.citation_correct is False


def test_refusal_of_an_answerable_question_fails_facts_and_citation():
    r = score_case(CASE, [passage("motor-excess-policy")], Answer.refusal())
    assert r.citation_correct is False and r.fact_match is False
    assert r.refusal_correct is None  # refusal accuracy only counts must-refuse cases


def test_must_refuse_case():
    assert score_case(REFUSE, [], Answer.refusal()).refusal_correct is True
    leaked = score_case(REFUSE, [passage("pricing-motor-rate-review-draft")], Answer("7.5% [x]", ["x"]))
    assert leaked.refusal_correct is False
    assert leaked.forbidden_doc_retrieved and leaked.forbidden_content


def test_gate_fails_on_any_leak_even_with_perfect_quality():
    good = score_case(CASE, [passage("motor-excess-policy")], Answer("£95 [motor-excess-policy]", ["motor-excess-policy"]))
    leak = score_case(REFUSE, [passage("pricing-motor-rate-review-draft")], Answer.refusal())
    rows = gate(summarise([good, leak]), {"retrieval_hit_rate_at_k": 0.9, "forbidden_doc_retrieved_max": 0})
    assert {name: ok for name, _, _, ok in rows} == {"retrieval_hit_rate_at_k": True, "forbidden_doc_retrieved": False}


def test_unscored_metrics_are_skipped_by_the_gate():
    good = score_case(CASE, [passage("motor-excess-policy")], Answer("£95 [motor-excess-policy]", ["motor-excess-policy"]))
    rows = gate(summarise([good]), {"faithfulness": 0.95, "_comment": "ignored"})
    assert rows == []  # faithfulness is only scored with --judge


def test_golden_set_is_well_formed():
    import json
    from pathlib import Path

    from harbourline import load_passages

    path = Path(__file__).resolve().parents[1] / "evals" / "golden.jsonl"
    cases = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    known = {p.doc_id for p in load_passages()[0]} | {"motor-excess-policy-v2", "legacy-share-motor-excess"}
    assert len({c["id"] for c in cases}) == len(cases)
    for c in cases:
        assert c["should_refuse"] != bool(c["expected_doc_ids"]), c["id"]
        assert set(c["expected_doc_ids"]) | set(c["forbidden_doc_ids"]) <= known, c["id"]
