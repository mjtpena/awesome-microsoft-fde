---
name: scope-reset
description: "Reset an AI engagement's scope when discovery, the data audit or early results show the agreed scope won't work: lay out the options (narrow, re-sequence, pivot, stop), decide with evidence, present to the sponsor without losing them, and update the canvas, ADRs and plan. Use in the Understand step, typically weeks 2 to 4, or whenever the evidence changes."
---

# Scope Reset

> Part of the [skills](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/skills/README.md) in the [Awesome Microsoft FDE](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/README.md) guide. **Step:** 2 Understand (typically weeks 2–4), or any time the evidence changes · **Pillar:** [6 Consulting and delivery](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/docs/pillars/06-consulting-and-delivery.md)

A one-page decision paper for the sponsor: here is what we learnt, here is why the agreed scope won't land, here are the options, here is what we recommend. See a [filled-in example](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/examples/knowledge-assistant/scope-reset.md) for a fictional knowledge assistant.

💬 **Our take:** a scope reset in week three is the discovery process working, not failing. The expensive failure is the one nobody calls: ten weeks spent building the original ask, a launch, and a tool nobody uses. Stopping early is a success compared with shipping something nobody uses.

## When to use

- The [data audit](../data-audit/SKILL.md) shows the data can't support the scope: missing, unreadable, overshared, or with no source of truth.
- Discovery shows the business measure in the [use-case canvas](../ai-use-case-canvas/SKILL.md) can't be met by the agreed shape, or the users' real problem is different.
- A scope element changes the risk profile beyond what the engagement can carry in the time: for example customer-facing, regulated, or write actions added to an internal read-only assistant.
- The first evaluation run is far below the bar and the cause is the scope, not the build.
- A blocker (access, approval, an owner who won't engage) will outlast the engagement.

## Rules

- **Raise it as soon as the evidence is solid, not when it's convenient.** Every week you wait costs a week of the engagement and some of the sponsor's trust. Flag it as a risk in the [weekly status](../weekly-status/SKILL.md) the week you suspect it.
- **Evidence, not opinion.** Each reason for the reset points to a finding: a data-audit row, an interview, an evaluation run, a blocked access request. If you can't point to one, you're not ready to reset.
- **Always lay out all four options**, even the ones you don't recommend. A sponsor who sees only one option feels managed; one who sees four, with trade-offs, decides.
- **Lead with what they still get.** The sponsor's measure of success matters more than the original feature list. Show how the recommended option still moves their business measure, and when.
- **No surprises in the room.** Walk the sponsor through it one to one before any wider meeting. Never let them hear it first in front of their own stakeholders.
- **Deferred isn't deleted.** What comes out of scope goes into the backlog with the reason and what would have to be true to bring it back.
- **Write down the decision and everything it changes**: the canvas, the ADRs, the plan, the stakeholder map. An undocumented reset gets re-litigated in week eight.

### The four options

| Option | What it means | Choose it when | Watch out for |
|---|---|---|---|
| Narrow | Same problem, smaller slice: fewer users, sources, document types or channels | The core idea works, but not everywhere at once | Narrowing until the result no longer moves the business measure |
| Re-sequence | Same scope, different order: do the feasible part first, the hard part in a later release | A dependency (data clean-up, an approval, a permission fix) will land, but not in time | Release 2 that never gets funded; agree its trigger now |
| Pivot | A different problem or shape that the evidence shows is more valuable or feasible | Discovery found the real pain is somewhere else | Losing the sponsor, whose mandate was the original problem; check they still own the new one |
| Stop | End or pause the engagement, with findings | No option meets a business measure anyone will fund, or a blocker can't be cleared | Treating it as failure; the findings are the deliverable |

### When stopping is the right answer

Recommend stopping when, on the evidence:

- No narrowed or re-sequenced option moves a business measure the sponsor will still put their name to.
- The data needed doesn't exist, has no owner, and nobody will fund creating it.
- The risk owner (security, data protection, legal) won't accept the residual risk of any option, and won't say what would change their mind.
- The sponsor has gone, and no one else will own the outcome.

A stop paper gives the customer what they learnt, what would have to change for the project to work, and a ranked list of what to fix first. That's worth more to them than a launch nobody uses, and it keeps your credibility for the next engagement. 💬

## Steps

1. Collect the evidence: the data-audit rows, interview notes, evaluation runs or blockers that triggered this.
2. Write the [template](#template) to `docs/engagement/scope-reset-<N>.md` in the customer's repository. Fill the four options honestly, then the recommendation.
3. Check the recommendation against the canvas's business measure and exit criteria. If it changes the measure, say so plainly.
4. Walk the sponsor through it one to one. Adjust the paper with what they tell you about their own stakeholders, using the [stakeholder map](../stakeholder-map/SKILL.md).
5. Present it to the wider group with the sponsor leading or alongside you. Get the decision in writing.
6. Update everything the decision changes, in the same week:
   - [Use-case canvas](../ai-use-case-canvas/SKILL.md): users, sources, shape, out of scope, exit criteria. Bump the version and get it re-signed.
   - [ADRs](../adr/SKILL.md): a new ADR for the scope decision itself, and mark any ADR the change supersedes.
   - [Data audit](../data-audit/SKILL.md): which sources are now in or out.
   - [Evaluation plan](../eval-plan/SKILL.md): remove or add golden-set categories; check the release bar still fits.
   - The plan and the backlog: deferred items, with their trigger to return.
7. Record the decision and the new plan in the next weekly status.

Write everything into the customer's repository, not your own drive. Everything you write belongs to the customer. Delete sections that don't apply: a short, filled-in document beats a long, empty one.

## Scenarios

Used in every scenario. Common triggers:

- **Knowledge assistant:** no source of truth for "current", too many unreadable scans, oversharing that can't be fixed in time, or a customer-facing channel added to an internal assistant.
- **Action-taking agent:** write actions the customer can't approve or reverse safely yet. Re-sequence to read-only or draft-only first.
- **Data agent:** no agreed semantic model or metric definitions. Narrow to one domain with an owner.
- **Regulated:** an approval cycle longer than the engagement. Re-sequence to work the approval in parallel on synthetic data.
- **Disconnected:** a required model or service isn't available in the target environment. Pivot the shape or stop.

## Template

Write everything inside the block below to the file named in the steps, then fill it in.

````markdown
# Scope Reset: <Engagement>

**Date:** · **Week:** · **Raised by:** · **Decision by (sponsor):** · **Status:** Proposed / Agreed / Rejected

## In one sentence

<What we learnt, and what we recommend.>

## What we agreed

| Item | Original scope (canvas version <N>) |
|---|---|
| Users | |
| Sources / data | |
| Shape (answers only / actions / channel) | |
| Business measure and target | |
| Exit criteria | |

## What we found

| Finding | Evidence (link) | Why it matters to the scope |
|---|---|---|

## Options

| Option | What it means here | Business measure: still met? when? | Risk | Effort and time |
|---|---|---|---|---|
| Narrow | | | | |
| Re-sequence | | | | |
| Pivot | | | | |
| Stop | | | | |

## Our recommendation

<The option, why, and what the sponsor still gets and when.>

## What changes

| Document | Change | Owner | Done |
|---|---|---|---|
| Use-case canvas | | | |
| ADRs | New ADR-<N>: <scope decision>; supersedes … | | |
| Data audit | | | |
| Evaluation plan | | | |
| Plan / timeline | | | |
| Stakeholder map | | | |

## Deferred to the backlog

| Item | Why deferred | What would have to be true to bring it back | Owner |
|---|---|---|---|

**Agreed by (sponsor):** · **Date:**
````
