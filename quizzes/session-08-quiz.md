# Session 8 Quiz — Azure Cost Management

**Time:** 15 minutes · **Items:** 12 · **Composition:** 9 new, 3 carry-forward (S2–S7)
**Objectives:** 3.1.1, 3.1.2, 3.1.3, 3.1.4 (plus 1.1.6 scheduled second pass)
**Carry-forward objectives:** 1.1.6, 2.3.2, 2.4.5
**Target:** 80%

---

## Questions

**1.** Which of these affect what an Azure resource costs? (Select all that apply.)

- A. The resource type and the settings chosen for it
- B. The region where the resource is deployed
- C. The number of tags applied to the resource
- D. The subscription type, which may include usage allowances
- E. Third-party charges for solutions purchased through Azure Marketplace

**2.** A team provisions a virtual machine, then deletes the VM but leaves its disks, network interface, and public IP address in place. What is the cost consequence?

- A. None; dependent resources are always deleted with the VM
- B. The leftover resources continue to incur charges until they are removed
- C. The resources are billed at half rate while unattached
- D. Azure automatically deletes unattached resources after 24 hours

**3.** Moving data out of an Azure datacenter is priced using which concept?

- A. Availability zones
- B. Billing zones, which are geographical groupings of regions used for data-transfer pricing
- C. Region pairs
- D. Management groups

**4.** Which statement about the Azure pricing calculator is correct?

- A. Adding resources to the calculator provisions them in your subscription
- B. It produces an estimate only, and nothing is provisioned or charged
- C. It reports your actual spend for the current billing cycle
- D. It replaced Microsoft Cost Management

**5.** A team wants to compare the monthly estimated cost of the same three-tier design in two different regions before deploying anything. Which tool should they use?

- A. Microsoft Cost Management cost analysis
- B. The Azure pricing calculator
- C. Azure Advisor
- D. Azure Monitor

**6.** Which feature of Microsoft Cost Management lets you view accumulated costs broken down by subscription, resource group, or service to find where spend is accruing?

- A. Cost analysis
- B. Budget alerts
- C. Resource locks
- D. Azure Policy compliance state

**7.** Which statements about budgets and cost alerts are correct? (Select all that apply.)

- A. A budget can be scoped to a subscription, resource group, or service type
- B. Setting a budget automatically stops all spending when the limit is reached
- C. Budget alerts notify recipients when spending crosses a threshold you define
- D. Budgets can trigger automation that suspends or modifies resources at a threshold
- E. Credit alerts and department spending quota alerts are both types of cost alert

**8.** Which statement about resource tags is correct?

- A. Resources inherit tags from their resource group and subscription automatically
- B. Tags are name and value pairs that are not inherited, and Azure Policy can enforce required tags
- C. Tags can only be applied through the Azure portal
- D. Every resource must carry the same set of tags

**9.** An organization wants monthly cost reports broken down by internal cost center and by environment. What is the prerequisite?

- A. A separate subscription per cost center
- B. A consistent tagging strategy applied to the resources
- C. A resource lock on each resource group
- D. Read access to the pricing calculator

**10.** *(Carry-forward)* A workload runs a predictable, constant compute load and the team can commit financially for three years, but wants flexibility in which VM series it uses over that period. Which option fits best?

- A. A reservation for a specific VM size
- B. Azure savings plan for compute
- C. Azure Spot Virtual Machines
- D. Pay-as-you-go

**11.** *(Carry-forward)* Storage costs need to come down for a dataset that is accessed a few times a year but must remain immediately readable. Which change is most appropriate?

- A. Move the data to the archive tier
- B. Move the data to the cool or cold tier
- C. Change redundancy from GZRS to LRS and keep the hot tier
- D. Delete the data and re-upload when needed

**12.** *(Carry-forward)* A finance analyst must review cost data for a subscription but must not be able to change any resources. Which approach follows least privilege?

