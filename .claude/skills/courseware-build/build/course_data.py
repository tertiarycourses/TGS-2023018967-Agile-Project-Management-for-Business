"""
SINGLE SOURCE OF TRUTH — WSQ Agile Project Management for Business (TGS-2023018967).

Every artifact (PPT, LP, LG, LG.md, activities/) is generated from this file plus
data_domain1.py … data_domain3.py, so titles, activity numbering, learning
outcomes, the schedule and the assessment can never drift apart.

Content lineage:
  * The legacy v8 master deck (292 slides) — all original teaching content retained.
  * Beefed up from: Atlassian (agile project management + the five agile metrics),
    APM UK (agile project management resource), Coursera (Agile beginner's guide),
    Rasmussen (what is agile project management), Adobe Business (agile
    methodology / agile marketing), GeeksforGeeks (agile project management).
"""

# ------------------------------------------------------------------ metadata
TITLE        = "Agile Project Management for Business"
SHORT_TITLE  = "Agile Project Management for Business"
COURSE_CODE  = "TGS-2023018967"
VERSION      = "v9.0"
VERSION_DATE = "17 August 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr Alfred Ang"
DAYS         = 2
DURATION_HRS = 16
COURSE_URL   = "https://www.tertiarycourses.com.sg/wsq-agile-project-management-for-business.html"

# ------------------------------------------------------------------ skills framework
TSC_TITLE = "Business Agility"
TSC_CODE  = "ICT-BIN-4038-1.1"

TSC_ABILITIES = [
    ("A1", "Share information actively within and across teams to bridge operational barriers"),
    ("A2", "Organise work in alignment with operational priorities"),
    ("A3", "Implement Agile or lean practices to reduce waste and defects in operating procedures and practices"),
    ("A4", "Measure progress against targets for defined business outcomes on a regular basis"),
    ("A5", "Experiment with new ideas, products or services"),
    ("A6", "Assess work performance and quality to ensure continuous improvement"),
    ("A7", "Manage individual work responsibilities and take ownership of individual and team outcomes"),
]

TSC_KNOWLEDGE = [
    ("K1", "Methods to analyse current and future business operating landscapes"),
    ("K2", "Methods to analyse current and future customer needs and preferences"),
    ("K3", "Organisational policies, processes and standards"),
    ("K4", "Types of change management methodologies, tools and practices"),
    ("K5", "Types of team composition and formation models"),
    ("K6", "Values and principles of Agile methodologies"),
    ("K7", "Types of Agile methodologies and practices"),
]

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Adopt a new Agile mindset for project management",
    "LO2: Share and implement Agile practices within the teams",
    "LO3: Build an Agile team to execute and track the project performance",
]

# ------------------------------------------------------------------ target audience
JOB_ROLES = [
    "Project Manager", "Scrum Master", "Product Owner", "Business Analyst",
    "Team Leader", "IT Project Manager", "Change Manager", "Operations Manager",
    "Programme Manager",
]

PREREQUISITES = [
    "Basic computer operation proficiency",
    "Minimum 3 GCE 'O' Level passes including English, or Workplace Literacy (WPL) Level 5",
    "Minimum 1 year of working experience",
    "A positive learning attitude and willingness to participate in team activities",
]

# ------------------------------------------------------------------ ed-tools used in the activities
ED_TOOLS = [
    dict(name="5 Whys",          url="https://alfredang.github.io/5whys/",
         use="Root-cause analysis in the sprint retrospective (Activity 6)"),
    dict(name="Fishbone",        url="https://alfredang.github.io/fishbone/",
         use="Cause-and-effect analysis of delivery problems (Activity 2)"),
    dict(name="Pareto Chart",    url="https://alfredang.github.io/paretochart/",
         use="Prioritising the 20% of causes driving 80% of defects (Activity 7)"),
    dict(name="RACI Matrix",     url="https://alfredang.github.io/raci/",
         use="Clarifying Agile role accountability (Activity 4)"),
    dict(name="Scrum Board",     url="https://alfredang.github.io/scrum/",
         use="Running the sprint board, backlog and burndown (Activities 3, 5, 8)"),
    dict(name="Design Thinking", url="https://alfredang.github.io/designthinking/",
         use="Empathising with customers to shape the product vision (Activity 1)"),
]

