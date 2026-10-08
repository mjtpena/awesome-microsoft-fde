---
name: copilot-instructions
description: "Create a .github/copilot-instructions.md for a customer repository that encodes the customer's rules first, then engagement conventions for infrastructure, agents, data and the scenario. Use at the start of the build phase when AI coding assistants are allowed in the repository."
---

# Copilot Instructions

> Part of the [skills](../README.md) in the [Awesome Microsoft FDE](../../README.md) guide. **Step:** 4 Build · **Pillar:** [1 Software engineering](../../docs/pillars/01-software-engineering.md)

Rules for AI coding assistants (such as GitHub Copilot) working in the customer's repository.

## When to use

- At the start of the build, once the [access request](../access-request/SKILL.md) confirms AI coding assistants are allowed.
- When a new ADR changes how code should be written.

## Rules

- The customer's conventions beat our preferences: keep the "Customer rules" section first.
- Only include rules you'll actually enforce in review.
- Delete scenario sections that don't apply.

## Steps

1. Write the [template](#template) to `.github/copilot-instructions.md` in the customer's repository.
2. Fill "Customer rules" from the repository's existing linting config, contribution guide and the access request.
3. Keep the scenario section for this engagement; delete the others.
4. Open it as a pull request so the customer's reviewers agree the rules.

Write everything into the customer's repository, not your own drive. Everything you write belongs to the customer. Delete sections that don't apply: a short, filled-in document beats a long, empty one.

## Scenarios

Used in every scenario. Each [scenario pack](../README.md#scenario-packs) says what to add.

## Template

Write everything inside the block below to the file named in the steps, then fill it in.

````markdown
# Copilot Instructions

## Customer rules (fill in first)

- Language and framework: <e.g. Python 3.12, .NET 9>
- Style and linting: <tooling and config>
- Branching and review: <who approves, required checks>
- Forbidden: <e.g. no new dependencies without approval>

## How we work

- Follow Research → Plan → Implement → Review. No implementation without an approved plan in `.copilot-tracking/` (HVE Core convention).
- Small pull requests. Each one says what changed, how it was tested and which ADR it relates to.
- Never commit secrets, keys, connection strings or customer data. Use managed identities.
- Mark any dependency on a preview feature with `# PREVIEW:` and a link to its documentation.

## Infrastructure

- Infrastructure-as-code only: Bicep or Terraform using Azure Verified Modules. No portal-only resources.
- Reference built-in roles by ID, not name, in code (Foundry roles were renamed from "Azure AI *" to "Foundry *").
- Use the Azure MCP Server for Azure context. The Copilot cloud agent gets Reader only unless an ADR says otherwise; note that it runs MCP tools without asking for approval.

## Agents and AI

- Microsoft Agent Framework (Python or .NET) for code-based agents.
- Every tool has one purpose, typed and validated inputs, and clear error messages. Any tool that writes requires human approval.
- Emit OpenTelemetry traces for every request, model call and tool call.
- Don't change prompts or instructions without running the evaluation set (`eval-plan.md`) and recording the result.

## Data

- Fabric deployments use `fabric-cicd` with an explicit `token_credential`.
- Never read from or write to production data stores from local development.

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
