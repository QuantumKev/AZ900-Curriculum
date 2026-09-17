# Domain 1 Checkpoint — Describe Cloud Concepts

**When:** Start of Session 3, replacing the warm-up · **Time:** 15 minutes · **Items:** 12
**Coverage:** all 15 Domain 1 objectives (1.1.1–1.3.4)
**Target:** 75%

Diagnostic, not punitive. The result decides which Domain 1 objectives get priority in the
Session 4–S8 warm-ups and in the Session 11 cumulative block. Multi-objective items keep a
whole domain inside 15 minutes.

Review every item in class immediately afterward.

---

## Questions

**1.** Which statement best captures what makes something cloud computing rather than traditional IT?

- A. The workload runs on virtualized hardware
- B. Computing services are delivered over the internet and rented rather than owned
- C. The hardware is newer than five years old
- D. The organization has more than one datacenter

**2.** Which item is always the customer's responsibility, in every cloud service type?

- A. The physical hosts
- B. The operating system
- C. The accounts and identities in the environment
- D. The physical network

**3.** Which statement correctly describes how responsibility shifts across service types?

- A. IaaS places the most responsibility on the provider, and SaaS the most on the customer
- B. IaaS places the most responsibility on the customer, SaaS the most on the provider, and PaaS sits between them
- C. Responsibility is identical in all three; only pricing differs
- D. The customer is responsible for physical security in IaaS

**4.** (Match each scenario to the cloud model that fits best: public, private, hybrid, or multicloud.)

- i. A single organization runs a dedicated cloud environment in its own datacenter
- ii. A company keeps regulated data on dedicated infrastructure and runs its public website with a cloud provider, connecting the two
- iii. A startup with no hardware buys all of its infrastructure from a cloud provider
- iv. An enterprise runs production workloads with two different public cloud providers and manages security in both

**5.** Which outcome is the clearest consequence of the consumption-based model?

- A. You purchase capacity in advance to guarantee availability
- B. You pay only for resources you use, and you can release them when demand drops
- C. Infrastructure costs become capital expenditure
- D. Costs are fixed and independent of usage

**6.** A team can commit to a three-year term on a specific virtual machine size for a steady workload. Which pricing option is intended for that situation?

- A. Pay-as-you-go
- B. A reservation
- C. Azure Spot Virtual Machines
- D. The Azure free account

**7.** Which description matches serverless computing?

- A. Code runs on a VM you size and patch yourself
- B. Code is triggered by an event, resources are allocated around the run and released afterward, and you pay for the time it executes
- C. A dedicated physical host is reserved for your workload
- D. A managed desktop is delivered to remote users

**8.** An application must keep serving users during a datacenter-level failure and must handle a fivefold traffic increase during a sale. Which two cloud benefits are being described?

- A. Governance and compliance
- B. High availability and scalability
- C. Manageability and predictability
- D. Security and reliability

**9.** Which statement describes reliability as distinct from predictability?

- A. Reliability is forecasting cost; predictability is recovering from failure
- B. Reliability is recovering from failure and continuing to function; predictability is being able to anticipate performance and cost
- C. They are two names for the same property
- D. Reliability applies only to storage; predictability only to compute

**10.** Which pair of capabilities are governance and security benefits of the cloud?

- A. Deploying from templates to meet technical standards, and cloud-based auditing that flags noncompliant resources
- B. Buying hardware in bulk, and negotiating vendor discounts
- C. Writing application code, and running unit tests
- D. Assigning licenses, and paying invoices

**11.** Which set of activities describes management *in* the cloud?

- A. Autoscaling resources and automatically replacing failing resources
- B. Deploying from preconfigured templates and receiving metric-based alerts
- C. Using a web portal, a command line interface, APIs, or PowerShell to manage the environment
- D. Monitoring resource health and configuring automatic alerts

**12.** (Match each requirement to the cloud service type that fits best: IaaS, PaaS, or SaaS.)

- i. Full control of the operating system for a lift-and-shift migration
- ii. A ready-to-use email and messaging product with no development work
- iii. A managed development framework with built-in scalability and multitenancy so developers write less infrastructure code
- iv. Rapidly created and destroyed test environments replicating an established server configuration
- v. Business intelligence tooling delivered as a service for a team to analyze its own data

