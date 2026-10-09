#!/usr/bin/env python3
"""Check the house rules in CONTRIBUTING.md that a linter can't.

Run from the repository root: python scripts/check_docs.py
Exits non-zero and prints one line per problem.

With --stale-days N, it instead lists pages whose "Last verified" or
"Facts checked" date is more than N days old. The weekly job runs this.
"""

import argparse
import re
import sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO_URL = "https://github.com/mjtpena/awesome-microsoft-fde/blob/main/"
SKIP_DIRS = {".git", "node_modules"}

problems = []


def problem(path, msg):
    problems.append(f"{path.relative_to(ROOT).as_posix()}: {msg}")


def markdown_files():
    for path in sorted(ROOT.rglob("*.md")):
        if not SKIP_DIRS.intersection(path.relative_to(ROOT).parts):
            yield path


def strip_code(text):
    """Remove fenced code blocks so headings and links inside them are ignored."""
    return re.sub(r"^(`{3,}|~{3,}).*?^\1\s*$", "", text, flags=re.S | re.M)


def slugify(heading):
    """GitHub's anchor rules: lowercase, drop punctuation, spaces become hyphens."""
    heading = re.sub(r"<[^>]+>", "", heading).strip().lower()
    heading = re.sub(r"[^\w\- ]", "", heading)
    return heading.replace(" ", "-")


def anchors(path, cache={}):
    if path not in cache:
        seen = set()
        for heading in re.findall(r"^#{1,6} (.+?)\s*#*$", strip_code(path.read_text(encoding="utf-8")), re.M):
            base = slug = slugify(heading)
            n = 1
            while slug in seen:
                slug = f"{base}-{n}"
                n += 1
            seen.add(slug)
        cache[path] = seen
    return cache[path]


def check_links(path, text):
    for target in re.findall(r"\]\(([^)\s]+)\)", strip_code(text)):
        if "/awesome-microsoft-fde" in target and not target.startswith(REPO_URL.split("/blob/")[0]):
            problem(path, f"link to this repository has the wrong owner: {target}")
        if target.startswith(REPO_URL):
            file_part, _, anchor = target[len(REPO_URL):].partition("#")
            dest = ROOT / file_part
        elif re.match(r"[a-z]+:", target):
            continue
        else:
            file_part, _, anchor = target.partition("#")
            dest = (path.parent / file_part).resolve() if file_part else path
        if not dest.exists():
            problem(path, f"broken link {target}")
        elif anchor and dest.suffix == ".md" and anchor not in anchors(dest):
            problem(path, f"missing anchor {target}")


def check_footnotes(path, text):
    text = re.sub(r"`[^`\n]*`", "", strip_code(text))
    defined = set(re.findall(r"^\[\^([\w-]+)\]:", text, re.M))
    used = set(re.findall(r"\[\^([\w-]+)\](?!:)", text))
    for name in sorted(used - defined):
        problem(path, f"footnote [^{name}] is used but not defined")
    for name in sorted(defined - used):
        problem(path, f"footnote [^{name}] is defined but never used")


def check_skill(folder, index_text):
    name = folder.name
    files = [p.name for p in folder.iterdir()]
    if files != ["SKILL.md"]:
        problem(folder, f"skill folder must hold only SKILL.md, found {files}")
    skill = folder / "SKILL.md"
    if not skill.exists():
        return
    text = skill.read_text(encoding="utf-8")

    front = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not front:
        problem(skill, "missing YAML frontmatter")
        return
    fields = dict(re.findall(r"^(\w+): (.*)$", front.group(1), re.M))
    if fields.get("name") != name:
        problem(skill, f"frontmatter name {fields.get('name')!r} doesn't match folder {name!r}")
    description = fields.get("description", "")
    if not (description.startswith('"') and description.endswith('"')):
        problem(skill, "description must be a quoted string")

    if not name.startswith("scenario-"):
        h2s = re.findall(r"^## (.+)$", strip_code(text), re.M)
        if not h2s or h2s[-1] != "Template":
            problem(skill, "the last section must be '## Template'")
        if "````markdown" not in text:
            problem(skill, "the template must sit in a ````markdown fence")

    for target in re.findall(r"\]\((\.\./\.\./[^)]+|\.\./(?:\.\./)?(?:docs|README)[^)]*)\)", text):
        problem(skill, f"link leaves skills/ with a relative path; use {REPO_URL}... ({target})")

    # Skills get copied into customer repositories and never updated, so dated
    # facts and prices belong in the technical reference. Link targets are exempt.
    prose = re.sub(r"\]\([^)]*\)|https?://\S+", "](...)", text)
    for match in re.finditer(r"US\$|\$\d|\b20\d\d\b", prose):
        line = prose[: match.start()].count("\n") + 1
        problem(skill, f"line {line}: date or price in a skill; link to the technical reference instead")

    if f"({name}/SKILL.md)" not in index_text:
        problem(skill, "not listed in skills/README.md")


VERIFIED_DATE = re.compile(r"(?:\*\*Last verified:\*\*|\*Facts checked on) (\d{1,2} \w+ \d{4})")


def check_freshness(max_age_days, today):
    """List pages whose verification date is older than max_age_days."""
    stale = []
    for path in [ROOT / "README.md", *sorted((ROOT / "docs").rglob("*.md"))]:
        match = VERIFIED_DATE.search(path.read_text(encoding="utf-8"))
        if not match:
            continue
        checked = datetime.strptime(match.group(1), "%d %B %Y").date()
        age = (today - checked).days
        if age > max_age_days:
            stale.append(f"{path.relative_to(ROOT).as_posix()}: last verified {match.group(1)} ({age} days ago)")
    return stale


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stale-days", type=int, metavar="N",
                        help="only list pages whose verification date is more than N days old")
    args = parser.parse_args()
    if args.stale_days is not None:
        stale = check_freshness(args.stale_days, date.today())
        for line in stale:
            print(line)
        print(f"{len(stale)} page(s) need re-verifying" if stale else "All pages verified recently.")
        return 1 if stale else 0

    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        check_links(path, text)
        check_footnotes(path, text)

    for path in sorted((ROOT / "docs").rglob("*.md")):
        if path.name != "README.md" and "**Last verified:**" not in path.read_text(encoding="utf-8"):
            problem(path, "missing a '**Last verified:**' date")

    index_text = (ROOT / "skills" / "README.md").read_text(encoding="utf-8")
    for folder in sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir()):
        check_skill(folder, index_text)

    for line in problems:
        print(line)
    print(f"{len(problems)} problem(s)" if problems else "All checks passed.")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
