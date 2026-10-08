---
name: scenario-data-agent
description: "Plan a data and analytics agent engagement that answers plain-English questions over business data: default design, which skills to use and what to add, discovery questions, top risks and the Microsoft services. Use when users want to query sales, finance or operations data."
---

# Scenario Pack: Data and Analytics Agent

> Part of the [skills](../README.md) in the [Awesome Microsoft FDE](../../README.md) guide. **The engagement:** "Let people ask our sales, finance or operations data questions in plain English." **Hardest pillar:** [2 Data](../../docs/pillars/02-data.md).

## Our default design 💬

```mermaid
flowchart LR
    SRC["Operational systems<br/>ERP · CRM · databases"] --> B["Raw layer"] --> S["Clean layer"] --> G["Curated layer<br/>star schema · agreed metrics"]
    U["Business user"] --> AG["Data agent"]
    AG -- "read-only, limited queries" --> G
    AG -. "answer + the query used" .-> U
```

- **The agent queries only the curated layer.** Never point it at raw tables with cryptic column names.
- **Agree metric definitions before building.** "Revenue" means three different things in most companies.
- **Show the query or calculation with every answer,** so users can check it.
- **Match a trusted report.** If the agent's number differs from the finance report, users will trust neither.

## Skill kit

| Skill | What to add for this scenario |
|---|---|
| [`discovery-interview`](../discovery-interview/SKILL.md) | Which reports people trust; which metric definitions are disputed |
| [`data-audit`](../data-audit/SKILL.md) | **Critical.** Fill the business-data section: questions → tables → trusted report → definition owner |
| [`adr`](../adr/SKILL.md) | Data layer the agent queries; metric definitions; query limits |
| [`eval-plan`](../eval-plan/SKILL.md) | Numbers compared to the trusted report; ambiguous questions that need clarification |
| [`cost-model`](../cost-model/SKILL.md) | Query compute on the data platform |
| [`go-live-readiness`](../go-live-readiness/SKILL.md) | Core + data-agent add-ons |

## Discovery questions

1. What are the 20 questions people ask analysts most often?
2. Which report is the source of truth for each metric?
3. Which definitions are disputed, and who settles disputes?
4. Who may see which rows (for example, by region or business unit)?
5. How fresh must the data be: real time, daily or monthly?

## Top risks

| Risk | What we do |
|---|---|
| Plausible but wrong numbers | Curated layer only; golden set checked against trusted reports; show the query |
| Ambiguous questions answered confidently | Teach the agent to ask which definition the user means |
| Row-level permissions bypassed | Agent runs with the user's identity; test with restricted users |
| Expensive queries | Read-only, time-limited and row-limited queries; capacity monitoring |

## On Microsoft

| Need | Our default | Source |
|---|---|---|
| Getting data in | Mirroring for operational databases; shortcuts for open-format data | [Phase 1](../../docs/microsoft-technical-reference.md#phase-1-data-engineering-on-microsoft-fabric) |
| The agent | Fabric data agent (generally available; F2 capacity or higher; runs with the user's identity and data permissions) | [Phase 4](../../docs/microsoft-technical-reference.md#copilot-studio--m365-copilot-extensibility) |
| Where users meet it | Fabric data agent added as a tool in Copilot Studio | [Phase 4](../../docs/microsoft-technical-reference.md#copilot-studio--m365-copilot-extensibility) |
| Business context | Fabric IQ semantic models and ontology | [Stack](../../docs/microsoft-technical-reference.md#-the-microsoft-fde-stack-oct-2026) |
| Deployment | `fabric-cicd` with an explicit `token_credential` | [Phase 1](../../docs/microsoft-technical-reference.md#phase-1-data-engineering-on-microsoft-fabric) |

## Practise

The CFO says the agent's quarterly revenue is 4% higher than the board report. Walk through how you find out why.
