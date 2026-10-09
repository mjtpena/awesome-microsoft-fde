---
name: field-feedback
description: "Turn a field finding into a product-gap report a product team can triage: one finding per report, a reproduction on a clean environment with no customer data, customer impact, the workaround in use, how many engagements hit it, severity, the specific ask, and confidentiality checks. Written in your own organisation's internal workspace, never the customer's repository. Use weekly from the field notes, after any incident that exposed a product gap, and at handover."
---

# Field Feedback

> Part of the [skills](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/skills/README.md) in the [Awesome Microsoft FDE](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/README.md) guide. **Step:** Every week (from the weekly-status field notes) and at handover · **Pillar:** [6 Consulting and delivery](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/docs/pillars/06-consulting-and-delivery.md)

A product-gap report that a product manager can triage in five minutes and an engineer can reproduce in thirty. See a [filled-in example](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/examples/knowledge-assistant/field-feedback.md) for a fictional knowledge assistant.

💬 **Our take:** this loop is what makes forward deployed engineering an engineering function rather than staffing. Without it, an FDE team is skilled people building workarounds at one customer at a time, and the product never learns. With it, every engagement makes the next one cheaper. A team that files nothing is either working on a perfect product or not doing the job.

## When to use

- Every week: review the field notes log from the [weekly status](../weekly-status/SKILL.md) and turn any finding that cost real time, or that you've seen before, into a report.
- After an [incident review](../incident-review/SKILL.md) that found a product gap among the contributing factors.
- At [handover](../handover/SKILL.md): file anything still sitting in the field notes. Once you leave, nobody else will.

## Rules

- **Internal only.** The report lives in your own organisation's internal workspace or the product team's intake system. Never in the customer's repository, tenant, or a shared channel with the customer in it.
- **One finding per report.** Two problems in one report get triaged as the easier one.
- **Reproduce on a clean environment with no customer data.** Your own test subscription or tenant, synthetic documents, invented names. If you can't reproduce it away from the customer, say so and say why; don't paste their data to prove it.
- **Describe the problem, not the customer's data.** No document contents, prompts with real names, screenshots of their tenant, or identifiers. Name the customer only if your agreement with them allows it and the product team needs it to prioritise; otherwise use an industry and size ("a mid-sized insurer").
- **Check the customer agreement before you share anything.** Some agreements forbid naming the customer or describing their architecture even internally beyond the delivery team. If unsure, ask the engagement lead.
- **Say what you're asking for.** A fix, a documentation change, a setting, a roadmap answer, or just "count this". A report with no ask gets closed.
- **Count engagements, not complaints.** How many engagements hit this, and how much time it cost each, is what moves a backlog. Check with other FDE teams before filing; add to an existing report rather than duplicating it.
- **Severity follows customer impact, not how annoying it was to work around.**
- **Tell the customer what affects them separately.** Known issues and workarounds go in the handover's "Known product issues" table, with a public tracking link if one exists. The internal report doesn't.

### Severity

| Severity | Meaning |
|---|---|
| S1 Blocker | No workaround; the engagement can't ship, or shipped with a risk a customer had to formally accept |
| S2 Major | A workaround exists but costs days of engineering, or leaves a risk the customer has to operate around |
| S3 Moderate | A workaround costs hours, or is easy to get wrong |
| S4 Minor | Friction, missing documentation, or an unclear error message |

Raise severity by one if three or more engagements have hit it. 💬

## Steps

1. Pick one finding from the field notes. Search the product team's intake for an existing report; if one exists, add your engagement's evidence to it instead.
2. Reproduce it on a clean environment with synthetic data. Write the minimal steps.
3. Write the [template](#template) to your organisation's internal workspace (for example `field-feedback/<product>-<short-name>.md`) or the product team's intake form.
4. Fill impact and workaround from the engagement, with customer details stripped.
5. Ask other FDE teams whether they've hit it; record the count.
6. Run the confidentiality check before you submit.
7. Link the report from the field notes log and from the incident review's internal block, if there was one.
8. Review open reports at handover and follow up on any that have had no response.

## Scenarios

Used in every scenario. Common sources of findings:

- **Knowledge assistant:** ingestion and extraction gaps, version handling, permission trimming edge cases, channel limits on citations.
- **Action-taking agent:** missing approval or rollback hooks, identity and consent gaps for tools.
- **Data agent:** semantic model limits, query generation on real schemas.
- **Regulated:** features missing from private-networking or regional deployments.
- **Disconnected:** features that assume internet access, and update paths that don't work offline.

## Template

Write everything inside the block below to your own organisation's internal workspace, then fill it in. Never write it to the customer's repository.

````markdown
# Field Feedback: <Product / feature>: <the gap in a few words>

> Internal. Contains no customer data. Not for the customer's repository or tenant.

**Filed by:** · **Severity:** S1 / S2 / S3 / S4 · **Engagements affected:** <count> · **Status:** Draft / Filed / Acknowledged / Planned / Closed · **Tracking link:**

## The gap

<Two sentences: what the product does, and what a customer needed it to do.>

## Reproduction (clean environment, synthetic data)

| Item | Detail |
|---|---|
| Environment | <own test subscription or tenant; region; relevant settings> |
| Product versions / SKUs / preview flags | |
| Steps | 1. … 2. … 3. … |
| Expected | |
| Actual | |
| Reproduced away from the customer? | Yes / No: why not |

## Customer impact

| Question | Answer |
|---|---|
| Customer (industry and size, or name if the agreement allows) | |
| Scenario | Knowledge assistant / Action agent / Data agent (+ Regulated / Disconnected) |
| What it blocked or put at risk | |
| Engineering time lost | |
| Did it cause an incident? | Yes / No: link to the internal incident notes |

## Workaround in use

| Workaround | Cost to build | Cost to operate | Weaknesses |
|---|---|---|---|

## Other engagements

| Team / engagement (no customer data) | Same gap? | Workaround |
|---|---|---|

## What we're asking for

- [ ] Product fix: <the behaviour we need>
- [ ] Documentation change: <where and what>
- [ ] Roadmap answer: <the question>
- [ ] Count this: no change needed now

## Confidentiality check

- [ ] No customer document content, prompts, names, identifiers or screenshots
- [ ] Customer named only if the agreement allows it
- [ ] Reproduction uses synthetic data only
- [ ] Checked by the engagement lead
````
