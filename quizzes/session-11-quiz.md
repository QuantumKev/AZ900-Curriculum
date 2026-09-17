# Session 11 Quiz — Monitoring, and Domain 3 Checkpoint

**Time:** 15 minutes · **Items:** 12
**Composition:** 6 new (monitoring), 3 Domain 3 checkpoint (3.1–3.3), 3 mixed review (S1–S7)
**Objectives:** 3.4.1, 3.4.2, 3.4.3
**Checkpoint objectives:** all of 3.1.1–3.3.5, via three multi-part items
**Mixed review objectives:** 1.1.2, 2.2.5, 2.4.6
**Target:** 80%

This quiz doubles as the Domain 3 checkpoint. Items 7–9 are multi-part by design: together
they sweep all twelve objectives from Sessions 8, 9, and 10 in three items, the same
technique the Domain 1 and Domain 2 checkpoints use.

---

## Questions

**1.** What does Azure Advisor do?

- A. Reports whether Azure itself is experiencing an outage
- B. Evaluates your Azure resources and makes recommendations to improve reliability, security, performance, operational excellence, and cost
- C. Collects and queries log and metric data from your resources
- D. Estimates the cost of resources before you deploy them

**2.** Which are Azure Advisor recommendation categories? (Select all that apply.)

- A. Reliability
- B. Security
- C. Performance
- D. Operational Excellence
- E. Cost

**3.** A virtual machine in your subscription is unreachable and you need to know whether the problem is on Azure's side or yours, for that specific VM. Which view should you check?

- A. Azure Status
- B. Service Health
- C. Resource Health
- D. Application Insights

**4.** You hear reports of a widespread outage and want a global picture of Azure health across all services and regions. Which view should you check?

- A. Azure Status
- B. Service Health
- C. Resource Health
- D. Azure Advisor

**5.** Which information does Service Health show that Azure Status does not?

- A. Outages, planned maintenance, and health advisories specific to the services and regions you actually use, with alerting
- B. The global health of every Azure service in every region
- C. Application request rates and response times
- D. Estimated monthly spend by resource group

**6.** (Match each need to the Azure Monitor capability that fits: Log Analytics, Azure Monitor alerts, Application Insights.)

- i. Write and run a query against collected data to find all errors in the last hour
- ii. Be notified when a virtual machine's CPU stays above 80 percent, with the notification routed to an on-call group
- iii. Track a web application's request rates, response times, failure rates, and dependency calls

**7.** *(Domain 3 checkpoint — cost management.)* (Match each need to the right capability: the pricing calculator, Microsoft Cost Management cost analysis, budgets with alerts, tags.)

- i. Estimate what a proposed design will cost in two candidate regions before deploying it
- ii. See where spend has already accrued, broken down by subscription, resource group, or service
- iii. Be notified when spending crosses a defined threshold, and optionally trigger automation
- iv. Attach the metadata that makes cost reports answer "which cost center" and "which environment"

**8.** *(Domain 3 checkpoint — governance and compliance.)* (For each statement, answer yes or no.)

- i. Azure Policy can prevent a noncompliant resource from being created, and also evaluates resources that already existed.
- ii. A Delete lock allows authorized users to read and update a resource but not delete it.
- iii. Microsoft Purview's purpose is to discover and classify data across your estate and trace its lineage.
- iv. A subscription Owner can delete a resource that has a Delete lock applied, without removing the lock.

**9.** *(Domain 3 checkpoint — managing and deploying.)* (Match each need to the right option: Azure portal, Azure Cloud Shell, Azure Arc, infrastructure as code, ARM template.)

- i. A browser-based shell, already authenticated to your credentials, supporting both Azure PowerShell and the Azure CLI
- ii. Govern servers in your own datacenter and Kubernetes clusters in another cloud from Azure
- iii. A declarative JSON file describing the resources to deploy, which Azure validates and orchestrates
- iv. The practice of managing infrastructure through code and templates rather than manual configuration
- v. A web console with custom dashboards for building, managing, and monitoring resources

**10.** *(Mixed review)* For an application hosted on an IaaS virtual machine, which responsibilities are the customer's? (Select all that apply.)

- A. Operating system patching
- B. Physical datacenter security
- C. The data stored by the application
- D. Identity and access configuration
- E. Maintenance of the physical network

**11.** *(Mixed review)* An organization needs a private, dedicated connection from its datacenter to Azure that does not traverse the public internet. Which option meets the requirement?

- A. Site-to-site VPN
- B. Point-to-site VPN
- C. Azure ExpressRoute
- D. Virtual network peering

**12.** *(Mixed review)* Which action best reflects the Zero Trust principle of "assume breach"?

