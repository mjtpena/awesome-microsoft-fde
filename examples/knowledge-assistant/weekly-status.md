# Weekly Status: Harbourline Policy Assistant (weeks 1, 3 and 6)

> **Worked example.** Three filled-in [`weekly-status`](../../skills/weekly-status/SKILL.md) pages for a fictional engagement, plus the internal field-notes log for week 6; see [examples](../README.md). Everything below, including names and systems, is invented. Microsoft product facts follow the [technical reference](../../docs/microsoft-technical-reference.md); check it before relying on them.

In the engagement, each week is its own file in Harbourline's repository (`docs/engagement/status/week-1.md` and so on). They're in one file here so you can see how a status changes from green to amber and back. The field-notes log at the end **doesn't live in Harbourline's repository**: it's in the delivery team's own engagement workspace.

---

## Week 1

### Weekly Status: Harbourline Policy Assistant · Week 1

**Overall:** 🟢 On track · **Target date:** go-live in week 9 · **Change since last week:** first status

**In one sentence:** we have production data approval, the first round of discovery interviews done, and a stakeholder map everyone has seen; nothing is built on real data yet, which is where we expected to be.

#### What we showed

- Demo: a throwaway prompt agent answering questions from 20 public sample policy documents, shown to D. Whitfield, M. Costa and A. Novak on Friday. Purpose: show what "a cited answer in Teams" looks like before anyone writes requirements.
- Measure: none yet. The business baseline is set: a median of 22 minutes to find the right policy for a complex claim (30 handlers shadowed), and 1 in 12 audited decisions citing a superseded version.

#### What changed

- Production data approval granted on Thursday, nine working days after the [access request](access-request.md) went in on day 1.
- [Engagement charter](engagement-kickoff.md) signed at Monday's kickoff.
- [Discovery interviews](discovery-interview.md): claims handlers, team leaders, underwriting, pricing, security, identity, records. The top 20 questions are drafted, each with the source-of-truth document named by M. Costa or A. Novak.
- [Stakeholder map](stakeholder-map.md) shared. G. Patel (Head of Pricing) added as an approver after the pricing interview: the Pricing site holds drafts that only their team may see.

#### Decisions needed (with a date)

| Decision | Options | Our recommendation | Needed by | Owner |
|---|---|---|---|---|
| Agent platform | Copilot Studio; Foundry prompt agent behind the APIM (Azure API Management) gateway | Foundry, because security needs the gateway and logs in Harbourline's own subscription. Draft ADR-001 circulated | Week 2, Wednesday | R. Okafor |
| Oversharing review of the three SharePoint sites before anything is indexed | Run it now; run it after the first build | Now. Indexing exposes whatever is overshared | Week 2, Monday | L. Moreau |
| Who sets the release bar for answer quality | Sponsor; quality team; both | D. Whitfield sets it, the quality team advises | Week 2, Friday | D. Whitfield |

#### Risks and blockers

| Risk / blocker | Impact | Mitigation | Owner | Since |
|---|---|---|---|---|
| No reliable "current version" flag on the Claims Policy site (seen in interviews; data audit to confirm) | Wrong answers from superseded policies: the problem we're here to fix | Data audit in week 2 counts duplicates; A. Novak to propose a version rule | A. Novak | Week 1 |
| Bot Service rights for publishing to Teams aren't covered by the Foundry roles we requested | Can't publish to Teams in week 4 | Second access request raised Friday | J. Tan | Week 1 |

#### Next week

- Use-case canvas workshop with D. Whitfield; ADRs 001 to 006 drafted; threat model to version 0.3 for the second security review.
- Data audit across all four sources.
- First draft of the evaluation plan, with M. Costa co-writing the golden set.

---

## Week 3

### Weekly Status: Harbourline Policy Assistant · Week 3

**Overall:** 🟡 At risk · **Target date:** go-live in week 9 (unchanged, for the reduced scope) · **Change since last week:** 🟢 → 🟡

**In one sentence:** the data audit showed the original scope couldn't be delivered safely in ten weeks, so D. Whitfield agreed to cut release 1 to internal Motor and Property handlers; Pricing site permissions must be fixed before we index it.

#### What we showed

- Demo: the agent on a test index of the Underwriting site (about 1,100 documents, clean `Status` column), answering 15 of the top 20 questions with correct citations. Shown to D. Whitfield, M. Costa, A. Novak and two Motor handlers.
- Measure: golden set at 64 draft cases (target 120 by week 5). No scored run yet.

#### What changed

