# How to Administer the Quizzes

Four ways to deliver this bank, from zero setup to full LMS. Pick one and stay with it —
switching mid-course costs you more class time than any of them saves.

Everything below is already generated; you never retype an item. Run
`python3 tools/export-quizzes.py` and you get printable handouts, a CSV of all 199 items,
and LMS import files.

## Choose your delivery method

| Method | Setup for you | What learners need | Auto-graded | Best when |
| --- | --- | --- | --- | --- |
| **Paper** | Print the handout | Nothing | No, but you review in class anyway | In-person classes, low-tech rooms, or the first cohort |
| **Microsoft Forms** | 15–20 min per quiz, once | A browser and the link | Yes | You have a Microsoft 365 account, which fits an Azure course |
| **Google Forms** | 15–20 min per quiz, once | A browser and the link | Yes | Your organization runs on Google Workspace |
| **LMS import (Moodle, Canvas, Blackboard)** | 5 min per quiz using the GIFT files | Their existing LMS login | Yes, with per-objective reporting | You already run a gradebook |

All four end the same way: **you review every item in class immediately after the quiz.**
That review is where the learning happens. Auto-grading saves your evenings; it does not
replace the review.

---

## Option 1 — Paper

1. Run `python3 tools/export-quizzes.py`.
2. Print `handouts/<quiz>-handout.md`, or the PDF of it, one per learner. Each handout has a name line, the instructions, the questions, and an answer grid on its own page.
3. Keep the matching quiz file in `quizzes/` open on your screen — the answer key is the second half of it.
4. After collecting the sheets, read the answers aloud and work through the rationale for each. Learners mark their own sheet and record missed objective IDs on their objective checklist.

**What learners need:** nothing but a pen.

---

## Option 2 — Microsoft Forms

Natural fit for this course, and free with any Microsoft account.

**Set up one quiz (do this once per quiz, before you need it):**

