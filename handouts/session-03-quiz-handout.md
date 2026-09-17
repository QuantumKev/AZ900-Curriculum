# Session 3 Quiz — Azure Architecture

**Name:** <span class="blank"></span>  **Session:** <span class="blank"></span>

**Time:** 15 minutes · **Items:** 12 · **Target:** 80%

Answer every question. For *select all that apply*, mark every correct option. For
matching questions, write the matching term next to each numeral. For yes/no sets,
write yes or no next to each numeral. Your instructor reviews every answer in class
immediately afterward.

---

**1.** (Match each description to the correct term: datacenter, region, availability zone, region pair, sovereign region.)

- i. A physical facility of racked servers with dedicated power, cooling, and networking, which you do not interact with directly &nbsp; <span class="blank"></span>
- ii. A geographical area containing at least one, and potentially several, nearby datacenters connected by a low-latency network &nbsp; <span class="blank"></span>
- iii. Physically separate datacenters within one region, each with independent power, cooling, and networking &nbsp; <span class="blank"></span>
- iv. Two regions in the same geography, at least 300 miles apart, used for replication and staged platform updates &nbsp; <span class="blank"></span>
- v. An instance of Azure isolated from the main instance of Azure for legal or compliance reasons &nbsp; <span class="blank"></span>

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

**10.** A hospital keeps patient records on infrastructure dedicated to itself and runs its public appointment-booking website on a third-party provider's shared infrastructure. Which cloud model does the combination describe?

- A. Public cloud
- B. Private cloud
- C. Hybrid cloud
- D. Multicloud

**11.** An application's virtual machines are struggling under load. The team adds four more identical virtual machines behind a load balancer. Which scaling approach is this?

- A. Vertical scaling
- B. Horizontal scaling
- C. Scaling up
- D. Manual failover

**12.** A team must run software that requires a specific operating system version, custom kernel settings, and its own installed agents. Which cloud service type fits, and why?

- A. SaaS, because it requires the least technical expertise
- B. PaaS, because the provider handles the operating system
- C. IaaS, because it gives control over the operating system and installed software
- D. Any of the three; the requirement does not affect the choice

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