- **Scope reset** ([scope-reset.md](scope-reset.md)), signed by D. Whitfield on Thursday. The original ask also covered a customer-facing version in the claims portal and all 4,000 staff. Release 1 is now **internal claims handlers only, Motor and Property first**. The portal version is in the backlog, and needs its own threat model and responsible AI assessment.
- [Data audit](data-audit.md) findings:
  - Claims Policy site: 31% of about 2,400 documents exist in more than one version, with no reliable "current" flag.
  - File share: 140 scanned PDFs with no text layer; the `drafts` folder is excluded.
  - **Pricing site: shared with "Everyone except external users"**, including about 300 documents with drafts. Anyone at Harbourline could open them today, and the assistant would have repeated them.
- [ADR-003](adr-003-current-version-only.md) accepted: index only the current version, using `Status` or A. Novak's version rule where it's missing.

#### Decisions needed (with a date)

| Decision | Options | Our recommendation | Needed by | Owner |
|---|---|---|---|---|
| Approve the Pricing site permission change (remove "Everyone except external users"; Pricing team group only) | Approve; delay and exclude Pricing from the index | Approve. It's a live exposure with or without the assistant | Week 4, Tuesday | G. Patel |
| Version rule for Claims Policy documents without `Status` | Latest modified date; highest version number in the file name; A. Novak's team tags them by hand | Highest version number, with A. Novak's team checking the 40 most-used policies by hand | Week 4, Wednesday | A. Novak |
| Scanned PDFs on the file share | OCR (optical character recognition) all 140; OCR only the 35 cited in the top questions; leave them out | OCR all 140, with M. Costa checking the 35 most used | Week 4, Friday | M. Costa |

#### Risks and blockers

| Risk / blocker | Impact | Mitigation | Owner | Since |
|---|---|---|---|---|
| **Pricing drafts visible to all staff** | Confidential pricing guidance in answers to any user | Pricing excluded from every index until L. Moreau confirms the fix; low-privilege test with 25 pricing questions after every re-index ([threat model](threat-model.md)) | L. Moreau (fix), G. Patel (approve) | Week 3 |
| Duplicate versions on the Claims Policy site | Superseded answers | ADR-003 version rule; incident cases planned in the golden set | A. Novak | Week 1 |
| Pressure to bring back the portal version before go-live | Re-opens the scope reset; customer-facing use needs a separate assessment | Backlog item with a named owner and a date to revisit after go-live | D. Whitfield | Week 3 |
| Teams doesn't show native citations for Foundry agents ([technical reference](../../docs/microsoft-technical-reference.md#phase-2-azure-architecture--ai-landing-zones)) | "Answers that cite the policy" is the core promise | Agent writes source title, section and link into the answer text; D. Whitfield to judge it in the week-4 pilot | E. Marsh | Week 2 |
| Bot Service rights | Can't publish to Teams | Granted Wednesday. **Closed** | J. Tan | Week 1 |

#### Next week

- Pilot with 12 Motor handlers in Teams, on real data from Claims Policy, Underwriting and the file share's `published` folder.
- Pricing indexed only after L. Moreau's fix is confirmed with the low-privilege test.
- Golden set to 120.

---

## Week 6

### Weekly Status: Harbourline Policy Assistant · Week 6

**Overall:** 🟡 At risk (🔴 Off track from Tuesday to Thursday) · **Target date:** go-live in week 9, held · **Change since last week:** 🟢 → 🔴 → 🟡

**In one sentence:** the assistant gave a team leader a superseded Motor excess figure after Monday's re-index; we traced it to an old file-share copy with no status, fixed the data and the version rule, and the evaluation is back above the bar, but the pilot doesn't widen until week 7.

#### What we showed

