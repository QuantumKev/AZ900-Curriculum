#!/usr/bin/env python3
"""Turn the Markdown quiz files into things you can hand out or import.

Usage:
    python3 tools/export-quizzes.py

Reads every quiz in quizzes/ and writes:

    handouts/<quiz>-handout.md   questions only, with a name/date header and
                                 an answer grid, ready to print
    exports/item-bank.csv        one row per item: type, stem, options, answer,
                                 objective IDs, source link
    exports/gift/<quiz>.txt      GIFT format for LMS import (Moodle, and other
                                 tools that read GIFT)
    exports/import-report.md     what converted cleanly and what needs manual
                                 entry

Nothing here is authored by hand; re-run it after editing any quiz file.
"""

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QUIZ_DIR = ROOT / "quizzes"
HANDOUT_DIR = ROOT / "handouts"
EXPORT_DIR = ROOT / "exports"
GIFT_DIR = EXPORT_DIR / "gift"

SKIP = {"README.md", "coverage-matrix.md", "administration-guide.md", "warm-ups.md"}

TITLE_RE = re.compile(r"^# (.+)$", re.M)
ITEM_RE = re.compile(r"^\*\*(\d+)\.\*\*[ ]?(.*)$", re.M)
CHOICE_RE = re.compile(r"^- ([A-E])\. (.+)$")
PART_RE = re.compile(r"^- ([ivx]+)\. (.+)$")
KEY_ROW_RE = re.compile(r"^\| (\d+) \| ([^|]*) \| ([^|]*) \| ([^|]*) \| ([^|]*) \|", re.M)


def classify(stem: str, has_choices: bool, has_parts: bool) -> str:
    low = stem.lower()
    if has_parts and "yes or no" in low:
        return "yes-no"
    if has_parts:
        return "matching"
    # The ordering convention is a parenthetical instruction, e.g.
    # "(Put these Azure scopes in order ...)". Plain prose such as "which two
    # options fit, in order?" is still a single-answer item.
    if re.search(r"\(put [^)]*in order", low):
        return "ordering"
    if "select all that apply" in low:
        return "multi-select"
    if has_choices:
        return "single"
    return "unknown"


def parse_quiz(path: Path) -> dict:
    text = path.read_text()
    title_match = TITLE_RE.search(text)
    title = title_match.group(1) if title_match else path.stem
    if "## Answer key" not in text:
        return {}
    questions_half, key_half = text.split("## Answer key", 1)
    header = questions_half.split("## Questions", 1)[0]
    body = questions_half.split("## Questions", 1)[-1]

    keys = {
        num: {
            "answer": answer.strip(),
            "objectives": re.findall(r"\d\.\d\.\d", objectives),
            "why": why.strip(),
            "source": source.strip(),
        }
        for num, answer, objectives, why, source in KEY_ROW_RE.findall(key_half)
    }

    items = []
    matches = list(ITEM_RE.finditer(body))
    for index, match in enumerate(matches):
        number = match.group(1)
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        block = body[match.start():end]
        stem_lines, choices, parts = [match.group(2).strip()], [], []
        for line in block.splitlines()[1:]:
            stripped = line.strip()
            choice = CHOICE_RE.match(stripped)
            part = PART_RE.match(stripped)
            if choice:
                choices.append((choice.group(1), choice.group(2).strip()))
            elif part:
                parts.append((part.group(1), part.group(2).strip()))
            elif stripped and not stripped.startswith(("---", "|", "**Instructor", "**Objectives", "**Scoring", "**On the", "**Note", "> ")):
                stem_lines.append(stripped)
        stem = " ".join(s for s in stem_lines if s).strip()
        carry = bool(re.search(r"\*\((Carry-forward|Mixed review|Domain 3 checkpoint)", stem))
        stem = re.sub(r"\*\((Carry-forward|Mixed review)\)\*\s*", "", stem).strip()
        items.append(
            {
                "quiz": path.stem,
                "quiz_title": title,
                "number": number,
                "stem": stem,
                "choices": choices,
                "parts": parts,
                "type": classify(stem, bool(choices), bool(parts)),
                "carry_forward": carry,
                **keys.get(number, {"answer": "", "objectives": [], "why": "", "source": ""}),
            }
        )
    return {"title": title, "header": header, "items": items, "path": path}


def strip_links(text: str) -> str:
    return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)


