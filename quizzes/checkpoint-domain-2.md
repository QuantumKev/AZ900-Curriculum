# Domain 2 Checkpoint — Describe Azure Architecture and Services

**When:** Start of Session 8, replacing the warm-up · **Time:** 15 minutes · **Items:** 12
**Coverage:** all 27 Domain 2 objectives (2.1.1–2.4.8)
**Target:** 75%

Domain 2 is the largest domain at 35–40% of the exam and the widest in service names. This
checkpoint arrives immediately after Session 7 completes the domain. Multi-objective items
are used heavily; several items carry three or more objectives.

---

## Questions

**1.** (Match each description to the correct term: datacenter, region, availability zone, region pair, sovereign region.)

- i. Physically separate datacenters within one region, each with independent power, cooling, and networking
- ii. A geographical area containing one or more nearby networked datacenters
- iii. A physical facility of racked servers that customers do not deploy to directly
- iv. Two regions in the same geography, at least 300 miles apart, used for replication and staged updates
- v. An isolated instance of Azure for legal or compliance purposes

**2.** (For each statement, answer yes or no.)

- i. A resource can belong to only one resource group at a time.
- ii. A subscription is both a billing boundary and an access control boundary.
- iii. Management groups sit above subscriptions, and subscriptions inherit the governance conditions applied to them.
- iv. Resource groups can be nested inside other resource groups.

**3.** A team needs to run several instances of an application on one host, starting and stopping them quickly, without managing a separate operating system per instance — and separately needs to run short code triggered by queue messages. Which two compute options fit?

- A. Virtual machines for both
- B. Containers for the first, functions for the second
- C. Functions for the first, virtual machines for the second
- D. Azure Virtual Desktop for both

**4.** Which combination correctly matches the requirement to the service?

- A. Identical load-balanced VMs that scale automatically → availability set; centrally managed Windows desktops for remote workers → Azure Virtual Desktop
- B. Identical load-balanced VMs that scale automatically → virtual machine scale set; centrally managed Windows desktops for remote workers → Azure Virtual Desktop
- C. Identical load-balanced VMs that scale automatically → Azure App Service; centrally managed Windows desktops for remote workers → virtual machine scale set
- D. Both requirements → Azure Container Apps

**5.** Which items must be specified when provisioning a virtual machine? (Select all that apply.)

- A. VM size, including family, vCPU count, and RAM
- B. Storage disks
- C. Virtual network and network interface
- D. An Azure Policy initiative
- E. A Microsoft Purview data map

**6.** A development team wants managed hosting for a web app and a REST API, in the language of their choice, with automatic scaling and Git-based deployment, and no operating system to maintain. Which option fits?

- A. Azure Virtual Machines in an availability set
- B. Azure App Service
- C. Azure Data Box
- D. Azure Virtual Desktop

**7.** (Match each connectivity requirement to the right option: virtual network peering, site-to-site VPN, point-to-site VPN, Azure ExpressRoute, Azure DNS.)

- i. Encrypted connection from a single laptop into an Azure virtual network
- ii. Private, dedicated connectivity from a datacenter to Azure that does not use the public internet
- iii. Direct private connectivity between two Azure virtual networks over the Microsoft backbone
- iv. Encrypted connection from an on-premises network's gateway to an Azure virtual network over the internet
- v. Hosting DNS domains and resolving names for Azure and external resources

**8.** A database must be reachable from resources inside a virtual network using a private IP address from that network's address space, and not from the internet. What should be configured?

- A. A public endpoint
- B. A private endpoint
- C. A network security group rule allowing all inbound traffic
- D. ExpressRoute Global Reach

**9.** (Match each requirement to the Azure Storage service and access tier combination that fits.)

- i. Serving website images that users request constantly
- ii. Customer invoices retained for compliance, accessed a few times a year but needed immediately when accessed
- iii. Long-term backups that are rarely accessed, retained for at least 180 days, where retrieval latency is acceptable
- iv. A managed file share that Windows and Linux clients mount concurrently

**10.** An organization needs a storage design that survives both an availability zone failure in the primary region and a regional disaster, and must be able to read the secondary copy before any failover. Which redundancy option fits, and which account type supports it?

- A. LRS on premium page blobs
- B. ZRS on premium file shares
- C. RA-GZRS on standard general-purpose v2
- D. GRS on premium block blobs

**11.** (Match each need to the right tool: AzCopy, Azure Storage Explorer, Azure File Sync, Azure Migrate, Azure Data Box.)

- i. Assess an on-premises server estate and migrate it to Azure from a single portal
- ii. Ship 60 TB into Azure when the network connection is too slow
- iii. Command-line copying and one-direction synchronization of blobs and files
- iv. A cross-platform graphical app for managing blobs and files
- v. Keep a Windows file server bidirectionally synced with Azure Files, caching hot files locally

**12.** (For each statement, answer yes or no.)

- i. Microsoft Entra Domain Services provides a managed domain with domain join, group policy, LDAP, and Kerberos/NTLM without you deploying domain controllers.
- ii. Windows Hello for Business, the Microsoft Authenticator app, and FIDO2 security keys are the three passwordless options in Microsoft Entra ID.
- iii. Conditional Access collects signals, makes a decision, then enforces it by allowing, blocking, or challenging for multifactor authentication.
- iv. Azure RBAC uses a deny model, so the most restrictive role assignment always wins.
- v. The three Zero Trust principles are verify explicitly, use least privilege access, and assume breach.
- vi. In defense in depth, the perimeter layer uses DDoS protection to filter large-scale attacks.
- vii. Microsoft Defender for Cloud provides a secure score, prioritized recommendations, and security alerts across Azure, hybrid, and other clouds.
- viii. B2B collaboration users are typically represented in your directory as guests.

