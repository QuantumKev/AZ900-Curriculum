# Source Validation Log

What was verified in Phase 1, against which source, and what it changed in the
curriculum. This is the audit trail for every factual claim in
[`../curriculum/`](../curriculum/).

## Rules applied

1. Microsoft Learn is the source of truth. Where a secondary source disagrees, Microsoft Learn wins and the disagreement is recorded here.
2. No content was copied verbatim from any source. Objective wording in the map is condensed; the official study guide is the only authority for exact wording.
3. No exam dumps were consulted. The only practice instrument referenced is Microsoft's official free practice assessment.
4. No Azure facts were invented. Anything not confirmable in current Microsoft documentation is marked **NEEDS VERIFICATION** rather than asserted.
5. The secondary repositories were not cloned. They were reviewed through their published pages and files.

### A note on dates

This curriculum uses **no calendar dates for scheduling** — sessions and the post-course
plan are relative only. Dates appear in this log solely as source version metadata
published by the source itself (for example, Microsoft's "Skills measured as of July 20,
2026", a product retirement date, or a repository's last-push timestamp). Those are facts
about the sources, not schedule entries.

---

## Verification pass — findings

### V1 — Current exam domains and weights

**Source:** [AZ-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900), "Skills at a glance"

Confirmed, skills measured as of **July 20, 2026**:

| Domain | Weight |
| --- | --- |
| Describe cloud concepts | 25–30% |
| Describe Azure architecture and services | 35–40% |
| Describe Azure management and governance | 30–35% |

The certification page shows **Last Updated 07/20/2026**, and the Microsoft Learn catalog
reports the same last-modified timestamp for the certification record, so the study guide
and the certification page agree on the current revision.

**Study guide change log for the July 20, 2026 revision:** audience profile — no change;
*Describe Azure architecture and services* — no change; *Describe Azure compute and
networking services* — **minor**; *Describe Azure management and governance* — no change;
*Describe features and tools for managing and deploying Azure resources* — **minor**;
*Describe monitoring tools in Azure* — **minor**.

**Result:** weights adopted as current. Instructional minutes were allocated to land
inside all three ranges (28.1% / 38.9% / 33.0%).

### V2 — Official exam objectives extracted

**Source:** same study guide, "Skills measured as of July 20, 2026"

All objective bullets were extracted into
[`../curriculum/exam-objective-map.md`](../curriculum/exam-objective-map.md) and assigned
local IDs: **57 objectives** across 11 skill groups (Domain 1: 15, Domain 2: 27,
Domain 3: 15).

Two notes carried from the study guide itself, both relevant to how the course is taught:

- The bulleted items illustrate how a skill is assessed; related topics may also appear. This is why context-only module topics are still taught, just not weighted.
- Most questions cover generally available features; preview features may appear if commonly used.

**Result:** the objective map is keyed to this list. Every one of the 57 objectives is
mapped to a teaching session, a practice activity, a formative quiz, and at least one
cumulative review touch.

### V3 — Official learning paths and modules reviewed

**Sources:** the three exam-content learning paths, the guided-projects path, and all 12
content modules (links in [`microsoft-learn-links.md`](./microsoft-learn-links.md)),
cross-checked against the Microsoft Learn catalog API for module and unit inventories.

Confirmed structure: Part 1 (3 modules), Part 2 (5 modules), Part 3 (4 modules), Part 4
(8 guided projects). Twelve content modules, which the curriculum maps one-to-one onto
Sessions 1–11.

Notable structural finding: the official training path **now separates compute and
networking into two modules** ("Describe Azure compute services" and "Describe Azure
networking services"), while the exam study guide still groups them under a single skill.
The compute module's URL still contains `compute-networking-services`, which is why older
links still resolve.

**Result:** the course follows the exam grouping for objective mapping and the training
split for sequencing — Session 4 compute, Session 5 networking.

### V4 — Serverless and pricing-model coverage gap

**Sources:** [consumption-based model unit](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/6-describe-consumption-based-model) · [Azure functions unit](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/6-functions) · [cost factors unit](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/2-describe-factors-affect-costs-azure)

Two Domain 1 objectives are taught outside the Domain 1 learning path:

- **Compare cloud pricing models (1.1.6):** the consumption-based model unit covers pay-as-you-go, CapEx vs OpEx, and capacity planning, but the side-by-side of pricing models — pay-as-you-go, reservations, Azure savings plan for compute, and Azure Spot Virtual Machines — is in the Domain 3 cost-factors unit.
- **Describe serverless (1.1.7):** there is no dedicated serverless unit in Part 1. The substantive treatment is the Azure Functions unit in the Domain 2 compute module.

**Result:** recorded as gaps G1 and G2. Both objectives are taught in Session 2 using the
cross-domain sources, then deliberately re-taught and re-quizzed where Microsoft teaches
them (1.1.6 in Session 8, 1.1.7 in Session 4).

### V5 — Current terminology confirmed

Checked against the current module units so the course never presents a retired name as
current.

| Current term | Confirmed in | Retired name still common in older material |
| --- | --- | --- |
| Microsoft Entra ID | [Directory services unit](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/2-directory-services) | Azure Active Directory, Azure AD |
| Microsoft Entra Connect | same unit | Azure AD Connect |
| Microsoft Entra Domain Services | same unit | Azure AD Domain Services, Azure AD DS |
| Microsoft Entra External ID for customers | [External identities unit](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/4-external-identities) | Azure AD B2C |
| Microsoft Defender for Cloud | identity module | Azure Security Center, Azure Defender |
| Microsoft Cost Management | cost module | Azure Cost Management + Billing (as a tool name) |
| Microsoft Purview | governance module | Azure Purview |
| Hot, cool, cold, and archive access tiers | [Storage services unit](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/4-describe-azure-storage-services) | Hot/cool/archive only — the **cold** tier is missing from older guides |
| Azure Container Instances, Azure Container Apps, AKS | [Containers unit](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/5-containers) | Container Instances treated as the only container option |
| Azure Monitor with Log Analytics, alerts, Application Insights | [Azure Monitor unit](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/4-describe-azure-monitor) | Azure Monitor treated as a single undifferentiated tool |

Also confirmed: **Azure AD B2C is no longer available to purchase for new customers
effective May 1, 2025** ([Azure AD B2C overview](https://learn.microsoft.com/en-us/azure/active-directory-b2c/overview)), which is why the external-identities objective is taught under the Entra External ID name only.

**Result:** the terminology table above is the reference for slides and handouts. Session
7 addresses the Entra renaming explicitly, because learners will encounter "Azure AD" in
almost every third-party resource they find.

### V6 — Total Cost of Ownership (TCO) calculator is retired

**Source:** [Explore the pricing calculator unit](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/3-compare-pricing-total-cost-of-ownership-calculators)

The unit states plainly that the TCO calculator has been retired, and the current
objective is "Explore the pricing calculator" — singular, no comparison. Older objective
wording asked candidates to compare the Pricing calculator and the TCO calculator, and
both secondary references still teach that comparison.

**Result:** Session 8 teaches the pricing calculator only, and closes with a short
explanation of why older study material shows a second calculator. This is a likely source
of learner confusion, so it is addressed rather than ignored.

### V7 — Copilot in Azure appears in official module content

**Source:** [Describe tools for interacting with Azure unit](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/2-describe-interacting-azure)

The unit now introduces Copilot in Azure alongside the portal, Azure PowerShell, the Azure
CLI, and Cloud Shell. Copilot is **not** a bulleted objective in the July 20, 2026 skills
measured. Its presence is consistent with the change log marking that skill area "minor."

Whether Copilot in Azure can appear on the exam is **NEEDS VERIFICATION** — the study
guide's own note allows for related topics.

**Result:** demonstrated in Session 10 as context, labeled as not-an-objective, and
excluded from the Phase 2 quiz bank.

### V8 — Official course duration conflict

**Sources:** [AZ-900T00 course page](https://learn.microsoft.com/en-us/training/courses/az-900t00) · Microsoft Learn catalog API record for `course.az-900t00`

The course page displays **Course Duration: 1 day**. The catalog record for the same
course reports **24 hours**. Both are Microsoft sources and they disagree.

**Status: NEEDS VERIFICATION.**

**Result:** this course's 24 instructional hours match the catalog figure. The conflict is
disclosed in the course overview rather than silently resolved.

### V9 — Azure free account terms are described inconsistently

**Sources:** [cloud concepts learning path](https://learn.microsoft.com/en-us/training/paths/microsoft-azure-fundamentals-describe-cloud-concepts/) · [cost factors unit](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/2-describe-factors-affect-costs-azure) · [Azure free account](https://azure.microsoft.com/en-us/free/)

The learning path blurb offers "Pay as you go or try Azure free for up to 30 days." The
cost-factors unit describes a free trial with products free for 12 months, credit to spend
within the first 30 days, and more than 25 always-free products. These framings do not
match, and free-account terms change.

**Status: NEEDS VERIFICATION** before every cohort.

**Result:** the course overview instructs instructors to confirm current terms on the
Azure free account page at cohort start, and no specific credit amount or duration is
stated anywhere in this curriculum.

### V10 — Exam logistics verified

**Sources:** [certification page](https://learn.microsoft.com/en-us/credentials/certifications/azure-fundamentals/?practice-assessment-type=certification) · [exam duration and exam experience](https://learn.microsoft.com/en-us/credentials/support/exam-duration-exam-experience) · [exam scoring and score reports](https://learn.microsoft.com/en-us/credentials/certifications/exam-scoring-reports) · [retake policy](https://learn.microsoft.com/en-us/credentials/support/retake-policy) · [certification renewal](https://learn.microsoft.com/en-us/credentials/certifications/renew-your-microsoft-certification)

Confirmed: passing score is **700 or greater**; Fundamentals exams have a **45-minute exam
duration and 65-minute seat time**; the exam is proctored and may include interactive
components; a first retake is allowed **24 hours** after a failed attempt with longer waits
after that; **Fundamentals certifications do not expire**; **Microsoft Learn is not
available during Fundamentals exams** (it is a role-based-exam feature only); a free
practice assessment and an exam sandbox both exist; scheduling is through Pearson VUE, or
Certiport for students and educators.

**Question count is NEEDS VERIFICATION.** Microsoft publishes only a general statement
that most exams contain 40–60 questions and explicitly says counts can vary and change. No
AZ-900-specific count is published, so none is stated in this curriculum.

**Result:** Session 12's logistics block uses exactly these facts. The "no Microsoft Learn
during the exam" point is called out because learners who have read about role-based exams
frequently assume otherwise.

### V11 — Secondary reference: AzureMentor AZ-900 Study Guide

**Source:** [AzureMentor/Azure-AZ-900-Study-Guide](https://github.com/AzureMentor/Azure-AZ-900-Study-Guide) — four markdown files reviewed through GitHub's published file contents; repository last pushed **April 7, 2025**; no license file; not cloned.

**Where it agrees with current Microsoft material:** domain titles and all three weight
ranges (25–30% / 35–40% / 30–35%) match; it uses Microsoft Entra ID and Microsoft Entra
Domain Services naming; it uses Microsoft Purview and Microsoft Defender for Cloud naming;
its objective list is otherwise close to the current one.

**Conflicts and drift:**

| # | Finding | Resolution |
| --- | --- | --- |
| C1 | Lists "Compare the Pricing Calculator and the Total Cost of Ownership (TCO) Calculator." | Microsoft Learn states the TCO calculator is retired and the objective is pricing calculator only. Microsoft wins. |
| C2 | Links external identities to the legacy Azure AD B2C documentation for the B2C capability. | Current module name is Microsoft Entra External ID for customers; B2C is closed to new customers as of May 1, 2025. Teach current naming only. |
| C3 | Splits "benefits of high availability" and "benefits of scalability" into two objectives. | Current study guide has a single combined bullet. Cosmetic, but the objective map follows the official bullet structure. |
| C4 | Routes the practice assessment through a third-party link shortener. | This curriculum uses the canonical `learn.microsoft.com` practice-assessment URL. |
| C5 | Two objective links are empty placeholders (containers under application hosting, virtual subnets). | Filled from Microsoft documentation in the objective map. |
| C6 | Predates the July 20, 2026 revision. | Not treated as current; used only as a cross-check. |

**Result:** useful as an independent confirmation that the domain weights adopted here are
right. Not used as a teaching source.

### V12 — Secondary reference: John Savill's AZ-900 Certification Course

**Source:** [johnthebrit/AZ900CertCourse](https://github.com/johnthebrit/AZ900CertCourse) — repository README and the 40-page course handout PDF reviewed; repository last pushed **April 6, 2025**; handout marked copyright 2025; no license file; not cloned.

The repository holds a handout of links and section headings for a video course, plus a
YouTube playlist pointer. It is a companion to video content rather than a study guide.

**Conflicts and drift:**

| # | Finding | Resolution |
| --- | --- | --- |
| C7 | Organized around an **older AZ-900 domain structure**, with section names such as "Describe General Security and Network Security Features," "Describe Azure Cost Management and Service Level Agreements," and "Describe Core Solutions and Management Tools on Azure." | The current exam has three domains with different skill groupings. Sequencing in this curriculum follows the current study guide. |
| C8 | Includes the **Pricing and TCO Calculators** together. | TCO calculator is retired. Same resolution as C1. |
| C9 | Includes **Azure Blueprints** as a topic. | Blueprints is not a current objective, and it is **retiring January 31, 2027 with phased retirement from July 31, 2026**, with migration to deployment stacks and template specs ([Blueprints overview](https://learn.microsoft.com/en-us/azure/governance/blueprints/overview)). Excluded. |
| C10 | Includes **service level agreements** as a topic area. | SLAs are not in the current skills measured. Excluded from exam-mapped content. |
| C11 | Includes topics outside the current objective list: Microsoft Cloud Adoption Framework, Microsoft Sentinel, Azure Key Vault, Azure Dedicated Hosts, DevOps technologies, AI services, and Azure Marketplace as its own topic. | All excluded as exam scope. Note that Azure Marketplace *is* in scope, but only as a cost factor inside objective 3.1.1, which is how this curriculum teaches it. |
| C12 | Predates the July 20, 2026 revision. | Not treated as current. |

**Positive note:** the handout uses current names where it matters most — Microsoft Entra,
Microsoft Sentinel, and Microsoft Defender for Cloud rather than their retired names — so
its terminology is not the problem. Its **scope** is the problem: it is broader than, and
structured differently from, the current exam.

**Result:** may be recommended to learners as optional video reinforcement, with an
explicit warning that its section structure predates the current exam and that several of
its topics are no longer exam scope.

---

## Consolidated: outdated terms and topics

Do **not** present any of these as current. Learners will meet all of them in third-party
material.

### Renamed

| Outdated | Current |
| --- | --- |
| Azure Active Directory / Azure AD | Microsoft Entra ID |
| Azure AD Connect | Microsoft Entra Connect |
| Azure AD Domain Services / Azure AD DS | Microsoft Entra Domain Services |
| Azure AD B2C | Microsoft Entra External ID for customers |
| Azure Security Center / Azure Defender | Microsoft Defender for Cloud |
| Azure Sentinel | Microsoft Sentinel (and not an AZ-900 objective) |
| Azure Purview | Microsoft Purview |
| Azure Cost Management + Billing (as tool name) | Microsoft Cost Management |

### Retired or retiring

| Item | Status |
| --- | --- |
| Total Cost of Ownership (TCO) calculator | Retired; Microsoft Learn states so directly |
| Azure Blueprints | Retiring January 31, 2027, phased from July 31, 2026; migrate to deployment stacks or template specs |
| Azure AD B2C for new customers | Not available to purchase for new customers effective May 1, 2025 |

### Dropped from the objectives (present in older AZ-900 material)

Service level agreements and composite SLAs · Azure Blueprints · Microsoft Cloud Adoption
Framework · Microsoft Sentinel · Azure Key Vault · Azure Dedicated Hosts · Azure
Marketplace as a standalone topic · the TCO calculator.

### Emphasis shifts rather than renames

- **Availability sets** remain a listed objective (2.2.2), but the official VM unit notes that in regions supporting availability zones, zone-based designs are often preferred. Teach availability sets as exam content without presenting them as the default resiliency answer.
- **Azure Monitor** should be taught as a platform with three named components rather than one tool, matching the current objective wording that explicitly names Log Analytics, Azure Monitor alerts, and Azure Monitor Application Insights.

---

## Consolidated: NEEDS VERIFICATION

| # | Item | Why it is uncertain | What to do |
| --- | --- | --- | --- |
| N1 | AZ-900 question count | Microsoft publishes only a general 40–60 range for most exams and says counts vary and change | Never state a count to learners; describe the 45-minute duration instead |
| N2 | Official course length: 1 day vs 24 hours | The AZ-900T00 course page and the Learn catalog record disagree (V8) | Keep the 24-hour plan; recheck the course page before publishing marketing copy |
| N3 | Azure free account terms | Microsoft Learn pages describe the offer inconsistently and the offer changes (V9) | Confirm on the Azure free account page at each cohort start; state no specifics in materials |
| N4 | Examinability of context-only module topics | Sustainability, encryption and key management, Service Trust Portal, AI/ML/IoT, cost optimization, Copilot in Azure appear in modules but not in the bulleted objectives; the study guide allows related topics | Teach briefly as context, exclude from the quiz bank, revisit if a future revision adds them |
| N5 | Current storage account types and performance tiers | The fundamentals module does not enumerate account kinds; this list changes over time (gap G5) | Read the storage account overview doc before teaching Session 6 |
| N6 | Whether availability sets are on a deprecation path | The VM unit expresses a preference for zone-based designs but announces no retirement | Do not tell learners availability sets are deprecated; teach the stated preference only |
| N7 | Practice assessment scoring and item count | Microsoft does not publish the practice assessment's length or how its score relates to the exam | Use the 85% two-attempt readiness bar as a course convention, not as a Microsoft claim |

---

## Re-validation procedure for future cohorts

Run this before each cohort, and immediately if Microsoft announces an AZ-900 update.

1. Open the [study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900) and check the "Skills measured as of" date. If it is later than **July 20, 2026**, read the change log table and continue; if not, the objective map is still current.
2. Diff the objective bullets against [`../curriculum/exam-objective-map.md`](../curriculum/exam-objective-map.md). Add, retire, or re-word objective IDs as needed; retired IDs should be struck rather than reused, so quiz items stay traceable.
3. Re-check the three domain weights and, if they moved, re-check the instructional-minute allocation table in the objective map and course overview.
4. Re-open the modules for any skill area marked changed, and update the affected session in [`../curriculum/six-week-plan.md`](../curriculum/six-week-plan.md).
5. Re-check the terminology table in this log against the current module units.
6. Re-check every item in the NEEDS VERIFICATION table; resolve what can now be resolved.
7. Re-check all links in [`microsoft-learn-links.md`](./microsoft-learn-links.md) for redirects and dead pages.
8. Append findings to this log rather than overwriting it, so the trail of what changed and when stays intact.
