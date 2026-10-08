---
name: discovery-interview
description: "Run and record a 30–45 minute discovery interview with a sponsor, end user, security person, operator or data owner, ending in a five-whys chain to a business measure. Use in the first weeks of an engagement to understand the problem before designing anything."
---

# Discovery Interview

> Part of the [skills](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/skills/README.md) in the [Awesome Microsoft FDE](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/README.md) guide. **Step:** 2 Understand · **Pillar:** [6 Consulting and delivery](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/docs/pillars/06-consulting-and-delivery.md)

An interview guide and notes sheet for one person. Ask open questions, then ask "why?" again until you reach a number the business cares about.

## When to use

- Weeks one and two, before you commit to a design.
- When a new stakeholder appears or the scope changes.

## Rules

- 30–45 minutes per person.
- Interview at least one sponsor, two end users, one security or risk person and one operator.
- Watching someone do the task beats any interview: ask them to show you.
- Record quotes and observations, then the implication and follow-up for each.

## Steps

1. Write the [template](#template) to `docs/engagement/discovery/<name>.md`, one file per interviewee.
2. Ask which role type the interviewee is and keep only the matching role section plus "For everyone".
3. Add the scenario add-on questions for the engagement's scenario.
4. After the interview, fill the notes table and the five-whys line. Feed the business measure into the [AI use-case canvas](../ai-use-case-canvas/SKILL.md).

Write everything into the customer's repository, not your own drive. Everything you write belongs to the customer. Delete sections that don't apply: a short, filled-in document beats a long, empty one.

## Scenarios

Used in every scenario. Each [scenario pack](https://github.com/mjtpena/awesome-microsoft-fde/blob/main/skills/README.md#scenario-packs) says what to add.

## Template

Write everything inside the block below to the file named in the steps, then fill it in.

````markdown
# Discovery Interview: <Name, role>

**Date:** · **Interviewer:** · **Role type:** Sponsor / End user / Security / Operator / Data owner

## For everyone

1. What does a good outcome look like in six months? How would you measure it?
2. What happens today? Walk me through the last time you did it.
3. What's the most annoying part? What do people do to work around it?
4. What have you tried before? Why didn't it stick?
5. What would make this project fail?

## Sponsor

- Which number do you report upwards that this should move?
- What's the budget for running this after we leave, and who owns it?
- Who could stop this project? Have they been involved?

## End users

- Show me. (Watch the task, note every system and copy-paste.)
- Where do you look for the answer today? How do you know it's right?
- What would make you stop using a new tool after a week?

## Security and risk

- What review does a new AI system go through? How long does it take? What gets rejected?
- Which data classifications are involved, and what rules apply?
- Which identity, network and logging standards must we follow?

## Operator / platform team

- What does your team need to run this: monitoring, runbooks, a specific language or platform?
- How are deployments done here? Who approves production changes?
- What breaks most often in systems like this?

## Data owner

- Where does the data live? How fresh is it? What's wrong with it?
- Who can see it today, and should the AI respect the same permissions?

## Scenario add-ons

- **Knowledge assistant:** What are the top 20 questions people ask? Which documents are the source of truth? How often do they change?
- **Action agent:** Which actions are reversible? What's the cost of a wrong action? Who approves today?
- **Data agent:** Which reports do people trust? Which metric definitions are disputed?
- **Regulated:** Which regulator or framework applies? Who signs the risk acceptance?
- **Disconnected:** How often is the site connected? How do software updates arrive today?

## Notes

| Quote / observation | Implication | Follow-up |
|---|---|---|

**The five whys for this person:** want → why → why → why → why → **business measure:**
````
