# Final Readiness Set — Session 12

**Time:** 45 minutes, timed, closed-book · **Items:** 45
**Coverage:** all 57 objectives
**Target:** 85% overall, with no domain below 75%

Administer under exam conditions: 45 minutes, no notes, no discussion, no lookups. That
matches the exam duration for Fundamentals exams. Learners should also take the
[official Microsoft practice assessment](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-900/practice/assessment?assessment-type=practice&assessmentId=23)
— this set is a complement to it, not a replacement, and only Microsoft's assessment
reflects the real item styles and interface.

## Domain distribution

| Domain | Exam weight | Items | Share |
| --- | --- | --- | --- |
| 1. Describe cloud concepts | 25–30% | 12 (Q1–Q12) | 26.7% |
| 2. Describe Azure architecture and services | 35–40% | 18 (Q13–Q30) | 40.0% |
| 3. Describe Azure management and governance | 30–35% | 15 (Q31–Q45) | 33.3% |

Score each domain separately. A learner at 85% overall who is at 60% in Domain 3 is not
ready, which is why the per-domain floor exists.

---

## Questions

### Domain 1 — Describe cloud concepts (Q1–Q12)

**1.** An organization stops buying servers and instead rents compute, storage, and networking from a provider over the internet, releasing resources when it no longer needs them. Which characteristic of cloud computing does this describe?

- A. Virtualization
- B. Consumption of services delivered over the internet rather than owned infrastructure
- C. Disaster recovery
- D. Containerization

**2.** A company runs an application on an Azure virtual machine and installs its own web server software on it. Which responsibilities belong to the company? (Select all that apply.)

- A. Patching the web server software
- B. Patching the guest operating system
- C. Maintaining the physical host hardware
- D. Controlling who has access to the application's data
- E. Securing the datacenter's physical perimeter

**3.** (Match each situation to the cloud model that fits best: public, private, hybrid, multicloud.)

- i. A government department requires resources dedicated to itself with complete control of security
- ii. An insurer keeps its policy database on dedicated infrastructure and runs its quote calculator in a provider's cloud, connected together
- iii. A media startup runs entirely on services bought from one cloud provider
- iv. A bank runs workloads with two separate public cloud providers and manages security in both

**4.** Which statement best explains why cloud spending is classified as an operating expense?

- A. Cloud resources depreciate over five years
- B. You pay for services as you consume them rather than purchasing infrastructure up front
- C. Cloud providers invoice annually
- D. Cloud resources cannot be capitalized because they are virtual

**5.** A team has two workloads: a steady production API that will run for three years on a known VM size, and an overnight batch job that can be interrupted and restarted. Which pricing approach suits each?

- A. Spot for the API; reservation for the batch job
- B. Reservation for the API; spot for the batch job
- C. Pay-as-you-go for both
- D. Savings plan for the API; reservation for the batch job

**6.** Which requirement most clearly points to a serverless service?

- A. The workload needs a specific Linux kernel version
- B. Work arrives unpredictably as messages and each unit finishes in seconds
- C. Users need a full managed Windows desktop
- D. The workload requires a dedicated physical host

**7.** An application adds instances during a sale and removes them afterward, and separately the team increases the RAM on its database server. Which two scaling types are in use, in that order?

- A. Vertical, then horizontal
- B. Horizontal, then vertical
- C. Both horizontal
- D. Both vertical

**8.** Which statement describes cost predictability as a cloud benefit?

- A. Costs never change once resources are deployed
- B. You can track usage in real time, analyze patterns, and forecast future spend, including with the pricing calculator
- C. All Azure services cost the same in every region
- D. Costs are fixed by a service-level agreement

**9.** An organization wants deployments to consistently meet its technical standards, and wants to be alerted when a deployed resource drifts out of compliance with its baseline. Which cloud benefit category does this describe?

- A. Scalability
- B. Security and governance
- C. Manageability in the cloud
- D. Elasticity

**10.** Which list contains only *management of the cloud* capabilities?

- A. Azure portal, Azure CLI, REST APIs
- B. Autoscaling deployments, template-based deployment, automatic replacement of failing resources, metric-based alerts
- C. Purchasing subscriptions, assigning licenses
- D. Writing application code, running tests

