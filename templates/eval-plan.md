# Evaluation Plan: <Agent / System name>

> **Step:** 3 Design (written), 4–5 Build and harden (run on every change) · **Pillar:** 5 AI applications · **Scenarios:** all (critical for knowledge, action and data agents)
>
> **How to use:** write this before tuning any prompt. The golden set is co-written with the customer, because they define "good". See [Pillar 5](../docs/pillars/05-ai-applications.md).

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
