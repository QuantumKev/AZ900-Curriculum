# Session 3 instructor notes — Azure Architecture

**Objectives:** 2.1.1, 2.1.2, 2.1.3, 2.1.4, 2.1.5, 2.1.6, 2.1.7
**Slides:** [session-03-slides.md](session-03-slides.md)
**Lab:** [../labs/session-03-lab.md](../labs/session-03-lab.md)
**Checkpoint:** [../quizzes/checkpoint-domain-1.md](../quizzes/checkpoint-domain-1.md) — replaces the warm-up
**Quiz:** [../quizzes/session-03-quiz.md](../quizzes/session-03-quiz.md) — 12 items
**Domain minutes:** Domain 1 — 15, Domain 2 — 105

## Run of show

| Min | Block | Leave it when |
| --- | --- | --- |
| 0–15 | Domain 1 checkpoint, then a 3-minute scan of shared misses | You know the two Domain 1 ideas to reload in Sessions 4 and 5 |
| 15–40 | Physical infrastructure | They can separate datacenter, region, zone, region pair, sovereign region |
| 40–65 | Management infrastructure | They can order root → management group → subscription → resource group → resource, and say a subscription is billing plus access |
| 65–95 | Lab | Hierarchy drawn. Resource group handled, or the diagram-only path finished |
| 95–110 | Quiz | Reviewed |
| 110–120 | Wrap | Naming and "one resource group per lab" agreed. Compute previewed in one sentence |

## Before you walk in

- Checkpoint printed or open. Review key with you.
- [Azure geographies](https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/) open for the vocabulary drill.
- A rehearsed resource-group create. If you will deploy a resource, know how you delete the group. Resource groups are free. Resources inside them may not be.
- Gap G3 is the point of the drill: learners collapse datacenter, region, and zone into one word, "the datacenter."

## 0–15 Checkpoint

Quiet 12-item sweep. Review only the items at least two people missed. Write those objective IDs on the board. They drive the Session 4 and 5 warm-ups. Do not reteach Domain 1.

## 15–40 Physical (2.1.1, 2.1.2, 2.1.3)

Work the geography site, not a metaphor pile. Show one geography, name a region inside it, and say a region is a group of datacenters close enough for a latency target.

Availability zones: physically separate, independent power, cooling, and network, minimum of three in a region that offers them. Not every region has zones. Say that, or someone will think the dropdown always appears.

Region pairs: Azure chooses the pair inside a geography. Platform replication and staged maintenance use the pair. You usually do not "create a region pair." Distance: the curriculum's retrieval answer is that paired regions are at least about 300 miles apart. If a learner asks for the current statement, read it from [cross-region replication](https://learn.microsoft.com/en-us/azure/reliability/cross-region-replication-azure) rather than inventing a tighter number.

Sovereign regions: separate compliance boundary. Do not catalog every sovereign cloud name unless the module you just read lists the ones you are willing to say. The exam skill is recognizing the category.

Zonal vs zone-redundant vs non-regional. Pin one example each: a virtual machine you place in zone 1; a service that replicates across zones for you; Microsoft Entra ID as something you do not park in a region.

## 40–65 Management (2.1.4–2.1.7)

Resource, then resource group. Two rules people miss: one resource, one resource group; groups do not nest. Deleting the group deletes the resources in it. That is why labs use `az900-sNN-lab`.

Subscription: billing boundary and access-control boundary. Say both every time. A subscription is not "an account," and it is not a region.

Management groups: organize subscriptions so policy and access can sit above them. Root management group exists for the tenant. You organize underneath.

Inheritance: assign at a management group or subscription, and it flows down to resource groups and resources. We do not configure policy today. We only mark the arrow on the drawing so Sessions 7 and 9 have somewhere to land.

## 65–95 Lab

[Session 3 lab](../labs/session-03-lab.md). Drill first (G3), then the resource group, then the drawing. If accounts are not ready, the no-cost path is the drill plus the drawing. Do not spend the block on a failed storage-account create.

## 95–120 Quiz and wrap

Review, then five minutes on naming: one group per session, tags `course` and `session`, delete before you leave. Preview Session 4 in one sentence: compute is where IaaS and PaaS become buttons.

## If you are short on time

Cut the deployed resource. Keep the drill and the drawing. Keep the quiz. Sovereign regions can be one sentence if the zone distinction took longer.

## Sources

[Core architectural components](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/) · [Physical infrastructure](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/5-describe-azure-physical-infrastructure) · [Management infrastructure](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/6-describe-azure-management-infrastructure) · [Geographies](https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/) · [Management groups](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview)
