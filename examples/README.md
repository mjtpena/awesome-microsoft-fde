# Worked examples

> Part of the [Awesome Microsoft FDE](../README.md) guide. One fictional engagement, taken from day 0 to handover, with every skill filled in. Read them in order to see what "done" looks like, and how the documents feed each other.

Everything here is invented: the company, the people, the systems, the numbers and any product gap described. Don't copy the content into a real engagement, and don't cite it as evidence about any Microsoft product. Copy the level of detail.

## The fictional engagement

**Harbourline Insurance** (fictional) has 4,000 staff, about 900 of them claims handlers. Handlers search three SharePoint sites and a file share for the current version of underwriting and claims policies. The sponsor, the Head of Claims Operations, wants handlers to ask questions in Teams and get answers that cite the policy they came from. The assistant only answers; it changes nothing.

### The fact sheet

Every example agrees with this sheet. If you add an example, use these facts and add new ones here first.

**People.** Everyone is referred to by role and initial; use "they" for all of them.

| Who | Role | Part in the story |
|---|---|---|
| D. Whitfield | Head of Claims Operations | Sponsor and business owner after handover |
| M. Costa | Motor claims team leader | Subject-matter expert; co-wrote the golden set; leads the pilot group |
| A. Novak | Underwriting policy manager | Subject-matter expert; owns which policy version is current |
| R. Okafor | Security Architect | Security review; accepts residual risks |
| J. Tan | Identity Lead | Entra roles and agent identity |
| L. Moreau | SharePoint administrator | Site permissions; fixes the Pricing oversharing |
| G. Patel | Head of Pricing | Owns the Pricing site; must approve anything that touches pricing drafts |
| H. Ito | Records manager | Log retention |
| F. Lindqvist | Data Protection Officer | Responsible AI and privacy sign-off |
| K. Brennan | IT Finance | Budget owner for running costs |
| S. Adeyemi | Platform team lead | Named technical owner after handover; on-call for the assistant |
| E. Marsh, T. Osei | FDEs (lead and second) | The delivery team, plus a part-time product engineer from the vendor side |

**The problem in numbers** (from discovery).

- Shadowing 30 handlers for a day: a median of 22 minutes per complex claim spent finding the right policy.
- The quality team's quarterly audit: 1 in 12 sampled claim decisions cited a superseded policy version.
- **Success measure agreed in the canvas:** median time to a cited policy answer under 2 minutes, and superseded-policy citations in the audit halved, within one quarter of go-live.

**Sources.**

| Source | Documents | What the data audit found |
|---|---|---|
| SharePoint: Claims Policy | about 2,400 | 31% exist in more than one version; no reliable "current" flag |
| SharePoint: Underwriting | about 1,100 | Clean; A. Novak's team maintains a `Status` column |
| SharePoint: Pricing | about 300, including drafts | Shared with "Everyone except external users": the oversharing finding |
| File share: legacy policies | about 1,800 (600 in `published`) | 140 scanned PDFs with no text layer; `drafts` folder excluded |