---

## Answer key

| Q | Answer | Objective | Why | Source |
| --- | --- | --- | --- | --- |
| 1 | i–availability zone, ii–region, iii–datacenter, iv–region pair, v–sovereign region | 2.1.1, 2.1.2, 2.1.3 | The five physical-infrastructure terms. Customers deploy to regions and zones; datacenters are the underlying facilities. Score per pair. | [Azure physical infrastructure](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/5-describe-azure-physical-infrastructure) |
| 2 | i–yes, ii–yes, iii–yes, iv–no | 2.1.4, 2.1.5, 2.1.6, 2.1.7 | Resources belong to exactly one resource group; subscriptions are billing and access boundaries; management groups pass governance conditions down; resource groups cannot be nested. Score per statement. | [Azure management infrastructure](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/6-describe-azure-management-infrastructure) |
| 3 | B | 2.2.1 | Containers run multiple lightweight instances on one host without a per-instance OS to manage; functions run event-triggered code, including triggers from queue messages. | [Azure containers](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/5-containers) · [Azure functions](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/6-functions) |
| 4 | B | 2.2.2 | Scale sets provide identical load-balanced VMs with automatic scaling; availability sets provide in-region resiliency but do not change instance counts. Azure Virtual Desktop delivers centrally managed desktops and apps. | [Azure virtual machines](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/2-virtual-machines) · [Azure virtual desktop](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/4-virtual-desktop) |
| 5 | A, B, C | 2.2.3 | Size, disks, and networking are the required VM choices. Policy initiatives and Purview data maps are governance features unrelated to provisioning a VM. | [Azure virtual machines](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/2-virtual-machines) |
| 6 | B | 2.2.4 | App Service is the managed application hosting option covering web apps, API apps, WebJobs, and mobile back ends, with automatic scaling, built-in load balancing, and Git-based deployment. | [Application hosting options](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/7-describe-application-hosting-options) |
| 7 | i–point-to-site VPN, ii–ExpressRoute, iii–virtual network peering, iv–site-to-site VPN, v–Azure DNS | 2.2.5 | The five named networking capabilities in the objective. Score per pair. | [Azure virtual networking](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/2-virtual-network) · [VPNs](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/3-virtual-private-networks) · [ExpressRoute](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/4-expressroute) · [Azure DNS](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/5-domain-name-system) |
| 8 | B | 2.2.6 | A private endpoint exists in the virtual network and uses a private IP from its address space. A public endpoint is internet-reachable; an allow-all NSG rule would do the opposite of what is required. | [Azure virtual networking](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/2-virtual-network) |
| 9 | i–Blob Storage, hot tier; ii–Blob Storage, cool or cold tier; iii–Blob Storage, archive tier; iv–Azure Files | 2.3.1, 2.3.2 | Hot for frequent access, cool (30+ days) or cold (90+ days) for infrequent but immediately readable, archive (180+ days) where rehydration latency is acceptable. Azure Files provides the SMB/NFS managed share. Score per pair. | [Azure storage services](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/4-describe-azure-storage-services) |
| 10 | C | 2.3.3, 2.3.4 | GZRS gives zone redundancy in the primary region plus geo-replication; the RA- variant adds read access to the secondary before failover; and standard general-purpose v2 is the account type that supports RA-GZRS. Premium account types are limited to LRS or ZRS. | [Azure storage redundancy](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/3-redundancy) · [Azure storage accounts](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/2-accounts) |
| 11 | i–Azure Migrate, ii–Azure Data Box, iii–AzCopy, iv–Azure Storage Explorer, v–Azure File Sync | 2.3.5, 2.3.6 | Migrate for assessment and migration; Data Box for offline bulk transfer up to 80 TB usable; AzCopy for command-line copy and one-direction sync; Storage Explorer for the cross-platform GUI; File Sync for bidirectional server sync with cloud tiering. Score per pair. | [Data migration options](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/6-identify-azure-data-migration-options) · [File movement options](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/7-identify-azure-file-movement-options) |
| 12 | i–yes, ii–yes, iii–yes, iv–no, v–yes, vi–yes, vii–yes, viii–yes | 2.4.1, 2.4.2, 2.4.3, 2.4.4, 2.4.5, 2.4.6, 2.4.7, 2.4.8 | Only statement iv is false: Azure RBAC uses an **allow** model, and permissions from multiple assignments combine. Score per statement. | [Directory services](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/2-directory-services) · [Authentication methods](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/3-authentication-methods) · [External identities](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/4-external-identities) · [Conditional access](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/5-conditional-access) · [RBAC](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/6-role-based-access-control) · [Zero Trust](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/7-describe-zero-trust-model) · [Defense in depth](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/8-describe-defense-depth) · [Defender for Cloud](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/9-describe-microsoft-defender-for-cloud) |

## Scoring notes

Every item is worth one point, out of 12. Items 1, 2, 7, 9, 11, and 12 are multi-part and
earn fractional credit — correct parts divided by total parts. Item 5 is multi-select and
is all-or-nothing.

| Result | Action |
| --- | --- |
| 9.0+ of 12 | Domain 2 is holding. Standard warm-up rotation continues. |
| 7.5–8.9 | Give the missed objective IDs priority in the Session 9 and Session 10 warm-ups. |
| Below 7.5 | Make one of the two Session 11 re-teach slots a Domain 2 slot, and assign the relevant module units before Session 11. |

Record misses by objective ID. Sessions 11 and 12 both allocate re-teaching time based on
this checkpoint and the Domain 1 checkpoint, and that allocation needs per-objective data.
