# AZ-900 Curriculum — 6 Weeks, 12 Sessions

A complete instructional plan for teaching **Exam AZ-900: Microsoft Azure Fundamentals**
to adult beginners in six weeks, built strictly against current Microsoft Learn material.

- 6 weeks, 2 sessions per week, 12 sessions, 2 hours each — **24 instructional hours**
- Designed so learners sit the exam **within 10 days** after the final session
- No calendar dates anywhere: sessions and the post-course plan use relative numbering
- All **57 current exam objectives** mapped to where they are taught, practiced, quizzed, and cumulatively reviewed

**This repository is Phase 1 only: the curriculum map.** Quizzes, slides, labs, and
handouts are later phases. See [Status](#status) below.

## Contents

| File | What it is |
| --- | --- |
| [`curriculum/course-overview.md`](curriculum/course-overview.md) | Audience, prerequisites, outcomes, exam snapshot, instructional model, assessment strategy, hands-on environment options, the 10-day post-course readiness plan, instructor prep, accessibility, risks |
| [`curriculum/six-week-plan.md`](curriculum/six-week-plan.md) | All 12 sessions, block by block, with minute budgets, practice activities, quiz scope, assignments, and source links per session |
| [`curriculum/exam-objective-map.md`](curriculum/exam-objective-map.md) | All 57 objectives with taught / practiced / quizzed / cumulatively-reviewed columns, coverage totals, time-versus-weight analysis, and the gap list |
| [`quizzes/`](quizzes/) | The full assessment bank: warm-ups, 11 session quizzes, 2 domain checkpoints, and the timed final readiness set — 197 scored items plus 66 retrieval prompts, with answer keys, objective IDs, and sources. Start at [`quizzes/README.md`](quizzes/README.md) |
| [`sources/microsoft-learn-links.md`](sources/microsoft-learn-links.md) | Every primary source, learning path, module, guided project, verified unit, and per-objective Azure documentation link |
| [`sources/source-validation-log.md`](sources/source-validation-log.md) | What was verified and how, conflicts with secondary sources, outdated terminology, NEEDS VERIFICATION items, and the re-validation procedure |

## Exam snapshot

Verified against Microsoft Learn, skills measured **as of July 20, 2026**.

| Domain | Weight |
| --- | --- |
| Describe cloud concepts | 25–30% |
| Describe Azure architecture and services | 35–40% |
| Describe Azure management and governance | 30–35% |

Passing score is **700 or greater**. Fundamentals exams allow **45 minutes** of exam time
within a **65-minute** seat time, are proctored, and — unlike role-based exams — do **not**
provide access to Microsoft Learn during the exam. Fundamentals certifications do not
expire. Sources for each of these facts are in
[`sources/microsoft-learn-links.md`](sources/microsoft-learn-links.md).

## Course shape

| Week | Session | Topic |
| --- | --- | --- |
| 1 | 1 | Cloud Computing Foundations |
| 1 | 2 | Cloud Benefits, Pricing Models, and IaaS/PaaS/SaaS |
| 2 | 3 | Azure Architecture |
| 2 | 4 | Azure Compute |
| 3 | 5 | Azure Networking |
| 3 | 6 | Azure Storage |
| 4 | 7 | Azure Identity, Access, and Security |
| 4 | 8 | Azure Cost Management |
| 5 | 9 | Governance and Compliance |
| 5 | 10 | Managing and Deploying Azure Resources |
| 6 | 11 | Monitoring + Cumulative Review |
| 6 | 12 | Full AZ-900 Exam Readiness |

Every session runs the same shape: a 10-minute cumulative warm-up, two or three teaching
blocks, 30 minutes of practice, and a 15-minute formative quiz — mostly on that session's
objectives, plus a carry-forward block from earlier sessions whose range widens as the
course proceeds. Domain checkpoints land at the start of Session 3 (Domain 1), the start of
Session 8 (Domain 2), and inside the Session 11 quiz (Domain 3). Session 12 is a timed
45-item readiness pass plus a debrief and gap clinic.

Instructional time is allocated to match the published exam weights: 28.1% Domain 1,
38.9% Domain 2, 33.0% Domain 3 of the 1,440 total minutes.

## Source of truth

**Primary — Microsoft Learn always wins.**

1. [Microsoft Certified: Azure Fundamentals](https://learn.microsoft.com/en-us/credentials/certifications/azure-fundamentals/?practice-assessment-type=certification)
2. [Study guide for Exam AZ-900](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900)
3. [Course AZ-900T00-A: Introduction to Cloud Infrastructure](https://learn.microsoft.com/en-us/training/courses/az-900t00)

**Secondary — cross-check only, not teaching sources.**

- [AzureMentor/Azure-AZ-900-Study-Guide](https://github.com/AzureMentor/Azure-AZ-900-Study-Guide)
- [johnthebrit/AZ900CertCourse](https://github.com/johnthebrit/AZ900CertCourse)

Both secondary references were last updated before the July 20, 2026 skills revision, so
neither is treated as current. Neither was cloned, and no content from either was copied.
Every disagreement is recorded in
[`sources/source-validation-log.md`](sources/source-validation-log.md).

### Content rules

- Microsoft Learn wins over any other source, always.
- No verbatim copying from any source.
- No exam dumps, brain dumps, or "real exam questions." The only practice instrument referenced is Microsoft's official free practice assessment.
- No invented Azure facts. Anything unverifiable in current Microsoft documentation is labeled **NEEDS VERIFICATION** instead of asserted.
- Current product names only. The outdated-terminology reference table is in the validation log.
- Source links are provided for every major topic, using canonical `learn.microsoft.com` URLs rather than link shorteners.

## How to use this repository

**Program leads:** read [`curriculum/course-overview.md`](curriculum/course-overview.md)
first. It defines the audience, the assessment strategy, the hands-on environment options
including a no-cost path, and the 10-day post-course exam plan.

**Instructors:** teach from [`curriculum/six-week-plan.md`](curriculum/six-week-plan.md).
Each session lists its objectives, minute-by-minute blocks, practice activity with a
no-cost fallback, quiz scope, assignment, and source links. Before each cohort, run the
re-validation procedure at the end of
[`sources/source-validation-log.md`](sources/source-validation-log.md).

**Content authors (Phase 2 onward):** build against
[`curriculum/exam-objective-map.md`](curriculum/exam-objective-map.md). Objective IDs such
as `2.2.5` are stable handles for quiz items, slides, and lab instructions. The gap list
in that file names the places where learners predictably need more than the official
modules provide.

Objective IDs are local to this repository. Microsoft does not publish objective numbers;
these IDs exist to make coverage traceable.

## Coverage at a glance

| Domain | Objectives | Taught | Practiced | Quizzed | Reviewed cumulatively |
| --- | --- | --- | --- | --- | --- |
| Describe cloud concepts | 15 | 15 | 15 | 15 | 15 |
| Describe Azure architecture and services | 27 | 27 | 27 | 27 | 27 |
| Describe Azure management and governance | 15 | 15 | 15 | 15 | 15 |
| **Total** | **57** | **57** | **57** | **57** | **57** |

Assessment coverage is verified the same way: every objective appears in at least one
session quiz, in the checkpoint for its domain, and in the final readiness set. See
[`quizzes/coverage-matrix.md`](quizzes/coverage-matrix.md), which is generated from the
answer keys rather than maintained by hand.

## Status

**Phase 1 — complete.** Objective verification, source validation, and the curriculum map.

**Phase 2 — complete.** The assessment bank: 66 warm-up retrieval prompts, 11 session
quizzes with progressive carry-forward, 2 domain checkpoints, and a timed 45-item final
readiness set. 197 scored items, all objective-mapped and Microsoft Learn sourced.

Not yet built:

- Phase 3 — session materials: slides, instructor notes, learner handouts, objective checklists
- Phase 4 — lab guides: step-by-step versions of each session's practice activity, with no-cost variants
- Phase 5 — cohort operations: enrollment communications, readiness tracking, exam-scheduling support

## License and attribution

This curriculum is original instructional design. It references Microsoft Learn content by
link and paraphrase only; no Microsoft content is reproduced here. Microsoft, Azure, and
Microsoft Entra are trademarks of Microsoft Corporation. All Microsoft Learn content
remains subject to Microsoft's terms.