- Demo: replayed the wrong answer end to end from the logs (question, retrieved documents, answer), then the same question on the fixed index. Shown to D. Whitfield, M. Costa, A. Novak, R. Okafor and S. Adeyemi.
- Measure: correctness 88% (week 5) → **81%** after the re-index (release blocked) → 86% on the fixed index, with the 8 new incident cases ([evaluation plan](eval-plan.md#results-log)).

#### What changed

- **Incident** ([incident review](incident-review.md)). On Tuesday a Motor team leader asked about the young-driver excess and got the figure from a superseded policy, with a confident citation. They forwarded it to D. Whitfield. Timeline: reported 10:40, pilot paused 11:05 with the kill switch (API disabled on the gateway), root cause found 15:30.
- **Root cause was retrieval, not the model.** Monday's scheduled re-index picked up an old copy of the Motor Excess Policy in the file share's `published` folder. It had no `Status`, so the version rule didn't apply, and it ranked above the current version. Faithfulness stayed at 96%: the model faithfully quoted the wrong document.
- Fix: the old copy and four other unflagged duplicates removed from the index; [ADR-003](adr-003-current-version-only.md) amended so a file-share document is indexed only if no SharePoint document with the same policy ID exists; a duplicate-version check added to every re-index; re-indexing now runs in test first and must pass the evaluation before production. Pilot resumed Thursday 16:00.
- Eight cases added to the golden set (GS-121 to GS-128). Field feedback filed with the product team ([field-feedback.md](field-feedback.md)).
- Release 0.6 (prompt changes for multi-part questions) was **blocked by the gate** at 81% and hasn't shipped. That part worked as designed.

#### Decisions needed (with a date)

| Decision | Options | Our recommendation | Needed by | Owner |
|---|---|---|---|---|
| Widen the pilot to 60 handlers in week 7 | Widen on schedule; wait another week | Widen, if the week-7 full run passes with all 8 incident cases correct | Week 7, Tuesday | D. Whitfield |
| Who approves a production re-index from now on | Platform on-call alone; on-call plus a passing evaluation run | A passing test-environment run is the approval; on-call just presses the button | Week 7, Monday | S. Adeyemi |
| Clean up the legacy files in the file share's `published` folder that duplicate SharePoint policies | Archive; leave and rely on the version rule | Archive, owned by A. Novak's team. It's the real fix; the rule is the safety net | Week 8 | A. Novak |

#### Risks and blockers

| Risk / blocker | Impact | Mitigation | Owner | Since |
|---|---|---|---|---|
| **Trust after the incident** | Handlers stop using it; D. Whitfield's confidence drops | Replay shown in the demo; M. Costa briefs the pilot group Monday; every answer shows the policy's effective date | M. Costa | Week 6 |
| Re-index changes answers outside the release gate | Repeat of this week | Re-index in test first; evaluation and pricing test must pass; duplicate-version check ([runbook](runbook.md)) | S. Adeyemi | Week 6 |
| Other unflagged duplicates we haven't found | More superseded answers | Duplicate-version check runs on every re-index and must return zero | T. Osei | Week 6 |
| Pricing drafts visible to all staff | Confidential content in answers | Fixed by L. Moreau in week 4; low-privilege test passed again after this week's re-index (0 of 25). Kept open until go-live | L. Moreau | Week 3 |
| Agent 365 licence needed for Defender to cover the agent ([technical reference](../../docs/microsoft-technical-reference.md#phase-3-identity-security--governance-for-agents)) | No Defender agent coverage at go-live | Logs to Log Analytics for security operations in the meantime; licence decision by week 8 | J. Tan | Week 2 |

#### Next week

- Full evaluation run on 0.7; widen the pilot to 60 handlers if it passes.
- Red-team run against the test deployment ([red-team.md](red-team.md)).
- Responsible AI impact assessment to F. Lindqvist for sign-off ([responsible-ai-impact-assessment.md](responsible-ai-impact-assessment.md)).

---

## Internal: field notes log (week 6 entries)

> **This block is not in Harbourline's repository.** It's appended to `field-notes.md` in the delivery team's own engagement workspace, and only what Harbourline's agreement allows is shared with the product team. It describes problems, not customer data. The filed version is [field-feedback.md](field-feedback.md).

```markdown
# Field Notes: Harbourline / Policy Assistant

> Internal to the delivery team. Don't copy into the customer's repository or tenant. Describe problems, not customer data.

| Week | Product / feature | What broke or was missing | Workaround | Seen at other customers? | Suggested fix | Filed where (link) |
|---|---|---|---|---|---|---|
| 2 | Foundry agent published to Teams | No native citations or streaming in Teams. The customer's whole ask was cited answers | Agent writes source title, section, effective date and link into the answer text; checked by the eval rubric | Yes: two other knowledge-assistant engagements this half | Native citation cards for Foundry agents in Teams | Known limitation on Learn; +1 added to the existing product item |
| 6 | Knowledge base indexing (file-share source) | A re-index silently changed answers. Nothing tied an indexer run to an evaluation run, so a document with no version metadata went live without any gate | Re-index in test first; pipeline runs the eval and a duplicate-version check before the production re-index | Similar story from one other team (legacy file shares) | Event or hook when an indexer run completes, so a pipeline can gate on it; a near-duplicate report across knowledge sources | field-feedback.md, filed week 6 |
| 6 | Evaluation | Faithfulness stayed at 96% while correctness fell to 81%; a team watching only groundedness would have missed this | Score retrieval separately against expected document IDs | Common pattern | Make retrieval scoring against expected sources the default in the agent evaluation samples | Shared in internal FDE channel |
```
