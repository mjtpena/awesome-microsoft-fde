# ADR-003: Index only the current version of each policy

> **Worked example.** A filled-in [`adr`](../../skills/adr/SKILL.md) for a fictional engagement; see [examples](../README.md). Everything below, including names and systems, is invented. Microsoft product facts follow the [technical reference](../../docs/microsoft-technical-reference.md); check it before relying on them.

- **Status:** Accepted (week 2). Amended week 6: see [Amendment 1](#amendment-1-week-6)
- **Date:** week 2, day 3
- **Deciders:** A. Novak (Underwriting policy manager, owns which version is current), D. Whitfield (Head of Claims Operations), E. Marsh (lead FDE); reviewed by S. Adeyemi (Platform team lead)
- **Pillar(s):** 2 Data · 5 AI

## Context

The quality audit found 1 in 12 sampled claim decisions cited a superseded policy version. That's the problem the assistant exists to fix, so it must not reproduce it.

- **Claims Policy** (about 2,400 documents): 31% exist in more than one version, and the `Current` column is filled on only 38% of documents and sometimes wrong ([data audit](data-audit.md#how-each-finding-was-measured)).
- **Underwriting** (about 1,100): A. Novak's team maintains a reliable `Status` column.
- **File share** `published` folder (600 documents): no version metadata at all.
- Handlers sometimes need to know what an old policy said, for claims that started under it. That's rare, and the [discovery interviews](discovery-interview.md) didn't find it among the 20 most-asked questions.
- Retrieval ranks by relevance, not by date. Two near-identical versions score almost the same, so ranking alone won't reliably pick the current one.

## Options considered

| Option | Pros | Cons | Maturity (generally available / preview) | Who maintains it after handover |
|---|---|---|---|---|
| A. Index everything; tell the agent to prefer the newest | No ingestion logic | The model sees both versions and has to guess; "newest" by modified date is often a copy, not the current policy. Repeats the audit problem | Generally available | Nobody; that's the problem |
| B. Index everything with a version field; filter at query time | Old versions available if ever needed | Same version-detection problem, moved to query time; harder to test; every query depends on the filter being right | Generally available | Platform team |
| **C. Index only the current version**: `Status = Current` where the column exists; otherwise a version rule agreed with A. Novak | The index holds one answer per policy; easy to test; matches how handlers should work | Old versions unavailable through the assistant; the rule needs an owner; a wrong rule silently hides the current version | Generally available (ingestion filtering in our pipeline before the knowledge base) | Platform team runs it; A. Novak owns the rule |
| D. Clean up the sources first, then index everything | Fixes the root cause for everyone | Months of A. Novak's team's time; outside this engagement's scope ([canvas](ai-use-case-canvas.md)) | n/a | A. Novak's team |

## Decision

We will index only the current version of each policy, because a single answer per policy is the only design that we can test directly against the audit problem.

- **Underwriting:** documents with `Status = Current`.
- **Claims Policy:** within each group of documents sharing a normalised title, the highest published major version; ties broken by the latest "effective from" date in the document header. A. Novak agreed the rule and checked it against 50 groups.
- **File share:** each document in `published` treated as current. `drafts` excluded.
- Questions about an old version are answered with "I can only see the current version" and a link to the site's version history.

## Consequences

- **Security and identity:** none beyond the [threat model](threat-model.md). Fewer documents indexed means a smaller exposure if trimming ever fails.
- **Cost (monthly, at expected usage):** a smaller index than indexing all versions. Exact figures are in the [cost model](cost-model.md).
- **Operations and ownership:** the version rule is code in the ingestion pipeline, with unit tests built from A. Novak's 50 checked groups. A. Novak is the named owner of the rule; S. Adeyemi's team runs it. A change to the rule is a pull request A. Novak approves.
- **Lock-in and exit path:** the rule runs before the knowledge base, so it moves with us if the knowledge base is ever replaced.
- **Preview dependencies and fallback:** none.
- **Evaluation:** the [evaluation plan](eval-plan.md) includes cases whose correct answer changed between versions, so a wrong rule shows up as a correctness drop.

## Amendment 1 (week 6)

**Date:** week 6, day 5 · **Agreed by:** A. Novak, D. Whitfield, R. Okafor (Security Architect), E. Marsh

**What happened.** The assistant cited a superseded Motor excess policy to a team leader, who forwarded it to D. Whitfield. The cause was retrieval, not the model. An old copy of the policy sat on the file share with no status. Under the original decision every `published` file-share document counted as current, so the old copy was indexed alongside the current SharePoint version and ranked higher for that question. The rule de-duplicated within each source but never across sources. Correctness on the golden set fell from 88% to 81% after the week-6 re-index. Full timeline in the [incident review](incident-review.md).

**The amendment.**

1. **File-share documents that duplicate a SharePoint document are excluded**, matched on policy reference or, where there's none, normalised title, unless A. Novak marks the file-share copy current in a small allow-list kept in the repository (`ingestion/fileshare-allowlist.csv`). File-share documents with neither a policy reference nor a clear title match are held for A. Novak's review rather than indexed.
2. **Re-index check.** A re-index is treated as a release. It runs on the test index first and must pass two gates before production is re-indexed:
   - the cross-source duplicate report shows no policy indexed twice;
   - the full evaluation run, including the eight cases added after the incident (GS-121 to GS-128), meets the release bar in the [evaluation plan](eval-plan.md). The production re-index needs that passing run's ID.

   If either fails, production keeps its current index and the platform on-call is alerted. Steps are in the [runbook](runbook.md).

**Result.** Five Motor policies had an older file-share copy; all are now excluded, along with the other cross-source duplicates the report found. Correctness recovered to 90% in week 7. The gap that let a status-less copy through is filed as [field feedback](field-feedback.md).

💬 The skill says never edit an accepted ADR; supersede it. We appended a dated amendment instead, and left the original text untouched above it, because the decision itself (index only the current version) stands and only the rule for one source tightened. R. Okafor agreed. If the decision had changed, a new ADR would have superseded this one.