# ------------------------------------------------------------------ topics (= skills domains)
TOPICS = [
    dict(num=1, code="01",
         title="Introduction to Agile Project Management",
         subtitle="Business landscape · Waterfall · Agile overview · The paradigm shift",
         weighting="Day 1 AM · K1, K2, K3, A2, A5",
         hours=4,
         tsc="K1, K2, K3, A2, A5",
         lo="LO1",
         concepts=[
            "A reality check on today's business operating landscape: VUCA conditions — volatility, uncertainty, complexity and ambiguity — mean the plan you wrote in month one is stale by month three.",
            "The waterfall model freezes scope at the start, demands complete upfront estimation, and shows the customer nothing until the very end — which is precisely where its risk concentrates.",
            "Agile is an umbrella term for iterative, incremental delivery. APM (UK) defines it as 'an iterative approach to delivering a project throughout its life cycle', releasing benefit continuously rather than only at the end.",
            "Agile inverts the traditional iron triangle: cost and time become fixed, scope becomes the variable. You buy a timebox and a team, not a fixed feature list.",
            "Methods to analyse the operating landscape — PESTLE, SWOT, Porter's Five Forces and scenario planning — are still used, but re-run every quarter instead of once per project.",
            "Methods to analyse customer needs — personas, empathy maps, journey maps, Kano analysis, jobs-to-be-done and A/B experiments — replace the one-off requirements interview.",
            "Agile delivers value early: the highest-value 20% of scope typically carries most of the business benefit, and shipping it in month two rather than month twelve changes the return profile entirely.",
            "Agile lowers the cost of change. In waterfall the cost of change rises exponentially with time; short iterations flatten that curve because less has been built on top of a wrong assumption.",
            "Agile is not licence to skip planning or documentation. It replans continuously and documents 'barely sufficiently' — the discipline moves, it does not disappear.",
            "Choosing the approach: stable requirements, fixed regulatory scope and a strong documentation mandate favour waterfall; evolving requirements, high novelty and a need for fast feedback favour Agile; many organisations run a hybrid.",
            "Agile beyond software: Adobe applies it to marketing campaigns, Toyota to manufacturing flow, PayPal to workforce alignment and Spotify to delivery speed. Finance, construction, biotech and HR all run Agile today.",
            "Organisational policies, processes and standards must be restructured for Agile to hold — governance shifts from stage-gate approval to incremental funding and continuous assurance.",
         ]),
    dict(num=2, code="02",
         title="Agile Essentials",
         subtitle="Manifesto values & principles · Scrum · Lean · Kanban · XP · Overcoming resistance",
         weighting="Day 1 PM · K4, K6, K7, A1, A3",
         hours=4,
         tsc="K4, K6, K7, A1, A3",
         lo="LO2",
         concepts=[
            "The Agile Manifesto (2001) holds 4 values and 12 principles. Each value is a preference, not a prohibition — 'we value X over Y' means both matter, X matters more when they conflict.",
            "Value 1 — Individuals and interactions over processes and tools: projects are undertaken by people, problems are solved by people, and no tool rescues a team that will not talk.",
            "Value 2 — Working software over comprehensive documentation: deliver something that works, and keep documents barely sufficient, just in time and for a reason.",
            "Value 3 — Customer collaboration over contract negotiation: manage change rather than suppress it, and build a shared, written definition of 'done'.",
            "Value 4 — Responding to change over following a plan: in high-change environments, energy spent defending the original plan is energy taken from delivering value.",
            "The 12 principles operationalise the values — early and continuous delivery, welcoming late change, short timescales, daily business-developer collaboration, motivated individuals, face-to-face conversation, working software as the measure of progress, sustainable pace, technical excellence, simplicity, self-organising teams, and regular reflection.",
            "Scrum is the most widely adopted framework (roughly 63% of Agile teams): 3 accountabilities, 3 artefacts and 5 events, all built on empiricism — transparency, inspection and adaptation.",
            "Scrum accountabilities: the Product Owner owns value and the backlog order; the Scrum Master owns the process and removes impediments as a servant leader; the Developers own how the work gets done.",
            "Scrum artefacts: the Product Backlog (ordered, refined, never finished), the Sprint Backlog (the Sprint Goal plus the selected items and the plan), and the Increment (usable, meeting the Definition of Done).",
            "Scrum events: Sprint Planning (what and how), the Daily Scrum (15 minutes, re-plan the next 24 hours), the Sprint Review (inspect the increment with stakeholders), the Sprint Retrospective (inspect the process), and the Sprint itself as the container.",
            "Lean, from Toyota, targets the eight wastes and holds seven principles: eliminate waste, amplify learning, decide as late as possible, deliver fast, empower the team, build quality in, and optimise the whole.",
            "Kanban ('signboard') runs five practices: visualise the workflow, limit work in progress, manage flow, make process policies explicit, and improve collaboratively. WIP limits are the engine — they surface bottlenecks instead of hiding them.",
            "Little's Law ties it together: Cycle Time = Work in Progress ÷ Throughput. Halve WIP at constant throughput and you halve cycle time — this is why limiting WIP speeds delivery.",
            "Extreme Programming (XP) contributes five values (simplicity, communication, feedback, courage, respect) and engineering practices: TDD, pair programming, continuous integration, refactoring, collective code ownership, small releases and sustainable pace.",
            "Scrum vs Kanban vs Scrumban: Scrum suits teams of 5–9 with a cadence and a goal; Kanban suits continuous-flow and high-variability work such as support queues; Scrumban blends a Scrum cadence with Kanban WIP limits.",
            "Other methods worth knowing: DSDM/AgilePM (the APM-endorsed framework with feasibility, foundations, evolutionary development and deployment), Feature-Driven Development, Crystal, and SAFe/LeSS for scaling.",
            "Finding Agile support: map stakeholders and address each fear directly — sponsors fear failure, managers fear loss of control, teams fear exposure, and users fear losing features.",
            "Handling resistance: start with a willing pilot team, make the wins visible, use evolutionary rather than revolutionary change, train and coach, and never present Agile as a way to get more for less.",
         ]),
    dict(num=3, code="03",
         title="Agile Project Execution and Tracking",
         subtitle="Team building & vision · User stories & estimation · Execution · Metrics · Continuous improvement",
         weighting="Day 2 · K5, A4, A6, A7",
         hours=6,
         tsc="K5, A4, A6, A7",
         lo="LO3",
         concepts=[
            "Team composition and formation models: high-performing Agile teams are cross-functional, self-organising, fewer than about 12 people, co-located or deliberately connected, with a shared vision and stable membership.",
            "Generalising specialists — members deep in one skill but capable across several — remove the single-point bottleneck that specialists create when work queues behind one person.",
            "Tuckman's model (forming, storming, norming, performing, adjourning) tells the leader which style to use: directing, then coaching, then supporting, then delegating. Adaptive leadership means matching style to team maturity.",
            "Shu-Ha-Ri and the Dreyfus model describe skill acquisition — obey the practice, adapt the practice, transcend the practice. New Agile teams should follow the framework before tailoring it.",
            "Servant leadership: shield the team from interruption, remove impediments, re-communicate the vision, and tap intrinsic motivation — autonomy, mastery and purpose — rather than relying on authority.",
            "Setting the vision: an Agile charter (who, what, why, when, where, how), a product vision statement, an elevator pitch, personas, wireframes and a shared Definition of Done all create the same picture in every head.",
            "Requirements as user stories: 'As a <role>, I want <goal>, so that <benefit>'. Stories carry value, are refined through conversation, and are confirmed by acceptance criteria — the three Cs: card, conversation, confirmation.",
            "INVEST tests a story: Independent, Negotiable, Valuable, Estimatable, Small, Testable. A story failing INVEST will fail in the sprint.",
            "Prioritisation techniques: MoSCoW (must, should, could, won't), dot voting, 100-point allocation, monopoly money, Kano analysis and weighted shortest job first. All must end in one ordered list.",
            "Relative estimation beats absolute estimation: story points capture complexity, effort and risk together. Planning poker with the Fibonacci sequence, affinity estimating and T-shirt sizing all defeat anchoring and the loudest-voice effect.",
            "Release and iteration planning: velocity (average points per sprint) converts an estimated backlog into a forecast range. 250 points at 18 points per sprint is about 14 sprints — a range, never a promise.",
            "Timeboxing and Parkinson's Law: the Daily Scrum is 15 minutes, a retrospective about 2 hours, a sprint 1–4 weeks. Work expands to fill the time available, so the box does the managing.",
            "The five Agile metrics that matter (Atlassian): sprint burndown (progress inside the sprint), epic/release burndown (progress across releases), velocity (forecasting capacity), the control chart (cycle and lead time), and the cumulative flow diagram (where the bottleneck is).",
            "Reading a cumulative flow diagram: a band widening vertically over time is a bottleneck at that status. Reading a burndown: a flat line means work is not being finished, not that nobody is busy.",
            "Lead time versus cycle time: lead time is the customer's whole wait; cycle time is the team's active portion. Throughput is the volume delivered per period. Excess WIP inflates all three.",
            "Metric anti-patterns: velocity is a forecasting tool, not a productivity target. Comparing velocity between teams, or rewarding it, produces point inflation and destroys the forecast.",
            "Assessing work performance: the Sprint Review inspects the product with stakeholders; the Retrospective inspects the process with the team; team self-assessments inspect the team itself.",
            "The retrospective in five stages: set the stage, gather data, generate insights, decide what to do, and close — about two hours for a two-week sprint. Insight techniques include 5 Whys, fishbone analysis, and dot voting.",
            "Continuous improvement through Kaizen and the Plan-Do-Check-Act cycle: small, frequent, team-owned improvements, each with a named owner and a SMART action carried into the next sprint backlog.",
            "Root-cause discipline: 5 Whys drills a single causal chain, the fishbone diagram spreads causes across categories, and a Pareto chart shows which few causes carry most of the pain. Use them together, then act on the top cause.",
            "Value stream mapping exposes waiting time between steps — usually far larger than the processing time — and gives the biggest, cheapest improvement available to most teams.",
            "Risk as anti-value: maintain a risk-adjusted backlog and a risk burndown chart. Expected monetary value = probability × impact, and risk work is scheduled as real backlog items, not as a side register.",
            "Technical and process debt: work skipped to go faster compounds into a slower team. Refactoring and cleanup must be funded inside the sprint, not deferred to a mythical later.",
            "Ownership and accountability (A7): the team commits to a Sprint Goal collectively, each member pulls their own work, updates the board honestly, and raises impediments the same day they appear.",
         ]),
]