**11.** A team wants a managed platform with built-in scalability and multitenancy so developers write less infrastructure code, but they still own and deploy the application. A second team needs full control of the operating system for a lift-and-shift migration. Which service types fit, in that order?

- A. IaaS, then PaaS
- B. PaaS, then IaaS
- C. SaaS, then PaaS
- D. PaaS, then SaaS

**12.** (Match each purchase to the cloud service type: IaaS, PaaS, or SaaS.)

- i. A subscription to a hosted expense-tracking application used by the finance team as-is
- ii. Virtual machines the customer patches and configures
- iii. A managed analytics and business intelligence service the customer points at its own data
- iv. A messaging and email product delivered ready to use

### Domain 2 — Describe Azure architecture and services (Q13–Q30)

**13.** A workload must remain available if an entire Azure region becomes unavailable, and data must stay within the same geography for compliance. Which capability is designed for this?

- A. Availability zones
- B. Region pairs
- C. Availability sets
- D. Resource groups

**14.** (For each statement, answer yes or no.)

- i. An availability-zone-enabled region contains a minimum of three separate availability zones.
- ii. Customers choose which individual datacenter within a region their resources are deployed to.
- iii. Availability zones within a region have independent power, cooling, and networking.

**15.** A company wants development and production workloads billed separately, with different access policies, and wants each project's resources grouped so that all of a project's resources can be deleted together. Which two constructs does this describe, in order?

- A. Management groups, then subscriptions
- B. Subscriptions, then resource groups
- C. Resource groups, then tags
- D. Tags, then subscriptions

**16.** An organization with 30 subscriptions must apply one governance rule and one role assignment that reach every subscription and every resource beneath them, without repeating the assignment. Where should these be applied, and what makes it work?

- A. On each subscription, because assignments cannot be made higher
- B. At a management group, because subscriptions and their contents inherit its conditions
- C. On a resource group, because resource groups can contain subscriptions
- D. In Microsoft Entra ID, because identity governs resource configuration

**17.** Which option describes the compute choice that requires no operating system management by the customer and runs code only when an event triggers it?

- A. Azure Virtual Machines
- B. Azure Container Instances
- C. Azure Functions
- D. Azure Virtual Desktop

**18.** A retailer needs identical, load-balanced virtual machines whose count rises and falls with demand, and separately needs to protect a pair of legacy VMs from a single rack or planned-maintenance failure within one region. Which two options fit, in order?

- A. Availability set, then virtual machine scale set
- B. Virtual machine scale set, then availability set
- C. Azure Virtual Desktop, then availability set
- D. Virtual machine scale set, then region pair

**19.** Which statement about virtual machine provisioning is correct?

- A. Disks and networking are created automatically and cannot be chosen
- B. You choose the size (family, vCPU, RAM), storage disks, and networking such as the virtual network, network interface, and optionally a public IP
- C. VM size cannot be changed after creation under any circumstances
- D. A VM must be deployed to a specific datacenter

**20.** Which requirement is best served by Azure App Service rather than by virtual machines or containers?

- A. Running a legacy application that requires a specific OS build and custom drivers
- B. Hosting a web app and REST API with automatic scaling and Git-based deployment, without managing an operating system
- C. Orchestrating a fleet of containers across many nodes
- D. Delivering managed Windows desktops to remote workers

**21.** Which statements about Azure virtual networks are correct? (Select all that apply.)

- A. A virtual network can be divided into subnets
- B. Network security groups can allow or block traffic based on source, destination, port, and protocol
- C. Virtual network peering routes traffic between peered networks over the public internet
- D. Peered virtual networks can be in different regions
- E. Azure routes traffic between subnets in a virtual network by default

**22.** (Match each requirement to the correct option: site-to-site VPN, point-to-site VPN, ExpressRoute, Azure DNS, private endpoint.)

- i. A remote worker's laptop needs an encrypted connection into a virtual network
- ii. A datacenter needs private connectivity to Azure that does not use the public internet
- iii. A storage account must be reachable only from inside a virtual network, using a private IP from its address space
- iv. An on-premises network gateway needs an encrypted tunnel to an Azure virtual network over the internet
- v. A team needs to host DNS records for its domain using the same credentials and billing as its other Azure services

**23.** Which statement about endpoints is correct?

