"""Load policy documents and decide which passages may be indexed.

Two rules live here because they were both learned the hard way:

* ADR-003 (amended in week 6): index only documents whose status is
  ``current``. A document with *no* status is held for the policy owner's
  review, not indexed. The week-6 incident was an old file-share copy with no
  status that the original rule treated as current because it sat in the
  ``published`` folder.
* Indirect prompt injection: passages that look like instructions to an AI are
  dropped at ingestion. This is a cheap screen, not a defence you can rely on;
  production adds a content-safety service on the gateway (see README).
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

DEFAULT_DATA_DIR = Path(__file__).resolve().parents[2] / "sample-data"

_META = re.compile(r"^(Status|Groups|Version):[ \t]*(.+?)[ \t]*$", re.M)
_H1 = re.compile(r"^# (.+)$", re.M)
_H2 = re.compile(r"^## (.+)$", re.M)
_INJECTION = re.compile(
    r"ignore (all |any |your |the )?(previous |prior )?instructions"
    r"|note (for|to) (ai|the) assistants?"
    r"|you are now in .{0,20} mode",
    re.I,
)


@dataclass(frozen=True)
class Passage:
    """One section of one document: the unit that is retrieved and cited."""

    id: str  # unique and safe as an Azure AI Search key
    doc_id: str  # the file name without .md; what citations point to
    title: str
    section: str
    content: str
    groups: tuple[str, ...]
    score: float = 0.0
    match: float = 0.0  # share of the question's terms found here, 0 to 1


@dataclass
class Document:
    doc_id: str
    title: str
    status: str | None
    groups: tuple[str, ...]
    sections: list[tuple[str, str]] = field(default_factory=list)


def parse_document(path: Path) -> Document:
    text = path.read_text(encoding="utf-8")
    title_match = _H1.search(text)
    title = title_match.group(1).strip() if title_match else path.stem
    parts = _H2.split(text)
    meta = dict(_META.findall(parts[0]))
    groups = tuple(g.strip() for g in meta.get("Groups", "").split(",") if g.strip())
    sections = [(parts[i].strip(), parts[i + 1].strip()) for i in range(1, len(parts) - 1, 2)]
    status = meta.get("Status", "").strip().lower() or None
    return Document(path.stem, title, status, groups, sections)


def index_decision(doc: Document) -> str | None:
    """Return why a document must NOT be indexed, or None if it may be."""
    if doc.status is None:
        return "no Status line: held for the policy owner's review, not indexed (ADR-003 amendment)"
    if doc.status != "current":
        return f"status is {doc.status!r}, not 'current'"
    if not doc.groups:
        return "no Groups line: nobody would be allowed to see it"
    return None


def looks_like_injection(text: str) -> bool:
    return bool(_INJECTION.search(text))


def load_passages(data_dir: Path = DEFAULT_DATA_DIR) -> tuple[list[Passage], list[str]]:
    """Return the passages that may be indexed, and a log of what was left out and why."""
    passages: list[Passage] = []
    skipped: list[str] = []
    for path in sorted(data_dir.glob("*.md")):
        if path.name.lower() == "readme.md":
            continue
        doc = parse_document(path)
        reason = index_decision(doc)
        if reason:
            skipped.append(f"{doc.doc_id}: {reason}")
            continue
        for section, content in doc.sections:
            if looks_like_injection(content):
                skipped.append(f"{doc.doc_id} / {section}: looks like an instruction to an AI, dropped")
                continue
            slug = re.sub(r"[^a-z0-9]+", "-", section.lower()).strip("-")
            passages.append(Passage(f"{doc.doc_id}--{slug}", doc.doc_id, doc.title, section, content, doc.groups))
    return passages, skipped
