# WSQ — Agile Project Management for Business

[![WSQ Course](https://img.shields.io/badge/WSQ-TGS--2023018967-1F6FEB)](https://www.tertiarycourses.com.sg/wsq-agile-project-management-for-business.html)
[![Duration](https://img.shields.io/badge/Duration-2%20days%20%C2%B7%2016%20hours-10B981)](#lesson-plan)
[![TSC](https://img.shields.io/badge/TSC-Business%20Agility%20ICT--BIN--4038--1.1-7C3AED)](#skills-framework-mapping)
[![Version](https://img.shields.io/badge/Version-v9.0-F59E0B)](#version-history)
[![SkillsFuture](https://img.shields.io/badge/SkillsFuture-Funded-DC2626)](https://courses.myskillsfuture.gov.sg/courses/TGS-2023018967)

Courseware for the WSQ course **Agile Project Management for Business**, delivered by
[Tertiary Infotech Academy Pte Ltd](https://www.tertiarycourses.com.sg) (UEN 201200696W).

This repository holds the **single-source build pipeline** for the course: one content module
drives the slide deck, the Lesson Plan, the Learner Guide and the activity folders, so they can
never drift apart.

---

## Course at a glance

| | |
|---|---|
| **Course code** | TGS-2023018967 |
| **Duration** | 2 days · 16 instructional hours (+ 2 hours assessment) |
| **Level** | Beginner |
| **TSC** | Business Agility · ICT-BIN-4038-1.1 |
| **Assessment** | Written Assessment (SAQ, 1 h) + Case Study (1 h) — both open book |
| **Delivery** | Physical classroom, synchronous Zoom, or corporate on-site |
| **Funding** | SkillsFuture funded · up to 70% for eligible Singaporeans/PRs and SMEs |
| **Course page** | <https://www.tertiarycourses.com.sg/wsq-agile-project-management-for-business.html> |

### Learning outcomes

- **LO1** — Adopt a new Agile mindset for project management
- **LO2** — Share and implement Agile practices within the teams
- **LO3** — Build an Agile team to execute and track the project performance

### Course outline

| Topic | Title | Focus | Activities |
|---|---|---|---|
| 1 | Introduction to Agile Project Management | Business landscape · waterfall · Agile overview · the paradigm shift | 1–2 |
| 2 | Agile Essentials | Manifesto values & principles · Scrum · Lean · Kanban · XP · resistance | 3–4 |
| 3 | Agile Project Execution and Tracking | Team & vision · user stories · execution · metrics · improvement | 5–8 |

---

## What's in this repository

```
.
├── courseware/                     the delivered artifacts (one live version)
│   ├── WSQ - Master Trainer Slides - ... - v9.0.pptx   120 slides
│   ├── WSQ - Master Trainer Slides - ... - v9.0.pdf
│   ├── WSQ - Lesson Plan - ...      - v9.0.docx/.pdf   15 pages
│   ├── WSQ - Learner Guide - ...    - v9.0.docx/.pdf   53 pages
│   └── assets/                     20 diagrams/charts + 6 tool screenshots
│
├── activities/                     8 activities, one folder each
│   ├── activity-01-empathise-customer-design-thinking/
│   │   ├── README.md               brief + full step-by-step
│   │   └── WORKSHEET.md            team fill-in worksheet
│   ├── activity-02-…  …  activity-08-velocity-forecast-metrics/
│   └── README.md                   activity index
│
├── LG-Agile Project Management for Business.md   Markdown mirror of the Learner Guide
│
└── .claude/skills/courseware-build/build/        the build pipeline
    ├── course_data.py              SINGLE SOURCE — metadata, outcomes, topics, concepts
    ├── data_domain1.py … 3.py      the 8 activities (one file per topic)
    ├── make_charts.py              generates every diagram/chart asset
    ├── build_slides.py             → the PPTX
    ├── build_lesson_plan.py        → the LP DOCX
    ├── build_learner_guide.py      → the LG DOCX + Markdown mirror
    ├── build_activities.py         → the activities/ folders
    └── build_assessment.py         → the assessment set (NOT in this repo — see below)
```

> **The assessment set is deliberately not in this repository.** The WA and Case Study question
> papers and their answer keys are confidential assessor material and are distributed via Google
> Drive and the LMS only. `assessment/` is gitignored.

---

## The running case study

All eight activities work on **one** business case, so the artefacts learners build compound
across the two days:

> **HarbourFront Logistics Pte Ltd** — a 140-staff Singapore third-party logistics (3PL)
> provider. Its *CustomerConnect* self-service tracking portal ran as an 11-month waterfall
> project, was delivered 4 months late, and 62% of its shipped features go unused. Learners are
> appointed Agile project lead for the restart.

```
Activity 1  Empathise            → customer insight + top-3 features
     ↓
Activity 2  Fishbone             → why the waterfall delivery failed
     ↓
Activity 3  Backlog + planning   → stories, estimates, sprint goal, Definition of Done
     ↓
Activity 4  RACI                 → who is accountable for what
     ↓
Activity 5  Execute Sprint 1     → board, burndown, impediments, actual velocity
     ↓
Activity 6  Retro + 5 Whys       → the root cause, and one SMART action
     ↓
Activity 7  Pareto               → which few causes are worth fixing first
     ↓
Activity 8  Velocity + CFD       → the forecast, and the real bottleneck
```

## Activities and tools

Every activity uses a browser-based tool — nothing to install, no login.

| # | Activity | Tool | Min | LO |
|---|---|---|---|---|
| 1 | Empathise with the Customer to Reframe a Failing Project | [Design Thinking](https://alfredang.github.io/designthinking/) | 45 | LO1 |
| 2 | Diagnose the Waterfall Failure with a Fishbone Analysis | [Fishbone](https://alfredang.github.io/fishbone/) | 45 | LO1 |
| 3 | Build the Product Backlog and Run Sprint 1 Planning | [Scrum Board](https://alfredang.github.io/scrum/) | 60 | LO2 |
| 4 | Clarify Agile Role Accountability with a RACI Matrix | [RACI](https://alfredang.github.io/raci/) | 45 | LO2 |
| 5 | Execute Sprint 1 and Track It on the Scrum Board | [Scrum Board](https://alfredang.github.io/scrum/) | 60 | LO3 |
| 6 | Run the Sprint Retrospective with 5 Whys Root-Cause Analysis | [5 Whys](https://alfredang.github.io/5whys/) | 45 | LO3 |
| 7 | Prioritise Defect Causes with a Pareto Chart | [Pareto Chart](https://alfredang.github.io/paretochart/) | 45 | LO3 |
| 8 | Forecast the Release from Velocity and Read the Agile Metrics | [Scrum Board](https://alfredang.github.io/scrum/) | 45 | LO3 |

---

## Skills Framework mapping

TSC **Business Agility** (`ICT-BIN-4038-1.1`). Nothing is assessed that is not taught *and*
practised.

### Abilities

| Code | Ability | Taught in |
|---|---|---|
| A1 | Share information actively within and across teams to bridge operational barriers | Topic 2 · Activity 4 |
| A2 | Organise work in alignment with operational priorities | Topics 1–2 · Activities 2, 4 |
| A3 | Implement Agile or lean practices to reduce waste and defects | Topics 2–3 · Activities 3, 7 |
| A4 | Measure progress against targets on a regular basis | Topic 3 · Activities 5, 7, 8 |
| A5 | Experiment with new ideas, products or services | Topic 1 · Activity 1 |
| A6 | Assess work performance and quality for continuous improvement | Topic 3 · Activities 6, 7, 8 |
| A7 | Manage responsibilities and take ownership of outcomes | Topic 3 · Activities 5, 6, 8 |

### Knowledge

| Code | Knowledge | Taught in |
|---|---|---|
| K1 | Methods to analyse current and future business operating landscapes | Topic 1 · Activity 2 |
| K2 | Methods to analyse current and future customer needs and preferences | Topic 1 · Activity 1 |
| K3 | Organisational policies, processes and standards | Topic 1 · Activity 2 |
| K4 | Types of change management methodologies, tools and practices | Topic 2 |
| K5 | Types of team composition and formation models | Topic 3 · Activities 4, 5 |
| K6 | Values and principles of Agile methodologies | Topic 2 · Activity 3 |
| K7 | Types of Agile methodologies and practices | Topic 2 · Activity 3 |

---

## Lesson plan

Each training day delivers exactly **8 instructional hours** (09:30–18:30, with a 1-hour lunch
excluded; tea breaks counted within). The 2-hour assessment sits outside instructional time.

| Day | Theme |
|---|---|
| 1 | The Agile mindset and the essentials — why Agile, the Manifesto, Scrum, Lean and Kanban |
| 2 | Building and running an Agile team — vision, stories, execution, metrics and improvement |

---

## Rebuilding the courseware

All artifacts are generated. Edit the content module, never the output files.

```bash
# 1. regenerate the diagram + chart assets
python3 .claude/skills/courseware-build/build/make_charts.py

# 2. build the artifacts
python3 .claude/skills/courseware-build/build/build_slides.py
python3 .claude/skills/courseware-build/build/build_lesson_plan.py
python3 .claude/skills/courseware-build/build/build_learner_guide.py
python3 .claude/skills/courseware-build/build/build_activities.py

# 3. render the PDFs
soffice --headless --convert-to pdf --outdir courseware "courseware/<file>"

# 4. inject page-numbered TOCs into the LP and LG, then re-render
python3 .claude/skills/courseware-build/build/inject_toc.py "<docx>" "<pdf>" 2
```

**Requirements:** Python 3 with `python-pptx`, `python-docx`, `matplotlib`, `Pillow`, `pypdf`;
LibreOffice for PDF rendering; `pdftoppm` (poppler) for page rendering.

### Design rules enforced by the build

- **All-white slides**, Arial throughout, 16:9 (13.333 × 7.5 in), brand palette.
- **Highly visual** — tile grids, numbered process strips, comparison tables, concept cards and
  20 generated diagrams. No bullet walls. Mean ≈ 29 shapes per slide, 0 shapes off-slide.
- **Step-by-step procedures appear ONLY in the Learner Guide.** The deck carries a tool slide, an
  activity briefing and a debrief per activity — never numbered steps.
- **No practice exams.**
- Every generated asset in `courseware/assets/` is asserted to be placed on a slide at build time.
- The LP's slide references are read from `slide_map.json`, written by the deck build, so they can
  never cite a slide the deck does not have.

---

## Content sources

The courseware was rebuilt from the legacy v8 master deck (all original teaching content
retained) and substantially expanded from:

- [Agile Manifesto](https://agilemanifesto.org/) — the four values and twelve principles
- [Atlassian — Agile Project Management](https://www.atlassian.com/agile/project-management) — the five agile metrics
- [APM (UK) — Agile Project Management](https://www.apm.org.uk/resources/find-a-resource/agile-project-management/) — definition, benefits, governance
- [Coursera — What Is Agile?](https://www.coursera.org/articles/what-is-agile-a-beginners-guide) — lifecycle and framework comparison
- [Rasmussen — What Is Agile Project Management?](https://www.rasmussen.edu/degrees/business/blog/what-is-agile-project-management/) — Agile in business contexts
- [Adobe Business — Agile methodology](https://business.adobe.com/blog/basics/agile) — Agile for marketing and creative teams
- [GeeksforGeeks — Agile Project Management](https://www.geeksforgeeks.org/software-engineering/agile-project-management/) — lifecycle phases and comparisons

---

## Version history

| Version | Date | Changes |
|---|---|---|
| **v9.0** | 17 August 2026 | Full content revamp. Rebuilt on a single-source pipeline. Expanded Agile theory (Manifesto, Scrum accountabilities/artefacts/events, Lean, Kanban + Little's Law, XP, DSDM, scaling). Added the five Agile metrics with worked interpretation. Replaced generic exercises with 8 tool-based activities on one running case study. Added activity debriefs, 20 generated visuals and full TSC mapping. |
| v8.0 | 28 November 2022 | Previous released version. |

---

## Related courses

- WSQ — Fast-Track Innovations with Agile Design Thinking and Generative AI (GenAI)
- WSQ — Design Thinking Course for Businesses
- WSQ — Effective Project Management for Small Projects
- WSQ — Innovative Problem Solving with Generative AI (GenAI)
- WSQ — Mastering Agile Project Management for IT Projects

## Support

| | |
|---|---|
| Email | <enquiry@tertiaryinfotech.com> |
| Telephone | +65 6100 0613 |
| Website | <https://www.tertiarycourses.com.sg> |
| LMS / TMS | <https://lms-tms.tertiaryinfotech.com> |

---

© 2026 Tertiary Infotech Academy Pte Ltd (UEN 201200696W). All rights reserved.