- A. A private endpoint has a public IP address but restricts access with a firewall rule
- B. A public endpoint has a public IP address and can be accessed from anywhere in the world
- C. Public and private endpoints are two names for the same feature
- D. Private endpoints can only be used with virtual machines

**24.** (Match each requirement to the Azure Storage service: Blob Storage, Azure Files, Queue Storage, Azure Disk Storage, Table Storage.)

- i. Block-level volume attached to a virtual machine
- ii. NoSQL store for large amounts of structured, non-relational data
- iii. Object store for unstructured media and backup data
- iv. Messages held for asynchronous processing between application components
- v. Managed share mountable over SMB or NFS by multiple clients at once

**25.** Data must be retained for seven years, is accessed roughly twice a year, must be immediately readable when accessed, and cost should be as low as possible given that constraint. Which access tier fits?

- A. Hot
- B. Cool or cold
- C. Archive
- D. Premium page blobs

**26.** Which statement about Azure Storage redundancy is correct?

- A. LRS replicates data across three availability zones in the primary region
- B. ZRS replicates data synchronously across three availability zones in the primary region
- C. GRS keeps all copies within a single datacenter
- D. Secondary-region data is readable by default with GRS, before any failover

**27.** A workload needs Azure Files shares accessible over both SMB and NFS, with high performance. Which storage account type is required?

- A. Standard general-purpose v2
- B. Premium block blobs
- C. Premium file shares
- D. Premium page blobs

**28.** An organization must move 70 TB into Azure over a constrained network link, and separately needs a repeatable command-line way to copy and one-way synchronize blobs between two storage accounts. Which two tools fit, in order?

- A. AzCopy, then Azure Data Box
- B. Azure Data Box, then AzCopy
- C. Azure File Sync, then Azure Storage Explorer
- D. Azure Migrate, then Azure File Sync

**29.** (For each statement, answer yes or no.)

- i. Microsoft Entra ID is the cloud-based identity and access management service, and Microsoft Entra Connect synchronizes identities from on-premises Active Directory.
- ii. Microsoft Entra Domain Services requires you to deploy and patch your own domain controllers in Azure.
- iii. Single sign-on lets one identity access multiple applications, and its security depends on the strength of the initial authentication.
- iv. Windows Hello for Business, the Microsoft Authenticator app, and FIDO2 security keys are passwordless options.

**30.** (For each statement, answer yes or no.)

- i. B2B collaboration represents external users in your directory, typically as guests.
- ii. Conditional Access can require multifactor authentication only for sign-ins from unexpected locations, while allowing known locations without a second factor.
- iii. Azure RBAC permissions assigned at a management group are inherited by subscriptions, resource groups, and resources beneath it.
- iv. Zero Trust assumes the internal network is inherently trustworthy.
- v. In defense in depth, the data layer is at the center and every other layer exists to protect it.
- vi. Microsoft Defender for Cloud calculates a secure score and can extend protection to AWS and GCP resources.

### Domain 3 — Describe Azure management and governance (Q31–Q45)

**31.** Which factors increase what a deployed workload costs in Azure? (Select all that apply.)

- A. Choosing a region with higher local power and labor costs
- B. Leaving disks and public IP addresses in place after deleting their virtual machine
- C. Applying more tags to the resources
- D. Transferring data out of Azure datacenters across billing zones
- E. Purchasing a third-party solution through Azure Marketplace

**32.** A team must produce a cost estimate for a proposed design, comparing two regions, before anything is deployed. Which tool fits, and what is its key limitation?

- A. Cost analysis; it only shows spend that has already occurred
- B. The pricing calculator; it produces estimates only and provisions nothing
- C. Azure Advisor; it only reviews resources that already exist
- D. Azure Monitor; it reports telemetry rather than cost

**33.** Which capability shows accumulated Azure costs over time, broken down by subscription, resource group, or service, to identify spending trends?

- A. The pricing calculator
- B. Microsoft Cost Management cost analysis
- C. Azure Service Health
- D. Resource locks

**34.** An organization needs monthly spend reported by internal cost center and by environment, and wants the required metadata to be reapplied automatically if someone removes it. What combination achieves this?

- A. Resource locks plus RBAC
- B. Tags plus Azure Policy enforcement
- C. Management groups plus budgets
- D. Purview plus Advisor

