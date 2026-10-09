# Data Audit: Harbourline Insurance / Claims and Underwriting Policies

> **Worked example.** A filled-in [`data-audit`](../../skills/data-audit/SKILL.md) for a fictional engagement; see [examples](../README.md). Everything below, including names and systems, is invented. Microsoft product facts follow the [technical reference](../../docs/microsoft-technical-reference.md); check it before relying on them.

**Version:** 1.0 · **Date:** week 3, day 2 · **Audited by:** T. Osei, E. Marsh, with A. Novak (data owner) and L. Moreau (SharePoint administrator) · **Feeds:** the [scope reset](scope-reset.md), [ADR-003](adr-003-current-version-only.md), the [threat model](threat-model.md)

Production data access arrived on week 1, day 5 (see the [access request](access-request.md)), so this audit ran in weeks 2 and 3 against real content. Every access path was tested as `svc-test-motor`, a low-privilege account with a Motor handler's groups.

## Sources

| Source | System | Structured / documents | Format (open / proprietary) | Volume | How fresh it must be | Owner | Access path | Quality issues | Sensitivity |
|---|---|---|---|---|---|---|---|---|---|
| Claims Policy | SharePoint site | Documents | Word and PDF (open) | About 2,400 | Next working day | D. Whitfield; currency decided by A. Novak | Indexer managed identity, site-scoped | **31% exist in more than one version; no reliable "current" flag** | Internal |
| Underwriting | SharePoint site | Documents | Word and PDF | About 1,100 | Next working day | A. Novak | Same | Clean; `Status` column maintained by A. Novak's team | Internal |
| Pricing | SharePoint site | Documents | Word, Excel, PDF | About 300, including drafts | Next working day | G. Patel | Same, after the permission fix | **Shared with "Everyone except external users"** | Confidential (drafts) |
| Legacy policies | On-premises file share | Documents | PDF, some Word | About 1,800; 600 in `published` | Weekly | A. Novak | Managed identity over ExpressRoute; `published` folder only | **140 scanned PDFs with no text layer**; no version metadata at all | Internal |

## How each finding was measured

