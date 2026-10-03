# Session 6 slides — Azure Storage

Each `##` heading is one slide. Notes: [session-06-instructor-notes.md](session-06-instructor-notes.md).

## 1. Azure storage

Session 6. Which storage service, which tier, how many copies, and how data gets there.

## 2. Six services, six jobs

| Service | Job |
| --- | --- |
| Blob Storage | Files and objects: video, images, backups, static websites |
| Azure Files | A file share, SMB or NFS, like a team drive |
| Queue Storage | Messages waiting for a worker |
| Table Storage | Structured, non-relational rows. NoSQL |
| Disk Storage | Disks attached to virtual machines |
| Storage account | The container that holds these services and their settings |

Blob is not a file share. A file share is not a VM disk. A queue is not a table.

## 3. Storage accounts

You create a storage account before the services inside it.

Performance and account kind change over time. Confirm the current list on the storage account overview before you memorize a table. What stays true for the exam: the account is where you pick redundancy, and the services above live under it.

## 4. Redundancy

Copies, and where they sit.

| Option | Copies live |
| --- | --- |
| LRS — locally redundant | Three copies in one datacenter location in the primary region |
| ZRS — zone-redundant | Three copies across availability zones in the primary region |
| GRS — geo-redundant | LRS in the primary region, plus copies in the paired region |
| GZRS — geo-zone-redundant | ZRS in the primary region, plus copies in the paired region |

Read-access variants (RA-GRS, RA-GZRS) let you read the copy in the paired region, not only fail over to it.

LRS does not survive a datacenter loss. ZRS is about zones. GRS and GZRS are about the region pair from Session 3.

## 5. Access tiers

For blob data, tiers trade access frequency against cost.

- **Hot** — accessed often. Higher storage price, lower access cost.
- **Cool** — accessed less often. Lower storage price, higher access cost, a minimum retention period.
- **Cold** — even less often. Still online. Longer minimum retention.
- **Archive** — rarely accessed. Lowest storage price. Not readable until it is rehydrated. Longest minimum retention.

Confirm the current minimum durations on the access-tiers page the week you teach. The decision the exam wants is the direction: cooler means cheaper to keep and slower or costlier to read.

## 6. Moving files

**AzCopy.** Command-line copy of blobs and files, built for large transfers.

**Azure Storage Explorer.** A graphical app for the same accounts, when a person needs to look and copy.

**Azure File Sync.** Keeps an on-premises Windows file server in sync with an Azure file share. This is a sync product, not a one-time copy tool.

## 7. Migration

**Azure Migrate.** Assess servers, databases, and apps, then migrate them. Discovery and move. Not a USB drive.

**Azure Data Box.** A physical device Microsoft ships. You load data that is too big or too slow to send over the network, and ship it back. Offline bulk transfer.

## 8. Lab and quiz

Price the same capacity two ways in the pricing calculator: hot with LRS, and cool with GRS. Explain why the numbers differ.

Match six transfer stories to AzCopy, Storage Explorer, File Sync, Azure Migrate, or Data Box.

Assignment: [Describe Azure storage services](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/).
