# Activity 8 — Forecast the Release from Velocity and Read the Agile Metrics

**Course:** Agile Project Management for Business (TGS-2023018967)  
**Topic 3:** Agile Project Execution and Tracking  
**Learning outcome:** LO3  
**Duration:** 45 minutes  
**Team size:** 3–4 learners  
**Tool:** [Scrum Board](https://alfredang.github.io/scrum/)  

---

## Objective

Measure progress against targets for defined business outcomes and forecast delivery from empirical data (A4, A6, A7).

## The situation

The HarbourFront committee meets on Friday and wants one answer: when will the remaining CustomerConnect scope be delivered? The team has completed 4 sprints with velocities of 14, 18, 17 and 21 points. There are 186 points left in the backlog. The programme director wants a single date. The operations manager has separately asked why the support queue keeps growing despite the team 'going faster'.

## What you will do

Your team computes average velocity, builds a forecast range rather than a single date, plots a release burndown, and interprets a supplied cumulative flow diagram and control chart to locate the bottleneck behind the growing support queue. You then write the committee answer — a range with its assumptions stated.

## What you will produce

A velocity-based forecast range in sprints and calendar dates, a release burndown, a written interpretation of the CFD and control chart naming the bottleneck, and a one-paragraph answer to the committee.

## Materials

Scrum tool (alfredang.github.io/scrum), the velocity data and the supplied CFD/control chart in Learner Guide Activity 8

## Data files in this folder

- `data/sprint-velocity.csv`
- `data/backlog-remaining.csv`

## Step-by-step instructions

1. Record the 4 sprint velocities in the Scrum tool: 14, 18, 17, 21. Compute the average (17.5) and note the range (14 to 21).
2. Compute the forecast three ways. Average: 186 ÷ 17.5 = 10.6, so 11 sprints. Pessimistic (slowest): 186 ÷ 14 = 13.3, so 14 sprints. Optimistic (fastest): 186 ÷ 21 = 8.9, so 9 sprints.
3. Convert to calendar dates at 2 weeks per sprint: roughly 18 to 28 weeks, with 22 weeks as the most likely. Present the range, never the single number.
4. Write the assumptions the forecast depends on: the team stays stable, the backlog does not grow, the 186 points are estimated at the same scale, and no sprint is lost to other work. State them with the range — a forecast without assumptions is a promise.
5. Plot the release burndown: 186 points remaining, dropping by the average velocity each sprint, to zero. Add the pessimistic and optimistic lines to show the cone of uncertainty narrowing as sprints complete.
6. Now open the supplied cumulative flow diagram in the Learner Guide. Identify which band is widening vertically over time — the Testing band. A widening band is a bottleneck at that status.
7. Confirm it against the control chart: cycle time has risen from 3.1 days in Sprint 1 to 7.4 days in Sprint 4, while lead time has risen faster still. Work is entering faster than it is leaving Testing.
8. Explain the operations manager's growing support queue with Little's Law: Cycle Time = WIP ÷ Throughput. Velocity rose because more work was started, while throughput past the Testing constraint did not — so WIP and cycle time both rose. The team looks faster and delivers to the customer more slowly.
9. Recommend the counter-intuitive action: lower the WIP limit on Testing and stop starting new stories until Testing clears. Rising velocity with rising cycle time is a warning, not an achievement.
10. State plainly why velocity must not be a target. If the committee rewards velocity, the team inflates estimates, the forecast breaks, and the Testing bottleneck gets worse.
11. Write the one-paragraph committee answer: the range, the most likely date, the stated assumptions, the identified bottleneck, and the single action you are taking about it.

## Self-check — are you done?

> Your answer is a range with assumptions, not a single date. You identify Testing as the bottleneck from the CFD and confirm it with the control chart. You explain the growing queue with Little's Law. If your recommendation is 'increase velocity', re-read the control chart — that is what caused the problem.

## Debrief — what this activity proves

- Five metrics, one story: burndown for the sprint, release burndown for the release, velocity for the forecast, control chart for cycle time, CFD for the bottleneck.
- Velocity up and cycle time up at the same time always means WIP is up. Little's Law is not optional arithmetic.
- This is A4 in practice: measuring progress against targets for defined business outcomes — and being honest with the committee about uncertainty.

---

Record your team's output in [WORKSHEET.md](WORKSHEET.md). The same instructions appear in the Learner Guide, section 6.8.
