# Contributing

Thanks for helping keep this roadmap accurate. By taking part you agree to the [code of conduct](CODE_OF_CONDUCT.md). Found a fact that's out of date? [Open a stale-fact issue](https://github.com/mjtpena/awesome-microsoft-fde/issues/new?template=stale-fact.yml). Security concerns go through [SECURITY.md](SECURITY.md).

## Where things go

- **README.md** is for beginners. Use plain language, spell out every acronym the first time you use it, and add new terms to the glossary. Cite sources as footnotes (`[^name]`) rather than inline links, and keep it short: if a detail changes monthly, it belongs in `docs/`.
- **docs/** holds the detailed, fully sourced reference material. Inline links and status labels are fine there.
- **docs/pillars/** pages keep the same layout: in plain words, our stance, what you need to know, on Microsoft, mistakes, prove it, interview questions, skills.
- **skills/** holds one folder per skill, named in lowercase with hyphens. Each folder holds one self-contained `SKILL.md` and nothing else, so the file works in any agent or chat tool.
  - `SKILL.md` starts with [Agent Skills](https://agentskills.io/) frontmatter: `name` (must match the folder name) and a quoted `description` saying what the skill does and when to use it. The body follows the same layout as the existing skills: the step and pillar line, when to use, rules, steps, scenarios, template. Keep it plain Markdown with no tool-specific syntax.
  - The template goes last, under `## Template`, inside a ` ````markdown ` fence (four backticks, so Mermaid blocks inside it still work). Only the document to fill in goes in the fence; guidance goes above it. Scenario-specific content goes in a clearly labelled section so readers can delete what doesn't apply.
  - Add the new skill to the tables in [skills/README.md](skills/README.md) and to the relevant scenario packs.
  - Add a worked example in [examples/knowledge-assistant/](examples/README.md) that agrees with the fact sheet, and a case for it in [skill-evals/cases.json](skill-evals/cases.json). When you change a template, update its example in the same pull request.
  - **Links:** people copy skill folders into their agent's skills directory, so links that leave the `skills/` folder (to `docs/` or the README files) must be absolute `https://github.com/mjtpena/awesome-microsoft-fde/blob/main/...` URLs. Links between sibling skills (`../adr/SKILL.md`) stay relative.
  - **No prices or dates anywhere in a skill.** Skill folders get copied into agents' skill directories and customers' repositories, and are never updated. Name the meter, licence or requirement and link to the dated fact in `docs/microsoft-technical-reference.md`. `scripts/check_docs.py` enforces this.
  - **Internal notes stay out of the customer's repository.** Anything that assesses named people or carries feedback to the product team goes in a separate template block labelled "Internal" and is written to the team's own workspace.
  - Scenario packs use the layout: when to use, steps, our default design, skill kit, discovery questions, top risks, on Microsoft, practise.
  - **Keep each piece of scenario content in one place.** What goes into a filled-in document lives in that skill's template, under "Scenario add-ons"; the pack's skill kit names the add-on to fill and doesn't restate it. Discovery questions live only in the packs; the `discovery-interview` template tells readers to paste them in.
- **reference/** holds runnable code. Keep it small, tested and honest about what it leaves out; its offline evaluation gate must pass in CI.
- **Opinions are welcome.** Mark them 💬 (or put them under "Our stance" / "Our take") and argue for them.

## House rules

1. **Cite every factual claim.** Prefer Microsoft Learn, official Microsoft blogs, or Microsoft GitHub repos. Third-party sources are acceptable only when named as such. Job postings and other pages that disappear: add an `[archived](https://web.archive.org/...)` link next to the source, but only after checking that the snapshot shows the text you cite (many job boards archive as an empty page).
2. **Label status.** Use ✅ GA, 🧪 Preview, 🔜 Announced, ⚠️ Watch out.
3. **Mark opinion, and back it where you can.** Practitioner guidance gets 💬. If a source points the same way, cite it next to the opinion. If it's an estimate from experience, say so ("in our experience", "roughly") rather than giving a number that looks measured.
4. **Date-stamp changes.** Update the "Facts checked" date in the README or the "Last verified" date in the relevant `docs/` page (every page under `docs/`, pillar pages included, carries one) when you re-verify a section.
5. **No marketing copy.** Technical, specific, actionable.
6. **Log template changes.** Add a line under "Unreleased" in [CHANGELOG.md](CHANGELOG.md) for anything a reader would want to know before updating a copied skill. To release, rename "Unreleased" to the version and push a `vX.Y.Z` tag; the release workflow attaches `skills.zip`.

## PR checklist

- [ ] Links resolve
- [ ] Status labels updated
- [ ] No unsourced numbers, dates, or prices

## Automated checks

Every pull request runs these checks ([`.github/workflows/docs.yml`](.github/workflows/docs.yml)). Run them locally before you push:

| Check | Command | What it catches |
|---|---|---|
| House rules | `python scripts/check_docs.py` | Broken relative links and anchors, unused or missing footnotes, skill frontmatter and layout, skills missing from the index |
| Worked examples | `python scripts/grade_skill_output.py --examples` | An example that no longer follows its skill's template, or that lost a fact from the brief |
| Reference implementation | see [`reference/knowledge-assistant/README.md`](reference/knowledge-assistant/README.md) | Failing unit tests, or an evaluation score below the bar (runs only when `reference/` changes) |
| Markdown lint | `npx markdownlint-cli2 "**/*.md"` | Formatting slips; see [`.markdownlint-cli2.jsonc`](.markdownlint-cli2.jsonc) for the rules we switch off |
| External links | `lychee --config lychee.toml .` | Dead source links |

A scheduled job also checks external links every Monday and opens an issue labelled `stale-fact` when a source has gone, or when a page hasn't been re-verified for 90 days (`python scripts/check_docs.py --stale-days 90`).
