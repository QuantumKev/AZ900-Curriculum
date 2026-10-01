# Session 2 instructor notes — Cloud Benefits, Pricing Models, and IaaS/PaaS/SaaS

**Objectives taught:** 1.1.6, 1.1.7, 1.2.1, 1.2.2, 1.2.3, 1.2.4, 1.3.1, 1.3.2, 1.3.3, 1.3.4
**Slides:** [session-02-slides.md](session-02-slides.md)
**Lab:** [../labs/session-02-lab.md](../labs/session-02-lab.md)
**Quiz:** [../quizzes/session-02-quiz.md](../quizzes/session-02-quiz.md) — 12 items (10 new, 2 carry-forward), 15 minutes
**Warm-up:** [../quizzes/warm-ups.md](../quizzes/warm-ups.md), Session 2 set — recalls Session 1
**Domain minutes:** Domain 1 — 120

This is the session to teach next if the first meeting was introductions and a practice exam.

## Run of show

| Min | Block | Slides | Leave the block when |
| --- | --- | --- | --- |
| 0–10 | Warm-up, or recovery if Session 1 was not taught | 2 | The room can produce the six Session 1 answers, or you have taught the ones they cannot |
| 10–35 | Teach A — availability, scale, reliability, predictability | 3–6 | They can contrast scale up vs scale out, and name both kinds of predictability |
| 35–55 | Teach B — security, governance, manageability | 7–9 | They can sort "portal" into management in the cloud and "autoscale" into management of the cloud |
| 55–75 | Teach C — service types, serverless, pricing | 10–16 | They can place a workload in IaaS, PaaS, or SaaS, and pick a pricing model without confusing reservation and savings plan |
| 75–105 | Practice | lab | Both sorts done. Function App seen, even if only on your screen |
| 105–120 | Quiz and review | 17–18 | Reviewed in the room. Both Learn modules assigned |

The plan budgets Teach C at 20 minutes and practice at 30. If you spend the warm-up on recovery, steal the extra minutes from the Function App demo, not from the quiz.

## This cohort — Session 1 was not a lecture

The first meeting was introductions and a practice assessment. Objectives 1.1.1 through 1.1.5 were not taught. The practice assessment is a preview of the whole exam. It does not replace the Session 1 lecture, and it will have felt hard. Tell them that in the first minute so they do not treat a low score as a verdict.

Do this instead of a normal warm-up:

1. Say the five ideas in four minutes, one sentence each. Cloud computing is rented compute, storage, and networking. The provider always owns the building, the physical network, and the hosts; you always own data, devices, and identities. Public is open to buy, private is for one organization, hybrid connects them. Consumption is pay for what you use, and that spend is operating expenditure, not a capital purchase.
2. Ask the six warm-up prompts from [`warm-ups.md`](../quizzes/warm-ups.md). They are free recall, not multiple choice.
3. Any prompt two or more people miss, teach with the worked example in the Session 1 notes. Cap it at 10 minutes total for this opening. Park anything still shaky on the board and hit it again in the quiz review.

Do not run the Session 1 slide deck. Do not skip Session 2 content to "finish Session 1 properly." Session 3 opens with the Domain 1 checkpoint, so the Learn modules are the rest of the catch-up, and you should say that when you assign them.

Log what the room missed in [`../operations/session-log.md`](../operations/session-log.md).

## Before you walk in

- Warm-up prompts on a card in your hand, not on the projector. Free recall dies if the question sits on screen with the answer.
- Lab worksheets printed through the instructor-key break.
- Quiz ready. Carry-forward items are 1.1.2 and 1.1.5. If this cohort never heard those, a miss there is expected; review them with the Session 1 sentence, not a speech.
- Function App demo rehearsed to the point of choosing a plan, then discarded. See the lab. If your subscription is not ready, the no-cost path is the whole room watching the [Functions overview](https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview) while you narrate the five sentences in the lab. Do not troubleshoot a deployment during the 30-minute block.
- Pricing facts you must be able to say without notes: a reservation commits to a specific resource for one or three years. A savings plan commits to an hourly compute spend for one or three years and can apply across eligible compute services. Spot uses spare capacity and can be evicted. Do not quote a discount percentage. Those rates change, and the exam does not require the number.

## 0–10 Warm-up

Six prompts, about a minute each, including the answer from a learner before you confirm. Accept substance, not wording.

Priority if you are in the recovery path: prompts 2 and 3 (what you always own, what the provider always owns) and prompt 5 (CapEx, OpEx, which one cloud consumption is). Those two ideas are the floor for service types and pricing.

## 10–35 Teach A — benefits, first half (1.2.1, 1.2.2)

High availability: the service keeps answering because you designed out single points of failure. Do not teach availability zones yet. Say "more than one copy, separated from each other" and point at Session 3.

Scale up vs scale out. Worked example: a café with one espresso machine. Scale up is a faster machine. Scale out is a second machine and a second barista. Cloud scale-out is useful because you can send the second barista home when the line is gone. Write "up = vertical = bigger" and "out = horizontal = more copies" on the board. The quiz reverses these on purpose.

Reliability: recover and continue. Availability is staying up. Reliability is surviving the failure. One sentence is enough if you give an example: a disk dies, the app comes back on another copy.

Predictability, both kinds, back to back so they do not collapse into one word.

