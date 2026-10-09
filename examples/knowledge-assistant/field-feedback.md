# Field Feedback: Superseded Duplicates Across Knowledge Sources

> **Worked example.** A filled-in [`field-feedback`](../../skills/field-feedback/SKILL.md) report for a fictional engagement; see [examples](../README.md). Everything below, including names and systems, is invented.
>
> ⚠️ **The product gap in this report is invented for illustration.** It is not a known defect in Foundry IQ, Azure AI Search or any other Microsoft product, and this page is not evidence about how those products behave. It shows the shape and level of detail of a good report. Before filing anything like it for real, check current Microsoft Learn documentation and release notes: the capability may exist, or be configured differently from what you assumed.

This report lives in the delivery team's internal workspace, never in Harbourline's repository. It came out of the [week-6 incident review](incident-review.md#internal-engagement-notes-and-product-feedback).

---

**Filed by:** E. Marsh (lead FDE) · **Severity:** S2 Major · **Engagements affected:** 1 confirmed, 2 reported similar · **Status:** Filed, week 6 · **Tracking link:** internal intake item (link in the workspace copy)

## The gap

A knowledge base that indexes the same policy from two connected sources (for example a SharePoint site and a file share) retrieves both versions, with nothing to say one supersedes the other. Customers with document sprawl need a way to mark or detect superseded duplicates across sources, so the old version is never retrieved.

## Reproduction (clean environment, synthetic data)

| Item | Detail |
|---|---|
| Environment | The team's own test subscription and test Microsoft 365 tenant. One knowledge base with two knowledge sources: a SharePoint site and a file-based source |
| Product versions / SKUs / preview flags | Recorded in the workspace copy at the time of filing |
| Steps | 1. Create `Leave Policy` version 3 on the SharePoint site, with a `Status` column set to `Current`. 2. Put `Leave Policy` version 2, same title and policy reference, in the file-based source, with no status metadata. 3. Index both. 4. Ask "How many days of carer's leave do I get?", where the figure differs between versions |
| Expected | Only version 3 retrieved, or version 2 marked as superseded so it can be filtered out |
| Actual | Both retrieved. Version 2 ranked first on 6 of 10 phrasings. In the configuration we tried, we found no setting to link the two documents or to filter on a status that exists in only one source |
| Reproduced away from the customer? | Yes. No customer documents, names or text used |

## Customer impact

| Question | Answer |
|---|---|
| Customer | A mid-sized insurer (named in the workspace copy; the agreement allows naming within the delivery organisation, not outside it) |
| Scenario | Knowledge assistant, internal staff, read-only |
| What it blocked or put at risk | A pilot user was given a superseded policy figure. One claim decision used it before it was caught. The customer's business measure is halving superseded-policy citations, so this hits the reason the project exists |
| Engineering time lost | About four days: investigation, the workaround, and new evaluation cases |
| Did it cause an incident? | Yes: see the internal incident notes |

## Workaround in use

| Workaround | Cost to build | Cost to operate | Weaknesses |
|---|---|---|---|
| A version rule in our own ingestion step: a file-share document is indexed only if no SharePoint document with the same policy reference is marked `Current`. Documents with no policy reference are held for manual review | About two days | The policy owner reviews held documents; roughly 210 at first, a few a month after | Depends on a consistent policy reference in every document. Custom code the customer now has to own. Doesn't generalise to other customers without rework |
| Evaluation cases that fail if any superseded version is retrieved | Half a day | Runs on every re-index | Catches the problem; doesn't prevent it |

## Other engagements

| Team / engagement | Same gap? | Workaround |
|---|---|---|
| Public-sector knowledge assistant (another FDE team) | Similar: policies duplicated between an intranet and a document library | Excluded the older source entirely |
| Manufacturing maintenance manuals (another FDE team) | Possibly: duplicate manuals across two sites, not yet confirmed as the same cause | None yet |

## What we're asking for

- [x] Product fix: a supported way to mark a document as superseded by another, or to detect likely duplicates across knowledge sources and keep only the one with a current status
- [x] Documentation change: guidance for multi-source knowledge bases on handling the same document in more than one source
- [ ] Roadmap answer
- [ ] Count this

## Confidentiality check

- [x] No customer document content, prompts, names, identifiers or screenshots
- [x] Customer named only if the agreement allows it (workspace copy only)
- [x] Reproduction uses synthetic data only
- [x] Checked by the engagement lead (E. Marsh is the lead; checked by T. Osei as second reviewer)

---

**What Harbourline sees instead:** the [handover](handover.md) lists this under "Known product issues and workarounds" as a symptom and the workaround they now own, with no internal tracking link, because there's no public one.
