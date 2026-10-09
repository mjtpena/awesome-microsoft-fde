"""Command line: python -m harbourline {ask,corpus,index}."""

from __future__ import annotations

import argparse
import os
import sys

from .answering import ExtractiveAnswerer, LlmAnswerer
from .corpus import load_passages
from .retrieval import AzureSearchRetriever, LocalRetriever


def _env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        sys.exit(f"{name} is not set. Run `azd up`, then load its outputs (see README), or use --offline.")
    return value


def build_pipeline(offline: bool):
    """Return (retriever, answerer). Offline needs nothing; online needs the azd outputs."""
    if offline:
        passages, _ = load_passages()
        return LocalRetriever(passages), ExtractiveAnswerer()
    retriever = AzureSearchRetriever(_env("AZURE_SEARCH_ENDPOINT"), _env("AZURE_SEARCH_INDEX"))
    answerer = LlmAnswerer(_env("HARBOURLINE_GATEWAY_URL"), _env("HARBOURLINE_MODEL"))
    return retriever, answerer


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="harbourline", description="Harbourline policy assistant (reference)")
    sub = parser.add_subparsers(dest="command", required=True)

    ask = sub.add_parser("ask", help="ask a policy question")
    ask.add_argument("question")
    ask.add_argument("--offline", action="store_true", help="local BM25 + extractive answers, no Azure")
    ask.add_argument("--groups", default="all-staff", help="comma-separated groups of the asking user")
    ask.add_argument("-k", type=int, default=5, help="passages to retrieve")
    ask.add_argument("--show-passages", action="store_true")

    sub.add_parser("corpus", help="show which documents are indexed and which are left out, and why")
    sub.add_parser("index", help="create the Azure AI Search index and upload the passages")

    args = parser.parse_args(argv)

    if args.command == "corpus":
        passages, skipped = load_passages()
        for doc_id in sorted({p.doc_id for p in passages}):
            print(f"indexed  {doc_id}")
        for line in skipped:
            print(f"skipped  {line}")
        return 0

    if args.command == "index":
        from .indexer import build_index

        for line in build_index(_env("AZURE_SEARCH_ENDPOINT"), _env("AZURE_SEARCH_INDEX")):
            print(line)
        return 0

    retriever, answerer = build_pipeline(args.offline)
    groups = [g.strip() for g in args.groups.split(",") if g.strip()]
    passages = retriever.search(args.question, groups, k=args.k)
    if args.show_passages:
        for p in passages:
            print(f"  {p.score:7.3f}  match={p.match:.2f}  {p.id}")
    answer = answerer.answer(args.question, passages)
    print(answer.text)
    if answer.citations:
        print("Sources: " + ", ".join(answer.citations))
    return 0
