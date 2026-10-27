<!-- Copyright (c) 2026 Kevin Robinson. All Rights Reserved. -->

# Session 9 instructor script — Describe features and tools in Azure for governance and compliance

**Microsoft Learn module:** [Describe features and tools in Azure for governance and compliance](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/)

**Checked against the live module:** 27 October 2026

**Other Session 9 files:** [instructor notes](../session-09-instructor-notes.md) · [slides](../session-09-slides.md) · [lab](../../labs/session-09-lab.md) · [quiz](../../quizzes/session-09-quiz.md) · [warm-up](../../quizzes/warm-ups.md)

## How to read this script

| Label | What to do |
| --- | --- |
| **Say** | Read it out loud, word for word. |
| **Ask** | Ask the class. Wait for answers. Then read the **Answer** out loud. |
| **Exam tip** | Read it out loud. |
| **Board** | Write it on the whiteboard. |
| **Do** | For you only. Do not read it out loud. |

The script follows Microsoft's unit order. Your instructor notes teach Policy first. Microsoft starts with Purview. The total time is the same. Policy still gets the longest block, because the exam mixes Policy, RBAC, and locks the most.

## Microsoft's units, in order

1. [Introduction](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/1-introduction)
2. [Describe the purpose of Microsoft Purview](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/2-describe-purpose-microsoft-purview)
3. [Describe the purpose of Azure Policy](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/3-describe-purpose-azure-policy)
4. [Describe the purpose of resource locks](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/4-describe-purpose-resource-locks)
5. [Describe the purpose of the Service Trust portal](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/6-describe-purpose-service-trust-portal)
6. Module assessment. Students take it on Learn after class. Do not show it in class.
7. [Summary](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/8-summary)

## Microsoft's learning objectives

- Describe the purpose of Microsoft Purview.
- Describe the purpose of Azure Policy.
- Describe the purpose of resource locks.
- Describe the purpose of the Service Trust portal.

The summary also says you should be able to explain governance guardrails for AI-assisted admin work. That idea is in the Policy unit and the summary. Teach it in one short block. Do not put it on the quiz.

## What this course scores

These three are on the exam list for this course:

- Microsoft Purview
- Azure Policy
- Resource locks

The Service Trust portal is in the module. It is not on the exam list. Teach it for one minute so nobody confuses it with Purview. Do not quiz it.

## Two-hour plan

| Time | Block | Slide |
| --- | --- | --- |
| 0:00–0:10 | Warm-up | 1 |
| 0:10–0:13 | 1. Introduction | 1 |
| 0:13–0:22 | 2. Microsoft Purview | 5 |
| 0:22–0:42 | 3. Azure Policy | 2, 3 |
| 0:42–0:55 | 4. Resource locks | 4 |
| 0:55–1:00 | 5. Service Trust portal, and one AI sentence | 6 |
| 1:00–1:30 | Lab | 8 |
| 1:30–1:45 | Quiz | 8 |
| 1:45–2:00 | Wrap-up: five tools | 7 |

**If you fall behind:**

- At 0:20, if you are still on Purview, skip the Microsoft 365 list. Keep the three Purview jobs: find data, classify sensitive data, show lineage.
- At 0:40, if you have not finished Policy, keep audit versus deny, Policy versus RBAC, and inheritance. Skip the Azure DevOps sentence and the Copilot sentence until the end.
- At 0:52, if locks are unfinished, keep Delete versus ReadOnly, inheritance, and "even an Owner must remove the lock."
- Cut the Service Trust portal before you cut the lock demo or the quiz.
- Never cut the five-tool table at the end.

## Before class

- Print or open the warm-up, the quiz, and both answer keys.
- Open a built-in Azure Policy definition you can show on screen for the no-cost lab path.
- Rehearse a Delete lock on a resource group: add the lock, try to delete, read the error, remove the lock, delete the group.

## Today's client

Contoso Health is the made-up clinic company from earlier sessions. Today the compliance officer has four requests. Each request is one part of the lesson.

---

## 0:00 — Warm-up

