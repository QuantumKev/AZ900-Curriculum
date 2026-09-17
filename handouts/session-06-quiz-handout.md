# Session 6 Quiz — Azure Storage

**Name:** <span class="blank"></span>  **Session:** <span class="blank"></span>

**Time:** 15 minutes · **Items:** 12 · **Target:** 80%

Answer every question. For *select all that apply*, mark every correct option. For
matching questions, write the matching term next to each numeral. For yes/no sets,
write yes or no next to each numeral. Your instructor reviews every answer in class
immediately afterward.

---

**1.** (Match each requirement to the Azure Storage service that fits: Blob Storage, Azure Files, Queue Storage, Azure Disk Storage, Table Storage.)

- i. Store and stream large video files to browsers &nbsp; <span class="blank"></span>
- ii. Provide a managed file share that Windows, Linux, and macOS clients can mount concurrently &nbsp; <span class="blank"></span>
- iii. Hold messages so application components can process work asynchronously &nbsp; <span class="blank"></span>
- iv. Provide a block-level volume for an Azure virtual machine &nbsp; <span class="blank"></span>
- v. Store large amounts of structured, non-relational data in a NoSQL store &nbsp; <span class="blank"></span>

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

**10.** Which tool keeps an on-premises Windows file server bidirectionally synchronized with Azure Files, with frequently accessed files cached locally?

- A. AzCopy
- B. Azure File Sync
- C. Azure Migrate
- D. Azure Storage Explorer

**11.** A team needs to assess an on-premises server estate and then migrate those servers to Azure, tracking the whole effort from one place. Which service is designed for this?

- A. Azure Data Box
- B. Azure Migrate
- C. Azure Arc
- D. Azure Advisor

**12.** When creating a virtual machine, which choice most directly affects the VM's storage performance?

- A. The resource group name
- B. The disk type and configuration selected for the VM
- C. The tags applied to the VM
- D. The subscription's billing cycle

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
