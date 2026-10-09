# ADR-004: The assistant is read-only

> **Worked example.** A filled-in [`adr`](../../skills/adr/SKILL.md) for a fictional engagement; see [examples](../README.md). Everything below, including names and systems, is invented. Microsoft product facts follow the [technical reference](../../docs/microsoft-technical-reference.md); check it before relying on them.

- **Status:** Accepted
- **Date:** week 2, day 3
- **Deciders:** D. Whitfield (Head of Claims Operations), R. Okafor (Security Architect), E. Marsh (lead FDE)
- **Pillar(s):** 4 Security · 5 AI · 6 Delivery

## Context

The sponsor's ask is answers with citations; the assistant "only answers; it changes nothing" ([canvas](ai-use-case-canvas.md)). Two requests for actions came up anyway in the [discovery interviews](discovery-interview.md):

- M. Costa asked whether the assistant could **flag a policy as out of date** when a handler spots one, so A. Novak's team hears about it.
- A Property handler asked whether it could **paste the cited paragraph into the claim record** in the claims system.

Constraints:

- R. Okafor's review treats any AI system that writes to a business system as a separate risk class, with a longer review and a human-approval requirement.
- The engagement is ten weeks. An action needs its own tool design, error handling, approval step and audit trail (see the [action-agent pack](../../skills/scenario-action-agent/SKILL.md)).
- Answers can be wrong. The week-2 bar is correctness ≥ 85%, not 100% ([evaluation plan](eval-plan.md)).

## Options considered

| Option | Pros | Cons | Maturity (generally available / preview) | Who maintains it after handover |
|---|---|---|---|---|
| **A. Read-only: one knowledge-base search tool, no write tools** | Smallest attack surface; excessive agency and tool misuse don't apply; fits the review window; simplest to run | Handlers still copy citations by hand; stale-policy reports go through the existing route | Generally available | Platform team |
| B. Add a "report stale policy" tool that creates an item in A. Novak's team's queue | Useful signal for A. Novak; low-impact, reversible write | A write tool changes the threat model and the review class; injected text in a document could make the agent file spam reports; needs an approval step to stay safe | Generally available | Platform team, plus A. Novak's team for the queue |
| C. Add a "write to claim record" tool | Saves a copy-paste per claim | Writes to the system of record from an answer that may be wrong; needs on-behalf-of identity into the claims system, a human-approval step and an audit trail; out of scope for release 1 | Generally available, but a large build | Claims systems team, who aren't involved |

## Decision

We will give the assistant no write tools, because every action requested is either low value or high risk, and read-only keeps it inside a review R. Okafor can complete in the engagement's time.

Option B's need is met **outside the agent**: every answer ends with a short footer linking to the existing policy-queries mailbox that A. Novak's team already reads. The handler decides whether to report; the agent sends nothing.

## Consequences

- **Security and identity:** the agent has one tool, a read-only knowledge-base query trimmed to the user's permissions. Excessive agency and tool misuse are marked "doesn't apply" in the [threat model](threat-model.md#4-threats), with this ADR as the reason. The blast radius of a successful prompt injection is a wrong or leaked answer, not a changed record. The agent's Entra Agent ID has one role and no write permissions anywhere.
- **Cost (monthly, at expected usage):** no tool calls beyond retrieval. See the [cost model](cost-model.md).
- **Operations and ownership:** nothing to roll back, no failed-write handling in the [runbook](runbook.md). The go-live review checks the tool list is still exactly one search tool ([go-live readiness](go-live-readiness.md)).
- **Lock-in and exit path:** none. Adding an action later is additive.
- **Preview dependencies and fallback:** none.
- **Revisit when:** a release adds any action. That release needs a new ADR, a revised threat model with excessive agency and tool misuse back in scope, a human-approval design, and a new review with R. Okafor. The stale-policy report (option B) is the likely first candidate, logged in the release 2 backlog.

💬 "Read-only" is a design choice worth writing down even when nobody argues with it. It's the single line in the threat model that removes two whole threat categories, and it's the line most likely to be eroded quietly by a well-meant "small" feature request in month three.