---

## Answer key

| Q | Answer | Objective | Why | Source |
| --- | --- | --- | --- | --- |
| 1 | B | 1.1.1 | Cloud computing is delivery of computing services over the internet on a rental basis. Virtualization alone is not cloud computing — plenty of on-premises datacenters are virtualized. | [What is cloud computing](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/3-what-cloud-compute) |
| 2 | C | 1.1.2 | Accounts and identities, data, and connecting devices always stay with the customer. The operating system depends on the service type; the physical layers are always the provider's. | [Shared responsibility model](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/4-describe-shared-responsibility-model) |
| 3 | B | 1.1.2 | IaaS puts the most on the customer, SaaS the most on the provider, and PaaS distributes responsibility between the two. | [Shared responsibility model](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/4-describe-shared-responsibility-model) |
| 4 | i–private, ii–hybrid, iii–public, iv–multicloud | 1.1.3, 1.1.4 | Single-organization environment is private; interconnected private plus public is hybrid; buying everything from a provider is public; two or more public providers is multicloud. Score one point per pair, then round. | [Define cloud models](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/5-define-cloud-models) |
| 5 | B | 1.1.5 | Paying only for what you use and releasing resources on demand is the defining consequence; cloud consumption is classified as operational, not capital, expenditure. | [Consumption-based model](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/6-describe-consumption-based-model) |
| 6 | B | 1.1.6 | Reservations commit to specific resources for one or three years to reduce cost. Spot is for interruptible workloads; pay-as-you-go carries no commitment and no discount. | [Cost factors](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/2-describe-factors-affect-costs-azure) |
| 7 | B | 1.1.7 | Serverless is event-driven: the event wakes the code, Azure allocates and then deallocates resources, and charging is based on the time the code runs. | [Azure functions](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/6-functions) |
| 8 | B | 1.2.1 | Continuing to serve during a failure is high availability; absorbing a traffic increase is scalability. | [High availability and scalability](https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/2-high-availability-scalability-cloud) |
| 9 | B | 1.2.2 | Reliability is recovery and continued function; predictability covers anticipating performance (autoscaling, load balancing, high availability) and cost (usage tracking, forecasting, the pricing calculator). | [Reliability and predictability](https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/3-reliability-predictability-cloud) |
| 10 | A | 1.2.3 | Templates that enforce standards and cloud-based auditing that flags out-of-compliance resources are the named governance benefits; automatic patching in PaaS and SaaS and provider-scale DDoS resilience are the security side. | [Security and governance](https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/4-security-governance-cloud) |
| 11 | C | 1.2.4 | Management *in* the cloud is the interfaces — portal, CLI, APIs, PowerShell. A, B, and D are all management *of* the cloud. | [Manageability](https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/5-manageability-cloud) |
| 12 | i–IaaS, ii–SaaS, iii–PaaS, iv–IaaS, v–PaaS | 1.3.1, 1.3.2, 1.3.3, 1.3.4 | Lift-and-shift and rapid test-environment replication are the IaaS scenarios; development framework and analytics or business intelligence are the PaaS scenarios; a ready-to-use product is SaaS. Score one point per pair, then round. | [IaaS](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/2-describe-infrastructure-service) · [PaaS](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/3-describe-platform-service) · [SaaS](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/4-describe-software-service) |

## What to do with the result

| Result | Action |
| --- | --- |
| 10–12 correct | Domain 1 is holding. Keep the standard warm-up rotation. |
| 8–9 correct | Identify the missed objective IDs and give those objectives priority in the Session 4 and Session 5 warm-ups. |
| Below 8 | Add a 10-minute Domain 1 re-teach to Session 4 using the missed objectives, and assign the relevant module units as homework. Domain 1 is 25–30% of the exam; it is worth the time now rather than in Week 6. |

Record per-objective misses, not just totals. The Session 11 cumulative block re-teaches
the two weakest areas from this checkpoint and the Domain 2 checkpoint, so the data has to
be specific enough to act on.
