# Cumulative Warm-Ups (Sessions 2–12)

Ten minutes at the start of every session after the first. **Free recall, not multiple
choice** — learners produce the answer, then check it. Ungraded.

Run it verbally, as a poll, or on paper. Six prompts, roughly 60–90 seconds each including
the answer. If two or more learners miss the same prompt, re-teach it on the spot rather
than moving on; that decision is the whole purpose of the block.

Sessions 3 and 8 replace the warm-up with a domain checkpoint
([`checkpoint-domain-1.md`](./checkpoint-domain-1.md),
[`checkpoint-domain-2.md`](./checkpoint-domain-2.md)). The Session 3 and Session 8 sets
below are the short warm-ups to use if a cohort needs the checkpoint moved, and are worth
keeping as spare retrieval material either way.

Each prompt shows the objective ID and the expected answer. Accept any phrasing that
contains the substance; these are recall checks, not wording checks.

---

## Session 2 warm-up — recalls S1

1. **(1.1.1)** In one sentence, what is cloud computing?
   *Expected:* using computing services — compute, storage, networking, databases — delivered over the internet from someone else's datacenter, rented rather than owned.
2. **(1.1.2)** Name three things that remain your responsibility no matter which cloud service type you use.
   *Expected:* your data and information; the devices allowed to connect; the accounts and identities in your environment.
3. **(1.1.2)** Name three things the cloud provider is always responsible for.
   *Expected:* the physical datacenter, the physical network, the physical hosts.
4. **(1.1.3)** What single characteristic most clearly separates a public cloud from a private cloud?
   *Expected:* a public cloud is available to anyone who wants to buy the services; a private cloud is used by a single organization.
5. **(1.1.5)** What does CapEx mean, what does OpEx mean, and which one describes cloud consumption?
   *Expected:* CapEx is up-front spending on physical infrastructure; OpEx is ongoing spending on services; cloud consumption is an operating expense.
6. **(1.1.4)** Give one situation where a hybrid cloud is the better answer than a public cloud.
   *Expected:* any reasonable answer — keeping regulated or sensitive workloads on private infrastructure while bursting to public cloud for temporary demand, or a phased migration.

## Session 3 warm-up — recalls S1–S2 (spare; S3 normally runs the Domain 1 checkpoint)

1. **(1.3.4)** A team wants to run a legacy application that needs a specific OS build and custom drivers. Which cloud service type fits, and why?
   *Expected:* IaaS — they need control of the operating system and installed software.
2. **(1.2.1)** What is the difference between vertical and horizontal scaling?
   *Expected:* vertical changes the capability of a resource (more CPU or RAM); horizontal changes the number of resources (adding or removing instances).
3. **(1.1.6)** Name two Azure pricing commitments that cost less than pay-as-you-go, and say what you give up for each.
   *Expected:* reservations (commit to specific resources for one or three years) and Azure savings plan for compute (commit to an hourly spend for one or three years); you give up flexibility in exchange for a lower rate. Spot pricing is also acceptable, where you give up guaranteed capacity.
4. **(1.1.7)** What makes a service serverless?
   *Expected:* you don't provision or maintain servers; an event triggers the code, and resources are allocated and deallocated around the run, so you pay only while it executes.
5. **(1.2.4)** What is the difference between management *of* the cloud and management *in* the cloud?
   *Expected:* management of the cloud is managing your cloud resources (autoscaling, template deployment, health monitoring, alerts); management in the cloud is how you interact with the environment (portal, CLI, PowerShell, APIs).
6. **(1.1.2)** For a SaaS email service, who patches the application, and who manages the user accounts?
   *Expected:* the provider patches the application; you manage the accounts and identities.

## Session 4 warm-up — recalls S1–S3

1. **(2.1.4)** Can a resource belong to two resource groups? Can resource groups be nested?
   *Expected:* no to both. Every resource belongs to exactly one resource group, and resource groups can't be nested.
2. **(2.1.5)** Name the two boundaries a subscription represents.
   *Expected:* a billing boundary and an access control boundary.
3. **(2.1.2)** How many availability zones does an availability-zone-enabled Azure region have at minimum?
   *Expected:* three separate availability zones.
4. **(1.1.2)** On an IaaS virtual machine, who is responsible for patching the operating system?
   *Expected:* you are. The provider covers physical infrastructure and connectivity.
5. **(1.3.1 / 1.3.2)** Give one scenario each where IaaS is the better choice and where PaaS is the better choice.
   *Expected:* IaaS for lift-and-shift migration or when you need full OS control; PaaS for a development framework or analytics work where you don't want to manage the OS or middleware.
6. **(2.1.7)** Put these in order from broadest to narrowest: resource, subscription, management group, resource group.
   *Expected:* management group, subscription, resource group, resource.

## Session 5 warm-up — recalls S1–S4

1. **(2.2.1)** Compare a virtual machine, a container, and a function in one sentence each.
   *Expected:* a VM gives you a full OS you manage; a container is a lightweight package that shares the host OS and starts and stops quickly; a function runs your code in response to an event with no infrastructure to manage.
