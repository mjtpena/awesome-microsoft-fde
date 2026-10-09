---
name: incident-review
description: "Run a blameless post-incident review for an AI system failure (a wrong or harmful answer, a data leak, a wrong action, a cost spike): classify the failing layer from traces before anyone edits the prompt, then write the timeline, impact, contributing factors, new golden-set cases and regression test, and actions with owners and dates. Produces a customer-facing review and an internal block for the product team. Use within days of any incident in build, pilot or production."
---

# Incident Review

> Part of the [skills](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/skills/README.md) in the [Awesome Microsoft FDE](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/README.md) guide. **Step:** 4–5 Build and harden, and after go-live · **Pillars:** [5 AI applications](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/docs/pillars/05-ai-applications.md), [6 Consulting and delivery](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/docs/pillars/06-consulting-and-delivery.md)

What happened, why the system let it happen, and what now stops it happening again. An AI incident handled well builds more trust with a sponsor than a month of clean demos. Handled badly, it ends the engagement. See a [filled-in example](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/examples/knowledge-assistant/incident-review.md) for a fictional knowledge assistant.

## When to use

- Any time the system gives a wrong or harmful answer that someone acted on or forwarded, shows a user data they shouldn't see, takes a wrong action, or costs far more than expected.
- During a pilot as well as in production. The first incident usually happens in the pilot, in front of the sponsor.
- When a near miss would have been an incident with one more step (the wrong answer was caught before anyone used it). Review those too, in a lighter form.

## Rules

- **Contain first, review second.** If the failure can repeat, use the kill switch or the containment step from the [runbook](../runbook/SKILL.md) before you investigate.
- **Classify the failing layer from evidence before anyone touches the prompt.** Pull the trace for the failing request: the input, the retrieved documents, the tool calls, the identity used and the output. Most "the AI got it wrong" incidents turn out to be retrieval, data or permissions. A prompt edit made in a panic hides the real cause and breaks other cases. 💬
- **Blameless.** Write what the system allowed, not who slipped. "Human error" is never a root cause: it's a sign that the system made the wrong action easy. Name roles in the timeline, not people's failings.
- **Contributing factors, not one root cause.** AI incidents nearly always need several things to line up: a bad document, a ranking quirk, a missing evaluation case, an instruction that didn't say "show the version date". List them all; each gets an action or an explicit "accepted".
- **Every incident becomes evaluation cases and a regression test.** The failing request, plus close variants, go into the golden set in the [evaluation plan](../eval-plan/SKILL.md). The fix isn't done until those cases pass in the pipeline and the full set still meets the release bar.
- **Every action has one named owner and a date.** "The team" owns nothing.
- **Two versions.** The customer-facing review lives in the customer's repository. Product feedback and candid notes about the engagement go in an **internal** block in your own organisation's workspace, never in the customer's repository or tenant. Raise the product gap as a [field-feedback](../field-feedback/SKILL.md) report.
- **Don't speculate in writing.** Until the trace confirms a cause, write "suspected" and say what evidence would confirm it.

### Classify the failing layer

Work down this list with the trace open. Stop at the first layer where the evidence shows the fault, then check the layers below it too, because there is often more than one.

| Layer | What it looks like in the trace | Typical fix | Where it's recorded |
|---|---|---|---|
| Permissions | A document the user can't open in the source was retrieved, or the agent used its own identity where it should have used the user's | Fix the access-control list or trimming; re-run the low-privilege tests | [Threat model](../threat-model/SKILL.md), [ADR](../adr/SKILL.md) |
| Data | The right document was retrieved, but its content is wrong, stale, duplicated or unreadable (for example a scan with no text) | Fix or remove the source; agree an owner for "current" | [Data audit](../data-audit/SKILL.md) |
| Retrieval | The right document exists and is readable, but wasn't in the top results, or a worse one ranked above it | Index filters, metadata, chunking, ranking | ADR, evaluation plan (retrieval metrics) |
| Instructions | The right content was retrieved, but the agent ignored, misread or over-generalised it, or didn't refuse when it should have | Instruction change, tested against the full golden set | Evaluation plan |
| Model | Right content, clear instructions, still wrong, and repeatably so across runs | Different model or deployment, or a narrower task; rare in our experience 💬 | ADR |
| Tool | A tool was called with the wrong arguments, the wrong tool was chosen, or a tool returned an error the agent glossed over | Tool schema, validation, approval step | Threat model, runbook |
| Integration | The channel, gateway or client dropped or changed something: truncated citations, a stale cache, a timeout returned as an answer | Fix the integration; add an end-to-end test | Runbook |

