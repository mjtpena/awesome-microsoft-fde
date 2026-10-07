# ADR-00X: <Decision in a few words>

> **Step:** 3 Design · **Pillars:** all · **Scenarios:** all (critical for regulated and disconnected, where reviewers want the paper trail)
>
> **How to use:** one architecture decision record (ADR) per decision that would be expensive to reverse. Keep it to one page. Store it in the customer's repository under `docs/adr/`. Never edit an accepted ADR; supersede it with a new one.

- **Status:** Proposed | Accepted | Superseded by ADR-00Y
- **Date:**
- **Deciders:**
- **Pillar(s):** 1 Software · 2 Data · 3 Cloud/network · 4 Security · 5 AI · 6 Delivery

## Context

What forces this decision? Include constraints from the customer: policies, skills, budget, deadlines.

## Options considered

| Option | Pros | Cons | Maturity (generally available / preview) | Who maintains it after handover |
|---|---|---|---|---|

## Decision

We will … because …

## Consequences

- **Security and identity:**
- **Cost (monthly, at expected usage):**
- **Operations and ownership:**
- **Lock-in and exit path:** what it would take to move away from this choice
- **Preview dependencies and fallback:**

## Decisions most engagements need, by scenario 💬

| Scenario | ADRs to expect |
|---|---|
| All | Agent platform (low code vs code) · where users meet the agent · identity model (as itself vs on behalf of user) · gateway in front of models · how evaluation gates releases |
| Knowledge assistant | Ingestion approach per source · chunking strategy · search type (hybrid, re-ranking, agentic retrieval) · permission trimming |
| Action agent | Which actions need human approval · tool design and error handling · audit trail |
| Data agent | Which data layer the agent queries · metric definitions · query safety limits |
| Regulated | Private networking design · exceptions to "nothing public" (for example Teams publishing) · log retention and location |
| Disconnected | Model selection for local hardware · update and transfer process · local identity |
