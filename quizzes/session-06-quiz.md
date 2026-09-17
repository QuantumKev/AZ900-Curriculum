# Session 6 Quiz — Azure Storage

**Time:** 15 minutes · **Items:** 12 · **Composition:** 9 new, 3 carry-forward (S2–S5)
**Objectives:** 2.3.1, 2.3.2, 2.3.3, 2.3.4, 2.3.5, 2.3.6
**Carry-forward objectives:** 1.2.2, 2.1.2, 2.2.3
**Target:** 80%

---

## Questions

**1.** (Match each requirement to the Azure Storage service that fits: Blob Storage, Azure Files, Queue Storage, Azure Disk Storage, Table Storage.)

- i. Store and stream large video files to browsers
- ii. Provide a managed file share that Windows, Linux, and macOS clients can mount concurrently
- iii. Hold messages so application components can process work asynchronously
- iv. Provide a block-level volume for an Azure virtual machine
- v. Store large amounts of structured, non-relational data in a NoSQL store

**2.** Which statement about Azure Blob Storage is correct?

- A. It is designed for structured relational data with enforced schemas
- B. It is an object store for unstructured text and binary data, accessible over HTTP or HTTPS
- C. It can only be accessed from inside the virtual network where it is created
- D. It requires an Azure virtual machine to be running to serve content

**3.** Which access tier is appropriate for data that is rarely accessed, stored for at least 180 days, and can tolerate retrieval latency?

- A. Hot
- B. Cool
- C. Cold
- D. Archive

**4.** Which statements about blob access tiers are correct? (Select all that apply.)

- A. The cool tier is intended for data stored for at least 30 days
- B. The cold tier is intended for data stored for at least 90 days
- C. The archive tier can be set at the storage account level
- D. Hot, cool, and cold tiers can be set at the account level
- E. Cool and cold tiers have lower storage costs but higher access costs

**5.** Which redundancy option replicates data synchronously across three availability zones in the primary region?

- A. Locally redundant storage (LRS)
- B. Zone-redundant storage (ZRS)
- C. Geo-redundant storage (GRS)
- D. Read-access geo-redundant storage (RA-GRS)

**6.** An organization needs the highest resilience for a critical dataset: protection against both a zone failure in the primary region and a regional disaster. Which redundancy option should they choose?

- A. LRS
- B. ZRS
- C. GRS
- D. GZRS

**7.** With GRS configured and no failover performed, can an application read the data in the secondary region?

- A. Yes, secondary-region data is always readable
- B. No, unless read access to the secondary region is enabled with the read-access variant
- C. Yes, but only through AzCopy
- D. No, secondary-region data is never readable under any configuration

**8.** Which statements about storage accounts are correct? (Select all that apply.)

- A. Standard general-purpose v2 is the recommended account type for most Azure Storage scenarios
- B. Storage account names must be globally unique in Azure
- C. Storage account names may be 3 to 24 characters using numbers and lowercase letters only
- D. Premium page blobs support all redundancy options
- E. NFS file share support requires the premium file shares account type

**9.** A company must move 60 TB of archive data into Azure, and its internet connection is too slow to transfer that volume in a reasonable time. Which option fits best?

- A. AzCopy
- B. Azure File Sync
- C. Azure Data Box
- D. Azure Storage Explorer

**10.** *(Carry-forward)* Which tool keeps an on-premises Windows file server bidirectionally synchronized with Azure Files, with frequently accessed files cached locally?

- A. AzCopy
- B. Azure File Sync
- C. Azure Migrate
- D. Azure Storage Explorer

**11.** *(Carry-forward)* A team needs to assess an on-premises server estate and then migrate those servers to Azure, tracking the whole effort from one place. Which service is designed for this?

- A. Azure Data Box
- B. Azure Migrate
- C. Azure Arc
- D. Azure Advisor

**12.** *(Carry-forward)* When creating a virtual machine, which choice most directly affects the VM's storage performance?

