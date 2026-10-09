# Engagement Charter: Harbourline Insurance · Policy Assistant

> **Worked example.** A filled-in [`engagement-kickoff`](../../skills/engagement-kickoff/SKILL.md) charter for a fictional engagement; see [examples](../README.md). Everything below, including names and systems, is invented. In the customer's repository this is `docs/engagement/charter.md`.

**Version:** 1.1 (after the week-3 scope reset) · **Agreed by (sponsor):** D. Whitfield (Head of Claims Operations) · **Date agreed:** week 1, Monday, at kickoff (version 1.0); re-agreed week 3, Friday (version 1.1)

Drafted by E. Marsh on week 0, day 1, from the sales notes and a 30-minute call with D. Whitfield, and sent the same day as the [access request](access-request.md). Walked through line by line at Monday's kickoff. The change log at the bottom shows what moved since.

## 1. Why we're here

| Field | Answer |
|---|---|
| Problem in one sentence | Claims handlers spend too long finding the current version of a policy, and too often cite a superseded one |
| Who has the problem, and how many of them | About 900 claims handlers, Motor and Property first. Team leaders answer the same policy questions over and over |
| What it costs today (time, errors, money, risk) | Version 1.0 said "to confirm in discovery". Confirmed in week 1: a median of **22 minutes** per complex claim spent finding the right policy (30 handlers shadowed for a day); **1 in 12** sampled claim decisions in the quality team's quarterly audit cited a superseded version |
| Success measure and target | Median time to a cited policy answer **under 2 minutes**, and superseded-policy citations in the quarterly audit **halved**, within one quarter of go-live. Signed in the [use-case canvas](ai-use-case-canvas.md) |
| Who judges success | D. Whitfield |
| How and when it's measured | Time: the same shadowing method on a sample of handlers, one quarter after go-live. Citations: the quality team's next quarterly audit sample, tagged the same way as the baseline |

## 2. Scope

| In scope | Out of scope (and why) |
|---|---|
| An assistant in Teams that answers policy questions and cites the policy, section and effective date it used | Any change to a policy, claim or system. The assistant answers; it changes nothing (later recorded in ADR-004) |
| Internal claims handlers, Motor and Property first, starting with a pilot group led by M. Costa | **Customer-facing version in the claims portal.** In scope at version 1.0; moved out at the [scope reset](scope-reset.md) in week 3. In the backlog with its own trigger |
| Sources: the Claims Policy, Underwriting and Pricing SharePoint sites (Pricing only after its permissions are fixed) and the file share's `published` folder | **All 4,000 staff.** In scope at version 1.0; moved out in week 3 for lack of discovery evidence and the Pricing oversharing |
| Ingestion, the agent, the evaluation gate, the gateway policies and the infrastructure, all deployed from code | Lines of business other than Motor and Property in release 1 |
| Runbook, handover and pairing with the platform team | Rewriting or cleaning the source documents. A. Novak's team owns the content; we report what we find |

Anything not listed as in scope is out until D. Whitfield agrees a change (see the change log).

## 3. When we leave, and what "done" means

**Exit date:** end of week 10 · **Go-live target:** week 9

Done means all of these are true:

- [ ] Running in Harbourline's Azure subscription, deployed by their pipeline from code in their `policy-assistant` repository
- [ ] Automated tests and the evaluation gate prove it meets the release bar D. Whitfield agrees in week 2, including a low-privilege run that returns no pricing-draft content
- [ ] Security sign-off from R. Okafor and responsible AI and privacy sign-off from F. Lindqvist
- [ ] S. Adeyemi's platform team has run it without us for at least one week
- [ ] [Runbook](runbook.md) and [handover](handover.md) accepted by S. Adeyemi (technical) and D. Whitfield (business)
- [ ] Baselines for both success measures recorded before go-live, so the measurement a quarter later has something to compare against

## 4. Team and cadence

| Name | Organisation | Role in this engagement | Time on it |
|---|---|---|---|
| D. Whitfield | Harbourline | Sponsor; business owner after handover | Friday demo, plus one hour a week |
| S. Adeyemi | Harbourline | Platform team lead; technical owner after handover | Two engineers pairing from week 4 |
| M. Costa | Harbourline | Subject-matter expert (Motor claims); co-writes the golden set; leads the pilot group | Half a day a week; more in weeks 4–5 |
| A. Novak | Harbourline | Subject-matter expert (underwriting); decides which policy version is current | Half a day a week |
| R. Okafor, J. Tan | Harbourline | Security Architect; Identity Lead | Fortnightly security check-in |
| F. Lindqvist | Harbourline | Data Protection Officer; responsible AI and privacy sign-off | Weeks 2, 5 and 7 |
| E. Marsh | Delivery team | Lead FDE | Full time, on site Monday to Wednesday |
| T. Osei | Delivery team | FDE | Full time |
| Product engineer | Delivery team (vendor side) | Pairs on the agent and evaluation code | Part time |

The full list of approvers is in the [stakeholder map](stakeholder-map.md).

