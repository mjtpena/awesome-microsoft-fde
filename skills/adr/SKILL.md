---
name: adr
description: "Write an architecture decision record (ADR): context, options with pros, cons, maturity and owner after handover, the decision, and its consequences for security, cost, operations, lock-in and preview dependencies. Use for any decision that would be expensive to reverse."
---

# Architecture Decision Record

> Part of the [skills](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/skills/README.md) in the [Awesome Microsoft FDE](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/README.md) guide. **Step:** 3 Design · **Pillars:** all

One page per decision that would be expensive to reverse. Reviewers in regulated and disconnected engagements want this paper trail.

## When to use

- Whenever you choose a platform, identity model, network design, data layer or anything else that would be expensive to undo.
- When an exception to a customer rule is needed (for example, a public endpoint in a private-only design).

## Rules

- One decision per ADR, one page each.
- Store ADRs in the customer's repository under `docs/adr/`, numbered.
- Never edit an accepted ADR; supersede it with a new one.
- Always list the option of doing the simpler thing, and say who maintains each option after handover.

## Steps

1. Find the next free number in `docs/adr/` and write the [template](#template) to `docs/adr/ADR-00X-<short-title>.md`.
2. Fill the context with the customer's constraints first: policies, skills, budget, deadlines.
3. Compare at least two options, including maturity (generally available or preview).
4. Write the decision as "We will … because …", then every consequence line.
5. If this supersedes an earlier ADR, update only the old ADR's status line.

Write everything into the customer's repository, not your own drive. Everything you write belongs to the customer. Delete sections that don't apply: a short, filled-in document beats a long, empty one.

## Decisions most engagements need, by scenario 💬

| Scenario | ADRs to expect |
|---|---|
| All | Agent platform (low code vs code) · where users meet the agent · identity model (as itself vs on behalf of user) · gateway in front of models · how evaluation gates releases |
| Knowledge assistant | Ingestion approach per source · chunking strategy · search type (hybrid, re-ranking, agentic retrieval) · permission trimming |
| Action agent | Which actions need human approval · tool design and error handling · audit trail |
| Data agent | Which data layer the agent queries · metric definitions · query safety limits |
| Regulated | Private networking design · exceptions to "nothing public" (for example Teams publishing) · log retention and location |
| Disconnected | Model selection for local hardware · update and transfer process · local identity |

## Scenarios

Used in every scenario. **Critical** in: [regulated, private-only](../scenario-regulated-private/SKILL.md), [disconnected or sovereign](../scenario-disconnected-sovereign/SKILL.md). Those packs say what to add.

## Template

Write everything inside the block below to the file named in the steps, then fill it in.

````markdown
# ADR-00X: <Decision in a few words>

- **Status:** Proposed | Accepted | Superseded by ADR-00Y
- **Date:**
- **Deciders:**
- **Pillar(s):** 1 Software · 2 Data · 3 Cloud/network · 4 Security · 5 AI · 6 Delivery

## Context

What forces this decision? Include constraints from the customer: policies, skills, budget, deadlines.

## Options considered

| Option | Pros | Cons | Maturity (generally available / preview) | Who maintains it after handover |
|---|---|---|---|---|

## Decision

We will … because …

## Consequences

- **Security and identity:**
- **Cost (monthly, at expected usage):**
- **Operations and ownership:**
- **Lock-in and exit path:** what it would take to move away from this choice
- **Preview dependencies and fallback:**
````
