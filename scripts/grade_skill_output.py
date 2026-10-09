#!/usr/bin/env python3
"""Grade a document an agent (or a person) produced by following a skill.

    python scripts/grade_skill_output.py <skill-name> <output.md>
    python scripts/grade_skill_output.py --examples

The first form grades one output. The second grades every worked example
listed in skill-evals/cases.json, which is what CI runs: the examples are the
reference answers, so they must pass their own skill's checks.

The checks are the ones a reviewer would otherwise do by eye:

1. Every required section of the skill's template is present. Sections whose
   heading contains "Scenario" or "add-on" are optional, because the skills
   tell readers to delete what doesn't apply. cases.json can mark more.
2. No template placeholders are left, such as "<Agent / System name>".
3. The case's must-include phrases appear (the facts the brief gave).

Judgement (is the threat model any good?) still needs a person or an LLM
judge; see skill-evals/README.md.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CASES = ROOT / "skill-evals" / "cases.json"
OPTIONAL = re.compile(r"scenario|add-on", re.I)
# Placeholders look like <Agent / System name> or <what changed>: angle
# brackets around words, but not HTML comments, tags or autolinks.
PLACEHOLDER = re.compile(r"<(?![!/a-z]+[ >]|https?:)[A-Z][^<>\n]{1,60}>")


def template_of(skill):
    text = (ROOT / "skills" / skill / "SKILL.md").read_text(encoding="utf-8")
    blocks = re.findall(r"^````markdown\n(.*?)^````\s*$", text, re.S | re.M)
    if not blocks:
        sys.exit(f"skills/{skill}/SKILL.md has no ````markdown template")
    return "\n".join(blocks)


def headings(text, level):
    text = re.sub(r"^```.*?^```\s*$", "", text, flags=re.S | re.M)
    return re.findall(rf"^{'#' * level} (.+?)\s*$", text, re.M)


def normalise(heading):
    """Compare headings loosely: drop numbering, placeholders, emoji and case."""
    heading = re.sub(r"<[^>]*>|[^\w\s]", " ", heading.lower())
    heading = re.sub(r"^\s*\d+\s+", "", heading)
    return " ".join(heading.split())


def grade(skill, output_path, case=None):
    case = case or {}
    output = output_path.read_text(encoding="utf-8")
    found = {normalise(h) for level in (2, 3) for h in headings(output, level)}
    optional = {normalise(h) for h in case.get("optional_sections", [])}
    failures = []

    for heading in headings(template_of(skill), 2):
        key = normalise(heading)
        if OPTIONAL.search(heading) or key in optional or not key:
            continue
        if not any(key in f or f in key for f in found if f):
            failures.append(f"missing section '{heading}'")

    for match in PLACEHOLDER.finditer(re.sub(r"`[^`\n]*`", "", output)):
        failures.append(f"unfilled placeholder {match.group(0)}")

    for phrase in case.get("must_include", []):
        if phrase.lower() not in output.lower():
            failures.append(f"missing expected content '{phrase}'")

    return failures


def main(argv):
    if argv == ["--examples"]:
        cases = json.loads(CASES.read_text(encoding="utf-8"))["cases"]
        total = 0
        for case in cases:
            path = ROOT / case["reference"]
            if not path.exists():
                print(f"FAIL {case['skill']}: reference {case['reference']} doesn't exist")
                total += 1
                continue
            failures = grade(case["skill"], path, case)
            total += len(failures)
            print(f"{'FAIL' if failures else 'pass'} {case['skill']} ({case['reference']})")
            for failure in failures:
                print(f"     {failure}")
        print(f"{total} problem(s)" if total else "All examples pass their skill checks.")
        return 1 if total else 0

    if len(argv) != 2:
        print(__doc__)
        return 2
    skill, output = argv
    cases = {c["skill"]: c for c in json.loads(CASES.read_text(encoding="utf-8"))["cases"]}
    failures = grade(skill, Path(output), cases.get(skill))
    for failure in failures:
        print(failure)
    print(f"{len(failures)} problem(s)" if failures else "Pass.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
