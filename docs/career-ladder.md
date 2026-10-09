# From FDE to Principal: How the Job Changes with Seniority

> Part of the [Awesome Microsoft FDE](../README.md) guide. What changes as a forward deployed engineer (FDE) moves from early career to senior to staff and principal, what a principal actually does all week, the anti-patterns of senior FDEs, and how to build evidence for promotion.
> New to the topic? Start with the [README](../README.md) and [the FDE role and market](fde-role-and-market.md). This page assumes you know what the job is and asks how it grows.
>
> Not official Microsoft guidance, and not a description of any employer's levelling framework. See the [disclaimer](../README.md#disclaimer).

**Last verified:** 9 October 2026.

💬 Level names and expectations differ between employers, and most don't publish theirs. **The level descriptions below are our opinion from field experience**, written as three broad bands rather than any company's grades. Facts about real postings and published writing are linked inline.

## What the market asks for at each level

Most FDE postings sit in the middle. In an analysis of 1,000 postings, 12% asked for 0–2 years of experience, 60% for 3–5 years, 20% for 6–8 years and 8% for 9 or more ([Bloomberry](https://bloomberry.com/blog/i-analyzed-1000-forward-deployed-engineer-jobs-what-i-learned/); breakdown in the [role research](fde-role-and-market.md#what-the-job-postings-actually-ask-for)). Senior roles exist, but they're a minority, and they're described differently:

- Microsoft's Industry Solutions Engineering (ISE) **Principal Software Engineer** posting asks for 8+ years of coding experience and up to 50% travel. Its duties include lighthouse customer engagements and identifying recurring patterns across engagements to feed into product roadmaps ([posting](https://jobs.anitab.org/companies/microsoft/jobs/79366247-principal-software-engineer-ise), [archived](https://web.archive.org/web/20260614170608/https://jobs.anitab.org/companies/microsoft/jobs/79366247-principal-software-engineer-ise)).
- ISE also advertises a **Principal Technical Program Manager, Forward Deployed Engineering**: a programme role alongside the engineering one, which tells you that running engagements at scale is treated as a job in itself ([posting](https://jobs.anitab.org/companies/microsoft/jobs/81414702-principal-technical-program-manager-forward-deployed-engineering), [archived](https://web.archive.org/web/20260613192559/https://jobs.anitab.org/companies/microsoft/jobs/81414702-principal-technical-program-manager-forward-deployed-engineering)).
- Anthropic's FDE posting asks the engineer to codify deployment patterns for its Product and Engineering teams ([posting](https://jobs.generalcatalyst.com/companies/anthropic/jobs/70192292-forward-deployed-engineer-applied-ai)).
- Palantir describes its forward deployed engineers (Deltas) as working with Product Development teams "when new capabilities are required" ([Palantir: Who wants to be a Delta?](https://blog.palantir.com/who-wants-to-be-a-delta-8d2ea948035)), and frames the split as a Dev's "one capability for many customers" against a Delta's "one customer, many capabilities" ([Palantir: Dev versus Delta](https://blog.palantir.com/dev-versus-delta-demystifying-engineering-roles-at-palantir-ad44c2a6e87)).

💬 The thread through all of these: **seniority in this job is measured by how much of what you learn on one engagement reaches other customers.** Early career, you solve one customer's problem. At principal, you change what every future engagement starts from.

## What changes at each level 💬

| | Early career | Senior | Staff / principal |
|---|---|---|---|
| **Scope** | A workstream inside an engagement: the retrieval pipeline, the evaluation harness, the infrastructure-as-code | A whole engagement, end to end, from discovery to handover | A portfolio: several engagements, an industry, or a solution area |
| **Ambiguity** | Given a defined problem and a design | Given a customer and a vague goal; turns it into a scope and a success measure | Given a market signal or a struggling account; decides whether there's an engagement at all |
| **Concurrent engagements** | One | One, sometimes two | Several, mostly through other people |
| **Customer seniority** | Customer engineers and end users | The sponsor, security lead and architecture board | Executives on both sides; trusted enough to say "don't buy this yet" |
| **Influence on product** | Files good bugs with reproduction steps | Writes field notes that product teams act on | Owns the field-to-product loop for an area; product leaders seek them out |
| **Reuse** | Uses the team's templates and accelerators | Improves them; extracts one reusable piece per engagement | Decides which assets the organisation builds and maintains, and retires the rest |
| **Failure they own** | A component that doesn't work | An engagement that misses its outcome | A pattern of engagements failing the same way |
| **Main output** | Working code | A handed-over system and a satisfied sponsor | Other people's engagements going well, and a better product |

**The shift that catches people out** is between senior and principal. A senior FDE succeeds by being very good on site. A principal succeeds when engagements they never set foot in go well. Many excellent senior engineers stall here because they keep optimising the thing they're best at.

## The principal's job 💬

### Turning one-off fixes into reusable assets

Every engagement produces a fix that the next customer will need: a Bicep module that satisfies a common landing-zone policy, an evaluation harness, a private-networking pattern, a prompt-injection test set. A principal's habit is to ask, at the end of every engagement, "what here should never be built from scratch again?", and then to make that thing reusable: documented, tested, owned and findable.

Three forms, in rising order of effort:

1. **Skills and templates.** A checklist or template that encodes judgement: what this repository's [`/skills`](../skills/README.md) are. Cheapest to make, easiest to adopt.
2. **Accelerators.** Code that starts an engagement in week 1 instead of week 3: an infrastructure template, an evaluation pipeline, a deployable reference agent.
3. **Reference implementations.** A complete, production-shaped system for a common scenario, used to show customers and engineers what "good" looks like. Microsoft's ISE publishes its working method and tooling this way, in the [Code-With Engineering Playbook](https://microsoft.github.io/code-with-engineering-playbook/ISE/) and [HVE Core](https://microsoft.github.io/hve-core/).

An asset that only you know about isn't reusable. Count adoption by other teams, not assets created.

### Owning the field-to-product loop

[Belief #9](../README.md#-what-we-believe) says feeding what you learn back to the product is what makes this engineering and not staffing. A senior FDE writes good field notes. A principal makes sure they land: they collect field feedback across engagements, spot the pattern ("five of our last eight customers hit this private-endpoint limit"), quantify it, take it to the product group with evidence, and follow up until it's on a roadmap or explicitly declined. Use [`field-feedback`](../skills/field-feedback/SKILL.md).

### Running several engagements through other people

You can't be on site at four customers. You can:

- run the kickoff and the first sponsor conversation yourself, then hand day-to-day leadership to a senior FDE;
- read every weekly status and ask one sharp question a week on each;
- join the moments that decide outcomes: the security review, the architecture board, the go-live decision, a scope reset;
- step in fast when a warning sign from the [field guide](field-guide.md) appears, and step out again.

### Deal shaping without becoming sales

Principals get pulled into deals. Done well, this is valuable: you shape the scope so it's deliverable, set realistic success measures and stop the account team from selling something the product can't do. Done badly, you become a pre-sales engineer with a forward deployed title.

**Our rule:** help shape *what* is sold and *whether* it's deployable. Don't own the number, don't do the commercial negotiation, and don't build the demo for every opportunity.

### Technical due diligence before an engagement is sold

Before your organisation commits a team, someone should answer "is this deployable?" That's often the principal. A one-hour check with the customer's architects covers:

- **Data:** does the data exist, can we get access to it, and is it good enough? ([`data-audit`](../skills/data-audit/SKILL.md))
- **Platform:** will the landing zone, network and identity policies allow the design? Which features are in preview? ([belief #7](../README.md#-what-we-believe))
- **People:** is there a sponsor with a measurable outcome, and someone who'll own it afterwards? ([`stakeholder-map`](../skills/stakeholder-map/SKILL.md))
- **Risk:** is this a use case that needs a responsible AI review before anyone builds? ([`responsible-ai-impact-assessment`](../skills/responsible-ai-impact-assessment/SKILL.md))

If the answer is "not yet", say so and propose the smaller engagement that makes it deployable. The cheapest failed engagement is the one that was never sold.

### Mentoring and writing

A principal's leverage comes from other engineers. Pair with them on their hardest customer conversation, review their design documents and status notes, and let them run the meeting while you sit in. Write constantly: architecture decision records, field notes, internal posts on patterns, and post-incident reviews. Writing is how a principal's judgement reaches engagements they never attend.

## Anti-patterns of senior FDEs 💬

| Anti-pattern | What it looks like | Why it hurts | The fix |
|---|---|---|---|
| **Hero mode** | Fixing production at 2 a.m., every week; the customer asks for you by name | Feels like impact, but it hides a system that isn't operable and a team that isn't learning. It also burns you out | Every heroic fix becomes a runbook entry and an [`incident-review`](../skills/incident-review/SKILL.md). Then someone else handles the next one |
| **The only one who can run it** | Deployments, secrets or evaluations tied to you; handover keeps slipping | Fails [belief #8](../README.md#-what-we-believe). You can never leave, and the customer can never stop paying for you | Customer engineers on the commit history from week 1; game days before handover ([`handover`](../skills/handover/SKILL.md)) |
| **The pre-sales demo machine** | Most weeks spent on demos for opportunities; little production code shipped | You lose the field contact that made you valuable, and the demos drift from what's deployable | Cap deal support at a fixed share of your time, agreed with your manager. Prefer due diligence over demos |
| **The bespoke builder** | Every engagement starts from an empty repository | Nothing compounds; your organisation is selling hours | Start from the team's accelerators. Extract one asset per engagement |
| **The silent expert** | Strong opinions, few documents | Your judgement doesn't scale and leaves when you do | Write the ADR, the field note, the internal post |
| **The product cynic** | "Product never listens, so I don't file feedback" | Breaks the loop that justifies the job | File it with evidence anyway, track it, escalate patterns |

## Building evidence for promotion 💬

Promotion committees rarely see your best work, because the best work in this job happens inside a customer's walls. You have to bring the evidence.

**Keep a brag document.** Julia Evans' widely shared argument is that important work goes unrewarded when the people deciding don't know about it or forget it, so you should keep a running record of what you did and why it mattered ([jvns.ca: brag documents](https://jvns.ca/blog/brag-documents/)). For an FDE, build it from artefacts you already produce:

- **Handovers.** For each engagement: the outcome against the success measure, the date it went live, and the call-after-handover test. Did the customer run it without you?
- **Field feedback accepted into product.** Each field note that led to a fix, a feature or a documentation change, with a link to the item. This is the strongest evidence at senior and above, because it shows impact beyond one customer.
- **Reusable assets adopted by other teams.** Name the asset, the teams using it, and the weeks it saved them. Ask those teams for a one-line quote.
- **People.** Engineers you mentored who now lead engagements; reviews and pairing sessions.
- **Bad news handled well.** A scope reset or an incident review that saved an engagement. Committees value judgement under pressure.

Write it weekly, five lines at a time, from your [`weekly-status`](../skills/weekly-status/SKILL.md) notes. Reconstructing a year from memory doesn't work.

**Match the evidence to the level.** If your promotion case is all "I built X", it reads as senior. A principal case needs "other people and other customers did better because of me".

## Interview signals at senior level 💬

Senior and principal FDE interviews test judgement more than syntax. What interviewers listen for, in our experience:

| Signal | Strong answer | Weak answer |
|---|---|---|
| **Scoping** | Asks about the outcome and the owner before the architecture | Starts drawing services in the first minute |
| **Saying no** | A real example of trading scope with a sponsor and keeping the relationship | "I always deliver what the customer asks" |
| **Failure** | A specific engagement that went wrong, what they'd do differently, and what they changed in their process afterwards | A failure that was someone else's fault |
| **Reuse** | Names an asset they built that other teams adopted, with evidence | Every story is a bespoke build |
| **Product loop** | A piece of field feedback that changed a product, and how they got it there | "We told the product team" |
| **Leverage** | How they ran an engagement they weren't on full time; who they grew | Every success depended on them being there |
| **Handover** | Describes how they knew the customer could run it without them | Handover means "we sent the documents" |
| **Trade-offs** | Will recommend against their own employer's product when it's the wrong fit, and explain why | Every answer is the flagship product |

[Interview prep](interview-prep.md) has case studies to practise these out loud. Staff-level engineering writing outside the FDE world is useful too: Will Larson's staff engineer archetypes (tech lead, architect, solver, right hand) map loosely onto how principal FDEs specialise ([lethain.com](https://lethain.com/staff-engineer-archetypes/)).

---

← [The field guide](field-guide.md) · [The FDE role and market](fde-role-and-market.md) →