def write_handout(quiz: dict) -> Path:
    items = quiz["items"]
    meta = {}
    for field in ("Time", "Items", "Composition", "Target"):
        found = re.search(rf"\*\*{field}:\*\* ([^·\n]+)", quiz["header"])
        if found:
            meta[field] = found.group(1).strip()

    lines = [
        f"# {quiz['title']}",
        "",
        '**Name:** <span class="blank"></span>  **Session:** <span class="blank"></span>',
        "",
    ]
    facts = " · ".join(f"**{k}:** {v}" for k, v in meta.items() if k in ("Time", "Items", "Target"))
    if facts:
        lines += [facts, ""]
    lines += [
        "Answer every question. For *select all that apply*, mark every correct option. For",
        "matching questions, write the matching term next to each numeral. For yes/no sets,",
        "write yes or no next to each numeral. Your instructor reviews every answer in class",
        "immediately afterward.",
        "",
        "---",
        "",
    ]
    for item in items:
        lines.append(f"**{item['number']}.** {strip_links(item['stem'])}")
        lines.append("")
        for letter, option in item["choices"]:
            lines.append(f"- {letter}. {strip_links(option)}")
        for numeral, part in item["parts"]:
            lines.append(f"- {numeral}. {strip_links(part)} &nbsp; <span class=\"blank\"></span>")
        lines.append("")
    lines += ["<!-- pagebreak -->", "", "## Answer sheet", "", "| # | Your answer | # | Your answer |", "| --- | --- | --- | --- |"]
    half = (len(items) + 1) // 2
    for i in range(half):
        left = items[i]["number"]
        right = items[i + half]["number"] if i + half < len(items) else ""
        lines.append(f"| {left} |  | {right} |  |")
    lines += ["", "**Score:** ____ / " + str(len(items)), "", "**Objectives to review:** <span class=\"blank blank-wide\"></span>", ""]

    HANDOUT_DIR.mkdir(exist_ok=True)
    out = HANDOUT_DIR / f"{quiz['path'].stem}-handout.md"
    out.write_text("\n".join(lines))
    return out


def gift_escape(text: str) -> str:
    text = strip_links(text)
    for char in ("~", "=", "#", "{", "}", ":"):
        text = text.replace(char, "\\" + char)
    return text.replace("*", "")


def write_gift(quiz: dict) -> tuple[Path, list[str]]:
    lines, manual = [], []
    tag = quiz["path"].stem.replace("session-", "S").replace("-quiz", "")
    for item in quiz["items"]:
        name = f"{tag}-Q{item['number']}"
        stem = gift_escape(item["stem"])
        objective = ", ".join(item["objectives"])
        lines.append(f"// objectives: {objective}")
        if item["type"] == "single":
            correct = item["answer"].strip()
            options = []
            for letter, option in item["choices"]:
                marker = "=" if letter == correct else "~"
                options.append(f"    {marker}{gift_escape(option)}")
            lines.append(f"::{name}:: {stem} {{\n" + "\n".join(options) + "\n}\n")
        elif item["type"] == "multi-select":
            correct = {c.strip() for c in item["answer"].split(",")}
            share = round(100 / max(len(correct), 1), 5)
            options = []
            for letter, option in item["choices"]:
                if letter in correct:
                    options.append(f"    ~%{share}%{gift_escape(option)}")
                else:
                    options.append(f"    ~%-100%{gift_escape(option)}")
            lines.append(f"::{name}:: {stem} {{\n" + "\n".join(options) + "\n}\n")
        elif item["type"] == "matching":
            pairs = dict(
                re.findall(r"([ivx]+)[–-]\s*([^,]+)", item["answer"])
            )
            rows = []
            for numeral, part in item["parts"]:
                answer = pairs.get(numeral, "").strip()
                if not answer:
                    manual.append(f"{name} (matching: could not read pair {numeral})")
                    continue
                rows.append(f"    ={gift_escape(part)} -> {gift_escape(answer)}")
            if rows:
                lines.append(f"::{name}:: {stem} {{\n" + "\n".join(rows) + "\n}\n")
        elif item["type"] == "yes-no":
            verdicts = dict(re.findall(r"([ivx]+)[–-]\s*(yes|no)", item["answer"], re.I))
            for numeral, part in item["parts"]:
                verdict = verdicts.get(numeral, "").lower()
                if verdict not in ("yes", "no"):
                    manual.append(f"{name}{numeral} (yes/no: could not read verdict)")
                    continue
                flag = "T" if verdict == "yes" else "F"
                lines.append(f"::{name}{numeral}:: {gift_escape(part)} {{{flag}}}\n")
        else:
            manual.append(f"{name} ({item['type']}: no GIFT equivalent, enter manually)")
            lines.append(f"// MANUAL ENTRY NEEDED: {name} ({item['type']})\n")

    GIFT_DIR.mkdir(parents=True, exist_ok=True)
    out = GIFT_DIR / f"{quiz['path'].stem}.txt"
    out.write_text(
        f"// {quiz['title']}\n"
        f"// Generated from quizzes/{quiz['path'].name} by tools/export-quizzes.py\n"
        "// GIFT format. Import into Moodle: Question bank > Import > GIFT format.\n\n"
        + "\n".join(lines)
    )
    return out, manual


