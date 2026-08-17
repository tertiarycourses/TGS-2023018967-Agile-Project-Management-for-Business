"""
Topic 1 activities — Introduction to Agile Project Management (LO1).

Running case: HarbourFront Logistics Pte Ltd, a 140-staff Singapore third-party
logistics (3PL) provider. Its "CustomerConnect" self-service tracking portal ran
as an 11-month waterfall project, was delivered 4 months late, and 62% of the
shipped features are unused. The company is deciding whether to restart the
programme using Agile. Learners work this case throughout Day 1.
"""

DOMAIN1 = [
    dict(
        num=1, topic=1,
        title="Empathise with the Customer to Reframe a Failing Project",
        duration=45,
        objective="Analyse current and future customer needs and preferences using Design Thinking to reframe requirements around customer value (K2, A5).",
        lo="LO1",
        tool="Design Thinking", tool_url="https://alfredang.github.io/designthinking/",
        scenario=(
            "HarbourFront Logistics spent 11 months building the CustomerConnect portal from a "
            "signed-off 96-page requirements document. Six months after launch, only 3 of 24 "
            "features are used weekly. The top customer complaint to the call centre is still "
            '"where is my shipment right now?" — a question the portal was supposed to answer. '
            "You are the newly appointed Agile project lead. Before writing a single new "
            "requirement, you must understand the customer."
        ),
        desc=(
            "Working in teams of 3–4 as the CustomerConnect project team, you use the Design "
            "Thinking tool to build an empathy map and a persona for Priya Menon, a warehouse "
            "operations executive at a HarbourFront customer who tracks 40–60 inbound shipments "
            "a week. You then reframe the original requirement statement into a customer-value "
            "problem statement and identify the three highest-value features to deliver first."
        ),
        build=(
            "A completed empathy map and persona for Priya Menon, a reframed problem statement, "
            "and a ranked list of the top 3 customer-value features with the reasoning for each."
        ),
        services="Design Thinking tool (alfredang.github.io/designthinking), the HarbourFront case brief, team flip chart",
        steps=[
            ("Open the Design Thinking tool at https://alfredang.github.io/designthinking/ and start a new canvas named 'CustomerConnect — Priya Menon'.", ""),
            ("Read the HarbourFront case brief in the Learner Guide, Activity 1. Highlight every statement that is evidence about the customer, and ignore statements that are internal opinion.", ""),
            ("In the EMPATHISE stage, complete the four quadrants for Priya. SAYS: 'I just need to know if it clears customs today.' THINKS: 'If I guess wrong I hold up the whole production line.' DOES: refreshes the portal, then calls the hotline anyway. FEELS: anxious, and not trusted with information.", ""),
            ("Add the pains and gains. Pains: no real-time status, 6 clicks to reach a shipment, no alerting. Gains: one glance to confirm arrival, an alert before a delay affects production.", ""),
            ("In the DEFINE stage, write the reframed problem statement in the form: 'Priya, a warehouse operations executive, needs a way to know the live customs and delivery status of her inbound shipments, because guessing wrong stops her production line.'", ""),
            ("Compare your reframed statement with the original requirement: 'The system shall provide a shipment reporting module with configurable export formats.' Note in one sentence what the original optimised for instead of the customer.", ""),
            ("In the IDEATE stage, generate at least 8 feature ideas that would satisfy the reframed statement. Do not evaluate while generating.", ""),
            ("Rank the ideas by customer value and select the top 3. For each, write one sentence stating the benefit to Priya, not the feature description.", ""),
            ("Export or screenshot the canvas and paste it into your team's Activity 1 worksheet. Nominate one member to present the reframed statement in 90 seconds.", ""),
        ],
        test=(
            "Your reframed problem statement names a specific user, a specific need and a "
            "specific consequence — and contains no solution or technology. Your top 3 features "
            "each state a customer benefit. If any 'feature' is a module name or a format, it is "
            "still a requirement, not a value statement — rewrite it."
        ),
        debrief=[
            "The original project delivered exactly what was signed off, and still failed. Signed-off scope is not the same as delivered value.",
            "Empathising took 45 minutes. It would have changed 11 months of build.",
            "This is K2 in practice: analysing current and future customer needs is a repeatable method, not an intuition.",
        ],
    ),
    dict(
        num=2, topic=1,
        title="Diagnose the Waterfall Failure with a Fishbone Analysis",
        duration=45,
        objective="Analyse the current business operating landscape and diagnose why a waterfall delivery failed, using cause-and-effect analysis (K1, K3, A2).",
        lo="LO1",
        tool="Fishbone", tool_url="https://alfredang.github.io/fishbone/",
        scenario=(
            "The HarbourFront management committee wants to know why CustomerConnect was 4 months "
            "late and 62% unused before it approves any new funding. The programme director's "
            'explanation was "the team underestimated". The CEO is not satisfied with that answer '
            "and has asked your team for a structured diagnosis by Friday."
        ),
        desc=(
            "Your team uses the Fishbone (Ishikawa) tool to analyse the problem statement "
            "'CustomerConnect delivered late and mostly unused'. You populate six cause "
            "categories, identify which causes are structural to the waterfall approach rather "
            "than failures of individual effort, and mark which ones an Agile approach would "
            "actually address. You then write a one-page recommendation to the committee."
        ),
        build=(
            "A completed fishbone diagram with 6 categories and at least 18 causes, each tagged "
            "as structural or behavioural, plus a one-page recommendation identifying which "
            "causes Agile addresses and which it does not."
        ),
        services="Fishbone tool (alfredang.github.io/fishbone), the HarbourFront project post-mortem data in the Learner Guide",
        steps=[
            ("Open the Fishbone tool at https://alfredang.github.io/fishbone/ and enter the problem statement 'CustomerConnect delivered 4 months late and 62% of features unused' as the effect.", ""),
            ("Create six cause categories: Process, People, Requirements, Governance, Technology, and Customer Involvement.", ""),
            ("Under Requirements, add causes from the post-mortem data: scope frozen at month 1, 96-page document signed off before any prototype, no change route except a formal variation, 41 change requests rejected.", ""),
            ("Under Process, add: single integration at month 9, no working software until month 8, testing compressed into the final 6 weeks, defects found after the design was locked.", ""),
            ("Under Customer Involvement, add: customer consulted at requirements and at UAT only, an 8-month gap with no customer contact, no customer in the room when priorities were set.", ""),
            ("Under Governance, add: stage-gate approvals rewarded documents over working output, progress reported as percent-complete of tasks, no mechanism to stop or redirect funding mid-project.", ""),
            ("Under People and Technology, add the remaining causes: one specialist per skill creating queues, no shared definition of done, an unproven integration platform chosen at month 2 and unvalidated until month 9.", ""),
            ("Review every cause and tag it S (structural — caused by the delivery approach itself) or B (behavioural — caused by how people acted). Count each.", ""),
            ("For each structural cause, name the specific Agile practice that addresses it: frozen scope → product backlog with continuous reordering; late integration → potentially shippable increment each sprint; customer gap → sprint review every 2 weeks; percent-complete reporting → working software as the measure of progress.", ""),
            ("Identify at least two causes that Agile does NOT fix on its own — for example an unproven platform still needs a technical spike, and a governance model that cannot fund incrementally must itself be changed.", ""),
            ("Export the diagram and draft the one-page recommendation to the committee: the diagnosis, the structural/behavioural split, and what must change beyond the delivery method.", ""),
        ],
        test=(
            "Your diagram carries at least 18 causes across all 6 categories, every cause is "
            "tagged S or B, and each structural cause is paired with a named Agile practice. "
            "Your recommendation honestly identifies at least two causes Agile will not fix — "
            "a diagnosis that concludes 'Agile solves everything' has not been done properly."
        ),
        debrief=[
            "Most causes tag as structural. The team did not fail; the approach concentrated all risk at the end.",
            "This is why the cost-of-change curve matters: every one of these causes became expensive because it was discovered late.",
            "K3 in practice: organisational policies and governance had to change too. Adopting Agile inside a stage-gate funding model produces theatre, not agility.",
        ],
    ),
]
