# Session 6 lab — Price two storage designs, pick a transfer tool

**Time:** 30 minutes
**Objectives practiced:** 2.3.1–2.3.6, 3.1.2
**You need:** a browser. The pricing calculator does not require a sign-in.

---

## Part A — Same data, two designs (15 minutes)

Open the [pricing calculator](https://azure.microsoft.com/en-us/pricing/calculator/).

1. Add **Storage Accounts**, blob storage. Region: the one the instructor names. Capacity: 10 TB. Redundancy: **LRS**. Access tier: **Hot**. Write down the monthly estimate.
2. Duplicate the estimate or edit a second one. Same region, same 10 TB. Redundancy: **GRS**. Access tier: **Cool**. Write down that monthly estimate.
3. Answer in three lines:
   - Which number is higher, and which knob did it (tier, redundancy, or both)?
   - What failure does GRS survive that LRS does not?
   - Why might cool still be the wrong tier if the files are opened every day?

Do not treat the dollar amount as something to memorize. The point is that redundancy and tier are separate decisions and both move the bill.

## Part B — Which tool? (10 minutes)

Write **AzCopy**, **Storage Explorer**, **File Sync**, **Azure Migrate**, or **Data Box**.

1. A script must copy millions of blobs every night.
2. An administrator wants a desktop app to upload one folder and see the container.
3. A branch-office Windows file server should stay in sync with an Azure file share.
4. You need to discover on-premises virtual machines and plan a move into Azure.
5. 200 TB must move, and the site's internet link would take months.
6. A person who will not use a command line has to delete a handful of blobs.

## Part C — Optional project (after class, or only if Part A is done and accounts are ready)

Either:

- [Deploy a static website with Azure Blob Storage](https://learn.microsoft.com/en-us/training/modules/guided-project-deploy-static-website-blob-storage/), or
- [Share files securely](https://learn.microsoft.com/en-us/training/modules/guided-project-share-files-securely/)

Use resource group `az900-s06-lab`, tags `course=az900` and `session=s06`, and delete the group when the project is done.

### No-cost path

Parts A and B are the lab. Skip Part C, or follow the project on the instructor's screen without selecting Create.

<div class="pagebreak"></div>

## Instructor key

### Part A

GRS stores copies in the paired region, so it survives loss of the primary region. LRS does not. Cool is for infrequent access; data read constantly belongs on hot, because access charges and the retrieval pattern erase the storage discount. Dollar figures will not match between cohorts. Do not publish them as curriculum.

### Part B

1. AzCopy
2. Storage Explorer
3. File Sync
4. Azure Migrate
5. Data Box
6. Storage Explorer
