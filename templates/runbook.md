# Runbook: <Agent / System name>

> **Step:** 6 Hand over (start writing in step 4) · **Pillar:** 1 Software engineering · **Scenarios:** all (critical for action agent and disconnected)
>
> **How to use:** written for the person on call at 2 a.m. who didn't build this. Test it by having someone else follow it to fix a simulated incident. If they need to ask you anything, the runbook isn't finished.

**Owner:** · **On-call / support group:** · **Last tested:** · **Repository:**

## What it is

One paragraph: what the system does, who uses it, and what happens to them if it's down.

```mermaid
flowchart LR
    U["Users"] --> CH["Channel"] --> GW["Gateway"] --> AG["Agent"] --> DEP["Models · tools · data"]
```

## Where things are

| Component | Resource / location | Dashboard | Logs |
|---|---|---|---|

## Routine operations

| Task | How often | Steps / command | Who |
|---|---|---|---|
| Deploy a new version | | Run pipeline `<name>` | |
| Run the evaluation set | Before each release | | |
| Refresh / re-index knowledge | | | |
| Rotate or review access | | | |
| Review cost against budget | Monthly | | |
| Add production failures to the golden set | Weekly | | |

## Health checks

| Signal | Normal | Alert threshold | Dashboard |
|---|---|---|---|
| Error rate | | | |
| p95 latency | | | |
| Token spend per day | | | |
| Evaluation score (scheduled) | | | |

## Incidents

| Symptom | Likely cause | Check | Fix |
|---|---|---|---|
| Users get errors | Gateway limits, model quota, expired permission | Gateway and agent logs | |
| Answers suddenly worse | Stale or failed index refresh; changed source documents; model version change | Evaluation run, index status | |
| Can't connect after a network change | Private DNS or firewall rule | Name resolution from the workload network | |
| Spend spike | Loop, abuse or traffic growth | Token usage by caller | |
| Agent took a wrong action (action agents) | | Audit log | Use the kill switch, then roll back |

## Kill switch

How to disable the agent immediately, who's allowed to, and how to turn it back on:

## Rollback

How to return to the previous version:

## Scenario sections

- **Knowledge assistant:** how to re-index one source; how to remove a document urgently (for example, one that was shared by mistake).
- **Action agent:** how to find and reverse every action from a given time window.
- **Data agent:** how to check whether a wrong number is a data problem or an agent problem.
- **Disconnected:** offline update procedure step by step; how to collect diagnostics without internet; local contacts.

## Escalation

| Level | Who | When | Contact |
|---|---|---|---|
