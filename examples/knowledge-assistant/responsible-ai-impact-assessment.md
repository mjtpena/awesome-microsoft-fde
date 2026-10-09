# Responsible AI Impact Assessment: Harbourline Policy Assistant

> **Worked example.** A filled-in [`responsible-ai-impact-assessment`](../../skills/responsible-ai-impact-assessment/SKILL.md) for a fictional engagement; see [examples](../README.md). Everything below, including names and systems, is invented. Microsoft product facts follow the [technical reference](../../docs/microsoft-technical-reference.md); check it before relying on them.

**Version:** 1.0 (signed) · **Date:** week 7, Friday · **Prepared by:** E. Marsh, T. Osei (FDEs), with M. Costa · **Reviewed by (privacy / responsible AI):** F. Lindqvist (Data Protection Officer)

Draft 0.2 went to F. Lindqvist in week 3, after the [scope reset](scope-reset.md), and draft 0.5 in week 5 with the first full evaluation run. Version 1.0 adds the week-6 incident, the week-7 evaluation and the [red-team](red-team.md) results. In the customer's repository this is `docs/responsible-ai/impact-assessment.md`.

## 1. The system

| Field | Answer |
|---|---|
| What it does, in one sentence | Answers claims handlers' policy questions in Teams, citing the current policy, section and effective date it used |
| Who uses it, and how many | Internal claims handlers only: about 900 Motor and Property handlers at go-live; pilot of 60 in week 7 |
| Where users meet it | Teams, over the source-IP-filtered route in [ADR-006](adr-006-teams-public-route.md) |
| Does it write or change anything? | No. No write tools ([ADR-004](adr-004-read-only.md)) |
| Model(s) and where they run | A model from the Foundry catalogue, deployed in Harbourline's own Azure subscription, behind the APIM (Azure API Management) gateway |
| Knowledge and data sources | Claims Policy, Underwriting and Pricing SharePoint sites; file share `published` folder. Current versions only ([ADR-003](adr-003-current-version-only.md)); retrieval trimmed to each user's document permissions |
| Related documents | [Use-case canvas](ai-use-case-canvas.md), [threat model](threat-model.md), [evaluation plan](eval-plan.md), [red-team report](red-team.md), [incident review](incident-review.md) |

## 2. Intended uses

| ID | Who | Task | Setting | Benefit |
|---|---|---|---|---|
| U1 | Motor and Property claims handler | Find the current policy rule that applies to the claim in front of them, and the clause to cite | At their desk in Teams, mid-claim | Time to a cited answer down from a median of 22 minutes; fewer superseded citations |
| U2 | Claims team leader | Check which version of a policy is current before answering a handler or reviewing a decision | Teams, during case reviews | Fewer repeat questions; consistent answers across teams |
| U3 | Quality team reviewer | Look up the policy in force to compare against a sampled decision | Teams, during the quarterly audit | Faster audit; same source of truth as handlers |

## 3. Out-of-scope, restricted and sensitive uses

| Use | Why it's out of scope | How the system discourages or prevents it |
|---|---|---|
| Deciding whether to accept, decline or settle a claim | The handler is the decision-maker; a policy lookup isn't a claim decision | Instructions decline and point to the referral criteria and team leader. Golden case GS-090 checks it every run |
| Answering policyholders, directly or by pasting answers into customer letters | Customer communication goes through compliance review; deferred at the scope reset | Not published to the claims portal. Pilot briefing and the Teams welcome message say answers are for internal reference |
| Pricing or rating decisions | Pricing drafts are confidential to G. Patel's team | Pricing content is permission-trimmed; zero pricing-draft content is a release-bar item |
| Questions about individual customers, claims or staff | The assistant has no access to claims or HR data and shouldn't receive it | Instructions and the pilot briefing ask handlers not to type claim numbers or customer names (see section 9) |
| Lines of business other than Motor and Property | Not tested in release 1 | Those policies are indexed for reference, but the golden set covers Motor and Property only. Listed as a known limitation |

**Sensitive use check:** does any output feed a decision about a person's employment, finances, health, legal status or access to a service? **Yes, indirectly.** Handlers use the answers when deciding claims, which affects policyholders' money. That's why the handler stays the decision-maker, every answer cites its source, and the quality team audits decisions as they do today. F. Lindqvist agreed this doesn't need Harbourline's extended review because the assistant makes no decision and changes nothing; it would if an action or a customer-facing channel were added.

## 4. Stakeholders

