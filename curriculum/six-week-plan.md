# Six-Week Plan — 12 Sessions, 24 Instructional Hours

Six weeks, two sessions per week, 120 minutes per session. No calendar dates are used
anywhere in this plan: cohorts run on relative session numbers, so the same plan works
for any start point or cadence.

Objective IDs map to [`exam-objective-map.md`](./exam-objective-map.md). Every session's
minute budget is attributed to an exam domain so the course as a whole matches the
published exam weights.

## Standard 120-minute session shape

| Block | Minutes | Purpose |
| --- | --- | --- |
| Cumulative warm-up | 10 | Spaced retrieval on prior sessions. Low stakes, verbal or poll. Not graded. |
| Teach block A | 25 | New objective content, instructor-led with one worked example. |
| Teach block B | 25 | New objective content, second cluster. |
| Practice | 30 | Portal, Cloud Shell, guided project, calculator, or structured sorting activity. |
| Session quiz | 15 | Formative, this session's objectives only. Answers reviewed immediately. |
| Wrap and assignment | 15 | Misconception cleanup, objective checklist, next-session prep. |

Sessions 11 and 12 replace part of this shape with review and full-length practice; their
tables note the difference.

Instructors may shift up to 10 minutes between teach and practice, but the warm-up and
the session quiz are fixed. Those two blocks are what make the cumulative review and
coverage guarantees in the objective map true.