**35.** Which requirement is Microsoft Purview designed to address?

- A. Restricting which regions resources may be deployed to
- B. Discovering and classifying sensitive data across on-premises, multicloud, and SaaS data, with end-to-end lineage
- C. Detecting brute-force attacks against virtual machines
- D. Estimating the monthly cost of a proposed architecture

**36.** Which statements about Azure Policy are correct? (Select all that apply.)

- A. It can prevent noncompliant resources from being created
- B. It evaluates resources that existed before the policy was assigned
- C. It groups related policy definitions into initiatives
- D. It determines which users may perform actions on a resource
- E. It can remediate some noncompliant configurations automatically

**37.** A production resource group must be protected so that nobody — including subscription owners — can delete it accidentally, while engineers can still update the resources inside. What is applied, and what is the consequence for an owner who needs to delete it later?

- A. A ReadOnly lock; the owner can delete after re-authenticating
- B. A Delete lock; the owner must remove the lock first, because locks apply regardless of RBAC
- C. An Azure Policy deny assignment; the owner must request an exception
- D. The Reader role for all users; the owner is unaffected

**38.** Which statement about the ways to interact with Azure is correct?

- A. The Azure CLI and Azure PowerShell differ in capability, with the CLI limited to read operations
- B. Azure Cloud Shell is browser-based, already authenticated to your credentials, and supports both Azure PowerShell and the Azure CLI
- C. The Azure portal requires local installation on Windows
- D. Only the portal communicates with Azure Resource Manager

**39.** An enterprise runs servers in its own datacenter and Kubernetes clusters in another public cloud, and wants to apply Azure Policy and inventory tracking to all of it from Azure. Which service enables this?

- A. Azure Migrate
- B. Azure Arc
- C. Azure Virtual Desktop
- D. Azure Data Box

**40.** Which statement best describes infrastructure as code?

- A. Storing infrastructure diagrams alongside application source code
- B. Defining and provisioning infrastructure through code and templates instead of manual configuration, so deployments are repeatable and reviewable
- C. Writing application code that scales automatically
- D. Running scripted health checks against production resources

**41.** Which statements about Azure Resource Manager and ARM templates are correct? (Select all that apply.)

- A. Every request from the portal, CLI, PowerShell, SDKs, and APIs passes through Resource Manager
- B. Resource Manager authenticates and authorizes requests before passing them to the target service
- C. ARM templates use declarative JSON to describe the desired resources
- D. ARM templates require you to specify the deployment order of every resource manually
- E. The same template can be redeployed to produce a consistent result

**42.** A team wants a prioritized list of suggested improvements to its existing Azure environment across reliability, security, performance, operational excellence, and cost. Which service provides this?

- A. Azure Advisor
- B. Azure Service Health
- C. Azure Monitor
- D. Microsoft Purview

**43.** An engineer needs to know whether a specific virtual machine's current problem originates with Azure or with their own configuration. Which view answers that?

- A. Azure Status
- B. Service Health
- C. Resource Health
- D. Azure Advisor

**44.** (Match each need to the Azure Monitor capability: Log Analytics, Azure Monitor alerts, Application Insights.)

- i. Notify an on-call group when a metric threshold is breached
- ii. Query collected log data to investigate a pattern of errors
- iii. Monitor a web application's response times, failure rates, and dependency calls, with availability tests

**45.** A team is told their Azure bill is too high. They want both a report of where the money actually went last month and a list of Azure-generated recommendations for reducing spend. Which two tools should they use, in order?

- A. The pricing calculator, then Azure Monitor
- B. Microsoft Cost Management cost analysis, then Azure Advisor
- C. Azure Advisor, then resource locks
- D. Azure Service Health, then Microsoft Purview

---

## Answer key

### Domain 1

