---
name: cost-model
description: "Estimate monthly running cost of an AI solution at expected usage and at 3× usage, list cost controls, and produce a one-slide summary for the sponsor. Use in design (draft) and hardening (final); critical for disconnected engagements where hardware dominates."
---

# Cost Model

> Part of the [skills](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/skills/README.md) in the [Awesome Microsoft FDE](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/README.md) guide. **Step:** 5 Harden (draft in step 3) · **Pillar:** [6 Consulting and delivery](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/docs/pillars/06-consulting-and-delivery.md)

What the solution will cost per month and what drives it, on one slide the sponsor understands. Customers cancel projects late over cost surprises.

## When to use

- Draft in design, alongside the [use-case canvas](../ai-use-case-canvas/SKILL.md).
- Finalise before go-live, and revisit when usage assumptions change.

## Rules

- Use the customer's actual price sheet: list prices change.
- Always show what happens at 3× usage.
- Every assumption has a source or reasoning.
- Pair the estimate with controls (limits, budgets, alerts).

## Steps

1. Write the [template](#template) to `docs/engagement/cost-model.md` in the customer's repository.
2. Fill usage assumptions with the sponsor; mark guesses as guesses.
3. Fill the monthly cost table; check the Microsoft meters listed in the template comment.
4. Tick the cost controls that are in place and raise the rest as risks.
5. Write the one-slide summary last.

Write everything into the customer's repository, not your own drive. Everything you write belongs to the customer. Delete sections that don't apply: a short, filled-in document beats a long, empty one.

## Scenarios

Used in every scenario. **Critical** in: [disconnected or sovereign](../scenario-disconnected-sovereign/SKILL.md). Those packs say what to add.

## Template

Write everything inside the block below to the file named in the steps, then fill it in.

````markdown
# Cost Model: <Agent / System name>

## Usage assumptions

| Assumption | Value | Source / reasoning |
|---|---|---|
| Users | | |
| Conversations per user per day | | |
| Model calls per conversation | | |
| Average input / output tokens per call | | |
| Tool calls per conversation | | |
| Documents / data volume indexed | | |
| Working days per month | | |

## Monthly cost

| Component | Pricing unit | Units / month | Unit price | Monthly cost | Notes |
|---|---|---|---|---|---|
| Model usage | per token | | | | |
| Agent hosting | | | | | |
| Search / knowledge index | | | | | |
| Data platform capacity | | | | | |
| Gateway | | | | | |
| Monitoring and logs | | | | | |
| Licences (per user) | per user / month | | | | |
| **Total** | | | | | |
| **At 3× usage** | | | | | |

<!-- Microsoft meters to check (each billed differently). Rates aren't copied here because they change:
     use the customer's price sheet, and the current rates in the technical reference.
     - Foundry model and agent consumption
     - Azure AI Search tier
     - Fabric capacity (F SKU)
     - Copilot Studio: Copilot Credits, charged at different rates for answers, actions and tenant graph grounding;
       employee-facing use by Microsoft 365 Copilot-licensed users is not charged; GitHub Copilot harness usage is not
       covered by Microsoft 365 Copilot licences; with prepaid capacity, agents are disabled once overage passes a threshold
     - Work IQ API: Copilot Credits per tool call
     - Agent 365: licensed per user, not per agent
     - API Management tier, Application Insights / Log Analytics ingestion
     Current rates: https://github.com/mjtpena/awesome-microsoft-fde/blob/main/docs/microsoft-technical-reference.md#copilot-studio--m365-copilot-extensibility and https://github.com/mjtpena/awesome-microsoft-fde/blob/main/docs/microsoft-technical-reference.md#phase-3-identity-security--governance-for-agents -->

## Cost controls

- [ ] Per-team token limits at the gateway
- [ ] Budgets and alerts on the subscription or resource group
- [ ] Caching for repeated questions (if appropriate)
- [ ] Loop and retry limits in the agent
- [ ] Credit or capacity caps for low-code environments

## Scenario notes

- **Knowledge assistant:** indexing and re-indexing large document sets can cost more than answering questions; estimate both.
- **Action agent:** count tool calls, which often outnumber model calls.
- **Data agent:** query compute on the data platform is often the biggest line.
- **Disconnected:** replace consumption with hardware, power, support and the people who run it on site.

## One-slide summary

> At <N> users, this costs about **<$X> per month**, mainly driven by **<top driver>**. At 3× usage it's **<$Y>**. Controls in place: <list>.
````
