# AI Use-Case Canvas: Harbourline Policy Assistant

> **Worked example.** A filled-in [`ai-use-case-canvas`](../../skills/ai-use-case-canvas/SKILL.md) for a fictional engagement; see [examples](../README.md). Everything below, including names and systems, is invented. Microsoft product facts follow the [technical reference](../../docs/microsoft-technical-reference.md); check it before relying on them.

**Version:** 1.1 · **Built from:** the [discovery interviews](discovery-interview.md) and the [data audit](data-audit.md)

| Version | Date | Change | Agreed by |
|---|---|---|---|
| 1.0 | Week 2, day 3 | First signed version. Users: all 4,000 staff, plus a customer-facing version in the claims portal | D. Whitfield |
| 1.1 | Week 3, day 4 | **Scope reset.** Release 1 narrowed to internal claims handlers, Motor and Property first. Customer portal and all-staff access moved to "out of scope for release 1". Driven by the [data audit](data-audit.md): Claims Policy versioning and the Pricing oversharing couldn't be fixed for 4,000 users and the public in the time left. Full reasoning in the [scope reset](scope-reset.md) | D. Whitfield, re-signed |

## The problem

| Field | Answer |
|---|---|
| Problem in one sentence | Claims handlers spend too long finding the current version of a policy, and too often cite a superseded one |
| Business measure and target (from the five whys) | **Median time to a cited policy answer under 2 minutes** (baseline 22 minutes, from shadowing 30 handlers), **and superseded-policy citations in the quarterly quality audit halved** (baseline 1 in 12 sampled decisions), within one quarter of go-live |
| Who uses it, and how many | Internal staff only: about 900 claims handlers, Motor and Property first. Pilot of 12 Motor handlers led by M. Costa, widening to 60 before go-live |
| What they do today | Search three SharePoint sites and a file share, open several versions, check dates by hand, then ask a colleague to confirm |
| What's explicitly **out** of scope | Customer-facing answers in the claims portal (release 2 at the earliest, with its own threat model and [responsible AI assessment](responsible-ai-impact-assessment.md)). Staff outside claims. Lines of business other than Motor and Property in release 1. Any change to a policy, claim or system. Rewriting or cleaning the source documents themselves |

## The shape

| Field | Answer |
|---|---|
| Scenario | Knowledge assistant |
| Knowledge and data sources | SharePoint: Claims Policy (Motor and Property sections), Underwriting, Pricing (after the oversharing fix); file share `published` folder. Only the current version of each policy is indexed ([ADR-003](adr-003-current-version-only.md)) |
| Does it write or change anything? | **No.** No write tools ([ADR-004](adr-004-read-only.md)) |
| Human approval points | None at run time, because it takes no action. The handler remains the decision-maker on every claim; A. Novak approves which version counts as current |
| Where users meet it | Teams, over a source-IP-filtered public route ([ADR-006](adr-006-teams-public-route.md)) |

## Platform choice

| Field | Answer |
|---|---|
| Platform | Foundry prompt agent with its own Entra Agent ID, behind the Azure API Management (APIM) gateway, with a Foundry IQ knowledge base on Azure AI Search |
| Why this one (and why not the simpler option) | Copilot Studio was the simpler option and was considered first. R. Okafor required the gateway and all request logging inside Harbourline's own Azure subscription, alongside their existing security monitoring. Recorded in ADR-001. A Foundry IQ knowledge base rather than a hand-built vector pipeline, so the platform team doesn't maintain chunking and embedding code (ADR-002) |
| Who will maintain it, and what skills do they have? | S. Adeyemi's platform team: Bicep, Python, Azure DevOps, the shared APIM instance. No prior AI experience; pairing from week 4 |
| Preview features we depend on, and the fallback for each | None by design. We don't use LLM query planning or layout-aware ingestion, both preview at the time of writing ([technical reference: Foundry IQ](../../docs/microsoft-technical-reference.md#foundry-iq-enterprise-knowledge), [RAG blueprint](../../docs/microsoft-technical-reference.md#enterprise-rag-blueprint-azure)). Fallback if a multi-part question needs planning later: single-query retrieval, already the default |

💬 Teams was the users' choice and the sponsor's requirement, and it costs us something: Foundry agents published to Teams don't support citations as a structured feature ([technical reference, Phase 2](../../docs/microsoft-technical-reference.md#phase-2-azure-architecture--ai-landing-zones)). Cited answers are the point of this assistant, so the agent writes the source title, version and link into the answer text, and the [evaluation plan](eval-plan.md) checks every answer has one. See [ADR-006](adr-006-teams-public-route.md).

## Quality, safety and cost

| Field | Answer |
|---|---|
| Golden set size and who writes it | 120 cases to start: 72 common, 24 hard or multi-part, 12 must refuse or escalate, 12 adversarial. Written by M. Costa and A. Novak, starting from the 20 most-asked questions. See the [evaluation plan](eval-plan.md) |
| Release bar | Retrieval hit rate at 5 results ≥ 90%; faithfulness ≥ 95%; correctness ≥ 85%; 100% correct refusals; zero pricing-draft content for a non-pricing user; p95 latency ≤ 8 s |
| Main risks (accuracy, data leakage, harmful actions) | **Accuracy:** superseded versions retrieved, because Claims Policy has no reliable current flag ([data audit](data-audit.md)). **Data leakage:** Pricing site shared with "Everyone except external users". **Harmful actions:** none; read-only. Full list in the [threat model](threat-model.md) |
| Identity model | Both. The agent acts as itself (Entra Agent ID, keyless) to call the model; retrieval is trimmed to the asking user's document permissions |
| Expected monthly cost at target usage | About 113,000 questions a month (900 handlers × 6 a day × 21 working days). See [`cost-model.md`](cost-model.md); agreed with K. Brennan in week 8 |

## Exit criteria (agree before building)

- [ ] Release bar met on the golden set, including the low-privilege pricing run
- [ ] Security sign-off: R. Okafor, including the ADR-006 exception
- [ ] Responsible AI and privacy sign-off: F. Lindqvist
- [ ] Named owner at the customer: **S. Adeyemi (technical), D. Whitfield (business)**
- [ ] Running in Harbourline's Azure subscription, deployed from code by their pipeline
- [ ] [Runbook](runbook.md) and [handover](handover.md) accepted, including the re-index check
- [ ] Baseline for both success measures recorded before go-live, so the quarter-after measurement has something to compare against

**Agreed by (sponsor):** D. Whitfield · **Date:** week 2, day 3 (v1.0); re-signed week 3, day 4 (v1.1)

## Open questions for the sponsor

- Who in the quality team re-runs the audit sample a quarter after go-live, and will they tag superseded-policy citations the same way? (Owner: D. Whitfield, by week 6.)
- What does release 2 need to show before the customer portal is reconsidered? Proposed in the [scope reset](scope-reset.md); not yet agreed.
