<!-- Copyright (c) 2026 Kevin Robinson. All Rights Reserved. -->

# Session 8 instructor script — Describe cost management in Azure

**Microsoft Learn module:** [Describe cost management in Azure](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/)

**Checked against the live module:** 22 October 2026

**Other Session 8 files:** [instructor notes](../session-08-instructor-notes.md) · [slides](../session-08-slides.md) · [lab](../../labs/session-08-lab.md) · [quiz](../../quizzes/session-08-quiz.md) · [Domain 2 checkpoint](../../quizzes/checkpoint-domain-2.md)

## How to read this script

| Label | What to do |
| --- | --- |
| **Say** | Read it out loud, word for word. |
| **Ask** | Ask the class. Wait for answers. Then read the **Answer** out loud. |
| **Exam tip** | Read it out loud. |
| **Board** | Write it on the whiteboard. |
| **Do** | For you only. Do not read it out loud. |

The script follows Microsoft's unit order. The instructor notes teach the pricing options early. Microsoft compares them in the last unit, so this script does too. The total time is the same.

Do not give prices or discount percentages from memory. They change often, and the exam does not ask for them.

## Microsoft's units, in order

1. [Introduction](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/1-introduction)
2. [Describe factors that can affect costs in Azure](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/2-describe-factors-affect-costs-azure)
3. [Explore the pricing calculator](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/3-compare-pricing-total-cost-of-ownership-calculators)
4. [Describe the Microsoft Cost Management tool](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/6-describe-azure-tool)
5. [Describe the purpose of tags](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/7-describe-purpose-of-tags)
6. [Describe cost optimization options in Azure](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/7a-describe-cost-optimization-options)
7. Module assessment. Students take it on Learn after class. Do not show it in class.
8. [Summary](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/9-summary)

## Microsoft's learning objectives

- Describe factors that can affect costs in Azure.
- Describe the Azure pricing calculator.
- Describe the Microsoft Cost Management tool.
- Describe the purpose of tags.
- Describe cost optimization options, including reservations, savings plans, and Spot pricing.

## Two-hour plan

| Time | Block | Slide |
| --- | --- | --- |
| 0:00–0:15 | Domain 2 checkpoint | 1 |
| 0:15–0:18 | 1. Introduction | 1 |
| 0:18–0:33 | 2. What affects the cost | 3 |
| 0:33–0:39 | 3. Pricing calculator | 4 |
| 0:39–0:49 | 4. Cost Management | 6 |
| 0:49–0:56 | 5. Tags | 7 |
| 0:56–1:05 | 6. Ways to pay less | 2 |
| 1:05–1:35 | Lab | 8 |
| 1:35–1:50 | Quiz | 8 |
| 1:50–2:00 | Wrap-up and summary | 5 |

**If you fall behind:**

- At 0:30, if you are still on geography, skip the free trial details and the Marketplace certification sentence.
- At 0:45, if you have not reached budgets, skip the details of credit alerts and department alerts. Keep the three alert names.
- At 1:00, if you have not started section 6, read only the three options, the memory line, and the quick round.
- Never cut the two-region price check in the lab, the quiz, or the TCO warning.

## Before class

