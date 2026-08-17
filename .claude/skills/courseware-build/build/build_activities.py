#!/usr/bin/env python3
"""Generate the per-activity folders from the same single source as the deck/LP/LG.

Each activity gets its OWN folder:

    activities/activity-NN-<slug>/
        README.md          the activity brief + full step-by-step (mirrors the LG)
        WORKSHEET.md       the fill-in worksheet the team completes
        data/*.csv         any dataset the activity needs (Activities 7 and 8)

Also writes activities/README.md as the index.
"""
import os, sys, re, csv

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import course_data as C
from data_domain1 import DOMAIN1
from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3

ACTIVITIES = DOMAIN1 + DOMAIN2 + DOMAIN3


def _find_repo(start):
    env = os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env):
        return env
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "activities")):
            return d
    return os.path.dirname(os.path.dirname(HERE))


REPO = _find_repo(HERE)
ACTDIR = os.path.join(REPO, "activities")

SLUGS = {
    1: "empathise-customer-design-thinking",
    2: "diagnose-waterfall-fishbone",
    3: "product-backlog-sprint-planning",
    4: "agile-raci-accountability",
    5: "execute-sprint-scrum-board",
    6: "retrospective-5whys",
    7: "defect-pareto-analysis",
    8: "velocity-forecast-metrics",
}

# ------------------------------------------------------------------ datasets
DATASETS = {
    7: [("defect-causes.csv",
         [["Defect cause category", "Count"],
          ["Stale or missing feed data", 44],
          ["Unclear acceptance criteria", 31],
          ["Environment and configuration drift", 17],
          ["Carrier API contract changes", 11],
          ["UI validation gaps", 8],
          ["Access and permission errors", 5],
          ["Report formatting", 3],
          ["Documentation errors", 1]])],
    8: [("sprint-velocity.csv",
         [["Sprint", "Committed points", "Completed points (Done only)", "Avg cycle time (days)"],
          ["Sprint 1", 20, 14, 3.1],
          ["Sprint 2", 20, 18, 4.3],
          ["Sprint 3", 22, 17, 5.8],
          ["Sprint 4", 22, 21, 7.4]]),
        ("backlog-remaining.csv",
         [["Item", "Value"],
          ["Points remaining in backlog", 186],
          ["Average velocity", 17.5],
          ["Slowest sprint velocity", 14],
          ["Fastest sprint velocity", 21],
          ["Sprint length (weeks)", 2]])],
    3: [("starter-backlog.csv",
         [["ID", "User story", "Notes"],
          ["CC-01", "As a warehouse operations executive, I want a live customs status on each "
                    "inbound shipment, so that I can re-sequence today's production.",
           "From Activity 1 — highest customer value"],
          ["CC-02", "As a warehouse operations executive, I want an alert before a shipment is "
                    "delayed, so that I can warn production early.", "From Activity 1"],
          ["CC-03", "As a warehouse operations executive, I want one screen showing all my "
                    "inbound shipments, so that I do not click through six pages.",
           "From Activity 1"],
          ["CC-04", "As a customer admin, I want to log in securely, so that only my company's "
                    "shipments are visible.", "Enabling story"],
          ["CC-05", "As the system, I need a carrier data feed, so that shipment status is "
                    "current.", "Enabling story — see the Activity 6 root cause"],
          ["CC-06", "As the system, I need an alerting service, so that delay alerts can be "
                    "sent.", "Enabling story"],
          ["...", "Add at least 6 more stories in your team", "Target: 12+ stories total"]])],
}