- Performance: autoscale and a load balancer keep the page fast at lunch and at midnight.
- Cost: you can look at usage and forecast the bill. Name the pricing calculator as the tool, and say we use it in Sessions 6 and 8. Do not open it today unless the practice block finishes early.

## 35–55 Teach B — security, governance, manageability (1.2.3, 1.2.4)

Governance is not a product name yet. Azure Policy is Session 9. Today: templates so deployments match a standard, auditing so drift is visible, and the ability to fix many resources when the standard changes. Say plainly that moving to the cloud does not make an organization compliant.

Manageability is the slide people mix up. Put two columns on the board and make the room sort four phrases before you show the answer:

- Azure portal → management **in** the cloud
- Azure CLI → management **in** the cloud
- Autoscale → management **of** the cloud
- Deploy from a template → management **of** the cloud
- Alert when CPU stays high → management **of** the cloud

Sustainability: one minute, marked context, not quizzed. Shared datacenters can be more efficient than a closet server for each small organization. Then leave it.

## 55–75 Teach C — service types, serverless, pricing (1.3.1–1.3.4, 1.1.7, 1.1.6)

Draw the responsibility shift as a staircase, not three unrelated products. As you move IaaS → PaaS → SaaS, you hand the provider more of the stack, and you give up control of that layer.

Worked examples, one each:

- IaaS: the clinic lifts the scheduling server into a virtual machine and still patches Windows.
- PaaS: a developer deploys the scheduling API to a host that patches the OS. The developer does not get to pick a custom driver.
- SaaS: staff open a finished scheduling product in a browser. The clinic manages who can sign in, and owns the appointment data.

Ask: "Who patches the OS?" after each example. IaaS you, PaaS provider, SaaS provider. That question is the whole objective.

Serverless, immediately after PaaS so it does not become a fourth column. Say: there are servers; you do not provision them; an event runs your code; you pay for the run. Azure Functions is the picture. It is not a cloud model. The wrong answer on the quiz is "a fourth deployment model alongside public, private, and hybrid."

Pricing. Teach the table by what you give up, not by a discount percent.

- Pay-as-you-go: no commitment. Default. Right for anything you cannot describe yet.
- Reservation: you commit to a specific resource, typically a virtual machine size in a region, for one or three years, and the rate drops. Wrong choice if the size will change next month.
- Azure savings plan for compute: you commit to an hourly dollar amount for one or three years. The discount can apply across eligible compute, so you are not pinned to one size. This is the distinction the quiz tests. Reservation is the specific resource. Savings plan is the spend.
- Spot: spare capacity, deepest cut, the provider can evict you. Only for work that can stop and restart. A batch job. Not a clinic's scheduling system during the day.

Gap G1: the side-by-side lives in the cost module, not the cloud-concepts path. You are teaching it in the right week on purpose. Tell the room we repeat it in Session 8 next to real cost tools. Gap G2: serverless is the same story; Session 4 builds a Function.

## 75–105 Practice

[Session 2 lab](../labs/session-02-lab.md).

Part A then Part B on paper, in pairs. Walk the room. The errors you want to catch in the moment:

- Calling Microsoft 365 "PaaS" because it is Microsoft. It is SaaS.
- Calling any website "SaaS." A site you build and host on a virtual machine is IaaS. A site you deploy as code onto a managed platform is PaaS. SaaS means you consume the vendor's finished application.
- Putting a steady three-year virtual machine on spot because spot is "cheapest." Cheapest is wrong if the workload cannot be evicted.
- Putting a specific unchanging virtual machine on a savings plan when the question says a specific size for three years. That is a reservation. Use the savings plan when the question stresses a spend commitment across compute services.

Part C is your demo. Five minutes. If it is not rehearsed, do the no-cost narration in the lab and move to the quiz. A failed deployment teaches nothing.

## 105–120 Quiz and review

Closed notes, 15 minutes, then immediate review. Target 80 percent.

On review, stay on the two confusions above if they show up: reservation vs savings plan, and serverless as a service style rather than a deployment model. Carry-forward misses on shared responsibility or CapEx/OpEx get the one-sentence version from the recovery script.

Assignment, both modules, including their assessments:

- [Describe the benefits of using cloud services](https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/)
- [Describe cloud service types](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/)

If this cohort missed the Session 1 lecture, add the Session 1 module as well: [Describe cloud computing](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/). Say why: Session 3 starts with a 12-item checkpoint across all 15 Domain 1 objectives.

Update the readiness tracker with the Session 2 quiz percent. Note anyone who missed both carry-forward items; they need the Session 1 module before Session 3, not a conversation in the hallway only.

## If you are short on time

Cut in this order: sustainability slide (already one minute), Function App demo (use the no-cost narration), then the second worked example under governance. Do not cut the pricing table. Do not cut the quiz. Do not cut scale up vs scale out.

## If you have ten extra minutes

Open the pricing calculator, add one virtual machine, and show that region and size change the estimate. Do not teach calculator technique. That is Session 8. You are only making "cost predictability" concrete.

## Sources

[Benefits](https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/) · [Service types](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/) · [Cost factors, pricing models](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/2-describe-factors-affect-costs-azure) · [Azure Functions unit](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/6-functions) · [Functions overview](https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview)
