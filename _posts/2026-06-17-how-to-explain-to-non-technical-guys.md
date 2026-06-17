---
layout: post
title: "How to Explain Technical Issues to Non-Technical Stakeholders"
date: 2026-06-17
tags: [communication, soft-skills, career, project-management]
---

I recently got rejected from a client because I failed to communicate technical issues clearly to non-technical stakeholders. I am a tech person, so my natural instinct is to explain the problem in technical terms. That was the mistake.

Here is what I learned to do differently.

## Lead with business impact, not the problem

Non-technical people are driven by business outcomes, not technical details. They do not care what broke — they care what it costs.

Instead of saying "our database is experiencing high latency," say:

> Our database slowdown is causing customers to abandon their cart at checkout, which means we are losing revenue with every failed transaction.

The audience is the customer. The cost is revenue loss. That is what gets attention.

## Apply the "So What?" test

For every technical statement, ask: **"What does this mean to the business?"**

If you cannot answer that question clearly, your explanation is not ready for a non-technical audience. Keep asking "so what?" until you land on something that affects money, customers, or reputation.

## Use business analogies

Non-technical people do not know your technical vocabulary. Replace it with language they already understand.

| Technical term | Business analogy |
|---|---|
| Server overload | More guests than the restaurant can seat |
| Technical debt | Taking out a fast loan that still needs to be repaid |
| Latency spike | A cashier queue that suddenly tripled in length |

## Structure your message clearly

Use this three-part structure for every incident or status update:

1. **What happened** — the plain-English description of the issue
2. **Why it matters** — the business impact (customers, revenue, operations)
3. **What we are doing** — the action being taken and the expected outcome

Example:

> Our payment system is down. This is preventing customers from completing purchases, which directly impacts revenue. We are currently optimizing the database and adding capacity, and we expect full recovery within two hours.

## Quantify the impact whenever possible

Numbers make the abstract concrete. If you can attach a figure to the problem and the solution, do it.

> Payment success rate dropped by 20% due to database latency. We are scaling up resources and expect the success rate to recover to baseline within the next two hours.

---

## Managing a large project with many non-technical stakeholders

The tips above work well for a single incident or a one-on-one conversation. But when you are running a large project with multiple stakeholders across different departments, you need a more systematic approach. Here are the frameworks I use.

### 1. Stakeholder Mapping — know your audience first

Before you communicate anything, map your stakeholders using a **Power-Interest Grid**. Place each person on a two-axis grid:

- **Power** (vertical axis): How much authority do they have to make decisions or block the project?
- **Interest** (horizontal axis): How much do they care about the day-to-day details?

| | Low interest | High interest |
|---|---|---|
| **High power** | Keep satisfied — brief, infrequent updates | Manage closely — involve early, update often |
| **Low power** | Monitor — minimal effort | Keep informed — regular status updates |

A CEO typically sits in high power / low interest — they want a one-paragraph summary, not a Jira board. A department head affected by the migration sits in high power / high interest — they need to be in the loop early and often.

This grid tells you **what to say, how much detail to include, and how often to communicate** — for every person on the project.

### 2. RACI Matrix — eliminate confusion about ownership

On large projects, non-technical stakeholders often do not know who to ask when something goes wrong. A **RACI matrix** solves this.

For every major decision or deliverable, assign:

- **R — Responsible**: Who does the work
- **A — Accountable**: Who owns the outcome (only one person)
- **C — Consulted**: Who provides input before a decision
- **I — Informed**: Who is notified after a decision

Example for a database migration:

| Task | Engineer | Tech Lead | Product Manager | CTO |
|---|---|---|---|---|
| Migration plan | R | A | C | I |
| Go / No-go decision | C | C | A | A |
| Status updates to stakeholders | C | R | A | I |

When stakeholders know the matrix, they stop pinging the wrong people. It also prevents the common failure where everyone assumes someone else is handling communication.

### 3. Communication Plan — the right message to the right person at the right time

Define your communication cadence upfront and put it in writing. A simple plan covers:

| Audience | Format | Frequency | Owner |
|---|---|---|---|
| Executive sponsors | One-paragraph email summary | Weekly | Project lead |
| Department heads | Status meeting (15 min) | Bi-weekly | Project lead |
| All stakeholders | Written status report | Monthly | Tech lead |
| Affected teams | Slack update | Per milestone | Engineer |

Publishing this plan at the start of the project sets expectations. Stakeholders stop sending ad-hoc requests for updates because they know exactly when the next one is coming.

### 4. RAG Status Reporting — make project health instantly readable

For ongoing project updates, use **RAG status** (Red / Amber / Green). It gives stakeholders a health check in a single glance without requiring them to read technical detail.

| Status | Meaning |
|---|---|
| 🟢 Green | On track — no action needed from stakeholders |
| 🟡 Amber | At risk — a decision or resource may be needed soon |
| 🔴 Red | Blocked or off track — stakeholder action required now |

A weekly status report using RAG might look like this:

> **Project: Payment Platform Migration**
> Overall: 🟡 Amber
>
> - Timeline: 🟢 On track for Q3 delivery
> - Budget: 🟡 At risk — third-party licensing costs came in 15% higher than estimated
> - Scope: 🔴 Blocked — awaiting approval to defer the reporting module to Phase 2
>
> **Action required:** Approval needed on scope change by Friday to keep the timeline green.

This format works because non-technical stakeholders can skim it in 30 seconds and know exactly what needs their attention.

### 5. BLUF — put the conclusion first, always

**BLUF (Bottom Line Up Front)** is a communication technique from the military. The rule is simple: state your conclusion or request in the very first sentence. Never bury it.

Most engineers write emails like a story — build up the context, explain the technical details, then reveal the ask at the end. Busy stakeholders stop reading before they get there.

BLUF format:

> **[What you need / what happened]** — [one sentence]
> **Context:** [brief background, 2-3 sentences max]
> **Details:** [optional — for those who want to dig deeper]

Example:

> We need a decision on the reporting module scope by Friday or we will miss the Q3 deadline.
>
> **Context:** The reporting module requires an additional 3 weeks of work that was not in the original estimate. Deferring it to Phase 2 keeps everything else on schedule.
>
> **Details:** [link to scope change document]

The ask is in the first line. The context supports it. The details are optional. This works for email, Slack, status reports, and presentations.

### 6. The One-Pager — your executive communication tool

For major decisions, milestone reviews, or budget conversations, prepare a **one-pager**. One page forces you to distill complexity into what actually matters. Structure it as:

1. **Situation** — what is the current state of the project?
2. **Problem or opportunity** — what decision or issue needs attention?
3. **Options** — what are the choices? (usually two or three, with trade-offs)
4. **Recommendation** — what do you suggest and why?
5. **Ask** — what do you need from the stakeholder and by when?

Executives make decisions faster when the information is pre-structured this way. They can read, react, and respond in one meeting instead of three.

---

## Putting it all together

For a large project, the sequence is:

1. **Before the project starts** — map your stakeholders, define the RACI, and publish the communication plan
2. **During the project** — send RAG status updates on schedule, use BLUF in every written communication
3. **At decision points** — prepare a one-pager with a clear recommendation and a specific ask

The core shift remains the same as handling a single incident: move from describing the system to describing the consequence. At scale, the difference is that you also need to be deliberate about who gets what message, how often, and in what format.

Get that structure right and the technical credibility follows.
