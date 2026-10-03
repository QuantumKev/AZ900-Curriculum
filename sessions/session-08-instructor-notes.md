# Session 8 instructor notes — Azure Cost Management

**Objectives:** 3.1.1, 3.1.2, 3.1.3, 3.1.4, second pass on 1.1.6, touch 1.1.5 and 1.1.1
**Slides:** [session-08-slides.md](session-08-slides.md)
**Lab:** [../labs/session-08-lab.md](../labs/session-08-lab.md)
**Checkpoint:** [../quizzes/checkpoint-domain-2.md](../quizzes/checkpoint-domain-2.md) — replaces the warm-up
**Quiz:** [../quizzes/session-08-quiz.md](../quizzes/session-08-quiz.md)
**Domain minutes:** Domain 1 — 20, Domain 2 — 5, Domain 3 — 95

## Run of show

| Min | Block | Leave it when |
| --- | --- | --- |
| 0–15 | Domain 2 checkpoint | Two weak Domain 2 objectives written down for Session 11 |
| 15–40 | Cost factors and pricing models again | They can name orphaned resources and geography as cost factors, and restate reservation vs savings plan vs spot |
| 40–65 | Cost Management, calculator, tags | Calculator vs Cost Management is clear. A tag is not a lock and not a policy |
| 65–95 | Lab | Two-region estimate exists. One tag is explained in a sentence |
| 95–110 | Quiz | |
| 110–120 | Wrap | TCO calculator called out as retired |

## Checkpoint

Same pattern as Session 3. Review only shared misses. The 27 Domain 2 objectives cannot be retaught in the review. Pick two IDs for the Session 11 clinic and put them in the session log.

## Teach A

Open from Session 1: you pay for what you use. Then the factors on the slide. The one beginners skip is orphaned resources: a disk left behind when a VM is deleted, a public IP nobody detached. Say "the bill does not care that you meant to delete it."

Geography: price differs by region, and data leaving a region costs money. The lab makes this numeric without you quoting a rate.

Marketplace: third-party products can appear on the Azure invoice. One sentence.

Pricing models, second pass, from the Session 2 table. Do not reteach the whole of Session 2. Ask the room the reservation vs savings plan question before you show the slide. Gap G1 said this second pass is scheduled. This is it.

## Teach B

Pricing calculator: a forward estimate of a design. No sign-in required. It will not warn you about the idle disk from last week.

Microsoft Cost Management: cost analysis of actual and forecast spend, budgets, alerts. A budget does not stop the resources. If you want spending to stop, that is a different control (and often not what a beginner tenant can do). Do not tell the room a budget is a spending cap unless you have verified that behavior for the offer they are on. Teach alert, not kill switch.

Tags: `key=value`, for reporting. They do not grant access (that is RBAC), they do not constrain shape (that is Policy, next session), they do not block delete (that is a lock, next session). You can foreshadow those three sentences. They are the Session 9 open.

## Wrap — TCO

Say it plainly. The Total Cost of Ownership calculator is retired. Older PDFs and videos still assign it. The study guide's current cost objective is factors, the pricing calculator, cost management capabilities, and tags. Validation log V6 is your source if someone pushes back.

## If you are short on time

The calculator lab is the no-cost path and the objective. Cut the guided project before you cut the two-region reprice. Keep the TCO warning. It is a known trap and it takes one minute.

## Sources

[Cost module](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/) · [Cost factors](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/2-describe-factors-affect-costs-azure) · [Pricing calculator unit](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/3-compare-pricing-total-cost-of-ownership-calculators) · [Cost Management](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/overview-cost-management) · [Calculator](https://azure.microsoft.com/en-us/pricing/calculator/) · [Tags](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources)
