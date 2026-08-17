"""
Topic 2 activities — Agile Essentials (LO2).

Running case continues: HarbourFront Logistics has approved a 6-sprint Agile
restart of CustomerConnect. Learners now build the backlog, run the first sprint
planning, and clarify who is accountable for what.
"""

DOMAIN2 = [
    dict(
        num=3, topic=2,
        title="Build the Product Backlog and Run Sprint 1 Planning",
        duration=60,
        objective="Implement Agile practices by converting business needs into an ordered product backlog and a committed sprint backlog with a sprint goal (K6, K7, A3).",
        lo="LO2",
        tool="Scrum Board", tool_url="https://alfredang.github.io/scrum/",
        scenario=(
            "HarbourFront's committee has approved a restart: 6 sprints of 2 weeks, one team of 7 "
            "people, and a hard demonstration to the top 5 customers in 12 weeks. Nothing from the "
            "old 96-page document is carried over unexamined. You are the team, with your trainer "
            "as Product Owner. Sprint 1 planning starts now."
        ),
        desc=(
            "Your team writes user stories from the Activity 1 customer insight, applies INVEST, "
            "estimates with planning poker using the Fibonacci sequence, orders the backlog with "
            "MoSCoW, then loads Sprint 1 to a capacity of 20 story points and writes a single "
            "sprint goal. You use the Scrum tool to hold the backlog and the sprint board."
        ),
        build=(
            "A product backlog of at least 12 estimated user stories in priority order, a Sprint 1 "
            "backlog of about 20 points, one written sprint goal, and a Definition of Done agreed "
            "by the whole team."
        ),
        services="Scrum tool (alfredang.github.io/scrum), Fibonacci planning-poker cards, the Activity 1 persona and top-3 features",
        steps=[
            ("Open the Scrum tool at https://alfredang.github.io/scrum/ and create a new project named 'CustomerConnect Restart'.", ""),
            ("Write your first three user stories from the Activity 1 top-3 features, in the form 'As a <role>, I want <goal>, so that <benefit>'. Example: 'As a warehouse operations executive, I want a live customs status on each inbound shipment, so that I can decide whether to re-sequence today's production.'", ""),
            ("Add acceptance criteria to each story using Given/When/Then. For the live-status story: 'Given a shipment in customs clearance, when I open the shipment card, then I see the current customs state and the timestamp it was last updated.'", ""),
            ("Expand the backlog to at least 12 stories. Cover the customer-facing needs, then add the enabling stories the team needs — user authentication, the carrier data feed, and an alerting service.", ""),
            ("Test every story against INVEST. Any story that cannot be finished inside one 2-week sprint fails 'Small' — split it by workflow step or by data type, never by technical layer.", ""),
            ("Run planning poker on each story. Deal the Fibonacci cards (1, 2, 3, 5, 8, 13, 21), reveal simultaneously, and have the highest and lowest estimators explain before re-voting. Record the agreed points in the tool.", ""),
            ("Any story estimated at 13 or 21 points must be split before it can enter a sprint — a number that large means the team does not yet understand it.", ""),
            ("Order the full backlog using MoSCoW. Be strict: if more than 60% of your backlog is 'Must have', you have not prioritised, you have relabelled.", ""),
            ("Write ONE sprint goal for Sprint 1 stating the business outcome, not a list of stories. Example: 'A customer can see the live status of one shipment end to end.'", ""),
            ("Pull stories from the top of the ordered backlog into Sprint 1 until you reach about 20 points. Stop at the capacity line even if the next story is attractive.", ""),
            ("Agree the team's Definition of Done as a checklist — coded, peer reviewed, tested, deployed to staging, and accepted by the Product Owner. Record it in the tool where the whole team can see it.", ""),
            ("Confirm that every story in Sprint 1 serves the sprint goal. Remove any story that does not, however small it is.", ""),
        ],
        test=(
            "Sprint 1 holds about 20 points, every story in it serves the one written sprint goal, "
            "no story exceeds 8 points, every story has Given/When/Then acceptance criteria, and "
            "the Definition of Done is visible to the whole team. A sprint whose stories serve "
            "four unrelated goals is a task list, not a sprint."
        ),
        debrief=[
            "The sprint goal is the single most skipped artefact and the one that makes the sprint reviewable.",
            "Splitting by workflow step keeps every slice demonstrable; splitting by technical layer produces a sprint with nothing to show.",
            "This is A3 in practice: implementing Agile practices to reduce waste — an ordered backlog stops the team building the 62% nobody used.",
        ],
    ),
    dict(
        num=4, topic=2,
        title="Clarify Agile Role Accountability with a RACI Matrix",
        duration=45,
        objective="Share information across teams and organise work in alignment with priorities by making Agile role accountability explicit (K5, A1, A2).",
        lo="LO2",
        tool="RACI Matrix", tool_url="https://alfredang.github.io/raci/",
        scenario=(
            "Two weeks into the restart, CustomerConnect has stalled in a familiar way. The old "
            "programme director is still approving every story change. The Scrum Master has been "
            "asked to produce a weekly percent-complete report. Two developers have escalated that "
            "they receive conflicting priorities from the Product Owner and from the operations "
            "manager. Nobody is behaving badly — the accountabilities were never made explicit."
        ),
        desc=(
            "Your team uses the RACI tool to map 12 real project decisions and activities against "
            "the five roles in play. You then find the anti-patterns — activities with two "
            "Accountables, activities with none, and roles consulted on everything — and produce "
            "the corrected matrix that resolves the conflicting-priorities escalation."
        ),
        build=(
            "A completed RACI matrix covering 12 activities across 5 roles, a list of the "
            "anti-patterns found, and the corrected matrix with the specific change that resolves "
            "the developers' escalation."
        ),
        services="RACI tool (alfredang.github.io/raci), the CustomerConnect role brief in the Learner Guide",
        steps=[
            ("Open the RACI tool at https://alfredang.github.io/raci/ and create a matrix named 'CustomerConnect Restart — Accountability'.", ""),
            ("Add the five roles as columns: Product Owner, Scrum Master, Developers, Programme Director, Operations Manager (customer proxy).", ""),
            ("Add these 12 activities as rows: order the product backlog; write acceptance criteria; estimate stories; select stories into the sprint; decide how the work is built; change the sprint scope mid-sprint; remove impediments; report progress to the committee; accept a completed story; approve the release to production; decide the Definition of Done; run the retrospective.", ""),
            ("Assign R, A, C and I for each activity. Apply the Scrum accountabilities honestly: the Product Owner is Accountable for backlog order and for accepting stories; the Developers are Accountable for how the work is built and for selecting how much enters the sprint.", ""),
            ("Assign 'change the sprint scope mid-sprint' carefully. In Scrum the Developers own the sprint content once the sprint starts; the Product Owner negotiates, and does not overrule.", ""),
            ("Now audit your matrix. Rule 1: exactly one A per row. Find every row with two A's or none.", ""),
            ("Rule 2: a role marked C on nearly every row is a bottleneck. Check whether the Programme Director is Consulted on everything — and decide which of those should become I.", ""),
            ("Rule 3: R with no A is orphaned work, and A with no R is a manager with nobody doing the work. Fix both.", ""),
            ("Trace the developers' escalation through your matrix. Two roles giving priorities means two A's on 'order the product backlog'. Resolve it by making the Product Owner the single A and the Operations Manager a C.", ""),
            ("Change 'report progress to the committee' from a percent-complete report to a sprint review demonstration, and reassign the R accordingly.", ""),
            ("Export the corrected matrix. Write two sentences on which single change would most reduce the team's confusion, and why.", ""),
        ],
        test=(
            "Every one of the 12 rows has exactly one A. No role is C on more than about half the "
            "rows. The developers' conflicting-priorities escalation is traceable to a specific "
            "duplicate A in your first draft, and your corrected matrix removes it."
        ),
        debrief=[
            "Most Agile 'transformation failures' are accountability failures wearing an Agile label.",
            "The single A rule is what makes a Product Owner viable. Two Accountables for backlog order guarantees the escalation you just resolved.",
            "This is A1 and A2 in practice: sharing information across teams to bridge operational barriers, and organising work in line with actual priorities.",
        ],
    ),
]
