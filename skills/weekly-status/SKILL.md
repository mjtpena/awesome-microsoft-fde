---
name: weekly-status
description: "Write a one-page weekly status after the Friday demo: overall RAG status, one-sentence summary, what was shown, decisions needed with dates, risks and blockers, next week, and field notes for the product team. Use every week of an engagement."
---

# Weekly Status

> Part of the [skills](../README.md) in the [Awesome Microsoft FDE](../../README.md) guide. **Step:** Every week, after the Friday demo · **Pillar:** [6 Consulting and delivery](../../docs/pillars/06-consulting-and-delivery.md)

One page that tells the sponsor whether to worry, even if they only read the first three lines.

## When to use

- Every week, the same day as the demo.

## Rules

- One page. Send it the same day.
- Lead with the overall status and what changed.
- Every decision you need has an owner and a date.
- Record field notes for the product team: that loop is part of the job.

## Steps

1. Write the [template](#template) to `docs/engagement/status/week-<N>.md` in the customer's repository.
2. Fill the first three lines last, once you know the whole picture.
3. Pull risks from the previous week's status and update them rather than starting fresh.
4. Carry unresolved blockers from the [access request](../access-request/SKILL.md).

Write everything into the customer's repository, not your own drive. Everything you write belongs to the customer. Delete sections that don't apply: a short, filled-in document beats a long, empty one.

## Scenarios

Used in every scenario. Each [scenario pack](../README.md#scenario-packs) says what to add.

## Template

Write everything inside the block below to the file named in the steps, then fill it in.

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

## Field notes for the product team

| What broke or was missing | Workaround | Seen before? | Suggested fix |
|---|---|---|---|
````