WS_FIELDS = {
    1: ["Persona name and role", "SAYS (quote)", "THINKS", "DOES", "FEELS",
        "Pains (at least 3)", "Gains (at least 2)",
        "REFRAMED PROBLEM STATEMENT (user + need + consequence, no solution)",
        "What the ORIGINAL requirement optimised for instead",
        "Top 3 features by customer value — state the BENEFIT, not the feature"],
    2: ["Problem statement (the effect)",
        "Causes — Requirements", "Causes — Process", "Causes — Customer Involvement",
        "Causes — Governance", "Causes — People", "Causes — Technology",
        "Count of causes tagged STRUCTURAL (S)", "Count tagged BEHAVIOURAL (B)",
        "Structural cause → the Agile practice that addresses it (one line each)",
        "At least TWO causes Agile does NOT fix, and what would fix them",
        "One-page recommendation to the committee (3–5 sentences)"],
    3: ["Sprint 1 SPRINT GOAL (one business outcome, not a list)",
        "Story 1 — text, points, Given/When/Then",
        "Story 2 — text, points, Given/When/Then",
        "Story 3 — text, points, Given/When/Then",
        "Total stories in the product backlog (target 12+)",
        "MoSCoW split — count of Must / Should / Could / Won't",
        "Stories pulled into Sprint 1, and total points (target ~20)",
        "Any story you SPLIT, and how you split it",
        "Your team's DEFINITION OF DONE (checklist)",
        "Confirm: does every Sprint 1 story serve the sprint goal? Which did you remove?"],
    4: ["The 5 roles used as columns",
        "Row with TWO Accountables in your first draft",
        "Row with NO Accountable in your first draft",
        "Which role was Consulted on too many rows, and what you changed to I",
        "How 'change the sprint scope mid-sprint' is assigned, and why",
        "How 'report progress to the committee' changed",
        "The specific duplicate A that caused the developers' escalation",
        "The single change that most reduces the team's confusion, and why (2 sentences)"],
    5: ["Sprint 1 committed points", "WIP limit set on In Progress",
        "Burndown — remaining points at Day 0,1,2,3,4,5,6,7,8,9,10",
        "Impediment 1 (Day 3, stale timestamps) — decision and rationale",
        "Impediment 2 (Day 5, capacity loss) — decision, and when you told the PO",
        "Impediment 3 (Day 7, new story) — displaced a story, or pushed to Sprint 2? Why?",
        "ACTUAL VELOCITY (fully-Done points only)",
        "Points CARRIED OVER (recorded separately)",
        "Sprint Review feedback from the reviewing team",
        "What your burndown shape tells you about your WIP"],
    6: ["The ONE problem chosen for analysis, and why that one",
        "Why 1", "Why 2", "Why 3", "Why 4", "Why 5 (the root cause)",
        "Backwards check — read the chain with 'because'. Does every link hold?",
        "Is the root cause something YOUR TEAM can change? (If no, keep asking why)",
        "SMART action — owner, measure, and deadline",
        "Story points allocated in the Sprint 2 backlog",
        "Plus / Delta on the retrospective itself"],
    7: ["Total defects entered (must be 120)",
        "Categories in descending order",
        "Cumulative % after cause 1 / 2 / 3 / 4",
        "The VITAL FEW — which causes, and the % they account for",
        "Link to Activity 6 — which root cause sits under the top two bars?",
        "Sprint 4 target — numeric and verifiable",
        "Your answer to the operations manager who wants all 120 fixed",
        "What you are deliberately NOT fixing this sprint, and the cost of fixing it"],
    8: ["Average velocity", "Forecast — average / pessimistic / optimistic (in sprints)",
        "Forecast in calendar weeks (range)",
        "The assumptions your forecast depends on (list them)",
        "Which CFD band is widening — the bottleneck",
        "Cycle time trend from the control chart",
        "Explain the growing support queue using Little's Law",
        "Your recommended action (and why it is NOT 'increase velocity')",
        "The one-paragraph answer to the committee"],
}


def slugged(a):
    return f"activity-{a['num']:02d}-{SLUGS[a['num']]}"


os.makedirs(ACTDIR, exist_ok=True)
index = []

for a in ACTIVITIES:
    folder = os.path.join(ACTDIR, slugged(a))
    os.makedirs(os.path.join(folder, "data"), exist_ok=True)
    topic = [t for t in C.TOPICS if t["num"] == a["topic"]][0]

    # ---------------------------------------------------------------- README
    L = []
    L.append(f"# Activity {a['num']} — {a['title']}")
    L.append("")
    L.append(f"**Course:** {C.TITLE} ({C.COURSE_CODE})  ")
    L.append(f"**Topic {a['topic']}:** {topic['title']}  ")
    L.append(f"**Learning outcome:** {a['lo']}  ")
    L.append(f"**Duration:** {a['duration']} minutes  ")
    L.append(f"**Team size:** 3–4 learners  ")
    L.append(f"**Tool:** [{a['tool']}]({a['tool_url']})  ")
    L.append("")
    L.append("---")
    L.append("")
    L.append("## Objective")
    L.append("")
    L.append(a["objective"])
    L.append("")
    L.append("## The situation")
    L.append("")
    L.append(a["scenario"])
    L.append("")
    L.append("## What you will do")
    L.append("")
    L.append(a["desc"])
    L.append("")
    L.append("## What you will produce")
    L.append("")
    L.append(a["build"])
    L.append("")
    L.append("## Materials")
    L.append("")
    L.append(a["services"])
    L.append("")
    if a["num"] in DATASETS:
        L.append("## Data files in this folder")
        L.append("")
        for fname, _rows in DATASETS[a["num"]]:
            L.append(f"- `data/{fname}`")
        L.append("")
    L.append("## Step-by-step instructions")
    L.append("")
    for i, (stext, _cmd) in enumerate(a["steps"], 1):
        L.append(f"{i}. {stext}")
    L.append("")
    L.append("## Self-check — are you done?")
    L.append("")
    L.append(f"> {a['test']}")
    L.append("")
    L.append("## Debrief — what this activity proves")
    L.append("")
    for d in a["debrief"]:
        L.append(f"- {d}")
    L.append("")
    L.append("---")
    L.append("")
    L.append(f"Record your team's output in [WORKSHEET.md](WORKSHEET.md). "
             f"The same instructions appear in the Learner Guide, section 6.{a['num']}.")
    L.append("")
    with open(os.path.join(folder, "README.md"), "w") as f:
        f.write("\n".join(L))

    # ---------------------------------------------------------------- WORKSHEET
    W = []
    W.append(f"# Activity {a['num']} Worksheet — {a['title']}")
    W.append("")
    W.append(f"**Team members:** ______________________________________________  ")
    W.append(f"**Date:** ______________  ")
    W.append(f"**Tool:** {a['tool_url']}  ")
    W.append("")
    W.append("---")
    W.append("")
    for i, field in enumerate(WS_FIELDS[a["num"]], 1):
        W.append(f"### {i}. {field}")
        W.append("")
        W.append("```")
        W.append("")
        W.append("")
        W.append("```")
        W.append("")
    W.append("---")
    W.append("")
    W.append("## Self-check before you finish")
    W.append("")
    W.append(f"- [ ] {a['test']}")
    W.append("- [ ] Every team member can explain the output, not just the person who typed it.")
    W.append("- [ ] The artefact is exported or screenshotted into this worksheet.")
    W.append("")
    with open(os.path.join(folder, "WORKSHEET.md"), "w") as f:
        f.write("\n".join(W))

    # ---------------------------------------------------------------- data
    for fname, rows in DATASETS.get(a["num"], []):
        with open(os.path.join(folder, "data", fname), "w", newline="") as f:
            csv.writer(f).writerows(rows)

    index.append((a, slugged(a)))
    print(f"  wrote activities/{slugged(a)}/  "
          f"({len(a['steps'])} steps, {len(WS_FIELDS[a['num']])} worksheet fields"
          f"{', ' + str(len(DATASETS[a['num']])) + ' data file(s)' if a['num'] in DATASETS else ''})")