- A. Trusting all traffic originating inside the corporate network
- B. Segmenting access and verifying end-to-end encryption to limit the impact of a compromise
- C. Requiring a password of at least 16 characters
- D. Publishing all applications through a single public endpoint

---

## Answer key

| Q | Answer | Objective | Why | Source |
| --- | --- | --- | --- | --- |
| 1 | B | 3.4.1 | Advisor evaluates your resources and recommends improvements, acting as a personalized best-practices guide in the portal, with actions you can take, postpone, or dismiss. A is Service Health, C is Azure Monitor, D is the pricing calculator. | [Purpose of Azure Advisor](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/2-describe-purpose-of-azure-advisor) |
| 2 | A, B, C, D, E | 3.4.1 | Advisor has five categories: Reliability, Security, Performance, Operational Excellence, and Cost. All five options are correct, which is the point of the item. | [Purpose of Azure Advisor](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/2-describe-purpose-of-azure-advisor) |
| 3 | C | 3.4.2 | Resource Health zooms in on an individual resource and reports whether it is running normally and whether the issue is on Azure's side or yours. | [Azure Service Health](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/3-describe-azure-service-health) |
| 4 | A | 3.4.2 | Azure Status gives the global picture across all services and regions. Service Health narrows to your services; Resource Health narrows to one resource. | [Azure Service Health](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/3-describe-azure-service-health) |
| 5 | A | 3.4.2 | Because you are signed in, Service Health knows which services and regions matter to you and shows relevant outages, planned maintenance, and health advisories, with alerts you can configure. | [Azure Service Health](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/3-describe-azure-service-health) |
| 6 | i–Log Analytics, ii–Azure Monitor alerts, iii–Application Insights | 3.4.3 | Log Analytics is where you write and run queries against data Azure Monitor collected; alerts fire on a condition and route notification through an action group; Application Insights monitors application performance and usage including dependencies and availability tests. Score one point per pair. | [Describe Azure Monitor](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/4-describe-azure-monitor) |
| 7 | i–pricing calculator, ii–cost analysis, iii–budgets with alerts, iv–tags | 3.1.1, 3.1.2, 3.1.3, 3.1.4 | The pricing calculator estimates before deployment; cost analysis reports accrued spend; budgets alert at thresholds and can trigger automation; tags supply the metadata cost reports group by. Fractional credit. | [Explore the pricing calculator](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/3-compare-pricing-total-cost-of-ownership-calculators) · [Cost Management tool](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/6-describe-azure-tool) · [Purpose of tags](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/7-describe-purpose-of-tags) |
| 8 | i–yes, ii–yes, iii–yes, iv–no | 3.2.1, 3.2.2, 3.2.3 | Only iv is false: locks apply regardless of RBAC, so even an Owner must remove the lock first. Fractional credit. | [Azure Policy](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/3-describe-purpose-azure-policy) · [Resource locks](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/4-describe-purpose-resource-locks) · [Microsoft Purview](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/2-describe-purpose-microsoft-purview) |
| 9 | i–Azure Cloud Shell, ii–Azure Arc, iii–ARM template, iv–infrastructure as code, v–Azure portal | 3.3.1, 3.3.2, 3.3.3, 3.3.4, 3.3.5 | Each option maps to exactly one need. Note the distinction between the practice (infrastructure as code) and the artifact (an ARM template). Fractional credit. | [Tools for interacting with Azure](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/2-describe-interacting-azure) · [Azure Arc](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/3-describe-purpose-of-azure-arc) · [ARM and ARM templates](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/4-describe-azure-resource-manager-azure-arm-templates) |
| 10 | A, C, D | 1.1.2 | On IaaS the customer owns the operating system and above, plus data and identity in every model. Physical datacenter and physical network are always the provider's. | [Shared responsibility model](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/4-describe-shared-responsibility-model) |
| 11 | C | 2.2.5 | ExpressRoute provides private connectivity that bypasses the public internet. Both VPN types cross the internet inside an encrypted tunnel; peering connects virtual networks, not on-premises datacenters. | [Azure ExpressRoute](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/4-expressroute) |
| 12 | B | 2.4.6 | Assume breach means limiting potential impact, segmenting access, verifying end-to-end encryption, and using analytics for visibility and detection. A is the perimeter assumption Zero Trust rejects. | [Zero Trust model](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/7-describe-zero-trust-model) |

**Scoring the checkpoint:** record items 7–9 separately, with fractional credit, and note
which parts were missed. Those parts name the Domain 3 objectives that need re-teaching in
the Session 12 gap clinic, regardless of the total score on this quiz. Every item is worth
one point out of 12; items 2 and 10 are multi-select and all-or-nothing, and items 6–9 earn
fractional credit.
