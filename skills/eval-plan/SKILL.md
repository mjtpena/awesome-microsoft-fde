---
name: eval-plan
description: "Write an evaluation plan for an AI agent: golden set built with the customer, metrics scored separately for retrieval and generation, a release bar, when evaluations run and a results log. Use before tuning any prompt, and run it on every change."
---

# Evaluation Plan

> Part of the [skills](../README.md) in the [Awesome Microsoft FDE](../../README.md) guide. **Step:** 3 Design (written), 4–5 Build and harden (run on every change) · **Pillar:** [5 AI applications](../../docs/pillars/05-ai-applications.md)

How you'll prove the AI is good enough to ship. If you can't measure it, you can't ship it. See [Pillar 5](../../docs/pillars/05-ai-applications.md).

## When to use

- Before tuning any prompt.
- On every pull request (fast subset) and before every release (full set).

## Rules

- Co-write the golden set with the customer's subject-matter experts: they define "good".
- Score retrieval and generation separately. If retrieval fails, no prompt change will help. 💬
- Add every real production failure to the golden set.
- A release below the bar is blocked.

## Steps

1. Write the [template](#template) to `docs/quality/eval-plan.md` and create the golden set file next to it in the repository.
2. Agree the release bar for each metric with the sponsor and record it.
3. Keep the scenario section for this engagement and delete the rest.
4. Wire the evaluation into the pipeline as described under "When it runs".
5. Log every run in the results table.

Write everything into the customer's repository, not your own drive. Everything you write belongs to the customer. Delete sections that don't apply: a short, filled-in document beats a long, empty one.

## Scenarios

Used in every scenario. **Critical** in: [knowledge assistant](../scenario-knowledge-assistant/SKILL.md), [action-taking agent](../scenario-action-agent/SKILL.md), [data agent](../scenario-data-agent/SKILL.md). Those packs say what to add.

## Template

Write everything inside the block below to the file named in the steps, then fill it in.

````markdown
# Evaluation Plan: <Agent / System name>

## Golden set

| Item | Detail |
|---|---|
| Size | 50–200 cases to start |
| Written by | Customer subject-matter experts + FDE |
| Mix | Common questions (60%) · hard or multi-part (20%) · should refuse or escalate (10%) · adversarial (10%) |
| Stored where | In the repository, versioned |
| Refreshed how | Add every real failure from production |

Case format:

| ID | Input | Expected answer / action | Source document(s) or expected query | Category | Must refuse? |
|---|---|---|---|---|---|

## Metrics and release bar

| Metric | What it checks | Release bar | Measured by |
|---|---|---|---|
| Retrieval | Did search find the right passage or table? | | |
| Faithfulness / groundedness | Is the answer supported by what was retrieved? | | |
| Correctness | Does it match the expected answer? | | |
| Task completion / adherence | Did the agent do what was asked, within its instructions? | e.g. ≥ 85% | |
| Tool-call accuracy | Right tool, right arguments? | | |
| Safety | Refuses harmful or out-of-scope requests | | |
| Latency (p95) | | e.g. ≤ 8 s | |
| Cost per conversation | | | |

💬 Score retrieval and generation separately. If retrieval fails, no prompt change will help.

<!-- Microsoft: Foundry agent evaluators act like pass/fail unit tests; Microsoft's example release bar is 85% Task Adherence.
     If the agent uses the Azure AI Search tool, avoid groundedness and tool-call evaluators; put retrieved content in the
     dataset as `context` and use Retrieval / Document Retrieval evaluators instead.
     See docs/microsoft-technical-reference.md#evaluation--agentops -->

## When it runs

- [ ] On every pull request (subset, fast)
- [ ] Before every release (full set; blocks release if below the bar)
- [ ] Nightly or weekly on production samples
- [ ] Red-team scan before launch and on a schedule after

## Scenario sections

### Knowledge assistant
- Measure citation correctness: does the cited passage actually support the claim?
- Include questions whose answer is **not** in the documents; the right answer is "I don't know".
- Run the set as a low-privilege user and confirm restricted content never appears.

### Action agent
- For each write action: correct tool, correct arguments, approval requested, and correct behaviour when the tool fails.
- Include requests that should be declined or escalated to a human.

### Data agent
- Compare numbers against a trusted report, not just "looks plausible".
- Include ambiguous questions; the right behaviour is to ask which definition the user means.

### Disconnected
- The evaluation must run on site with local models; confirm the tooling works without internet.

## Results log

| Date | Version | Retrieval | Faithfulness | Task | Safety | p95 latency | Cost / conv. | Pass? |
|---|---|---|---|---|---|---|---|---|
````
