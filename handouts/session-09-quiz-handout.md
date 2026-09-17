# Session 9 Quiz — Governance and Compliance

**Name:** <span class="blank"></span>  **Session:** <span class="blank"></span>

**Time:** 15 minutes · **Items:** 12 · **Target:** 80%

Answer every question. For *select all that apply*, mark every correct option. For
matching questions, write the matching term next to each numeral. For yes/no sets,
write yes or no next to each numeral. Your instructor reviews every answer in class
immediately afterward.

---

**1.** What is the purpose of Azure Policy?

- A. To control who can perform actions on Azure resources
- B. To create, assign, and manage rules that control or audit resource configurations so they stay compliant with your standards
- C. To prevent resources from being deleted
- D. To monitor application performance and availability

**2.** What is an Azure Policy initiative?

- A. A single policy rule applied to one resource
- B. A group of related policy definitions assigned and tracked together toward a larger compliance goal
- C. A role assignment that spans multiple subscriptions
- D. A cost budget with an alert threshold

**3.** You assign a policy at a resource group that restricts VM sizes. Which resources does it affect?

- A. Only resources created after the assignment
- B. Only resources explicitly added to the policy scope
- C. All resources in that resource group, including existing VMs, which are evaluated and monitored for compliance
- D. Nothing until the policy is assigned on each resource individually

**4.** Which statements about Azure Policy are correct? (Select all that apply.)

- A. Policy can prevent noncompliant resources from being created
- B. Policy assignments are inherited by resources within the assigned scope
- C. Policy can automatically remediate some noncompliant configurations, such as adding a missing required tag
- D. Policy replaces the need for Azure RBAC
- E. Resources can be marked as exceptions to a policy

**5.** A team must ensure a production resource group cannot be deleted by accident, while still allowing engineers to update the resources inside it. What should they apply?

- A. A ReadOnly lock on the resource group
- B. A Delete lock on the resource group
- C. The Reader role at resource group scope
- D. An Azure Policy denying all write operations

**6.** A ReadOnly lock is applied to a resource. What can authorized users do?

- A. Read, update, and delete the resource
- B. Read the resource, but not update or delete it
- C. Nothing; the resource becomes inaccessible
- D. Update the resource but not delete it

**7.** You are an Owner of a subscription and need to delete a resource that has a Delete lock applied. What must happen first?

- A. Nothing; Owner permissions override resource locks
- B. The lock must be removed, because locks apply regardless of RBAC permissions
- C. An Azure Policy exception must be created
- D. The resource must be moved to another resource group

**8.** What is the purpose of Microsoft Purview?

- A. To provide a unified view of your data estate for data governance, risk, and compliance, including automated discovery, sensitive data classification, and end-to-end lineage
- B. To detect and respond to security threats against virtual machines
- C. To estimate the cost of Azure resources before deployment
- D. To deploy Azure resources from declarative templates

**9.** Which requirement is the best fit for Microsoft Purview rather than for Azure Policy?

- A. Ensuring all new storage accounts are deployed only in approved regions
- B. Finding where sensitive data is stored across on-premises, multicloud, and SaaS data, and tracing its lineage
- C. Preventing accidental deletion of a production resource group
- D. Notifying the finance team when spend passes 80% of budget

**10.** An organization wants one policy to apply to all 20 of its subscriptions without assigning it 20 times. Where should the policy be assigned?

- A. On each resource group
- B. At the management group containing the subscriptions
- C. On the Microsoft Entra tenant only
- D. On a single representative subscription

**11.** Which tool answers the question "what is this user allowed to do in this subscription," as opposed to "is this resource configured correctly"?

- A. Azure Policy
- B. Azure RBAC
- C. Resource locks
- D. Microsoft Purview

**12.** A governance standard requires that every new resource carry an `Owner` tag, and that the tag be restored if someone removes it. What enforces this?

- A. A resource lock
- B. Azure Policy
- C. Microsoft Cost Management budgets
- D. Azure RBAC role assignment

<!-- pagebreak -->

## Answer sheet

| # | Your answer | # | Your answer |
| --- | --- | --- | --- |
| 1 |  | 7 |  |
| 2 |  | 8 |  |
| 3 |  | 9 |  |
| 4 |  | 10 |  |
| 5 |  | 11 |  |
| 6 |  | 12 |  |

**Score:** ____ / 12

**Objectives to review:** <span class="blank blank-wide"></span>
