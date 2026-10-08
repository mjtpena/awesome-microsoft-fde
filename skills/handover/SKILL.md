---
name: handover
description: "Document an engagement handover: what was delivered, results against exit criteria, evaluation baseline, RACI, named owner, knowledge transfer, ranked backlog, accepted risks, and known product issues with workarounds. Use from week one and complete when the customer's owner has run the system alone for a week."
---

# Handover

> Part of the [skills](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/skills/README.md) in the [Awesome Microsoft FDE](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/README.md) guide. **Step:** 6 Hand over · **Pillar:** [6 Consulting and delivery](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/docs/pillars/06-consulting-and-delivery.md)

Proof the customer can run the system without you. You've succeeded when they don't call you for routine work.

## When to use

- Start in week one and fill it in as you go.
- Complete at the end of the engagement.

## Rules

- Handover is complete when the named owner has operated the system **without you for at least one week**. Signing the document isn't the finish line; that week is.
- Results are measured against the exit criteria in the [use-case canvas](../ai-use-case-canvas/SKILL.md).
- The evaluation baseline becomes the customer's alert threshold.
- Tell the customer about known product issues that affect them, with the workaround and a public tracking link where one exists. Your internal feedback to the product team stays in your internal [field notes](../weekly-status/SKILL.md), not here. 💬

## Steps

1. Write the [template](#template) to `docs/engagement/handover.md` in the customer's repository.
2. Link each delivered item to its location as it's created.
3. Copy the exit criteria from the use-case canvas and fill in evidence.
4. Record the evaluation baseline from the latest [evaluation](../eval-plan/SKILL.md) results log.
5. Fill the RACI with named people, not teams, then record the week the owner ran it alone.
6. From your internal field notes, copy only the product issues the customer needs to know about into "Known product issues": the symptom, the workaround, and a public link if there is one.

Write everything into the customer's repository, not your own drive. Everything you write belongs to the customer. Delete sections that don't apply: a short, filled-in document beats a long, empty one.

## Scenarios

Used in every scenario. Each [scenario pack](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/skills/README.md#scenario-packs) says what to add.

## Template

Write everything inside the block below to the file named in the steps, then fill it in.

````markdown
# Handover: <Engagement>

## What was delivered

| Item | Location | Status |
|---|---|---|
| Running system (production) | | |
| Source code and infrastructure-as-code | | |
| Pipelines | | |
| ADRs | `docs/adr/` | |
| Threat model | | |
| Evaluation plan and golden set | | |
| Runbook | | |
| Cost model | | |

## Results against the exit criteria

| Exit criterion (from the use-case canvas) | Target | Achieved | Evidence |
|---|---|---|---|
| Business measure | | | |
| Evaluation release bar | | | |
| Security sign-off | | | |
| Deployed from code in the customer's environment | | | |

## Evaluation baseline

The scores at handover. If future scores fall below these, quality has dropped.

| Metric | Baseline | Alert if below |
|---|---|---|

## RACI

| Activity | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| Day-to-day operation | | | | |
| Incidents | | | | |
| Releases and evaluation | | | | |
| Knowledge / data refresh | | | | |
| Access reviews | | | | |
| Cost management | | | | |
| Security monitoring | | | | |

**Named owner:** ______ · **Operated the system alone from:** ______ **to:** ______

## Knowledge transfer

| Session | Audience | Date | Recording / notes |
|---|---|---|---|
| Architecture walkthrough | | | |
| Runbook drill (simulated incident) | | | |
| Evaluation and release process | | | |

## Backlog (ranked)

| # | Item | Why it matters | Effort |
|---|---|---|---|

## Known issues and accepted risks

| Issue / risk | Impact | Accepted by | Review date |
|---|---|---|---|

## Known product issues and workarounds

| Issue | Affects | Workaround | Public tracking link (if any) |
|---|---|---|---|

**Accepted by (customer owner):** · **Date:**
````