| Ritual | When | Who | Output |
|---|---|---|---|
| Demo on real data | Every Friday, 14:00, 30 minutes | D. Whitfield, M. Costa, A. Novak, S. Adeyemi, delivery team | Feedback and decisions |
| Weekly status | Friday, after the demo | D. Whitfield; copied to the approvers | One page in `docs/engagement/status/` ([example](weekly-status.md)) |
| Stand-up | Daily, 09:15, 15 minutes | Delivery team; platform engineers from week 4 | |
| Security check-in | Fortnightly, Wednesday | R. Okafor, J. Tan | Updated [threat model](threat-model.md) |
| Architecture review board | Fortnightly; papers five working days before | R. Okafor chairs | ADR approvals |
| Steering | Week 3, week 6 and the go-live decision | D. Whitfield and their director | Scope and exit decisions |

## 5. Working agreements

- Code, infrastructure, prompts, evaluation data and documents live in Harbourline's `policy-assistant` repository from the first commit. Harbourline owns everything we write.
- We work in Harbourline's tenant with corporate accounts, least-privilege and time-limited roles, all requested in one [access request](access-request.md). No production data leaves Harbourline's environment.
- Every important technical decision is an ADR (architecture decision record) in the repository, approved through the board where R. Okafor says it must be.
- We demo on real data from the first week we have access. Until then we say so and show what we have.
- Platform engineers pair with us from week 4, so S. Adeyemi's team has deployed, re-indexed and rolled back the system before handover.
- Anything we learn about product gaps goes to our own team's notes, not into Harbourline's repository; known issues that affect Harbourline go into the handover.

## 6. How decisions get made

| Kind of decision | Who decides | Who's consulted | Where it's recorded |
|---|---|---|---|
| Scope, exit date, success measure | D. Whitfield | E. Marsh, M. Costa | This charter and the canvas |
| Architecture and platform | R. Okafor, at the architecture review board | S. Adeyemi, J. Tan | ADRs |
| Security and residual risk | R. Okafor | J. Tan; D. Whitfield for data leakage | Threat model |
| Which policy version is current | A. Novak | M. Costa | ADR-003 |
| Anything that touches Pricing content | G. Patel | L. Moreau | Data audit |
| Responsible AI and privacy | F. Lindqvist | D. Whitfield | [Impact assessment](responsible-ai-impact-assessment.md) |
| Go / no-go | D. Whitfield | R. Okafor, F. Lindqvist, S. Adeyemi | [Go-live readiness](go-live-readiness.md) |

## 7. Escalation path

| Level | Who | When to use it | Expected response |
|---|---|---|---|
| 1 | The named approver for the blocked item | Any blocker | 2 working days |
| 2 | D. Whitfield | Blocked for more than 2 working days, or a decision missed its date | Raised at the next claims leadership meeting |
| 3 | D. Whitfield's director and the delivery team's engagement manager | Exit date or success measure at risk | At the next steering |

💬 We used level 2 in week 1: production data approval was stuck after three emails, and one line on D. Whitfield's leadership agenda moved it. See the [access request](access-request.md).

## 8. First two weeks

| Day / week | What happens | Who | Output |
|---|---|---|---|
| Week 0, day 1 | Charter drafted; access request sent to D. Whitfield | E. Marsh | `charter.md`, `access-request.md` |
| Week 1, Monday | Kickoff: this charter agreed | D. Whitfield, all named above | Charter version 1.0 |
| Week 1, days 2–4 | Discovery interviews; a day shadowing 30 handlers | E. Marsh, T. Osei | [Discovery notes](discovery-interview.md) |
| Week 1, Friday | First demo: a throwaway agent on 20 public sample documents; first status | Delivery team | `status/week-1.md` |
| Week 2 | Data audit across all four sources; ADRs 001–006 drafted; threat model to version 0.3; first evaluation plan | Delivery team, A. Novak, R. Okafor | [Data audit](data-audit.md), ADRs, [threat model](threat-model.md), [evaluation plan](eval-plan.md) |
| Week 2, Wednesday | Use-case canvas signed | D. Whitfield | [Canvas](ai-use-case-canvas.md) version 1 |

## 9. Risks we already know about

| Risk | Impact | Mitigation | Owner |
|---|---|---|---|
| Production data approval takes longer than a week | No real documents for the data audit | Access request on day 0; escalate at day 3; work on a hand-exported sample meanwhile | D. Whitfield |
| No reliable "current version" flag on the Claims Policy site (raised on the sales call) | Wrong answers from superseded policies: the problem we're here to fix | Data audit counts duplicates in week 2; A. Novak proposes a version rule | A. Novak |
| Portal and all-staff scope in ten weeks | Too much to test properly before go-live | Revisit after the data audit, at the week-3 steering | D. Whitfield |

## Change log

| Version | Date | What changed | Agreed by |
|---|---|---|---|
| 1.0 | Week 1, Monday | First agreed version. The claims-portal version for policyholders was added in the meeting at the request of D. Whitfield's director, so scope was all 4,000 staff in Teams plus policyholders in the portal | D. Whitfield |
| 1.1 | Week 3, Friday | **Scope reset.** Release 1 narrowed to internal claims handlers, Motor and Property first. Portal and all-staff access moved to out of scope, with backlog triggers. Exit date, go-live week, success measure and exit criteria unchanged. Problem costs filled in from discovery. See the [scope reset](scope-reset.md) | D. Whitfield |
