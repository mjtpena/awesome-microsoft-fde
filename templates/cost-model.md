# Cost Model: <Agent / System name>

> **Step:** 5 Harden (draft in step 3) · **Pillar:** 6 Consulting and delivery · **Scenarios:** all (critical for disconnected, where hardware dominates)
>
> **How to use:** estimate monthly running cost at expected usage, then show what happens at 3× usage. Use the customer's actual price sheet; list prices change. The goal is one slide the sponsor understands.

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

<!-- Microsoft meters to check (each billed differently):
     - Foundry model and agent consumption
     - Azure AI Search tier
     - Fabric capacity (F SKU)
     - Copilot Studio: Copilot Credits (e.g. generative answer = 2, agent action = 5, tenant graph grounding = 10);
       GitHub Copilot harness usage is NOT covered by Microsoft 365 Copilot licences
     - Work IQ API: Copilot Credits (0.1 per tool call)
     - Agent 365: per user (US$15/user/month standalone or within Microsoft 365 E7)
     - API Management tier, Application Insights / Log Analytics ingestion
     Sources: docs/microsoft-technical-reference.md -->

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
