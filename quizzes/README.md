# Quiz Bank — Phase 2

Every assessment instrument for the 12-session course: warm-ups, session quizzes, domain
checkpoints, and the final readiness set. **197 scored items plus 66 warm-up retrieval
prompts**, all traceable to a current AZ-900 objective and a Microsoft Learn source.

Microsoft Learn is the only source for item content. The two GitHub study guides remain
useful as optional learner resources, but no item in this bank is derived from them —
they are cross-checks, not authorities.

## Contents

| Instrument | File | When | Items |
| --- | --- | --- | --- |
| Warm-ups (S2–S12) | [`warm-ups.md`](./warm-ups.md) | First 10 min of each session | 66 prompts |
| Session 1 quiz | [`session-01-quiz.md`](./session-01-quiz.md) | End of S1 | 12 |
| Session 2 quiz | [`session-02-quiz.md`](./session-02-quiz.md) | End of S2 | 12 |
| Domain 1 checkpoint | [`checkpoint-domain-1.md`](./checkpoint-domain-1.md) | Start of S3 | 12 |
| Session 3 quiz | [`session-03-quiz.md`](./session-03-quiz.md) | End of S3 | 12 |
| Session 4 quiz | [`session-04-quiz.md`](./session-04-quiz.md) | End of S4 | 12 |
| Session 5 quiz | [`session-05-quiz.md`](./session-05-quiz.md) | End of S5 | 12 |
| Session 6 quiz | [`session-06-quiz.md`](./session-06-quiz.md) | End of S6 | 12 |
| Session 7 quiz | [`session-07-quiz.md`](./session-07-quiz.md) | End of S7 | 10 |
| Domain 2 checkpoint | [`checkpoint-domain-2.md`](./checkpoint-domain-2.md) | Start of S8 | 12 |
| Session 8 quiz | [`session-08-quiz.md`](./session-08-quiz.md) | End of S8 | 12 |
| Session 9 quiz | [`session-09-quiz.md`](./session-09-quiz.md) | End of S9 | 12 |
| Session 10 quiz | [`session-10-quiz.md`](./session-10-quiz.md) | End of S10 | 12 |
| Session 11 quiz / Domain 3 checkpoint | [`session-11-quiz.md`](./session-11-quiz.md) | End of S11 | 12 |
| Final readiness set | [`final-readiness-set.md`](./final-readiness-set.md) | S12, timed | 45 |

## How the progression works

Each objective is assessed four times, at increasing distance from when it was taught and
at increasing difficulty. This is the mechanism behind the taught / practiced / quizzed /
reviewed columns in [`../curriculum/exam-objective-map.md`](../curriculum/exam-objective-map.md).

1. **Warm-up (ungraded).** Free-recall prompts on earlier sessions. No options to choose from — learners must produce the answer. Fastest, cheapest form of retrieval practice, and it exposes gaps before new content lands on top of them.
2. **Session quiz (formative).** Mostly items on the session just taught, plus a **carry-forward block** drawn from earlier sessions. The carry-forward range widens as the course proceeds, so by Session 10 an item can come from anywhere in Sessions 1–9.
3. **Domain checkpoint (diagnostic).** A full sweep of one domain, administered after the domain is complete: Domain 1 at the start of Session 3, Domain 2 at the start of Session 8, Domain 3 inside the Session 11 quiz. Checkpoints use multi-objective items so a whole domain fits into 15 minutes.
4. **Final readiness set (summative).** 45 items in 45 minutes, matching the exam's duration and domain weights.

### Carry-forward composition

| Quiz | Items | New-session items | Carry-forward items | Carry-forward drawn from |
| --- | --- | --- | --- | --- |
| S1 | 12 | 12 | 0 | — |
| S2 | 12 | 10 | 2 | S1 |
| S3 | 12 | 9 | 3 | S1–S2 |
| S4 | 12 | 9 | 3 | S1–S3 |
| S5 | 12 | 9 | 3 | S1–S4 |
| S6 | 12 | 9 | 3 | S2–S5 |
| S7 | 10 | 8 | 2 | S1–S6 |
| S8 | 12 | 9 | 3 | S2–S7 |
| S9 | 12 | 9 | 3 | S3–S8 |
| S10 | 12 | 9 | 3 | S4–S9 |
| S11 | 12 | 6 | 6 | 3 from Domain 3 (S8–S10) + 3 mixed from S1–S7 |

Carry-forward selections follow the cumulative review schedule in
[`../curriculum/six-week-plan.md`](../curriculum/six-week-plan.md), so the quiz bank and
the session plan reinforce the same objectives in the same order.

### Difficulty ramp

