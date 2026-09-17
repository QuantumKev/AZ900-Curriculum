# AZ-900 Exam Objective Map

Every objective in this map is copied structurally (not verbatim in prose form) from the
official **Exam AZ-900 study guide**, skills measured **as of July 20, 2026**.

- Source of truth: [Study guide for Exam AZ-900](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900)
- Certification page: [Microsoft Certified: Azure Fundamentals](https://learn.microsoft.com/en-us/credentials/certifications/azure-fundamentals/) (page shows Last Updated 07/20/2026)
- Official course: [AZ-900T00-A: Introduction to Cloud Infrastructure](https://learn.microsoft.com/en-us/training/courses/az-900t00)

Objective IDs (`1.1.1`, `2.2.5`, …) are local to this repository. Microsoft does not
publish objective numbers, so these IDs exist only to make mapping, quiz banks, and
review sheets traceable. Wording in the tables is condensed; the official wording is the
only authority.

## Current domains and weights

| Domain | Official title | Weight | Objectives in this map |
| --- | --- | --- | --- |
| 1 | Describe cloud concepts | 25–30% | 15 |
| 2 | Describe Azure architecture and services | 35–40% | 27 |
| 3 | Describe Azure management and governance | 30–35% | 15 |
| | **Total** | **100%** | **57** |

Verified against the study guide's "Skills at a glance" section. The study guide change
log records the July 20, 2026 revision as **Minor** in three skill areas (Azure compute
and networking services; features and tools for managing and deploying Azure resources;
monitoring tools in Azure) and **No change** elsewhere. The three domain weights did not
change in that revision.

## How to read the coverage columns

| Column | Meaning |
| --- | --- |
| **Taught** | Session where the objective receives first-pass direct instruction. |
| **Practiced** | Session where learners do something with it: portal or CLI activity, guided project, sorting/scenario exercise, or calculator work. |
| **Quizzed** | Session whose end-of-session formative quiz includes the objective. Every session ends with a 15-minute quiz covering that session's objectives. |
| **Reviewed cumulatively** | Later sessions that revisit the objective through the 10-minute spaced-retrieval warm-up, a domain checkpoint, or the Session 12 readiness pass. |

Domain checkpoints are why some sessions appear in nearly every review column: the
Domain 1 checkpoint at the start of Session 3 sweeps all 15 Domain 1 objectives, the
Domain 2 checkpoint at the start of Session 8 sweeps all 27 Domain 2 objectives, the
Session 11 quiz sweeps Domain 3, and Session 12 sweeps all 57.

Quiz items themselves are **not** part of Phase 1. This map defines *where* assessment
happens so the Phase 2 quiz bank can be built against it.

Session numbers refer to [`six-week-plan.md`](./six-week-plan.md).

---

## Domain 1 — Describe cloud concepts (25–30%)

### 1.1 Describe cloud computing

| ID | Objective | Taught | Practiced | Quizzed | Reviewed cumulatively |
| --- | --- | --- | --- | --- | --- |
| 1.1.1 | Define cloud computing | S1 | S1 | S1 | S2, S3, S4, S8, S11, S12 |
| 1.1.2 | Describe the shared responsibility model | S1 | S1 | S1 | S2, S3, S4, S7, S11, S12 |
| 1.1.3 | Define cloud models, including public, private, and hybrid | S1 | S1 | S1 | S2, S3, S5, S11, S12 |
| 1.1.4 | Identify appropriate use cases for each cloud model | S1 | S1 | S1 | S2, S3, S5, S11, S12 |
| 1.1.5 | Describe the consumption-based model | S1 | S1 | S1 | S2, S3, S8, S11, S12 |
| 1.1.6 | Compare cloud pricing models | S2 | S2, S8 | S2, S8 | S3, S8, S11, S12 |
| 1.1.7 | Describe serverless | S2 | S2, S4 | S2, S4 | S3, S4, S11, S12 |

Sources:

- [Describe cloud computing](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/) (module)
- [Shared responsibility in the cloud](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility) (Azure docs)
- [Describe the consumption-based model](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/6-describe-consumption-based-model) (unit)
- Pricing-model comparison detail (pay-as-you-go, reservations, Azure savings plan for compute, spot) lives in [Describe factors that can affect costs in Azure](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/2-describe-factors-affect-costs-azure) — see gap **G1**.
- Serverless detail lives in [Describe Azure functions](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/6-functions) — see gap **G2**.

### 1.2 Describe the benefits of using cloud services

| ID | Objective | Taught | Practiced | Quizzed | Reviewed cumulatively |
| --- | --- | --- | --- | --- | --- |
| 1.2.1 | Describe the benefits of high availability and scalability in the cloud | S2 | S2 | S2 | S3, S4, S11, S12 |
| 1.2.2 | Describe the benefits of reliability and predictability in the cloud | S2 | S2 | S2 | S3, S6, S11, S12 |
| 1.2.3 | Describe the benefits of security and governance in the cloud | S2 | S2 | S2 | S3, S7, S9, S11, S12 |
| 1.2.4 | Describe the benefits of manageability in the cloud | S2 | S2 | S2 | S3, S10, S11, S12 |

Sources:

- [Describe the benefits of using cloud services](https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/) (module)
- [Availability zones overview](https://learn.microsoft.com/en-us/azure/reliability/availability-zones-overview) (Azure docs, supports 1.2.1/1.2.2)

The module also contains a **sustainability** unit. Sustainability is not a listed
objective in the July 20, 2026 skills measured; it is taught as context in Session 2 and
excluded from quizzing. See **context-only topics** below.

### 1.3 Describe cloud service types

| ID | Objective | Taught | Practiced | Quizzed | Reviewed cumulatively |
| --- | --- | --- | --- | --- | --- |
| 1.3.1 | Describe infrastructure as a service (IaaS) | S2 | S2, S4 | S2 | S3, S4, S11, S12 |
| 1.3.2 | Describe platform as a service (PaaS) | S2 | S2, S4 | S2 | S3, S4, S6, S11, S12 |
| 1.3.3 | Describe software as a service (SaaS) | S2 | S2 | S2 | S3, S7, S11, S12 |
| 1.3.4 | Identify appropriate use cases for each cloud service type (IaaS, PaaS, and SaaS) | S2 | S2, S4 | S2 | S3, S4, S6, S11, S12 |

Sources:

- [Describe cloud service types](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/) (module)

---

## Domain 2 — Describe Azure architecture and services (35–40%)

### 2.1 Describe the core architectural components of Azure

| ID | Objective | Taught | Practiced | Quizzed | Reviewed cumulatively |
| --- | --- | --- | --- | --- | --- |
| 2.1.1 | Describe Azure regions, region pairs, and sovereign regions | S3 | S3 | S3 | S5, S6, S8, S11, S12 |
| 2.1.2 | Describe availability zones | S3 | S3 | S3 | S6, S8, S11, S12 |
| 2.1.3 | Describe Azure datacenters | S3 | S3 | S3 | S8, S11, S12 |
| 2.1.4 | Describe Azure resources and resource groups | S3 | S3 | S3 | S4, S8, S9, S11, S12 |
| 2.1.5 | Describe subscriptions | S3 | S3 | S3 | S8, S9, S11, S12 |
| 2.1.6 | Describe management groups | S3 | S3 | S3 | S8, S9, S11, S12 |
| 2.1.7 | Describe the hierarchy of resource groups, subscriptions, and management groups | S3 | S3 | S3 | S8, S9, S10, S11, S12 |

Sources:

- [Describe the core architectural components of Azure](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/) (module)
- [Describe Azure physical infrastructure](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/5-describe-azure-physical-infrastructure) (unit: datacenters, regions, availability zones, region pairs, sovereign regions)
- [Describe Azure management infrastructure](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/6-describe-azure-management-infrastructure) (unit: resources, resource groups, subscriptions, management groups, hierarchy)
- [Azure geographies and global infrastructure](https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/)
- [Cross-region replication and region pairs](https://learn.microsoft.com/en-us/azure/reliability/cross-region-replication-azure)
- [Management groups overview](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview)

### 2.2 Describe Azure compute and networking services

| ID | Objective | Taught | Practiced | Quizzed | Reviewed cumulatively |
| --- | --- | --- | --- | --- | --- |
| 2.2.1 | Compare compute types, including containers, virtual machines, and functions | S4 | S4 | S4 | S5, S8, S10, S11, S12 |
| 2.2.2 | Describe virtual machine options, including Azure virtual machines, Azure Virtual Machine Scale Sets, availability sets, and Azure Virtual Desktop | S4 | S4 | S4 | S5, S8, S11, S12 |
| 2.2.3 | Describe the resources required for virtual machines | S4 | S4 | S4 | S5, S6, S8, S11, S12 |
| 2.2.4 | Describe application hosting options, including web apps, containers, and virtual machines | S4 | S4 | S4 | S6, S8, S10, S11, S12 |
| 2.2.5 | Describe virtual networking, including the purpose of Azure virtual networks, subnets, peering, Azure DNS, Azure VPN Gateway, and ExpressRoute | S5 | S5 | S5 | S6, S7, S8, S11, S12 |
| 2.2.6 | Define public and private endpoints | S5 | S5 | S5 | S6, S7, S8, S11, S12 |

Sources:

- [Describe Azure compute services](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/) (module)
- [Describe Azure networking services](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/) (module)
- [Describe Azure virtual machines](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/2-virtual-machines) (unit: sizes/families, scale sets, availability sets)
- [Describe Azure containers](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/5-containers) (unit: Azure Container Instances, Azure Container Apps, AKS)
- [Describe Azure functions](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/6-functions) (unit)
- [Describe application hosting options](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/7-describe-application-hosting-options) (unit: Azure App Service)
- [Describe Azure virtual networking](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/2-virtual-network) (unit: includes the public/private endpoint definitions)
- Azure docs: [Virtual Machines](https://learn.microsoft.com/en-us/azure/virtual-machines/overview) · [Virtual Machine Scale Sets](https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/overview) · [Availability sets](https://learn.microsoft.com/en-us/azure/virtual-machines/availability-set-overview) · [Azure Virtual Desktop](https://learn.microsoft.com/en-us/azure/virtual-desktop/overview) · [App Service](https://learn.microsoft.com/en-us/azure/app-service/overview) · [Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview) · [Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/overview) · [AKS](https://learn.microsoft.com/en-us/azure/aks/what-is-aks) · [Virtual Network](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview) · [VNet peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-peering-overview) · [Azure DNS](https://learn.microsoft.com/en-us/azure/dns/dns-overview) · [VPN Gateway](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpngateways) · [ExpressRoute](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction) · [Private endpoints](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)

The compute module also contains an **AI, machine learning, and IoT/Edge** unit, which
has no matching objective in the current skills measured. It is context only.

### 2.3 Describe Azure storage services

| ID | Objective | Taught | Practiced | Quizzed | Reviewed cumulatively |
| --- | --- | --- | --- | --- | --- |
| 2.3.1 | Compare Azure Storage services | S6 | S6 | S6 | S7, S8, S11, S12 |
| 2.3.2 | Describe storage tiers | S6 | S6 | S6 | S8, S11, S12 |
| 2.3.3 | Describe redundancy options | S6 | S6 | S6 | S8, S11, S12 |
| 2.3.4 | Describe storage account options and storage types | S6 | S6 | S6 | S8, S11, S12 |
| 2.3.5 | Identify options for moving files, including AzCopy, Azure Storage Explorer, and Azure File Sync | S6 | S6 | S6 | S8, S10, S11, S12 |
| 2.3.6 | Describe migration options, including Azure Migrate and Azure Data Box | S6 | S6 | S6 | S8, S10, S11, S12 |

Sources:

- [Describe Azure storage services](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/) (module)
- [Describe Azure storage services](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/4-describe-azure-storage-services) (unit: blobs, files, queues, disks, tables; hot/cool/cold/archive access tiers)
- Azure docs: [Storage introduction](https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction) · [Access tiers](https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview) · [Redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy) · [Storage account overview](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview) · [AzCopy](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10) · [Azure File Sync](https://learn.microsoft.com/en-us/azure/storage/file-sync/file-sync-introduction) · [Azure Migrate](https://learn.microsoft.com/en-us/azure/migrate/migrate-services-overview) · [Azure Data Box](https://learn.microsoft.com/en-us/azure/databox/data-box-overview)

### 2.4 Describe Azure identity, access, and security

| ID | Objective | Taught | Practiced | Quizzed | Reviewed cumulatively |
| --- | --- | --- | --- | --- | --- |
| 2.4.1 | Describe directory services in Azure, including Microsoft Entra ID and Microsoft Entra Domain Services | S7 | S7 | S7 | S8, S9, S11, S12 |
| 2.4.2 | Describe authentication methods in Azure, including single sign-on (SSO), multifactor authentication (MFA), and passwordless | S7 | S7 | S7 | S8, S9, S11, S12 |
| 2.4.3 | Describe external identities in Azure | S7 | S7 | S7 | S8, S11, S12 |
| 2.4.4 | Describe Microsoft Entra Conditional Access | S7 | S7 | S7 | S8, S9, S11, S12 |
| 2.4.5 | Describe Azure role-based access control (RBAC) | S7 | S7 | S7 | S8, S9, S10, S11, S12 |
| 2.4.6 | Describe the concept of Zero Trust | S7 | S7 | S7 | S8, S9, S11, S12 |
| 2.4.7 | Describe the purpose of the defense-in-depth model | S7 | S7 | S7 | S8, S9, S11, S12 |
| 2.4.8 | Describe the purpose of Microsoft Defender for Cloud | S7 | S7 | S7 | S8, S9, S11, S12 |

Sources:

- [Describe Azure identity, access, and security](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/) (module)
- [Describe Azure directory services](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/2-directory-services) (unit: Microsoft Entra ID, Microsoft Entra Connect, Microsoft Entra Domain Services)
- [Describe Azure external identities](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/4-external-identities) (unit: B2B collaboration, B2B direct connect, Microsoft Entra External ID for customers)
- Azure/Entra docs: [What is Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/fundamentals/whatis) · [Microsoft Entra Domain Services](https://learn.microsoft.com/en-us/entra/identity/domain-services/overview) · [SSO](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/what-is-single-sign-on) · [MFA](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mfa-howitworks) · [Passwordless](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-passwordless) · [External Identities](https://learn.microsoft.com/en-us/entra/external-id/external-identities-overview) · [Conditional Access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview) · [Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview) · [Zero Trust](https://learn.microsoft.com/en-us/security/zero-trust/zero-trust-overview) · [Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction)

The identity module also contains an **encryption and key management** unit, which has no
matching objective in the current skills measured. It is context only.

---

## Domain 3 — Describe Azure management and governance (30–35%)

### 3.1 Describe cost management in Azure

| ID | Objective | Taught | Practiced | Quizzed | Reviewed cumulatively |
| --- | --- | --- | --- | --- | --- |
| 3.1.1 | Describe factors that can affect costs in Azure | S8 | S8 | S8 | S9, S11, S12 |
| 3.1.2 | Explore the pricing calculator | S8 | S6, S8 | S8 | S11, S12 |
| 3.1.3 | Describe cost management capabilities in Azure | S8 | S8 | S8 | S9, S11, S12 |
| 3.1.4 | Describe the purpose of tags | S8 | S8, S9 | S8 | S9, S10, S11, S12 |

Sources:

- [Describe cost management in Azure](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/) (module)
- [Describe factors that can affect costs in Azure](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/2-describe-factors-affect-costs-azure) (unit: resource type, consumption, maintenance, geography, subscription type, Azure Marketplace; reservations, savings plan, spot)
- [Explore the pricing calculator](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/3-compare-pricing-total-cost-of-ownership-calculators) (unit; states the TCO calculator has been retired)
- Azure docs: [Microsoft Cost Management](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/overview-cost-management) · [Pricing calculator](https://azure.microsoft.com/en-us/pricing/calculator/) · [Tag resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources)

The cost module also contains a **cost optimization options** unit. The current objective
list stops at "cost management capabilities," so optimization practices (right-sizing,
shutting down unused resources, budgets, advisor-driven savings) are taught as applied
context inside 3.1.1 and 3.1.3 rather than as a separate examinable objective.

### 3.2 Describe features and tools in Azure for governance and compliance

| ID | Objective | Taught | Practiced | Quizzed | Reviewed cumulatively |
| --- | --- | --- | --- | --- | --- |
| 3.2.1 | Describe the purpose of Microsoft Purview in Azure | S9 | S9 | S9 | S11, S12 |
| 3.2.2 | Describe the purpose of Azure Policy | S9 | S9 | S9 | S10, S11, S12 |
| 3.2.3 | Describe the purpose of resource locks | S9 | S9 | S9 | S10, S11, S12 |

Sources:

- [Describe features and tools in Azure for governance and compliance](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/) (module)
- Azure docs: [Microsoft Purview](https://learn.microsoft.com/en-us/purview/purview) · [Azure Policy](https://learn.microsoft.com/en-us/azure/governance/policy/overview) · [Lock resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources)

The module also contains a **Service Trust Portal** unit with no matching objective in the
current skills measured. It is context only.

### 3.3 Describe features and tools for managing and deploying Azure resources

| ID | Objective | Taught | Practiced | Quizzed | Reviewed cumulatively |
| --- | --- | --- | --- | --- | --- |
| 3.3.1 | Describe the Azure portal | S10 | S1, S3, S10 | S10 | S11, S12 |
| 3.3.2 | Describe Azure Cloud Shell, Azure CLI, and Azure PowerShell | S10 | S5, S10 | S10 | S11, S12 |
| 3.3.3 | Describe the purpose of Azure Arc | S10 | S10 | S10 | S11, S12 |
| 3.3.4 | Describe infrastructure as code (IaC) | S10 | S10 | S10 | S11, S12 |
| 3.3.5 | Describe Azure Resource Manager (ARM) and ARM templates | S10 | S4, S10 | S10 | S11, S12 |

Sources:

- [Describe features and tools for managing and deploying Azure resources](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/) (module)
- [Describe tools for interacting with Azure](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/2-describe-interacting-azure) (unit: Azure portal, Azure PowerShell, Azure CLI, Azure Cloud Shell, Copilot in Azure)
- Azure docs: [Azure portal](https://learn.microsoft.com/en-us/azure/azure-portal/azure-portal-overview) · [Cloud Shell](https://learn.microsoft.com/en-us/azure/cloud-shell/overview) · [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/what-is-azure-cli) · [Azure PowerShell](https://learn.microsoft.com/en-us/powershell/azure/what-is-azure-powershell) · [Azure Arc](https://learn.microsoft.com/en-us/azure/azure-arc/overview) · [Infrastructure as code](https://learn.microsoft.com/en-us/devops/deliver/what-is-infrastructure-as-code) · [ARM](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview) · [ARM templates](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/overview)

The tools unit now also introduces **Copilot in Azure**, which is not a listed objective.
It is demonstrated in Session 10 as context and excluded from quizzing.

### 3.4 Describe monitoring tools in Azure

| ID | Objective | Taught | Practiced | Quizzed | Reviewed cumulatively |
| --- | --- | --- | --- | --- | --- |
| 3.4.1 | Describe the purpose of Azure Advisor | S11 | S11 | S11 | S12 |
| 3.4.2 | Describe Azure Service Health | S11 | S11 | S11 | S12 |
| 3.4.3 | Describe Azure Monitor, including Log Analytics, Azure Monitor alerts, and Azure Monitor Application Insights | S11 | S11 | S11 | S12 |

Sources:

- [Describe monitoring tools in Azure](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/) (module)
- [Describe Azure Monitor](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/4-describe-azure-monitor) (unit: Log Analytics, Azure Monitor alerts and action groups, Application Insights)
- Azure docs: [Azure Advisor](https://learn.microsoft.com/en-us/azure/advisor/advisor-overview) · [Azure Service Health](https://learn.microsoft.com/en-us/azure/service-health/overview) · [Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/overview) · [Log Analytics](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-overview) · [Azure Monitor alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview) · [Application Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview)

---

## Coverage summary

| Domain | Objectives | Taught | Practiced | Quizzed | Reviewed cumulatively |
| --- | --- | --- | --- | --- | --- |
| 1. Cloud concepts | 15 | 15 | 15 | 15 | 15 |
| 2. Azure architecture and services | 27 | 27 | 27 | 27 | 27 |
| 3. Azure management and governance | 15 | 15 | 15 | 15 | 15 |
| **Total** | **57** | **57 (100%)** | **57 (100%)** | **57 (100%)** | **57 (100%)** |

No objective is mapped to fewer than one teaching session, one practice activity, one
formative quiz, and one cumulative review touch. Every objective is also swept in
Session 12's full readiness pass.

### Objectives by session (first-pass teaching)

| Session | Objectives taught | Count |
| --- | --- | --- |
| S1 | 1.1.1–1.1.5 | 5 |
| S2 | 1.1.6, 1.1.7, 1.2.1–1.2.4, 1.3.1–1.3.4 | 10 |
| S3 | 2.1.1–2.1.7 | 7 |
| S4 | 2.2.1–2.2.4 | 4 |
| S5 | 2.2.5, 2.2.6 | 2 |
| S6 | 2.3.1–2.3.6 | 6 |
| S7 | 2.4.1–2.4.8 | 8 |
| S8 | 3.1.1–3.1.4 | 4 |
| S9 | 3.2.1–3.2.3 | 3 |
| S10 | 3.3.1–3.3.5 | 5 |
| S11 | 3.4.1–3.4.3 | 3 |
| S12 | none (cumulative readiness) | 0 |
| | **Total** | **57** |

Sessions 5, 9, and 11 carry fewer new objectives on purpose. Networking (S5) and
governance (S9) are where beginner learners historically stall, and S11 must absorb both
new monitoring content and the first full cumulative review, so those sessions trade
breadth for depth and reinforcement.

### Instructional time against exam weights

Minutes are planned per session in [`six-week-plan.md`](./six-week-plan.md); the totals
below include first-pass teaching, practice, quizzing, and review time attributed to each
domain.

| Domain | Exam weight | Planned minutes | Share of 1,440 min | In range |
| --- | --- | --- | --- | --- |
| 1. Cloud concepts | 25–30% | 405 | 28.1% | Yes |
| 2. Azure architecture and services | 35–40% | 560 | 38.9% | Yes |
| 3. Azure management and governance | 30–35% | 475 | 33.0% | Yes |
| **Total** | **100%** | **1,440** | **100%** | — |

Domain 1 reaches its share through continued spaced review rather than front-loaded
lecture: 240 of its 405 minutes are in Sessions 1–2, and the remaining 165 are warm-ups,
the pricing-model second pass in Session 8, and the Session 11–12 review blocks.

---

## Gaps, weak coverage, and cross-domain placement

These are the places where the official objective list and the official training content
do not line up neatly, or where beginner learners predictably need more than the modules
provide.

| ID | Objective(s) | Issue | Mitigation in this curriculum |
| --- | --- | --- | --- |
| G1 | 1.1.6 Compare cloud pricing models | The Domain 1 learning path covers pay-as-you-go and CapEx/OpEx but not a side-by-side of pricing models. Reservations, Azure savings plan for compute, and spot pricing are taught in the Domain 3 cost module. | Teach the comparison in S2 using the cost-factors unit as the source, then re-teach it inside cost management in S8. Objective is quizzed in both S2 and S8. |
| G2 | 1.1.7 Describe serverless | No dedicated serverless unit exists in the Domain 1 path; the substantive treatment is the Azure Functions unit in the Domain 2 compute module. | Introduce serverless conceptually in S2 next to PaaS, then apply it in S4 with the Azure Functions guided project. Quizzed in S2 and S4. |
| G3 | 2.1.3 Describe Azure datacenters | The module treats datacenters briefly as the substrate for regions and zones; it is easy for learners to conflate datacenter, region, and availability zone. | Add a 10-minute vocabulary drill in S3 using the Azure global infrastructure site, and a distinguishing item set in the S3 quiz. |
| G4 | 2.2.6 Define public and private endpoints | Covered in only a short passage of the virtual networking unit, and commonly confused with service endpoints (also mentioned in the same unit). | Dedicated S5 teaching block plus a public/private/service endpoint discrimination exercise using the Private Link docs. |
| G5 | 2.3.4 Describe storage account options and storage types | The module focuses on services and redundancy; account kinds and performance tiers need the storage account overview doc. | Use the storage account overview doc in S6. **NEEDS VERIFICATION** of the current account-type and performance-tier list at delivery time, since this list changes. |
| G6 | 2.4.3 Describe external identities in Azure | Naming is mid-transition: the module says "Microsoft Entra External ID for customers (formerly Azure AD B2C)", and Azure AD B2C is closed to new customers effective May 1, 2025. | Teach B2B collaboration, B2B direct connect, and Microsoft Entra External ID for customers with current names only. Do not teach B2C-specific configuration. |
| G7 | 3.2.1 Describe the purpose of Microsoft Purview in Azure | Purview is a broad portfolio; beginners over-scope it. | Scope S9 strictly to governance/compliance purpose as framed by the module, and state explicitly what is out of scope for AZ-900. |
| G8 | 3.3.4 Describe infrastructure as code (IaC) | The objective names ARM and ARM templates; the wider Azure ecosystem has moved much IaC authoring to Bicep, which the objective does not name. | Teach IaC concepts and ARM/ARM templates as the examinable content; mention Bicep once as current practice and label it context, not exam scope. |
| G9 | 3.4.3 Describe Azure Monitor | One short unit covers Log Analytics, alerts, and Application Insights together; three distinct tools in roughly three minutes of official content. | Give each its own S11 block with a concrete example, plus the Service Health and Activity Log alerts guided project. |
| G10 | All practice activities | Several practice activities assume an Azure subscription the learner controls. | Every session lists a no-cost fallback (Cloud Shell, pricing calculator, read-only portal views, guided projects, instructor demo). See course overview. |

### Context-only topics (taught, not quizzed)

Present in the official modules but **not** in the July 20, 2026 skills measured. Teach
briefly for coherence, label as context, and keep out of the Phase 2 quiz bank:

- Sustainability considerations in the cloud (benefits module)
- AI, machine learning, and IoT/Edge services in Azure (compute module)
- Encryption and key management in Azure (identity module)
- Cost optimization options in Azure (cost module)
- Service Trust Portal (governance module)
- Copilot in Azure (managing and deploying module)

Whether any of these appear on the exam is **NEEDS VERIFICATION** — the study guide notes
that related topics may be covered even when not bulleted, so they are taught but not
weighted.

### Not in current objectives — do not treat as exam scope

Frequently found in older AZ-900 material, including both secondary references:

- Service level agreements and composite SLAs
- Azure Blueprints (retiring January 31, 2027, phased from July 31, 2026)
- Microsoft Cloud Adoption Framework for Azure (a study resource, not an objective)
- Microsoft Sentinel, Azure Key Vault, Azure Dedicated Hosts
- The Total Cost of Ownership (TCO) calculator (retired)
- Azure Marketplace as a standalone topic (it appears only as a cost factor in 3.1.1)

See [`../sources/source-validation-log.md`](../sources/source-validation-log.md) for the
conflict-by-conflict record.
