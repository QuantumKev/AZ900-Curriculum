# Domain 2 Checkpoint — Describe Azure Architecture and Services

**Name:** <span class="blank"></span>  **Session:** <span class="blank"></span>

**Time:** 15 minutes · **Items:** 12 · **Target:** 75%

Answer every question. For *select all that apply*, mark every correct option. For
matching questions, write the matching term next to each numeral. For yes/no sets,
write yes or no next to each numeral. Your instructor reviews every answer in class
immediately afterward.

---

**1.** (Match each description to the correct term: datacenter, region, availability zone, region pair, sovereign region.)

- i. Physically separate datacenters within one region, each with independent power, cooling, and networking &nbsp; <span class="blank"></span>
- ii. A geographical area containing one or more nearby networked datacenters &nbsp; <span class="blank"></span>
- iii. A physical facility of racked servers that customers do not deploy to directly &nbsp; <span class="blank"></span>
- iv. Two regions in the same geography, at least 300 miles apart, used for replication and staged updates &nbsp; <span class="blank"></span>
- v. An isolated instance of Azure for legal or compliance purposes &nbsp; <span class="blank"></span>

**2.** (For each statement, answer yes or no.)

- i. A resource can belong to only one resource group at a time. &nbsp; <span class="blank"></span>
- ii. A subscription is both a billing boundary and an access control boundary. &nbsp; <span class="blank"></span>
- iii. Management groups sit above subscriptions, and subscriptions inherit the governance conditions applied to them. &nbsp; <span class="blank"></span>
- iv. Resource groups can be nested inside other resource groups. &nbsp; <span class="blank"></span>

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

- i. Encrypted connection from a single laptop into an Azure virtual network &nbsp; <span class="blank"></span>
- ii. Private, dedicated connectivity from a datacenter to Azure that does not use the public internet &nbsp; <span class="blank"></span>
- iii. Direct private connectivity between two Azure virtual networks over the Microsoft backbone &nbsp; <span class="blank"></span>
- iv. Encrypted connection from an on-premises network's gateway to an Azure virtual network over the internet &nbsp; <span class="blank"></span>
- v. Hosting DNS domains and resolving names for Azure and external resources &nbsp; <span class="blank"></span>

**8.** A database must be reachable from resources inside a virtual network using a private IP address from that network's address space, and not from the internet. What should be configured?

- A. A public endpoint
- B. A private endpoint
- C. A network security group rule allowing all inbound traffic
- D. ExpressRoute Global Reach

**9.** (Match each requirement to the Azure Storage service and access tier combination that fits.)

- i. Serving website images that users request constantly &nbsp; <span class="blank"></span>
- ii. Customer invoices retained for compliance, accessed a few times a year but needed immediately when accessed &nbsp; <span class="blank"></span>
- iii. Long-term backups that are rarely accessed, retained for at least 180 days, where retrieval latency is acceptable &nbsp; <span class="blank"></span>
- iv. A managed file share that Windows and Linux clients mount concurrently &nbsp; <span class="blank"></span>

**10.** An organization needs a storage design that survives both an availability zone failure in the primary region and a regional disaster, and must be able to read the secondary copy before any failover. Which redundancy option fits, and which account type supports it?

- A. LRS on premium page blobs
- B. ZRS on premium file shares
- C. RA-GZRS on standard general-purpose v2
- D. GRS on premium block blobs

**11.** (Match each need to the right tool: AzCopy, Azure Storage Explorer, Azure File Sync, Azure Migrate, Azure Data Box.)

- i. Assess an on-premises server estate and migrate it to Azure from a single portal &nbsp; <span class="blank"></span>
- ii. Ship 60 TB into Azure when the network connection is too slow &nbsp; <span class="blank"></span>
- iii. Command-line copying and one-direction synchronization of blobs and files &nbsp; <span class="blank"></span>
- iv. A cross-platform graphical app for managing blobs and files &nbsp; <span class="blank"></span>
- v. Keep a Windows file server bidirectionally synced with Azure Files, caching hot files locally &nbsp; <span class="blank"></span>

**12.** (For each statement, answer yes or no.)

- i. Microsoft Entra Domain Services provides a managed domain with domain join, group policy, LDAP, and Kerberos/NTLM without you deploying domain controllers. &nbsp; <span class="blank"></span>
- ii. Windows Hello for Business, the Microsoft Authenticator app, and FIDO2 security keys are the three passwordless options in Microsoft Entra ID. &nbsp; <span class="blank"></span>
- iii. Conditional Access collects signals, makes a decision, then enforces it by allowing, blocking, or challenging for multifactor authentication. &nbsp; <span class="blank"></span>
- iv. Azure RBAC uses a deny model, so the most restrictive role assignment always wins. &nbsp; <span class="blank"></span>
- v. The three Zero Trust principles are verify explicitly, use least privilege access, and assume breach. &nbsp; <span class="blank"></span>
- vi. In defense in depth, the perimeter layer uses DDoS protection to filter large-scale attacks. &nbsp; <span class="blank"></span>
- vii. Microsoft Defender for Cloud provides a secure score, prioritized recommendations, and security alerts across Azure, hybrid, and other clouds. &nbsp; <span class="blank"></span>
- viii. B2B collaboration users are typically represented in your directory as guests. &nbsp; <span class="blank"></span>

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