**Do:** Use the Session 9 set in [warm-ups.md](../../quizzes/warm-ups.md). Do not project the answers.

**Say:**

> Before we talk about governance, I need six answers from earlier sessions. Work with a neighbor if you want. You have about eight minutes.

**Do:** At about 0:08, take answers out loud. Accept the idea, not the exact wording. If two people miss the same one, re-teach that one fact in one sentence and move on.

**Answers to listen for:**

1. Assign the policy at the management group so every subscription under it inherits it.
2. No. Tags are not inherited. Put them where you need them, or use Azure Policy to require them.
3. Any four of: resource type and settings, consumption, leftover resources, geography, billing zones for data transfer, subscription type, Marketplace charges.
4. Role assignments grant permissions, and they add together. Read plus write means both.
5. Microsoft Cost Management with cost analysis to see spend. Budgets with budget alerts to get a warning.
6. Defender for Cloud gives a secure score, security recommendations, security alerts, and threat protection. Plain Azure Policy does not.

**Say:**

> Hold the first answer. A rule at a management group reaches every subscription under it. Today we learn what those rules are, and how they are different from who may click Delete.

---

## 0:10 — 1. Introduction

**Learn unit:** [Introduction](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/1-introduction)

**Do:** Show slide 1.

**Say:**

> Today is about governance and compliance. Governance means Contoso stays in control of its Azure environment. Compliance means Contoso meets its own rules and outside rules, such as a healthcare rule about patient data.
>
> Contoso's compliance officer has four requests.

**Board:**

```text
Request                                         Today's topic
Know where our patient data lives               Microsoft Purview
Stop VMs outside our two regions                Azure Policy
Stop anyone from deleting production by accident Resource locks
Read Microsoft's own compliance paperwork       Service Trust portal
```

**Say:**

> These four are today's four topics, in the same order as Microsoft's module. The first three can be on the exam. The fourth is for awareness only.
>
> You already know two other tools from earlier sessions. RBAC answers who may do an action. Tags answer how we label a resource for reports. Keep those on the table. Today we separate all five.

**Exam tip:** The exam mixes these tools. Read the question. Is it about a person, a resource shape, a delete, a label, or the data itself?

---

## 0:13 — 2. Microsoft Purview

**Learn unit:** [Describe the purpose of Microsoft Purview](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/2-describe-purpose-microsoft-purview)

**Do:** Show slide 5.

**Move on when:** students can say Purview is about data governance, risk, and compliance, and they can name discovery, classification, and lineage.

**Say:**

> Microsoft Purview is a family of tools for data governance, risk, and compliance. Its job is to give Contoso one view of its data.
>
> Contoso's data is not only in Azure. Some is on-premises, at headquarters. Some is in other clouds. Some is in software as a service, such as Microsoft 365. Purview brings insights about all of that together.
>
> Microsoft names three things Purview helps you keep current:

**Board:**

```text
Microsoft Purview
1. Automated data discovery     find the data
2. Sensitive data classification mark what is sensitive
3. End-to-end data lineage      see where data came from and where it went
```

**Say:**

> Discovery means Purview finds the data for you. Classification means it labels sensitive data, such as patient records. Lineage means it shows the path of the data, from where it started to where it is used.
>
> Purview has two main solution areas.
>
> First, risk and compliance. Microsoft 365 is a core part of this. Teams, OneDrive, and Exchange are examples. Purview helps Contoso protect sensitive data across clouds, apps, and devices. It helps Contoso find data risks and manage regulatory compliance. It also helps Contoso get started with regulatory compliance.
>
> Second, unified data governance. This is the map of Contoso's whole data estate. It can cover data in Azure, in SQL and Hive databases, on local servers, and in other clouds such as Amazon S3.
>
> With unified data governance, Contoso can:
>
> - Build an up-to-date map of the data estate, with classification and lineage.
> - Find where sensitive data is stored.
> - Give data users a safe place to find useful data.
> - See how data is stored and used.
> - Manage access to that data in a secure way, at scale.
>
> That is as far as we go for this exam. We will not open the Purview portal today. We will not walk through Microsoft Fabric or a product catalog. If Contoso asks "where is our sensitive data, and can we prove it?", think Purview. If Contoso asks "may this storage account be created in this region?", that is Azure Policy, not Purview.

