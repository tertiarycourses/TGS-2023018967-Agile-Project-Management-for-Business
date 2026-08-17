"""
Topic 3 activities — Agile Project Execution and Tracking (LO3).

Running case concludes: CustomerConnect Sprint 1 is executed and tracked, Sprint 2
is diagnosed and improved, defects are prioritised, and the team forecasts the
remaining releases from real velocity data.
"""

DOMAIN3 = [
    dict(
        num=5, topic=3,
        title="Execute Sprint 1 and Track It on the Scrum Board",
        duration=60,
        objective="Measure progress against targets on a regular basis by executing a sprint on a live board and reading the burndown (K5, A4, A7).",
        lo="LO3",
        tool="Scrum Board", tool_url="https://alfredang.github.io/scrum/",
        scenario=(
            "Sprint 1 of the CustomerConnect restart runs for 10 working days with a committed 20 "
            "points. Your team will simulate all 10 days in compressed time, holding a daily "
            "stand-up each 'day', moving cards, and hitting three real impediments the trainer "
            "injects: the carrier data feed returns stale timestamps on Day 3, a developer is "
            "pulled onto a production incident on Day 5, and the Product Owner requests a new "
            "story mid-sprint on Day 7."
        ),
        desc=(
            "Using your Sprint 1 backlog from Activity 3, your team runs the sprint day by day on "
            "the Scrum board. Each simulated day you hold a 3-minute stand-up answering the three "
            "questions, move cards across To Do / In Progress / Testing / Done, respect a WIP "
            "limit of 3 in progress, log impediments, and update the burndown. You handle each "
            "injected impediment as the framework prescribes."
        ),
        build=(
            "A completed 10-day sprint board, a burndown chart with all 10 data points, an "
            "impediment log with the resolution of each of the 3 injections, and the actual "
            "velocity achieved."
        ),
        services="Scrum tool (alfredang.github.io/scrum), the Sprint 1 backlog from Activity 3, the trainer's impediment cards",
        steps=[
            ("Open your 'CustomerConnect Restart' project in the Scrum tool and switch to the sprint board. Confirm Sprint 1 holds the stories and points you committed in Activity 3.", ""),
            ("Set a WIP limit of 3 on the In Progress column. This is the constraint that makes the simulation behave like a real team.", ""),
            ("Record the sprint's starting total in points and plot Day 0 on the burndown. Draw the ideal line from the starting total to zero at Day 10.", ""),
            ("Day 1–2: each team member pulls ONE story, moves it to In Progress, and works it. Hold a 3-minute stand-up: what did I finish, what am I taking next, what is blocking me. Move only genuinely finished work to Done — finished means it meets the Definition of Done.", ""),
            ("Day 3 — impediment 1: the carrier feed returns stale timestamps. Log it as an impediment, not as a story. Decide as a team whether the affected story can still meet the Definition of Done; if it cannot, move it back and record why. The Scrum Master owns removing this, and the sprint goal does not change.", ""),
            ("Update the burndown each day. When you plot Day 3, notice the line flattening — a flat burndown means work is being started but not finished, which is the signal to check your WIP.", ""),
            ("Day 5 — impediment 2: a developer is pulled to a production incident for two days. Recalculate remaining capacity, and decide as a team which committed story is at risk. Tell the Product Owner the same day — surfacing it on Day 9 is the failure, not the capacity loss itself.", ""),
            ("Day 7 — impediment 3: the Product Owner asks for a new 5-point story mid-sprint. Apply the framework: the Developers own the sprint content. Either the new story displaces an equal-sized committed story by agreement, or it goes to the top of the product backlog for Sprint 2. Record which you chose and why.", ""),
            ("Day 8–10: drive the remaining work to Done. Any story not meeting the Definition of Done at Day 10 returns to the product backlog at its original estimate — never count it as partially done.", ""),
            ("Compute your actual velocity: the total points of stories that fully met the Definition of Done. Record it in the tool, and record the points that carried over separately.", ""),
            ("Hold a 10-minute Sprint Review. Demonstrate the increment against the sprint goal you wrote in Activity 3, and have another team act as the customer and give feedback.", ""),
            ("Export the board, the burndown and the impediment log into your Activity 5 worksheet.", ""),
        ],
        test=(
            "Your burndown has 10 plotted points and an ideal line. Your velocity counts only "
            "fully-Done stories, with carryover recorded separately. All 3 impediments are logged "
            "with a decision and a rationale. If your burndown is a straight diagonal line, you "
            "have plotted the plan, not the sprint — plot what actually happened."
        ),
        debrief=[
            "The flat burndown on Day 3 is the most valuable thing on the chart. It is an early warning, and it only appears if the board is honest.",
            "Carryover counted as velocity destroys forecasting. Velocity must mean 'Done', or every forecast built on it is fiction.",
            "The Day 7 injection is the real test of Agile discipline: welcoming change does not mean accepting unbounded scope inside a committed sprint.",
        ],
    ),
    dict(
        num=6, topic=3,
        title="Run the Sprint Retrospective with 5 Whys Root-Cause Analysis",
        duration=45,
        objective="Assess work performance and quality to ensure continuous improvement, drilling to the root cause of a delivery problem (A6, A7).",
        lo="LO3",
        tool="5 Whys", tool_url="https://alfredang.github.io/5whys/",
        scenario=(
            "Sprint 1 finished 6 of 20 committed points short. In the review, one customer noted "
            "that the shipment status feature 'works but shows yesterday's data'. In the "
            "retrospective, the team's first instinct is to blame the carrier data feed. The Scrum "
            "Master pushes for a real root cause, because the same class of problem appeared twice "
            "in the old waterfall project."
        ),
        desc=(
            "Your team runs a full retrospective in the five stages, using the 5 Whys tool on the "
            "single highest-impact problem from Sprint 1. You drive past the first plausible "
            "answer to a root cause the team can actually act on, then convert it into one SMART "
            "action with a named owner that enters the Sprint 2 backlog as a real item."
        ),
        build=(
            "A completed 5 Whys chain of at least 5 levels reaching an actionable root cause, plus "
            "one SMART improvement action with a named owner, a measure, and a place in the Sprint "
            "2 backlog."
        ),
        services="5 Whys tool (alfredang.github.io/5whys), your Activity 5 impediment log and burndown",
        steps=[
            ("Set the stage (5 minutes). Each member states in one word how the sprint felt. The Scrum Master states the one rule: we examine the process, not the people.", ""),
            ("Gather data (10 minutes). Put the facts on the table from Activity 5: 14 of 20 points Done, the Day 3 stale-timestamp impediment, the Day 5 capacity loss, the Day 7 scope request, and the customer's review comment.", ""),
            ("Choose ONE problem to analyse — the one with the largest impact on the sprint goal. Here it is 'the shipment status feature displays stale data'. Resist analysing all five problems at once.", ""),
            ("Open the 5 Whys tool at https://alfredang.github.io/5whys/ and enter that problem statement.", ""),
            ("Why 1: Why does it display stale data? Because the carrier feed timestamps were not refreshed within the display window.", ""),
            ("Why 2: Why was that not caught before the review? Because the story's acceptance criteria did not specify a maximum data age.", ""),
            ("Why 3: Why did the acceptance criteria omit it? Because the team wrote criteria for what the screen shows, not for how fresh the data must be.", ""),
            ("Why 4: Why was freshness not treated as a requirement? Because the Definition of Done has no data-quality check, so nobody was required to consider it.", ""),
            ("Why 5: Why does the Definition of Done omit data quality? Because it was copied from the previous project's checklist and never revisited for a real-time product. This is the root cause — and it is a process cause the team owns and can change.", ""),
            ("Sanity-check the chain by reading it backwards: because the DoD was copied and not revisited, freshness was never required, so criteria omitted it, so it was not tested, so stale data shipped. If the reverse reading breaks, a link is wrong — fix it.", ""),
            ("Generate insights: note that this same root cause would also have produced the two data problems in the old waterfall project. A root cause that explains prior failures too is usually the real one.", ""),
            ("Decide what to do. Write ONE SMART action: 'The Scrum Master will facilitate a 30-minute DoD revision in Sprint 2 Day 1, adding a data-freshness check with a maximum age stated per data source; done when the revised DoD is agreed by all 7 members and visible on the board.'", ""),
            ("Add the action to the Sprint 2 backlog as a real item with points. An improvement action with no capacity allocated is a wish, not a commitment.", ""),
            ("Close the retrospective with a Plus/Delta round: one thing to keep, one thing to change about the retrospective itself.", ""),
        ],
        test=(
            "Your chain reaches a process or system cause the team can change, not a person and "
            "not an external party. Reading it backwards with 'because' holds together at every "
            "link. Your SMART action has an owner, a measure and points in the Sprint 2 backlog. "
            "If your root cause is 'the carrier's fault', you stopped at Why 1."
        ),
        debrief=[
            "Stopping at 'the carrier feed was stale' would have produced a ticket. Reaching the copied Definition of Done produced a systemic fix.",
            "A root cause you cannot act on is not a root cause — it is an excuse with a diagram.",
            "This is A6 in practice: assessing work performance and quality to drive continuous improvement, with PDCA closing the loop in the next sprint.",
        ],
    ),
    dict(
        num=7, topic=3,
        title="Prioritise Defect Causes with a Pareto Chart",
        duration=45,
        objective="Measure progress against targets and reduce waste and defects by identifying the few causes driving most of the failures (A3, A4, A6).",
        lo="LO3",
        tool="Pareto Chart", tool_url="https://alfredang.github.io/paretochart/",
        scenario=(
            "Three sprints in, CustomerConnect has accumulated 120 logged defects. The team has "
            "capacity to attack roughly two root causes in Sprint 4, and the operations manager "
            "wants all 120 fixed. The Scrum Master has categorised every defect by cause and "
            "wants the team to decide with data rather than by whoever complains loudest."
        ),
        desc=(
            "Your team loads the 120-defect dataset into the Pareto tool, builds the ranked bar "
            "chart with the cumulative percentage line, identifies the vital few causes crossing "
            "the 80% threshold, and converts that finding into a Sprint 4 commitment with a "
            "measurable target. You then confront the trade-off with the operations manager."
        ),
        build=(
            "A completed Pareto chart of 8 defect categories with a cumulative line, the "
            "identified vital few, and a Sprint 4 improvement commitment with a numeric target "
            "and the projected defect reduction."
        ),
        services="Pareto tool (alfredang.github.io/paretochart), the 120-defect dataset in the Learner Guide Activity 7",
        steps=[
            ("Open the Pareto tool at https://alfredang.github.io/paretochart/ and create a chart named 'CustomerConnect Defect Causes — Sprints 1–3'.", ""),
            ("Enter the 8 defect categories and counts from the Learner Guide dataset: Stale or missing feed data 44; Unclear acceptance criteria 31; Environment and configuration drift 17; Carrier API contract changes 11; UI validation gaps 8; Access and permission errors 5; Report formatting 3; Documentation errors 1.", ""),
            ("Confirm the total is 120. If the tool reports a different total, one category was entered twice — reconcile before reading anything from the chart.", ""),
            ("Let the tool sort the categories descending and plot the cumulative percentage line. Never read a Pareto chart that is not sorted.", ""),
            ("Read the cumulative line and identify where it crosses 80%. Stale/missing feed data alone is 36.7%; adding unclear acceptance criteria reaches 62.5%; adding environment drift reaches 76.7%; adding API contract changes reaches 85.8%.", ""),
            ("Name the vital few: the top 3 causes account for 76.7% of all defects, and the top 4 for 85.8%. The remaining 4 categories together account for just 14.2%.", ""),
            ("Connect this to Activity 6. Your 5 Whys root cause — a Definition of Done with no data-quality check — sits underneath the two largest bars, which together are 62.5% of all defects. The same fix attacks both.", ""),
            ("Set a measurable Sprint 4 target: fix the top 2 causes at the root and reduce total defect inflow by at least 50% in Sprint 4, measured as defects logged per sprint.", ""),
            ("Prepare the answer to the operations manager. State it in his terms: fixing 2 of 8 causes addresses 62.5% of defects, and fixing all 8 would cost roughly 3 sprints of capacity to eliminate a final 14.2%. Recommend the trade-off explicitly.", ""),
            ("Export the chart and record the target in your Sprint 4 planning notes so the next retrospective can verify whether the reduction was actually achieved.", ""),
        ],
        test=(
            "Your chart is sorted descending, the cumulative line reaches 100%, and your vital few "
            "are justified by the crossing point rather than chosen by intuition. Your Sprint 4 "
            "target is numeric and verifiable. If your recommendation is 'fix everything', you "
            "have not used the chart to make a decision."
        ),
        debrief=[
            "Pareto turns 'everything is broken' into 'two things are broken and they cause most of it'.",
            "Activities 6 and 7 combine: 5 Whys finds the cause, Pareto proves it is the one worth fixing first.",
            "This is A3 and A4 in practice: reducing waste and defects, and measuring against a defined target rather than an impression.",
        ],
    ),
    dict(
        num=8, topic=3,
        title="Forecast the Release from Velocity and Read the Agile Metrics",
        duration=45,
        objective="Measure progress against targets for defined business outcomes and forecast delivery from empirical data (A4, A6, A7).",
        lo="LO3",
        tool="Scrum Board", tool_url="https://alfredang.github.io/scrum/",
        scenario=(
            "The HarbourFront committee meets on Friday and wants one answer: when will the "
            "remaining CustomerConnect scope be delivered? The team has completed 4 sprints with "
            "velocities of 14, 18, 17 and 21 points. There are 186 points left in the backlog. The "
            "programme director wants a single date. The operations manager has separately asked "
            "why the support queue keeps growing despite the team 'going faster'."
        ),
        desc=(
            "Your team computes average velocity, builds a forecast range rather than a single "
            "date, plots a release burndown, and interprets a supplied cumulative flow diagram "
            "and control chart to locate the bottleneck behind the growing support queue. You then "
            "write the committee answer — a range with its assumptions stated."
        ),
        build=(
            "A velocity-based forecast range in sprints and calendar dates, a release burndown, a "
            "written interpretation of the CFD and control chart naming the bottleneck, and a "
            "one-paragraph answer to the committee."
        ),
        services="Scrum tool (alfredang.github.io/scrum), the velocity data and the supplied CFD/control chart in Learner Guide Activity 8",
        steps=[
            ("Record the 4 sprint velocities in the Scrum tool: 14, 18, 17, 21. Compute the average (17.5) and note the range (14 to 21).", ""),
            ("Compute the forecast three ways. Average: 186 ÷ 17.5 = 10.6, so 11 sprints. Pessimistic (slowest): 186 ÷ 14 = 13.3, so 14 sprints. Optimistic (fastest): 186 ÷ 21 = 8.9, so 9 sprints.", ""),
            ("Convert to calendar dates at 2 weeks per sprint: roughly 18 to 28 weeks, with 22 weeks as the most likely. Present the range, never the single number.", ""),
            ("Write the assumptions the forecast depends on: the team stays stable, the backlog does not grow, the 186 points are estimated at the same scale, and no sprint is lost to other work. State them with the range — a forecast without assumptions is a promise.", ""),
            ("Plot the release burndown: 186 points remaining, dropping by the average velocity each sprint, to zero. Add the pessimistic and optimistic lines to show the cone of uncertainty narrowing as sprints complete.", ""),
            ("Now open the supplied cumulative flow diagram in the Learner Guide. Identify which band is widening vertically over time — the Testing band. A widening band is a bottleneck at that status.", ""),
            ("Confirm it against the control chart: cycle time has risen from 3.1 days in Sprint 1 to 7.4 days in Sprint 4, while lead time has risen faster still. Work is entering faster than it is leaving Testing.", ""),
            ("Explain the operations manager's growing support queue with Little's Law: Cycle Time = WIP ÷ Throughput. Velocity rose because more work was started, while throughput past the Testing constraint did not — so WIP and cycle time both rose. The team looks faster and delivers to the customer more slowly.", ""),
            ("Recommend the counter-intuitive action: lower the WIP limit on Testing and stop starting new stories until Testing clears. Rising velocity with rising cycle time is a warning, not an achievement.", ""),
            ("State plainly why velocity must not be a target. If the committee rewards velocity, the team inflates estimates, the forecast breaks, and the Testing bottleneck gets worse.", ""),
            ("Write the one-paragraph committee answer: the range, the most likely date, the stated assumptions, the identified bottleneck, and the single action you are taking about it.", ""),
        ],
        test=(
            "Your answer is a range with assumptions, not a single date. You identify Testing as "
            "the bottleneck from the CFD and confirm it with the control chart. You explain the "
            "growing queue with Little's Law. If your recommendation is 'increase velocity', "
            "re-read the control chart — that is what caused the problem."
        ),
        debrief=[
            "Five metrics, one story: burndown for the sprint, release burndown for the release, velocity for the forecast, control chart for cycle time, CFD for the bottleneck.",
            "Velocity up and cycle time up at the same time always means WIP is up. Little's Law is not optional arithmetic.",
            "This is A4 in practice: measuring progress against targets for defined business outcomes — and being honest with the committee about uncertainty.",
        ],
    ),
]