# ------------------------------------------------------------------ index
I = []
I.append(f"# Activities — {C.TITLE}")
I.append("")
I.append(f"**Course code:** {C.COURSE_CODE}  ")
I.append(f"**Version:** {C.VERSION} · {C.VERSION_DATE}  ")
I.append("")
I.append("Every activity has its own folder containing the brief, the full step-by-step "
         "instructions, a worksheet, and any data files needed. All eight activities work on "
         "one running case study — **HarbourFront Logistics Pte Ltd** and its CustomerConnect "
         "portal — so the artefacts you build compound across the two days.")
I.append("")
I.append("## The running case")
I.append("")
I.append("HarbourFront Logistics is a 140-staff Singapore third-party logistics (3PL) provider. "
         "Its CustomerConnect self-service tracking portal ran as an 11-month waterfall project, "
         "was delivered 4 months late, and 62% of its shipped features go unused. You are "
         "appointed Agile project lead for the restart.")
I.append("")
I.append("## Activity index")
I.append("")
I.append("| # | Activity | Topic | LO | Tool | Min |")
I.append("|---|---|---|---|---|---|")
for a, slug in index:
    I.append(f"| {a['num']} | [{a['title']}]({slug}/) | Topic {a['topic']} | {a['lo']} | "
             f"[{a['tool']}]({a['tool_url']}) | {a['duration']} |")
I.append("")
I.append("## Tools used")
I.append("")
I.append("| Tool | URL | Used in |")
I.append("|---|---|---|")
for t in C.ED_TOOLS:
    I.append(f"| {t['name']} | {t['url']} | {t['use']} |")
I.append("")
I.append("All tools are browser-based. Nothing to install, no login required.")
I.append("")
I.append("## How the activities build on each other")
I.append("")
I.append("```")
I.append("Activity 1  Empathise → the customer insight and the top-3 features")
I.append("     ↓")
I.append("Activity 2  Fishbone → why the waterfall delivery failed (structural vs behavioural)")
I.append("     ↓")
I.append("Activity 3  Backlog + Sprint 1 planning → stories, estimates, sprint goal, DoD")
I.append("     ↓")
I.append("Activity 4  RACI → who is accountable for what (resolves the priority conflict)")
I.append("     ↓")
I.append("Activity 5  Execute Sprint 1 → board, burndown, impediments, actual velocity")
I.append("     ↓")
I.append("Activity 6  Retrospective + 5 Whys → the root cause, and one SMART action")
I.append("     ↓")
I.append("Activity 7  Pareto → which few causes are worth fixing first")
I.append("     ↓")
I.append("Activity 8  Velocity forecast + CFD/control chart → the answer to the committee")
I.append("```")
I.append("")
I.append(f"Full step-by-step instructions are also in the Learner Guide, section 6. "
         f"The trainer slides deliberately do NOT carry the steps.")
I.append("")
with open(os.path.join(ACTDIR, "README.md"), "w") as f:
    f.write("\n".join(I))

print(f"\nWrote activities/README.md index")
print(f"Activity folders: {len(index)}")
print(f"Total steps across all activities: {sum(len(a['steps']) for a, _ in index)}")