# ------------------------------------------------------------------ day themes
DAY_THEMES = {
    1: "The Agile mindset and the essentials",
    2: "Building and running an Agile team",
}

# ------------------------------------------------------------------ the day agenda (SINGLE SOURCE)
# Both the deck's "Lesson Plan — Day N" slides and the Lesson Plan's detailed schedule
# tables are generated from THIS list, so the two can never contradict each other.
# (time, headline, detail) — the abridged agenda shown to learners on the slide.
DAY_AGENDA = {
    1: [("09:30  Welcome & admin", "Digital attendance (AM) · introductions · ground rules · outcomes"),
        ("11:00  Topic 1", "Introduction to Agile Project Management (Activities 1–2)"),
        ("13:00  Lunch break", "1 hour · digital attendance (PM) on return"),
        ("16:45  Topic 2", "Agile Essentials begins (Activities 3–4 on Day 2)"),
        ("18:30  End of Day 1", "Recap and Q&A")],
    2: [("09:30  Digital attendance (AM)", "Recap of Day 1"),
        ("09:45  Topic 2 continued", "Lean · Kanban · XP · change management (Activities 3–4)"),
        ("13:00  Lunch break", "1 hour · digital attendance (PM) on return"),
        ("14:45  Topic 3", "Agile Project Execution and Tracking (Activities 5–8)"),
        ("18:30  Feedback & TRAQOM", "Course feedback and the mandatory TRAQOM survey"),
        ("19:00  Final Assessment", "Digital attendance (Assessment) · WA (1 h) + Case Study (1 h)")],
}

# ------------------------------------------------------------------ assessment
ASSESSMENT = dict(
    written="Written Assessment (WA) — Short-Answer Questions (SAQ), 1 hour, open book.",
    practical="Case Study (CS) — an applied business scenario with structured tasks, 1 hour, open book.",
    note="A minimum of 75% attendance is required to be eligible for assessment and funding. "
         "Learners must be assessed Competent in both instruments.",
    open_book="Open book: slides, Learner Guide and approved course materials only.",
)

# ------------------------------------------------------------------ recommended courses
RECOMMENDED = [
    "WSQ - Fast-Track Innovations with Agile Design Thinking and Generative AI (GenAI)",
    "WSQ - Design Thinking Course for Businesses",
    "WSQ - Effective Project Management for Small Projects",
    "WSQ - Innovative Problem Solving with Generative AI (GenAI)",
    "WSQ - Mastering Agile Project Management for IT Projects",
]
