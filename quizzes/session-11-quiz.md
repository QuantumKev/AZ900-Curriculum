# Session 11 Quiz — Monitoring, and Domain 3 Checkpoint

**Time:** 15 minutes · **Items:** 12
**Composition:** 6 new (monitoring), 3 Domain 3 checkpoint (3.1–3.3), 3 mixed review (S1–S7)
**Objectives:** 3.4.1, 3.4.2, 3.4.3
**Checkpoint objectives:** 3.1.3, 3.2.2, 3.3.5
**Mixed review objectives:** 1.1.2, 2.2.5, 2.4.6
**Target:** 80%

This quiz doubles as the Domain 3 checkpoint. Objectives 3.1–3.3 were each quizzed in their
own session; the checkpoint items here confirm they held.

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

**7.** *(Domain 3 checkpoint)* Which tool shows where Azure spend has already accrued, broken down by subscription, resource group, or service?

- A. The Azure pricing calculator
- B. Microsoft Cost Management cost analysis
- C. Azure Advisor
- D. Azure Service Health

**8.** *(Domain 3 checkpoint)* A standard requires that no storage account be created outside two approved regions. Which service enforces it?

- A. Azure Policy
- B. Resource locks
- C. Azure RBAC
- D. Microsoft Purview

**9.** *(Domain 3 checkpoint)* Which statement about Azure Resource Manager templates is correct?

- A. They are imperative scripts that list deployment commands in order
- B. They are declarative JSON files describing the resources you want, which Azure validates and then deploys in dependency order
- C. They can only be created by exporting from the Azure portal
- D. They apply only to virtual machines

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
| 7 | B | 3.1.3 | Cost analysis in Microsoft Cost Management reports actual accrued spend by billing cycle, subscription, resource group, resource, and service. The pricing calculator estimates before deployment. | [Microsoft Cost Management tool](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/6-describe-azure-tool) |
| 8 | A | 3.2.2 | Restricting allowed locations is a classic Azure Policy control, and Policy can block noncompliant creation outright. Locks prevent change or deletion; RBAC governs who may act. | [Purpose of Azure Policy](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/3-describe-purpose-azure-policy) |
| 9 | B | 3.3.5 | ARM templates are declarative JSON that define the desired resources; Azure validates the template and orchestrates creation in the right order, in parallel where possible. Exporting from the portal is one way to obtain a template, not the only way. | [Azure Resource Manager and ARM templates](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/4-describe-azure-resource-manager-azure-arm-templates) |
| 10 | A, C, D | 1.1.2 | On IaaS the customer owns the operating system and above, plus data and identity in every model. Physical datacenter and physical network are always the provider's. | [Shared responsibility model](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/4-describe-shared-responsibility-model) |
| 11 | C | 2.2.5 | ExpressRoute provides private connectivity that bypasses the public internet. Both VPN types cross the internet inside an encrypted tunnel; peering connects virtual networks, not on-premises datacenters. | [Azure ExpressRoute](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/4-expressroute) |
| 12 | B | 2.4.6 | Assume breach means limiting potential impact, segmenting access, verifying end-to-end encryption, and using analytics for visibility and detection. A is the perimeter assumption Zero Trust rejects. | [Zero Trust model](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/7-describe-zero-trust-model) |

**Scoring the checkpoint:** record items 7–9 separately. Any learner missing two or three
of them needs Domain 3 re-teaching in the Session 12 gap clinic, regardless of their total
score on this quiz.
