# Session 2 Quiz — Cloud Benefits, Pricing Models, and IaaS/PaaS/SaaS

**Time:** 15 minutes · **Items:** 12 · **Composition:** 10 new, 2 carry-forward (S1)
**Objectives:** 1.1.6, 1.1.7, 1.2.1, 1.2.2, 1.2.3, 1.2.4, 1.3.1, 1.3.2, 1.3.3, 1.3.4
**Carry-forward objectives:** 1.1.2, 1.1.5
**Target:** 80%

---

## Questions

**1.** A workload runs continuously and predictably for the next three years on a specific virtual machine size. Which pricing approach is most likely to reduce its cost?

- A. Pay-as-you-go
- B. A reservation
- C. Azure Spot Virtual Machines
- D. The Azure free account

**2.** A data-processing job can be interrupted and restarted without harm, and the team wants the lowest possible compute price. Which option fits?

- A. A reservation
- B. Azure savings plan for compute
- C. Azure Spot Virtual Machines
- D. Pay-as-you-go

**3.** Which statement describes Azure savings plan for compute?

- A. You commit to a specific VM size and region for one or three years
- B. You commit to an hourly spend on eligible compute services for one or three years
- C. You pay nothing until you exceed a monthly threshold
- D. You bid on unused capacity and may be evicted

**4.** Which statement about serverless computing is correct?

- A. There are no servers involved anywhere in the architecture
- B. You must keep at least one instance running to receive events
- C. An event triggers your code, and resources are allocated only around the run
- D. Serverless is a fourth cloud deployment model alongside public, private, and hybrid

**5.** Which pair correctly matches the scaling type to its action?

- A. Vertical scaling adds more virtual machines; horizontal scaling adds CPU and RAM
- B. Vertical scaling adds CPU and RAM to a resource; horizontal scaling adds or removes resources
- C. Both add resources; only the billing differs
- D. Vertical scaling happens automatically; horizontal scaling is always manual

**6.** Which best describes reliability as a cloud benefit?

- A. Predicting next quarter's cloud spend accurately
- B. The ability of a system to recover from failures and continue to function
- C. Guaranteeing identical performance in every region
- D. Encrypting data at rest and in transit

**7.** A team uses autoscaling and load balancing so response times stay steady as traffic changes. Which benefit does this primarily demonstrate?

- A. Cost predictability
- B. Performance predictability
- C. Manageability in the cloud
- D. Governance

**8.** Which of these are examples of governance and compliance benefits in the cloud? (Select all that apply.)

- A. Deploying from templates so resources meet your technical standards
- B. Cloud-based auditing that flags resources out of compliance with your baseline
- C. Automatic replication of all data to every region by default
- D. Updating resources at scale when standards change

**9.** Which group of capabilities describes *management of the cloud* rather than *management in the cloud*?

- A. Azure portal, Azure CLI, Azure PowerShell, REST APIs
- B. Autoscaling resources, deploying from templates, automatically replacing failing resources, metric-based alerts
- C. Purchasing subscriptions, assigning licenses, paying invoices
- D. Writing application code, running unit tests, publishing releases

**10.** (Match each scenario to the cloud service type that fits best: IaaS, PaaS, or SaaS. Each type is used at least once.)

- i. A team lifts and shifts existing servers to the cloud and needs full control of the operating system
- ii. Developers want a managed platform with built-in scalability so they can focus on application code, without handling OS licensing or patching
- iii. A finance department subscribes to a ready-to-use expense-tracking application
- iv. A team needs to rapidly create and tear down test environments that replicate an established server configuration
- v. An analytics team wants business intelligence tooling delivered as a service so they can mine their own data

**11.** *(Carry-forward)* A company subscribes to a cloud-based expense-tracking application. Who is responsible for patching the application, and who is responsible for managing user accounts?

- A. The provider patches the application; the customer manages user accounts
- B. The customer patches the application; the provider manages user accounts
- C. The provider does both
- D. The customer does both

**12.** *(Carry-forward)* Which outcome is a direct consequence of the consumption-based model?

- A. You must forecast capacity a year ahead to avoid penalties
- B. You avoid paying for capacity that sits idle
- C. Compute costs are fixed but storage costs vary
- D. Scaling down requires a support request

---

## Answer key

| Q | Answer | Objective | Why | Source |
| --- | --- | --- | --- | --- |
| 1 | B | 1.1.6 | Reservations commit to specific resources for a one- or three-year term to reduce cost, which suits steady, predictable workloads. Spot is for interruptible work; pay-as-you-go costs more for steady use. | [Cost factors](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/2-describe-factors-affect-costs-azure) |
| 2 | C | 1.1.6 | Spot Virtual Machines use unused capacity at lower prices, and workloads can be evicted when Azure needs the capacity back — acceptable only for interruption-tolerant jobs such as batch processing. | [Cost factors](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/2-describe-factors-affect-costs-azure) |
| 3 | B | 1.1.6 | A savings plan commits to an hourly spend on eligible compute for one or three years and applies the best available price automatically, trading resource specificity for flexibility. A describes a reservation; D describes spot. | [Cost factors](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/2-describe-factors-affect-costs-azure) |
| 4 | C | 1.1.7 | Serverless means the platform allocates resources when an event triggers the code and deallocates when it finishes, so nothing needs to stay provisioned between events. Servers still exist — you just don't manage them. | [Azure functions](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/6-functions) |
| 5 | B | 1.2.1 | Vertical scaling changes a resource's capability (CPU, RAM); horizontal scaling changes the number of resources. Both can be automatic or manual. | [High availability and scalability](https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/2-high-availability-scalability-cloud) |
| 6 | B | 1.2.2 | Reliability is recovery from failure and continued function, supported by the cloud's decentralized, multi-region design. A is cost predictability. | [Reliability and predictability](https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/3-reliability-predictability-cloud) |
| 7 | B | 1.2.2 | Autoscaling and load balancing are the named mechanisms behind performance predictability. Cost predictability is about forecasting spend. | [Reliability and predictability](https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/3-reliability-predictability-cloud) |
| 8 | A, B, D | 1.2.3 | Templates, cloud-based auditing, and updating at scale are the governance benefits described. C is false — replication to other regions is a configuration choice, not a default. | [Security and governance](https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/4-security-governance-cloud) |
| 9 | B | 1.2.4 | Management *of* the cloud is managing the resources themselves: autoscaling, template deployment, automatic replacement, alerting. A is management *in* the cloud — the interfaces you use. | [Manageability](https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/5-manageability-cloud) |
| 10 | i–IaaS, ii–PaaS, iii–SaaS, iv–IaaS, v–PaaS | 1.3.1, 1.3.2, 1.3.3, 1.3.4 | Lift-and-shift and rapid test-environment replication are the two named IaaS scenarios. Development frameworks and analytics or business intelligence tooling are the two named PaaS scenarios. A ready-to-use finance application is SaaS. Score one point per correct pair, then round. | [IaaS](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/2-describe-infrastructure-service) · [PaaS](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/3-describe-platform-service) · [SaaS](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/4-describe-software-service) |
| 11 | A | 1.1.2 (carry-forward) | In SaaS the provider manages nearly the whole stack including application maintenance, while the customer keeps data, identity and access, and device posture. | [Software as a Service](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/4-describe-software-service) |
| 12 | B | 1.1.5 (carry-forward) | Not paying for idle capacity is a stated benefit of the consumption model; you add resources when demand rises and release them when it falls. | [Consumption-based model](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/6-describe-consumption-based-model) |