| Q | Answer | Objective | Why | Source |
| --- | --- | --- | --- | --- |
| 1 | B | 1.1.1 | Cloud computing is consuming computing services over the internet rather than owning infrastructure, with the ability to release resources. Virtualization and containerization are technologies, not the defining characteristic. | [What is cloud computing](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/3-what-cloud-compute) |
| 2 | A, B, D | 1.1.2 | On IaaS the customer owns installed software, the guest OS, and — in every model — the data and its access. Physical hosts and datacenter security are always the provider's. | [Shared responsibility model](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/4-describe-shared-responsibility-model) |
| 3 | i–private, ii–hybrid, iii–public, iv–multicloud | 1.1.3, 1.1.4 | Dedicated single-entity environment with full control is private; interconnected private and public is hybrid; buying everything from one provider is public; two public providers is multicloud. | [Define cloud models](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/5-define-cloud-models) |
| 4 | B | 1.1.5 | Paying for services as consumed makes cloud spending operational rather than capital expenditure. | [Consumption-based model](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/6-describe-consumption-based-model) |
| 5 | B | 1.1.6 | Reservations suit steady, predictable workloads on known resources; spot suits interruption-tolerant work using unused capacity at lower prices. | [Cost factors](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/2-describe-factors-affect-costs-azure) |
| 6 | B | 1.1.7 | Unpredictable, short, event-triggered units of work are the serverless case; nothing needs to remain provisioned between events. | [Azure functions](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/6-functions) |
| 7 | B | 1.2.1 | Adding and removing instances is horizontal scaling; increasing RAM on an existing resource is vertical scaling. | [High availability and scalability](https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/2-high-availability-scalability-cloud) |
| 8 | B | 1.2.2 | Cost predictability comes from real-time usage tracking, monitoring, analytics on patterns, and estimation tools such as the pricing calculator. | [Reliability and predictability](https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/3-reliability-predictability-cloud) |
| 9 | B | 1.2.3 | Templates that make deployments meet standards, and auditing that flags resources out of compliance with a baseline, are the governance and security benefits. | [Security and governance](https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/4-security-governance-cloud) |
| 10 | B | 1.2.4 | Management *of* the cloud is autoscaling, template deployment, automatic replacement of failing resources, and metric-based alerts. A is management *in* the cloud. | [Manageability](https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/5-manageability-cloud) |
| 11 | B | 1.3.1, 1.3.2 | A managed development platform with built-in scalability and multitenancy is PaaS; full OS control for lift-and-shift is IaaS. | [PaaS](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/3-describe-platform-service) · [IaaS](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/2-describe-infrastructure-service) |
| 12 | i–SaaS, ii–IaaS, iii–PaaS, iv–SaaS | 1.3.3, 1.3.4 | Ready-to-use applications are SaaS; customer-managed VMs are IaaS; managed analytics tooling the customer points at its own data is PaaS. | [SaaS](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/4-describe-software-service) |

### Domain 2