**Exam tip:** Purview is about the data. Policy is about how an Azure resource is set up. A lock is about delete or change. Do not answer Purview for a region rule or a delete rule.

**Ask:** Contoso wants to find files that contain personal patient data across Azure and Microsoft 365. Which tool?

**Answer:** Microsoft Purview.

**Ask:** Contoso wants every new storage account to land in only two regions. Is that Purview?

**Answer:** No. That is Azure Policy. We will cover that next.

**Say:**

> Contoso still needs rules about what Azure resources may look like. That is Azure Policy.

---

## 0:22 — 3. Azure Policy

**Learn unit:** [Describe the purpose of Azure Policy](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/3-describe-purpose-azure-policy)

**Do:** Show slide 2.

**Move on when:** students can say definition, initiative, assignment, inheritance, audit versus deny, and Policy versus RBAC.

**Say:**

> How does Contoso make sure its resources stay compliant? How does Contoso get a warning if a resource's settings change?
>
> Azure Policy is the Azure service that lets you create, assign, and manage policies. Those policies control or audit your resources. They enforce rules across resource settings so those settings stay compliant with Contoso's standards.
>
> Hear the two verbs. Control. Audit. Control means Policy can stop a bad create or change. Audit means Policy can report a problem and still leave the resource alone.

### Definitions, initiatives, and assignment

**Say:**

> Azure Policy lets you define one policy, or a group of related policies. A group of related policies is called an initiative.
>
> Azure Policy evaluates your resources. It highlights resources that are not compliant. It can also stop noncompliant resources from being created.
>
> You assign a policy at a scope. A scope can be a management group, a subscription, a resource group, or even one resource. Policies are inherited. If you assign a policy at a high level, it applies to everything under that level. If you assign a policy on a resource group, every resource in that group gets the policy.

**Board:**

```text
Azure Policy words
Definition     one rule
Initiative     a group of related rules
Assignment     the rule attached to a scope
Scope          management group, subscription, resource group, or resource
Inheritance    children get the parent's assignment
Compliance     compliant or not compliant
```

**Say:**

> After you assign a policy, you read the compliance state. Compliant means the resource meets the rule. Not compliant means it does not.
>
> Azure Policy comes with built-in policy and initiative definitions for Storage, Networking, Compute, Security Center, and Monitoring.
>
> Here is a concrete picture. Contoso defines a policy that allows only certain virtual machine sizes. That policy runs when someone creates a new virtual machine. It also runs when someone resizes an existing virtual machine. Azure Policy also evaluates the virtual machines Contoso already has, including ones created before the policy existed.
>
> In some cases, Azure Policy can fix a noncompliant resource for you. Microsoft calls this remediation. For example, Contoso can require an AppName tag, and Azure Policy can add the tag when it is missing. Contoso still stays in control, because a resource can be marked as an exception to a policy.
>
> Azure Policy also works with Azure DevOps. It can apply rules in the build and release pipeline, before and after Contoso deploys an application. Recognize that sentence. Do not configure a pipeline today.

### Audit versus deny

**Do:** Show slide 3.

**Say:**

> I want two words you will hear on the exam and in the lab: audit and deny.
>
> Audit means Policy reports the problem. The resource stays. Contoso can see it on a compliance report.
>
> Deny means Policy blocks the create or update that would break the rule. The action fails.
>
> There are other effects, such as modify or append. For this class, master audit and deny. If a question only says "report" or "prevent," map those to audit and deny.

**Board:**

```text
Audit   report only. The resource can still exist.
Deny    block the create or update.
```

### Policy is not RBAC

**Say:**

> This is the most common mix-up in the whole course.
>
> Azure RBAC answers: may this person do this action?
>
> Azure Policy answers: may this resource look like this?
>
> Write Contoso's example with me.

