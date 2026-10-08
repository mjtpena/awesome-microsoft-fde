---
name: agent-instructions
description: "Create or extend the instructions file that AI coding assistants read in a customer repository (AGENTS.md, or the tool's own file such as .github/copilot-instructions.md): the customer's rules first, decisions from ADRs, then engagement conventions the customer has agreed to. Use at the start of the build phase when AI coding assistants are allowed in the repository."
---

# Agent Instructions

> Part of the [skills](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/skills/README.md) in the [Awesome Microsoft FDE](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/README.md) guide. **Step:** 4 Build · **Pillar:** [1 Software engineering](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/docs/pillars/01-software-engineering.md)

Rules for AI coding assistants (such as GitHub Copilot, Claude Code or Codex) working in the customer's repository. The customer's rules come first. Our conventions are proposals they can reject.

## When to use

- At the start of the build, once the [access request](../access-request/SKILL.md) confirms AI coding assistants are allowed.
- When a new ADR changes how code should be written.

## Rules

- **The customer's conventions beat our preferences.** Keep "Customer rules" first. Every engagement convention is a proposal: keep it only if the customer agrees in review, and delete it otherwise.
- **Technology choices come from ADRs, not from this file.** The file records what an ADR decided; it doesn't make the decision.
- **Extend, don't replace.** If the repository already has an instructions file, add to it.
- Only include rules you'll actually enforce in review.
- Delete scenario sections that don't apply.

## Steps

1. Look for existing instructions files: `AGENTS.md`, `.github/copilot-instructions.md`, `.github/instructions/`, `CLAUDE.md`. **If one exists, it's the main file:** add the template's sections to it. Only create `AGENTS.md` when there's none; several assistants read it.
2. Ask which AI coding assistants the customer allows (from the access request) and check which files each one reads in its current documentation. Keep one set of rules: every other tool's file is a one-line pointer or import to the main file, never a second copy. Facts as of October 2026:
   - GitHub Copilot's cloud agent reads `AGENTS.md`, `.github/copilot-instructions.md`, `.github/instructions/**.instructions.md` and `CLAUDE.md` ([GitHub changelog](https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions)).
   - Claude Code reads `CLAUDE.md`, and reads `AGENTS.md` only when there's no `CLAUDE.md`. If both are needed, put `@AGENTS.md` (or `@` and the path to the main file) in `CLAUDE.md` to import it ([Claude Code docs](https://code.claude.com/docs/en/memory)).
3. Fill "Customer rules" from the repository's existing linting config, contribution guide, CI checks and the access request.
4. Fill "Decisions from ADRs" with a link to each accepted ADR that affects code.
5. Keep only the engagement conventions you'll propose, and the scenario section for this engagement.
6. Open it as a pull request. Delete every proposal the customer's reviewers don't accept, then record the pull request in the file.

Write everything into the customer's repository, not your own drive. Everything you write belongs to the customer. Delete sections that don't apply: a short, filled-in document beats a long, empty one.

## On Microsoft 💬

Conventions worth proposing when the ADRs land on the Microsoft stack. Check each against the [technical reference](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/docs/microsoft-technical-reference.md) first, because names and defaults change:

- Code-based agents on Microsoft Agent Framework; infrastructure in Bicep or Terraform using Azure Verified Modules.
- Foundry built-in roles were renamed from "Azure AI \*" to "Foundry \*" with the same IDs, which is why code should use role IDs.
- Azure MCP Server for Azure context. The GitHub Copilot cloud agent's Azure identity is Reader by default, and it runs MCP tools without asking for approval.
- Fabric deployments with `fabric-cicd`, passing an explicit `token_credential`.

## Scenarios

Used in every scenario. Each [scenario pack](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/skills/README.md#scenario-packs) says what to add.

## Template

Write everything inside the block below to the file named in the steps, then fill it in.

````markdown
# Instructions for AI Coding Assistants

These rules apply to every AI coding assistant working in this repository. Customer rules take precedence over everything below.

## Customer rules (fill in first)

- Language and framework: <e.g. Python 3.12, .NET 9>
- Style and linting: <tooling and config>
- Branching and review: <who approves, required checks>
- Forbidden: <e.g. no new dependencies without approval>

## Decisions from ADRs

| Area | Decision | ADR |
|---|---|---|
| Agent framework | | `docs/adr/ADR-00X-...` |
| Infrastructure-as-code tool | | |
| Identity model | | |
| Data layer | | |

## Engagement conventions (agreed in pull request <#N>)

<!-- Proposals. Keep only what the customer's reviewers accept. -->

- Plan before implementing: for any change touching more than a few files, write a short plan and link it in the pull request.
  <!-- If the team adopts HVE Core, use its Research → Plan → Implement → Review flow and `.copilot-tracking/` folder. -->
- Small pull requests. Each one says what changed, how it was tested and which ADR it relates to.
- Never commit secrets, keys, connection strings or customer data. Use managed identities.
- Mark any dependency on a preview feature with a `PREVIEW:` comment and a link to its documentation.
- Infrastructure-as-code only, using the tool chosen in the ADR. No resources created by hand in the portal.
- Reference built-in roles by ID, not name, in code: role names change.
- Every agent tool has one purpose, typed and validated inputs, and clear error messages. Any tool that writes requires human approval.
- Emit OpenTelemetry traces for every request, model call and tool call.
- Don't change prompts or instructions without running the evaluation set (`docs/quality/eval-plan.md`) and recording the result.
- Never read from or write to production data stores from local development.
- AI coding assistants with cloud access get read-only roles unless an ADR says otherwise. Check whether the assistant runs tools without asking for approval.

## Scenario sections

### Knowledge assistant
- Retrieval code must pass the user's identity through so results are permission-trimmed. Add a test with a low-privilege user.

### Action agent
- Every write action logs who requested it, what was approved and the result. Provide a dry-run mode.

### Data agent
- Generated queries are read-only, time-limited and row-limited. Query only the curated (gold) layer.

### Regulated / disconnected
- No calls to public endpoints. All packages come from the approved internal feed.
````
