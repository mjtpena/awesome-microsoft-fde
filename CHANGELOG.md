# Changelog

What changed in each release, most recent first. Releases are tagged `vMAJOR.MINOR.PATCH` and each one attaches a `skills.zip` you can install from.

People copy skill templates into customer repositories, so check this page when you update a copy:

- **Major:** a skill's template changed in a way that makes an older filled-in copy inconsistent (a section removed or renamed), or a skill was renamed or removed.
- **Minor:** a new skill, scenario pack or example; new sections or rows in a template.
- **Patch:** wording, fixes, links and re-verified facts.

## Unreleased

### Changed

- **README:** opens with what the kit contains and a quickstart, and a new Part 3, "The kit", covers the skills and scenario packs, the worked Harbourline engagement, the reference implementation and how the kit is tested, with diagrams and charts. The interview scenarios are now section 16. Templates unchanged.
- **CI:** the workflows use the Node.js 24 versions of their actions (`actions/checkout@v6`, `actions/setup-python@v6`, `actions/upload-artifact@v6`, `DavidAnson/markdownlint-cli2-action@v24`, `peter-evans/create-issue-from-file@v6`), which clears the Node.js 20 deprecation warning on every job.
- **Markdown lint:** repeated headings are allowed when they sit under different parents (MD024 `siblings_only`), so each release section in this changelog can have its own "Added" and "Changed".

## 1.0.0

The first versioned release: 20 skills, five scenario packs, a worked example for every skill and a runnable reference implementation.

### Added

- Six skills for the moments that decide engagements: `engagement-kickoff`, `scope-reset`, `responsible-ai-impact-assessment`, `red-team`, `incident-review` and `field-feedback` (internal), with rows in every scenario pack.
- A worked example for every skill: one fictional engagement (Harbourline Insurance) from kickoff to handover, with a shared fact sheet in `examples/README.md` that every example agrees with.
- A reference implementation in `reference/knowledge-assistant/`: a small knowledge assistant that runs offline, an evaluation gate that scores retrieval and answers separately and runs in CI, and Bicep for the Azure resources.
- Skill evaluations: `scripts/grade_skill_output.py` checks a skill's output against its template, and CI grades every worked example with it. `skill-evals/README.md` explains how to run a skill through your own agent and judge the result.
- Two docs pages: the field guide (what actually goes wrong) and From FDE to principal (how the job changes with seniority).
- Technical reference: Red teaming and Responsible AI subsections. PyRIT's repository has moved to `microsoft/PyRIT`.
- A weekly freshness check that opens an issue when a page hasn't been re-verified for 90 days (`python scripts/check_docs.py --stale-days 90`).
- A field survey issue form, to replace the guide's estimate of how an FDE's week splits with data.
- Automated checks on every pull request: links and anchors, footnotes, skill structure, Markdown lint and external links, plus a weekly dead-link report.
- Outline answers to the interview case studies and answers to the rapid-fire questions.
- A worked example: a filled-in threat model for a fictional knowledge assistant.
- Versioned releases, each with a `skills.zip`, and this changelog.
- One-line install commands for the skills.
- Issue templates for stale facts and skill proposals, a code of conduct and a security policy.

### Changed

- **`threat-model`, `eval-plan`, `runbook`, `weekly-status`:** link to the new `red-team`, `incident-review` and `field-feedback` skills. Templates unchanged.
- **`discovery-interview`:** the "Scenario add-ons" section of the template is now "Scenario questions"; paste the questions from your scenario pack. The packs are the only copy.
- **`agent-instructions`:** the list of files each coding assistant reads moved to the technical reference.
- Pillar pages carry a "Last verified" date, and skills no longer contain dates or prices.

## Before versioning (up to October 2026)

The guide, the six pillar deep dives, 14 skills and five scenario packs, built in the commits up to `cbd0b06`. See the [commit history](https://github.com/mjtpena/awesome-microsoft-fde/commits/main).