| Q | Answer | Objective | Why | Source |
| --- | --- | --- | --- | --- |
| 13 | B | 2.1.1 | Region pairs replicate across a geography at least 300 miles apart, keeping data in the same geography for residency purposes. Availability zones protect within a region only. | [Azure physical infrastructure](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/5-describe-azure-physical-infrastructure) |
| 14 | i–yes, ii–no, iii–yes | 2.1.2, 2.1.3 | Zone-enabled regions have at least three zones with independent power, cooling, and networking. Customers deploy to regions and zones; they do not select individual datacenters. | [Azure physical infrastructure](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/5-describe-azure-physical-infrastructure) |
| 15 | B | 2.1.4, 2.1.5 | Subscriptions separate billing and access control; resource groups group resources so actions — including deletion — apply to the whole group. | [Azure management infrastructure](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/6-describe-azure-management-infrastructure) |
| 16 | B | 2.1.6, 2.1.7 | Management groups sit above subscriptions; policy and RBAC assignments there are inherited all the way down, which is why one assignment suffices. | [Azure management infrastructure](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/6-describe-azure-management-infrastructure) |
| 17 | C | 2.2.1 | Azure Functions is the event-driven serverless option with no VMs or containers to maintain. Container Instances still involves a container you supply; VMs require OS management. | [Azure functions](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/6-functions) |
| 18 | B | 2.2.2 | Scale sets give identical load-balanced VMs that scale with demand; availability sets spread VMs across update and fault domains for in-region resiliency. | [Azure virtual machines](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/2-virtual-machines) |
| 19 | B | 2.2.3 | Size, disks, and networking are all chosen at provisioning time. Deployment targets a region — and optionally a zone — not a specific datacenter. | [Azure virtual machines](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/2-virtual-machines) |
| 20 | B | 2.2.4 | App Service is the managed hosting option for web apps and APIs with automatic scaling and Git-based deployment. A needs a VM; C needs AKS; D needs Azure Virtual Desktop. | [Application hosting options](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/7-describe-application-hosting-options) |
| 21 | A, B, D, E | 2.2.5 | Subnets, network security groups, cross-region peering, and default inter-subnet routing are all correct. C is false — peered traffic stays private on the Microsoft backbone. | [Azure virtual networking](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/2-virtual-network) |
| 22 | i–point-to-site VPN, ii–ExpressRoute, iii–private endpoint, iv–site-to-site VPN, v–Azure DNS | 2.2.5, 2.2.6 | Each option maps to exactly one requirement. Score per pair. | [VPNs](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/3-virtual-private-networks) · [ExpressRoute](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/4-expressroute) · [Azure DNS](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/5-domain-name-system) |
| 23 | B | 2.2.6 | A public endpoint has a public IP and is reachable from anywhere; a private endpoint uses a private IP inside a virtual network. | [Azure virtual networking](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/2-virtual-network) |
| 24 | i–Azure Disk Storage, ii–Table Storage, iii–Blob Storage, iv–Queue Storage, v–Azure Files | 2.3.1 | The five core storage services and their canonical uses. Score per pair. | [Azure storage services](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/4-describe-azure-storage-services) |
| 25 | B | 2.3.2 | Cool (30+ days) and cold (90+ days) lower storage cost while keeping data immediately readable. Archive is cheaper still but requires rehydration, so it fails the immediacy requirement. | [Azure storage services](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/4-describe-azure-storage-services) |
| 26 | B | 2.3.3 | ZRS replicates synchronously across three availability zones in the primary region. LRS keeps three copies in one datacenter; GRS adds an asynchronous secondary region; secondary data is not readable before failover unless a read-access variant is used. | [Azure storage redundancy](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/3-redundancy) |
| 27 | C | 2.3.4 | Premium file shares is the account type for Azure Files that supports both SMB and NFS shares at high performance. | [Azure storage accounts](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/2-accounts) |
| 28 | B | 2.3.5, 2.3.6 | Data Box handles large offline transfers when bandwidth is the constraint; AzCopy is the command-line tool for copying and one-direction synchronization between storage accounts. | [Data migration options](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/6-identify-azure-data-migration-options) · [File movement options](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/7-identify-azure-file-movement-options) |
| 29 | i–yes, ii–no, iii–yes, iv–yes | 2.4.1, 2.4.2 | Entra Domain Services is a managed domain — Azure deploys and maintains the domain controllers, so ii is false. Score per statement. | [Directory services](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/2-directory-services) · [Authentication methods](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/3-authentication-methods) |
| 30 | i–yes, ii–yes, iii–yes, iv–no, v–yes, vi–yes | 2.4.3, 2.4.4, 2.4.5, 2.4.6, 2.4.7, 2.4.8 | Only iv is false: Zero Trust assumes breach and does not treat the internal network as inherently trustworthy. Score per statement. | [External identities](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/4-external-identities) · [Conditional access](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/5-conditional-access) · [RBAC](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/6-role-based-access-control) · [Zero Trust](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/7-describe-zero-trust-model) · [Defense in depth](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/8-describe-defense-depth) · [Defender for Cloud](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/9-describe-microsoft-defender-for-cloud) |

### Domain 3

