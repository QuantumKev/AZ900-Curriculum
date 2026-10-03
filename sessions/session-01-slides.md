# Session 1 slides — Cloud Computing Foundations

Each `##` heading is one slide. Talk track is in
[session-01-instructor-notes.md](session-01-instructor-notes.md).

## 1. Cloud Computing Foundations

AZ-900, Session 1 of 12. Two hours.

Today: what the exam is, what cloud computing is, who is responsible for what, and how you pay for it.

## 2. What AZ-900 is

Microsoft Certified: Azure Fundamentals.

It checks vocabulary and judgment: given a situation, which cloud idea or Azure service fits.

Passing score: 700 or greater. Exam time: 45 minutes. Seat time: 65 minutes.

Fundamentals certifications do not expire.

## 3. What AZ-900 is not

Not a job-role exam. You will not configure a production environment on the exam.

Microsoft Learn is not available during Fundamentals exams.

There is no lab inside the exam. The questions are scenarios, comparisons, and definitions.

## 4. Three domains

| Domain | Weight |
| --- | --- |
| Describe cloud concepts | 25–30% |
| Describe Azure architecture and services | 35–40% |
| Describe Azure management and governance | 30–35% |

Skills measured as of July 20, 2026. Cloud concepts are a large share of a short exam, which is why we start here.

## 5. How these 12 sessions work

Each meeting: retrieval, teaching, practice, a short quiz, then an assignment on Microsoft Learn.

You sit the exam within 10 days after Session 12. We schedule it on the first day of that window.

Accommodations must be requested before you register. We will say that again in Session 12.

## 6. Cloud computing

Cloud computing is renting compute, storage, and networking from a provider, delivered over the internet, instead of buying and running those resources yourself.

Someone else's datacenter. Your workload. You pay for what you use.

## 7. The three things you are renting

- **Compute** — processing. Virtual machines, containers, functions, hosted apps.
- **Storage** — data at rest. Disks, files, objects.
- **Networking** — how those pieces reach each other and reach users.

Almost every later Azure service is one of these, or a managed combination of them.

## 8. Words we will use all course

| Word | Means |
| --- | --- |
| On-premises | In a datacenter or office the organization runs |
| Cloud | A provider's datacenters, consumed as a service |
| Workload | The application or job you are trying to run |
| Tenant | Your organization's identity boundary in Microsoft's cloud |
| Subscription | The billing and access boundary inside that tenant |
| Resource | One thing you create: a virtual machine, a storage account, a network |

## 9. Shared responsibility

The provider always owns the building, the physical network, and the physical hosts.

You always own your information and data, the devices people use to connect, and the accounts and identities in your environment.

Everything in between shifts as you move from infrastructure as a service, to platform as a service, to software as a service. We name those three formally next session.

## 10. Who patches the operating system

- You run a virtual machine you created: **you** patch the operating system.
- You deploy code to a platform the provider runs: **the provider** patches the operating system. You still own the code and the data.
- You subscribe to email the provider operates: **the provider** patches the application. You still own the mailboxes' contents and who can sign in.

## 11. Cloud models

- **Public** — anyone can buy it. Shared physical infrastructure. Azure is a public cloud.
- **Private** — used by a single organization. May sit on-premises or be hosted for that organization alone.
- **Hybrid** — public and private connected, so one workload or one organization uses both.
- **Multicloud** — more than one public cloud. Vocabulary only today; Azure Arc returns in Session 10.

## 12. Which model fits

Public: a new public website, a startup, a dev environment with no data-residency constraint.

Private: a workload that must stay on infrastructure dedicated to one organization.

Hybrid: regulated data stays private, while a seasonal burst uses public cloud. Or a migration that is only partway done.

The exam asks you to pick from a short scenario, not to design a network.

## 13. Consumption-based model

You pay for what you use, for as long as you use it.

Capacity planning changes: you do not buy the biggest server "just in case." You add capacity when demand shows up, and you stop paying when you release it.

This is operating expense, not a capital purchase of hardware.

## 14. CapEx and OpEx

- **Capital expenditure (CapEx)** — spend up front to own an asset. Servers, storage arrays, the room they sit in.
- **Operating expenditure (OpEx)** — spend as you go for a service. Cloud consumption is OpEx.

Next session compares the Azure pricing offers that sit on top of this model: pay-as-you-go, reservations, savings plan, spot.

## 15. Practice, then a quiz

Two sorts, then a look at the Azure portal.

The quiz is formative. We review every item before you leave. Target for the quiz: 80 percent. A miss is information, not a grade that follows you.

## 16. Before Session 2

Finish the Microsoft Learn module **Describe cloud computing**, including its assessment.

Create a free Microsoft Learn account if you have not.

Decide your hands-on path: Azure free account, a subscription we provide, or the no-cost path. The course can be finished with no Azure account.