- A. Assign Owner at the subscription scope
- B. Assign Contributor at the subscription scope
- C. Assign a read-level role at the subscription scope
- D. Apply a ReadOnly resource lock to every resource group

---

## Answer key

| Q | Answer | Objective | Why | Source |
| --- | --- | --- | --- | --- |
| 1 | A, B, D, E | 3.1.1 | Resource type and settings, geography, subscription type, and Azure Marketplace third-party billing are all named cost factors, along with consumption and maintenance. Tag count has no cost effect — tags help you *report* on cost. | [Cost factors](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/2-describe-factors-affect-costs-azure) |
| 2 | B | 3.1.1 | Deprovisioning a VM does not necessarily deprovision the storage and networking resources created with it, and those keep charging. This is the maintenance cost factor. | [Cost factors](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/2-describe-factors-affect-costs-azure) |
| 3 | B | 3.1.1 | Billing zones are geographical groupings of regions used specifically for data-transfer pricing, and are not the same thing as availability zones. Some inbound transfers are free; outbound is priced by zone. | [Cost factors](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/2-describe-factors-affect-costs-azure) |
| 4 | B | 3.1.2 | The pricing calculator is informational; prices are estimates, nothing is provisioned, and you are not charged for what you model. Note that the Total Cost of Ownership (TCO) calculator has been retired. | [Explore the pricing calculator](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/3-compare-pricing-total-cost-of-ownership-calculators) |
| 5 | B | 3.1.2 | The pricing calculator estimates costs before deployment and supports comparing regions, service tiers, and redundancy options. Cost analysis reports on spend that has already happened. | [Explore the pricing calculator](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/3-compare-pricing-total-cost-of-ownership-calculators) |
| 6 | A | 3.1.3 | Cost analysis is the Cost Management feature that visualizes and aggregates costs by billing cycle, subscription, resource group, resource, region, or service. | [Microsoft Cost Management tool](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/6-describe-azure-tool) |
| 7 | A, C, D, E | 3.1.3 | Budgets can be scoped several ways, alert at thresholds you define, and can trigger automation such as shutting down nonproduction resources. The three cost alert types are budget, credit, and department spending quota. B is false — a budget alerts and can trigger automation, but does not itself halt spending. | [Microsoft Cost Management tool](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/6-describe-azure-tool) |
| 8 | B | 3.1.4 | Tags are name and value metadata, are not inherited from subscriptions or resource groups, can be managed through the portal, PowerShell, CLI, ARM templates, or REST API, and can be required and reapplied through Azure Policy. | [Purpose of tags](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/7-describe-purpose-of-tags) |
| 9 | B | 3.1.4 | Cost reporting by cost center and environment depends on consistent tags such as CostCenter and Environment. Separate subscriptions are one way to divide billing but are not required to report this way. | [Purpose of tags](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/7-describe-purpose-of-tags) |
| 10 | B | 1.1.6 (carry-forward) | A savings plan commits to an hourly spend on eligible compute rather than to a specific resource, which is exactly the flexibility described. A reservation would lock the VM size. | [Cost factors](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/2-describe-factors-affect-costs-azure) |
| 11 | B | 2.3.2 (carry-forward) | Cool and cold tiers lower storage cost for infrequently accessed data while keeping it immediately readable. Archive has the lowest storage cost but requires rehydration, so the data is not immediately readable. | [Azure storage services](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/4-describe-azure-storage-services) |
| 12 | C | 2.4.5 (carry-forward) | Least privilege means granting only the access needed — a read-level role at the scope where the analyst needs visibility. Owner and Contributor both allow changes; a resource lock restricts everyone, not just this analyst, and is not an access-control mechanism. | [Azure role-based access control](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/6-role-based-access-control) |

**Instructor note on item 4:** this is the item where learners who studied from older
third-party material will look for a TCO calculator option. Use the review to state
plainly that the TCO calculator is retired and the objective now covers the pricing
calculator only.
