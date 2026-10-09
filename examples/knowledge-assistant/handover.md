# Handover: Harbourline Policy Assistant

> **Worked example.** A filled-in [`handover`](../../skills/handover/SKILL.md) for a fictional engagement; see [examples](../README.md). Everything below, including names, systems, scores and the product gap marked as invented, is invented. Microsoft product facts follow the [technical reference](../../docs/microsoft-technical-reference.md); check it before relying on them.

**Date:** week 10, Friday · **Technical owner:** S. Adeyemi (Platform team lead) · **Business owner:** D. Whitfield (Head of Claims Operations) · **Delivery team:** E. Marsh, T. Osei

Started in week 1 and filled in as each item landed. The last internal block is in the delivery team's workspace, not in Harbourline's repository; it's on this page only so you can see both.

## What was delivered

| Item | Location | Status |
|---|---|---|
| Running system (production) | Teams app "Policy Assistant", about 900 Motor and Property handlers; Motor live week 9 Monday, Property week 9 Thursday | Live |
| Source code and infrastructure-as-code | `policy-assistant` repository: `infra/`, `agent/`, `ingestion/`, `gateway/` | Merged to `main` |
| Pipelines | `deploy`, `reindex`, `evaluate`, `redteam`, `kill-switch` | Running; owned by the platform team |
| ADRs | `docs/adr/` (ADR-001 to ADR-006; [ADR-003](adr-003-current-version-only.md) amended week 6) | Accepted |
| Threat model | `docs/security/threat-model.md` ([example](threat-model.md)) | Signed by R. Okafor, week 7 |
| Responsible AI impact assessment | `docs/quality/responsible-ai-impact-assessment.md` ([example](responsible-ai-impact-assessment.md)) | Signed by F. Lindqvist, week 7 |
| Evaluation plan and golden set | `docs/quality/eval-plan.md` ([example](eval-plan.md)), `eval/golden-set.jsonl` (128 cases) | Running on every pull request, release and re-index |
| Runbook | `docs/operations/runbook.md` ([example](runbook.md)) | Drilled in week 10 |
| Cost model | `docs/engagement/cost-model.md` ([example](cost-model.md)) | Agreed with K. Brennan, week 8 |
| Coding-assistant instructions | `AGENTS.md` ([example](agent-instructions.md)) | Merged |
| Go-live readiness and incident review | [go-live-readiness.md](go-live-readiness.md), [incident-review.md](incident-review.md) | Closed |

## Results against the exit criteria