2. **(2.2.2)** What is the difference between a virtual machine scale set and an availability set?
   *Expected:* a scale set creates and manages a group of identical load-balanced VMs and can scale automatically; an availability set spreads VMs across update and fault domains so one maintenance event or hardware failure doesn't take them all down.
3. **(2.2.3)** Name four things you choose when you create a virtual machine.
   *Expected:* any four of size (family, vCPU, RAM), disks, virtual network and subnet, public IP address, network interface, image and OS.
4. **(1.1.3 / 1.1.4)** Which cloud model connects public and private cloud together, and name one reason to choose it.
   *Expected:* hybrid; to keep certain workloads or data on private infrastructure while using public cloud for the rest, or to handle temporary demand spikes.
5. **(2.1.1)** What is a region pair, and roughly how far apart are paired regions?
   *Expected:* two regions in the same geography that Azure pairs for replication and staged updates, at least 300 miles apart.
6. **(2.2.4)** Name the Azure service that hosts web apps, APIs, and mobile back ends without you managing the OS.
   *Expected:* Azure App Service.

## Session 6 warm-up — recalls S2–S5

1. **(2.2.5)** Which connectivity option is private and does not travel over the public internet?
   *Expected:* Azure ExpressRoute.
2. **(2.2.5)** What is the difference between a site-to-site and a point-to-site VPN connection?
   *Expected:* site-to-site connects an on-premises network or gateway to an Azure virtual network; point-to-site connects a single device or client computer into the virtual network.
3. **(2.2.6)** What is the difference between a public endpoint and a private endpoint?
   *Expected:* a public endpoint has a public IP address and is reachable from the internet; a private endpoint lives inside a virtual network and uses a private IP from that network's address space.
4. **(2.1.2)** How do availability zones differ from region pairs in what they protect against?
   *Expected:* availability zones protect against a datacenter-level failure within one region; region pairs protect against a failure affecting a whole region.
5. **(1.2.2)** Give one example of performance predictability and one example of cost predictability.
   *Expected:* performance — autoscaling or load balancing keeps response times steady under changing demand; cost — tracking usage and using the pricing calculator to forecast spend.
6. **(2.2.5)** Name what lets two virtual networks communicate directly over the Microsoft backbone rather than the public internet.
   *Expected:* virtual network peering.

## Session 7 warm-up — recalls S1–S6

1. **(1.1.2)** For a cloud SQL database offered as a managed service, who maintains the database engine and who is responsible for the data in it?
   *Expected:* the provider maintains the database service; you are responsible for the data you put in it.
2. **(1.2.3)** Name two ways the cloud helps with governance and compliance.
   *Expected:* templates that make deployments meet your standards, cloud-based auditing that flags out-of-compliance resources, and automatic patching depending on the service model.
3. **(2.3.1)** Match the workload to the storage service: a video file, a shared drive for a team, messages waiting to be processed, a disk for a VM.
   *Expected:* Blob Storage, Azure Files, Queue Storage, Azure Disk Storage.
4. **(1.3.3)** Give two examples of SaaS.
   *Expected:* any two of email, messaging, productivity applications, finance or expense tracking.
5. **(2.2.6)** A database should be reachable from inside a virtual network but not from the internet. What do you use?
   *Expected:* a private endpoint.
6. **(2.3.1)** Which storage service holds structured, non-relational data as a NoSQL store?
   *Expected:* Azure Table Storage.

## Session 8 warm-up — recalls S2–S7 (spare; S8 normally runs the Domain 2 checkpoint)

1. **(2.4.5)** If you assign the Reader role at subscription scope, what can that group see?
   *Expected:* every resource group and resource in that subscription — permissions inherit down the hierarchy.
2. **(2.4.2)** Name the three categories of authentication factors and give an example of each.
   *Expected:* something you know (password, challenge question), something you have (a code sent to a phone), something you are (fingerprint or face scan).
3. **(2.4.6)** State the three Zero Trust guiding principles.
   *Expected:* verify explicitly, use least privilege access, assume breach.
4. **(2.3.3)** Which redundancy option copies data across three availability zones in the primary region?
   *Expected:* zone-redundant storage (ZRS).
5. **(2.4.1)** What is the difference between Microsoft Entra ID and Microsoft Entra Domain Services?
   *Expected:* Entra ID is the cloud identity and access management service; Entra Domain Services provides a managed domain with domain join, group policy, LDAP, and Kerberos/NTLM for applications that need traditional domain features.
6. **(2.3.2)** Which blob access tier suits data that is rarely accessed and kept for at least 180 days?
   *Expected:* the archive tier.

## Session 9 warm-up — recalls S3–S8

1. **(2.1.7)** Where do you assign a policy so that every subscription under it inherits the rule?
   *Expected:* at the management group.
2. **(3.1.4)** Do resources inherit tags from their resource group or subscription?
   *Expected:* no. Tags are not inherited; apply them where you need them, or enforce them with Azure Policy.
3. **(3.1.1)** Name four factors that affect what an Azure resource costs.
   *Expected:* any four of resource type and settings, consumption, maintenance of leftover resources, geography and region, network traffic and billing zones, subscription type, Azure Marketplace third-party charges.
