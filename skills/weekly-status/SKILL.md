---
name: weekly-status
description: "Write a one-page weekly status after the Friday demo: overall RAG status, one-sentence summary, what was shown, decisions needed with dates, risks and blockers, next week, plus internal field notes for the product team kept outside the customer's repository. Use every week of an engagement."
---

# Weekly Status

> Part of the [skills](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/skills/README.md) in the [Awesome Microsoft FDE](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/README.md) guide. **Step:** Every week, after the Friday demo · **Pillar:** [6 Consulting and delivery](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/docs/pillars/06-consulting-and-delivery.md)

One page that tells the sponsor whether to worry, even if they only read the first three lines. Plus a running, **internal** log of field notes for the product team.

## When to use

- Every week, the same day as the demo.

## Rules

- One page. Send it the same day.
- Lead with the overall status and what changed.
- Every decision you need has an owner and a date.
- Record field notes for the product team: that loop is part of the job. 💬 Turn each one worth fixing into a [field-feedback](../field-feedback/SKILL.md) report.
- **Field notes stay internal.** They go in your own organisation's engagement workspace, not in the status page or the customer's repository. Share only what the customer's agreement with you allows: describe the problem, not their data.

## Steps

1. Write the [template](#template) to `docs/engagement/status/week-<N>.md` in the customer's repository.
2. Fill the first three lines last, once you know the whole picture.
3. Pull risks from the previous week's status and update them rather than starting fresh.
4. Carry unresolved blockers from the [access request](../access-request/SKILL.md).
5. Append this week's field notes to `field-notes.md` in your team's internal engagement workspace. If there's no internal location, ask; don't put them in the customer's repository.

Delete sections that don't apply: a short, filled-in document beats a long, empty one.

## Scenarios

Used in every scenario. Each [scenario pack](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/skills/README.md#scenario-packs) says what to add.

## Template

Two blocks. Write each to the location named in the steps, then fill it in.

### Customer repository: weekly status

````markdown
# Weekly Status: <Engagement> · Week <N>

**Overall:** 🟢 On track / 🟡 At risk / 🔴 Off track · **Target date:** · **Change since last week:**

**In one sentence:** <what's true now that wasn't true last week>

## What we showed

- Demo: <what, on which data, to whom>
- Measure: <progress on the business target or evaluation score, e.g. golden set 72% → 81%>

## What changed

-

## Decisions needed (with a date)

| Decision | Options | Our recommendation | Needed by | Owner |
|---|---|---|---|---|

## Risks and blockers

| Risk / blocker | Impact | Mitigation | Owner | Since |
|---|---|---|---|---|

## Next week

-
````

### Internal: field notes log

````markdown
# Field Notes: <Customer> / <Engagement>

> Internal to the delivery team. Don't copy into the customer's repository or tenant. Describe problems, not customer data.

| Week | Product / feature | What broke or was missing | Workaround | Seen at other customers? | Suggested fix | Filed where (link) |
|---|---|---|---|---|---|---|
````
