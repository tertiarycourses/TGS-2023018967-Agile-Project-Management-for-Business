# Activity 7 — Prioritise Defect Causes with a Pareto Chart

**Course:** Agile Project Management for Business (TGS-2023018967)  
**Topic 3:** Agile Project Execution and Tracking  
**Learning outcome:** LO3  
**Duration:** 45 minutes  
**Team size:** 3–4 learners  
**Tool:** [Pareto Chart](https://alfredang.github.io/paretochart/)  

---

## Objective

Measure progress against targets and reduce waste and defects by identifying the few causes driving most of the failures (A3, A4, A6).

## The situation

Three sprints in, CustomerConnect has accumulated 120 logged defects. The team has capacity to attack roughly two root causes in Sprint 4, and the operations manager wants all 120 fixed. The Scrum Master has categorised every defect by cause and wants the team to decide with data rather than by whoever complains loudest.

## What you will do

Your team loads the 120-defect dataset into the Pareto tool, builds the ranked bar chart with the cumulative percentage line, identifies the vital few causes crossing the 80% threshold, and converts that finding into a Sprint 4 commitment with a measurable target. You then confront the trade-off with the operations manager.

## What you will produce

A completed Pareto chart of 8 defect categories with a cumulative line, the identified vital few, and a Sprint 4 improvement commitment with a numeric target and the projected defect reduction.

## Materials

Pareto tool (alfredang.github.io/paretochart), the 120-defect dataset in the Learner Guide Activity 7

## Data files in this folder

- `data/defect-causes.csv`

## Step-by-step instructions

1. Open the Pareto tool at https://alfredang.github.io/paretochart/ and create a chart named 'CustomerConnect Defect Causes — Sprints 1–3'.
2. Enter the 8 defect categories and counts from the Learner Guide dataset: Stale or missing feed data 44; Unclear acceptance criteria 31; Environment and configuration drift 17; Carrier API contract changes 11; UI validation gaps 8; Access and permission errors 5; Report formatting 3; Documentation errors 1.
3. Confirm the total is 120. If the tool reports a different total, one category was entered twice — reconcile before reading anything from the chart.
4. Let the tool sort the categories descending and plot the cumulative percentage line. Never read a Pareto chart that is not sorted.
5. Read the cumulative line and identify where it crosses 80%. Stale/missing feed data alone is 36.7%; adding unclear acceptance criteria reaches 62.5%; adding environment drift reaches 76.7%; adding API contract changes reaches 85.8%.
6. Name the vital few: the top 3 causes account for 76.7% of all defects, and the top 4 for 85.8%. The remaining 4 categories together account for just 14.2%.
7. Connect this to Activity 6. Your 5 Whys root cause — a Definition of Done with no data-quality check — sits underneath the two largest bars, which together are 62.5% of all defects. The same fix attacks both.
8. Set a measurable Sprint 4 target: fix the top 2 causes at the root and reduce total defect inflow by at least 50% in Sprint 4, measured as defects logged per sprint.
9. Prepare the answer to the operations manager. State it in his terms: fixing 2 of 8 causes addresses 62.5% of defects, and fixing all 8 would cost roughly 3 sprints of capacity to eliminate a final 14.2%. Recommend the trade-off explicitly.
10. Export the chart and record the target in your Sprint 4 planning notes so the next retrospective can verify whether the reduction was actually achieved.

## Self-check — are you done?

> Your chart is sorted descending, the cumulative line reaches 100%, and your vital few are justified by the crossing point rather than chosen by intuition. Your Sprint 4 target is numeric and verifiable. If your recommendation is 'fix everything', you have not used the chart to make a decision.

## Debrief — what this activity proves

- Pareto turns 'everything is broken' into 'two things are broken and they cause most of it'.
- Activities 6 and 7 combine: 5 Whys finds the cause, Pareto proves it is the one worth fixing first.
- This is A3 and A4 in practice: reducing waste and defects, and measuring against a defined target rather than an impression.

---

Record your team's output in [WORKSHEET.md](WORKSHEET.md). The same instructions appear in the Learner Guide, section 6.7.
