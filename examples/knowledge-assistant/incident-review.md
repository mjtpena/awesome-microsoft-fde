# Incident Review: Superseded Motor Excess Policy

> **Worked example.** A filled-in [`incident-review`](../../skills/incident-review/SKILL.md) for a fictional engagement; see [examples](../README.md). Everything below, including names, systems and the product gap, is invented. Microsoft product facts follow the [technical reference](../../docs/microsoft-technical-reference.md); check it before relying on them.

The customer-facing review lives in Harbourline's repository at `docs/operations/incidents/week-6-superseded-excess.md`. The internal block at the end lives in the delivery team's own workspace; it's on this page only so you can see both.

## Customer repository: incident review

**Status:** Closed (week 7, Friday) · **Severity:** 2 (reached pilot users and the sponsor; contained before any claim was settled on it) · **Review owner:** E. Marsh (lead FDE) · **Review held:** week 6, Thursday, with D. Whitfield, M. Costa, A. Novak and the file-share owner

### Summary

On week 6, Tuesday, the pilot assistant told a Motor team leader the young-driver excess from a superseded version of the Motor Excess Policy, citing an old copy on the file share. The cause was retrieval of a duplicate document with no status, not the model or the instructions. Older copies are now kept out of the index by an amended version rule (ADR-003), re-indexing is gated like a release, and eight new golden-set cases fail the pipeline if a superseded copy is ever retrieved again.

### Impact

| Question | Answer |
|---|---|
| Who saw or acted on the output | 14 answers in the pilot group (12 Motor handlers) over about 40 hours cited one of five legacy copies. One team leader forwarded an answer to D. Whitfield |
| What decisions or actions it affected | The quality team checked every claim the 12 handlers touched in that window. Three applied a Motor excess; one used the superseded figure and was corrected before settlement. No customer was affected |
| Data exposed | None. All five documents were ones every pilot user is allowed to read |
| Duration (first occurrence to containment) | About 40 hours: re-index on Monday evening to containment on Wednesday morning |
| Cost impact | None measurable |
| Executive or customer communication sent | Yes. D. Whitfield sent a four-line note to their director on Wednesday afternoon (drafted with E. Marsh). Pilot group told in their Teams channel on Wednesday morning |

### Timeline

All times from the gateway logs, Foundry traces and the pilot Teams channel. Week 6.

