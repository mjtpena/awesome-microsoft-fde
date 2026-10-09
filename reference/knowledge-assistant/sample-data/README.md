# Sample policy documents

Invented Harbourline Insurance policies for the reference implementation. None of it is real guidance, and none of the figures are real.

Each document starts with a short metadata block that the loader reads:

- `Status:` must be `current` for the document to be indexed. `superseded`, `draft` or a missing status means it is left out (ADR-003 as amended in week 6).
- `Groups:` the groups allowed to retrieve it. Most documents are `all-staff`; the pricing draft is `pricing` only.

Four files exist to reproduce real problems from the engagement:

| File | What it reproduces |
|---|---|
| `motor-excess-policy-v2.md` | A superseded version with a `Status: superseded` line |
| `legacy-share-motor-excess.md` | The week-6 incident: an old copy from the file share with no status at all |
| `pricing-motor-rate-review-draft.md` | The oversharing finding: pricing drafts that only the pricing group may see |
| `claims-payment-authority.md` | Indirect prompt injection: one section hides an instruction aimed at the assistant |

This README is not a policy and is never indexed.