| Stakeholder | Uses it directly? | How they're affected | Potential benefit | Potential harm |
|---|---|---|---|---|
| Claims handlers | Yes | Use answers mid-claim | Less searching; more confidence in the version | Acting on a wrong answer; blamed for an assistant's error |
| Team leaders | Yes | Fewer repeat questions; review decisions that used it | Time back | Wrong answers spread if a team leader forwards one (it happened in week 6) |
| Policyholders | No | Their claims are decided by handlers who use it | Faster, more consistent decisions on the current terms | A claim decided on a wrong or superseded rule |
| Pricing team | No | Their drafts sit on an indexed site | None | Confidential drafts exposed to the wrong people |
| Policy owners (A. Novak's team) | No | Their documents are the source of every answer | Errors in documents become visible sooner | Blamed for answers drawn from content they'd marked superseded |
| Platform team | Operate it | On call after handover | Reusable pattern | Pager load if quality drifts unnoticed |

## 5. Potential harms, mitigations and tests

| Harm | Applies? | How it could happen here | Mitigation | Tested how (pass bar) | Result | Residual risk and who accepts it |
|---|---|---|---|---|---|---|
| Quality of service | Yes | Answers are worse for Property than Motor (the golden set started with Motor), or for the 140 legacy scanned policies, where text came from OCR (optical character recognition) | Golden set covers both lines; OCR output spot-checked by A. Novak's team and M. Costa; correctness reported per line of business and per source | Correctness ≥ 85% overall, and no line or source more than 5 points below the overall figure | Week 7: 90% overall; Motor 91%, Property 88%, file-share sources 87% | Low. Accepted by D. Whitfield |
| Allocation | Yes, indirectly | A wrong or superseded rule leads to a claim being underpaid or wrongly declined | Current versions only (ADR-003, amended week 6); handler decides; quality audit unchanged | Superseded-version cases GS-121 to GS-128 must retrieve no superseded copy; re-index gated by the full evaluation | All 8 pass since week 6; one affected claim in the week-6 incident was corrected before settlement | Medium until a quarter of audit data exists, then review. Accepted by D. Whitfield |
| Overreliance | Yes, **highest risk** | Handlers copy the answer without opening the cited policy, especially once it's usually right | Every answer shows the policy title, section, effective date and a link; welcome message and pilot briefing say "check the cited policy before you apply it"; must-refuse cases say "I can't find that" rather than guess | Correctness rubric checks the citation supports the claim; weekly sample of 50 production answers reviewed by M. Costa's group; pilot survey asks how often handlers open the source | Citation present in 128 of 128 cases; week-7 pilot survey: 41 of 52 handlers say they open the source "most times" | Medium. Accepted by D. Whitfield, with the weekly sample as the control |
| Privacy | Yes | Handlers paste claim numbers or customer names into questions; logs then hold personal data. Or a user sees documents they can't open | Instructions and briefing ask handlers not to; permission-trimmed retrieval; logs restricted to platform on-call and security operations; retention set by H. Ito | Low-privilege run (`svc-eval-lowpriv`) on every release and re-index; weekly sample checked for personal data in questions | Zero pricing-draft content after the red-team fix (see RT-02 in the [red-team report](red-team.md)); 3 questions in the week-7 sample contained a claim number, so the briefing was repeated | Low. Accepted by F. Lindqvist |
| Transparency | Yes | Users don't realise it's AI, think it searches everything, or can't tell where an answer came from | Teams welcome message and the assistant's name say it's an AI assistant; it states which sources it searches; answers always cite | Welcome message reviewed by F. Lindqvist; citation present on every golden case | Done; see section 8 | Low |
| Harmful or inappropriate content | Low | A user asks for something offensive or off topic | Content safety on the gateway for prompts and responses; instructions keep it to policy questions | Automated red-team scan across content-harm categories; 12 adversarial golden cases | Attack success rate within the bar agreed with R. Okafor in every category after the fix ([red-team report](red-team.md)) | Low. Accepted by R. Okafor |
| Stereotyping or demeaning output | Low | Answers about claimants paraphrase policy language in a demeaning way | Answers quote or closely paraphrase the policy; instructions forbid opinions about claimants | Red-team scan's hateful and unfair content category; M. Costa's weekly sample | No findings | Low |
| Misuse outside the intended uses | Yes | Answers pasted into customer letters or used for pricing | Section 3 controls; quality team aware | Quality audit looks for assistant wording in customer letters | First check due one quarter after go-live (owner: D. Whitfield) | Low. Accepted by D. Whitfield |

## 6. Known limitations

| Limitation | Effect on users | What users are told |
|---|---|---|
| Only Motor and Property are tested | Answers for other lines may be less reliable | "Release 1 is tested for Motor and Property policies. For other lines, check the source carefully." |
| Teams shows citations as text, not citation cards ([technical reference](../../docs/microsoft-technical-reference.md#phase-2-azure-architecture--ai-landing-zones)) | Users click a link in the answer instead of a citation panel | How to open the cited policy, in the welcome message |
| The index refreshes nightly | A policy changed today may not appear until tomorrow | "Policies changed today may not be included until the next working day." |
| It can't see claims, customer or HR data | It can't answer "what did we decide on claim X?" | Stated in the welcome message |

## 7. Human oversight

| Point | Who | What they check | How the design supports it |
|---|---|---|---|
| Before acting on an answer | The handler | That the cited policy says what the answer says, and is current | Policy title, section, effective date and link in every answer |
| Reporting a wrong answer | Any user | Flag it in one click | Thumbs-down in Teams; triaged weekly by M. Costa; real failures become golden cases |
| Monitoring quality after go-live | M. Costa's group, then S. Adeyemi's team | Weekly sample of 50 production answers; evaluation baseline as the alert threshold | Weekly retrieval check (incident action 5); [handover](handover.md) baseline |
| Turning it off | Platform on-call | | Kill switch on the gateway, used for real in week 6 ([runbook](runbook.md#kill-switch)) |

## 8. Transparency to users

- **How users are told it's AI:** the Teams app is named "Policy Assistant (AI)". The first message in every new chat says: "I'm an AI assistant. I answer from Harbourline's current claims and underwriting policies only, and I can be wrong."
- **What they're told it can and can't do:** answers policy questions with a citation; doesn't make claim decisions, see claims or customer data, or know about policies changed today.
- **What they're told to do before acting on an answer:** "Open the cited policy and check it before you apply it to a claim." Repeated in M. Costa's pilot briefing and the go-live announcement.
- **Where they report a problem:** the thumbs-down button, or the claims operations channel in Teams.
- **Where the user guidance lives, and who keeps it current:** the Claims Policy site home page; owner D. Whitfield's team, reviewed with each release.

## 9. Data handling

| Question | Answer |
|---|---|
| What data the system reads, and its classification | Claims and underwriting policies (Internal); Pricing drafts (Confidential), only for users who can open them |
| Personal data involved? Lawful basis and purpose | Not by design. Handlers' names and Entra IDs are logged with each request, for security and audit, under Harbourline's existing staff IT monitoring notice. Claim numbers and customer names shouldn't appear in questions; if they do, they're treated as claims data |
| What's logged (prompts, answers, retrieved documents) and who can read the logs | Question, answer, retrieved document IDs, user ID and timings, in Harbourline's Log Analytics workspace. Readable by platform on-call and security operations only |
| Retention period and who set it | Set by H. Ito (Records manager) in week 3 and recorded in Harbourline's records schedule, as F. Lindqvist asked, in writing |
| Where data is processed and stored (regions) | Foundry, Azure AI Search and logs in Harbourline's Azure subscription and region. Answers reach Teams through Microsoft 365 on the route accepted in ADR-006; F. Lindqvist reviewed how Microsoft 365 handles the agent's responses and accepted it. Chats with the assistant fall under Harbourline's existing Teams retention policy, confirmed by H. Ito |
| Is any data used to train or fine-tune a model? | No. No fine-tuning; questions and answers are used only for evaluation and the weekly sample |
| How a user or data subject request is handled | Through Harbourline's existing request process; the log query to find a user's requests is in the [runbook](runbook.md) |

## 10. Sign-off

| Reviewer | Role | Decision | Conditions | Date |
|---|---|---|---|---|
| F. Lindqvist | Data Protection Officer | **Approved with conditions** | 1. Monthly red-team scan and the low-privilege run after every re-index, owner S. Adeyemi after handover. 2. New review before any new user group, line of business or channel, and before the claims-portal version. 3. Briefing on keeping claim numbers and names out of questions repeated at go-live and in the go-live announcement | Week 7, Friday |
| R. Okafor | Security Architect (consulted on harms with a security cause) | Agreed | Red-team findings closed or accepted (see the [red-team report](red-team.md)) | Week 7, Friday |
| D. Whitfield | Head of Claims Operations (business owner) | Approved | Accepts the residual risks marked above | Week 7, Friday |

**Next review:** one quarter after go-live, with the first audit results; or sooner on a trigger: a new user group, line of business, channel, data source or model.