The warm-up samples from every earlier session listed for it in the [cumulative review
schedule](#cumulative-review-schedule) at the end of this file. Each session's warm-up
note names the priority items for that sitting, not the full set.

## Deviation from the suggested sequence

The suggested 12-session sequence was kept almost intact, because it already tracks the
official objective groupings. Three changes are justified by the current Microsoft
objectives and content structure:

1. **Session 1 stops after the consumption-based model; Session 2 picks up pricing-model
   comparison and serverless.** "Compare cloud pricing models" and "Describe serverless"
   are both objectives under *Describe cloud computing*, but Microsoft teaches the
   substance of both outside the cloud-concepts learning path (pricing models in the cost
   module, serverless in the Azure Functions unit). Pairing pricing models with the
   consumption model recap and serverless with PaaS makes both teachable to beginners in
   one pass.
2. **Compute (Session 4) and networking (Session 5) stay separate, matching the official
   training split.** The exam study guide groups compute and networking in one skill, but
   the official learning path now ships them as two modules ("Describe Azure compute
   services" and "Describe Azure networking services"). Following the training split
   gives networking a full session, which is where beginners need it.
3. **Cost management (Session 8) explicitly re-teaches objective 1.1.6.** Reservations,
   Azure savings plan for compute, and spot pricing are Domain 1 exam content that
   Microsoft documents in the Domain 3 cost module, so the second pass is scheduled rather
   than left to chance.

Everything else follows the suggested order: foundations, benefits and service types,
architecture, compute, networking, storage, identity and security, cost, governance,
management and deployment, monitoring plus cumulative review, then full exam readiness.

---

# Week 1 — Cloud foundations

## Session 1 — Cloud Computing Foundations

**Objectives taught:** 1.1.1, 1.1.2, 1.1.3, 1.1.4, 1.1.5
**Domain minutes:** Domain 1 — 120

| Block | Minutes | Content |
| --- | --- | --- |
| Orientation | 10 | Course map, the three exam domains and their weights, what the AZ-900 exam is and is not, how the 12 sessions and the 10-day post-course window fit together. Replaces the warm-up in Session 1 only. |
| Teach A | 25 | What cloud computing is (1.1.1). Compute, storage, networking as rented capacity. On-premises vs cloud vocabulary that beginners need for every later session. |
| Teach B | 25 | Shared responsibility model (1.1.2) and cloud models — public, private, hybrid (1.1.3), plus multicloud as vocabulary. Who patches what, in IaaS vs PaaS vs SaaS terms that get formalized in Session 2. |
| Practice | 30 | Two sorting exercises: (a) given 12 responsibilities, place each on the customer/provider/shared boundary for IaaS, PaaS, and SaaS; (b) given 8 short organization scenarios, pick public, private, or hybrid and defend it (1.1.4). Then a guided read-only Azure portal tour so learners see the console they will use for the rest of the course (also first exposure to 3.3.1). |
| Teach C | 15 | Consumption-based model (1.1.5): CapEx vs OpEx, pay for what you use, capacity planning without overprovisioning. |
| Session quiz | 15 | 1.1.1–1.1.5. |
| Wrap | 0 | Folded into the quiz review. |

**Practiced:** 1.1.1–1.1.5 (sorting and scenario exercises), 3.3.1 (portal tour)
**Quizzed:** 1.1.1–1.1.5
**Cumulative review target for later sessions:** shared responsibility reappears in S4 and S7; cloud models in S5; consumption model in S8.

**Assignment:** complete the [Describe cloud computing](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/) module, including its module assessment. Create an Azure account if using the free-account path (see course overview for the no-cost fallback).

**Sources:** [Describe cloud computing](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/) · [Shared responsibility in the cloud](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility) · [Consumption-based model unit](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/6-describe-consumption-based-model)

## Session 2 — Cloud Benefits, Pricing Models, and IaaS/PaaS/SaaS

**Objectives taught:** 1.1.6, 1.1.7, 1.2.1, 1.2.2, 1.2.3, 1.2.4, 1.3.1, 1.3.2, 1.3.3, 1.3.4
**Domain minutes:** Domain 1 — 120

| Block | Minutes | Content |
| --- | --- | --- |
| Warm-up | 10 | Retrieval on S1: shared responsibility boundaries, three cloud models, CapEx vs OpEx. |
| Teach A | 25 | Benefits of the cloud: high availability and scalability (1.2.1), reliability and predictability (1.2.2). Scale up vs scale out, why predictability has both performance and cost dimensions. |
| Teach B | 20 | Benefits continued: security and governance (1.2.3), manageability (1.2.4) — management *of* the cloud vs management *in* the cloud. Brief context note on sustainability (module content, not a listed objective). |
| Teach C | 20 | Cloud service types: IaaS (1.3.1), PaaS (1.3.2), SaaS (1.3.3), and where serverless sits (1.1.7) as an event-driven consumption model rather than a fourth service type. Pricing-model comparison (1.1.6): pay-as-you-go, reservations, Azure savings plan for compute, spot. |
| Practice | 30 | (a) Service-type triage: 12 workloads sorted into IaaS/PaaS/SaaS with a one-line justification (1.3.4). (b) Pricing-model matching: 6 workload profiles matched to pay-as-you-go, reservation, savings plan, or spot, including one deliberately interruption-tolerant batch job (1.1.6). (c) Instructor demo: create an Azure Function App in the portal to make serverless concrete (1.1.7). |
| Session quiz | 15 | 1.1.6, 1.1.7, 1.2.1–1.2.4, 1.3.1–1.3.4. |

**Practiced:** 1.1.6, 1.1.7, 1.2.1–1.2.4, 1.3.1–1.3.4
**Quizzed:** same
**Domain 1 checkpoint:** the S3 warm-up is extended to a 10-item Domain 1 checkpoint covering all 15 Domain 1 objectives.

**Assignment:** complete [Describe the benefits of using cloud services](https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/) and [Describe cloud service types](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/).

**Sources:** [Benefits module](https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/) · [Cloud service types module](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/) · [Cost factors unit (pricing models)](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/2-describe-factors-affect-costs-azure) · [Azure Functions unit (serverless)](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/6-functions)

---

# Week 2 — Azure architecture and compute

## Session 3 — Azure Architecture

**Objectives taught:** 2.1.1, 2.1.2, 2.1.3, 2.1.4, 2.1.5, 2.1.6, 2.1.7
**Domain minutes:** Domain 1 — 15, Domain 2 — 105

| Block | Minutes | Content |
| --- | --- | --- |
| Domain 1 checkpoint | 15 | 10-item cumulative check across all Domain 1 objectives, reviewed in class. Gaps here drive the S4 and S8 warm-up choices. |
| Teach A | 25 | Physical infrastructure: datacenters (2.1.3), regions (2.1.1), availability zones (2.1.2), region pairs and sovereign regions (2.1.1). Zonal vs zone-redundant vs non-regional services. |
| Teach B | 25 | Management infrastructure: resources and resource groups (2.1.4), subscriptions as billing and access-control boundaries (2.1.5), management groups (2.1.6), and the full hierarchy with inheritance (2.1.7). |
| Practice | 30 | (a) Vocabulary drill using the Azure global infrastructure site: for 8 statements, label each as datacenter, region, availability zone, region pair, or sovereign region (addresses gap G3). (b) In the portal or Cloud Shell, create a resource group, deploy one cheap resource into it, add a tag, and inspect the resource group blade. (c) Draw the hierarchy from tenant root group down to a resource and mark where policy and RBAC inherit. |
| Session quiz | 15 | 2.1.1–2.1.7. |
| Wrap | 10 | Naming-convention and resource-group-strategy discussion; preview of compute. |

**Practiced:** 2.1.1–2.1.7, plus 3.3.1 reinforcement
**Quizzed:** 2.1.1–2.1.7

**Assignment:** complete [Describe the core architectural components of Azure](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/).

**Sources:** [Core architectural components module](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/) · [Physical infrastructure unit](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/5-describe-azure-physical-infrastructure) · [Management infrastructure unit](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/6-describe-azure-management-infrastructure) · [Azure geographies](https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/) · [Management groups](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview)

## Session 4 — Azure Compute

**Objectives taught:** 2.2.1, 2.2.2, 2.2.3, 2.2.4
**Domain minutes:** Domain 1 — 10, Domain 2 — 95, Domain 3 — 15

| Block | Minutes | Content |
| --- | --- | --- |
| Warm-up | 10 | Retrieval on S1–S3, weighted to shared responsibility (1.1.2) and IaaS/PaaS placement (1.3.1, 1.3.2, 1.3.4) because compute is where those distinctions become concrete. |
| Teach A | 25 | Compute types compared (2.2.1): virtual machines, containers (Azure Container Instances, Azure Container Apps, AKS), and functions. Serverless second pass (1.1.7). |
| Teach B | 25 | VM options (2.2.2): Azure Virtual Machines, Virtual Machine Scale Sets, availability sets, Azure Virtual Desktop. Resources a VM requires (2.2.3): size family, disks, virtual network, public IP, NIC. Sizing vocabulary (D-series, E-series, B-series and the `D2s_v5` naming pattern). |
| Practice | 30 | Guided project: [Build a simple website endpoint with Azure Functions](https://learn.microsoft.com/en-us/training/modules/guided-project-build-basic-website-endpoint-with-functions/). Then in the portal, start a VM creation flow and an App Service creation flow side by side and compare the decisions each one demands (2.2.3, 2.2.4). Export the VM's ARM template from the review page without deploying (first exposure to 3.3.5). No-cost fallback: complete the creation flows up to the Review + create page and discard. |
| Teach C | 15 | Application hosting options (2.2.4): Azure App Service (web apps, API apps, WebJobs, mobile apps), containers, VMs — and how to choose. |
| Session quiz | 15 | 2.2.1–2.2.4, plus two items on 1.1.7. |

**Practiced:** 2.2.1–2.2.4, 1.1.7, 3.3.5
**Quizzed:** 2.2.1–2.2.4, 1.1.7

**Assignment:** complete [Describe Azure compute services](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/).

**Sources:** [Compute services module](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/) · [VMs unit](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/2-virtual-machines) · [Containers unit](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/5-containers) · [Application hosting unit](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/7-describe-application-hosting-options) · [VM Scale Sets](https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/overview) · [Availability sets](https://learn.microsoft.com/en-us/azure/virtual-machines/availability-set-overview) · [Azure Virtual Desktop](https://learn.microsoft.com/en-us/azure/virtual-desktop/overview)

---

# Week 3 — Networking and storage

## Session 5 — Azure Networking

**Objectives taught:** 2.2.5, 2.2.6
**Domain minutes:** Domain 1 — 5, Domain 2 — 95, Domain 3 — 20

| Block | Minutes | Content |
| --- | --- | --- |
| Warm-up | 10 | Retrieval on S1–S4, weighted to cloud models (1.1.3, 1.1.4) as the setup for hybrid connectivity, and compute types (2.2.1, 2.2.2). |
| Teach A | 25 | Virtual networks and subnets (2.2.5): isolation and segmentation, private address space, internet inbound and outbound, communication between Azure resources, route tables and user-defined routes, network security groups as traffic filters. |
| Teach B | 25 | Connectivity (2.2.5): VNet peering, Azure DNS, point-to-site and site-to-site VPN with Azure VPN Gateway, ExpressRoute as private non-internet connectivity. When each one is the right answer. |
| Teach C | 15 | Public and private endpoints (2.2.6), and how both differ from service endpoints (gap G4). |
| Practice | 30 | In Cloud Shell with the Azure CLI, create a virtual network with two subnets, then inspect it in the portal (2.2.5, and 3.3.2 practice). Endpoint discrimination exercise: 9 short descriptions labeled public endpoint, private endpoint, or service endpoint (2.2.6). Instructor demo of a peering configuration and a DNS zone. No-cost fallback: the CLI commands are read and traced against the docs instead of executed. |
| Session quiz | 15 | 2.2.5, 2.2.6. |

**Practiced:** 2.2.5, 2.2.6, 3.3.2
**Quizzed:** 2.2.5, 2.2.6

**Assignment:** complete [Describe Azure networking services](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/).

**Sources:** [Networking services module](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/) · [Virtual networking unit](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/2-virtual-network) · [Virtual Network docs](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview) · [VNet peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-peering-overview) · [Azure DNS](https://learn.microsoft.com/en-us/azure/dns/dns-overview) · [VPN Gateway](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpngateways) · [ExpressRoute](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction) · [Private endpoints](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)

## Session 6 — Azure Storage

**Objectives taught:** 2.3.1, 2.3.2, 2.3.3, 2.3.4, 2.3.5, 2.3.6
**Domain minutes:** Domain 1 — 5, Domain 2 — 95, Domain 3 — 20

| Block | Minutes | Content |
| --- | --- | --- |
| Warm-up | 10 | Retrieval on S2–S5, weighted to reliability and predictability (1.2.2) and availability zones (2.1.2), which redundancy options build on. |
| Teach A | 25 | Storage accounts and storage types (2.3.4) and the core services compared (2.3.1): Blobs, Files, Queues, Disks, Tables, with one canonical use case each. |
| Teach B | 25 | Redundancy (2.3.3): LRS, ZRS, GRS, GZRS and read-access variants, tied back to zones and region pairs. Access tiers (2.3.2): hot, cool, cold, archive, with minimum-retention and rehydration trade-offs. |
| Teach C | 15 | Moving files (2.3.5): AzCopy, Azure Storage Explorer, Azure File Sync. Migration (2.3.6): Azure Migrate for workload assessment and migration, Azure Data Box for offline bulk transfer. |
| Practice | 30 | Guided project: [Deploy a static website with Azure Blob Storage](https://learn.microsoft.com/en-us/training/modules/guided-project-deploy-static-website-blob-storage/) or [Share files securely](https://learn.microsoft.com/en-us/training/modules/guided-project-share-files-securely/). Then price two storage designs in the [pricing calculator](https://azure.microsoft.com/en-us/pricing/calculator/) — hot/LRS vs cool/GRS on the same capacity — and explain the delta (2.3.2, 2.3.3, and 3.1.2 practice). Tool-selection drill: 6 transfer scenarios matched to AzCopy, Storage Explorer, File Sync, Azure Migrate, or Data Box. |
| Session quiz | 15 | 2.3.1–2.3.6. |

**Practiced:** 2.3.1–2.3.6, 3.1.2
**Quizzed:** 2.3.1–2.3.6

**Assignment:** complete [Describe Azure storage services](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/).

**Sources:** [Storage services module](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/) · [Storage services unit](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/4-describe-azure-storage-services) · [Storage introduction](https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction) · [Access tiers](https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview) · [Redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy) · [Storage account overview](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview) · [AzCopy](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10) · [Azure File Sync](https://learn.microsoft.com/en-us/azure/storage/file-sync/file-sync-introduction) · [Azure Migrate](https://learn.microsoft.com/en-us/azure/migrate/migrate-services-overview) · [Azure Data Box](https://learn.microsoft.com/en-us/azure/databox/data-box-overview)

---

# Week 4 — Identity, security, and cost

## Session 7 — Azure Identity, Access, and Security

**Objectives taught:** 2.4.1, 2.4.2, 2.4.3, 2.4.4, 2.4.5, 2.4.6, 2.4.7, 2.4.8
**Domain minutes:** Domain 1 — 10, Domain 2 — 100, Domain 3 — 10

This session carries eight objectives, the most of any session. The trade is deliberate:
the objectives are conceptually tight (identity, then authorization, then security
posture) and the guided project exercises most of them at once.

| Block | Minutes | Content |
| --- | --- | --- |
| Warm-up | 10 | Retrieval on S1–S6, weighted to shared responsibility (1.1.2), security and governance benefits (1.2.3), SaaS (1.3.3), and the networking and storage material that security builds on (2.2.5, 2.2.6, 2.3.1). |
| Teach A | 25 | Directory services (2.4.1): Microsoft Entra ID, Microsoft Entra Connect for hybrid sync, Microsoft Entra Domain Services for managed domain scenarios. Tenant vs subscription vs directory. |
| Teach B | 25 | Authentication (2.4.2): SSO, MFA, passwordless. External identities (2.4.3): B2B collaboration, B2B direct connect, Microsoft Entra External ID for customers. Conditional Access (2.4.4) as signal-driven policy. |
| Teach C | 20 | Authorization and posture: Azure RBAC with scope inheritance (2.4.5), Zero Trust principles (2.4.6), defense in depth layers (2.4.7), Microsoft Defender for Cloud (2.4.8). Brief context note on encryption and key management (module content, not a listed objective). |
| Practice | 30 | Guided project: [Set up new employee access (Entra ID and RBAC)](https://learn.microsoft.com/en-us/training/modules/guided-project-new-employee-access/). Then: assign a built-in role at resource-group scope and predict its effective permissions at resource scope (2.4.5); review Conditional Access policy templates read-only (2.4.4); tour Defender for Cloud's secure score and recommendations (2.4.8). Defense-in-depth layering exercise: place 8 controls on the correct layer (2.4.7). |
| Session quiz | 10 | 2.4.1–2.4.8. |

**Practiced:** 2.4.1–2.4.8
**Quizzed:** 2.4.1–2.4.8
**Domain 2 checkpoint:** the S8 warm-up is extended to a 12-item Domain 2 checkpoint across 2.1–2.4.

**Assignment:** complete [Describe Azure identity, access, and security](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/).

**Sources:** [Identity module](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/) · [Directory services unit](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/2-directory-services) · [External identities unit](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/4-external-identities) · [Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/fundamentals/whatis) · [Entra Domain Services](https://learn.microsoft.com/en-us/entra/identity/domain-services/overview) · [Conditional Access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview) · [Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview) · [Zero Trust](https://learn.microsoft.com/en-us/security/zero-trust/zero-trust-overview) · [Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction)

## Session 8 — Azure Cost Management

**Objectives taught:** 3.1.1, 3.1.2, 3.1.3, 3.1.4 (plus scheduled second pass on 1.1.6)
**Domain minutes:** Domain 1 — 20, Domain 2 — 5, Domain 3 — 95

| Block | Minutes | Content |
| --- | --- | --- |
| Domain 2 checkpoint | 15 | 12-item cumulative check across Domain 2, reviewed in class. |
| Teach A | 25 | Factors that affect costs (3.1.1): resource type and settings, consumption, maintenance and orphaned resources, geography and billing zones for data transfer, subscription type, Azure Marketplace third-party billing. Opens by recapping the consumption-based model (1.1.5) and what "you pay for what you use" means concretely (1.1.1), then the pricing-model second pass (1.1.6): pay-as-you-go, reservations, Azure savings plan for compute, spot. |
| Teach B | 25 | Cost management capabilities (3.1.3): Microsoft Cost Management, cost analysis, budgets and alerts. The pricing calculator (3.1.2) and what it does and does not tell you. Tags (3.1.4) as the mechanism that makes cost reporting answer business questions. |
| Practice | 30 | Guided project: [Set up cost guardrails in Azure](https://learn.microsoft.com/en-us/training/modules/guided-project-cost-guardrails/). Then build a three-resource monthly estimate in the pricing calculator and re-price it in a second region to quantify the geography factor (3.1.1, 3.1.2). Apply a tag set to a resource group and explain which cost question each tag answers (3.1.4). Review cost analysis views if a subscription with usage is available. |
| Session quiz | 15 | 3.1.1–3.1.4 and 1.1.6. |
| Wrap | 10 | The retired TCO calculator: why older study material still shows it, and what the current objective actually asks. |

**Practiced:** 3.1.1–3.1.4, 1.1.6
**Quizzed:** 3.1.1–3.1.4, 1.1.6

**Assignment:** complete [Describe cost management in Azure](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/).

**Sources:** [Cost management module](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/) · [Cost factors unit](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/2-describe-factors-affect-costs-azure) · [Pricing calculator unit](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/3-compare-pricing-total-cost-of-ownership-calculators) · [Microsoft Cost Management](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/overview-cost-management) · [Pricing calculator](https://azure.microsoft.com/en-us/pricing/calculator/) · [Tag resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources)

---

# Week 5 — Governance and management

## Session 9 — Governance and Compliance

**Objectives taught:** 3.2.1, 3.2.2, 3.2.3
**Domain minutes:** Domain 1 — 5, Domain 2 — 5, Domain 3 — 110

| Block | Minutes | Content |
| --- | --- | --- |
| Warm-up | 10 | Retrieval weighted to hierarchy and inheritance (2.1.7), RBAC scope (2.4.5), tags (3.1.4), and the security-and-governance benefit (1.2.3). Governance only makes sense on top of these. |
| Teach A | 25 | Azure Policy (3.2.2): definitions, initiatives, assignment scope, compliance state, and how audit differs from deny. How Policy differs from RBAC — what you may do vs what a resource may look like. |
| Teach B | 25 | Resource locks (3.2.3): CanNotDelete and ReadOnly, inheritance, and why locks stop accidental deletion but not permission problems. Microsoft Purview in Azure (3.2.1): data governance and compliance purpose, scoped to what AZ-900 asks (gap G7). Brief context note on the Service Trust Portal. |
| Practice | 30 | Guided project: [Organize and protect resources with tags and locks](https://learn.microsoft.com/en-us/training/modules/guided-project-organize-resources-tags-locks/). Then assign a built-in audit policy at resource-group scope and read its compliance results (3.2.2); apply a CanNotDelete lock and attempt a delete to see the failure (3.2.3). Governance-tool triage: 9 requirements matched to Policy, RBAC, locks, tags, or Purview. |
| Session quiz | 15 | 3.2.1–3.2.3. |
| Wrap | 15 | Common confusions: Policy vs RBAC vs locks; management-group-level vs subscription-level governance. |

**Practiced:** 3.2.1–3.2.3, 3.1.4
**Quizzed:** 3.2.1–3.2.3

**Assignment:** complete [Describe features and tools in Azure for governance and compliance](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/).

**Sources:** [Governance and compliance module](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/) · [Microsoft Purview](https://learn.microsoft.com/en-us/purview/purview) · [Azure Policy](https://learn.microsoft.com/en-us/azure/governance/policy/overview) · [Lock resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources)

## Session 10 — Managing and Deploying Azure Resources

**Objectives taught:** 3.3.1, 3.3.2, 3.3.3, 3.3.4, 3.3.5
**Domain minutes:** Domain 1 — 5, Domain 2 — 5, Domain 3 — 110

| Block | Minutes | Content |
| --- | --- | --- |
| Warm-up | 10 | Retrieval weighted to compute and hosting choices (2.2.1, 2.2.4), RBAC (2.4.5), Policy and locks (3.2.2, 3.2.3), and the manageability benefit (1.2.4). |
| Teach A | 25 | Interfaces (3.3.1, 3.3.2): the Azure portal, Azure Cloud Shell, Azure CLI, Azure PowerShell — what each is for, and why CLI and PowerShell are functionally equivalent with different syntax. Brief context note on Copilot in Azure (module content, not a listed objective). |
| Teach B | 25 | Azure Resource Manager as the control plane every interface calls (3.3.5), ARM templates and declarative deployment, and infrastructure as code as a practice (3.3.4): repeatability, review, idempotence. One sentence on Bicep as current authoring practice, labeled context (gap G8). |
| Teach C | 15 | Azure Arc (3.3.3): projecting non-Azure and multicloud resources into Azure management so Policy, RBAC, and monitoring apply consistently. |
| Practice | 30 | Guided project: [Manage Azure resources with Cloud Shell and the Azure CLI](https://learn.microsoft.com/en-us/training/modules/guided-project-manage-resources-cloud-shell-cli/). Then run the same task three ways — portal, CLI, PowerShell — on one resource group and compare (3.3.1, 3.3.2). Export an existing resource's ARM template, identify parameters and resources sections, and redeploy into a second resource group (3.3.4, 3.3.5). |
| Session quiz | 15 | 3.3.1–3.3.5. |

**Practiced:** 3.3.1–3.3.5
**Quizzed:** 3.3.1–3.3.5

**Assignment:** complete [Describe features and tools for managing and deploying Azure resources](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/).

**Sources:** [Managing and deploying module](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/) · [Tools for interacting with Azure unit](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/2-describe-interacting-azure) · [Azure portal](https://learn.microsoft.com/en-us/azure/azure-portal/azure-portal-overview) · [Cloud Shell](https://learn.microsoft.com/en-us/azure/cloud-shell/overview) · [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/what-is-azure-cli) · [Azure PowerShell](https://learn.microsoft.com/en-us/powershell/azure/what-is-azure-powershell) · [Azure Arc](https://learn.microsoft.com/en-us/azure/azure-arc/overview) · [Infrastructure as code](https://learn.microsoft.com/en-us/devops/deliver/what-is-infrastructure-as-code) · [ARM](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview) · [ARM templates](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/overview)

---

# Week 6 — Monitoring and exam readiness

## Session 11 — Monitoring + Cumulative Review

**Objectives taught:** 3.4.1, 3.4.2, 3.4.3
**Domain minutes:** Domain 1 — 40, Domain 2 — 30, Domain 3 — 50

| Block | Minutes | Content |
| --- | --- | --- |
| Teach A | 20 | Azure Advisor (3.4.1) across its recommendation categories, and Azure Service Health (3.4.2): service issues, planned maintenance, health advisories, and resource health. |
| Teach B | 25 | Azure Monitor (3.4.3) as the platform, then each named component separately: Log Analytics for querying collected data, Azure Monitor alerts with action groups, Application Insights for application telemetry (gap G9). |
| Practice | 25 | Guided project: [Monitor Azure with Service Health and Activity Log alerts](https://learn.microsoft.com/en-us/training/modules/guided-project-monitor-service-health-activity-alerts/). Then review Advisor recommendations on any available subscription and classify each by category (3.4.1); run one provided Log Analytics query and read the result (3.4.3). |
| Cumulative review | 35 | Full sweep of Domains 1 and 2 (42 objectives) as a rapid-fire objective checklist plus targeted re-teaching of the two weakest areas from the S3 and S8 checkpoint data. Each learner marks every objective confident / shaky / blank on a printed objective checklist. |
| Session quiz | 15 | Doubles as the Domain 3 checkpoint: 3.4.1–3.4.3 in depth, plus mixed items spanning 3.1–3.3 and the Domain 1 and 2 review. |

**Practiced:** 3.4.1–3.4.3, plus review practice across Domains 1 and 2
**Quizzed:** 3.4.1–3.4.3, with checkpoint items across 3.1–3.3 and mixed Domain 1–2 review items
**Domain 3 checkpoint:** this session quiz. Objectives 3.1–3.3 were each quizzed in their own session and are swept again in S12.

**Assignment:** complete [Describe monitoring tools in Azure](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/). Take the [official AZ-900 practice assessment](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-900/practice/assessment?assessment-type=practice&assessmentId=23) once before Session 12 and bring the score-by-domain result.

**Sources:** [Monitoring module](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/) · [Azure Monitor unit](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/4-describe-azure-monitor) · [Azure Advisor](https://learn.microsoft.com/en-us/azure/advisor/advisor-overview) · [Azure Service Health](https://learn.microsoft.com/en-us/azure/service-health/overview) · [Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/overview) · [Log Analytics](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-overview) · [Alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview) · [Application Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview)

## Session 12 — Full AZ-900 Exam Readiness

**Objectives taught:** none new. All 57 objectives are reviewed.
**Domain minutes:** Domain 1 — 50, Domain 2 — 25, Domain 3 — 45

| Block | Minutes | Content |
| --- | --- | --- |
| Timed practice | 45 | Full-length attempt at the [official Microsoft practice assessment](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-900/practice/assessment?assessment-type=practice&assessmentId=23) under exam conditions: 45 minutes, no notes, no discussion. Mirrors the 45-minute exam duration for Fundamentals exams. |
| Debrief | 30 | Score by domain, then item-by-item reasoning on every missed question. Learners log each miss against its objective ID on the objective checklist. |
| Gap clinic | 25 | Re-teach the three weakest objectives across the cohort, chosen from the debrief data. Domain 1 items usually dominate here, which is why Session 12 carries the largest Domain 1 minute allocation. |
| Exam logistics | 10 | Exam duration 45 minutes and seat time 65 minutes; score of 700 or greater required; proctored delivery; scheduling through Pearson VUE, or Certiport for students and educators; retake allowed 24 hours after a first failed attempt, with longer waits after that; Fundamentals certifications do not expire; Microsoft Learn is **not** available during Fundamentals exams. Walk through the [exam sandbox](https://aka.ms/examdemo) so the interface is familiar. |
| Post-course plan | 10 | Hand out and walk through the 10-day readiness plan in [`course-overview.md`](./course-overview.md), including when to schedule the exam. |

**Practiced / quizzed / reviewed:** all 57 objectives.

**Sources:** [AZ-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900) · [Exam AZ-900 page](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-900/) · [Exam duration and exam experience](https://learn.microsoft.com/en-us/credentials/support/exam-duration-exam-experience) · [Exam scoring and score reports](https://learn.microsoft.com/en-us/credentials/certifications/exam-scoring-reports) · [Retake policy](https://learn.microsoft.com/en-us/credentials/support/retake-policy) · [Request accommodations](https://learn.microsoft.com/en-us/credentials/certifications/request-accommodations) · [Exam sandbox](https://aka.ms/examdemo)

---

## Cumulative review schedule

Every session's warm-up pulls from earlier sessions on an expanding-interval schedule.
Read a row as: this session's content is revisited in these later sessions.

| Content from | Revisited in |
| --- | --- |
| S1 | S2, S3, S4, S5, S7, S8, S11, S12 |
| S2 | S3, S4, S6, S7, S8, S9, S10, S11, S12 |
| S3 | S4, S5, S6, S8, S9, S10, S11, S12 |
| S4 | S5, S6, S8, S10, S11, S12 |
| S5 | S6, S7, S8, S11, S12 |
| S6 | S7, S8, S10, S11, S12 |
| S7 | S8, S9, S10, S11, S12 |
| S8 | S9, S10, S11, S12 |
| S9 | S10, S11, S12 |
| S10 | S11, S12 |
| S11 | S12 |
| S12 | 10-day post-course plan |

Sessions 3, 8, 11, and 12 appear in most rows because they carry the domain checkpoints
and the full sweeps. Earlier content therefore recurs on an expanding interval — a few
days later in the next session's warm-up, again at the domain checkpoint, and again in
Week 6.

Domain checkpoints: Domain 1 at the start of S3, Domain 2 at the start of S8, Domain 3
within the S11 quiz, full sweep in S12.

## Practice inventory

| Session | Primary hands-on activity | Official guided project | No-cost fallback |
| --- | --- | --- | --- |
| S1 | Read-only portal tour, responsibility and cloud-model sorting | — | Instructor-shared screen |
| S2 | Service-type and pricing-model triage, Function App demo | — | Instructor demo only |
| S3 | Resource group create, tag, hierarchy diagram | — | Portal free-tier resources or diagram-only |
| S4 | VM and App Service creation flows compared, template export | Build a simple website endpoint with Azure Functions | Stop at Review + create, discard |
| S5 | VNet and subnets via Azure CLI in Cloud Shell, endpoint discrimination | — | Trace CLI commands against docs |
| S6 | Static website or file share, storage pricing comparison | Deploy a static website with Azure Blob Storage; Share files securely | Pricing calculator only |
| S7 | Role assignment and scope prediction, Defender for Cloud tour | Set up new employee access (Entra ID and RBAC) | Docs-based RBAC scope exercise |
| S8 | Pricing calculator estimate, budget and tags | Set up cost guardrails in Azure | Pricing calculator (no sign-in needed) |
| S9 | Audit policy assignment, resource lock test | Organize and protect resources with tags and locks | Policy definition reading exercise |
| S10 | Same task in portal, CLI, and PowerShell; ARM template export and redeploy | Manage Azure resources with Cloud Shell and the Azure CLI | Cloud Shell (included with any Azure account) |
| S11 | Service Health and Activity Log alert, Advisor triage, Log Analytics query | Monitor Azure with Service Health and Activity Log alerts | Sample query walkthrough from docs |
| S12 | Timed official practice assessment | — | Free with a Microsoft Learn account |

All eight guided projects from the official
[Apply Azure skills in guided projects](https://learn.microsoft.com/en-us/training/paths/introduction-cloud-infrastructure-apply-azure-skills-guided-projects/)
learning path are used across the course.