| Exit criterion (from the [use-case canvas](ai-use-case-canvas.md)) | Target | Achieved | Evidence |
|---|---|---|---|
| Business measure: time to a cited policy answer | Median under 2 minutes | **1 min 35 s** median, 20 handlers timed by the quality team in week 9 (baseline 22 minutes) | Quality team timing sheet, linked in `docs/engagement/` |
| Business measure: superseded-policy citations in the audit | Halved from 1 in 12, within one quarter of go-live | **Not measurable yet.** The quarterly audit runs one quarter after go-live. Early signal: no superseded citations in the weekly production samples since week 7 | Owner: D. Whitfield. Review date in the backlog |
| Evaluation release bar | Retrieval at 5 ≥ 90%, faithfulness ≥ 95%, correctness ≥ 85%, refusals 100%, zero pricing leak, p95 ≤ 8 s | Met: 93%, 97%, 89%, 24/24, 0, 7.4 s (week 9, production) | [Results log](eval-plan.md#results-log) |
| Security sign-off | Threat model signed; residual risks accepted by name | Met, with one accepted risk (Agent 365, below) | [Threat model](threat-model.md), [go-live readiness](go-live-readiness.md) |
| Deployed from code in the customer's environment | Everything from the pipeline, in Harbourline's subscription | Met. No portal changes in the activity log since week 8 | Pipeline run history |

## Evaluation baseline

The scores at handover, from the week-9 production run. The week-7 run (the first at 128 cases with the pilot widened) is the comparison point if anyone asks what changed at go-live. These become the alert thresholds in the [runbook](runbook.md#health-checks).

| Metric | Week 7 | Baseline (week 9) | Alert if below |
|---|---|---|---|
| Retrieval hit rate at 5 results | 94% | 93% | 90% (release bar); investigate if it drops 3 points in a week |
| Faithfulness | 97% | 97% | 95% |
| Correctness | 90% | 89% | 85%; investigate below 87% |
| Correct refusals (24 cases) | 100% | 100% | 100%: any miss is an incident |
| Pricing-draft content, low-privilege user | 0 | 0 | Any: kill switch, then incident |
| p95 latency | 7.1 s | 7.4 s | 8 s for 30 minutes |

## RACI

| Activity | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| Day-to-day operation | Platform on-call | S. Adeyemi | M. Costa | D. Whitfield |
| Incidents | Platform on-call | S. Adeyemi | R. Okafor (security), A. Novak (policy versions) | D. Whitfield |
| Releases and evaluation | Platform engineer | S. Adeyemi | M. Costa (golden-set answers) | D. Whitfield |
| Knowledge / data refresh | Platform on-call (runs the gated re-index) | S. Adeyemi | A. Novak (current versions), L. Moreau (SharePoint permissions), G. Patel (Pricing site) | M. Costa |
| Golden-set content | M. Costa | D. Whitfield | A. Novak | S. Adeyemi |
| Access reviews | Platform engineer | J. Tan | R. Okafor | S. Adeyemi |
| Cost management | S. Adeyemi | K. Brennan | | D. Whitfield |
| Security monitoring | Security operations | R. Okafor | S. Adeyemi | J. Tan |
| Log retention | Platform engineer | H. Ito | F. Lindqvist | S. Adeyemi |

**Named owner:** S. Adeyemi (technical), D. Whitfield (business) · **Operated the system alone from:** week 10, Monday **to:** week 10, Friday. E. Marsh and T. Osei stayed reachable and weren't called. One alert (spend at 50% of the monthly budget, on schedule) handled by on-call alone.

## Knowledge transfer

| Session | Audience | Date | Recording / notes |
|---|---|---|---|
| Architecture walkthrough | Platform team, R. Okafor, J. Tan | Week 9, Tuesday | Recording and slides in `docs/engagement/kt/` |
| Evaluation and release process | Platform team, M. Costa | Week 9, Wednesday | Recording; M. Costa added a case end to end while recorded |
| Gated re-index and urgent document removal | Platform on-call rota, A. Novak, L. Moreau | Week 9, Thursday | Recording; [runbook](runbook.md#re-index-procedure) |
| Runbook drill (simulated incident) | Platform on-call rota | Week 10, Wednesday | Simulated "Answer cites a superseded policy": a planted legacy copy in test. On-call found it from the logs, removed it and re-ran the gate in 35 minutes, using only the runbook. One step clarified afterwards |
| Cost and budget review | S. Adeyemi, K. Brennan | Week 10, Thursday | Notes in the [cost model](cost-model.md) |

## Backlog (ranked)

| # | Item | Why it matters | Effort |
|---|---|---|---|
| 1 | Move the remaining legacy policies from the file share's `published` folder into SharePoint with a `Status`, then retire the cross-source rule | Removes the root cause of the week-6 incident instead of guarding against it | M (A. Novak's team plus 2 platform days) |
| 2 | Agent 365 licences and Defender coverage for the agent | Closes the one accepted security risk | S (J. Tan, K. Brennan) |
| 3 | Re-run the superseded-citation audit one quarter after go-live and compare with the 1-in-12 baseline | The second business measure; tells D. Whitfield whether it worked | S (quality team) |
| 4 | Other claims lines and wider staff groups (deferred by the [scope reset](scope-reset.md)) | The original ask covered all 4,000 staff. Needs its own golden set, an oversharing review of any new sites, and an updated cost model (about 4.4× the questions) | L |
| 5 | **Customer-facing version in the claims portal** (deferred by the [scope reset](scope-reset.md)) | The director's original request. Triggers agreed in week 3: release 1 has met the superseded-citation target for a full quarter; a curated policyholder corpus with a named owner; compliance and security sign-off on a new route. A separate engagement, using the regulated scenario pack | L, new engagement |
| 6 | Native citations in Teams if the product adds them | Replaces text citations; see known product issues | S, when available |
| 7 | Revisit semantic caching if usage triples | Only with per-user isolation and an authentication method security accepts ([cost model](cost-model.md#cost-controls)) | M |

## Known issues and accepted risks

| Issue / risk | Impact | Accepted by | Review date |
|---|---|---|---|
| Defender doesn't cover the agent until Agent 365 licensing is in place | Agent threat detection relies on gateway and Foundry logs plus three alerts | R. Okafor | One month after handover |
| Teams over a source-IP-filtered public route ([ADR-006](adr-006-teams-public-route.md)) | An exception to "nothing public"; compensating controls and the IP alert in place | R. Okafor | Annual security review |
| About 210 file-share documents with no policy reference held out of the index until reviewed | Some legacy procedures can't be answered yet. A. Novak reviewed them by week 8; 38 remain held as "unclear" | D. Whitfield | Backlog item 1 |
| Pricing site permissions could be widened again by a site owner | Pricing drafts in answers | G. Patel, with the low-privilege test after every re-index | Quarterly access review |

## Known product issues and workarounds

| Issue | Affects | Workaround | Public tracking link (if any) |
|---|---|---|---|
| Foundry agents published to Teams don't support citations as a structured feature, or streaming | Every answer: handlers see plain text, and wait for the whole answer | The agent writes the title, version, effective-from date and link into the answer text; the evaluation checks every non-refusal answer has one | [Microsoft Learn: publish to Microsoft 365 with private networking](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/publish-copilot-virtual-network) |
| No built-in way to flag the same policy in two connected knowledge sources as superseded (**invented gap, for illustration only**) | Any source added later that duplicates SharePoint content | ADR-003 amendment 1: file-share copies that match a SharePoint document by policy reference or normalised title aren't indexed unless on A. Novak's allow-list; the duplicate-version check in every re-index must report zero | None public. Reported to the product team by the delivery team |

**Accepted by (customer owner):** S. Adeyemi (technical), D. Whitfield (business) · **Date:** week 10, Friday

---

## Internal: product field notes at handover

> **Vendor workspace only.** This block lives in the delivery team's `field-notes.md`, not in Harbourline's repository or tenant. Only the customer-facing summary above goes to Harbourline. Describes problems, not Harbourline's data.

| Product / feature | Where it stands at handover | What we'd tell the next team |
|---|---|---|
| Cross-source superseded duplicates (invented gap) | Filed in week 6 as [field feedback](field-feedback.md); two other teams added similar reports | Ask "where else does a copy of this live?" in the data audit, and test it before indexing a second source |
| Teams citations for Foundry agents | Documented limitation; +1 added to the existing product item | Decide text citations with the sponsor in week 2, not after the pilot |
| Re-indexing outside the release gate | Our process gap, not the product's | Gate re-indexing like a release from day one; we've proposed this to the runbook and eval-plan skill maintainers |
