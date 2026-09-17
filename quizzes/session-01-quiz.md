# Session 1 Quiz — Cloud Computing Foundations

**Time:** 15 minutes · **Items:** 12 · **Composition:** 12 new, 0 carry-forward
**Objectives:** 1.1.1, 1.1.2, 1.1.3, 1.1.4, 1.1.5
**Target:** 80%

Definition-and-recall level. This is the first quiz of the course, so it establishes the
format rather than stretching learners.

---

## Questions

**1.** Which statement best describes cloud computing?

- A. Running virtualization software on servers your organization owns
- B. Delivering computing services such as compute, storage, and networking over the internet
- C. Backing up on-premises data to a second building
- D. Buying servers in bulk to lower the cost per unit

**2.** Under the shared responsibility model, which items remain your responsibility no matter which cloud service type you use? (Select all that apply.)

- A. The data and information you store in the cloud
- B. The physical hosts running your workloads
- C. The accounts and identities in your environment
- D. The physical network in the datacenter
- E. The devices allowed to connect to your cloud resources

**3.** Which three items are always the cloud provider's responsibility?

- A. Operating systems, applications, and network controls
- B. The physical datacenter, the physical network, and the physical hosts
- C. Identity and access, data, and devices
- D. Middleware, runtime, and application code

**4.** You deploy a virtual machine in Azure and install a database on it yourself. Who is responsible for applying database patches?

- A. Microsoft, because the VM runs in Microsoft's datacenter
- B. You, because you installed and manage the software on the VM
- C. Neither party; database patching is automatic in Azure
- D. Microsoft for security patches, you for feature updates

**5.** Which cloud service type places the most responsibility on the customer?

- A. SaaS
- B. PaaS
- C. IaaS
- D. All three place equal responsibility on the customer

**6.** An organization runs a cloud environment used only by itself, hosted in its own datacenter. Which cloud model is this?

- A. Public cloud
- B. Private cloud
- C. Hybrid cloud
- D. Multicloud

**7.** What most clearly distinguishes a public cloud from a private cloud?

- A. A public cloud is always cheaper
- B. A public cloud is available to anyone who wants to purchase the services
- C. A public cloud cannot be used for regulated workloads
- D. A public cloud has no service-level guarantees

**8.** A retailer keeps its customer database on its own private cloud infrastructure but wants to add public cloud capacity during a seasonal sales spike. Which cloud model does this describe?

- A. Public cloud
- B. Private cloud
- C. Hybrid cloud
- D. Sovereign cloud

**9.** An organization uses services from two different public cloud providers and manages resources and security in both. What is this arrangement called?

- A. Hybrid cloud
- B. Multicloud
- C. Private cloud
- D. Community cloud

**10.** A startup has no existing hardware, expects unpredictable growth, and wants to avoid buying servers. Which cloud model is the most appropriate starting point, and why?

- A. Private cloud, because it gives complete control over resources and security
- B. Public cloud, because it requires no capital expenditure to scale up
- C. Hybrid cloud, because it provides the most flexibility
- D. Private cloud, because data is not collocated with other tenants' data

**11.** In traditional IT budgeting, which term describes up-front spending on physical infrastructure such as servers and datacenter space?

- A. Operational expenditure (OpEx)
- B. Capital expenditure (CapEx)
- C. Consumption-based spending
- D. Total cost of ownership

**12.** Which statement about the consumption-based model is correct?

- A. You pay a fixed monthly fee regardless of usage
- B. You buy capacity a year in advance to guarantee availability
- C. You pay for the resources you use and can release them when demand drops
- D. You pay only for storage; compute is included

---

## Answer key

| Q | Answer | Objective | Why | Source |
| --- | --- | --- | --- | --- |
| 1 | B | 1.1.1 | Cloud computing is the delivery of computing services over the internet. A describes on-premises virtualization, and C describes offsite backup — neither involves renting a provider's services. | [What is cloud computing](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/3-what-cloud-compute) |
| 2 | A, C, E | 1.1.2 | Data, identities and accounts, and connecting devices stay with the customer in every service type. B and D are always the provider's. | [Shared responsibility model](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/4-describe-shared-responsibility-model) |
| 3 | B | 1.1.2 | The provider always owns the physical datacenter, physical network, and physical hosts. A and D vary by service type; C is always the customer's. | [Shared responsibility model](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/4-describe-shared-responsibility-model) |
| 4 | B | 1.1.2 | Software you install on an IaaS VM is yours to patch and maintain. The provider's responsibility stops at the physical infrastructure and connectivity. Contrast with a managed database service, where the provider maintains the engine. | [Shared responsibility model](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/4-describe-shared-responsibility-model) |
| 5 | C | 1.1.2 | IaaS leaves the customer responsible for the operating system and everything above it. SaaS is the opposite end; PaaS sits between the two. | [Shared responsibility model](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/4-describe-shared-responsibility-model) |
| 6 | B | 1.1.3 | A private cloud serves a single organization and may be hosted on-site, in a dedicated offsite datacenter, or by a third party. Hosting location alone does not make it hybrid. | [Define cloud models](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/5-define-cloud-models) |
| 7 | B | 1.1.3 | General availability to any purchaser is the defining difference. Cost, compliance suitability, and SLAs vary and are not the distinguishing characteristic. | [Define cloud models](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/5-define-cloud-models) |
| 8 | C | 1.1.4 | Hybrid interconnects private and public cloud, which is what lets a private environment surge into public capacity for temporary demand. | [Define cloud models](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/5-define-cloud-models) |
| 9 | B | 1.1.3 | Multicloud means using two or more public cloud providers. Hybrid is public plus private, which is not what is described. | [Define cloud models](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/5-define-cloud-models) |
| 10 | B | 1.1.4 | No capital expenditure to scale up is a listed public cloud advantage and matches a startup with no hardware. A and D are private cloud advantages that require buying hardware. | [Define cloud models](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/5-define-cloud-models) |
| 11 | B | 1.1.5 | CapEx is up-front spending on physical infrastructure; OpEx is ongoing spending on services, which is how cloud consumption is classified. | [Consumption-based model](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/6-describe-consumption-based-model) |
| 12 | C | 1.1.5 | The consumption-based model means paying for what you use and releasing resources when demand drops, with no up-front hardware cost. A and B describe the capacity-planning problem the model removes. | [Consumption-based model](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/6-describe-consumption-based-model) |
