#!/usr/bin/env python3
"""Generate the learner objective checklist from the objective map.

Usage:
    python3 tools/build-checklist.py

Writes handouts/objective-checklist.md — all 57 exam objectives with the session
that teaches each one and three columns to self-rate. Learners carry this for
the whole course; Sessions 11 and 12 are built around it.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAP = ROOT / "curriculum" / "exam-objective-map.md"
OUT = ROOT / "handouts" / "objective-checklist.md"

DOMAINS = {
    "1": ("Describe cloud concepts", "25–30%"),
    "2": ("Describe Azure architecture and services", "35–40%"),
    "3": ("Describe Azure management and governance", "30–35%"),
}
GROUPS = {
    "1.1": "Describe cloud computing",
    "1.2": "Describe the benefits of using cloud services",
    "1.3": "Describe cloud service types",
    "2.1": "Describe the core architectural components of Azure",
    "2.2": "Describe Azure compute and networking services",
    "2.3": "Describe Azure storage services",
    "2.4": "Describe Azure identity, access, and security",
    "3.1": "Describe cost management in Azure",
    "3.2": "Describe features and tools in Azure for governance and compliance",
    "3.3": "Describe features and tools for managing and deploying Azure resources",
    "3.4": "Describe monitoring tools in Azure",
}

ROW = re.compile(r"^\| (\d\.\d\.\d) \| (.+?) \| (S\d+) \| [^|]* \| [^|]* \| [^|]* \|$", re.M)


def main() -> None:
    rows = ROW.findall(MAP.read_text())
    if len(rows) != 57:
        raise SystemExit(f"expected 57 objectives, parsed {len(rows)}")

    lines = [
        "# AZ-900 Objective Checklist",
        "",
        '**Name:** <span class="blank"></span>',
        "",
        "All 57 objectives Microsoft publishes for Exam AZ-900. Bring this to every session.",
        "",
        "After each quiz review, mark every objective you were assessed on:",
        "",
        "- **C — Confident.** I could explain this to someone else and pick it out of a scenario.",
        "- **S — Shaky.** I recognize it but would not bet on a question about it.",
        "- **B — Blank.** I could not say what this is.",
        "",
        "Re-mark objectives as they come back around; the point is the change over time, not",
        "the first answer. Session 11 asks you to rate all of these, and Session 12 builds the",
        "gap clinic from what the class marked S and B. **You are ready for the exam when",
        "nothing is marked B.**",
        "",
        "Taught column: the session where the objective is first taught. It is then practiced,",
        "quizzed, and revisited in later sessions.",
        "",
    ]

    current_domain = current_group = None
    for objective_id, text, session in rows:
        domain = objective_id[0]
        group = objective_id[:3]
        if domain != current_domain:
            name, weight = DOMAINS[domain]
            lines += ["", f"## Domain {domain} — {name} ({weight})", ""]
            current_domain = domain
            current_group = None
        if group != current_group:
            # The blank line matters: a heading directly after a table row is
            # parsed as another row of that table.
            lines += [
                "",
                f"### {group} {GROUPS[group]}",
                "",
                "| ID | Objective | Taught | C | S | B |",
                "| --- | --- | --- | --- | --- | --- |",
            ]
            current_group = group
        clean = re.sub(r"\s+", " ", text).strip()
        lines.append(f"| {objective_id} | {clean} | {session} |  |  |  |")

    lines += [
        "",
        "<!-- pagebreak -->",
        "",
        "## Readiness record",
        "",
        "| Instrument | Score | Domain 1 | Domain 2 | Domain 3 | Objectives to repair |",
        "| --- | --- | --- | --- | --- | --- |",
        "| Domain 1 checkpoint (S3) |  | — | — | — |  |",
        "| Domain 2 checkpoint (S8) |  | — | — | — |  |",
        "| Session 11 quiz / Domain 3 checkpoint |  | — | — | — |  |",
        "| Final readiness set (S12) |  |  |  |  |  |",
        "| Official practice assessment, attempt 1 |  |  |  |  |  |",
        "| Official practice assessment, attempt 2 |  |  |  |  |  |",
        "",
        "**Book the exam when:** 85% or better on the final readiness set *and* on a separate",
        "attempt at the official practice assessment, no domain below 75%, and nothing on this",
        "checklist marked B.",
        "",
        "**Exam booked for:** day ____ of the 10-day window &nbsp;&nbsp; "
        '**Confirmation number:** <span class="blank"></span>',
        "",
    ]

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text("\n".join(lines))
    print(f"{OUT} — {len(rows)} objectives")


if __name__ == "__main__":
    main()
