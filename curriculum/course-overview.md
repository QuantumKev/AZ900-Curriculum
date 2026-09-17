# Course Overview — AZ-900 in 6 Weeks

A 12-session, 24-hour instructor-led course that takes an adult beginner from no cloud
background to sitting Exam AZ-900 within 10 days of the final session.

## Format

| Attribute | Value |
| --- | --- |
| Duration | 6 weeks |
| Sessions per week | 2 |
| Total sessions | 12 |
| Session length | 2 hours (120 minutes) |
| Total instructional hours | 24 |
| Delivery | Instructor-led; works in person, remote, or hybrid |
| Exam target | Within 10 days after the final session |
| Scheduling | Relative session numbers only — no calendar dates anywhere in this curriculum |

Twenty-four hours matches the duration Microsoft publishes for the official
[AZ-900T00-A: Introduction to Cloud Infrastructure](https://learn.microsoft.com/en-us/training/courses/az-900t00)
course in the Microsoft Learn catalog. The course page itself displays "1 day" as the
course duration, which conflicts with the catalog figure — see
[`../sources/source-validation-log.md`](../sources/source-validation-log.md), item **V8**.

## Audience

Adult beginners. Specifically:

- Career changers moving toward an IT or cloud role
- Help desk, desktop support, or operations staff with no Azure exposure
- Developers, analysts, or database staff who need Azure vocabulary
- Non-technical staff in technical organizations who need to follow cloud conversations

Microsoft's audience profile for this certification expects "skills and experience working
with an area of IT, such as infrastructure management, database management, or software
development." This course does not assume that experience, so Sessions 1 and 2 build the
vocabulary the profile takes for granted.

### Prerequisites

There are no formal prerequisites for AZ-900. For this course learners need:

- Comfort using a web browser and following multi-step instructions
- Basic familiarity with IT terms such as server, network, and database (built up in Session 1 if absent)
- An email address that can be used for a Microsoft Learn account
- Optionally, the ability to create an Azure account for hands-on work (a no-cost path is provided if not)

## Outcomes

By the end of Session 12, a learner who has completed the assigned work can:

1. Explain cloud computing, the shared responsibility model, cloud deployment models, and cloud service types, and pick the appropriate model for a described scenario.
2. Describe Azure's physical and management infrastructure and place any resource correctly in the management group, subscription, resource group, resource hierarchy.
3. Compare Azure compute, networking, and storage options and select a reasonable service for a stated requirement.
4. Describe Azure identity, access, and security capabilities, including Microsoft Entra ID, authentication methods, Conditional Access, Azure RBAC, Zero Trust, defense in depth, and Microsoft Defender for Cloud.
5. Describe how Azure costs arise, estimate them with the pricing calculator, and describe the governance, deployment, and monitoring tools Azure provides.
6. Answer AZ-900-style questions across all three exam domains at a level that supports a passing score of 700 or greater.

## Exam snapshot

| Item | Value | Source |
| --- | --- | --- |
| Exam | AZ-900: Microsoft Azure Fundamentals | [Exam page](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-900/) |
| Certification | Microsoft Certified: Azure Fundamentals | [Certification page](https://learn.microsoft.com/en-us/credentials/certifications/azure-fundamentals/) |
| Skills measured as of | July 20, 2026 | [Study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900) |
| Domain 1 | Describe cloud concepts — 25–30% | Study guide |
| Domain 2 | Describe Azure architecture and services — 35–40% | Study guide |
| Domain 3 | Describe Azure management and governance — 30–35% | Study guide |
| Passing score | 700 or greater | [Exam scoring and score reports](https://learn.microsoft.com/en-us/credentials/certifications/exam-scoring-reports) |
| Exam duration | 45 minutes (Fundamentals exams) | [Exam duration and exam experience](https://learn.microsoft.com/en-us/credentials/support/exam-duration-exam-experience) |
| Seat time | 65 minutes (Fundamentals exams) | Exam duration page |
| Question count | Most Microsoft exams contain 40–60 questions; no AZ-900-specific count is published — **NEEDS VERIFICATION** | Exam duration page |
| Delivery | Proctored; may contain interactive components | Certification page |
| Microsoft Learn during exam | Not available on Fundamentals exams | Exam duration page |
| Retake | Allowed 24 hours after a first failed attempt; longer waits for later retakes | [Retake policy](https://learn.microsoft.com/en-us/credentials/support/retake-policy) |
| Expiry | Fundamentals certifications do not expire | [Certification renewal](https://learn.microsoft.com/en-us/credentials/certifications/renew-your-microsoft-certification) |
| Scheduling | Pearson VUE, or Certiport for students and educators | Certification page |
| Accommodations | Requestable before registration | [Request accommodations](https://learn.microsoft.com/en-us/credentials/certifications/request-accommodations) |
| Free practice assessment | Yes | [AZ-900 practice assessment](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-900/practice/assessment?assessment-type=practice&assessmentId=23) |
| Exam interface demo | Exam sandbox | [aka.ms/examdemo](https://aka.ms/examdemo) |

Two exam facts are worth stating to learners early, because both contradict widespread
assumptions: Fundamentals exams give you 45 minutes of exam time (65 minutes of seat
time), and unlike role-based exams they do **not** give you access to Microsoft Learn
during the exam.

## Instructional model

Each objective moves through four states, and the objective map records where each state
happens for all 57 objectives.

1. **Taught** — first-pass direct instruction with a worked example.
2. **Practiced** — the learner does something: portal or CLI task, guided project, calculator estimate, or a structured sorting/scenario exercise.
3. **Quizzed** — the end-of-session formative quiz covers that session's objectives, with immediate review.
4. **Reviewed cumulatively** — the objective returns in later warm-ups, a domain checkpoint, and the Session 12 sweep.

Three design choices make this hold up for beginners:

- **Spaced retrieval over re-reading.** Every session opens with 10 minutes of retrieval on earlier sessions, on an expanding interval. Nothing is taught once.
- **Concrete before abstract.** Abstract objectives are anchored to something the learner has clicked, priced, or queried. Availability zones are taught before storage redundancy; RBAC before Azure Policy; resource groups before locks and tags.
- **Exam-shaped practice from Session 1.** Sorting and scenario exercises use the same "given a situation, choose the fitting option" structure as exam items, so Session 12 is not the first encounter with that format.

### Time allocation against exam weights

| Domain | Exam weight | Planned minutes of 1,440 | Share |
| --- | --- | --- | --- |
| Describe cloud concepts | 25–30% | 405 | 28.1% |
| Describe Azure architecture and services | 35–40% | 560 | 38.9% |
| Describe Azure management and governance | 30–35% | 475 | 33.0% |

Each domain's share of instructional time falls inside its published exam weight. Domain 1
gets there partly through review rather than lecture: its content is small in volume but
heavily weighted on the exam, so it recurs in warm-ups, gets a scheduled second pass on
pricing models in Session 8, and takes the largest share of Session 12.

## Assessment strategy

Every instrument below is written and ready to use in [`../quizzes/`](../quizzes/):
**199 scored items plus 66 warm-up retrieval prompts**, each traceable to an objective ID
and a Microsoft Learn source. Conventions, carry-forward composition, and scoring rules
are in [`../quizzes/README.md`](../quizzes/README.md); delivery options and the in-class
review script are in
[`../quizzes/administration-guide.md`](../quizzes/administration-guide.md).

| Instrument | When | Length | Scope | Purpose |
| --- | --- | --- | --- | --- |
| [Cumulative warm-up](../quizzes/warm-ups.md) | Start of every session after the first | 10 min, 6 prompts | Prior sessions, expanding interval | Free-recall retrieval practice; ungraded |
| Session quiz | End of every session | 10–15 min, 10–12 items | Mostly that session's objectives, plus a carry-forward block from earlier sessions | Confirm first-pass understanding and keep earlier material live |
| [Domain 1 checkpoint](../quizzes/checkpoint-domain-1.md) | Start of Session 3 | 15 min, 12 items | All 15 Domain 1 objectives | Catch conceptual gaps before Azure services pile on |
| [Domain 2 checkpoint](../quizzes/checkpoint-domain-2.md) | Start of Session 8 | 15 min, 12 items | All 27 Domain 2 objectives | Catch service-recall gaps at the halfway point |
| [Domain 3 checkpoint](../quizzes/session-11-quiz.md) | Inside the Session 11 quiz | 15 min, 12 items | Monitoring in depth, plus a sweep of all of 3.1–3.3 | Close the final domain |
| Cumulative review | Session 11 | 35 min | Domains 1 and 2 | Confidence self-rating against the objective checklist |
| [Final readiness set](../quizzes/final-readiness-set.md) | Session 12, timed | 45 min, 45 items | All 57 objectives, weight-aligned | Readiness signal by domain |
| Official practice assessment | Session 11 homework, then the 10-day window | 45 min | All objectives | Independent readiness reading in Microsoft's own item styles |

**Readiness bar before sitting the exam:** 85% or better overall with no domain below 75%,
on the Session 12 final readiness set *and* on a separate attempt at the official practice
assessment, with no objective marked blank on the objective checklist. Neither instrument
is the exam, and Microsoft publishes no relationship between practice scores and exam
outcomes, so the bar sits deliberately above the 700 passing score.

Two rules keep the assessment honest. Context-only topics — sustainability, encryption and
key management, the Service Trust Portal, AI/ML/IoT services, cost optimization, and
Copilot in Azure — are taught but never scored, because they are not bulleted objectives.
And no item anywhere in this course comes from an exam dump; items are written from
published objectives and official documentation, and the only third-party practice
instrument used is Microsoft's own.

## Hands-on environment

Hands-on work matters for retention, but no learner should be blocked by billing. Three
paths, in order of preference:

1. **Azure free account.** Learners create their own account. Exact current terms —
   included credit, which services are free and for how long — must be confirmed on the
   [Azure free account page](https://azure.microsoft.com/en-us/free/) before the course
   starts. Microsoft Learn describes these terms inconsistently across pages, so treat
   the free-account specifics as **NEEDS VERIFICATION** each time a cohort runs. See
   validation log item **V9**.
2. **Sponsored or organizational subscription** with a spending limit, a budget alert, and
   a resource-group-scoped role assignment per learner.
3. **No-cost path.** Every session in the six-week plan lists a no-cost fallback:
   Microsoft Learn guided projects, the pricing calculator (no sign-in needed), Azure
   Cloud Shell, read-only portal views, and instructor demonstration.

Cost hygiene taught as part of the course, not as an afterthought: tag everything created
in class, use one resource group per session so teardown is a single delete, and delete
lab resources at the end of each session. Sessions 8 and 9 make this explicit by
introducing budgets, tags, and locks.

## Post-course 10-day exam readiness plan

Relative days after the final session. No calendar dates.

| Day | Focus | Work |
| --- | --- | --- |
| 1 | Reset | Review the Session 12 debrief. List every objective marked shaky or blank. Schedule the exam for day 8, 9, or 10 — scheduling it on day 1 is the point. |
| 2 | Domain 1 | Redo the [cloud concepts learning path](https://learn.microsoft.com/en-us/training/paths/microsoft-azure-fundamentals-describe-cloud-concepts/) module assessments. Re-drill shared responsibility, cloud models, service types, pricing models, serverless. |
| 3 | Domain 2, part 1 | Architecture, compute. Re-draw the hierarchy from memory. Re-do the compute comparison table from memory, then check it. |
| 4 | Domain 2, part 2 | Networking, storage. Re-drill VPN vs ExpressRoute vs peering, public vs private vs service endpoints, redundancy options, access tiers. |
| 5 | Domain 2, part 3 | Identity and security. Re-drill Entra ID vs Entra Domain Services, SSO vs MFA vs passwordless, RBAC vs Policy, Zero Trust, defense in depth, Defender for Cloud. |
| 6 | Domain 3 | Cost, governance, management, monitoring. Re-drill Policy vs RBAC vs locks, Advisor vs Service Health vs Monitor, Log Analytics vs alerts vs Application Insights. |
| 7 | Practice | Full official practice assessment, timed. Review every miss against its objective ID. |
| 8 | Targeted repair | Only the objectives missed on day 7. Read the official module unit for each, then re-answer from memory. |
| 9 | Practice and confirm | Second full practice assessment, timed. Confirm the readiness bar. Walk the [exam sandbox](https://aka.ms/examdemo) again so the interface is not new. |
| 10 | Sit the exam | Light review of the objective checklist only. No new material. |

If the readiness bar is not met by day 9, reschedule rather than sit the exam. The retake
wait after a failed attempt is 24 hours for a first retake, but a reschedule costs
nothing but time.

## Course materials for learners

| Item | Give it to them | Source |
| --- | --- | --- |
| Syllabus | Before Session 1 | [`../syllabus/course-syllabus.md`](../syllabus/course-syllabus.md) and its PDF |
| Objective checklist | Session 1, and they keep it all course | [`../handouts/objective-checklist.md`](../handouts/objective-checklist.md) and its PDF |
| Quiz handouts | Each session, if delivering on paper | [`../handouts/`](../handouts/) |
| Answer keys with rationale and sources | After each quiz review | The second half of each file in [`../quizzes/`](../quizzes/) |
| 10-day readiness plan | Session 12 | This document, below |

The syllabus is student-facing and covers what learners must do before Session 1 — create a
free Microsoft Learn account using a personal Microsoft account, and choose between an Azure
free account, a provided subscription, or the no-cost path. It also states plainly that the
course can be completed without ever creating an Azure account.

Rebuild any of these after editing the source files:

```bash
python3 tools/export-quizzes.py     # handouts, item-bank.csv, GIFT exports
python3 tools/build-checklist.py    # objective checklist
bash tools/build-all-pdfs.sh        # every PDF
```

## Instructor preparation

Per session, budget roughly 60–90 minutes of prep:

- Read the official module for the session end to end, including its module assessment.
- Rehearse the practice activity in the same subscription type learners will use, and time it.
- Check the objective map's gap notes for that session — those are the predictable stumbles.
- Re-read the [study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900) change log before each cohort. If the "Skills measured as of" date has moved past July 20, 2026, re-run the validation pass in [`../sources/source-validation-log.md`](../sources/source-validation-log.md) before teaching.

House rules for content accuracy, applied to slides and any handouts:

- Microsoft Learn wins over every other source, always.
- No exam dumps, no memory-dump question banks, no "real exam questions." Practice items come from the official practice assessment or are written against published objectives.
- Current product names only. The outdated-terminology list in the validation log is the reference.
- Anything not verifiable in Microsoft's current documentation is labeled **NEEDS VERIFICATION** rather than stated as fact.

## Accessibility and inclusion

- Every activity has a keyboard-only path; the Azure portal and Cloud Shell both support one.
- Slides and handouts carry text alternatives for diagrams; the hierarchy and defense-in-depth diagrams also exist as indented lists.
- Sorting and scenario exercises work verbally, on paper, or in a shared document.
- Exam accommodations are introduced in Session 1 and again in Session 12, because they must be requested **before** registering.
- Acronyms are expanded on first use in every session, not just the first time in the course. Beginner cohorts lose the thread on unexplained acronyms faster than on unexplained concepts.

## Known risks

| Risk | Mitigation |
| --- | --- |
| Microsoft updates the skills measured mid-cohort | Re-run the validation pass before each cohort; the objective map is keyed to objective IDs so a change touches a small number of rows |
| Learners cannot create Azure accounts | No-cost fallback path listed per session |
| Session 7 carries eight objectives | Guided project exercises most of them together; quiz shortened to 10 minutes to protect practice time |
| Beginners conflate similar Azure services | Discrimination exercises are built into S3, S5, S6, S9, S10, and S11 rather than left to review |
| Ten-day post-course window slips | Exam is scheduled on day 1 of the window, not at the end of it |
| Outdated third-party study material | Conflicts and outdated terms are documented in the validation log and taught explicitly in Session 8 (TCO calculator) and Session 7 (Entra naming) |
