# Session 1 instructor notes — Cloud Computing Foundations

**Objectives:** 1.1.1, 1.1.2, 1.1.3, 1.1.4, 1.1.5
**Slides:** [session-01-slides.md](session-01-slides.md)
**Lab:** [../labs/session-01-lab.md](../labs/session-01-lab.md)
**Quiz:** [../quizzes/session-01-quiz.md](../quizzes/session-01-quiz.md) — 12 items, 15 minutes
**Domain minutes:** Domain 1 — 120

## Run of show

| Min | Block | Slides | What has to be true when you leave the block |
| --- | --- | --- | --- |
| 0–10 | Orientation | 1–5 | Learners can name the three domains and know Learn is closed during the exam |
| 10–35 | Teach A | 6–8 | They can define cloud computing as rented compute, storage, and networking |
| 35–60 | Teach B | 9–12 | They can place data, identities, and the physical datacenter on the right side, and pick public, private, or hybrid from a one-sentence scenario |
| 60–90 | Practice | lab | Both sorts done; everyone has seen the portal home |
| 90–105 | Teach C | 13–14 | CapEx vs OpEx, and why cloud consumption is OpEx |
| 105–120 | Quiz and review | 15–16 | Quiz taken and answers reviewed. Assignment spoken aloud |

Session 1 has no warm-up. The orientation replaces it. Wrap is folded into the quiz review.

## Before you walk in

- Quiz handouts printed, or the form open. Answer key stays with you until review.
- Objective checklists printed, one per learner. They keep this sheet all course.
- Portal signed in on the instructor machine, on a subscription where you will only look, not create.
- Lab pages printed through the instructor-key break. The key stays at your desk.
- Confirm the free-account terms on [azure.microsoft.com/free](https://azure.microsoft.com/en-us/free/) if you will tell anyone to create an account. **NEEDS VERIFICATION** each cohort (V9).

## 0–10 Orientation

Say what the certification is for: a shared vocabulary so a beginner can follow a cloud conversation and answer scenario questions. Say what it is not: you will not build a landing zone on this exam.

Put the three weights on the board. Domain 1 looks "introductory" and is still about a quarter to a third of the exam. That is why the first two sessions are all cloud concepts, and why those ideas come back in warm-ups for six weeks.

Two facts that contradict what people have heard about other Microsoft exams:

- Fundamentals exam time is 45 minutes, inside 65 minutes of seat time.
- Microsoft Learn is **not** available during the exam.

Mention accommodations once: request them before registering. You will repeat this in Session 12. Do not linger.

Hand out the objective checklist. Tell them the IDs (`1.1.1`) are ours, for tracking, not Microsoft's.

## 10–35 Teach A — what cloud computing is (1.1.1)

Worked example, say it slowly. A clinic keeps patient scheduling on a server in a closet. The closet needs power, cooling, patches, and a spare disk. Cloud computing is moving that workload onto rented capacity: someone else's building, someone else's hosts, a service you turn on and off.

Then the three nouns, with one Azure example each so the words stick, without turning this into a product tour:

- Compute — a virtual machine.
- Storage — a place to put files.
- Networking — a private network those two use to talk.

On-premises means the organization runs the facility. Cloud means the provider does. Write both words on the board. You will contrast them in every later session.

Vocabulary slide: tenant, subscription, and resource get formal definitions in Session 3 and Session 7. Today they only need to hear the words so the portal tour is not noise.

## 35–60 Teach B — shared responsibility and cloud models (1.1.2, 1.1.3, 1.1.4)

Draw three columns: always the provider, shifts with the service type, always the customer.

Always the provider: physical datacenter, physical network, physical hosts.

Always the customer: information and data, devices allowed to connect, accounts and identities.

The middle column is the exam's favorite trap. Do not list every layer. Use three sentences:

- Infrastructure as a service: you patch the operating system.
- Platform as a service: the provider patches the operating system; you own the application and the data.
- Software as a service: the provider runs the application; you own the data and who can sign in.

Tell them the formal names arrive next session. Today the point is that "in the cloud" does not mean "the provider does everything."

Cloud models. Public is multi-tenant and open to purchase. Private is dedicated to one organization. Hybrid is the two, connected. Multicloud is more than one public provider; say the word, do not teach Arc.

Use cases, one each, then stop. Ask the room to vote before you confirm:

- A student club website with no special data rules. Public.
- Records that must stay on infrastructure used only by one hospital system. Private, or the private half of hybrid.
- The hospital keeps the records private and bursts the public website to Azure in flu season. Hybrid.

If someone says "private cloud means on-premises only," correct it: private describes who the infrastructure is for, not which building it sits in. A hoster can run a private cloud for one customer.

## 60–90 Practice

Run [the Session 1 lab](../labs/session-01-lab.md). Sorting first, while energy is high. Portal tour second. If the room has no accounts, project yours and narrate the same six stops. Do not create a resource today.

Watch for: learners putting "accounts and identities" on the provider side, and learners calling every on-premises system a private cloud. A private cloud is a cloud model. A file server in a closet is on-premises; it is not automatically a private cloud.

## 90–105 Teach C — consumption-based model (1.1.5)

Come back to the clinic. Buying the server, the disks, and the closet build-out is capital expenditure (CapEx). Paying a monthly cloud bill for the hours the service ran is operating expenditure (OpEx). Cloud consumption is OpEx.

The planning change: you stop buying peak capacity "just in case" and sitting on it in August. You add capacity when the demand is real and release it when it is not. You still forecast. You just do not pre-buy the hardware.

Do not teach reservations, savings plans, or spot today. Those are Session 2 (objective 1.1.6). If someone asks, say "four offers, next session" and write the four names on the board so the question is visibly parked: pay-as-you-go, reservations, Azure savings plan for compute, spot.

## 105–120 Quiz and review

15 minutes, closed notes. Then review immediately. For each miss that two or more people share, one sentence of correction, not a second lecture.

Assignment, said out loud and on the last slide: complete [Describe cloud computing](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/), including the module assessment. Create a Learn account. Choose a hands-on path.

Mark the checklist: 1.1.1 through 1.1.5 taught today.

## If you are short on time

Cut the portal tour to the three stops in the lab's no-cost path (home, search, subscriptions). Do not cut the quiz. Do not cut shared responsibility. CapEx/OpEx can shrink to the two definitions and one sentence if the sorts ran long.

## If this meeting was only an introduction

If the cohort spent the first meeting on introductions and a practice assessment, do not pretend this lecture happened. Log that in the session log. Session 2's notes open with a recovery of these five objectives. The practice assessment is not a substitute for 1.1.1–1.1.5; it is a preview of the whole exam.

## Sources

[Describe cloud computing](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/) · [Shared responsibility](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility) · [Consumption-based model](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/6-describe-consumption-based-model)