def main() -> None:
    quizzes = []
    for path in sorted(QUIZ_DIR.glob("*.md")):
        if path.name in SKIP:
            continue
        quiz = parse_quiz(path)
        if quiz:
            quizzes.append(quiz)

    EXPORT_DIR.mkdir(exist_ok=True)
    rows, manual_all, counts = [], [], {}
    for quiz in quizzes:
        write_handout(quiz)
        _, manual = write_gift(quiz)
        manual_all += manual
        for item in quiz["items"]:
            counts[item["type"]] = counts.get(item["type"], 0) + 1
            rows.append(
                {
                    "quiz": quiz["path"].stem,
                    "item": item["number"],
                    "type": item["type"],
                    "carry_forward": "yes" if item["carry_forward"] else "no",
                    "objectives": " ".join(item["objectives"]),
                    "stem": strip_links(item["stem"]),
                    "options": " | ".join(
                        f"{k}. {strip_links(v)}" for k, v in (item["choices"] or item["parts"])
                    ),
                    "answer": item["answer"],
                    "rationale": strip_links(item["why"]),
                    "source": re.findall(r"\((https?://[^)]+)\)", item["source"]) [:1] and re.findall(r"\((https?://[^)]+)\)", item["source"])[0] or "",
                }
            )

    with (EXPORT_DIR / "item-bank.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "quiz", "item", "type", "carry_forward", "objectives",
                "stem", "options", "answer", "rationale", "source",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    report = [
        "# Import Report (generated)",
        "",
        f"Generated by `tools/export-quizzes.py` from {len(quizzes)} quiz files.",
        "",
        f"- **{len(rows)} items** exported to `item-bank.csv`",
        f"- GIFT files written to `gift/` — one per quiz",
        f"- Printable handouts written to `../handouts/`",
        "",
        "## Items by type",
        "",
        "| Type | Items | GIFT support |",
        "| --- | --- | --- |",
    ]
    support = {
        "single": "Yes — multiple choice",
        "multi-select": "Yes — multiple response with partial credit",
        "matching": "Yes — matching",
        "yes-no": "Yes — split into one true/false question per statement",
        "ordering": "No — enter manually",
        "unknown": "No — check the source file",
    }
    for kind, count in sorted(counts.items(), key=lambda pair: -pair[1]):
        report.append(f"| {kind} | {count} | {support.get(kind, '?')} |")
    report += ["", "## Needs manual entry", ""]
    report += [f"- {entry}" for entry in manual_all] or ["- Nothing; every item converted."]
    report += [
        "",
        "## Notes",
        "",
        "- Yes/no sets become individual true/false questions, so an LMS item count will be higher than the paper item count. Weight them so the set is worth one point in total.",
        "- Matching items export with the pairs intact, but check the shuffled answer list after import; some tools add the answers as distractors automatically.",
        "- GIFT carries no images, and none of these items need any.",
        "- The `// objectives:` comment above each question preserves the objective IDs. Moodle keeps comments on import, which is what lets you report by objective later.",
        "",
    ]
    (EXPORT_DIR / "import-report.md").write_text("\n".join(report))

    print(f"quizzes parsed: {len(quizzes)}")
    print(f"items exported: {len(rows)}")
    print("by type:", dict(sorted(counts.items())))
    print(f"manual entry needed: {len(manual_all)}")
    for entry in manual_all:
        print("  -", entry)


if __name__ == "__main__":
    main()
