# Go-Live Readiness: Harbourline Policy Assistant

> **Worked example.** A filled-in [`go-live-readiness`](../../skills/go-live-readiness/SKILL.md) checklist for a fictional engagement; see [examples](../README.md). Everything below, including names and systems, is invented. Microsoft product facts follow the [technical reference](../../docs/microsoft-technical-reference.md); check it before relying on them.

**Target go-live:** week 9, Monday, to about 900 Motor and Property handlers · **Decision meeting:** week 8, Thursday · **Go / no-go owner:** D. Whitfield (Head of Claims Operations) · **In the room:** R. Okafor, J. Tan, F. Lindqvist, K. Brennan, S. Adeyemi, M. Costa, E. Marsh, T. Osei

Started in week 3 and ticked as evidence arrived. Every ticked box links to its evidence. The two open boxes have an owner, a date and a written risk acceptance.

## Core checklist (every scenario)

### Identity and access

- [x] The agent has its own identity (Entra Agent ID); keys disabled on the Foundry account, keyless sign-in only. Evidence: a call with an API key returns 401, logged in the week-7 [red-team run](red-team.md)
- [x] Least-privilege roles scoped to specific resources: the agent has search index read only; the indexer has site-scoped read (ADR-005, see the [threat model](threat-model.md#3-identities-and-permissions)), not tenant-wide. FDE admin access was time-limited through Privileged Identity Management and ends in week 10. Evidence: role assignment export, reviewed by J. Tan in week 8
- [x] Callers only get the permissions they need: handlers reach the agent through Teams and the gateway; no handler has a Foundry role. Evidence: role assignment export

### Network

- [x] Private endpoints and private DNS tested from the platform team's own network for Foundry, Azure AI Search and storage. Evidence: name-resolution and connection test log, week 7
- [x] All model traffic goes through the APIM (Azure API Management) gateway, with per-user token limits and request logging. Evidence: 10× load test in week 7 showed throttling and the spend alert firing ([cost model](cost-model.md#cost-controls))
- [x] Outbound traffic restricted: public network access disabled on Foundry and Search. The only public route is the source-IP-filtered Teams route accepted in [ADR-006](adr-006-teams-public-route.md). Evidence: a request from an address outside the allowed ranges is rejected and raises the alert ([runbook](runbook.md#incidents))

### Data

- [x] Permission trimming verified with a low-privilege test user: 25 pricing questions as `svc-eval-lowpriv`, zero Pricing-site content. Run after every re-index since week 4, last on week 8's re-index. Evidence: [eval-plan.md](eval-plan.md#results-log), [threat model](threat-model.md#4-threats)
- [x] Oversharing review done for all three SharePoint sites; the Pricing site's "Everyone except external users" access removed by L. Moreau in week 4, approved by G. Patel. Evidence: [data audit](data-audit.md), site permission report

### Quality and safety

- [x] Golden set passes the agreed release bar: version 0.8 on 128 cases, retrieval at 5 results 94%, faithfulness 97%, correctness 90%, refusals 24 of 24, zero pricing leaks, p95 7.2 s. Evidence: [eval-plan.md](eval-plan.md#results-log)
- [x] Red-team scan run: the AI Red Teaming Agent, 40 manual jailbreak prompts and the seeded hidden-instruction document. Every finding fixed or accepted by R. Okafor; none open. Evidence: [red-team.md](red-team.md)
- [x] Threat model reviewed and signed off by security. Evidence: [threat-model.md](threat-model.md), final version signed by R. Okafor in week 7
- [x] Responsible AI impact assessment signed. Evidence: [responsible-ai-impact-assessment.md](responsible-ai-impact-assessment.md), signed by F. Lindqvist in week 7

### Operations

- [x] Tracing, dashboards and alerts live: retrieved document IDs traced per request; alerts for more than 20 content-safety blocks an hour, any request from outside the allowed IP ranges, and spend above 80% of the monthly budget. Evidence: each alert fired once in test and reached platform on-call
- [x] Budgets, cost alerts and caps in place. Evidence: [cost-model.md](cost-model.md), agreed with K. Brennan in week 8
- [x] Deployed from code via the pipeline: infrastructure, agent definition, instructions and gateway policies. Evidence: production deployment run from the pipeline in week 8; no portal changes in the activity log
- [x] Preview features listed, each with a fallback: none in the request path. Knowledge-base query planning (preview) is deliberately off. Evidence: dependency list in the repository README
- [x] Runbook tested by someone who didn't build the system: a platform engineer on S. Adeyemi's team worked a simulated "answers suddenly worse after a re-index" incident using only the runbook, in 40 minutes, with two questions that were then written into it. Evidence: drill notes, week 8 ([runbook.md](runbook.md))
- [ ] **Named owner, RACI and handover accepted.** Owner: S. Adeyemi. RACI agreed; handover completes in week 10 after the platform team operates the system alone ([handover.md](handover.md)). **Date:** week 10. Accepted as a condition by D. Whitfield: go-live doesn't wait for handover, but the FDEs stay on call through week 10
- [x] Kill switch documented and tested: disable the API on the gateway. Used for real in week 6 (pilot paused in under 30 minutes, see the [incident review](incident-review.md)) and drilled again in week 8. Evidence: [runbook.md](runbook.md#kill-switch)

## Scenario add-ons

### Knowledge assistant

- [x] Every answer cites its source **in Teams**, the channel handlers use. Foundry agents published to Teams don't show native citations ([technical reference](../../docs/microsoft-technical-reference.md#phase-2-azure-architecture--ai-landing-zones)), so the agent writes the policy title, section, effective date and a link into the answer text. Citation correctness is in the correctness rubric (90%). D. Whitfield accepted text citations after the week-4 pilot. Evidence: [eval-plan.md](eval-plan.md#knowledge-assistant), pilot feedback
- [x] Refresh schedule running and monitored: nightly incremental, monthly full; every re-index runs in test first, then the duplicate-version check, the evaluation and the pricing test before production ([ADR-003](adr-003-current-version-only.md), amended week 6). Evidence: indexer run history, weeks 6 to 8
- [x] "I don't know" behaviour tested: 6 golden cases ask about cover Harbourline doesn't offer; all answered "I can't find that". Evidence: [eval-plan.md](eval-plan.md#golden-set)
- [x] Superseded-version cases pass: GS-121 to GS-128 from the week-6 incident, all correct, no superseded document in any retrieved set. Evidence: [eval-plan.md](eval-plan.md#results-log)

## Microsoft-specific checks

Checked against the [technical reference](../../docs/microsoft-technical-reference.md) and Microsoft Learn on the Tuesday before the meeting. Checks for Copilot Studio, hosted agents and agent tools in the virtual network are deleted: none of them is in this design.

- [x] Agent identity via Entra Agent ID
- [ ] **Agent 365 licences in place for Defender to cover the Foundry agent.** Defender agent coverage for Foundry agents needs an Agent 365 licence ([technical reference](../../docs/microsoft-technical-reference.md#phase-3-identity-security--governance-for-agents)). J. Tan is confirming which users need a licence; K. Brennan has the per-user cost. **Owner:** J. Tan · **Date:** week 10. **Risk accepted** by R. Okafor until then: gateway and Foundry logs go to Harbourline's Log Analytics workspace and security operations watches the three alerts above
- [x] Callers who only invoke the agent use **Foundry Agent Consumer**; keyless sign-in. Evidence: role assignment export
- [x] API Management AI gateway: token limits, logging, `llm-content-safety` on prompts and responses. Evidence: gateway policy in the repository; content-safety alert test
- [x] Publishing to Teams with public access disabled: `enable_m365_public_endpoint` approved by R. Okafor in [ADR-006](adr-006-teams-public-route.md); Bot Service rights granted by J. Tan in week 3
- [x] Foundry agent published to Teams: missing citations and streaming accepted by D. Whitfield; Microsoft 365's handling of the agent's responses accepted by F. Lindqvist in the [responsible AI impact assessment](responsible-ai-impact-assessment.md)
- [x] Agent uses a knowledge base on Azure AI Search: faithfulness measured with retrieved passages as `context` in the dataset, not the tool-call evaluators. Evidence: [eval-plan.md](eval-plan.md#metrics-and-release-bar)
- [x] Purview oversharing assessment reviewed for the three indexed SharePoint sites. Evidence: [data audit](data-audit.md)

**Decision:** Go with conditions · **Signed:** D. Whitfield (Head of Claims Operations), with R. Okafor (security) and F. Lindqvist (data protection) · **Date:** week 8, Thursday

**Conditions:**

1. Handover to S. Adeyemi completes in week 10 after a week of the platform team operating alone; E. Marsh and T. Osei stay on call until then.
2. Agent 365 licensing decided by week 10 (J. Tan). If it isn't, R. Okafor reviews the risk acceptance again.
3. Rollout in two waves: Motor (about 500 handlers) on Monday, Property on Thursday if the first three days show no alert above threshold and the weekly production sample passes.