**Board:**

```text
Contributor role: Sam may create virtual machines.
Deny policy:      VMs only in East US and West US.

Sam tries to create a VM in North Europe.
RBAC says yes. Policy says no.
The create fails.
```

**Say:**

> Sam still has permission to create virtual machines. The resource shape is illegal. Permission and shape are two different questions. Policy does not replace RBAC. RBAC does not replace Policy.

### AI-assisted changes

**Say:**

> One more sentence from the module. If Contoso's team uses Copilot recommendations, or other AI helpers that suggest changes, Azure Policy still enforces Contoso's standards. Contoso can still require allowed locations, required tags, approved resource sizes, and security baseline controls. The AI suggestion does not get a free pass.

### Initiatives

**Say:**

> Back to initiatives. An initiative groups related policy definitions so Contoso can track compliance for a larger goal with one assignment.
>
> Microsoft's example is an initiative named Enable Monitoring in Azure Security Center. Its goal is to monitor security recommendations for Azure resource types.
>
> Under that initiative are policy definitions such as:
>
> - Monitor unencrypted SQL databases.
> - Monitor operating system vulnerabilities.
> - Monitor missing endpoint protection.
>
> That one initiative contains more than 100 separate policy definitions. Contoso assigns the initiative once. Contoso does not assign those 100 definitions one by one.

**Exam tip:** "Group of related policies" means initiative. "Report only" means audit. "Must fail if created outside two regions" means deny. "Who may restart the VM" means RBAC, not Policy.

**Ask:** Contoso wants a report of storage accounts that are not encrypted. Contoso does not want to block those accounts today. Audit or deny?

**Answer:** Audit.

**Ask:** Contoso wants virtual machines outside two regions to fail at create time. Audit or deny?

**Answer:** Deny.

**Ask:** Contoso assigns a VM size policy on a resource group. An old VM in that group was created last year. Does Policy care?

**Answer:** Yes. Policy evaluates existing resources too, not only new ones.

**Say:**

> Policy can stop a bad shape. It does not stop a tired Owner from deleting a production resource group. That is a resource lock.

---

## 0:42 — 4. Resource locks

**Learn unit:** [Describe the purpose of resource locks](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/4-describe-purpose-resource-locks)

**Do:** Show slide 4.

**Move on when:** students can name Delete and ReadOnly, say locks are inherited, and say even an Owner must remove the lock first.

**Say:**

> A resource lock prevents resources from being deleted or changed by accident.
>
> Even with Azure RBAC in place, someone with the right access can still delete a critical resource. A lock is the extra guardrail. Depending on the type of lock, it stops delete, or it stops update and delete.
>
> You can apply a lock to one resource, to a resource group, or to a whole subscription. Locks are inherited. If you put a lock on a resource group, every resource in that group gets the lock too.

### Two types of locks

**Say:**

> There are two types.
>
> Delete. In the Azure portal, the name is Delete. In the API, and in some command-line tools, the name is CanNotDelete. Same lock. Two names. Write both.
>
> With a Delete lock, authorized users can still read and change the resource. They cannot delete it.
>
> ReadOnly. Authorized users can read the resource. They cannot delete it, and they cannot update it. Applying this lock is like giving every authorized user only the Reader permissions on that resource.

**Board:**

```text
Lock types
Delete / CanNotDelete   read and change: yes. delete: no.
ReadOnly                read: yes. change: no. delete: no.
```

**Say:**

> You manage locks in the Azure portal, with PowerShell, with the Azure CLI, or with an Azure Resource Manager template. In the portal, open the resource, go to Settings, and open Locks.

### Even an Owner must remove the lock

**Say:**

> A lock does not mean the resource can never change. It means change takes two steps.
>
> First, remove the lock. Second, do the action your role allows.
>
> Resource locks apply no matter what RBAC role you have. Even if you are an Owner, you must remove the lock before you can do the blocked action.
>
> So a lock protects Contoso from an accident. It does not permanently block a person who is allowed to remove locks and then delete. The point is the extra step.