1. Go to [forms.office.com](https://forms.office.com) and create a **New Quiz**.
2. Title it to match the file, for example "AZ-900 Session 3 Quiz".
3. Open `exports/item-bank.csv` and filter to that quiz. For each row, add a question:
   - `type = single` → **Choice**, single answer
   - `type = multi-select` → **Choice**, turn on **Multiple answers**
   - `type = matching` → **Choice** per numeral (one question per row of the match), or a **Ranking** question if your tenant has it
   - `type = yes-no` → **Choice** with Yes and No, one question per statement
   - `type = ordering` → **Ranking**
4. Paste the stem, paste the options, then click the tick beside each correct option to mark it. Set points to 1 per question.
5. Paste the rationale from the CSV into the question's **Message** field so learners see *why* when they review their result. This is the highest-value 30 seconds per item you can spend.
6. Under **Settings**, turn on **Show results automatically** so learners see their score and the rationale as soon as they submit.
7. Under **Collect responses**, copy the link. Keep all 14 links in one document you can paste from each session.

**Run it in class:** paste the link in chat or show a QR code. Learners open it, answer,
submit, and see their score. You watch the live response summary, which shows you the
per-question failure rate in real time — use that to decide which items to spend review
time on.

**After class:** export responses to Excel. The per-question breakdown tells you which
objectives to weight in the next warm-up.

**What learners need:** a browser. Sign-in is optional — turn on "Anyone can respond" for
anonymous quizzes, or restrict to your organization if you want names attached to scores.

---

## Option 3 — Google Forms

Same shape as Microsoft Forms.

1. Create a form, then **Settings → Make this a quiz**.
2. Add questions from `exports/item-bank.csv`: **Multiple choice** for single-answer items, **Checkboxes** for select-all-that-apply, **Multiple choice grid** for matching and yes/no sets.
3. For each question use **Answer key** to mark the correct option, set 1 point, and paste the rationale into **Add answer feedback**.
4. In Settings, set **Release grade: immediately after each submission**.
5. Share the link. Responses land in a Google Sheet, and the **Insights** view gives you the per-question failure rate.

**What learners need:** a browser. A Google account is only needed if you require sign-in.

---

## Option 4 — LMS import (recommended if you have one)

`exports/gift/` holds one GIFT file per quiz. GIFT is Moodle's native text import format,
and several other tools read it. **198 of the 199 items convert automatically**; the single
ordering item needs manual entry (see `exports/import-report.md`).

**Moodle:**

1. Course → **Question bank → Import**.
2. Choose **GIFT format**, upload `exports/gift/session-03-quiz.txt`, import.
3. Create a Quiz activity, add the imported questions, set the time limit from the quiz file's header, and allow one attempt.
4. Repeat per quiz. Consider one question category per quiz so your question bank stays navigable.

**Canvas, Blackboard, and others:** most accept QTI rather than GIFT. Either convert GIFT
to QTI with a free converter, or use the CSV with your LMS's own bulk-import format. Canvas
also has a "New Quizzes" CSV importer that takes stem, options, and answer columns directly
from `exports/item-bank.csv`.

**Why GIFT is worth it:** each question carries a `// objectives: 2.1.4` comment. Keep those
and you can report scores by exam objective, which is exactly what the checkpoints are for.

**What learners need:** their normal LMS login.

---

## Warm-ups are different — do not put them in a tool

The 66 warm-up prompts in [`warm-ups.md`](./warm-ups.md) are **free recall**: no options to
choose from. Turning them into multiple choice destroys their value, because recognizing an
answer is far easier than producing one.

Run them out loud. Ask the question, wait — count to five silently, it feels much longer
than it is — then call on someone or take a chorus answer. Alternatively use a Teams or
Zoom poll with a text-entry question, or have learners write answers on paper they keep.

Never grade them. The moment a warm-up is graded, learners stop guessing out loud, and you
lose your view into what they actually know.

---

## Timing in the session

| Block | Minutes | Notes |
| --- | --- | --- |
| Hand out or share link | 1 | Have it ready before the session; do not set it up live |
| Learners answer | 10–12 | 15-minute quizzes are 12 items; a minute per item is right for beginners |
| Review every item | Remaining wrap-up time | Name the objective ID for each miss |

If you are short on time, cut **carry-forward items** first — they are marked in each quiz
file. Never cut the new-session items; those are the only assessment that objective gets
before its domain checkpoint.

## The review script that makes this work

For each item, in this order:

1. Ask who chose each option before revealing anything. Hands or poll.
2. Say the correct answer and **why the most popular wrong answer is wrong** — that is the sentence that changes someone's mental model.
3. Say the objective ID out loud: "that's 2.2.6, public and private endpoints."
4. Learners mark that objective on their checklist: confident, shaky, or blank.

Four steps, about 45 seconds per item.

## Tracking results

Use [`results-tracker.csv`](./results-tracker.csv). One row per objective, one column per
instrument; record how many learners missed each objective. Three decisions depend on it:

- Which objectives lead the next session's warm-up.
- Which two areas get re-taught in the Session 11 cumulative block.
- Which three objectives become the Session 12 gap clinic.

If you only track total scores, you cannot make any of those decisions, and Sessions 11 and
12 turn into generic review.

## What to give learners, and when

| When | Give them | From |
| --- | --- | --- |
| Before Session 1 | Syllabus, objective checklist | `syllabus/course-syllabus.pdf`, `handouts/objective-checklist.md` |
| Each session | The quiz, however you deliver it | `handouts/` or your quiz tool |
| After each quiz review | The answer key with rationale and Microsoft Learn links | The second half of each `quizzes/*.md` file |
| Session 11 | The official practice assessment link as homework | [AZ-900 practice assessment](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-900/practice/assessment?assessment-type=practice&assessmentId=23) |
| Session 12 | Final readiness set, then the 10-day plan | `quizzes/final-readiness-set.md`, syllabus |

Give learners the answer keys. These are teaching items written against published
objectives, not secured exam content, and the rationale plus source link is the best
revision material in the course. Withholding keys to preserve item secrecy would cost more
than it protects.

## One thing to tell learners in Session 1

Say this plainly: **the quizzes are not there to grade you, they are there to find gaps
while there is still time to fix them.** Learners who believe a quiz is a judgment hide
their confusion; learners who believe it is a diagnostic tell you what they do not
understand. The second group passes.

## Regenerating everything

```bash
python3 tools/export-quizzes.py     # handouts, item-bank.csv, GIFT files, import report
python3 tools/build-checklist.py    # learner objective checklist
bash tools/build-all-pdfs.sh        # syllabus, checklist, and handout PDFs
```

Re-run all three after editing any quiz or the objective map.