| Finding | How we measured it | What it means for scope |
|---|---|---|
| Claims Policy: 31% in more than one version | Exported file names, titles and modified dates for all 2,400 documents. Normalised titles (case, "v2", "FINAL", dates stripped) and counted groups with more than one file: 744 documents sit in such groups. A. Novak checked 50 groups by hand and agreed 47 were genuine duplicates of one policy | Can't index everything and hope ranking picks the right one. Index only the current version ([ADR-003](adr-003-current-version-only.md)) |
| Claims Policy: no reliable "current" flag | The site has a `Current` yes/no column. It's filled on 38% of documents, and 9 of the 50 checked groups had two documents marked current | Use a version rule agreed with A. Novak instead: highest published major version, then latest "effective from" date in the document header |
| Underwriting: clean | `Status` filled on every document; A. Novak's team sampled 30 and all matched what they consider current | Use `Status = Current` directly. Lowest-risk source; good first test |
| Pricing: overshared | SharePoint oversharing assessment, then confirmed by opening five draft documents as `svc-test-motor`. All five opened | **Blocker.** Permission trimming faithfully reproduces bad permissions. L. Moreau fixes the sharing before anything is indexed; G. Patel's approval is conditional on it |
| File share: 140 scans with no text layer | Text extraction run over the `published` folder; 140 of the 600 returned no text | Not searchable as they stand. OCR them during ingestion and have A. Novak's team spot-check 20; the method sits under ADR-002 |
| File share: no version metadata | No status column exists on a file share; folder names are the only signal | Treated as one version per file. ⚠️ This is the gap the week-6 incident came through: see the [incident review](incident-review.md) and the [ADR-003 amendment](adr-003-current-version-only.md#amendment-1-week-6) |

## Ingestion decision per source

| Source | Reference in place / Replicate / Batch copy | Why | Refresh schedule |
|---|---|---|---|
| Claims Policy | Indexed into the Foundry IQ knowledge base; only current versions, Motor and Property sections for release 1 | Permission-aware and maintained by the platform, not our code (ADR-002) | Incremental, nightly |
| Underwriting | Same; `Status = Current` only | Same | Incremental, nightly |
| Pricing | Same, only after the permission fix is confirmed | G. Patel's condition | Incremental, nightly |
| File share `published` | Indexer over the folder; `drafts` excluded | Same index, one place to trim | Weekly full re-index |

## Permissions

| Source | How permissions work today | Will the AI respect them? How? | Tested with a low-privilege user? |
|---|---|---|---|
| Claims Policy, Underwriting | Site groups; all claims staff can read | Yes: permission-trimmed retrieval using each document's access-control list ([RAG blueprint](../../docs/microsoft-technical-reference.md#enterprise-rag-blueprint-azure)) | Yes. 20 questions as `svc-test-motor`; results matched what the account can open |
| Pricing | **Broken:** everyone can read | Only once fixed. Trimming copies today's permissions, good or bad | Yes, and it failed (see above). Repeat after the fix and after every re-index: 25 pricing questions, pass bar zero pricing content |
| File share | NTFS groups; `published` readable by all staff | Yes, through the indexer's permission metadata | Yes. Five questions; all returned |

## Quality checks

| Dataset | Check | Rule | Current result | Automated? |
|---|---|---|---|---|
| Claims Policy | Unique | One indexed document per normalised title | 31% fail before the version rule; 0% after | Yes, in the ingestion pipeline |
| Underwriting | Current | Every indexed document has `Status = Current` | 100% | Yes |
| File share | Complete | Every indexed PDF has extractable text | 460 of 600 before OCR | Yes |
| All | Current | Effective-from date shown in each citation | Not yet: added to the [agent instructions](agent-instructions.md) | Checked in the [evaluation plan](eval-plan.md) |

## Knowledge assistant: documents

| Collection | Doc types | Count | Tables or images that matter? | Source of truth? | Out-of-date content? | Oversharing found? |
|---|---|---|---|---|---|---|
| Claims Policy | Word, PDF | About 2,400 | Yes: excess and limit tables | Yes, once the version rule applies | Yes, heavily | No |
| Underwriting | Word, PDF | About 1,100 | Yes: rating factor tables | Yes | Little | No |
| Pricing | Word, Excel, PDF | About 300 | Yes | Published guidance only | Drafts mixed in | **Yes** |
| File share | PDF (140 scans), Word | 600 in `published` | Some | Only where no SharePoint copy exists | Unknown | No |

- **Chunking approach:** the knowledge source's default chunking, checked on the 20 hardest documents (mostly tables). Excess tables split across chunks in 3 of the 20; acceptable for release 1, tracked in the [evaluation plan](eval-plan.md).
- **Metadata kept on each chunk:** title, source, version, effective-from date, owner, URL and permissions.

## Top five data risks

1. **Pricing drafts reach non-pricing users** through broken sharing. Owner: L. Moreau (fix), T. Osei (test). In the [threat model](threat-model.md#4-threats).
2. **Superseded Claims Policy versions retrieved** because there's no reliable current flag. Owner: A. Novak (rule), E. Marsh ([ADR-003](adr-003-current-version-only.md)).
3. **File-share copies duplicate SharePoint policies** with no version signal. Owner: A. Novak. Realised in week 6; see the [incident review](incident-review.md).
4. **Scanned PDFs extracted badly**, especially tables. Owner: T. Osei; 20-document spot check.
5. **Freshness:** a changed policy isn't live by the next working day if a nightly run fails silently. Owner: S. Adeyemi; alert in the [runbook](runbook.md).

💬 Risks 1 and 2 are why the [scope reset](scope-reset.md) happened. Fixing them for 900 internal handlers in the time left was realistic. Fixing them to the standard a customer-facing answer needs was not.
