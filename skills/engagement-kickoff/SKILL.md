---
name: engagement-kickoff
description: "Write the engagement charter for day 0 and week 1: the problem in one sentence, the success measure and who judges it, scope in and out, the exit date and what done means, team and cadence, working agreements, how decisions are made, the escalation path and the first two weeks' plan. Use before the access request and discovery, and revisit whenever scope changes."
---

# Engagement Kickoff

> Part of the [skills](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/skills/README.md) in the [Awesome Microsoft FDE](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/README.md) guide. **Step:** 0–1 Kickoff, before the access request and discovery · **Pillar:** [6 Consulting and delivery](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/docs/pillars/06-consulting-and-delivery.md)

The charter you agree with the sponsor in the first meeting. It says why you're here, when you leave and what has to be true when you do. Everything later in the engagement (the [use-case canvas](../ai-use-case-canvas/SKILL.md), the [weekly status](../weekly-status/SKILL.md), the [handover](../handover/SKILL.md)) is measured against it. See a [filled-in example](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/examples/knowledge-assistant/engagement-kickoff.md) for a fictional knowledge assistant.

## When to use

- Day 0: draft it from the sales notes and the first call, before you send the [access request](../access-request/SKILL.md).
- Week 1: walk through it at the kickoff meeting and get the sponsor to agree it.
- Whenever scope, the exit date or the team changes: update it and log the change at the bottom.

## Rules

- **Agree the exit date and exit criteria on day one.** An engagement without a leaving date becomes staff augmentation. 💬
- **Done means running in their environment, proven by tests, with a named owner.** A demo on your laptop is not done.
- **One sponsor judges success.** Name them. A committee can't sign anything off.
- **Write "out of scope" down.** The most useful line in the charter is the thing you agreed not to build.
- **Code lives in the customer's repository from the first commit, and the customer owns everything you write.** No private forks, no "we'll move it later".
- **Every decision has a forum and every blocker has an escalation path,** agreed before you need them.
- Keep it to two pages. If it's longer, the detail belongs in the canvas or an ADR (architecture decision record).

## Steps

1. Write the [template](#template) to `docs/engagement/charter.md` in the customer's repository. If you have no repository access yet, draft it in a shared document and move it on the first day you do.
2. Fill the problem, the success measure and the scope from the sales notes and the first sponsor call. Mark anything you're guessing as "to confirm in discovery".
3. Set the exit date and copy the core exit criteria. Add the customer-specific ones with the sponsor.
4. Name the team on both sides, including the person who will own the system after you leave. If nobody is named yet, record that as the first risk.
5. Agree the cadence, working agreements, decision forums and escalation path in the kickoff meeting. Don't negotiate them by email.
6. Write the first two weeks' plan so it ends with the canvas signed. Link the access request and the discovery interview schedule.
7. Get the sponsor to agree it in writing. Revisit it in the week-2 status and at every scope change; log each change at the bottom.

Write everything into the customer's repository, not your own drive. Everything you write belongs to the customer. Delete sections that don't apply: a short, filled-in document beats a long, empty one.

## Scenarios

Used in every scenario. Each [scenario pack](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/skills/README.md#scenario-packs) says what to add; the add-ons at the end of the template cover the common ones.

## Template

Write everything inside the block below to the file named in the steps, then fill it in.

````markdown
# Engagement Charter: <Customer> · <Engagement name>

**Version:** · **Agreed by (sponsor):** · **Date agreed:**

## 1. Why we're here

| Field | Answer |
|---|---|
| Problem in one sentence | |
| Who has the problem, and how many of them | |
| What it costs today (time, errors, money, risk) | To confirm in discovery |
| Success measure and target | e.g. median time to a cited answer under 2 minutes within one quarter of go-live |
| Who judges success | <one named sponsor> |
| How and when it's measured | |

## 2. Scope

| In scope | Out of scope (and why) |
|---|---|
| | |

Anything not listed as in scope is out until the sponsor agrees a change (see section 9).

## 3. When we leave, and what "done" means

**Exit date:** <date> · **Go-live target:** <date>

Done means all of these are true:

- [ ] Running in the customer's environment, deployed from code in the customer's repository
- [ ] Automated tests and the evaluation gate prove it meets the agreed release bar
- [ ] Security and privacy sign-off recorded
- [ ] A named owner at the customer has run it without us for at least one week
- [ ] Runbook and handover accepted by the owner
- [ ] <customer-specific criterion>

## 4. Team and cadence

| Name | Organisation | Role in this engagement | Time on it |
|---|---|---|---|
| | Customer | Sponsor | |
| | Customer | Owner after handover | |
| | Customer | Subject-matter expert | |
| | Customer | Security contact | |
| | Delivery team | Lead FDE | |
| | Delivery team | FDE | |

| Ritual | When | Who | Output |
|---|---|---|---|
| Demo on real data | Every Friday | Sponsor, users, team | Feedback and decisions |
| Weekly status | Friday, after the demo | Sponsor | One page in `docs/engagement/status/` |
| Stand-up | Daily, 15 minutes | Delivery team and customer engineers | |
| Security check-in | Fortnightly | Security contact | Updated threat model |
| Steering | Monthly, or at a milestone | Sponsor and their manager | Scope and exit decisions |

## 5. Working agreements

- Code, infrastructure and documents live in the customer's repository from the first commit. The customer owns everything we write.
- We work in the customer's tenant, with least-privilege, time-limited access requested in one access request.
- Every important technical decision is recorded as an ADR in the repository.
- We demo on real data, not slides.
- Customer engineers pair with us from week one, so the owner has seen every part before handover.
- <how we handle customer data, working hours, where we sit, tools we may use>

## 6. How decisions get made

| Kind of decision | Who decides | Who's consulted | Where it's recorded |
|---|---|---|---|
| Scope, exit date, success measure | Sponsor | Lead FDE | This charter (section 9) |
| Architecture and platform | | Security, owner | ADR |
| Security and residual risk | | | Threat model |
| Data access and use | | | Access request, data audit |
| Go / no-go | Sponsor | Security, owner | Go-live readiness |

## 7. Escalation path

| Level | Who | When to use it | Expected response |
|---|---|---|---|
| 1 | Named approver for the blocked item | Any blocker | 2 working days |
| 2 | Sponsor | Blocked for more than 2 working days, or a decision not made by its date | 1 working day |
| 3 | Sponsor's manager and delivery team's manager | Exit date or success measure at risk | At the next steering |

## 8. First two weeks

| Day / week | What happens | Who | Output |
|---|---|---|---|
| Day 0 | Charter drafted; access request sent | Lead FDE | `charter.md`, `access-request.md` |
| Week 1 | Kickoff; discovery interviews; stakeholder map | | Interview notes, stakeholder map |
| Week 1, Friday | First demo (even if it's a spike on sample data); first status | | `status/week-1.md` |
| Week 2 | Data audit started; draft architecture and threat model; first ADRs | | |
| Week 2, Friday | Use-case canvas signed by the sponsor | Sponsor | `use-case-canvas.md` |

## 9. Risks we already know about

| Risk | Impact | Mitigation | Owner |
|---|---|---|---|
| Access takes longer than planned | | Access request on day 0; escalate at day 3 | |
| No named owner after handover | | | Sponsor |

## Change log

| Version | Date | What changed | Agreed by |
|---|---|---|---|

## Scenario add-ons

- **Action agent:** list every action in or out of scope, and who must approve an action before go-live.
- **Regulated:** name the risk owner, privacy officer and any external assessor; add the review lead times to the first two weeks' plan.
- **Disconnected:** where the team works, how code and models get in and out, and clearance or device requirements for each person.
````
