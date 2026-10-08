---
name: ai-use-case-canvas
description: "Write the one-page scope for an AI engagement: problem, business measure, scenario shape, platform choice and why, quality bar, risks, cost and exit criteria, for the sponsor to sign. Use after discovery and before building."
---

# AI Use-Case Canvas

> Part of the [skills](../README.md) in the [Awesome Microsoft FDE](../../README.md) guide. **Step:** 2 Understand · **Pillars:** [5 AI applications](../../docs/pillars/05-ai-applications.md), [6 Consulting and delivery](../../docs/pillars/06-consulting-and-delivery.md)

The one-page scope. If a box is empty, that's your next discovery question.

## When to use

- After the first round of discovery interviews, before you build.
- Whenever the sponsor asks for something new: check it against what's in and out of scope.

## Rules

- Get the sponsor to agree it **in writing** before you build.
- Default to the simplest platform that meets the need, and write down the specific limitation that forces a more complex one. 💬
- Exit criteria are agreed now, not at the end.

## Steps

1. Write the [template](#template) to `docs/engagement/use-case-canvas.md` in the customer's repository.
2. Fill the problem section from the discovery notes, including the business measure from the five whys.
3. Pick the scenario and platform; justify the platform against the simpler option.
4. Leave empty boxes empty and list them as open questions for the sponsor.
5. Link the cost line to the [cost model](../cost-model/SKILL.md) and the release bar to the [evaluation plan](../eval-plan/SKILL.md).

Write everything into the customer's repository, not your own drive. Everything you write belongs to the customer. Delete sections that don't apply: a short, filled-in document beats a long, empty one.

## Scenarios

Used in every scenario. Each [scenario pack](../README.md#scenario-packs) says what to add.

## Template

Write everything inside the block below to the file named in the steps, then fill it in.

````markdown
# AI Use-Case Canvas: <Name>

## The problem

| Field | Answer |
|---|---|
| Problem in one sentence | |
| Business measure and target (from the five whys) | e.g. cut policy tickets by 30% in 3 months |
| Who uses it, and how many | Internal staff / external customers / both |
| What they do today | |
| What's explicitly **out** of scope | |

## The shape

| Field | Answer |
|---|---|
| Scenario | Knowledge assistant / Action agent / Data agent (+ Regulated / Disconnected) |
| Knowledge and data sources | |
| Does it write or change anything? | No / Yes: list actions and whether each is reversible |
| Human approval points | |
| Where users meet it | Teams / Microsoft 365 Copilot / web app / other |

## Platform choice

| Field | Answer |
|---|---|
| Platform | Copilot Studio / declarative agent / Foundry prompt agent / Agent Framework + Foundry hosted agent / Foundry Local |
| Why this one (and why not the simpler option) | |
| Who will maintain it, and what skills do they have? | |
| Preview features we depend on, and the fallback for each | |

💬 Default to the simplest platform that meets the need. Write down the specific limitation that forces you to a more complex one.

## Quality, safety and cost

| Field | Answer |
|---|---|
| Golden set size and who writes it | 50–200 questions, with the customer |
| Release bar | e.g. ≥ 85% task adherence, ≥ 90% correct citations |
| Main risks (accuracy, data leakage, harmful actions) | |
| Identity model | Agent acts as itself / on behalf of the user / both |
| Expected monthly cost at target usage | See `cost-model.md` |

## Exit criteria (agree before building)

- [ ] Release bar met on the golden set
- [ ] Security sign-off
- [ ] Named owner at the customer: ______
- [ ] Running in the customer's environment, deployed from code
- [ ] Runbook and handover accepted

**Agreed by (sponsor):** · **Date:**
````