**Exam tip:** "Can update, must not delete" means a Delete lock, also called CanNotDelete. "Cannot update or delete" means ReadOnly. "Owner still blocked until the lock is removed" is true for both.

**Ask:** Contoso's production resource group must stay. Engineers must still update the resources inside it. Which lock?

**Answer:** A Delete lock on the resource group. ReadOnly would also block the updates.

**Ask:** You are an Owner. A Delete lock is on the resource. Can you delete it right now?

**Answer:** No. Remove the lock first. Then delete, if your role still allows it.

**Ask:** Contoso puts a Delete lock on a resource group. Does a storage account inside that group get the lock?

**Answer:** Yes. Locks are inherited.

**Say:**

> One short stop left in the module. Then you will practice.

---

## 0:55 — 5. Service Trust portal, and one AI sentence

**Learn unit:** [Describe the purpose of the Service Trust portal](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/6-describe-purpose-service-trust-portal)

**Do:** Show slide 6. Keep this to about three minutes.

**Say:**

> The Microsoft Service Trust portal is a website where Microsoft publishes information about Microsoft's own security, privacy, and compliance practices. The address is servicetrust.microsoft.com.
>
> Think of it as Microsoft's paperwork about Microsoft. Audit reports. Control descriptions. Compliance documents for Microsoft cloud services and customer data.
>
> To open some of those documents, you sign in with a work or school Microsoft Entra account. You also accept Microsoft's non-disclosure agreement for compliance materials.
>
> On the site you will see My Library, where you can pin documents you care about, and All Documents, which is the full list. Microsoft keeps reports available for at least 12 months after publishing, or until a newer version replaces them.
>
> This portal is not on our scored objective list. We will not quiz it. Know it exists so you do not call it Purview. Purview is about Contoso's data. The Service Trust portal is about Microsoft's own compliance story.

**Do:** Show slide 7 briefly, or leave it for the wrap.

**Say:**

> One sentence from the module summary, then we lab. When Contoso uses Copilot or other AI helpers to change Azure, the same guardrails still apply. RBAC, Azure Policy, resource locks, and auditing still decide what is allowed.

---

## 1:00 — Lab (30 minutes)

**Do:** Show slide 8. Open the [Session 9 lab](../../labs/session-09-lab.md).

**Say:**

> For the next 30 minutes you will do three things. First, match nine business needs to the right tool. Second, read a policy. Third, put a Delete lock on a resource group and try to delete it. The failed delete is the lesson. Then remove the lock and delete the group for real. Do not leave a lock behind for next week.

**Do:**

- Part A is on paper for everyone.
- For Part B, name a built-in audit policy if the room can assign policy. Do not choose Deny on a shared subscription.
- If there is no subscription, use the no-cost path: show a built-in definition on the projector. Students write the goal in one line and whether the effect is audit or deny. For Part C, you add the lock and try the delete on the projector. Students write the error sentence and the API name CanNotDelete next to the portal word Delete.

**Do:** At about 1:25, review Part A out loud using the instructor key.

| # | Answer |
| --- | --- |
| 1 | RBAC |
| 2 | Policy (deny) |
| 3 | Policy (audit) |
| 4 | Lock (Delete / CanNotDelete) |
| 5 | Tag |
| 6 | Purview |
| 7 | Lock (Delete). ReadOnly would also block changes. |
| 8 | RBAC (Reader) |
| 9 | Tag |

**Say:**

> Notice items 7 and 8. "May change, must not delete" is a Delete lock. "May view, must not modify" is RBAC Reader. Same feeling. Different tools.

---

## 1:30 — Quiz (15 minutes)

**Do:** Hand out the [Session 9 quiz](../../quizzes/session-09-quiz.md). Target 80 percent. At about 1:42, stop. Review only the questions that two or more people missed.

**Say:**

> Quiz time. Twelve questions, about 12 minutes. Three questions review earlier sessions. Work on your own.

**Do:** If the room mixes Policy, RBAC, and locks in the review, ask this closing question:

**Ask:** What is the one thing that stops an Owner from deleting a resource right now?

