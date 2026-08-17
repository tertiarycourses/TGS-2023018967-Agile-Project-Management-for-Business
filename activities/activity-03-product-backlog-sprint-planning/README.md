# Activity 3 — Build the Product Backlog and Run Sprint 1 Planning

**Course:** Agile Project Management for Business (TGS-2023018967)  
**Topic 2:** Agile Essentials  
**Learning outcome:** LO2  
**Duration:** 60 minutes  
**Team size:** 3–4 learners  
**Tool:** [Scrum Board](https://alfredang.github.io/scrum/)  

---

## Objective

Implement Agile practices by converting business needs into an ordered product backlog and a committed sprint backlog with a sprint goal (K6, K7, A3).

## The situation

HarbourFront's committee has approved a restart: 6 sprints of 2 weeks, one team of 7 people, and a hard demonstration to the top 5 customers in 12 weeks. Nothing from the old 96-page document is carried over unexamined. You are the team, with your trainer as Product Owner. Sprint 1 planning starts now.

## What you will do

Your team writes user stories from the Activity 1 customer insight, applies INVEST, estimates with planning poker using the Fibonacci sequence, orders the backlog with MoSCoW, then loads Sprint 1 to a capacity of 20 story points and writes a single sprint goal. You use the Scrum tool to hold the backlog and the sprint board.

## What you will produce

A product backlog of at least 12 estimated user stories in priority order, a Sprint 1 backlog of about 20 points, one written sprint goal, and a Definition of Done agreed by the whole team.

## Materials

Scrum tool (alfredang.github.io/scrum), Fibonacci planning-poker cards, the Activity 1 persona and top-3 features

## Data files in this folder

- `data/starter-backlog.csv`

## Step-by-step instructions

1. Open the Scrum tool at https://alfredang.github.io/scrum/ and create a new project named 'CustomerConnect Restart'.
2. Write your first three user stories from the Activity 1 top-3 features, in the form 'As a <role>, I want <goal>, so that <benefit>'. Example: 'As a warehouse operations executive, I want a live customs status on each inbound shipment, so that I can decide whether to re-sequence today's production.'
3. Add acceptance criteria to each story using Given/When/Then. For the live-status story: 'Given a shipment in customs clearance, when I open the shipment card, then I see the current customs state and the timestamp it was last updated.'
4. Expand the backlog to at least 12 stories. Cover the customer-facing needs, then add the enabling stories the team needs — user authentication, the carrier data feed, and an alerting service.
5. Test every story against INVEST. Any story that cannot be finished inside one 2-week sprint fails 'Small' — split it by workflow step or by data type, never by technical layer.
6. Run planning poker on each story. Deal the Fibonacci cards (1, 2, 3, 5, 8, 13, 21), reveal simultaneously, and have the highest and lowest estimators explain before re-voting. Record the agreed points in the tool.
7. Any story estimated at 13 or 21 points must be split before it can enter a sprint — a number that large means the team does not yet understand it.
8. Order the full backlog using MoSCoW. Be strict: if more than 60% of your backlog is 'Must have', you have not prioritised, you have relabelled.
9. Write ONE sprint goal for Sprint 1 stating the business outcome, not a list of stories. Example: 'A customer can see the live status of one shipment end to end.'
10. Pull stories from the top of the ordered backlog into Sprint 1 until you reach about 20 points. Stop at the capacity line even if the next story is attractive.
11. Agree the team's Definition of Done as a checklist — coded, peer reviewed, tested, deployed to staging, and accepted by the Product Owner. Record it in the tool where the whole team can see it.
12. Confirm that every story in Sprint 1 serves the sprint goal. Remove any story that does not, however small it is.

## Self-check — are you done?

> Sprint 1 holds about 20 points, every story in it serves the one written sprint goal, no story exceeds 8 points, every story has Given/When/Then acceptance criteria, and the Definition of Done is visible to the whole team. A sprint whose stories serve four unrelated goals is a task list, not a sprint.

## Debrief — what this activity proves

- The sprint goal is the single most skipped artefact and the one that makes the sprint reviewable.
- Splitting by workflow step keeps every slice demonstrable; splitting by technical layer produces a sprint with nothing to show.
- This is A3 in practice: implementing Agile practices to reduce waste — an ordered backlog stops the team building the 62% nobody used.

---

Record your team's output in [WORKSHEET.md](WORKSHEET.md). The same instructions appear in the Learner Guide, section 6.3.
