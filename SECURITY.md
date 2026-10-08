# Security Policy

This repository is documentation and agent skills, not software you run as a service. Security issues here usually take one of these forms:

- **Unsafe guidance:** a skill, template or recommendation that would lead an engineer or an AI agent to build something insecure, such as over-broad permissions or a missing approval step.
- **Unsafe skill content:** text in a `SKILL.md` that could make an agent act harmfully when it follows the file.
- **The repository's own automation:** the scripts and GitHub Actions workflows under `scripts/` and `.github/`.

## Reporting

Report these privately through GitHub's [private vulnerability reporting](https://github.com/mjtpena/awesome-microsoft-fde/security/advisories/new) rather than in a public issue. Include the file, the section, and what could go wrong. If that form isn't available, contact the maintainer privately through their [GitHub profile](https://github.com/mjtpena).

You'll get an acknowledgement within a week. Fixes ship in a patch release, and the [changelog](CHANGELOG.md) says which skills changed, so people who copied them know to update.

Ordinary mistakes in guidance that aren't a security risk can go in a normal issue.

## Microsoft product vulnerabilities

This project isn't affiliated with Microsoft. Report vulnerabilities in Microsoft products to the [Microsoft Security Response Center](https://msrc.microsoft.com/report).
