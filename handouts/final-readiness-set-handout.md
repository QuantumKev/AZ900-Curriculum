# Final Readiness Set — Session 12

**Name:** <span class="blank"></span>  **Session:** <span class="blank"></span>

**Time:** 45 minutes, timed, closed-book · **Items:** 45 · **Target:** 85% overall, with no domain below 75%

Answer every question. For *select all that apply*, mark every correct option. For
matching questions, write the matching term next to each numeral. For yes/no sets,
write yes or no next to each numeral. Your instructor reviews every answer in class
immediately afterward.

---

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

- i. A government department requires resources dedicated to itself with complete control of security &nbsp; <span class="blank"></span>
- ii. An insurer keeps its policy database on dedicated infrastructure and runs its quote calculator in a provider's cloud, connected together &nbsp; <span class="blank"></span>
- iii. A media startup runs entirely on services bought from one cloud provider &nbsp; <span class="blank"></span>
- iv. A bank runs workloads with two separate public cloud providers and manages security in both &nbsp; <span class="blank"></span>

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

**12.** (Match each purchase to the cloud service type: IaaS, PaaS, or SaaS.) ### Domain 2 — Describe Azure architecture and services (Q13–Q30)

- i. A subscription to a hosted expense-tracking application used by the finance team as-is &nbsp; <span class="blank"></span>
- ii. Virtual machines the customer patches and configures &nbsp; <span class="blank"></span>
- iii. A managed analytics and business intelligence service the customer points at its own data &nbsp; <span class="blank"></span>
- iv. A messaging and email product delivered ready to use &nbsp; <span class="blank"></span>

**13.** A workload must remain available if an entire Azure region becomes unavailable, and data must stay within the same geography for compliance. Which capability is designed for this?

- A. Availability zones
- B. Region pairs
- C. Availability sets
- D. Resource groups

**14.** (For each statement, answer yes or no.)

- i. An availability-zone-enabled region contains a minimum of three separate availability zones. &nbsp; <span class="blank"></span>
- ii. Customers choose which individual datacenter within a region their resources are deployed to. &nbsp; <span class="blank"></span>
- iii. Availability zones within a region have independent power, cooling, and networking. &nbsp; <span class="blank"></span>

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

- i. A remote worker's laptop needs an encrypted connection into a virtual network &nbsp; <span class="blank"></span>
- ii. A datacenter needs private connectivity to Azure that does not use the public internet &nbsp; <span class="blank"></span>
- iii. A storage account must be reachable only from inside a virtual network, using a private IP from its address space &nbsp; <span class="blank"></span>
- iv. An on-premises network gateway needs an encrypted tunnel to an Azure virtual network over the internet &nbsp; <span class="blank"></span>
- v. A team needs to host DNS records for its domain using the same credentials and billing as its other Azure services &nbsp; <span class="blank"></span>

**23.** Which statement about endpoints is correct?

- A. A private endpoint has a public IP address but restricts access with a firewall rule
- B. A public endpoint has a public IP address and can be accessed from anywhere in the world
- C. Public and private endpoints are two names for the same feature
- D. Private endpoints can only be used with virtual machines

**24.** (Match each requirement to the Azure Storage service: Blob Storage, Azure Files, Queue Storage, Azure Disk Storage, Table Storage.)

- i. Block-level volume attached to a virtual machine &nbsp; <span class="blank"></span>
- ii. NoSQL store for large amounts of structured, non-relational data &nbsp; <span class="blank"></span>
- iii. Object store for unstructured media and backup data &nbsp; <span class="blank"></span>
- iv. Messages held for asynchronous processing between application components &nbsp; <span class="blank"></span>
- v. Managed share mountable over SMB or NFS by multiple clients at once &nbsp; <span class="blank"></span>

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

- i. Microsoft Entra ID is the cloud-based identity and access management service, and Microsoft Entra Connect synchronizes identities from on-premises Active Directory. &nbsp; <span class="blank"></span>
- ii. Microsoft Entra Domain Services requires you to deploy and patch your own domain controllers in Azure. &nbsp; <span class="blank"></span>
- iii. Single sign-on lets one identity access multiple applications, and its security depends on the strength of the initial authentication. &nbsp; <span class="blank"></span>
- iv. Windows Hello for Business, the Microsoft Authenticator app, and FIDO2 security keys are passwordless options. &nbsp; <span class="blank"></span>

**30.** (For each statement, answer yes or no.) ### Domain 3 — Describe Azure management and governance (Q31–Q45)

- i. B2B collaboration represents external users in your directory, typically as guests. &nbsp; <span class="blank"></span>
- ii. Conditional Access can require multifactor authentication only for sign-ins from unexpected locations, while allowing known locations without a second factor. &nbsp; <span class="blank"></span>
- iii. Azure RBAC permissions assigned at a management group are inherited by subscriptions, resource groups, and resources beneath it. &nbsp; <span class="blank"></span>
- iv. Zero Trust assumes the internal network is inherently trustworthy. &nbsp; <span class="blank"></span>
- v. In defense in depth, the data layer is at the center and every other layer exists to protect it. &nbsp; <span class="blank"></span>
- vi. Microsoft Defender for Cloud calculates a secure score and can extend protection to AWS and GCP resources. &nbsp; <span class="blank"></span>

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

- i. Notify an on-call group when a metric threshold is breached &nbsp; <span class="blank"></span>
- ii. Query collected log data to investigate a pattern of errors &nbsp; <span class="blank"></span>
- iii. Monitor a web application's response times, failure rates, and dependency calls, with availability tests &nbsp; <span class="blank"></span>

**45.** A team is told their Azure bill is too high. They want both a report of where the money actually went last month and a list of Azure-generated recommendations for reducing spend. Which two tools should they use, in order?

- A. The pricing calculator, then Azure Monitor
- B. Microsoft Cost Management cost analysis, then Azure Advisor
- C. Azure Advisor, then resource locks
- D. Azure Service Health, then Microsoft Purview

<!-- pagebreak -->

## Answer sheet

| # | Your answer | # | Your answer |
| --- | --- | --- | --- |
| 1 |  | 24 |  |
| 2 |  | 25 |  |
| 3 |  | 26 |  |
| 4 |  | 27 |  |
| 5 |  | 28 |  |
| 6 |  | 29 |  |
| 7 |  | 30 |  |
| 8 |  | 31 |  |
| 9 |  | 32 |  |
| 10 |  | 33 |  |
| 11 |  | 34 |  |
| 12 |  | 35 |  |
| 13 |  | 36 |  |
| 14 |  | 37 |  |
| 15 |  | 38 |  |
| 16 |  | 39 |  |
| 17 |  | 40 |  |
| 18 |  | 41 |  |
| 19 |  | 42 |  |
| 20 |  | 43 |  |
| 21 |  | 44 |  |
| 22 |  | 45 |  |
| 23 |  |  |  |

**Score:** ____ / 45

**Objectives to review:** <span class="blank blank-wide"></span>
