"""Retrievers: find the passages a given user is allowed to see.

Permission trimming happens HERE, in retrieval, not in the prompt. A passage the
user can't open never reaches the model, so no instruction or jailbreak can leak it.
"""

from __future__ import annotations

import math
import re
from collections import Counter
from dataclasses import replace
from typing import Protocol, Sequence

from .corpus import Passage

_STOPWORDS = frozenset(
    "a an and are as at be by can do does for from has have how i if in is it its "
    "me my of on or our should that the their them there this to us was we what "
    "when where which who will with you your".split()
)
_GROUP_NAME = re.compile(r"^[a-z0-9-]+$")


def tokenize(text: str) -> list[str]:
    tokens = []
    for word in re.findall(r"[a-z0-9]+", text.lower()):
        if word in _STOPWORDS:
            continue
        if len(word) > 3 and word.endswith("s") and not word.endswith("ss"):
            word = word[:-1]  # crude plural folding: claims -> claim
        tokens.append(word)
    return tokens


def coverage(question: str, text: str) -> float:
    """Unweighted share of the question's terms that appear in the text."""
    terms = set(tokenize(question))
    return len(terms & set(tokenize(text))) / len(terms) if terms else 0.0


class Retriever(Protocol):
    def search(self, question: str, groups: Sequence[str], k: int = 5) -> list[Passage]:
        """Return up to k passages that the user's groups may see, best first."""
        ...


class LocalRetriever:
    """BM25 over in-memory passages. Offline, deterministic, no dependencies."""

    def __init__(self, passages: Sequence[Passage], k1: float = 1.5, b: float = 0.75):
        self._passages = list(passages)
        self._docs = [Counter(tokenize(f"{p.title} {p.section} {p.content}")) for p in self._passages]
        self._lengths = [sum(d.values()) for d in self._docs]
        self._avg_len = sum(self._lengths) / max(len(self._lengths), 1)
        self._df = Counter(term for d in self._docs for term in d)
        self._k1, self._b = k1, b

    def _idf(self, term: str) -> float:
        n, df = len(self._docs), self._df.get(term, 0)
        return math.log((n - df + 0.5) / (df + 0.5) + 1)

    def search(self, question: str, groups: Sequence[str], k: int = 5) -> list[Passage]:
        allowed = set(groups)
        terms = set(tokenize(question))
        total_idf = sum(self._idf(t) for t in terms) or 1.0
        results = []
        for passage, doc, length in zip(self._passages, self._docs, self._lengths):
            if not allowed.intersection(passage.groups):
                continue  # permission trimming: the user can't see this passage
            score = 0.0
            for term in terms & doc.keys():
                tf = doc[term]
                norm = tf + self._k1 * (1 - self._b + self._b * length / self._avg_len)
                score += self._idf(term) * tf * (self._k1 + 1) / norm
            if score > 0:
                # IDF-weighted, so a rare unmatched word ("pet", "travel") pulls the match down hard.
                match = sum(self._idf(t) for t in terms & doc.keys()) / total_idf
                results.append(replace(passage, score=round(score, 4), match=round(match, 4)))
        results.sort(key=lambda p: (-p.score, p.id))
        return results[:k]


class AzureSearchRetriever:
    """Azure AI Search with keyless Entra auth. Trims by a `groups` field filter.

    The filter here is the classic security-filter pattern. A Foundry IQ knowledge
    base with permission sync trims on the user's real document ACLs instead; this
    reference keeps the simpler pattern so it runs anywhere.
    """

    def __init__(self, endpoint: str, index_name: str, credential=None):
        from azure.identity import DefaultAzureCredential
        from azure.search.documents import SearchClient

        self._client = SearchClient(endpoint, index_name, credential or DefaultAzureCredential())

    @staticmethod
    def group_filter(groups: Sequence[str]) -> str:
        for g in groups:
            if not _GROUP_NAME.match(g):
                raise ValueError(f"invalid group name {g!r}")  # stops OData filter injection
        return f"groups/any(g: search.in(g, '{','.join(groups)}', ','))"

    def search(self, question: str, groups: Sequence[str], k: int = 5) -> list[Passage]:
        results = self._client.search(
            search_text=question,
            filter=self.group_filter(groups),
            top=k,
            select=["id", "doc_id", "title", "section", "content", "groups"],
        )
        return [
            Passage(
                id=r["id"],
                doc_id=r["doc_id"],
                title=r["title"],
                section=r["section"],
                content=r["content"],
                groups=tuple(r["groups"]),
                score=round(r["@search.score"], 4),
                match=round(coverage(question, f'{r["title"]} {r["section"]} {r["content"]}'), 4),
            )
            for r in results
        ]
