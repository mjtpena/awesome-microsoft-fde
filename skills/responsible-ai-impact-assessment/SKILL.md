---
name: responsible-ai-impact-assessment
description: "Write a responsible AI impact assessment for the customer's privacy and responsible AI reviewers: intended and out-of-scope uses, affected stakeholders, potential harms (quality of service, allocation, overreliance, privacy, transparency), mitigations and how each is tested, human oversight, what users are told, data handling and sign-off. Use in design, alongside the threat model, and update before go-live; critical in regulated engagements."
---

# Responsible AI Impact Assessment

> Part of the [skills](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/skills/README.md) in the [Awesome Microsoft FDE](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/README.md) guide. **Step:** 3 Design (drafted), 5 Harden (signed) · **Pillars:** [4 Security and identity](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/docs/pillars/04-security-and-identity.md), [5 AI applications](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/docs/pillars/05-ai-applications.md)

The document the customer's privacy officer and responsible AI reviewers sign. The [threat model](../threat-model/SKILL.md) asks "what can an attacker make it do?"; this asks "who could it hurt when it works as designed, or fails?". The structure follows the shape of Microsoft's published Responsible AI Impact Assessment template, linked from the [technical reference](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/docs/microsoft-technical-reference.md#responsible-ai). If the customer has their own template, use theirs and map these sections onto it. See a [filled-in example](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/examples/knowledge-assistant/responsible-ai-impact-assessment.md) for a fictional knowledge assistant.

## When to use

- Week two or three, once the [use-case canvas](../ai-use-case-canvas/SKILL.md) says who uses the system and for what.
- Again before go-live, with real evaluation and red-team results in the "tested how" column.
- Whenever an intended use, a user group, a data source or the model changes.

## Rules

- **Find the reviewer in week one.** Ask who signs responsible AI and privacy, what they need and how long they take. Their lead time goes in the plan. 💬
- **Describe intended uses precisely:** who uses it, for what task, in what setting. "Answers questions" is not an intended use.
- **Write the out-of-scope uses as firmly as the in-scope ones,** and say how the system discourages them.
- **Every harm gets a mitigation and a test.** A mitigation with no test is a hope. Link each test to the [evaluation plan](../eval-plan/SKILL.md) or the [red-team](../red-team/SKILL.md) report.
- **Name the human who decides.** If a person must check the output before acting on it, say who, and how the design makes that easy.
- **Tell users it's AI.** Users are told they're talking to an AI system, what it can't do, and that they must check the cited source before acting.
- A reviewer, not the delivery team, signs it. Record who, when and any conditions.

## Steps

1. Write the [template](#template) to `docs/responsible-ai/impact-assessment.md` in the customer's repository.
2. Copy the problem, users and scope from the canvas into section 1. List intended uses one row each.
3. List out-of-scope and restricted uses, and anything that would make this a sensitive use under the customer's policy (decisions about people's jobs, money, health, legal status or access to services).
4. For each intended use, list the stakeholders, including people who never touch the system but are affected by its output.
5. Go through every harm row. Mark "doesn't apply" with a reason rather than deleting it.
6. For each mitigation, write how it's tested and the pass bar. Fill "Result" from the latest evaluation and red-team runs.
7. Fill human oversight, transparency and data handling with the owners who'll run them after handover.
8. Book the review. Record the decision, conditions and the date of the next review.

Write everything into the customer's repository, not your own drive. Everything you write belongs to the customer. Delete sections that don't apply: a short, filled-in document beats a long, empty one.

## Scenarios

Used in every scenario. **Critical** in: [regulated, private-only](../scenario-regulated-private/SKILL.md). Important in the [action-taking agent](../scenario-action-agent/SKILL.md) pack, where the harm from a wrong action is larger. The add-ons at the end of the template say what to add.

## Template

Write everything inside the block below to the file named in the steps, then fill it in.

````markdown
# Responsible AI Impact Assessment: <Agent / System name>

**Version:** · **Date:** · **Prepared by:** · **Reviewed by (privacy / responsible AI):**

## 1. The system

| Field | Answer |
|---|---|
| What it does, in one sentence | |
| Who uses it, and how many | |
| Where users meet it | Teams / web app / Microsoft 365 Copilot / other |
| Does it write or change anything? | No / Yes: list actions |
| Model(s) and where they run | |
| Knowledge and data sources | |
| Related documents | Use-case canvas, threat model, evaluation plan, red-team report |

## 2. Intended uses

One row per use. A use is who, doing what task, in what setting.

| ID | Who | Task | Setting | Benefit |
|---|---|---|---|---|
| U1 | | | | |

## 3. Out-of-scope, restricted and sensitive uses

| Use | Why it's out of scope | How the system discourages or prevents it |
|---|---|---|
| | | |

**Sensitive use check:** does any output feed a decision about a person's employment, finances, health, legal status or access to a service? <No / Yes: describe, and the extra review it triggers>

## 4. Stakeholders

| Stakeholder | Uses it directly? | How they're affected | Potential benefit | Potential harm |
|---|---|---|---|---|
| Primary users | Yes | | | |
| People the output is about or applied to | No | | | |
| Owners of the source content | No | | | |
| Operators and support | | | | |

## 5. Potential harms, mitigations and tests

| Harm | Applies? | How it could happen here | Mitigation | Tested how (pass bar) | Result | Residual risk and who accepts it |
|---|---|---|---|---|---|---|
| Quality of service (works worse for some groups, languages, regions or document types) | | | | | | |
| Allocation (output influences who gets a resource, opportunity or outcome) | | | | | | |
| Overreliance (users act on a wrong answer without checking) | | | | | | |
| Privacy (exposes personal or confidential data, or data to the wrong person) | | | | | | |
| Transparency (users don't know it's AI, what it's based on, or its limits) | | | | | | |
| Harmful or inappropriate content | | | | | | |
| Stereotyping or demeaning output | | | | | | |
| Misuse outside the intended uses | | | | | | |

## 6. Known limitations

| Limitation | Effect on users | What users are told |
|---|---|---|
| | | |

## 7. Human oversight

| Point | Who | What they check | How the design supports it |
|---|---|---|---|
| Before acting on an answer | | | e.g. every answer cites its source with a link |
| Reporting a wrong answer | | | e.g. feedback button routed to the owner |
| Monitoring quality after go-live | | | e.g. weekly sample review; evaluation baseline as alert threshold |
| Turning it off | | | Kill switch in the runbook |

## 8. Transparency to users

- How users are told it's AI:
- What they're told it can and can't do:
- What they're told to do before acting on an answer (for example: open and check the cited source):
- Where they report a problem:
- Where the user guidance lives, and who keeps it current:

## 9. Data handling

| Question | Answer |
|---|---|
| What data the system reads, and its classification | |
| Personal data involved? Lawful basis and purpose | |
| What's logged (prompts, answers, retrieved documents) and who can read the logs | |
| Retention period and who set it | |
| Where data is processed and stored (regions) | |
| Is any data used to train or fine-tune a model? | |
| How a user or data subject request is handled | |

## 10. Sign-off

| Reviewer | Role | Decision | Conditions | Date |
|---|---|---|---|---|
| | Privacy / data protection | Approved / Approved with conditions / Not approved | | |
| | Responsible AI or risk | | | |
| | Business owner | | | |

**Next review:** <date, or the trigger: new intended use, new user group, new data source, model change>

## Scenario add-ons

- **Action agent:** for each action, the harm if it's wrong, whether it's reversible, and the human approval step. Add "harmful action" to section 5.
- **Data agent:** wrong numbers presented with confidence; who checks a figure before it reaches a report or a decision.
- **Regulated:** map each mitigation to the customer's control framework or regulatory obligation; record the risk owner's acceptance.
- **Customer-facing:** how members of the public are told it's AI, accessibility, and the route to a human.
````
