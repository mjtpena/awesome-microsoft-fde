# Discovery Interviews: Harbourline Policy Assistant

> **Worked example.** Four filled-in [`discovery-interview`](../../skills/discovery-interview/SKILL.md) sheets for a fictional engagement; see [examples](../README.md). Everything below, including names and systems, is invented. In the customer's repository each interview is its own file under `docs/engagement/discovery/`; they're on one page here so you can read them together.

**Interviewers:** E. Marsh (lead FDE), T. Osei (second FDE) · **When:** week 1, days 2–4 · **Also done, not shown:** a second end user (a Property handler), A. Novak (data owner), and a day shadowing 30 handlers

## Scenario questions (knowledge assistant)

Pasted from the [knowledge-assistant scenario pack](../../skills/scenario-knowledge-assistant/SKILL.md#discovery-questions) and asked in every interview. Answers combined across interviews.

1. **What are the 20 questions people ask most? Where do they look today?** M. Costa listed 14 on the spot; the rest came from a week of the claims helpdesk queue. They start in the Claims Policy site, then Underwriting, then the file share. The 20 became the first golden-set cases in the [evaluation plan](eval-plan.md).
2. **Which documents are authoritative, and which are drafts or out of date?** Underwriting has a `Status` column that A. Novak's team maintains. Claims Policy has no reliable flag. Nobody could say which file-share documents are still in force.
3. **Who should not see which documents?** Pricing drafts: pricing team only. R. Okafor assumed this was already enforced. It isn't (see the [data audit](data-audit.md)).
4. **How often do the documents change, and how quickly must the assistant reflect changes?** A handful a week; A. Novak wants a changed policy live by the next working day.
5. **What's the cost of a wrong answer?** A claim paid or declined on a superseded rule: a complaint, a remediation exercise, and a finding in the quality audit. Not an annoyed employee.

## 1. D. Whitfield, Head of Claims Operations

**Date:** week 1, day 2 · **Interviewer:** E. Marsh · **Role type:** Sponsor

### For everyone (D. Whitfield)

1. **Good outcome in six months:** "Handlers stop asking each other which version is current." Measured by the quality audit and handle time.
2. **Today:** complex claims stall while handlers search. Team leaders answer the same policy questions repeatedly.
3. **Most annoying part:** the audit keeps finding superseded policies cited, and D. Whitfield has to explain it upwards each quarter.
4. **Tried before:** a policy index page on SharePoint in an earlier year. Nobody maintained it after its owner moved roles.
5. **What would make it fail:** "If it's confidently wrong once in front of the wrong person."

### Sponsor

- **Number reported upwards:** the quality audit's superseded-policy rate and average handle time on complex claims.
- **Running budget:** K. Brennan (IT Finance) owns it; D. Whitfield will fund it from the claims operations budget if the measure moves.
- **Who could stop it:** R. Okafor (security), G. Patel (anything touching pricing). D. Whitfield also wants a customer-facing version in the claims portal and access for all 4,000 staff. We noted this as a scope risk for the [canvas](ai-use-case-canvas.md).

### Notes (D. Whitfield)

| Quote / observation | Implication | Follow-up |
|---|---|---|
| "I want it in the portal for customers too" | Customer-facing answers are a different risk class | Raise in the canvas; revisited at the [week-3 scope reset](scope-reset.md) |
| Audit rate is reported quarterly | The success measure needs a quarter after go-live | Agree the timeframe in the canvas |

**The five whys:** handlers want answers faster → searching takes too long → three SharePoint sites and a file share, no current flag → claims get decided on old rules → audit findings and rework → **business measure:** superseded-policy citations in the quarterly audit (today 1 in 12).

## 2. M. Costa, Motor claims team leader

**Date:** week 1, day 3 · **Interviewer:** T. Osei · **Role type:** End user

### For everyone (M. Costa)

1. **Good outcome:** new handlers answer their own policy questions in their first month.
2. **Today:** shown live. Searched Claims Policy for "excess windscreen", got 11 results, opened four, checked dates by hand, then messaged a colleague to confirm.
3. **Most annoying part:** "Search finds everything except the right one."
4. **Tried before:** bookmarks and a personal folder of PDFs. They go out of date without anyone noticing.
5. **What would make it fail:** answers without the source, or slower than asking the person next to you.

### End users

- **Shown:** four systems touched for one question, two copy-pastes into the claim notes.
- **How they know it's right:** the document date and asking a senior handler. Neither is reliable.
- **What would make them stop:** one wrong answer they'd been told to trust.

### Notes (M. Costa)

| Quote / observation | Implication | Follow-up |
|---|---|---|
| **Shadowing (30 handlers, one day):** a median of 22 minutes per complex claim spent finding the right policy | The baseline for the success measure | Recorded in the [canvas](ai-use-case-canvas.md); re-measure after go-live |
| Copies a policy paragraph into claim notes | Citations need title, version and link the handler can paste | Citation format in the [agent instructions](agent-instructions.md) |
| Would co-write test questions with A. Novak | Golden-set authors | M. Costa and A. Novak own the golden set |

**The five whys:** wants a single search → results are noisy → old versions sit beside current ones → has to check with colleagues → time lost on every complex claim → **business measure:** median time to a cited policy answer (today 22 minutes).

## 3. R. Okafor, Security Architect

**Date:** week 1, day 3 · **Interviewer:** E. Marsh · **Role type:** Security

### For everyone (R. Okafor)

1. **Good outcome:** an AI system that passed review once and stays inside the rules.
2. **Today:** new systems go through architecture review and a threat model; about four weeks.
3. **Most annoying part:** projects arrive at review already built.
4. **Tried before:** a chatbot pilot was rejected because it sent data to an external service.
5. **What would make it fail:** data leakage, or anything public-facing without a documented exception.

### Security and risk

- **Review:** threat model plus architecture review board. Most rejections are for public endpoints and shared keys.
- **Classifications:** Internal and Confidential. Pricing drafts are Confidential.
- **Standards:** Entra sign-in only, no keys; private endpoints; logs to the security operations Log Analytics workspace.

### Notes (R. Okafor)

| Quote / observation | Implication | Follow-up |
|---|---|---|
| "Nothing public. No exceptions without an ADR." | Teams publishing will need an exception | [ADR-006](adr-006-teams-public-route.md); [threat model](threat-model.md) TB1 |
| Wants to see the threat model in week 2, not week 8 | Early review shortens the four weeks | Threat model v0.3 booked for week 2, day 4 |

**The five whys:** wants no new public endpoints → each one is attack surface → past incidents came from forgotten endpoints → findings delay audits → **business measure:** zero high findings at architecture review.

## 4. S. Adeyemi, Platform team lead

**Date:** week 1, day 4 · **Interviewer:** T. Osei · **Role type:** Operator

### For everyone (S. Adeyemi)

1. **Good outcome:** "My team can run it at 3am without calling you."
2. **Today:** the platform team runs Azure landing zones and the shared APIM instance.
3. **Most annoying part:** inheriting systems with no runbook and no tests.
4. **Tried before:** n/a for AI; a previous vendor left a hand-deployed app.
5. **What would make it fail:** anything not deployed from code, or in a language the team doesn't use.

### Operator / platform team

- **Needs:** Bicep, Python, alerts into the existing on-call rota, a [runbook](runbook.md).
- **Deployments:** Azure DevOps pipelines; S. Adeyemi approves production.
- **What breaks most:** expired credentials and silent indexing failures.

### Notes (S. Adeyemi)

| Quote / observation | Implication | Follow-up |
|---|---|---|
| "Silent indexing failures" | Index freshness needs an alert | Re-index check in the runbook; later part of the [ADR-003](adr-003-current-version-only.md) amendment |
| Will be named owner after handover | Pair from week 4, not week 10 | [Handover](handover.md) plan |

**The five whys:** wants code-deployed systems → hand-built ones can't be rebuilt → outages last longer → on-call load rises → **business measure:** time to restore service.