**Architecture.** Teams → Azure API Management gateway → Foundry prompt agent with its own Entra Agent ID → model in Foundry, plus a Foundry IQ knowledge base on Azure AI Search, permission-trimmed. See the diagram in the [threat model](knowledge-assistant/threat-model.md#2-how-the-system-works).

**Decisions** (ADRs in the customer's repository; the examples include three in full).

| ADR | Decision |
|---|---|
| ADR-001 | A Foundry prompt agent, not Copilot Studio: security required the gateway and logging in Harbourline's own Azure subscription |
| ADR-002 | A Foundry IQ knowledge base, not a hand-built vector pipeline |
| ADR-003 | Index only the current version of each policy, using the `Status` column or, where it's missing, a version rule agreed with A. Novak. Amended in week 6 after the incident |
| ADR-004 | Read-only: the assistant has no write tools |
| ADR-005 | The indexer gets site-scoped permissions, not tenant-wide |
| ADR-006 | Publish to Teams over a source-IP-filtered public route, with compensating controls |

**Timeline** (a 10-week engagement).

| Week | What happened |
|---|---|
| 0 | Access request sent on day 1; production data approval took nine working days |
| 1 | Kickoff, discovery interviews, stakeholder map |
| 2 | Canvas signed, ADRs 001–006, threat model v0.3, first evaluation plan |
| 3 | Data audit findings. **Scope reset:** the original ask also included a customer-facing version in the claims portal and all 4,000 staff. Release 1 became internal handlers only, Motor and Property first |
| 4 | First version on real data with a pilot group of 12 Motor handlers |
| 5 | Golden set at 120 cases; first full evaluation run passes the bar |
| 6 | **Incident:** the assistant cited a superseded Motor excess policy to a team leader, who forwarded it to D. Whitfield. Root cause was retrieval (an old copy on the file share with no status), not the model. Fixed, eight cases added to the golden set, ADR-003 amended, field feedback filed |
| 7 | Pilot widened to 60 handlers; red-team run; responsible AI assessment signed |
| 8 | Go-live readiness review; cost model agreed with K. Brennan |
| 9 | Go-live to about 900 Motor and Property handlers |
| 10 | Handover to S. Adeyemi (technical) and D. Whitfield (business) |

**Evaluation.** 120 golden cases to start (72 common, 24 hard or multi-part, 12 must refuse or escalate, 12 adversarial), 128 after the incident. Release bar: retrieval hit rate at 5 results ≥ 90%, faithfulness ≥ 95%, correctness ≥ 85%, 100% correct refusals, zero pricing-draft content for a non-pricing user, p95 latency ≤ 8 s. Correctness was 88% in week 5, fell to 81% after the week-6 re-index, and recovered to 90% in week 7.

**Usage for the cost model.** About 900 handlers × 6 questions a day × 21 working days ≈ 113,000 questions a month at go-live. Any unit rates in the examples are placeholders that show the method, not real prices.

## The examples

Read them in engagement order.

| Step | Example | Skill |
|---|---|---|
| 0 Kickoff | [Engagement charter](knowledge-assistant/engagement-kickoff.md) | [`engagement-kickoff`](../skills/engagement-kickoff/SKILL.md) |
| 1 Get access | [Access request](knowledge-assistant/access-request.md) | [`access-request`](../skills/access-request/SKILL.md) |
| 2 Understand | [Discovery notes](knowledge-assistant/discovery-interview.md) | [`discovery-interview`](../skills/discovery-interview/SKILL.md) |
| 2 Understand | [Stakeholder map](knowledge-assistant/stakeholder-map.md) | [`stakeholder-map`](../skills/stakeholder-map/SKILL.md) |
| 2 Understand | [Use-case canvas](knowledge-assistant/ai-use-case-canvas.md) | [`ai-use-case-canvas`](../skills/ai-use-case-canvas/SKILL.md) |
| 2 Understand | [Data audit](knowledge-assistant/data-audit.md) | [`data-audit`](../skills/data-audit/SKILL.md) |
| 2 Understand | [Scope reset, week 3](knowledge-assistant/scope-reset.md) | [`scope-reset`](../skills/scope-reset/SKILL.md) |
| 3 Design | [ADR-003: index only the current version](knowledge-assistant/adr-003-current-version-only.md) | [`adr`](../skills/adr/SKILL.md) |
| 3 Design | [ADR-004: read-only](knowledge-assistant/adr-004-read-only.md) | [`adr`](../skills/adr/SKILL.md) |
| 3 Design | [ADR-006: Teams over a filtered public route](knowledge-assistant/adr-006-teams-public-route.md) | [`adr`](../skills/adr/SKILL.md) |
| 3 Design | [Threat model](knowledge-assistant/threat-model.md) | [`threat-model`](../skills/threat-model/SKILL.md) |
| 3 Design | [Responsible AI impact assessment](knowledge-assistant/responsible-ai-impact-assessment.md) | [`responsible-ai-impact-assessment`](../skills/responsible-ai-impact-assessment/SKILL.md) |
| 3 Design | [Evaluation plan](knowledge-assistant/eval-plan.md) | [`eval-plan`](../skills/eval-plan/SKILL.md) |
| 4 Build | [Coding-assistant instructions](knowledge-assistant/agent-instructions.md) | [`agent-instructions`](../skills/agent-instructions/SKILL.md) |
| Every week | [Status: weeks 1, 3 and 6](knowledge-assistant/weekly-status.md) | [`weekly-status`](../skills/weekly-status/SKILL.md) |
| 4–5 Incident | [Incident review: the superseded excess policy](knowledge-assistant/incident-review.md) | [`incident-review`](../skills/incident-review/SKILL.md) |
| 4–5 Feedback | [Field feedback to the product team](knowledge-assistant/field-feedback.md) | [`field-feedback`](../skills/field-feedback/SKILL.md) |
| 5 Harden | [Red-team report](knowledge-assistant/red-team.md) | [`red-team`](../skills/red-team/SKILL.md) |
| 5 Harden | [Cost model](knowledge-assistant/cost-model.md) | [`cost-model`](../skills/cost-model/SKILL.md) |
| 5 Harden | [Go-live readiness](knowledge-assistant/go-live-readiness.md) | [`go-live-readiness`](../skills/go-live-readiness/SKILL.md) |
| 6 Hand over | [Runbook](knowledge-assistant/runbook.md) | [`runbook`](../skills/runbook/SKILL.md) |
| 6 Hand over | [Handover](knowledge-assistant/handover.md) | [`handover`](../skills/handover/SKILL.md) |

What a good example shows:

- Every row filled in, or marked "doesn't apply" with a reason.
- Defences and claims that say **how they're tested**, not just what they are.
- A named person accepting each residual risk and owning each action.
- Decisions that point to the ADR where they were made, and documents that agree with each other.

The [reference implementation](../reference/knowledge-assistant/README.md) is the same assistant as runnable code: infrastructure, agent and the evaluation gate.
