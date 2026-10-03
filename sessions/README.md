# Session materials — slides and instructor notes

Phase 3. One slide deck and one set of instructor notes for each of the 12 sessions.
Teach from the notes. Project or print the slides. The minute budgets match
[`../curriculum/six-week-plan.md`](../curriculum/six-week-plan.md).

| Session | Slides | Instructor notes |
| --- | --- | --- |
| 1 Cloud Computing Foundations | [slides](session-01-slides.md) | [notes](session-01-instructor-notes.md) |
| 2 Benefits, pricing, IaaS/PaaS/SaaS | [slides](session-02-slides.md) | [notes](session-02-instructor-notes.md) |
| 3 Azure Architecture | [slides](session-03-slides.md) | [notes](session-03-instructor-notes.md) |
| 4 Azure Compute | [slides](session-04-slides.md) | [notes](session-04-instructor-notes.md) |
| 5 Azure Networking | [slides](session-05-slides.md) | [notes](session-05-instructor-notes.md) |
| 6 Azure Storage | [slides](session-06-slides.md) | [notes](session-06-instructor-notes.md) |
| 7 Identity, access, and security | [slides](session-07-slides.md) | [notes](session-07-instructor-notes.md) |
| 8 Cost management | [slides](session-08-slides.md) | [notes](session-08-instructor-notes.md) |
| 9 Governance and compliance | [slides](session-09-slides.md) | [notes](session-09-instructor-notes.md) |
| 10 Managing and deploying resources | [slides](session-10-slides.md) | [notes](session-10-instructor-notes.md) |
| 11 Monitoring and cumulative review | [slides](session-11-slides.md) | [notes](session-11-instructor-notes.md) |
| 12 Exam readiness | [slides](session-12-slides.md) | [notes](session-12-instructor-notes.md) |

Labs for the practice block are in [`../labs/`](../labs/). Quizzes are already written in
[`../quizzes/`](../quizzes/).

## How a slide heading works

Each `##` heading in a slide file is one slide. Bullets are what learners should see,
not a script. Say the talk track from the instructor notes. Acronyms are expanded on
the slide where they first appear in that session.

## How to prep

Budget 60–90 minutes, as the course overview says.

1. Read the instructor notes for that session, including the "if you are short on time" cut.
2. Skim the official module linked at the bottom of the notes. Microsoft Learn wins if a note and the module disagree.
3. Rehearse the lab in [`../labs/`](../labs/) on the same kind of account learners will use.
4. Print the quiz handout, or have the Forms/LMS quiz open. See [`../quizzes/administration-guide.md`](../quizzes/administration-guide.md).
5. Print the objective checklist if learners do not already have it.

## This cohort

The first meeting was an introduction and a practice assessment, not the Session 1
lecture. Do not reteach Session 1 as a full 120 minutes inside Session 2. Use the
Session 2 warm-up as the diagnostic, then teach only the Session 1 ideas the room
cannot produce. The recovery script is at the top of
[`session-02-instructor-notes.md`](session-02-instructor-notes.md). Record what you
actually covered in [`../operations/session-log.md`](../operations/session-log.md).

## Print

```bash
bash tools/build-teaching-pdfs.sh
```

That writes a PDF next to each instructor-notes file and each lab. Slide files stay
Markdown so you can project them.
