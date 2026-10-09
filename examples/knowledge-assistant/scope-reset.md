# Scope Reset: Harbourline Policy Assistant

> **Worked example.** A filled-in [`scope-reset`](../../skills/scope-reset/SKILL.md) for a fictional engagement; see [examples](../README.md). Everything below, including names and systems, is invented. In the customer's repository this is `docs/engagement/scope-reset-1.md`.

**Date:** week 3, Thursday · **Week:** 3 of 10 · **Raised by:** E. Marsh (lead FDE) · **Decision by (sponsor):** D. Whitfield (Head of Claims Operations) · **Status:** Agreed (week 3, Friday)

## In one sentence

The data audit and discovery show we can't safely ship a claims-portal version for policyholders and an assistant for all 4,000 staff in ten weeks, so we recommend release 1 for internal claims handlers only, Motor and Property first, with the portal version deferred to the backlog.

## What we agreed

| Item | Original scope (canvas version 1, signed week 2) |
|---|---|
| Users | All 4,000 staff in Teams, plus policyholders through the claims portal |
| Sources / data | Three SharePoint sites (Claims Policy, Underwriting, Pricing) and the legacy file share |
| Shape | Answers only, with citations. Two channels: Teams and the claims portal |
| Business measure and target | Median time to a cited policy answer under 2 minutes; superseded-policy citations in the quality audit halved, within one quarter of go-live |
| Exit criteria | Release bar met; security sign-off; deployed from code; named owner ran it alone for a week |

The portal channel was added at kickoff at the request of D. Whitfield's director, who wanted to reduce "what does my policy cover?" calls.

## What we found

| Finding | Evidence | Why it matters to the scope |
|---|---|---|
| 31% of Claims Policy documents exist in more than one version, with no reliable "current" flag | [Data audit](data-audit.md), Claims Policy row | A wrong-version answer to a handler is caught by their team leader or the audit. A wrong-version answer to a policyholder is a customer communication on the wrong terms |
| The Pricing site is shared with "Everyone except external users" | Data audit; [threat model](threat-model.md) data-leakage row | Every extra staff group widens the blast radius until L. Moreau's permission fix is confirmed |
| 140 scanned PDFs on the file share have no text layer | Data audit, file-share row | OCR and checking take time we planned to spend on the evaluation |
| The measured problem is claims handlers: 22 minutes per complex claim, 1 in 12 audited decisions citing a superseded version | [Discovery notes](discovery-interview.md) and the 30-handler shadowing day | No discovery evidence yet for the other 3,100 staff. We'd be building for users we haven't met |
| A policyholder-facing answer would be treated as customer communication | Interview with Harbourline's compliance lead, week 3 | Needs the compliance team's review process, a separate curated corpus (policyholders can't be permission-trimmed against staff SharePoint), a public endpoint security hasn't agreed to, and a much stricter release bar. That's the [regulated, customer-facing risk profile](../../skills/scenario-regulated-private/SKILL.md), not the internal one we designed for |
| R. Okafor's design condition: no new public endpoints beyond the one in ADR-006 | [Stakeholder map](stakeholder-map.md), discovery notes | The portal needs a second, internet-facing route. Not agreeable inside ten weeks |

## Options

| Option | What it means here | Business measure: still met? when? | Risk | Effort and time |
|---|---|---|---|---|
| **Narrow** | Internal claims handlers only, in Teams. Motor and Property policies and handlers first (about 900 at go-live). Other lines of business and other staff later | Yes. Both targets are about claims handlers. Measurable one quarter after a week-9 go-live | Low to medium: internal, read-only, permission-trimmed. Pricing fix still needed before indexing | Fits in ten weeks with time for a proper golden set |
| Re-sequence | Keep everything, in order: internal staff by week 9, portal in a release 2 by week 16 | Internal part yes; the portal adds nothing to the agreed measure | High: release 2 would start before release 1 has shown the version problem is fixed | Needs a second engagement and compliance work starting now |
| Pivot | Portal first, for policyholders, to cut call volumes | No. Call volume isn't the agreed measure and has no baseline | Highest: customer-facing, on the data with the most duplicates | Not achievable in ten weeks |
| Stop | Pause until the Claims Policy duplicates are cleaned up | Not this quarter | Lowest technical risk; loses sponsor momentum and the pilot group | Clean-up is A. Novak's team, at their own pace |

## Our recommendation

**Narrow**, with the portal and the wider staff groups deferred to the backlog with clear triggers. D. Whitfield keeps both of their targets and the same go-live week. Handlers get an assistant that's been tested properly on the documents they use most, instead of a thinner one spread across 4,000 people and the public. The portal stays possible: release 1 is how Harbourline proves the version problem is fixed, which the portal needs first.

Before the wider meeting, E. Marsh walked D. Whitfield through this one to one on Tuesday. D. Whitfield chose to take the portal deferral to their director themselves, with the compliance finding as the lead reason, and asked for the backlog trigger to be written so it reads as "next", not "no".

## What changes

| Document | Change | Owner | Done |
|---|---|---|---|
| Use-case canvas | Version 2: users = internal claims handlers; Motor and Property first; claims portal and non-claims staff moved to "out of scope"; exit criteria unchanged. Re-signed by D. Whitfield | E. Marsh | Week 3, Fri |
| ADRs | ADR-001 to ADR-006 reviewed; none superseded. ADR-006's context updated: the filtered public route serves Teams for internal staff only; no portal route | E. Marsh | Week 3, Fri |
| Data audit | Duplicate clean-up prioritised to Motor and Property documents first; other lines follow | A. Novak, T. Osei | Week 4 |
| Evaluation plan | Golden set built from Motor and Property questions first; no policyholder-tone cases; release bar unchanged | M. Costa, E. Marsh | Week 4 |
| Plan / timeline | Pilot of 12 Motor handlers in week 4; go-live in week 9 to about 900 Motor and Property handlers | E. Marsh | Week 3, Fri |
| Stakeholder map | Compliance lead moved from "approves" to "informed" for release 1; added as an approver for the backlog item | E. Marsh | Week 3, Fri |

## Deferred to the backlog

| Item | Why deferred | What would have to be true to bring it back | Owner |
|---|---|---|---|
| Policyholder version in the claims portal | Changes the risk profile to customer-facing and regulated: compliance review of answers, a curated public corpus, a new internet-facing route, a stricter release bar. The data it would draw on has the most duplicates | Release 1 has met the superseded-citation target for a full quarter; a curated policyholder corpus with a named owner; compliance and security sign-off on the route; a separate engagement planned with the regulated pack | D. Whitfield |
| All 4,000 staff | No discovery evidence for non-claims staff; the Pricing oversharing widens the exposure with every group added | Discovery with at least two other staff groups; Pricing permission fix confirmed and re-tested | D. Whitfield, with L. Moreau for the permission fix |
| Other lines of business for claims handlers | Motor and Property cover the most-asked questions and the cleanest path to the measure | Release 1 live and stable; those lines' duplicates cleaned up | A. Novak |

**Agreed by (sponsor):** D. Whitfield, Head of Claims Operations · **Date:** week 3, Friday