| Sessions | Dominant item style |
| --- | --- |
| S1–S3 | Definition and recall. "What is X," "which statement is true," direct classification. |
| S4–S8 | Scenario selection. "A team needs X, which service fits," with plausible adjacent-service distractors. |
| S9–S12 | Discrimination and multi-constraint. Policy vs RBAC vs locks, Advisor vs Service Health vs Monitor, two constraints in one stem. |

Carry-forward items are written one notch harder than the original item on the same
objective. A Session 1 item might ask what the shared responsibility model is; the
Session 7 carry-forward item asks who is responsible for OS patching on an IaaS VM.

## Item conventions

Every quiz file has the same two parts, split by a horizontal rule:

- **Questions** — printable or LMS-importable as-is. No answers.
- **Answer key** — one table row per item: answer, objective ID, why the answer is right and the main distractor wrong, and the Microsoft Learn source.

Cut the file at the rule to produce a learner handout.

Item types used, and how to mark them:

| Type | Marker in stem | Notes |
| --- | --- | --- |
| Single best answer | none | Four options, exactly one correct. The default. |
| Multi-select | `(Select all that apply.)` | Key lists every correct option. All-or-nothing. |
| Matching | `(Match each … )` | Key gives the pairs. Fractional credit. |
| Ordering | `(Put … in order.)` | Used for hierarchy and layer items. All-or-nothing. |
| True/false set | `(For each statement, answer yes or no.)` | Mirrors the exam's problem-solution format. Fractional credit. |

**Every item is worth exactly one point**, whatever its type. Multi-part items — matching
and yes/no sets — earn correct parts divided by total parts. This matters most in the final
readiness set: awarding a point per pair would inflate Domain 2, which carries most of the
multi-part items, and break the weight alignment.

### Rules every item in this bank follows

1. **Objective-traceable.** Each item maps to at least one objective ID from the objective map. Nothing is assessed that is not on the current skills-measured list.
2. **Microsoft Learn sourced.** Each key row links the unit or doc that establishes the answer.
3. **No exam dumps.** No item is recalled from, modeled on, or checked against any real exam question. Items are written from published objectives and official documentation only.
4. **No verbatim copying.** Stems and options are original prose. Microsoft's wording is not reproduced.
5. **Current terminology only.** Microsoft Entra ID, not Azure AD. Microsoft Defender for Cloud, not Security Center. Pricing calculator, not TCO calculator. The full list is in [`../sources/source-validation-log.md`](../sources/source-validation-log.md).
6. **Context-only topics excluded.** Sustainability, encryption and key management, the Service Trust Portal, AI/ML/IoT services, cost optimization, and Copilot in Azure are taught for coherence but never scored, because they are not bulleted objectives. This follows the Phase 1 recommendation.
7. **Distractors are real services.** Wrong options are plausible adjacent Azure services that beginners actually confuse — availability sets versus availability zones, service endpoints versus private endpoints, Policy versus locks, Log Analytics versus Application Insights. A distractor is never a made-up product name.
8. **No trick items.** No double negatives, no "all of the above," no dependence on a number Microsoft does not publish.

## Scoring and what to do with the results

| Instrument | Target | If the learner is below it |
| --- | --- | --- |
| Warm-up | Not scored | Re-teach on the spot; it is 10 minutes and that is the point |
| Session quiz | 80% | Assign the module unit for each missed objective before the next session |
| Domain 1 checkpoint (S3) | 75% | Drives which Domain 1 objectives get warm-up priority in S4–S8 |
| Domain 2 checkpoint (S8) | 75% | Drives the re-teaching choices in the Session 11 cumulative block |
| Session 11 quiz / Domain 3 checkpoint | 80% | Drives the Session 12 gap clinic |
| Final readiness set (S12) | 85%, no domain below 75% | Do not schedule the exam yet; work the 10-day plan and retake |

The exam's passing score is 700 or greater, which is not a percentage of items and does
not translate cleanly into a percent correct. The course targets above it deliberately.
Practice scores are a readiness signal, not a prediction — Microsoft publishes no
relationship between practice assessment scores and exam outcomes.

## Objective coverage

All 57 objectives appear in at least one session quiz, at least one domain checkpoint, and
the final readiness set. The per-instrument breakdown lives in
[`coverage-matrix.md`](./coverage-matrix.md), which is generated from the answer keys.

## Using the bank

**Instructors:** print or import the Questions half, keep the key. Review every item
immediately after the quiz — the review is where the learning happens, not the scoring.
For missed items, name the objective ID out loud so learners can find it on their
objective checklist.

**Adapting item counts:** if a session runs long, cut carry-forward items first. Never cut
the new-session items; they are the only coverage that objective gets before its
checkpoint.

**Writing more items:** follow the eight rules above, map to an objective ID, cite the
unit, and add the item to the coverage matrix. Items for context-only topics do not belong
in this bank.
