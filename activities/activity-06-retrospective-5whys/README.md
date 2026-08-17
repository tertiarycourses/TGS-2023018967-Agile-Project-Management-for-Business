# Activity 6 — Run the Sprint Retrospective with 5 Whys Root-Cause Analysis

**Course:** Agile Project Management for Business (TGS-2023018967)  
**Topic 3:** Agile Project Execution and Tracking  
**Learning outcome:** LO3  
**Duration:** 45 minutes  
**Team size:** 3–4 learners  
**Tool:** [5 Whys](https://alfredang.github.io/5whys/)  

---

## Objective

Assess work performance and quality to ensure continuous improvement, drilling to the root cause of a delivery problem (A6, A7).

## The situation

Sprint 1 finished 6 of 20 committed points short. In the review, one customer noted that the shipment status feature 'works but shows yesterday's data'. In the retrospective, the team's first instinct is to blame the carrier data feed. The Scrum Master pushes for a real root cause, because the same class of problem appeared twice in the old waterfall project.

## What you will do

Your team runs a full retrospective in the five stages, using the 5 Whys tool on the single highest-impact problem from Sprint 1. You drive past the first plausible answer to a root cause the team can actually act on, then convert it into one SMART action with a named owner that enters the Sprint 2 backlog as a real item.

## What you will produce

A completed 5 Whys chain of at least 5 levels reaching an actionable root cause, plus one SMART improvement action with a named owner, a measure, and a place in the Sprint 2 backlog.

## Materials

5 Whys tool (alfredang.github.io/5whys), your Activity 5 impediment log and burndown

## Step-by-step instructions

1. Set the stage (5 minutes). Each member states in one word how the sprint felt. The Scrum Master states the one rule: we examine the process, not the people.
2. Gather data (10 minutes). Put the facts on the table from Activity 5: 14 of 20 points Done, the Day 3 stale-timestamp impediment, the Day 5 capacity loss, the Day 7 scope request, and the customer's review comment.
3. Choose ONE problem to analyse — the one with the largest impact on the sprint goal. Here it is 'the shipment status feature displays stale data'. Resist analysing all five problems at once.
4. Open the 5 Whys tool at https://alfredang.github.io/5whys/ and enter that problem statement.
5. Why 1: Why does it display stale data? Because the carrier feed timestamps were not refreshed within the display window.
6. Why 2: Why was that not caught before the review? Because the story's acceptance criteria did not specify a maximum data age.
7. Why 3: Why did the acceptance criteria omit it? Because the team wrote criteria for what the screen shows, not for how fresh the data must be.
8. Why 4: Why was freshness not treated as a requirement? Because the Definition of Done has no data-quality check, so nobody was required to consider it.
9. Why 5: Why does the Definition of Done omit data quality? Because it was copied from the previous project's checklist and never revisited for a real-time product. This is the root cause — and it is a process cause the team owns and can change.
10. Sanity-check the chain by reading it backwards: because the DoD was copied and not revisited, freshness was never required, so criteria omitted it, so it was not tested, so stale data shipped. If the reverse reading breaks, a link is wrong — fix it.
11. Generate insights: note that this same root cause would also have produced the two data problems in the old waterfall project. A root cause that explains prior failures too is usually the real one.
12. Decide what to do. Write ONE SMART action: 'The Scrum Master will facilitate a 30-minute DoD revision in Sprint 2 Day 1, adding a data-freshness check with a maximum age stated per data source; done when the revised DoD is agreed by all 7 members and visible on the board.'
13. Add the action to the Sprint 2 backlog as a real item with points. An improvement action with no capacity allocated is a wish, not a commitment.
14. Close the retrospective with a Plus/Delta round: one thing to keep, one thing to change about the retrospective itself.

## Self-check — are you done?

> Your chain reaches a process or system cause the team can change, not a person and not an external party. Reading it backwards with 'because' holds together at every link. Your SMART action has an owner, a measure and points in the Sprint 2 backlog. If your root cause is 'the carrier's fault', you stopped at Why 1.

## Debrief — what this activity proves

- Stopping at 'the carrier feed was stale' would have produced a ticket. Reaching the copied Definition of Done produced a systemic fix.
- A root cause you cannot act on is not a root cause — it is an excuse with a diagram.
- This is A6 in practice: assessing work performance and quality to drive continuous improvement, with PDCA closing the loop in the next sprint.

---

Record your team's output in [WORKSHEET.md](WORKSHEET.md). The same instructions appear in the Learner Guide, section 6.6.
