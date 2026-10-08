# Changelog

What changed in each release, most recent first. Releases are tagged `vMAJOR.MINOR.PATCH` and each one attaches a `skills.zip` you can install from.

People copy skill templates into customer repositories, so check this page when you update a copy:

- **Major:** a skill's template changed in a way that makes an older filled-in copy inconsistent (a section removed or renamed), or a skill was renamed or removed.
- **Minor:** a new skill, scenario pack or example; new sections or rows in a template.
- **Patch:** wording, fixes, links and re-verified facts.

## Unreleased

### Added

- Automated checks on every pull request: links and anchors, footnotes, skill structure, Markdown lint and external links, plus a weekly dead-link report.
- Outline answers to the interview case studies and answers to the rapid-fire questions.
- A worked example: a filled-in threat model for a fictional knowledge assistant.
- Versioned releases, each with a `skills.zip`, and this changelog.
- One-line install commands for the skills.

### Changed

- **`discovery-interview`:** the "Scenario add-ons" section of the template is now "Scenario questions"; paste the questions from your scenario pack. The packs are the only copy.
- **`agent-instructions`:** the list of files each coding assistant reads moved to the technical reference.
- Pillar pages carry a "Last verified" date, and skills no longer contain dates or prices.

## Before versioning (up to October 2026)

The guide, the six pillar deep dives, 14 skills and five scenario packs, built in the commits up to `cbd0b06`. See the [commit history](https://github.com/mjtpena/awesome-microsoft-fde/commits/main).
