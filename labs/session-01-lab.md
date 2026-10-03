# Session 1 lab — Shared responsibility, cloud models, portal tour

**Time:** 30 minutes
**Objectives practiced:** 1.1.1, 1.1.2, 1.1.3, 1.1.4, 1.1.5, and a first look at 3.3.1
**You need:** this worksheet, a pen. An Azure account is optional.

Work Part A, then Part B. Part C is a look at the portal. If you have no account, follow the no-cost path and watch the instructor's screen.

---

## Part A — Who is responsible? (12 minutes)

For each row, mark who is responsible under **IaaS** (a virtual machine you manage), **PaaS** (a platform you deploy code to), and **SaaS** (a finished application you subscribe to).

Use **C** for customer, **P** for provider. Some rows never change.

| # | Responsibility | IaaS | PaaS | SaaS |
| --- | --- | --- | --- | --- |
| 1 | Physical building and datacenter security | | | |
| 2 | Physical network between hosts | | | |
| 3 | Physical servers | | | |
| 4 | Information and data you store | | | |
| 5 | Laptops and phones people use to connect | | | |
| 6 | Accounts and identities — who is allowed in | | | |
| 7 | Operating system patches on a virtual machine you created | | | |
| 8 | Operating system patches on a platform you only deploy code to | | | |
| 9 | Application code you wrote and deployed | | | |
| 10 | The application code of a subscribed email service | | | |
| 11 | Deciding which users may open the application | | | |
| 12 | The virtualization layer under a virtual machine | | | |

One sentence, after the grid: which three rows were **C** in every column, and which three were **P** in every column?

## Part B — Which cloud model? (8 minutes)

For each organization, write **public**, **private**, or **hybrid**, and a reason of one line.

1. A campus club wants a public website. No regulation requires dedicated hardware.
2. A bank keeps trading systems on infrastructure used only by that bank, in facilities dedicated to it.
3. A hospital keeps patient records on dedicated infrastructure and uses a public cloud for the seasonal flu-shot scheduling site.
4. A startup builds a new mobile back end and wants to rent capacity by the hour with no datacenter of its own.
5. A manufacturer runs factory systems on its own cloud hardware and bursts monthly reporting into a public cloud.
6. A city agency is required to use a cloud environment dedicated to that government, not a shared public region.
7. A design firm has no servers and adopts a browser-based design suite anyone can buy.
8. A retailer runs the catalog on a public cloud and keeps the payment system on infrastructure dedicated to the company, connected to that public cloud.

## Part C — Portal tour (10 minutes)

Sign in at [https://portal.azure.com](https://portal.azure.com). Look only. Do not create anything.

1. Home. Find the search bar.
2. Search **Subscriptions**. Open the subscription you will use this course. Note its name.
3. Search **Resource groups**. Confirm whether any exist. A resource group is a folder for things you create. We create one in Session 3.
4. Search **Microsoft Entra ID**. Notice it opens a directory, not a virtual machine. Identity is a later session. Today you are only seeing that the portal is wider than "servers."
5. Sign out if this is a shared machine.

### No-cost path

Skip sign-in. Watch the instructor hit the same four stops. Write down the four names you saw: Home, Subscriptions, Resource groups, Microsoft Entra ID.

On paper, add one sentence: cloud computing, as you would say it to a coworker who has never heard the term. Check it against this bar: it mentions rented capacity, and it mentions at least two of compute, storage, and networking.

<div class="pagebreak"></div>

## Instructor key

Do not print this page for learners.

### Part A

Rows 1, 2, 3, and 12 are **P** in every column. The provider always owns the physical datacenter, the physical network, the physical hosts, and the virtualization layer under the service.

Rows 4, 5, 6, and 11 are **C** in every column. The customer always owns data, connecting devices, and identities, including who may use a SaaS application.

| # | IaaS | PaaS | SaaS |
| --- | --- | --- | --- |
| 7 OS on a VM you created | C | C if they created a VM; the row is about a VM, so C. If a learner argues PaaS has no such VM, accept C for IaaS only and "not your job" for PaaS. | P (you do not have that VM) |
| 8 OS on a platform you deploy code to | Not the IaaS case; provider if they are not running that OS. Mark P for PaaS. | P | P |
| 9 Application code you wrote | C | C | Not your code; if the row is "code you wrote," it does not apply to SaaS. Mark C / C / n/a |
| 10 Email application's code | P | P | P |

Be strict on rows 1–6 and 11–12. Be generous on 7–10 if the reason is right: "I patch an OS only when I am the one running that OS."

### Part B

1. Public
2. Private
3. Hybrid
4. Public
5. Hybrid
6. Private (a dedicated government cloud is still private use; do not require the name of a sovereign region)
7. Public
8. Hybrid

### Part C

Tour stops are Home, Subscriptions, Resource groups, Microsoft Entra ID. No resource is created, so there is nothing to delete.