**Answer:** A resource lock. Not RBAC. Not Policy. The Owner must remove the lock first.

---

## 1:45 — Wrap-up and summary

**Learn unit:** [Summary](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/8-summary)

**Do:** Show slide 7. Books closed. Rebuild the table from the room before you show the finished version.

**Say:**

> Close your notes. Rebuild the five-tool table with me. I will name the job. You name the tool.

**Ask (quick round):**

| Job | Answer |
| --- | --- |
| Who may do an action? | RBAC |
| What may a resource look like? | Policy |
| Block delete or block change, even for an Owner | Lock |
| Describe a resource so you can report on it | Tag |
| Govern the data itself | Purview |

**Board:** leave the finished table up.

```text
RBAC      Who may do an action
Policy    What a resource may look like
Lock      Block delete or change, even for an Owner
Tag       Label a resource for reports
Purview   Govern the data itself
```

**Say:**

> Two more confusions to lock down before you leave.
>
> First, Policy versus RBAC versus locks. Person. Shape. Accident protection.
>
> Second, where you assign a policy. Assign it at a management group, and every subscription under that group inherits it. Assign it at one subscription, and only that subscription and its children get it. Broader scope means more inheritance. Same tools.
>
> Here is today in four points.
>
> 1. Microsoft Purview gives Contoso one view of its data for governance, risk, and compliance. It finds data, classifies sensitive data, and shows lineage.
> 2. Azure Policy creates and assigns rules that audit or control resource settings. An initiative is a group of related policies. Policies inherit down. Audit reports. Deny blocks.
> 3. Resource locks stop accidental delete or change. Delete, also called CanNotDelete, allows change but not delete. ReadOnly allows read only. Even an Owner must remove the lock first.
> 4. The Service Trust portal is Microsoft's own compliance paperwork. It is not Purview, and we do not quiz it.
>
> Homework: finish the Microsoft Learn module, Describe features and tools in Azure for governance and compliance. Take the module assessment at the end.
>
> Next session is managing and deploying resources: the portal, Cloud Shell, the command-line tools, Azure Arc, and infrastructure as code.

**Do:** Students take the module assessment on their own. Do not show its questions in class.

---

# Exam review

## Ten things to know for the exam

1. Microsoft Purview is for data governance, risk, and compliance. It helps Contoso get one view of data across on-premises, multicloud, and software as a service.
2. Purview's three jobs to remember: automated data discovery, sensitive data classification, and end-to-end data lineage.
3. Azure Policy creates, assigns, and manages rules that control or audit resource configurations so they stay compliant.
4. An initiative is a group of related policy definitions, assigned and tracked together for a larger goal.
5. Policy assignments are inherited. Policy evaluates new resources and existing resources.
6. Audit reports noncompliance. Deny blocks the create or update. Policy can also fix some problems, such as adding a missing required tag. Resources can be marked as exceptions.
7. Policy is not RBAC. RBAC is who may act. Policy is what a resource may look like.
8. A Delete lock, also called CanNotDelete, allows read and change, but not delete. A ReadOnly lock allows read only.
9. Locks are inherited. Locks apply even to an Owner. The Owner must remove the lock before the blocked action.
10. The Service Trust portal is Microsoft's compliance information about Microsoft. It is context in this course, not a scored objective.

## Clue words

| If the question says... | Think... |
| --- | --- |
| "Where is sensitive data," "classify," "lineage," "data estate" | Microsoft Purview |
| "Resource configuration," "compliant," "allowed locations," "required tag" | Azure Policy |
| "Group of related policies," "larger compliance goal" | Initiative |
| "Report only," "do not block" | Audit |
| "Must fail," "prevent create" | Deny |
| "Who may restart," "who may delete," "Reader," "Contributor" | Azure RBAC |
| "Cannot be deleted by accident," "still allow updates" | Delete lock / CanNotDelete |
| "Cannot update or delete," "like Reader for everyone" | ReadOnly lock |
| "Even an Owner," "remove the lock first" | Resource locks apply regardless of RBAC |
| "One policy for all 20 subscriptions" | Assign at the management group |
| "Label for cost reports," "Owner tag," "CostCenter" | Tag |
| "Microsoft's audit reports about Microsoft" | Service Trust portal |
| "Copilot suggested a change" | Policy, RBAC, and locks still apply |

