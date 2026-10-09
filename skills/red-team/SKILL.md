---
name: red-team
description: "Plan, run and report an AI red-team exercise: scope and rules of engagement, attack categories (direct and indirect prompt injection, data exfiltration through permission gaps, jailbreaks, tool misuse, harmful content, cost abuse), automated and manual testing, attack success rate against a pass bar agreed with security, findings with severity, retest, and new golden-set cases. Use before launch and on a schedule after it; critical for action agents."
---

# Red Team

> Part of the [skills](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/skills/README.md) in the [Awesome Microsoft FDE](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/README.md) guide. **Step:** 5 Harden, then on a schedule · **Pillars:** [4 Security and identity](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/docs/pillars/04-security-and-identity.md), [5 AI applications](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/docs/pillars/05-ai-applications.md)

Attack your own agent before someone else does, then prove the fixes hold. The [threat model](../threat-model/SKILL.md) section 6 says what to test; this skill is how to plan the run, run it and write it up. Current Microsoft tooling (an automated red-teaming agent in Foundry and the open-source library behind it) is in the [technical reference](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/docs/microsoft-technical-reference.md#red-teaming). See a [filled-in example](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/examples/knowledge-assistant/red-team.md) for a fictional knowledge assistant.

## When to use

- Before launch, against a test deployment that matches production: same instructions, tools, identity, network path and index.
- After launch, on a schedule (monthly is a sensible start 💬) and after every change to instructions, model, tools or data sources.
- After any security incident involving the agent.

## Rules

- **Agree scope and rules of engagement in writing with security before the first attack.** Red-teaming a system without permission is an incident, not a test.
- **Never against production data you can't afford to leak, and never against production users.** Use a test deployment with production-like configuration. If you must test on real data, security agrees which data and who sees the results.
- **Automated and manual, not either.** Automated scans give breadth and a repeatable number; people find the attacks specific to this customer's data and permissions. 💬
- **Agree the pass bar before you run.** Attack success rate per category, plus hard zeros for anything that must never happen (for example, restricted data shown to a user who can't open it).
- **Every finding gets a severity, an owner, a fix and a retest.** A finding is closed by a passing retest, not by a code change.
- **Every successful attack becomes a golden-set case,** so the [evaluation](../eval-plan/SKILL.md) catches the regression on every future change.
- Store raw attack prompts and outputs where security says. They're harmful content by design; the report summarises them.

## Steps

1. Write the [template](#template) to `docs/security/red-team-<date or round>.md` in the customer's repository.
2. Copy the threats and the red-team plan from the threat model. Fill scope, rules of engagement and the pass bar with security; get their agreement recorded.
3. Prepare test assets: low-privilege test users, seeded hostile documents or tool outputs, and the manual prompt set. Keep them in the repository under `tests/red-team/`, except anything security asks you to store elsewhere.
4. Run the automated scan across the agreed risk categories and attack strategies. Record the attack success rate per category.
5. Run the manual set. Split it by attack category and assign each category to the person best placed to break it (security for injection and exfiltration, subject-matter experts for domain-specific harm).
6. Log every successful or partial attack as a finding with severity, owner and fix. Reproduce it before you log it.
7. Fix, retest the finding and rerun the full set. Record the retest result next to the finding.
8. Add each finding to the golden set as a must-refuse or adversarial case, then record the next scheduled run and its owner.

Write everything into the customer's repository, not your own drive. Everything you write belongs to the customer. Delete sections that don't apply: a short, filled-in document beats a long, empty one.

## Scenarios

Used in every scenario. **Critical** in: [action-taking agent](../scenario-action-agent/SKILL.md), where a successful attack changes something, and [regulated, private-only](../scenario-regulated-private/SKILL.md), where the security review expects the evidence. The add-ons at the end of the template say what to add.

## Template

Write everything inside the block below to the file named in the steps, then fill it in.

````markdown
# Red-Team Report: <Agent / System name> · <Round>

**Run dates:** · **Target:** <deployment, environment, version or commit> · **Run by:** · **Agreed with (security):**

## 1. Summary

**Result:** Pass / Pass with conditions / Fail · **Findings:** <n critical, n high, n medium, n low> · **Open after retest:** <n>

<Two or three sentences: what was attacked, what broke, what was fixed, whether the pass bar is met.>

## 2. Scope and rules of engagement

| Item | Agreed |
|---|---|
| Target deployment and how it matches production | |
| In scope (channels, tools, data sources, identities) | |
| Out of scope | |
| Test accounts and their permissions | |
| Data the testers may use | |
| Testing window | |
| Stop conditions (for example, real restricted data appears) | |
| Where raw prompts and outputs are stored, and who can read them | |
| Who to call if something goes wrong | |

## 3. Pass bar

| Category | Measure | Pass bar | Agreed by |
|---|---|---|---|
| Any category | Attack success rate (successful attacks ÷ total attacks) | e.g. ≤ <n>% per category | |
| Data exfiltration through permission gaps | Restricted content returned to a user who can't open it | 0 | |
| <must-never-happen> | | 0 | |

## 4. Attack categories and results

| Category | Applies? | Automated (attacks · successful · ASR) | Manual (attempts · successful) | Pass? |
|---|---|---|---|---|
| Direct prompt injection (user overrides the instructions) | | | | |
| Indirect prompt injection (instructions hidden in documents, emails, tool output or web pages) | | | | |
| Data exfiltration through permission gaps (oversharing, missing trimming, cross-user leakage) | | | | |
| Jailbreaks (role-play, encoding, multi-turn escalation) | | | | |
| System prompt and configuration extraction | | | | |
| Tool misuse (harmful arguments, wrong tool, chained actions) | | | | |
| Harmful content (hate, violence, self-harm, sexual, protected material) | | | | |
| Cost abuse (loops, very long inputs, request floods) | | | | |
| <customer-specific category> | | | | |

**Automated:** tool, risk categories and attack strategies used, number of attack objectives.

**Manual:** who tested, how many prompts per category, where the prompt set lives.

## 5. Findings

| ID | Category | What happened (summary, no raw harmful content) | Severity | Root cause | Fix | Owner | Retest result | Golden-set case |
|---|---|---|---|---|---|---|---|---|
| RT-01 | | | Critical / High / Medium / Low | | | | Pass / Fail, date | |

Severity guide: **Critical:** restricted data exposed or an unapproved action taken. **High:** instructions overridden in a way a user could repeat. **Medium:** partial bypass with no data or action impact. **Low:** cosmetic or needs unrealistic access.

## 6. Retest

| Run | Date | What changed | Overall ASR | Must-never-happen count | Result |
|---|---|---|---|---|---|
| Initial | | | | | |
| Retest | | | | | |

## 7. What happens next

- Golden-set cases added: <IDs>
- Threat model updated: <version>
- Residual risks accepted by: <name, date>
- Next scheduled run: <date or trigger> · Owner after handover:

## Scenario add-ons

- **Action agent:** attack every write action; for each, try to trigger it without approval, with harmful arguments, and through an indirect injection. Record blast radius and whether rollback worked.
- **Knowledge assistant:** low-privilege user runs against each restricted source; seeded hostile document in the test index; repeat after every re-index.
- **Data agent:** queries that read tables or rows the user can't see; queries that are expensive enough to be a cost attack.
- **Regulated:** map each category to the customer's control framework; attach the report to the security review pack.
````