- Print or open the checkpoint, the quiz, and both answer keys.
- Open the [pricing calculator](https://azure.microsoft.com/en-us/pricing/calculator/) in a browser tab.
- Pick two regions for the lab, on different continents.

## Today's client

Contoso Health is the made-up clinic company from earlier sessions. Today, its finance director has five questions. Each question is one part of the lesson.

---

## 0:00 — Domain 2 checkpoint

**Do:** Hand out the [Domain 2 checkpoint](../../quizzes/checkpoint-domain-2.md). It replaces the warm-up today. Keep the answer key with you.

**Say:**

> Before today's topic, we have a short check. It covers Domain 2 of the exam: Azure architecture and services. That is the largest part of the exam, about 35 to 40 percent.
>
> There are 12 questions. You have 12 minutes. Work on your own. I use your results to plan our review before the exam.

**Do:** At 0:12, stop. Review only the questions that two or more people missed. Give the correct answer and one reason. Do not re-teach whole topics.

**Do:** After class, put the scores in the [readiness tracker](../../operations/readiness-tracker.md). Write the two weakest Domain 2 objective numbers in the [session log](../../operations/session-log.md). Session 11 uses them.

---

## 0:15 — 1. Introduction

**Learn unit:** [Introduction](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/1-introduction)

**Do:** Show slide 1.

**Say:**

> Today is about money. Contoso Health just got its first large Azure bill. The finance director has five questions for us.

**Board:**

```text
Question                                    Today's topic
Why does Azure cost this much?              Cost factors
What will a new project cost?               Pricing calculator
What are we spending? Can we get a warning? Cost Management
Which team spent it?                        Tags
How can we pay less for the same work?      Reservations, savings plan, Spot
```

**Say:**

> These five questions are today's five topics, in the same order as Microsoft's module. All five can be on the exam.

**Exam tip:** The exam does not ask you for prices. It asks what changes the price, and which tool or option fits a situation.

---

## 0:18 — 2. What affects the cost

**Learn unit:** [Describe factors that can affect costs in Azure](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/2-describe-factors-affect-costs-azure)

**Do:** Show slide 3.

**Move on when:** students can name the six factors and give one example of each.

**Say:**

> Remember from Session 2: in the cloud, you pay for what you use. You rent what you need, and you give it back when you are done. Use more, pay more. Use less, pay less.
>
> Microsoft lists six things that affect what you pay. Please write them down.

**Board:**

```text
What affects the cost
1. Resource type
2. Consumption
3. Maintenance
4. Geography
5. Subscription type
6. Azure Marketplace
```

### Resource type

**Say:**

> First, resource type. What you create, the settings you choose, and the region you pick all change the price. Azure tracks how much you use and charges you for it.
>
> For a storage account, the price depends on the kind of data you store, how fast you need to reach it, how many backup copies you keep, and the region.
>
> For a virtual machine, the price depends on software licenses, such as the operating system. It also depends on the processor, the number of cores, the attached disks, and the network interface. The same virtual machine can cost a different amount in a different region.

### Consumption

**Say:**

> Second, consumption. This is pay-as-you-go. You pay for what you used during the billing cycle. There is no commitment.
>
> Azure also has three ways to pay less. I will name them now. We will compare them at the end of class.
>
> - A reservation. You commit to specific resources for one or three years.
> - Azure savings plan for compute. You commit to spend a set amount per hour on compute, for one or three years.
> - Spot Virtual Machines. You get a lower price by using Azure's spare capacity. Azure can take that capacity back when it needs it.

### Maintenance

**Say:**

> Third, maintenance. When you create a virtual machine, Azure also creates other resources for it, such as a disk, a network interface, and a public IP address. If you delete the virtual machine, those resources may stay behind. They keep costing money.
>
> Azure charges you for what exists, not for what you meant to delete. So check for leftover resources, and remove what you do not need. Keeping related resources in one resource group makes them easier to find.

**Exam tip:** If a question says someone deleted a virtual machine and is still being charged, think leftover resources. That is the maintenance factor.

### Geography

**Say:**

> Fourth, geography. When you create most resources, you choose a region. The same resource can cost a different amount in a different region. That is because power, labor, taxes, and fees are not the same everywhere.
>
> Moving data costs money too, and distance matters. Moving data within Europe costs less than moving it from Europe to Asia or South America.
>
> Azure prices data transfer with billing zones. A billing zone is a group of regions used only to price data transfer. It is not the same as an availability zone.
>
> Some data coming into Azure is free. Data going out of Azure is charged, based on the billing zone. You may see these called inbound and outbound, or ingress and egress.

**Exam tip:** A billing zone is used to price moving data. An availability zone is a separate group of datacenters inside one region. It helps keep an app running if one zone fails. They are different things.

### Subscription type

**Say:**

> Fifth, subscription type. Some subscriptions include free usage. For example, the Azure free trial includes some products free for 12 months, a credit to spend in your first 30 days, and more than 25 products that are always free.

### Azure Marketplace

**Say:**

> Sixth, Azure Marketplace. This is where you buy ready-made solutions from other companies. For example, a virtual machine with special software already installed, or a backup product.
>
> With Marketplace, you may pay for two things: the Azure resources, and the vendor's product or service. The vendor sets its own price. Every solution in Marketplace is certified to meet Azure's standards.

**Ask (quick round):** Read each situation. The class names the factor.

| Situation | Answer |
| --- | --- |
| Contoso picks a bigger virtual machine with more cores. | Resource type |
| Contoso's app ran twice as many hours this month. | Consumption |
| A disk from a deleted virtual machine is still there. | Maintenance |
| The same app costs more in another region. | Geography |
| A new developer gets a credit for the first 30 days. | Subscription type |
| Contoso buys a firewall product from another company. | Azure Marketplace |

**Say:**

> Contoso now wants to build something new. Before they build it, they want a price. That is the pricing calculator.

---

## 0:33 — 3. Pricing calculator

**Learn unit:** [Explore the pricing calculator](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/3-compare-pricing-total-cost-of-ownership-calculators)

**Do:** Show slide 4. Then open the [pricing calculator](https://azure.microsoft.com/en-us/pricing/calculator/) on the screen. You do not need to sign in.

**Move on when:** students know the calculator is for estimates before you build.

**Say:**

> The pricing calculator estimates what Azure resources will cost. You can price one resource, a full solution, or one of Microsoft's example scenarios.
>
> Remember three things. It is only an estimate. Nothing is created. You are not charged for anything you add.
>
> It covers compute, storage, and network costs. For storage, you can choose the storage type, the access tier, and the redundancy. You learned those in Session 6.
>
> Here is how a team uses it. Contoso plans a new patient website. They add an App Service plan, a database, and storage. Before they build anything, they compare the monthly estimate across regions, tiers, and redundancy options. The manager uses the estimate to approve the budget. When the design changes, they update the estimate.
>
> One more thing. Older study material mentions a second calculator, the Total Cost of Ownership calculator, or TCO calculator. Microsoft has retired it. I will come back to that at the end of class.

**Exam tip:** Before you build, use the pricing calculator. After you build, use Cost Management. If a question says "estimate" or "before we deploy," the answer is the pricing calculator.

**Ask:** Contoso's bill went up last week. Can the pricing calculator tell them why?

**Answer:** No. The calculator only estimates a design. It cannot see what you are running. For real spending, you use Cost Management. That is next.

---

## 0:39 — 4. Microsoft Cost Management

**Learn unit:** [Describe the Microsoft Cost Management tool](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/6-describe-azure-tool)

**Do:** Show slide 6.

**Move on when:** students can name cost analysis, the three alert types, and budgets, and they know a budget alone does not stop spending.

**Say:**

> In Azure, you can create resources in minutes. Sometimes for a real need. Sometimes to test something. Sometimes by mistake. If nobody is watching, you find out when the invoice arrives.
>
> Microsoft Cost Management is a set of tools that helps you see, track, and control your Azure costs. It does three main jobs. It shows your costs. It sends alerts. And it lets you set budgets.

### Cost analysis

**Say:**

> Cost analysis is the part of Cost Management that shows your costs as charts. You can break costs down by billing cycle, subscription, resource group, region, service, or a single resource. You can also see how costs add up over time, and compare that trend to your budget.
>
> Teams use it to answer questions like these. Why did spending jump after Tuesday's deployment? Which test resources are sitting unused? Are our tags and budgets working?

### Cost alerts

**Say:**

> Cost Management has three types of alerts: budget alerts, credit alerts, and department spending quota alerts. You see all of them in one place in the Azure portal, called cost alerts.

**Board:**

```text
Cost alerts
Budget alert        You choose the level, for example 80%
Credit alert        Enterprise Agreement. Automatic at 90% and 100%
Department quota    Enterprise Agreement. For example 50% or 75%
```

**Say:**

> A budget alert tells you when spending reaches a level you set. For example, 80 percent of the monthly budget for a test subscription. That gives the team time to act before they go over. The alert appears in the portal, and an email goes to the people on the list.
>
> The other two alerts are for organizations with an Enterprise Agreement. That is a large contract with Microsoft.
>
> A credit alert tells you when your prepaid money is running out. Microsoft calls that money Azure Prepayment. Credit alerts are sent automatically when 90 percent, and then 100 percent, of it is used.
>
> A department spending quota alert goes to department owners. A quota is the amount a department is allowed to spend. The alert tells them when the department reaches a set part of its quota, such as 50 or 75 percent.

### Budgets

**Say:**

> A budget is a spending limit that you set. You can set a budget for a subscription, a resource group, a type of service, and more. Each budget has an alert level. When spending reaches that level, the alert goes out.
>
> Here is the part people often get wrong. A budget does not stop spending by itself. It warns you. Think of a spending alert on a bank card. It tells you when you are close. It does not lock the card.
>
> If you want Azure to take action, you connect the budget to automation. For example, shut down test servers when spending reaches a set level.

**Exam tip:** "See what we spent" means cost analysis. "Warn us" means a budget alert. "Stop resources automatically" means a budget plus automation. A budget alone only warns.

**Ask:** Contoso set a $1,000 budget on the test subscription. Spending reaches $1,000. Do the test servers stop?

**Answer:** Only if Contoso set up automation. The budget sends an alert. By itself, it does not stop anything.

**Say:**

> Cost analysis can show costs by subscription or resource group. But the finance director wants costs by department, by project, and by owner. Azure does not know your departments. You have to tell it. That is what tags are for.

---

## 0:49 — 5. Tags

**Learn unit:** [Describe the purpose of tags](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/7-describe-purpose-of-tags)

**Do:** Show slide 7.

**Move on when:** students can say what a tag is, give two reasons to use one, and say that tags are not inherited.

**Say:**

> You already know two ways to organize resources: subscriptions and resource groups. Tags are a third way.
>
> A tag is a label you add to a resource. It is extra information about the resource. Microsoft calls this metadata. Each tag has a name and a value. A resource can have more than one tag.
>
> A good starter set has four tags: Environment, Owner, CostCenter, and Workload. A workload is the app or job the resource belongs to.

**Board:**

```text
Name          Value
Environment   Production
Owner         Sam Lee
CostCenter    4410
Workload      PatientPortal
```

**Say:**

> Microsoft lists six reasons to use tags.
>
> - Resource management. Find the resources for a team, an owner, an environment, or a workload.
> - Cost management. Report costs by cost center, track budgets, and forecast costs.
> - Operations. Mark how critical a resource is. This helps you set service-level agreements, or SLAs. An SLA is a promise to your users about uptime or performance.
> - Security. Label data by security level, such as public or confidential.
> - Governance and compliance. Mark resources that must meet a standard, such as the ISO 27001 security standard. You can also make an owner tag required on every resource.
> - Automation. Tools such as Azure DevOps can find tagged resources and run tasks on them.
>
> You can add, change, or remove tags in the Azure portal, with PowerShell or the Azure CLI, in Azure Resource Manager templates, or with the REST API.
>
> Two rules for the exam.
>
> First, tags are not inherited. If you tag a resource group, the resources inside it do not get that tag automatically.
>
> Second, Azure Policy can enforce tags. It can require a tag on new resources. It can also add a tag back if someone removes it. We cover Azure Policy next session.
>
> Also, not every resource needs every tag. For example, you might add an Impact tag only to mission-critical resources. Any resource without that tag is treated as not mission-critical.
>
> Tags are only labels. A tag does not control who can open a resource. That is role-based access control, from last session. A tag does not stop someone from deleting a resource. That is a resource lock, which we cover next session. And a tag does not change the price. It helps you report on the price.

**Exam tip:** "Report costs by department" or "by cost center" means tags. "Tags are inherited from the resource group" is false. "Require a tag" means Azure Policy.

**Ask:** Contoso tags a resource group with CostCenter 4410. Next week, someone creates a virtual machine in that group. Does the virtual machine have the tag?

**Answer:** No. Tags are not inherited. Tag the virtual machine too, or use Azure Policy to add it.

**Say:**

> We know what costs money, how to estimate it, how to watch it, and how to label it. One question is left. How can Contoso pay less for the same work?

---

## 0:56 — 6. Ways to pay less

**Learn unit:** [Describe cost optimization options in Azure](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/7a-describe-cost-optimization-options)

**Move on when:** students can choose a reservation, a savings plan, or Spot from a short description.

**Do:** Ask this question before you show slide 2. Let the room answer first.

**Ask:** From Session 2: what is the difference between a reservation and a savings plan?

**Answer:** A reservation commits to a specific resource. A savings plan commits to an amount you spend per hour on compute.

**Do:** Now show slide 2.

**Say:**

> Pay-as-you-go is the default. It is also called on-demand. There is no commitment. Azure has three ways to pay less.
>
> Reservations. You commit to a specific resource for one or three years. Azure gives you a lower price on matching usage. This is best for steady, predictable workloads.
>
> Azure savings plan for compute. You commit to spend a fixed amount per hour on compute, for one or three years. For example, five dollars an hour. You are not locked to one type of virtual machine. The savings apply across eligible compute services. This is best when usage is steady, but you need flexibility.
>
> Spot Virtual Machines. Azure sells its spare capacity at a lower price. Spare capacity means computing power Azure is not using right now. But Azure can take it back when it needs it. When that happens, your work is interrupted. Microsoft calls this eviction. Spot is best for work that can stop and start again, when the lowest price matters most.

**Board:**

```text
Reservation    Commit to a specific RESOURCE    1 or 3 years     Steady and predictable
Savings plan   Commit to SPENDING per hour      1 or 3 years     Steady, but flexible
Spot           Spare capacity, lower price      Can be evicted   Work that can restart
Pay-as-you-go  No commitment                    The default      Use is unknown or changing
```

**Say:**

> An easy way to remember the first two. Reservation and resource both start with R. Savings plan and spending both start with S.
>
> Microsoft gives three examples. A production database that runs 24 hours a day, 7 days a week, fits a reservation. A mix of web apps and APIs that move between compute services fits a savings plan. Large batch jobs, such as rendering video, or test jobs that can restart, fit Spot.
>
> Review these choices over time. A job that started on Spot may become business-critical. Then it should move off Spot. A workload that becomes steady may save money by moving from pay-as-you-go to a reservation or a savings plan.

**Exam tip:** If the question says the work must not be interrupted, the answer is not Spot. If it says "flexible" or "across compute services," think savings plan. If it says "the same resource for one or three years," think reservation.

**Ask (quick round):** Read each situation. The class names the option.

| Situation | Answer |
| --- | --- |
| Contoso's patient database runs all day, every day, on the same size of server for three years. | Reservation |
| Contoso converts X-ray images overnight. If the job stops, it can start again later. They want the lowest price. | Spot |
| Contoso's compute spending is steady, but next year some apps move from virtual machines to other compute services. | Savings plan for compute |
| A brand-new project. Nobody knows how much it will run yet. | Pay-as-you-go |

**Say:**

> That is the whole module. Now you will use the pricing calculator yourself.

---

## 1:05 — Lab (30 minutes)

**Do:** Show slide 8. Open the [Session 8 lab](../../labs/session-08-lab.md). Parts A and B need only a browser. Part C is optional and needs a subscription.

**Do:** Before they start, name the second region for step 5. Pick one on a different continent from the first.

**Say:**

> For the next 30 minutes, you will price three resources, move them to another region, and price them again. Then you will write four tags, and the business question each tag answers. You do not need to sign in to Azure for this.

**Do:** At about 1:30, ask the two lab questions out loud.

**Ask:** Which cost factor did changing the region show?

**Answer:** Geography.

**Ask:** Which pricing model did the calculator use?

**Answer:** Pay-as-you-go, unless you picked a reservation or a savings plan.

**Do:** If a student writes a tag that "stops the server from being deleted," correct it. That is a resource lock, next session. If someone does Part C, the goal is a budget alert. An empty cost analysis on a new subscription is a fine result.

---

## 1:35 — Quiz (15 minutes)

**Do:** Hand out the [Session 8 quiz](../../quizzes/session-08-quiz.md). The target is 80 percent. At 1:47, stop. Review only the questions that two or more people missed.

**Say:**

> Quiz time. Twelve questions, 12 minutes. Three questions review earlier sessions. Work on your own.

**Do:** Question 4 is where people look for a TCO calculator answer. If it comes up in the review, say it is retired and move on. You cover it in the wrap-up.

---

## 1:50 — Wrap-up and summary

**Learn unit:** [Summary](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/9-summary)

**Do:** Show slide 5.

**Say:**

> One warning before you study at home. Older videos, books, and practice tests talk about two calculators: the pricing calculator and the Total Cost of Ownership calculator, or TCO calculator. Microsoft has retired the TCO calculator. The current exam objective is the pricing calculator only. If a practice test asks about the TCO calculator, that practice test is out of date.

**Do:** Ask whether anyone has seen the TCO calculator in their study material. Note the answer in the [session log](../../operations/session-log.md).

**Say:**

> Here is today in five points.
>
> 1. Cost depends on resource type, consumption, maintenance, geography, subscription type, and Azure Marketplace.
> 2. The pricing calculator estimates cost before you build. It creates nothing and charges nothing.
> 3. Cost Management shows what you actually spend. Budgets and alerts warn you. A budget alone does not stop spending.
> 4. Tags are name and value labels for organizing and reporting. They are not inherited. Azure Policy can require them.
> 5. To pay less, use a reservation for steady work, a savings plan for steady but flexible compute, and Spot for work that can be interrupted.
>
> Homework: finish the Microsoft Learn module, Describe cost management in Azure. Take the module assessment at the end.
>
> Next session is governance. You will learn Azure Policy, resource locks, and Microsoft Purview. You will also see why a tag is not a lock.

**Do:** Students take the module assessment on their own. Do not show its questions in class.

---

# Exam review

## Ten things to know for the exam

1. In the cloud, you pay for what you use. Six factors change the cost: resource type, consumption, maintenance, geography, subscription type, and Azure Marketplace.
2. Deleting a virtual machine may leave its disk and network resources behind. They keep costing money until you delete them.
3. The same resource can cost a different amount in a different region.
4. A billing zone is a group of regions used to price data transfer. It is not an availability zone. Some inbound data is free. Outbound data is charged by billing zone.
5. A Marketplace product can add a vendor charge on top of the Azure charge. The vendor sets that price.
6. The pricing calculator estimates cost before you build. It creates nothing and charges nothing. The TCO calculator is retired.
7. Cost Management shows what you actually spend. Cost analysis breaks it down by subscription, resource group, region, service, or resource.
8. There are three cost alert types: budget, credit, and department spending quota. A budget warns you. It does not stop spending unless you add automation.
9. Tags are name and value pairs. They are not inherited. Azure Policy can require tags and add removed tags back.
10. A reservation commits to a specific resource. A savings plan commits to an hourly amount of compute spending. Spot is the cheapest, but Azure can evict it. Pay-as-you-go has no commitment.

## Clue words

| If the question says... | Think... |
| --- | --- |
| "Estimate," "before we deploy," "compare regions before we build" | Pricing calculator |
| "What did we spend," "where is the money going," "cost trend" | Cost analysis in Cost Management |
| "Notify us," "warn us at 80 percent" | Budget alert |
| "Enterprise Agreement," "Azure Prepayment," "90 percent and 100 percent" | Credit alert |
| "Department," "quota" | Department spending quota alert |
| "Shut down resources automatically at a set amount" | A budget connected to automation |
| "Report by cost center," "by department," "by owner" | Tags |
| "Require a tag," "put a removed tag back" | Azure Policy |
| "Cost of moving data out of Azure" | Outbound data transfer, priced by billing zone |
| "Deleted the virtual machine but still charged" | Leftover resources (maintenance) |
| "Third-party vendor," "software already installed" | Azure Marketplace |
| "Steady," "same resource," "one or three years" | Reservation |
| "Hourly amount," "flexible across compute services" | Azure savings plan for compute |
| "Can be interrupted," "batch job," "lowest cost" | Spot Virtual Machines |
| "No commitment," "use is unknown" | Pay-as-you-go |
| "TCO calculator" | Retired. Use the pricing calculator |

## Practice questions

**Do:** Use these if the lab ends early, or give them to students to study at home. They are new questions. They are not from the Session 8 quiz or Microsoft's module assessment. Read the question, wait, then read the answer.

1. Contoso Health sends patient reports every night from a region in Europe to clinics in Asia. Which cost factor is this?

   **Answer:** Geography. Moving data from Europe to Asia costs more than moving it within Europe.

2. Contoso buys a firewall from another company in Azure Marketplace. Who sets the price of the firewall software?

   **Answer:** The vendor. Contoso may pay for the Azure resources and for the vendor's product.

3. A new employee signs up for the Azure free trial. Name one thing it includes.

   **Answer:** Any one of these: some products free for 12 months, a credit for the first 30 days, or more than 25 always-free products.

4. Contoso's bill jumped right after Tuesday's deployment. Where should they look first?

   **Answer:** Cost analysis in Microsoft Cost Management.

5. A manager needs a monthly cost number to get a project approved. Nothing is built yet. Which tool?

   **Answer:** The pricing calculator.

6. An organization with an Enterprise Agreement gets an email that 90 percent of its Azure Prepayment is used. Which type of alert is this?

   **Answer:** A credit alert.

7. Someone removed the Owner tag from a production server. Contoso wants Azure to add it back automatically. What can do that?

   **Answer:** Azure Policy.

8. Contoso puts an Impact tag only on mission-critical servers. Is it a problem that the other servers do not have it?

   **Answer:** No. Not every resource needs every tag.

9. A manager says, "Tag the storage account Confidential so nobody else can open it." What is wrong with that plan?

   **Answer:** A tag is only a label. To control who can open the storage account, use role-based access control.

10. Contoso runs test jobs on Spot because they can restart. Later, the same jobs must finish on time every day for a clinic report. What should Contoso change?

    **Answer:** Move the jobs off Spot to an option that will not be interrupted, such as pay-as-you-go, a reservation, or a savings plan.

---

# Supplemental instructor context

**Do:** Use this only if a student asks. It is not in the Microsoft module. Say that you are going outside the module, answer in a sentence or two, then come back.

**"My free account stopped when the credit ran out. Isn't that a budget?"** No. That is a separate subscription feature, also called a spending limit. It is on by default for the free account and for some subscriptions that include credit. When the credit is used up, the deployed services are turned off for the rest of the billing period. Virtual machines are stopped, and storage becomes read-only. Pay-as-you-go subscriptions do not have a spending limit. A budget is different. It warns. Source: [Azure spending limit](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/spending-limit).

**"If a savings plan is flexible, why would anyone pick a reservation?"** Microsoft says reservations give deeper discounts, but they work best when usage is stable. A savings plan is more flexible. If you use less than the hourly amount, the unused part is lost for that hour. Use above the hourly amount is billed at pay-as-you-go rates. Microsoft now also offers a savings plan for databases. The module covers the savings plan for compute. Source: [What are savings plans?](https://learn.microsoft.com/en-us/azure/cost-management-billing/savings-plan/savings-plan-compute-overview)

**"What about Azure Advisor?"** Advisor also suggests ways to save money. It is taught in Session 11. On quiz question 5 it is a wrong answer, because Advisor does not estimate a design you have not built yet.

**Why older material shows two calculators.** Older versions of the exam objective asked students to compare the pricing calculator with the TCO calculator. The current Learn unit says the TCO calculator is retired. Entry V6 in [the source validation log](../../sources/source-validation-log.md) records this.

---

## Sources

Checked 22 October 2026. This script follows these units. It does not copy them.

- [Module: Describe cost management in Azure](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/)
- [Introduction](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/1-introduction)
- [Describe factors that can affect costs in Azure](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/2-describe-factors-affect-costs-azure)
- [Explore the pricing calculator](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/3-compare-pricing-total-cost-of-ownership-calculators)
- [Describe the Microsoft Cost Management tool](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/6-describe-azure-tool)
- [Describe the purpose of tags](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/7-describe-purpose-of-tags)
- [Describe cost optimization options in Azure](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/7a-describe-cost-optimization-options)
- [Summary](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/9-summary)

Supplemental only: [Azure pricing calculator](https://azure.microsoft.com/en-us/pricing/calculator/) · [Azure spending limit](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/spending-limit) · [What are savings plans?](https://learn.microsoft.com/en-us/azure/cost-management-billing/savings-plan/savings-plan-compute-overview)