4. **(2.4.5)** What does it mean that Azure RBAC uses an allow model?
   *Expected:* role assignments grant permissions and combine; if one assignment grants read and another grants write on the same scope, you have both.
5. **(3.1.3)** Name the tool you use to see where your Azure spend is going, and the feature you use to get notified at a spending threshold.
   *Expected:* Microsoft Cost Management with cost analysis; budgets with budget alerts.
6. **(2.4.8)** What does Microsoft Defender for Cloud give you that plain Azure Policy does not?
   *Expected:* security posture management with a secure score, prioritized security recommendations, security alerts, and threat protection across Azure, hybrid, and other clouds.

## Session 10 warm-up — recalls S4–S9

1. **(3.2.2 / 3.2.3)** One team keeps accidentally deleting a production resource group; another keeps deploying VMs in unapproved regions. Which tool solves which problem?
   *Expected:* a resource lock for the accidental deletion; Azure Policy for the region restriction.
2. **(3.2.2)** What is an Azure Policy initiative?
   *Expected:* a group of related policy definitions assigned and tracked together toward one compliance goal.
3. **(2.2.4)** Name three ways to host an application in Azure.
   *Expected:* Azure App Service web apps, containers, and virtual machines.
4. **(3.2.3)** You are an Owner and a ReadOnly lock is on the resource. Can you change it?
   *Expected:* not until you remove the lock. Locks apply regardless of RBAC role.
5. **(1.2.4)** Name three ways to interact with an Azure environment.
   *Expected:* any three of the Azure portal, Azure CLI, Azure PowerShell, Cloud Shell, REST APIs, SDKs.
6. **(3.1.4)** Give three tag names worth standardizing across an organization and say what question each answers.
   *Expected:* any three such as Environment (which lifecycle stage), Owner (who to contact), CostCenter (who pays), Workload or AppName (what it belongs to), Impact (how critical it is).

## Session 11 warm-up — recalls S4–S10

1. **(3.3.5)** What is Azure Resource Manager, and what goes through it?
   *Expected:* the deployment and management layer for Azure; every request from the portal, CLI, PowerShell, SDKs, and APIs goes through it, and it authenticates and authorizes before passing the request to the service.
2. **(3.3.4)** What does infrastructure as code mean, and name one benefit.
   *Expected:* defining and managing infrastructure through code or templates instead of manual configuration; benefits include repeatable deployments, review and version control, and consistent environments.
3. **(3.3.3)** What problem does Azure Arc solve?
   *Expected:* it projects non-Azure resources — servers, Kubernetes clusters, SQL Server, data services — into Azure Resource Manager so you can govern and manage hybrid and multicloud estates consistently from Azure.
4. **(3.3.2)** Azure CLI and Azure PowerShell: what is the real difference?
   *Expected:* functionally equivalent capability, different command syntax; pick the one you know. Both are available locally and in Cloud Shell.
5. **(2.4.4)** What three steps does Conditional Access take during sign-in?
   *Expected:* it collects signals, makes a decision, then enforces that decision by allowing, blocking, or challenging for MFA.
6. **(2.3.5 / 2.3.6)** You need to move 60 TB into Azure on a slow connection, and separately keep one Windows file server synced with Azure Files. Which tool for each?
   *Expected:* Azure Data Box for the bulk offline transfer; Azure File Sync for the ongoing server sync.

## Session 12 warm-up — recalls the whole course

1. **(3.4.1 / 3.4.2 / 3.4.3)** Advisor, Service Health, and Azure Monitor: what question does each answer?
   *Expected:* Advisor — what should I improve in my environment; Service Health — is Azure itself having a problem that affects me; Azure Monitor — what are my resources and applications actually doing.
2. **(3.4.3)** Log Analytics, Azure Monitor alerts, Application Insights: which one do you use to query collected data, which notifies you, and which watches an application?
   *Expected:* Log Analytics queries, alerts notify through action groups, Application Insights monitors application performance and usage.
3. **(1.1.2)** State the shared responsibility model in one sentence, then say how it shifts from IaaS to SaaS.
   *Expected:* responsibility for the stack is divided between provider and customer; IaaS puts the most on the customer, SaaS the most on the provider, PaaS sits in between.
4. **(2.1.1 / 2.1.2)** Datacenter, region, availability zone, region pair: define each in a few words.
   *Expected:* datacenter — a physical facility of servers; region — a geographical area containing one or more nearby networked datacenters; availability zone — physically separate datacenters within a region with independent power, cooling, and networking; region pair — two regions in the same geography paired for replication and staged updates.
5. **(2.4.5 / 3.2.2 / 3.2.3)** RBAC, Azure Policy, and resource locks: what does each control?
   *Expected:* RBAC controls who can do what and at which scope; Policy controls what resource configurations are allowed or audited; locks prevent deletion or modification regardless of role.
6. **(Exam logistics)** How long is the exam, what score do you need, and can you look things up on Microsoft Learn during it?
   *Expected:* 45 minutes of exam time within a 65-minute seat time; 700 or greater to pass; no — Microsoft Learn access is a role-based-exam feature and is not available on Fundamentals exams.