| Time | What happened | Source |
|---|---|---|
| Mon 18:05 | Scheduled re-index adds the file share's `published` folder, now including OCR text for the 140 scanned PDFs. Runs straight into the pilot index | Indexer run history |
| Tue 09:52 | First answer citing a legacy copy (Motor Excess Policy, file share) | Gateway log, request ID in the trace |
| Tue 14:31 | A Motor team leader asks about the young-driver excess, gets the old figure, and forwards the answer to D. Whitfield asking which figure is right | Pilot channel; email shared by D. Whitfield |
| Tue 16:10 | D. Whitfield forwards it to E. Marsh. Sponsor already aware | Email |
| Tue 16:40 | Trace pulled: both versions retrieved, legacy copy ranked first. Classified as retrieval; nobody edits the prompt | Foundry trace |
| Tue 17:30 | Gateway logs searched for every answer citing a file-share document with no `Status`: 14 found, across five legacy Motor documents | Log query, saved in the repository |
| Wed 08:15 | **Contained:** the five legacy documents removed from the index using the runbook's urgent-removal steps. Pilot told in Teams | Runbook log |
| Wed 10:00 | Full evaluation on version 0.6: correctness 81%, release bar 85%. Release blocked | [Evaluation results log](eval-plan.md#results-log) |
| Wed 15:00 | Quality team confirms one affected claim, corrected before settlement | Quality team email |
| Thu 11:00 | Review held; actions agreed | This document |
| Fri 16:00 | Version 0.6.1 passes the full evaluation on 128 cases; pilot stays at 12 users | Evaluation results log |

### Failing layer

| Layer | Evidence from the trace | At fault? |
|---|---|---|
| Permissions | All retrieved documents were readable by the user. Low-privilege run still at zero pricing content | No |
| Data | Five Motor policies had an older copy in the file share's `published` folder, with no `Status` and no "superseded" marking. We had treated `published` as meaning "in force" | Contributing |
| Retrieval | Both versions retrieved for the excess question. The legacy copy ranked first: shorter, with the excess table near the top, so it matched the query terms more closely | **Yes** |
| Instructions | The agent quoted the document it was given accurately and showed its effective date, as instructed. Faithfulness stayed at 96% | No |
| Model | Same behaviour on three runs; correct once the legacy copy was removed | No |
| Tool | One read-only search tool; called correctly | No |
| Integration | Teams showed the answer text and the cited source as written | No |

**Reproduced on the test environment:** Yes, on Tuesday evening, by re-indexing the test index with the same folder · **Trace or request ID:** recorded in the repository copy

### Contributing factors

| # | Factor | Why the system allowed it | Action or "accepted by" |
|---|---|---|---|
| 1 | Legacy copies of current policies sat in the file share's `published` folder | The [data audit](data-audit.md) found nobody could say which file-share documents were in force, but the version rule in [ADR-003](adr-003-current-version-only.md) only compared versions within one source, not across sources | Action 1, 2 |
| 2 | A re-index went straight to the pilot index | Re-indexing was treated as routine operations, not as a change. It never ran through the evaluation gate | Action 3 |
| 3 | No golden-set case had two versions of the same policy in two different sources | The 120 cases were written from the SharePoint sites first; the file share was added later | Action 4 |
| 4 | Retrieval scores weren't watched between releases | Nobody looked at retrieval quality until a user reported a wrong answer | Action 5 |
| 5 | The answer showed the old effective date, and the reader didn't notice | Expecting users to spot a date is not a control. We considered an instruction to flag conflicting sources, and rejected it: the decision in ADR-003 is that superseded versions are never indexed, so the fix belongs in the data | Accepted by D. Whitfield; no instruction change |

### What stops it happening again

| Change | Evaluation cases added (IDs) | Regression test | Documents updated |
|---|---|---|---|
| Version rule amended: a file-share document is indexed only if no document with the same policy reference is marked `Current` on a SharePoint site. Documents with no policy reference are held for A. Novak's review | GS-121 to GS-128 | Each case fails if any superseded version appears in the retrieved set, not only if the answer is wrong | [ADR-003](adr-003-current-version-only.md), amended; [data audit](data-audit.md) |
| Five legacy copies moved from `published` to an excluded `archive` folder by the file-share owner | GS-121 to GS-125 | As above | Data audit |
| Every re-index runs on the test index first, with the full evaluation, before production | n/a | Pipeline step: production re-index needs a passing evaluation run ID | [Evaluation plan](eval-plan.md#when-it-runs), [runbook](runbook.md) |
| New runbook incident row: "Answer cites a superseded policy" | n/a | Practised in the week-10 runbook drill | [Runbook](runbook.md) |

**Full evaluation after the fix:** version 0.6.1, 128 cases: retrieval at 5 results 91%, faithfulness 96%, correctness 86%, refusals 24/24, pricing leak 0. Passes narrowly; pilot stays at 12 users until the week-7 run.

### Actions

| # | Action | Owner | Due | Status |
|---|---|---|---|---|
| 1 | Amend ADR-003 with the cross-source version rule | E. Marsh | Week 6, Fri | Done |
| 2 | Review every file-share document with no policy reference (about 210) and mark current or archive | A. Novak | Week 8, Fri | Done (week 8) |
| 3 | Add the re-index gate to the pipeline and the runbook | T. Osei | Week 7, Wed | Done |
| 4 | Add GS-121 to GS-128 to the golden set and the pull-request subset | M. Costa, E. Marsh | Week 6, Fri | Done |
| 5 | Weekly retrieval check on 50 sampled production questions, owned after handover by the platform team | S. Adeyemi | Week 9 (go-live) | Done |
| 6 | Tell the quality team which policies had legacy copies, for the next quarterly audit | D. Whitfield | Week 7, Mon | Done |

### What went well

- The team leader questioned the figure instead of using it.
- The trace showed both documents and their ranks within half an hour, so nobody wasted a day on prompt changes.
- The release gate blocked version 0.6 before the pilot widened.

**Accepted by (customer):** D. Whitfield, Head of Claims Operations · **Date:** week 7, Friday

## Internal: engagement notes and product feedback

> Internal to the delivery team. Not in Harbourline's repository or tenant. Describes the problem, not Harbourline's data.

### Product gaps found

| Product / feature | Gap | Workaround used | Field-feedback report |
|---|---|---|---|
| Knowledge base over several sources (invented gap, for illustration only) | No built-in way to detect or flag the same document existing in two connected sources with different versions | A cross-source version rule in our own ingestion step, keyed on the policy reference | [Field feedback: superseded duplicates across sources](field-feedback.md) |

### Engagement lessons

- We accepted "`published` means in force" from one interview. The data audit flagged the doubt; we should have turned it into a test before indexing the folder.
- Re-indexing is a release. The [`runbook`](../../skills/runbook/SKILL.md) and [`eval-plan`](../../skills/eval-plan/SKILL.md) skills say "run on every change"; we hadn't counted data changes as changes. Raised with the skill maintainers.

### Relationship

- D. Whitfield was more reassured by the same-day trace and the claim check than worried by the error. They asked for the eight new cases to be shown at the Friday demo, and they were.
- The forwarding team leader is now one of the strongest advocates in the pilot. Thank them by name at go-live.
