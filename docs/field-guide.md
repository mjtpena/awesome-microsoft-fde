# The Field Guide: What Actually Goes Wrong

> Part of the [Awesome Microsoft FDE](../README.md) guide. The narrative, practitioner version of the "Mistakes we keep seeing" sections in the [pillar pages](pillars/README.md): what goes wrong on a forward deployed engineering (FDE) engagement, how to spot it early, and what to do about it.
> New to the topic? Start with the [README](../README.md) first, then [Pillar 6: Consulting and delivery](pillars/06-consulting-and-delivery.md). This page assumes you know what discovery, a weekly demo and a handover are.
>
> Not official Microsoft guidance. See the [disclaimer](../README.md#disclaimer).

**Last verified:** 9 October 2026.

💬 **Almost everything on this page is opinion from field experience**, not research. Where a fact or a study backs a point, it's linked inline. Where we give a number of days or weeks, it's a rule of thumb, not a measurement. Disagree with it on your own engagements; just don't ignore the warning signs.

Each section follows the same shape: **the pattern**, **early warning signs**, **what to do**, and **which skill helps**.

## Your first 30 days on an engagement 💬

**The pattern.** The first month decides the engagement, and most of it isn't building. Teams that spend week one writing code on their own laptops spend week six waiting for access, data and a security review they should have started on day one ([belief #2 and #3](../README.md#-what-we-believe)).

**What a principal does in week 1:**

| Day | Do this | Leave with |
|---|---|---|
| 1 | Meet the sponsor alone. Ask what they'll report upwards in 90 days, and what would make them cancel. Confirm the success measure in their words | One sentence of outcome, one number |
| 1 | File every access request you'll need for the whole engagement, not just this week: tenant accounts, subscriptions, data sources, repositories, the build pipeline | A tracked list with an owner and a date per request |
| 2 | Meet the security lead and the architecture board secretary. Show the one-page design and ask what will stop it | The review dates, the forms, and the name of the person who signs |
| 2–3 | Sit with two or three end users doing the task today. Watch, don't demo | The workarounds, and a list of real questions or records for the golden set |
| 3 | Meet the team who'll run it after you leave. Ask what they already operate and what they refuse to operate | A named owner candidate, and the platform constraints |
| 4 | Get a dev loop running, even an ugly one (see [working without your own laptop](#working-without-your-own-laptop-)) | A "hello world" deployed in the customer's environment |
| 5 | First Friday demo. Show the plan, the access tracker, the risks, and anything that runs, however small | A decisions-needed list the sponsor has seen |

**Weeks 2 to 4.** Week 2: something runs on real data, however narrow ([belief #4](../README.md#-what-we-believe)). Week 3: the evaluation plan and the first golden set exist, and the threat model has had one review. Week 4: you hold a short scope check with the sponsor. Is the success measure still right? Is anything blocked that will sink the date? This is the cheapest moment to change course.

**Early warning signs.** No named sponsor by day 3. Access requests with no owner. "The security team is busy, we'll book them later." Nobody can show you a real user. The customer's own engineers aren't in the room.

**What to do.** Treat each of these as a risk on the Friday status, with a date by which it sinks the engagement. Don't absorb them quietly.

**Skills that help:** [`engagement-kickoff`](../skills/engagement-kickoff/SKILL.md) · [`stakeholder-map`](../skills/stakeholder-map/SKILL.md) · [`access-request`](../skills/access-request/SKILL.md) · [`discovery-interview`](../skills/discovery-interview/SKILL.md) · [`ai-use-case-canvas`](../skills/ai-use-case-canvas/SKILL.md) · [`weekly-status`](../skills/weekly-status/SKILL.md)

## Working without your own laptop 💬

**The pattern.** Regulated customers often won't let your laptop touch their network. You get a customer-issued laptop or a virtual desktop, no local administrator rights, a proxy that inspects traffic, and package registries (npm, PyPI, NuGet) that are blocked or only reachable through an internal mirror. Engineers who wait for this to be "fixed" lose weeks.

**Early warning signs.** The onboarding email mentions a virtual desktop. Nobody can tell you how their own developers install a Python package. The customer's engineers develop somewhere else, or not at all.

**What to do, in roughly this order:**

1. **Ask how their own developers work, then copy it.** There is almost always an approved path: an internal package feed, a build agent pool, a sanctioned development image. Ask for that, not for exceptions.
2. **Use their package mirror.** Many Microsoft-centred organisations proxy public registries through an Azure Artifacts feed with upstream sources, which caches public packages inside the feed ([Microsoft Learn: upstream sources](https://learn.microsoft.com/azure/devops/artifacts/concepts/upstream-sources)). Point pip, npm and NuGet at that feed, and write the configuration into the repository so the next engineer doesn't rediscover it.
3. **Get a dev container working.** A `devcontainer.json` in the repository defines the toolchain once, and the same definition runs locally or in a cloud environment ([GitHub Docs: introduction to dev containers](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers), [Development Container Specification](https://containers.dev/)). Behind a proxy, budget time for the corporate root certificate inside the container image: it's the step people miss.
4. **Ask whether cloud development environments are allowed.** GitHub Codespaces runs a dev container on a cloud-hosted virtual machine ([GitHub Docs: what are Codespaces](https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces)). Microsoft Dev Box gives developers preconfigured cloud workstations that IT manages centrally ([Microsoft Learn: Dev Box](https://learn.microsoft.com/azure/dev-box/overview-what-is-microsoft-dev-box)). Either can be easier for a security team to approve than your laptop, because the customer controls the image and the network.
5. **Ask for a sandbox subscription.** A non-production subscription in the customer's tenant, with the landing-zone policies applied, lets you find the policy blockers (private endpoints only, denied regions, no public IP addresses) in week 1 instead of at go-live.
6. **Make the pipeline your dev loop if you must.** If you can't run anything locally, commit small changes and let the customer's build agents run tests and deploy to the sandbox. It's slow, so keep the changes small.

**Our take.** Don't build in your own tenant "for now" and plan to move it later. The move is never small, and everything that broke in the customer's environment is what you were paid to find.

**Skills that help:** [`access-request`](../skills/access-request/SKILL.md) · [`adr`](../skills/adr/SKILL.md) (record the dev-environment decision) · [`scenario-regulated-private`](../skills/scenario-regulated-private/SKILL.md) · [`scenario-disconnected-sovereign`](../skills/scenario-disconnected-sovereign/SKILL.md)

## Political failure modes 💬

Engagements rarely fail on code. They fail because the people around the work change, stall or compete. Here are the six we see most.

| Pattern | Early warning signs | What to do |
|---|---|---|
| **The sponsor leaves mid-engagement** | Re-organisation rumours; the sponsor delegates the Friday demo; decisions start "going upstairs" | Map a second sponsor from week 1. When it happens, ask for a 30-minute reset with the new sponsor within a week: outcome, measure, what's already proven. Expect the scope to change; reset it formally rather than carrying on as before |
| **The security lead who never has time** | Meetings moved twice; "send me the documents"; no review date | Make it small. Send a one-page threat model and three specific questions, not a 40-page pack. Ask who else can review. Escalate through the sponsor with a date: "without review by week 4, go-live moves" |
| **The shadow IT team who built a competing bot** | Someone demos "something similar" in week 2; users mention another tool; a business unit funded its own pilot | Don't compete. Meet them, learn what they built and why, and look for the part each does better. Often they own the users and you own the platform. Agree one roadmap with the sponsor. Unmanaged duplicates are how agent sprawl starts |
| **The champion who over-promises** | Your champion tells executives about features you haven't scoped; slides appear with dates you didn't give | Brief them before every executive meeting. Give them words to use: "in the pilot we're proving X; Y is on the backlog". Correct in private first, in writing second |
| **Procurement stall** | Licences, capacity or a partner contract "in progress" for weeks; the build depends on a product the customer hasn't bought | Make it a dated risk on the status. Build what doesn't depend on it. Show the sponsor the cost of waiting in weeks of team time |
| **A vendor competitor in the room** | Another vendor's engineers in the steering group; the customer asks for a bake-off | Be the person who tells the truth about trade-offs, including your own employer's products ([Pillar 6, stance 5](pillars/06-consulting-and-delivery.md#our-stance-)). Offer an agreed evaluation on the customer's own golden set. Never badmouth; let the measurements talk |

**Skills that help:** [`stakeholder-map`](../skills/stakeholder-map/SKILL.md) · [`threat-model`](../skills/threat-model/SKILL.md) · [`scope-reset`](../skills/scope-reset/SKILL.md) · [`eval-plan`](../skills/eval-plan/SKILL.md) · [`weekly-status`](../skills/weekly-status/SKILL.md)

## Scope creep, and saying no without losing the sponsor 💬

**The pattern.** Every request sounds small: "can it also do Teams?", "can it answer HR questions too?", "the CFO saw it and wants a dashboard". Each one competes with the success measure, and together they move the date.

**Early warning signs.** The demo audience grows and every new person asks for a feature. You're building things that aren't on the [`ai-use-case-canvas`](../skills/ai-use-case-canvas/SKILL.md). The success measure hasn't been mentioned in two weeks. The team is working evenings.

**What to do.**

- **Trade, don't refuse.** "Yes, and to fit it in we'd drop X or move the date by two weeks. Which do you prefer?" The sponsor decides, in writing, on the status. You never say a flat no to a sponsor; you show them the price.
- **Use the backlog as a pressure valve.** Every request goes on a visible, ranked backlog with the requester's name. People accept "not now" far more easily when they can see their item written down and ranked. The backlog is also part of the handover.
- **Re-anchor on the measure.** "Does this move the number we agreed?" If it doesn't, it's phase two.
- **Reset formally when the ground has moved.** If the sponsor, the measure or a major constraint has changed, don't patch the plan. Hold a short scope reset and re-agree the canvas.

**Skills that help:** [`scope-reset`](../skills/scope-reset/SKILL.md) · [`ai-use-case-canvas`](../skills/ai-use-case-canvas/SKILL.md) · [`weekly-status`](../skills/weekly-status/SKILL.md) · [`adr`](../skills/adr/SKILL.md)

## When the demo meets real users 💬

**The pattern.** The demo went well because the people watching wanted it to. Real users have a job to do, a workaround that already works, and no patience for a tool that's wrong.

**The "wrong once" effect.** Users who see one confident wrong answer often stop using the tool, even if it's right most of the time. Research backs this: in a series of experiments, people lost confidence in an algorithm faster than in a human after seeing both make the same mistake, and avoided the algorithm even when it outperformed the human ([Dietvorst, Simmons and Massey, 2015](https://doi.org/10.1037/xge0000033)). A follow-up found that giving people a small amount of control over the output reduced that aversion ([Dietvorst, Simmons and Massey, Management Science, 2018](https://doi.org/10.1287/mnsc.2016.2643)). In practice: show sources, make "I don't know" an acceptable answer, and let users correct or flag a response.

**Early warning signs.** Usage spikes in launch week, then falls. Users ask the old help desk "just to check". Feedback is all from the project team. Nobody can say how many people used it last week.

**What to do.**

- **Pilot with a small group that does the task every day**, not with executives. Their feedback is the only feedback that counts.
- **Train on the task, not the tool.** Show a user their own Tuesday-morning question being answered. Show what to do when it's wrong.
- **Measure usage from day one.** Weekly active users, repeat users, questions answered without escalation, and thumbs-down rate. Copilot Studio's analytics page reports sessions and engagement, resolution, escalation and abandonment for agents built there ([Microsoft Learn: Copilot Studio analytics](https://learn.microsoft.com/microsoft-copilot-studio/analytics-overview)); for code-first agents, build the same telemetry yourself.
- **Turn every reported wrong answer into a golden-set case** and say so publicly. Users forgive a mistake that visibly gets fixed.
- **Treat a serious bad answer as an incident.** Run a blameless review, fix the cause, and tell the users what changed.

**Skills that help:** [`eval-plan`](../skills/eval-plan/SKILL.md) · [`incident-review`](../skills/incident-review/SKILL.md) · [`red-team`](../skills/red-team/SKILL.md) · [`responsible-ai-impact-assessment`](../skills/responsible-ai-impact-assessment/SKILL.md) · [`go-live-readiness`](../skills/go-live-readiness/SKILL.md)

## Leaving well 💬

**The pattern.** [Belief #8](../README.md#-what-we-believe): you've succeeded when the customer runs it without you. The test is simple. **Count the routine calls you get in the month after handover.** A question about a new feature is fine. A call because a certificate expired, an index is stale or nobody knows how to deploy means the handover failed.

**Early warning signs that the handover will fail:**

- The named owner has never deployed a change or handled an alert without you watching.
- The runbook was written in the last week and nobody outside the team has followed it.
- The customer's engineers attend demos but don't commit code.
- The evaluation baseline lives on your machine, or only you know how to run it.
- Secrets, service principals or subscriptions are tied to your account.
- "We'll sort out support later."

**What to do.** Start the handover in week 1 by putting customer engineers on the commit history. From the midpoint, have the owner drive the Friday demo. Two weeks before you leave, run a game day: break something on purpose and watch the owner fix it using only the runbook. Then fix the runbook. Move every credential and resource off your identity before your last day. Write the field notes for the product team before you forget them.

**Skills that help:** [`handover`](../skills/handover/SKILL.md) · [`runbook`](../skills/runbook/SKILL.md) · [`go-live-readiness`](../skills/go-live-readiness/SKILL.md) · [`field-feedback`](../skills/field-feedback/SKILL.md)

## Keeping yourself sane 💬

**The pattern.** FDE postings commonly ask for 25 to 50% travel ([role research](fde-role-and-market.md#fde-vs-adjacent-roles-)), and travel and time pressure are the most cited downsides of the job ([Wikipedia](https://en.wikipedia.org/wiki/Forward_deployed_engineer)). Add context switching between customers, the emotional work of every political failure above, and the pull to be the hero who fixes it at midnight. The World Health Organization describes burn-out as resulting from chronic workplace stress that hasn't been successfully managed, marked by exhaustion, mental distance or cynicism about the job, and reduced professional efficacy ([WHO](https://www.who.int/news/item/28-05-2019-burn-out-an-occupational-phenomenon-international-classification-of-diseases)).

**Early warning signs.** You dread the Friday demo. You've stopped writing field notes because "what's the point". You're cynical about the customer in private. You're the only person who can deploy, so you can't take a day off.

**What to do.**

- **Protect focus time.** Batch meetings. Keep two half-days a week with no calls, and tell the customer when they are.
- **Limit concurrent engagements.** In our experience, two active engagements is the most an individual engineer can do well. A principal overseeing more does it through other people (see the [career ladder](career-ladder.md)).
- **Make travel deliberate.** Be on site for kickoff, discovery, the big reviews and handover. Do the build weeks remotely when the customer allows it.
- **Don't be the single point of failure.** If only you can run it, you can never leave, on holiday or at the end. This is the same fix as a good handover.
- **Write things down at the end of each day.** A five-line log makes the weekly status, the field notes and your promotion evidence nearly free, and it gets the day out of your head.
- **Talk to your manager early.** Saying "this engagement is burning me out" in week 4 is a resourcing problem. In week 10 it's a crisis.

**Skills that help:** [`weekly-status`](../skills/weekly-status/SKILL.md) · [`handover`](../skills/handover/SKILL.md) · [`field-feedback`](../skills/field-feedback/SKILL.md)

---

← [Pillar 6: Consulting and delivery](pillars/06-consulting-and-delivery.md) · [From FDE to principal](career-ladder.md) →
