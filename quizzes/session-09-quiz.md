# Session 9 Quiz — Governance and Compliance

**Time:** 15 minutes · **Items:** 12 · **Composition:** 9 new, 3 carry-forward (S3–S8)
**Objectives:** 3.2.1, 3.2.2, 3.2.3
**Carry-forward objectives:** 2.1.7, 2.4.5, 3.1.4
**Target:** 80%

Discrimination level. Half of this set exists to separate Azure Policy, Azure RBAC, and
resource locks, which beginners routinely conflate.

---

## Questions

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

**10.** *(Carry-forward)* An organization wants one policy to apply to all 20 of its subscriptions without assigning it 20 times. Where should the policy be assigned?

- A. On each resource group
- B. At the management group containing the subscriptions
- C. On the Microsoft Entra tenant only
- D. On a single representative subscription

**11.** *(Carry-forward)* Which tool answers the question "what is this user allowed to do in this subscription," as opposed to "is this resource configured correctly"?

- A. Azure Policy
- B. Azure RBAC
- C. Resource locks
- D. Microsoft Purview

**12.** *(Carry-forward)* A governance standard requires that every new resource carry an `Owner` tag, and that the tag be restored if someone removes it. What enforces this?

- A. A resource lock
- B. Azure Policy
- C. Microsoft Cost Management budgets
- D. Azure RBAC role assignment

---

## Answer key

| Q | Answer | Objective | Why | Source |
| --- | --- | --- | --- | --- |
| 1 | B | 3.2.2 | Azure Policy creates, assigns, and manages rules that control or audit resource configuration for compliance with your standards. A is RBAC, C is resource locks, D is Azure Monitor. | [Purpose of Azure Policy](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/3-describe-purpose-azure-policy) |
| 2 | B | 3.2.2 | An initiative groups related policy definitions so compliance can be tracked toward a larger goal; Microsoft's monitoring initiative alone contains over 100 definitions. | [Purpose of Azure Policy](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/3-describe-purpose-azure-policy) |
| 3 | C | 3.2.2 | Policy applies to everything in the assigned scope through inheritance and evaluates existing resources as well as new ones — including VMs created before the policy existed. | [Purpose of Azure Policy](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/3-describe-purpose-azure-policy) |
| 4 | A, B, C, E | 3.2.2 | Policy can block noncompliant creation, inherits through scope, can remediate some configurations such as a missing tag, and supports exceptions. D is false — Policy governs resource configuration, RBAC governs who may act. | [Purpose of Azure Policy](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/3-describe-purpose-azure-policy) |
| 5 | B | 3.2.3 | A Delete lock lets authorized users read and modify but not delete. A ReadOnly lock would also block the updates engineers need. The Reader role would restrict those users entirely rather than protecting the group from everyone. | [Purpose of resource locks](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/4-describe-purpose-resource-locks) |
| 6 | B | 3.2.3 | ReadOnly permits reading only; it is comparable to restricting all authorized users to Reader-level permissions on that resource. | [Purpose of resource locks](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/4-describe-purpose-resource-locks) |
| 7 | B | 3.2.3 | Locks apply regardless of RBAC permissions. Even an Owner must remove the lock first, which is the two-step process that makes locks effective against accidents. | [Purpose of resource locks](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/4-describe-purpose-resource-locks) |
| 8 | A | 3.2.1 | Purview is a family of data governance, risk, and compliance solutions giving a unified view of the data estate, with automated discovery, sensitive data classification, and end-to-end lineage across on-premises, multicloud, and SaaS data. | [Purpose of Microsoft Purview](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/2-describe-purpose-microsoft-purview) |
| 9 | B | 3.2.1 | Locating sensitive data across a whole data estate and tracing lineage is Purview's unified data governance role. A is Azure Policy, C is a resource lock, D is a Cost Management budget alert. | [Purpose of Microsoft Purview](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/2-describe-purpose-microsoft-purview) |
| 10 | B | 2.1.7 (carry-forward) | Assigning at the management group means every subscription beneath it inherits the policy, which is the reason management groups exist. | [Azure management infrastructure](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/6-describe-azure-management-infrastructure) |
| 11 | B | 2.4.5 (carry-forward) | RBAC governs who may perform which actions at which scope. Policy governs what configurations are allowed; locks prevent change or deletion; Purview governs data. | [Azure role-based access control](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/6-role-based-access-control) |
| 12 | B | 3.1.4 (carry-forward) | Azure Policy can require tags on new resources and reapply tags that have been removed. Tags are not inherited, so policy enforcement is how organizations keep them consistent. | [Purpose of tags](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/7-describe-purpose-of-tags) |

**Instructor note:** items 5–7 and 11 form the discrimination set. A good closing question
for the review is: "name the one thing that stops an Owner from deleting a resource" —
the answer is a resource lock, not RBAC and not Policy.
