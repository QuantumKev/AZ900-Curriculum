# Session 3 Quiz — Azure Architecture

**Time:** 15 minutes · **Items:** 12 · **Composition:** 9 new, 3 carry-forward (S1–S2)
**Objectives:** 2.1.1, 2.1.2, 2.1.3, 2.1.4, 2.1.5, 2.1.6, 2.1.7
**Carry-forward objectives:** 1.1.3, 1.2.1, 1.3.4
**Target:** 80%

---

## Questions

**1.** (Match each description to the correct term: datacenter, region, availability zone, region pair, sovereign region.)

- i. A physical facility of racked servers with dedicated power, cooling, and networking, which you do not interact with directly
- ii. A geographical area containing at least one, and potentially several, nearby datacenters connected by a low-latency network
- iii. Physically separate datacenters within one region, each with independent power, cooling, and networking
- iv. Two regions in the same geography, at least 300 miles apart, used for replication and staged platform updates
- v. An instance of Azure isolated from the main instance of Azure for legal or compliance reasons

**2.** Which statement about availability zones is correct?

- A. Every Azure region supports availability zones
- B. An availability zone is a logical grouping of subscriptions
- C. Availability-zone-enabled regions contain a minimum of three separate zones with independent power, cooling, and networking
- D. Availability zones are always in different geographies

**3.** Your organization must keep replicated data within the same geography for compliance and wants protection against an event that affects an entire region. Which Azure capability addresses this?

- A. Availability zones
- B. Region pairs
- C. Sovereign regions
- D. Resource groups

**4.** A US government agency requires an instance of Azure that is physically and logically network-isolated from the main instance of Azure. What is this called?

- A. A private cloud
- B. A sovereign region
- C. An availability zone
- D. A dedicated host

**5.** Which statements about resource groups are correct? (Select all that apply.)

- A. A resource can belong to more than one resource group at a time
- B. Every resource must belong to exactly one resource group
- C. Resource groups can be nested inside other resource groups
- D. Deleting a resource group deletes the resources inside it
- E. Access granted on a resource group applies to the resources it contains

**6.** In Azure, a subscription acts as which two kinds of boundary?

- A. A network boundary and a security boundary
- B. A billing boundary and an access control boundary
- C. A region boundary and a compliance boundary
- D. A tenant boundary and a licensing boundary

**7.** An organization has 14 subscriptions across three teams and wants to apply one policy and one role assignment that affect all of them without repeating the work per subscription. What should it use?

- A. A resource group containing the subscriptions
- B. Tags applied to each subscription
- C. A management group containing the subscriptions
- D. A separate Microsoft Entra tenant per team

**8.** (Put these Azure scopes in order from broadest to narrowest.)

- A. Resource
- B. Management group
- C. Resource group
- D. Subscription

**9.** A policy is assigned at the management group level restricting resource deployment to specific regions. What happens to the subscriptions inside that management group?

- A. Nothing until the policy is assigned again on each subscription
- B. They inherit the policy automatically, and resource or subscription owners cannot override it
- C. They inherit the policy but any owner can opt out
- D. Only new subscriptions inherit it; existing ones are unaffected

**10.** *(Carry-forward)* A hospital keeps patient records on infrastructure dedicated to itself and runs its public appointment-booking website on a third-party provider's shared infrastructure. Which cloud model does the combination describe?

- A. Public cloud
- B. Private cloud
- C. Hybrid cloud
- D. Multicloud

**11.** *(Carry-forward)* An application's virtual machines are struggling under load. The team adds four more identical virtual machines behind a load balancer. Which scaling approach is this?

- A. Vertical scaling
- B. Horizontal scaling
- C. Scaling up
- D. Manual failover

**12.** *(Carry-forward)* A team must run software that requires a specific operating system version, custom kernel settings, and its own installed agents. Which cloud service type fits, and why?

- A. SaaS, because it requires the least technical expertise
- B. PaaS, because the provider handles the operating system
- C. IaaS, because it gives control over the operating system and installed software
- D. Any of the three; the requirement does not affect the choice

---

## Answer key

| Q | Answer | Objective | Why | Source |
| --- | --- | --- | --- | --- |
| 1 | i–datacenter, ii–region, iii–availability zone, iv–region pair, v–sovereign region | 2.1.1, 2.1.2, 2.1.3 | These five terms are the vocabulary learners most often blur together. Note that customers deploy to regions and zones, not to individual datacenters. Score one point per pair, then round. | [Azure physical infrastructure](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/5-describe-azure-physical-infrastructure) · [Azure geographies](https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/) |
| 2 | C | 2.1.2 | Availability-zone-enabled regions have a minimum of three separate zones, each with independent power, cooling, and networking. A is false — not all regions support zones. | [Azure physical infrastructure](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/5-describe-azure-physical-infrastructure) |
| 3 | B | 2.1.1 | Region pairs replicate across a geography, at least 300 miles apart, and keep data in the same geography for residency and compliance purposes (Brazil South being the noted exception). Availability zones protect within a single region, not against a whole-region event. | [Azure physical infrastructure](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/5-describe-azure-physical-infrastructure) · [Region pairs](https://learn.microsoft.com/en-us/azure/reliability/cross-region-replication-azure) |
| 4 | B | 2.1.1 | Sovereign regions are isolated instances of Azure for compliance or legal purposes, such as the US Gov regions operated by screened US personnel. | [Azure physical infrastructure](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/5-describe-azure-physical-infrastructure) |
| 5 | B, D, E | 2.1.4 | A resource belongs to exactly one resource group; resource groups can't be nested; actions on the group — deletion, access grants — apply to everything inside. | [Azure management infrastructure](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/6-describe-azure-management-infrastructure) |
| 6 | B | 2.1.5 | Subscriptions are a billing boundary (separate invoices and reports) and an access control boundary (access policies applied at subscription level). | [Azure management infrastructure](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/6-describe-azure-management-infrastructure) |
| 7 | C | 2.1.6 | Management groups sit above subscriptions; one policy assignment or one role assignment on the group applies to every subscription beneath it. Resource groups cannot contain subscriptions. | [Azure management infrastructure](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/6-describe-azure-management-infrastructure) · [Management groups](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview) |
| 8 | B, D, C, A | 2.1.7 | Management group, then subscription, then resource group, then resource. Score all-or-nothing. | [Azure management infrastructure](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/6-describe-azure-management-infrastructure) |
| 9 | B | 2.1.7 | Governance conditions applied to a management group are inherited by all subscriptions beneath it, and the resource or subscription owner can't override the assignment. Exceptions are handled deliberately through Azure Policy, not by owner opt-out. | [Azure management infrastructure](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/6-describe-azure-management-infrastructure) |
| 10 | C | 1.1.3 (carry-forward) | Private infrastructure for sensitive records plus public cloud for the public-facing site is an interconnected hybrid environment. Multicloud would require two or more public providers. | [Define cloud models](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/5-define-cloud-models) |
| 11 | B | 1.2.1 (carry-forward) | Adding instances is horizontal scaling (scaling out). Vertical scaling, also called scaling up, would add CPU or RAM to existing machines. | [High availability and scalability](https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/2-high-availability-scalability-cloud) |
| 12 | C | 1.3.4 (carry-forward) | IaaS is the only type that gives the customer control of the operating system and installed software, which is exactly what custom kernel settings and agents require. | [IaaS](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/2-describe-infrastructure-service) |

**Instructor note on item 2:** learners often answer A because zones are discussed as a
standard capability. Reinforce that zone support is region-dependent, which is why region
selection matters when a design requires zone redundancy.
