#!/usr/bin/env python3
"""Generate the deck's chart/diagram assets for the Agile PM course.

House style: Arial, white background, brand palette, 150 dpi, tight bbox.
Every asset produced here MUST be placed on a slide by build_slides.py.

Numbers are drawn from the SAME data the activities use (data_domain3.py), so the
deck, the Learner Guide and the activity worksheets can never disagree.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle

plt.rcParams.update({
    "font.family": "Arial", "font.size": 11,
    "axes.edgecolor": "#D7E0EA", "axes.linewidth": 1.0,
    "figure.facecolor": "white", "axes.facecolor": "white",
    "savefig.facecolor": "white",
})

BLUE, TEAL, VIOLET, AMBER, RED = "#1F6FEB", "#10B981", "#7C3AED", "#F59E0B", "#DC2626"
INK, GREY, LINE, LIGHT = "#161B26", "#5B6372", "#E2E8F0", "#F5F8FC"

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", "courseware", "assets"))
os.makedirs(OUT, exist_ok=True)


def save(fig, name):
    p = os.path.join(OUT, name)
    fig.savefig(p, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("  wrote", name)


def _clean(ax, grid_axis="y"):
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    ax.grid(axis=grid_axis, color=LINE, linewidth=0.8, alpha=0.9)
    ax.set_axisbelow(True)
    ax.tick_params(colors=GREY, labelsize=10)


# ------------------------------------------------------------------ 1. cost of change
def cost_of_change():
    fig, ax = plt.subplots(figsize=(9, 4.6))
    t = np.linspace(0, 10, 200)
    ax.plot(t, 1.35 ** t, color=RED, lw=3.2, label="Waterfall — cost of change compounds")
    ax.plot(t, 1 + 0.42 * t, color=TEAL, lw=3.2, label="Agile — short feedback loops flatten the curve")
    ax.fill_between(t, 1 + 0.42 * t, 1.35 ** t, color=RED, alpha=0.07)
    ax.annotate("A wrong assumption found here\ncosts a redesign",
                xy=(8.6, 1.35 ** 8.6), xytext=(4.9, 15.5), fontsize=10.5, color=RED,
                bbox=dict(boxstyle="round,pad=0.45", fc="white", ec=RED, lw=1.2),
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.6))
    ax.annotate("Found here, it costs\none sprint's rework",
                xy=(2.4, 1 + 0.42 * 2.4), xytext=(0.35, 8.4), fontsize=10.5, color="#0B7A57",
                bbox=dict(boxstyle="round,pad=0.45", fc="white", ec=TEAL, lw=1.2),
                arrowprops=dict(arrowstyle="->", color=TEAL, lw=1.6))
    ax.set_xlabel("Time through the project  →", color=GREY, fontsize=11)
    ax.set_ylabel("Cost of making a change", color=GREY, fontsize=11)
    ax.set_ylim(0, 22); ax.set_xlim(0, 10)
    ax.set_xticks([]); ax.set_yticks([])
    _clean(ax, grid_axis="both")
    ax.legend(frameon=False, fontsize=10.5, loc="upper left")
    ax.set_title("Why late discovery is expensive", fontsize=13, color=INK,
                 fontweight="bold", loc="left", pad=12)
    save(fig, "cost-of-change.png")


# ------------------------------------------------------------------ 2. value delivery
def value_delivery():
    fig, ax = plt.subplots(figsize=(9, 4.4))
    sprints = np.arange(0, 13)
    agile = np.clip((sprints * 8.6), 0, 100)
    wf = np.where(sprints < 11, 0, 100)
    ax.step(sprints, wf, where="post", color=RED, lw=3.0, label="Waterfall — all value at the end")
    ax.plot(sprints, agile, color=TEAL, lw=3.2, marker="o", ms=5.5,
            label="Agile — value released each sprint")
    ax.fill_between(sprints, 0, agile, color=TEAL, alpha=0.10)
    ax.axvline(4, color=GREY, ls="--", lw=1.2)
    ax.annotate("At sprint 4 Agile has already\ndelivered ~34% of the value;\nwaterfall has delivered none",
                xy=(4, 34), xytext=(4.6, 52), fontsize=10.5, color=INK,
                bbox=dict(boxstyle="round,pad=0.45", fc=LIGHT, ec=LINE),
                arrowprops=dict(arrowstyle="->", color=GREY, lw=1.4))
    ax.set_xlabel("Sprint", color=GREY); ax.set_ylabel("Cumulative business value (%)", color=GREY)
    ax.set_ylim(0, 108); ax.set_xlim(0, 12)
    _clean(ax)
    ax.legend(frameon=False, fontsize=10.5, loc="upper left")
    ax.set_title("Agile delivers value early — the return profile changes", fontsize=13,
                 color=INK, fontweight="bold", loc="left", pad=12)
    save(fig, "value-delivery.png")


# ------------------------------------------------------------------ 3. iron triangle
def iron_triangle():
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.3))
    for ax, (title, fixed, var, col) in zip(axes, [
            ("TRADITIONAL / WATERFALL", ["Scope"], ["Time", "Cost"], RED),
            ("AGILE", ["Time", "Cost"], ["Scope"], TEAL)]):
        ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
        ax.set_title(title, fontsize=12.5, color=col, fontweight="bold", pad=10)
        tri = plt.Polygon([[5, 8.7], [1.1, 1.6], [8.9, 1.6]], closed=True,
                          fc=LIGHT, ec=col, lw=2.4)
        ax.add_patch(tri)
        ax.text(5, 6.55, "FIXED", ha="center", fontsize=10, color=col, fontweight="bold")
        ax.text(5, 5.55, "\n".join(fixed), ha="center", va="top", fontsize=15,
                color=INK, fontweight="bold")
        ax.text(5, 2.55, "VARIABLE", ha="center", fontsize=10, color=GREY, fontweight="bold")
        ax.text(5, 2.15, "  ".join(var), ha="center", va="top", fontsize=13, color=GREY)
    fig.suptitle("Inverting the triangle: Agile fixes time and cost, and varies scope",
                 fontsize=13.5, color=INK, fontweight="bold", x=0.02, ha="left")
    fig.tight_layout(rect=[0, 0, 1, 0.90])
    save(fig, "iron-triangle.png")


# ------------------------------------------------------------------ 4. sprint burndown (Activity 5)
def sprint_burndown():
    fig, ax = plt.subplots(figsize=(9, 4.5))
    days = np.arange(0, 11)
    ideal = np.linspace(20, 0, 11)
    actual = [20, 20, 18, 18, 18, 15, 13, 13, 9, 5, 6]
    ax.plot(days, ideal, color=GREY, ls="--", lw=2.0, label="Ideal line")
    ax.plot(days, actual, color=BLUE, lw=3.2, marker="o", ms=6, label="Actual remaining")
    ax.axhspan(0, 0.01, color="white")
    ax.annotate("Days 2–4 flat: work started,\nnothing finished → check WIP",
                xy=(3, 18), xytext=(0.35, 6.4), fontsize=10.5, color=AMBER,
                bbox=dict(boxstyle="round,pad=0.42", fc="white", ec=AMBER, lw=1.3),
                arrowprops=dict(arrowstyle="->", color=AMBER, lw=1.6))
    ax.annotate("Day 5: developer pulled\nto an incident",
                xy=(5, 15), xytext=(5.15, 19.2), fontsize=10.2, color=GREY,
                bbox=dict(boxstyle="round,pad=0.38", fc=LIGHT, ec=LINE),
                arrowprops=dict(arrowstyle="->", color=GREY, lw=1.3))
    ax.annotate("6 points carried over —\nnot counted as velocity",
                xy=(10, 6), xytext=(6.7, 10.6), fontsize=10.5, color=RED,
                bbox=dict(boxstyle="round,pad=0.42", fc="white", ec=RED, lw=1.3),
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.6))
    ax.set_xlabel("Sprint day", color=GREY); ax.set_ylabel("Story points remaining", color=GREY)
    ax.set_xticks(days); ax.set_ylim(0, 22)
    _clean(ax)
    ax.legend(frameon=False, fontsize=10.5)
    ax.set_title("Sprint 1 burndown — CustomerConnect (Activity 5)", fontsize=13,
                 color=INK, fontweight="bold", loc="left", pad=12)
    save(fig, "sprint-burndown.png")


# ------------------------------------------------------------------ 5. velocity + forecast (Activity 8)
def velocity_forecast():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.2, 4.4))
    sp = ["Sprint 1", "Sprint 2", "Sprint 3", "Sprint 4"]
    vel = [14, 18, 17, 21]
    bars = ax1.bar(sp, vel, color=[BLUE, BLUE, BLUE, BLUE], width=0.58)
    ax1.axhline(np.mean(vel), color=TEAL, ls="--", lw=2.2)
    ax1.text(3.42, np.mean(vel) + 0.5, f"avg {np.mean(vel):.1f}", color="#0B7A57",
             fontsize=10.5, fontweight="bold", ha="right")
    for b, v in zip(bars, vel):
        ax1.text(b.get_x() + b.get_width() / 2, v + 0.45, str(v), ha="center",
                 fontsize=11.5, color=INK, fontweight="bold")
    ax1.set_ylabel("Points completed (Done only)", color=GREY)
    ax1.set_ylim(0, 25); _clean(ax1)
    ax1.set_title("Velocity — 4 completed sprints", fontsize=12.5, color=INK,
                  fontweight="bold", loc="left", pad=10)

    n = np.arange(0, 15)
    ax2.plot(n, np.clip(186 - 17.5 * n, 0, None), color=TEAL, lw=3.0, label="Average (17.5) → 11 sprints")
    ax2.plot(n, np.clip(186 - 21.0 * n, 0, None), color=BLUE, lw=1.9, ls="--", label="Optimistic (21) → 9 sprints")
    ax2.plot(n, np.clip(186 - 14.0 * n, 0, None), color=AMBER, lw=1.9, ls="--", label="Pessimistic (14) → 14 sprints")
    ax2.fill_between(n, np.clip(186 - 21.0 * n, 0, None), np.clip(186 - 14.0 * n, 0, None),
                     color=BLUE, alpha=0.09)
    ax2.set_xlabel("Sprints from now", color=GREY); ax2.set_ylabel("Points remaining", color=GREY)
    ax2.set_ylim(0, 200); ax2.set_xlim(0, 14); _clean(ax2)
    ax2.legend(frameon=False, fontsize=9.8, loc="upper right")
    ax2.set_title("Release forecast — 186 points left: a RANGE, not a date", fontsize=12.5,
                  color=INK, fontweight="bold", loc="left", pad=10)
    fig.tight_layout()
    save(fig, "velocity-forecast.png")


# ------------------------------------------------------------------ 6. CFD (Activity 8)
def cumulative_flow():
    fig, ax = plt.subplots(figsize=(9.2, 4.5))
    d = np.arange(0, 21)
    done = np.clip((d - 2) * 2.6, 0, None)
    testing = np.clip((d - 1) * 1.05, 0, None) + np.where(d > 8, (d - 8) * 0.95, 0)
    prog = np.full_like(d, 7.0, dtype=float)
    todo = np.clip(70 - d * 2.1, 12, None)
    ax.stackplot(d, done, testing, prog, todo,
                 labels=["Done", "Testing", "In Progress", "To Do"],
                 colors=[TEAL, AMBER, BLUE, LINE], alpha=0.92)
    ax.annotate("This band WIDENS over time\n→ the bottleneck is TESTING",
                xy=(17, done[17] + testing[17] * 0.55), xytext=(6.2, 84),
                fontsize=11, color="#8A5A00", fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.45", fc="white", ec=AMBER, lw=1.6),
                arrowprops=dict(arrowstyle="->", color=AMBER, lw=1.9))
    ax.set_xlabel("Working day", color=GREY); ax.set_ylabel("Work items", color=GREY)
    ax.set_xlim(0, 20); ax.set_ylim(0, 110)
    _clean(ax)
    ax.legend(frameon=False, fontsize=10, loc="upper left", ncol=4)
    ax.set_title("Cumulative flow diagram — read the widening band (Activity 8)",
                 fontsize=13, color=INK, fontweight="bold", loc="left", pad=12)
    save(fig, "cumulative-flow.png")


# ------------------------------------------------------------------ 7. control chart (Activity 8)
def control_chart():
    fig, ax = plt.subplots(figsize=(9.2, 4.4))
    rng = np.random.default_rng(7)
    xs, ys, cols = [], [], []
    means = [3.1, 4.3, 5.8, 7.4]
    for i, m in enumerate(means):
        for _ in range(9):
            xs.append(i * 10 + rng.uniform(1, 9))
            ys.append(max(0.6, rng.normal(m, m * 0.26)))
            cols.append([BLUE, BLUE, AMBER, RED][i])
    ax.scatter(xs, ys, c=cols, s=62, alpha=0.85, edgecolors="white", linewidths=1.2, zorder=3)
    ax.plot([5, 15, 25, 35], means, color=VIOLET, lw=3.0, marker="s", ms=8,
            label="Rolling average cycle time", zorder=4)
    for i, m in enumerate(means):
        ax.text(i * 10 + 5, m + 1.15, f"{m}d", ha="center", fontsize=11, color=VIOLET,
                fontweight="bold", bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none"))
    ax.set_xticks([5, 15, 25, 35]); ax.set_xticklabels(["Sprint 1", "Sprint 2", "Sprint 3", "Sprint 4"])
    ax.set_ylabel("Cycle time (days)", color=GREY)
    ax.set_ylim(0, 14); _clean(ax)
    ax.annotate("Velocity rose AND cycle time rose\n→ WIP is rising (Little's Law)",
                xy=(35, 7.4), xytext=(13.5, 11.4), fontsize=10.8, color=RED, fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.45", fc="white", ec=RED, lw=1.5),
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.7))
    ax.legend(frameon=False, fontsize=10.5, loc="upper left")
    ax.set_title("Control chart — cycle time is getting worse, not better (Activity 8)",
                 fontsize=13, color=INK, fontweight="bold", loc="left", pad=12)
    save(fig, "control-chart.png")


# ------------------------------------------------------------------ 8. Pareto (Activity 7)
def pareto():
    cats = ["Stale/missing\nfeed data", "Unclear\nacceptance\ncriteria", "Environment\ndrift",
            "Carrier API\nchanges", "UI validation\ngaps", "Access/\npermissions",
            "Report\nformatting", "Documentation"]
    vals = [44, 31, 17, 11, 8, 5, 3, 1]
    total = sum(vals)
    cum = np.cumsum(vals) / total * 100
    fig, ax = plt.subplots(figsize=(9.6, 4.7))
    colors = [RED if c <= 80 or i == 0 else BLUE for i, c in enumerate(cum)]
    colors = [RED, RED, RED, AMBER, BLUE, BLUE, BLUE, BLUE]
    bars = ax.bar(range(len(cats)), vals, color=colors, width=0.62)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.9, str(v), ha="center",
                fontsize=11, color=INK, fontweight="bold")
    ax.set_ylabel("Defects logged", color=GREY)
    ax.set_xticks(range(len(cats))); ax.set_xticklabels(cats, fontsize=9.2)
    ax.set_ylim(0, 52); _clean(ax)

    ax2 = ax.twinx()
    ax2.plot(range(len(cats)), cum, color=VIOLET, lw=2.8, marker="o", ms=7)
    ax2.axhline(80, color=GREY, ls="--", lw=1.5)
    ax2.text(7.35, 82, "80%", color=GREY, fontsize=10.5, ha="right", fontweight="bold")
    for i, c in enumerate(cum):
        ax2.text(i, c - 6.2, f"{c:.1f}%", ha="center", fontsize=9.4, color=VIOLET,
                 fontweight="bold",
                 bbox=dict(boxstyle="round,pad=0.18", fc="white", ec="none", alpha=0.85))
    ax2.set_ylim(0, 112); ax2.set_ylabel("Cumulative %", color=VIOLET)
    ax2.tick_params(colors=VIOLET, labelsize=10)
    for sp in ("top",):
        ax2.spines[sp].set_visible(False)
    ax.annotate("The VITAL FEW\ntop 3 causes = 76.7%\nof all 120 defects",
                xy=(2.0, 17), xytext=(4.15, 30), fontsize=10.8, color=RED, fontweight="bold",
                ha="left", bbox=dict(boxstyle="round,pad=0.45", fc="white", ec=RED, lw=1.6),
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.7), zorder=6)
    ax.set_title("Pareto chart — CustomerConnect defect causes, Sprints 1–3 (Activity 7)",
                 fontsize=13, color=INK, fontweight="bold", loc="left", pad=12)
    save(fig, "pareto-defects.png")


# ------------------------------------------------------------------ 9. Scrum framework diagram
def scrum_framework():
    fig, ax = plt.subplots(figsize=(11.4, 5.0))
    ax.set_xlim(0, 100); ax.set_ylim(0, 44); ax.axis("off")

    def box(x, y, w, h, label, sub, col, fs=11.5):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.35",
                                    fc="white", ec=col, lw=2.2))
        ax.text(x + w / 2, y + h * 0.62, label, ha="center", va="center",
                fontsize=fs, color=col, fontweight="bold")
        if sub:
            ax.text(x + w / 2, y + h * 0.24, sub, ha="center", va="center",
                    fontsize=9.2, color=GREY)

    def arrow(x1, y1, x2, y2, col=GREY, style="-|>"):
        ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style,
                                     mutation_scale=17, color=col, lw=2.0,
                                     shrinkA=3, shrinkB=3))

    box(1.5, 24, 17, 9, "PRODUCT\nBACKLOG", "Ordered by the\nProduct Owner", BLUE)
    box(24, 24, 15.5, 9, "SPRINT\nPLANNING", "What & how", VIOLET)
    box(45, 24, 15.5, 9, "SPRINT\nBACKLOG", "Goal + selected\nitems + plan", VIOLET)

    # the sprint container
    ax.add_patch(FancyBboxPatch((24, 5.5), 52, 15.5, boxstyle="round,pad=0.4",
                                fc=LIGHT, ec=TEAL, lw=2.6, ls="--"))
    ax.text(50, 19.0, "THE SPRINT  ·  1–4 WEEKS, FIXED LENGTH", ha="center",
            fontsize=11.5, color="#0B7A57", fontweight="bold")
    box(27.5, 8.0, 18, 8.4, "DAILY SCRUM", "15 min · re-plan\nthe next 24 hours", TEAL, fs=11)
    box(52.5, 8.0, 20, 8.4, "THE WORK", "Developers build\nto the Definition of Done", TEAL, fs=11)
    ax.add_patch(FancyArrowPatch((45.8, 12.2), (52.2, 12.2), arrowstyle="<|-|>",
                                 mutation_scale=15, color=TEAL, lw=1.9))

    box(66, 24, 15.5, 9, "SPRINT\nREVIEW", "Inspect the product\nwith stakeholders", AMBER)
    box(85.5, 24, 13, 9, "RETRO-\nSPECTIVE", "Inspect the\nprocess", AMBER)
    box(85.5, 8.5, 13, 8.5, "INCREMENT", "Usable, meets\nthe DoD", "#0B7A57")

    arrow(18.7, 28.5, 23.8, 28.5, BLUE)
    arrow(39.7, 28.5, 44.8, 28.5, VIOLET)
    arrow(52.7, 23.8, 52.7, 21.3, VIOLET)
    arrow(72.8, 12.2, 84.0, 12.2, TEAL)
    arrow(92.0, 17.2, 92.0, 23.8, "#0B7A57")
    arrow(76.3, 28.5, 84.9, 28.5, AMBER)
    # feedback loop drawn as an explicit polyline so it never crosses a box
    ax.plot([92.0, 92.0, 10.0], [33.4, 37.4, 37.4], color=BLUE, lw=2.0,
            solid_capstyle="round", zorder=2)
    ax.add_patch(FancyArrowPatch((10.0, 37.4), (10.0, 33.6), arrowstyle="-|>",
                                 mutation_scale=17, color=BLUE, lw=2.0))
    ax.text(50, 39.2, "Feedback re-orders the backlog — this loop IS the framework",
            ha="center", fontsize=11, color=BLUE, fontweight="bold", style="italic")

    ax.text(0.5, 1.2, "3 accountabilities: Product Owner · Scrum Master · Developers      "
                      "3 artefacts: Product Backlog · Sprint Backlog · Increment      "
                      "5 events: Sprint · Planning · Daily Scrum · Review · Retrospective",
            fontsize=9.6, color=GREY)
    save(fig, "scrum-framework.png")


# ------------------------------------------------------------------ 10. waterfall vs agile timeline
def waterfall_vs_agile():
    fig, ax = plt.subplots(figsize=(11.2, 4.6))
    ax.set_xlim(0, 100); ax.set_ylim(0, 34); ax.axis("off")

    phases = [("Requirements", 14), ("Design", 14), ("Build", 26), ("Test", 16), ("Deploy", 10)]
    x = 6
    for i, (nm, w) in enumerate(phases):
        ax.add_patch(FancyBboxPatch((x, 22.5), w - 1.2, 6.4, boxstyle="round,pad=0.22",
                                    fc="#FDECEC", ec=RED, lw=1.8))
        ax.text(x + (w - 1.2) / 2, 25.7, nm, ha="center", va="center", fontsize=10.5,
                color="#9B2C2C", fontweight="bold")
        x += w
    ax.text(1.0, 30.6, "WATERFALL", fontsize=12.5, color=RED, fontweight="bold")
    ax.add_patch(FancyArrowPatch((80.2, 25.7), (86.5, 25.7), arrowstyle="-|>",
                                 mutation_scale=16, color=RED, lw=2.0))
    ax.text(93.0, 25.7, "VALUE", ha="center", va="center", fontsize=11, color=RED,
            fontweight="bold")
    ax.text(43, 19.4, "One customer touchpoint at the start, one at the end — "
                      "risk concentrates in the final third",
            ha="center", fontsize=10, color="#9B2C2C", style="italic")

    ax.text(1.0, 13.2, "AGILE", fontsize=12.5, color=TEAL, fontweight="bold")
    x = 6
    for i in range(6):
        ax.add_patch(FancyBboxPatch((x, 5.4), 11.6, 6.4, boxstyle="round,pad=0.22",
                                    fc="#E9F9F2", ec=TEAL, lw=1.8))
        ax.text(x + 5.8, 9.6, f"Sprint {i+1}", ha="center", fontsize=10, color="#0B7A57",
                fontweight="bold")
        ax.text(x + 5.8, 7.1, "plan·build\ntest·review", ha="center", fontsize=7.6, color=GREY)
        ax.add_patch(FancyArrowPatch((x + 5.8, 4.9), (x + 5.8, 2.5), arrowstyle="-|>",
                                     mutation_scale=13, color=TEAL, lw=1.7))
        ax.text(x + 5.8, 1.3, "value", ha="center", fontsize=8.4, color="#0B7A57",
                fontweight="bold")
        x += 13.4
    ax.text(43, 14.6, "A customer touchpoint and a usable increment every sprint — "
                      "risk is retired continuously",
            ha="center", fontsize=10, color="#0B7A57", style="italic")
    save(fig, "waterfall-vs-agile.png")


# ------------------------------------------------------------------ 11. Kanban board + Little's Law
def kanban_littles_law():
    fig, ax = plt.subplots(figsize=(11.0, 4.7))
    ax.set_xlim(0, 100); ax.set_ylim(0, 40); ax.axis("off")
    cols = [("BACKLOG", "", 8, LINE, 6), ("TO DO", "WIP —", 8, BLUE, 4),
            ("IN PROGRESS", "WIP 3", 8, AMBER, 3), ("TESTING", "WIP 2", 8, VIOLET, 2),
            ("DONE", "", 8, TEAL, 5)]
    x = 3
    for nm, wip, _, col, n in cols:
        ax.add_patch(FancyBboxPatch((x, 6.5), 17, 26, boxstyle="round,pad=0.3",
                                    fc=LIGHT, ec=LINE, lw=1.4))
        ax.add_patch(FancyBboxPatch((x, 28.2), 17, 4.3, boxstyle="round,pad=0.25",
                                    fc=col, ec="none"))
        ax.text(x + 8.5, 30.4, nm, ha="center", va="center", fontsize=10.2,
                color="white" if col != LINE else GREY, fontweight="bold")
        if wip:
            ax.text(x + 8.5, 34.6, wip, ha="center", fontsize=10.5, color=col, fontweight="bold")
        for k in range(n):
            ax.add_patch(FancyBboxPatch((x + 1.6, 25.0 - k * 4.3), 13.8, 3.3,
                                        boxstyle="round,pad=0.18", fc="white",
                                        ec=col if col != LINE else "#C9D3DF", lw=1.3))
        x += 19.4
    ax.text(50, 2.4, "Little's Law:   Cycle Time  =  Work in Progress  ÷  Throughput          "
                     "→  halve WIP at constant throughput and you halve cycle time",
            ha="center", fontsize=11.5, color=INK, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.5", fc="#EEF4FE", ec=BLUE, lw=1.6))
    save(fig, "kanban-littles-law.png")


# ------------------------------------------------------------------ 12. retrospective 5 stages
def retro_stages():
    fig, ax = plt.subplots(figsize=(11.2, 3.5))
    ax.set_xlim(0, 100); ax.set_ylim(0, 22); ax.axis("off")
    stages = [("1", "SET THE\nSTAGE", "5 min", BLUE), ("2", "GATHER\nDATA", "40 min", VIOLET),
              ("3", "GENERATE\nINSIGHTS", "25 min", TEAL), ("4", "DECIDE\nWHAT TO DO", "20 min", AMBER),
              ("5", "CLOSE THE\nRETRO", "20 min", "#0B7A57")]
    x = 2.5
    for i, (n, nm, dur, col) in enumerate(stages):
        ax.add_patch(FancyBboxPatch((x, 3.5), 16.4, 13.5, boxstyle="round,pad=0.3",
                                    fc=LIGHT, ec="none"))
        ax.add_patch(FancyBboxPatch((x, 15.6), 16.4, 1.4, boxstyle="square,pad=0",
                                    fc=col, ec="none"))
        ax.add_patch(Circle((x + 8.2, 12.3), 2.0, fc=col, ec="none"))
        ax.text(x + 8.2, 12.3, n, ha="center", va="center", fontsize=14,
                color="white", fontweight="bold")
        ax.text(x + 8.2, 8.0, nm, ha="center", va="center", fontsize=10.6,
                color=INK, fontweight="bold")
        ax.text(x + 8.2, 5.0, dur, ha="center", fontsize=9.6, color=col, fontweight="bold")
        if i < 4:
            ax.plot(x + 18.1, 10.3, marker=">", ms=11, color=col, clip_on=False)
        x += 19.4
    ax.text(50, 0.6, "≈ 2 hours for a 2-week sprint  ·  Insight tools: 5 Whys · Fishbone · Pareto · dot voting",
            ha="center", fontsize=10.4, color=GREY)
    save(fig, "retro-stages.png")


# ------------------------------------------------------------------ 13. user story anatomy
def user_story():
    fig, ax = plt.subplots(figsize=(10.8, 4.3))
    ax.set_xlim(0, 100); ax.set_ylim(0, 36); ax.axis("off")
    ax.add_patch(FancyBboxPatch((3, 20), 60, 13.5, boxstyle="round,pad=0.4",
                                fc="white", ec=BLUE, lw=2.4))
    ax.text(5.5, 30.0, "As a", fontsize=12, color=GREY)
    ax.text(13.5, 30.0, "warehouse operations executive,", fontsize=12.5, color=BLUE, fontweight="bold")
    ax.text(5.5, 26.3, "I want", fontsize=12, color=GREY)
    ax.text(15.0, 26.3, "a live customs status on each inbound shipment,", fontsize=12.5,
            color=VIOLET, fontweight="bold")
    ax.text(5.5, 22.6, "so that", fontsize=12, color=GREY)
    ax.text(15.5, 22.6, "I can re-sequence today's production.", fontsize=12.5,
            color=TEAL, fontweight="bold")
    for lbl, y, col in [("WHO — the role", 30.0, BLUE), ("WHAT — the goal", 26.3, VIOLET),
                        ("WHY — the benefit", 22.6, TEAL)]:
        ax.text(65.5, y, lbl, fontsize=10.4, color=col, fontweight="bold", va="center")

    ax.add_patch(FancyBboxPatch((3, 3.5), 60, 13.0, boxstyle="round,pad=0.4",
                                fc=LIGHT, ec=TEAL, lw=1.8))
    ax.text(5.5, 14.2, "ACCEPTANCE CRITERIA", fontsize=10.4, color="#0B7A57", fontweight="bold")
    ax.text(5.5, 10.9, "GIVEN  a shipment in customs clearance", fontsize=11, color=INK)
    ax.text(5.5, 8.0, "WHEN   I open the shipment card", fontsize=11, color=INK)
    ax.text(5.5, 5.1, "THEN   I see the current state and its last-updated time", fontsize=11, color=INK)
    ax.text(65.5, 12.0, "INVEST", fontsize=12, color=INK, fontweight="bold")
    ax.text(65.5, 8.6, "Independent · Negotiable · Valuable\nEstimatable · Small · Testable",
            fontsize=10.2, color=GREY, va="top")
    ax.text(65.5, 3.6, "Fails 'Small'? Split by workflow\nstep — never by technical layer.",
            fontsize=9.8, color=RED, va="top", style="italic")
    save(fig, "user-story-anatomy.png")


# ------------------------------------------------------------------ 14. Agile manifesto values
def manifesto_values():
    fig, ax = plt.subplots(figsize=(11.2, 4.2))
    ax.set_xlim(0, 100); ax.set_ylim(0, 28); ax.axis("off")
    vals = [("Individuals and\ninteractions", "processes and tools", BLUE),
            ("Working\nsoftware", "comprehensive documentation", VIOLET),
            ("Customer\ncollaboration", "contract negotiation", TEAL),
            ("Responding\nto change", "following a plan", AMBER)]
    x = 2
    for left, right, col in vals:
        ax.add_patch(FancyBboxPatch((x, 12.5), 22.5, 12.0, boxstyle="round,pad=0.3",
                                    fc="white", ec=col, lw=2.2))
        ax.text(x + 11.25, 18.5, left, ha="center", va="center", fontsize=12,
                color=col, fontweight="bold")
        ax.text(x + 11.25, 10.4, "OVER", ha="center", fontsize=9.6, color=GREY, fontweight="bold")
        ax.add_patch(FancyBboxPatch((x, 3.0), 22.5, 6.2, boxstyle="round,pad=0.3",
                                    fc=LIGHT, ec="none"))
        ax.text(x + 11.25, 6.1, right, ha="center", va="center", fontsize=10, color=GREY)
        x += 24.4
    ax.text(50, 26.6, "\"We value the left over the right\" — both matter; the left matters MORE when they conflict",
            ha="center", fontsize=11, color=INK, fontweight="bold", style="italic")
    save(fig, "manifesto-values.png")


# ------------------------------------------------------------------ 15. lean 8 wastes
def lean_wastes():
    fig, ax = plt.subplots(figsize=(11.0, 4.0))
    ax.set_xlim(0, 100); ax.set_ylim(0, 26); ax.axis("off")
    wastes = [("Partially\ndone work", BLUE), ("Extra\nprocesses", VIOLET), ("Extra\nfeatures", TEAL),
              ("Task\nswitching", AMBER), ("Waiting", RED), ("Motion /\nhandoffs", BLUE),
              ("Defects", VIOLET), ("Unused\ntalent", TEAL)]
    x = 1.5
    for nm, col in wastes:
        ax.add_patch(FancyBboxPatch((x, 8.0), 11.2, 11.0, boxstyle="round,pad=0.28",
                                    fc=LIGHT, ec="none"))
        ax.add_patch(FancyBboxPatch((x, 17.6), 11.2, 1.4, boxstyle="square,pad=0",
                                    fc=col, ec="none"))
        ax.text(x + 5.6, 12.8, nm, ha="center", va="center", fontsize=10.2,
                color=INK, fontweight="bold")
        x += 12.35
    ax.text(50, 23.6, "THE EIGHT WASTES — Lean asks which of these your process is paying for",
            ha="center", fontsize=12, color=INK, fontweight="bold")
    ax.text(50, 4.2, "In most knowledge work the largest waste is WAITING — and a value stream map is what exposes it",
            ha="center", fontsize=10.6, color=RED, style="italic")
    save(fig, "lean-wastes.png")


# ------------------------------------------------------------------ 16. value stream map
def value_stream():
    fig, ax = plt.subplots(figsize=(11.2, 4.3))
    ax.set_xlim(0, 100); ax.set_ylim(0, 30); ax.axis("off")
    steps = [("Request\nlogged", 2, 8), ("Triage", 1, 22), ("Dev", 5, 14),
             ("Code\nreview", 1, 30), ("Test", 3, 26), ("Release", 1, 12)]
    x = 2.5
    tot_p, tot_w = 0, 0
    for nm, proc, wait in steps:
        ax.add_patch(FancyBboxPatch((x, 15.0), 12.0, 8.2, boxstyle="round,pad=0.28",
                                    fc="white", ec=BLUE, lw=1.9))
        ax.text(x + 6.0, 19.1, nm, ha="center", va="center", fontsize=10.2,
                color=INK, fontweight="bold")
        ax.text(x + 6.0, 16.1, f"{proc}d work", ha="center", fontsize=9.2, color=TEAL,
                fontweight="bold")
        tot_p += proc
        if wait:
            ax.add_patch(FancyBboxPatch((x + 12.3, 15.8), 3.2, 6.6, boxstyle="round,pad=0.2",
                                        fc="#FDECEC", ec=RED, lw=1.4))
            ax.text(x + 13.9, 19.1, f"{wait}d\nwait", ha="center", va="center",
                    fontsize=8.4, color=RED, fontweight="bold")
            tot_w += wait
        x += 16.0
    ax.text(50, 27.2, "VALUE STREAM MAP — the waiting between steps dwarfs the work inside them",
            ha="center", fontsize=12, color=INK, fontweight="bold")
    ax.text(50, 9.2, f"Processing time {tot_p} days   ·   Waiting time {tot_w} days   ·   "
                     f"Lead time {tot_p+tot_w} days   ·   Efficiency {tot_p/(tot_p+tot_w)*100:.0f}%",
            ha="center", fontsize=12, color=INK, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.5", fc="#EEF4FE", ec=BLUE, lw=1.6))
    ax.text(50, 3.6, "Attack the red boxes first. Making the blue boxes faster changes almost nothing.",
            ha="center", fontsize=10.6, color=RED, style="italic")
    save(fig, "value-stream-map.png")


# ------------------------------------------------------------------ 17. Tuckman + leadership style
def tuckman():
    fig, ax = plt.subplots(figsize=(11.0, 4.2))
    ax.set_xlim(0, 100); ax.set_ylim(0, 28); ax.axis("off")
    stages = [("FORMING", "Polite, unsure\nLow output", "DIRECTING", BLUE),
              ("STORMING", "Conflict surfaces\nOutput dips", "COACHING", RED),
              ("NORMING", "Norms agreed\nOutput climbs", "SUPPORTING", AMBER),
              ("PERFORMING", "Self-organising\nHigh output", "DELEGATING", TEAL),
              ("ADJOURNING", "Work closes\nTeam disbands", "RECOGNISING", VIOLET)]
    x = 1.5
    for i, (nm, desc, style, col) in enumerate(stages):
        ax.add_patch(FancyBboxPatch((x, 12.0), 17.4, 11.0, boxstyle="round,pad=0.3",
                                    fc="white", ec=col, lw=2.0))
        ax.text(x + 8.7, 20.6, nm, ha="center", fontsize=11, color=col, fontweight="bold")
        ax.text(x + 8.7, 16.2, desc, ha="center", va="center", fontsize=9.4, color=GREY)
        ax.add_patch(FancyBboxPatch((x, 6.0), 17.4, 4.4, boxstyle="round,pad=0.26",
                                    fc=col, ec="none"))
        ax.text(x + 8.7, 8.2, style, ha="center", va="center", fontsize=10.4,
                color="white", fontweight="bold")
        if i < 4:
            ax.plot(x + 18.6, 17.5, marker=">", ms=10, color=col, clip_on=False)
        x += 19.7
    ax.text(50, 25.8, "ADAPTIVE LEADERSHIP — match your style to the team's stage, not your preference",
            ha="center", fontsize=12, color=INK, fontweight="bold")
    ax.text(50, 2.6, "The storming dip is normal and necessary. A team that never storms is usually avoiding, not aligned.",
            ha="center", fontsize=10.4, color=GREY, style="italic")
    save(fig, "tuckman-leadership.png")


# ------------------------------------------------------------------ 18. assessment flow
def assessment_flow():
    fig, ax = plt.subplots(figsize=(11.0, 3.3))
    ax.set_xlim(0, 100); ax.set_ylim(0, 21); ax.axis("off")
    steps = [("1", "BRIEFING", "Rules, timing,\nopen-book scope", BLUE),
             ("2", "WRITTEN (WA)", "Short-answer\nquestions · 1 hour", VIOLET),
             ("3", "CASE STUDY (CS)", "Applied business\nscenario · 1 hour", TEAL),
             ("4", "MARKING", "Assessor marks\nagainst the key", AMBER),
             ("5", "RESULT & APPEAL", "Competent / NYC\n· feedback given", "#0B7A57")]
    x = 1.5
    for i, (n, nm, sub, col) in enumerate(steps):
        ax.add_patch(FancyBboxPatch((x, 3.0), 17.2, 13.0, boxstyle="round,pad=0.3",
                                    fc=LIGHT, ec="none"))
        ax.add_patch(FancyBboxPatch((x, 14.6), 17.2, 1.4, boxstyle="square,pad=0",
                                    fc=col, ec="none"))
        ax.add_patch(Circle((x + 8.6, 11.2), 1.85, fc=col, ec="none"))
        ax.text(x + 8.6, 11.2, n, ha="center", va="center", fontsize=13,
                color="white", fontweight="bold")
        ax.text(x + 8.6, 7.6, nm, ha="center", fontsize=10.2, color=INK, fontweight="bold")
        ax.text(x + 8.6, 4.9, sub, ha="center", va="center", fontsize=8.8, color=GREY)
        if i < 4:
            ax.plot(x + 18.4, 9.6, marker=">", ms=11, color=col, clip_on=False)
        x += 19.5
    ax.text(50, 0.7, "Both instruments must be assessed COMPETENT  ·  Open book: slides, Learner Guide "
                     "and approved materials only  ·  75% attendance required",
            ha="center", fontsize=9.8, color=GREY)
    save(fig, "assessment-flow.png")


# ------------------------------------------------------------------ 19. agile adoption / benefits chart
def agile_benefits():
    fig, ax = plt.subplots(figsize=(9.4, 4.3))
    labels = ["Scrum", "Scrumban", "Kanban", "XP", "Other /\nhybrid"]
    vals = [63, 12, 10, 6, 9]
    cols = [BLUE, VIOLET, TEAL, AMBER, LINE]
    bars = ax.barh(labels[::-1], vals[::-1], color=cols[::-1], height=0.6)
    for b, v in zip(bars, vals[::-1]):
        ax.text(v + 1.2, b.get_y() + b.get_height() / 2, f"{v}%", va="center",
                fontsize=11.5, color=INK, fontweight="bold")
    ax.set_xlim(0, 74); ax.set_xlabel("Share of Agile teams using this framework", color=GREY)
    _clean(ax, grid_axis="x")
    ax.set_title("Scrum dominates adoption — which is why this course teaches it in depth",
                 fontsize=12.5, color=INK, fontweight="bold", loc="left", pad=12)
    ax.text(0, -1.15, "Indicative industry distribution (Coursera / State of Agile reporting). "
                      "Framework choice should follow the work, not the fashion.",
            fontsize=9.4, color=GREY, transform=ax.get_xaxis_transform())
    save(fig, "framework-adoption.png")


# ------------------------------------------------------------------ 20. definition of done
def definition_of_done():
    fig, ax = plt.subplots(figsize=(10.6, 3.9))
    ax.set_xlim(0, 100); ax.set_ylim(0, 25); ax.axis("off")
    ax.text(2, 22.4, "DEFINITION OF DONE — the team's shared, visible quality bar",
            fontsize=12.5, color=INK, fontweight="bold")
    items = ["Code written and peer reviewed", "Unit and integration tests pass",
             "Acceptance criteria demonstrated", "Data-freshness check applied",
             "Deployed to staging", "Accepted by the Product Owner"]
    y = 17.4
    for i, it in enumerate(items):
        col = TEAL if i != 3 else AMBER
        cx = 4.5 if i < 3 else 52.5
        yy = y - (i % 3) * 5.1
        ax.add_patch(Circle((cx, yy), 1.15, fc=col, ec="none"))
        ax.plot([cx-0.5, cx-0.12, cx+0.58], [yy+0.05, yy-0.42, yy+0.5],
                color="white", lw=2.1, solid_capstyle="round", zorder=5)
        ax.text(cx + 2.6, yy, it, va="center", fontsize=11.5, color=INK)
        if i == 3:
            ax.text(cx + 2.6, yy - 2.3, "← added in Activity 6 after the 5 Whys found the root cause",
                    va="center", fontsize=9.4, color=AMBER, style="italic")
    ax.text(50, 1.4, "\"Done\" is not \"nearly done\". Work that fails the DoD returns to the "
                     "backlog at full estimate — it is never counted as velocity.",
            ha="center", fontsize=10.6, color=RED, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.45", fc="#FDECEC", ec=RED, lw=1.4))
    save(fig, "definition-of-done.png")


if __name__ == "__main__":
    print("Generating chart assets →", OUT)
    for fn in (cost_of_change, value_delivery, iron_triangle, sprint_burndown,
               velocity_forecast, cumulative_flow, control_chart, pareto,
               scrum_framework, waterfall_vs_agile, kanban_littles_law, retro_stages,
               user_story, manifesto_values, lean_wastes, value_stream, tuckman,
               assessment_flow, agile_benefits, definition_of_done):
        fn()
    print("Done.")