- A. The resource group name
- B. The disk type and configuration selected for the VM
- C. The tags applied to the VM
- D. The subscription's billing cycle

---

## Answer key

| Q | Answer | Objective | Why | Source |
| --- | --- | --- | --- | --- |
| 1 | i–Blob Storage, ii–Azure Files, iii–Queue Storage, iv–Azure Disk Storage, v–Table Storage | 2.3.1 | These are the five core Azure Storage data services and their canonical use cases. Score one point per pair, then round. | [Azure storage services](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/4-describe-azure-storage-services) |
| 2 | B | 2.3.1 | Blob Storage is an unstructured object store reachable over HTTP or HTTPS from anywhere, via URLs, REST API, SDKs, CLI, PowerShell, or Storage Explorer. No VM is required. | [Azure storage services](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/4-describe-azure-storage-services) |
| 3 | D | 2.3.2 | Archive is for rarely accessed data stored at least 180 days with flexible latency requirements, at the lowest storage cost and highest rehydration latency. | [Azure storage services](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/4-describe-azure-storage-services) · [Access tiers](https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview) |
| 4 | A, B, D, E | 2.3.2 | Cool is for at least 30 days, cold for at least 90 days, hot/cool/cold can be set at account level, and cool and cold trade lower storage cost for higher access cost. C is false — archive is not available at the account level, only per blob. | [Azure storage services](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/4-describe-azure-storage-services) |
| 5 | B | 2.3.3 | ZRS replicates synchronously across three availability zones in the primary region and keeps data readable and writable if one zone is unavailable. LRS keeps all three copies in one datacenter. | [Azure storage redundancy](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/3-redundancy) |
| 6 | D | 2.3.3 | GZRS combines zone redundancy in the primary region with geo-replication to the paired secondary region, and is Microsoft's recommendation for maximum availability and disaster-recovery resilience. GRS uses LRS in both regions, so it does not protect against a zone failure the same way. | [Azure storage redundancy](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/3-redundancy) |
| 7 | B | 2.3.3 | By default secondary-region data is not readable until failover occurs; reading before failover requires the read-access variants, RA-GRS or RA-GZRS. | [Azure storage redundancy](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/3-redundancy) |
| 8 | A, B, C, E | 2.3.4 | Standard general-purpose v2 is recommended for most scenarios; names are globally unique, 3–24 characters, lowercase letters and numbers only; NFS file shares need premium file shares. D is false — premium page blobs support LRS only. | [Azure storage accounts](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/2-accounts) · [Storage account overview](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview) |
| 9 | C | 2.3.6 | Data Box is the physical, offline transfer service for very large datasets when bandwidth is the constraint; the device has a maximum usable capacity of 80 TB and ships to and from your datacenter. | [Azure data migration options](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/6-identify-azure-data-migration-options) |
| 10 | B | 2.3.5 (carry-forward) | Azure File Sync keeps a Windows server bidirectionally synced with Azure Files and supports cloud tiering so hot files stay local. AzCopy synchronizes in one direction only. | [Azure file movement options](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/7-identify-azure-file-movement-options) |
| 11 | B | 2.3.6 (carry-forward) | Azure Migrate is the hub for discovery, assessment, and migration of on-premises infrastructure, with server, database, and web app migration tooling in one portal. | [Azure data migration options](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/6-identify-azure-data-migration-options) |
| 12 | B | 2.2.3 (carry-forward) | Disk type and configuration drive storage capacity, IOPS, and throughput for a VM. Names, tags, and billing cycles have no performance effect. | [Azure virtual machines](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/2-virtual-machines) |

**Objectives 1.2.2 and 2.1.2 carry-forward:** covered by items 5–7, which require learners
to connect redundancy choices back to availability zones (2.1.2) and to reliability as a
cloud benefit (1.2.2). Call this link out explicitly during the review.
