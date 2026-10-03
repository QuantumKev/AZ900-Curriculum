# Session 8 slides — Azure Cost Management

Each `##` heading is one slide. Notes: [session-08-instructor-notes.md](session-08-instructor-notes.md).

## 1. What the bill is made of

Session 8. Domain 2 checkpoint first, then why Azure costs what it costs, and how you see it coming.

## 2. Pricing models, second pass

You learned these in Session 2. They are still a cloud-concepts objective, and they show up inside cost.

| Model | Commitment |
| --- | --- |
| Pay-as-you-go | None. Pay for use |
| Reservation | A specific resource, one or three years |
| Azure savings plan for compute | An hourly compute spend, one or three years |
| Spot | Spare capacity. You can be evicted |

## 3. What changes the cost

- The resource type, and the settings you picked (size, tier, redundancy).
- How much you consume, and for how long.
- Things you forgot to delete. An idle disk still costs money.
- Geography. The same resource in another region can price differently. Data transfer between regions and out to the internet is its own charge.
- The subscription offer you bought.
- Marketplace products. A third party can bill you through the same invoice.

## 4. Pricing calculator

The [pricing calculator](https://azure.microsoft.com/en-us/pricing/calculator/) estimates a design before you build it.

It does not read your current bill. It does not know about resources you already left running. It is a quote for a configuration you describe.

You used it for storage in Session 6. Today you build a small monthly estimate and change the region on purpose.

## 5. The TCO calculator is retired

Older study guides say to compare the pricing calculator with a Total Cost of Ownership calculator.

Microsoft Learn says that TCO calculator is retired. The objective is the pricing calculator. If a practice site still drills the TCO calculator, the practice site is out of date.

## 6. Microsoft Cost Management

After you are spending, Cost Management is where you look.

**Cost analysis** shows what you spent and what you are on track to spend.

**Budgets** set an amount. **Alerts** fire when you cross a threshold you chose. A budget alert does not, by itself, turn resources off.

## 7. Tags

A tag is metadata you attach to a resource or a resource group. A name and a value. `costCenter=finance`.

Tags do not secure anything and they do not change the price. They let cost analysis answer a business question: what did this project cost, what did this owner spend.

We put `course` and `session` tags on lab groups for the same reason.

## 8. Lab and quiz

Checkpoint results go into the readiness tracker.

Lab: a budget if the guided project is available, a three-resource estimate in two regions, and a tag you can explain.

Quiz includes the pricing-model objective again.

Assignment: [Describe cost management in Azure](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/).
