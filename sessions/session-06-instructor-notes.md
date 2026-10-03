# Session 6 instructor notes — Azure Storage

**Objectives:** 2.3.1, 2.3.2, 2.3.3, 2.3.4, 2.3.5, 2.3.6
**Also practiced:** 3.1.2 (pricing calculator)
**Slides:** [session-06-slides.md](session-06-slides.md)
**Lab:** [../labs/session-06-lab.md](../labs/session-06-lab.md)
**Quiz:** [../quizzes/session-06-quiz.md](../quizzes/session-06-quiz.md)
**Warm-up:** Session 6 set, weighted to reliability and availability zones, because redundancy sits on those
**Domain minutes:** Domain 1 — 5, Domain 2 — 95, Domain 3 — 20

## Run of show

| Min | Block | Leave it when |
| --- | --- | --- |
| 0–10 | Warm-up | Zones vs region pairs is solid enough to hang LRS/ZRS/GRS on |
| 10–35 | Services and the account | Six jobs are distinct. Blob, Files, and Disk are not synonyms |
| 35–60 | Redundancy and tiers | They can pick ZRS vs GRS from "zone failure" vs "region failure," and hot vs archive from "read it now" vs "keep it cheap" |
| 60–75 | Move and migrate | AzCopy vs Storage Explorer vs File Sync, and Migrate vs Data Box |
| 75–105 | Lab | Calculator comparison done. Tool drill done |
| 105–120 | Quiz | Reviewed |

## Before you walk in

- Pricing calculator open, one blob estimate already built, so you are not learning the UI live.
- Re-read [storage account overview](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview) and [access tiers](https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview). Account kinds and the cool/cold/archive minimum retention days change. Gap G5 says to treat the account-type list as **NEEDS VERIFICATION** at delivery. Teach the jobs and the tradeoffs even if a SKU name has moved.
- Do not quote a price. The calculator output is the price.

## Teach A

One canonical use case each, then stop:

- Blob — video file, backup, static site.
- Files — the team share.
- Queue — a list of work messages.
- Table — simple NoSQL entities.
- Disk — the VHD for a VM.
- Account — the settings wrapper: redundancy, and which services you turned on.

If they remember nothing else: a share you mount is Files; an object you address by URL is Blob; a disk on a VM is Disk.

## Teach B

Tie redundancy to Session 3 in one breath. LRS is one datacenter location. ZRS is zones in the region, so it wants a region that has zones. GRS adds the paired region on top of LRS. GZRS adds the paired region on top of ZRS. Read-access means applications can read the secondary, not only wait for a failover.

Tiers are a cost knob on blobs, not a redundancy knob. Hot, cool, cold, archive. Archive is offline until rehydration. Cooler tiers have minimum keep periods and higher read costs. Say "confirm the day counts on the docs page" and point at it, rather than freezing a number into a story that will rot. The quiz should be answerable from the direction of the tradeoff.

## Teach C

Moving files is not migrating a datacenter.

- AzCopy — scripted, large, blobs and files.
- Storage Explorer — a person clicking.
- File Sync — an on-premises file server staying aligned with Azure Files. Ongoing.

- Azure Migrate — assess and move workloads (VMs, databases, apps).
- Data Box — ship the bytes on a device when the network is the wrong tool.

## Lab

The guided project (static website or secure file share) is the right homework if class time is the calculator plus the drill. Both projects are linked in the lab. In a 30-minute block, the calculator is the part that serves 3.1.2 and does not depend on a subscription. Prefer that if accounts are shaky.

## If you are short on time

Cut the live project, not the redundancy table, not the tier contrast, not the six-scenario tool drill.

## Sources

[Storage module](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/) · [Storage introduction](https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction) · [Access tiers](https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview) · [Redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy) · [AzCopy](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10) · [File Sync](https://learn.microsoft.com/en-us/azure/storage/file-sync/file-sync-introduction) · [Azure Migrate](https://learn.microsoft.com/en-us/azure/migrate/migrate-services-overview) · [Data Box](https://learn.microsoft.com/en-us/azure/databox/data-box-overview)