## Practice questions

**Do:** Use these if the lab ends early, or give them for home study. They are new. They are not from the Session 9 quiz or Microsoft's module assessment.

1. Contoso wants a map of where patient data lives in Azure, at headquarters, and in Microsoft 365. Which tool?

   **Answer:** Microsoft Purview.

2. Contoso wants every new virtual machine to fail if it is created outside East US and West US. Which tool, and audit or deny?

   **Answer:** Azure Policy, with deny.

3. Contoso wants a list of unencrypted storage accounts, but does not want to break the accounts today. Audit or deny?

   **Answer:** Audit.

4. Contoso assigns 80 related security monitoring policies as one package. What is that package called?

   **Answer:** An initiative.

5. Sam is a Contributor. A deny policy blocks VMs in North Europe. Sam tries to create one there. What happens?

   **Answer:** The create fails. RBAC allowed the action. Policy blocked the shape.

6. Contoso needs engineers to change production resources, but nobody may delete the resource group. Which lock?

   **Answer:** A Delete lock, also called CanNotDelete.

7. An Owner wants to delete a locked resource. What must happen first?

   **Answer:** Remove the lock. Locks apply even to Owners.

8. Contoso puts a ReadOnly lock on a storage account. Can an engineer upload a new file to it?

   **Answer:** No. ReadOnly blocks updates and deletes.

9. Contoso opens a website to download Microsoft's own compliance report for Azure. Is that Purview?

   **Answer:** No. That is the Service Trust portal.

10. A Copilot suggestion would create a virtual machine in a blocked region. Does Copilot bypass Azure Policy?

    **Answer:** No. Azure Policy still enforces the rule.

---

# Supplemental instructor context

**Do:** Use this only if a student asks. Say that you are going outside the module, answer in a sentence or two, then come back.

**Portal Delete versus API CanNotDelete.** Same lock. The portal label is Delete. The API and some CLI output say CanNotDelete. The lab asks students to write both so the error text does not look like a different feature. Source: [Lock resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources).

**Policy effects beyond audit and deny.** Azure Policy has more effects, such as modify, append, deployIfNotExists, and auditIfNotExists. This course quizzes audit and deny. Name the others only if a student asks, and say the exam focus here is report versus block.

**Management groups.** Assigning Policy at a management group is why management groups exist for governance. Students met management groups in Session 3. One sentence is enough today: broader scope, more inheritance.

**Defender for Cloud versus Policy.** Session 7 and the warm-up already said Defender for Cloud uses Azure Policy as part of how it evaluates resources. Defender gives a secure score, recommendations, and threat alerts. Policy alone is the configuration rule. Do not re-teach Defender today.

**Why Purview stays short.** Gap G7 in the objective map: Purview is a large product family. AZ-900 asks for the purpose. Discovery, classification, lineage, and the two solution areas are enough.

---

## Sources

Checked 27 October 2026. This script follows these units. It does not copy them.

- [Module: Describe features and tools in Azure for governance and compliance](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/)
- [Introduction](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/1-introduction)
- [Describe the purpose of Microsoft Purview](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/2-describe-purpose-microsoft-purview)
- [Describe the purpose of Azure Policy](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/3-describe-purpose-azure-policy)
- [Describe the purpose of resource locks](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/4-describe-purpose-resource-locks)
- [Describe the purpose of the Service Trust portal](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/6-describe-purpose-service-trust-portal)
- [Summary](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/8-summary)

Supplemental only: [Azure Policy overview](https://learn.microsoft.com/en-us/azure/governance/policy/overview) · [Lock resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources) · [Microsoft Purview](https://learn.microsoft.com/en-us/purview/purview) · [Service Trust Portal](https://servicetrust.microsoft.com/)