On Microsoft, Foundry tracing, Application Insights and the gateway logs are where this evidence lives; check the [technical reference](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/docs/microsoft-technical-reference.md#evaluation--agentops) for current status. If you can't reconstruct the request from the logs, that is itself a contributing factor, and fixing it is an action.

### When to tell the customer's executives

Tell the sponsor the same day about any incident. Tell their executives, through the sponsor, when any of these is true:

- The wrong output reached an executive, a customer, a regulator or a decision that was acted on.
- Data reached someone who shouldn't have seen it. This may also trigger the customer's own data-breach process: tell the Data Protection Officer and let them decide, don't decide for them.
- An action changed something that couldn't be reversed.
- Spend went over the budget owner's alert level.

How: a short note from the sponsor, or from you with the sponsor's agreement, within one working day. Four lines: what happened, who was affected, what's already contained, and when the full review lands. Never let an executive hear about it from a forwarded screenshot first. 💬

## Steps

1. Contain the incident using the [runbook](../runbook/SKILL.md). Record the time.
2. Tell the sponsor the same day, and decide with them whether executives need a note (see above).
3. Pull the trace and logs for the failing request and preserve them before retention removes them.
4. Classify the failing layer with the table above. Reproduce the failure on the test environment before changing anything.
5. Write the [template](#template) to `docs/operations/incidents/<date>-<short-name>.md` in the customer's repository. Fill the timeline from logs, not memory.
6. Add the failing request and variants to the golden set; run the full evaluation on the fix; record the run in the evaluation results log.
7. Update everything the incident touched: the ADR that made the decision, the data audit, the threat model, and an incidents-table row in the runbook.
8. Hold a 30-minute review with the people involved on the customer's side. Agree the actions, owners and dates.
9. Write the internal block to your organisation's engagement workspace. File one [field-feedback](../field-feedback/SKILL.md) report per product gap and add a line to the [weekly status](../weekly-status/SKILL.md) field notes.
10. Close the review only when every action is done or explicitly accepted by a named person.

Write the customer-facing review into the customer's repository, not your own drive. Everything you write there belongs to the customer. Delete sections that don't apply: a short, filled-in document beats a long, empty one.

## Scenarios

Used in every scenario. What to emphasise:

- **Knowledge assistant:** usually data or retrieval: stale, duplicate or overshared documents. Check permissions first if the answer contained something the user shouldn't see.
- **Action-taking agent:** list every action taken, whether it was reversed, and who approved it. A wrong action is always an executive-level incident if it reached a customer.
- **Data agent:** capture the generated query, the result set and the semantic model version. A plausible wrong number is worse than an error.
- **Regulated:** follow the customer's own incident and breach procedure first; this review supplements it. Map actions to their control framework.
- **Disconnected:** logs may only be reachable on site. Record how evidence was collected and moved.

## Template

Two blocks. Write each to the location named in the steps, then fill it in.

### Customer repository: incident review

````markdown
# Incident Review: <short name>

**Status:** Draft / Actions open / Closed · **Severity:** 1 (reached customers, regulators or executive decisions) / 2 (reached users, contained) / 3 (near miss) · **Review owner:** · **Review held:**

## Summary

<Three sentences: what the system did, who it affected, and what now stops it happening again.>

## Impact

| Question | Answer |
|---|---|
| Who saw or acted on the output | |
| What decisions or actions it affected | |
| Data exposed (describe the type, not the content) | |
| Duration (first occurrence to containment) | |
| Cost impact | |
| Executive or customer communication sent | Yes / No: by whom, when |

## Timeline

Times from logs. Roles, not blame.

| Time | What happened | Source (log, trace, message) |
|---|---|---|
| | First occurrence | |
| | Detected, by whom (role) | |
| | Sponsor told | |
| | Contained | |
| | Fix deployed | |
| | Evaluation run passed | |

## Failing layer

| Layer | Evidence from the trace | At fault? |
|---|---|---|
| Permissions | | Yes / No / Contributing |
| Data | | |
| Retrieval | | |
| Instructions | | |
| Model | | |
| Tool | | |
| Integration | | |

**Reproduced on the test environment:** Yes / No · **Trace or request ID:**

## Contributing factors

What lined up to let this happen. No "human error".

| # | Factor | Why the system allowed it | Action or "accepted by" |
|---|---|---|---|

## What stops it happening again

| Change | Evaluation cases added (IDs) | Regression test | Documents updated |
|---|---|---|---|
| | | | ADR / data audit / threat model / runbook |

**Full evaluation after the fix:** <run ID, scores against the release bar>

## Actions

| # | Action | Owner | Due | Status |
|---|---|---|---|---|

## What went well

-

**Accepted by (customer):** · **Date:**
````

### Internal: engagement notes and product feedback

````markdown
# Incident Notes (Internal): <Customer> / <short name>

> Internal to the delivery team. Don't copy into the customer's repository or tenant. Describe problems, not customer data.

## Product gaps found

| Product / feature | Gap | Workaround used | Field-feedback report (link) |
|---|---|---|---|

## Engagement lessons

- What we'd do differently on the next engagement:
- Is the skill, checklist or template that should have caught this missing something? Raise it.

## Relationship

- How the sponsor took it, and what they need from us next:
````
