# AI Use-Case Canvas: <Name>

> **Step:** 2 Understand · **Pillars:** 5 AI applications, 6 Consulting and delivery · **Scenarios:** all
>
> **How to use:** this is the one-page scope. Get the sponsor to agree it in writing before you build. If a box is empty, that's your next discovery question.

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