| Q | Answer | Objective | Why | Source |
| --- | --- | --- | --- | --- |
| 31 | A, B, D, E | 3.1.1 | Geography, orphaned resources left behind by deprovisioning, outbound data transfer priced by billing zone, and Marketplace third-party charges are all cost factors. Tag count is not. | [Cost factors](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/2-describe-factors-affect-costs-azure) |
| 32 | B | 3.1.2 | The pricing calculator estimates before deployment and supports comparing regions; its limitation is that prices are estimates and nothing is provisioned or charged. | [Explore the pricing calculator](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/3-compare-pricing-total-cost-of-ownership-calculators) |
| 33 | B | 3.1.3 | Cost analysis shows accumulated costs over time and aggregates by subscription, resource group, or service to reveal trends. | [Microsoft Cost Management tool](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/6-describe-azure-tool) |
| 34 | B | 3.1.4 | Tags supply the cost-center and environment metadata; Azure Policy can require tags on new resources and reapply removed ones. Tags are not inherited, so enforcement matters. | [Purpose of tags](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/7-describe-purpose-of-tags) |
| 35 | B | 3.2.1 | Purview's unified data governance covers automated discovery, sensitive data classification, and end-to-end lineage across on-premises, multicloud, and SaaS data. | [Purpose of Microsoft Purview](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/2-describe-purpose-microsoft-purview) |
| 36 | A, B, C, E | 3.2.2 | Policy blocks noncompliant creation, evaluates pre-existing resources, groups definitions into initiatives, and can remediate some configurations. D is RBAC's job. | [Purpose of Azure Policy](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/3-describe-purpose-azure-policy) |
| 37 | B | 3.2.3 | A Delete lock blocks deletion while allowing reads and updates, and it applies regardless of RBAC — even an Owner must remove the lock first. | [Purpose of resource locks](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/4-describe-purpose-resource-locks) |
| 38 | B | 3.3.1, 3.3.2 | Cloud Shell is browser-based, inherits your credentials and permissions, and supports both Azure PowerShell and the Azure CLI. The CLI and PowerShell are functionally equivalent; the portal is web-based. | [Tools for interacting with Azure](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/2-describe-interacting-azure) |
| 39 | B | 3.3.3 | Azure Arc projects non-Azure servers, Kubernetes clusters, and data services into Azure Resource Manager so Azure governance and management apply consistently. | [Purpose of Azure Arc](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/3-describe-purpose-of-azure-arc) |
| 40 | B | 3.3.4 | Infrastructure as code means managing and provisioning infrastructure through code and templates instead of manual configuration, which is what makes deployments repeatable. | [ARM and ARM templates](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/4-describe-azure-resource-manager-azure-arm-templates) |
| 41 | A, B, C, E | 3.3.5 | All requests pass through Resource Manager, which authenticates and authorizes them; templates are declarative JSON and are repeatable. D is false — Resource Manager orchestrates dependency order for you. | [ARM and ARM templates](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/4-describe-azure-resource-manager-azure-arm-templates) |
| 42 | A | 3.4.1 | Advisor recommends improvements across exactly those five categories: Reliability, Security, Performance, Operational Excellence, and Cost. | [Purpose of Azure Advisor](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/2-describe-purpose-of-azure-advisor) |
| 43 | C | 3.4.2 | Resource Health reports on an individual resource and whether the issue is Azure's or yours. Azure Status is global; Service Health covers the services you use. | [Azure Service Health](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/3-describe-azure-service-health) |
| 44 | i–Azure Monitor alerts, ii–Log Analytics, iii–Application Insights | 3.4.3 | Alerts notify through action groups; Log Analytics is where queries run; Application Insights monitors application performance, usage, dependencies, and availability. Score per pair. | [Describe Azure Monitor](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/4-describe-azure-monitor) |
| 45 | B | 3.1.3, 3.4.1 | Cost analysis reports where the money went; Advisor's Cost category generates recommendations for reducing spend. The pricing calculator estimates future designs and cannot report actual spend. | [Microsoft Cost Management tool](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/6-describe-azure-tool) · [Purpose of Azure Advisor](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/2-describe-purpose-of-azure-advisor) |

## Debrief procedure

1. Score by domain before discussing any item. Write the three domain percentages on the board.
2. Walk every missed item, naming the objective ID. Learners mark each miss on their objective checklist.
3. Rank the objectives by number of learners who missed them. The top three become the Session 12 gap clinic.
4. Only then discuss the overall score. Learners fixate on the total and ignore the domain split, which is the part that decides whether they are ready.

**Scoring:** every item is worth exactly one point, so the domain totals stay at 12, 18,
and 15 out of 45 and the set keeps its weight alignment. Multi-select items (Q2, Q21, Q31,
Q36, Q41) are all-or-nothing. Multi-part items (Q3, Q12, Q14, Q22, Q24, Q29, Q30, Q44)
earn fractional credit — correct parts divided by total parts. Do not award one point per
pair; that would inflate Domain 2, which carries most of the multi-part items, to roughly
half the total.
