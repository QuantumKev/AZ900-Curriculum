# Session 8 lab — Estimate, reprice, tag

**Time:** 30 minutes
**Objectives practiced:** 3.1.1–3.1.4, 1.1.6
**You need:** a browser. No Azure sign-in for Parts A and B.

---

## Part A — Three resources, then another region (20 minutes)

In the [pricing calculator](https://azure.microsoft.com/en-us/pricing/calculator/), build one estimate. Use the cheapest reasonable choices. You are comparing, not designing production.

1. One virtual machine. A small size. Note the region.
2. One storage account, blob, a modest capacity, LRS, hot.
3. One App Service plan, a basic tier if it is offered, same region.
4. Write the estimated monthly total and the region name.
5. Change only the region on all three, to a second region the instructor names. Write the new total.
6. Answer: which cost factor did you just demonstrate? Which of the four pricing models is the calculator assuming if you did not add a reservation?

## Part B — Tags as questions (5 minutes)

You do not have to create a resource. Invent four tags for a resource group that holds this course's labs. For each tag, write the business question it would let a bill answer.

Example shape: `costCenter=training` answers "was this the training budget or the product budget?"

Use your own four. Do not stop at the example.

## Part C — Optional, subscription required

[Set up cost guardrails](https://learn.microsoft.com/en-us/training/modules/guided-project-cost-guardrails/).
A budget alert is the success criterion. If cost analysis is empty because the subscription is new, say so. Empty is an honest result, not a failed lab.

### No-cost path

Parts A and B only. The calculator is the objective 3.1.2 activity and does not need an account.

<div class="pagebreak"></div>

## Instructor key

Part A demonstrates geography (region) as a cost factor. Unless a reservation was added, the estimate is pay-as-you-go.

Part B: accept any tag that could group spend (owner, environment, cost center, application, cohort). Reject tags described as "this tag stops the VM from being deleted." That is a lock, next session.

Part C: a budget does not delete resources. An alert is the outcome to look for.
