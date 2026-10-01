# Session 2 lab — Service types, pricing models, serverless

**Time:** 30 minutes
**Objectives practiced:** 1.1.6, 1.1.7, 1.2.1, 1.2.2, 1.2.3, 1.2.4, 1.3.1, 1.3.2, 1.3.3, 1.3.4
**You need:** this worksheet. No Azure subscription. Part C is a demonstration.

---

## Part A — IaaS, PaaS, or SaaS (12 minutes)

Write **IaaS**, **PaaS**, or **SaaS**, and a reason of one line. Decide from who manages the operating system and whether the application is yours or the vendor's.

1. A team moves an existing server into the cloud and still needs a specific operating-system build and a custom driver.
2. The company buys Microsoft 365 email and calendars. Nobody patches an email server.
3. Developers deploy a web API. The platform patches the operating system. The team patches nothing under their code.
4. Finance subscribes to a finished expense-tracking application and only adds users.
5. A test lab needs virtual machines that match a production server image. They are created on Monday and deleted on Friday.
6. Analysts run queries in a managed analytics service. They never install a database engine.
7. Staff use a chat application the vendor operates entirely. The company manages membership.
8. An application requires a specific Linux kernel the team must control.
9. A team wants a framework that scales the number of instances for them, and they want to ship code without choosing a virtual-machine size.
10. A clinic subscribes to a browser-based scheduling product and does not host it.
11. A database administrator installs and tunes a database engine on a virtual machine.
12. A website is a set of files and code the team deploys onto a managed web platform. They do not remote in to patch Windows or Linux.

## Part B — Which pricing model? (10 minutes)

Write one of: **pay-as-you-go**, **reservation**, **savings plan**, **spot**.

1. The same virtual-machine size will run in the same region, steadily, for three years. It cannot be turned off unexpectedly.
2. A nightly job can stop halfway and restart later. The team wants the lowest compute price and will tolerate eviction.
3. Compute spend is steady, but the mix changes between virtual machines, containers, and functions. The team can commit to an hourly spend for a year, not to one virtual-machine size.
4. A new product launches next month. Nobody knows the traffic yet. The team refuses a one-year commit.
5. A development environment runs eight hours a day and changes size every week.
6. A rendering farm can lose machines at any moment. The work queue just retries the frame.

One sentence under the six: what does a reservation commit you to, that a savings plan does not?

## Part C — Serverless, on screen (8 minutes)

Watch the instructor open a Function App and stop before any long deployment. You are looking for five facts, not a working website. Write them down:

1. The thing being created is a Function App, not a virtual machine you patch.
2. The plan they point at is a consumption-style plan. You are not choosing a virtual-machine size as the main decision.
3. Code runs because something triggers it.
4. You pay around the run, not for a server that sits idle. Say this in your own words.
5. This is still built on servers. You are not managing them. Serverless is not a fourth model next to public, private, and hybrid.

### No-cost path

Parts A and B are the whole lab if no one is signed in to Azure. For Part C, follow the same five facts while the instructor talks through
[the Functions overview](https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview)
or through screenshots. Do not create a Function App on a personal subscription during class unless the instructor already rehearsed the delete.

<div class="pagebreak"></div>

## Instructor key

### Part A

1. IaaS — specific OS and a custom driver means you run the machine.
2. SaaS — finished email, vendor operates it.
3. PaaS — you deploy code; the platform owns the OS.
4. SaaS — finished application, you add users.
5. IaaS — virtual machines you image and destroy.
6. PaaS — managed engine, no OS work.
7. SaaS — vendor-operated chat.
8. IaaS — you must control the kernel.
9. PaaS — code and autoscale, no VM size as the point. If a learner says serverless, accept it only if they also say it is not a fourth service type; the sort is IaaS/PaaS/SaaS, and this row is PaaS.
10. SaaS — subscribed product, not hosted by the clinic.
11. IaaS — they install the engine.
12. PaaS — they deploy code onto a managed web platform.

### Part B

1. Reservation
2. Spot
3. Savings plan
4. Pay-as-you-go
5. Pay-as-you-go — it is not steady, and the size changes, so a reservation is a bad fit
6. Spot

A reservation commits you to a specific resource (size, and typically region) for one or three years. A savings plan commits you to an hourly compute spend, which can apply across eligible compute services.

### Part C demo script

Rehearse before class. Stop at the review screen. Delete anything you create before learners leave.

1. Portal search: **Function App**. Create.
2. Put it in a resource group named `az900-s02-demo`. Pick the region you will use all course.
3. Point at the hosting plan. Prefer the consumption-style plan the portal currently offers (Consumption or Flex Consumption). **NEEDS VERIFICATION** of the plan label on the day, because Microsoft renames hosting options. Do not pick a plan that asks you to choose a virtual-machine size; that hides the serverless point.
4. Say the five facts from Part C while that plan is on screen. Show that the trigger is the idea (HTTP, timer, queue) even if you do not create a function.
5. Discard the wizard. If a resource was created, delete the resource group `az900-s02-demo` before you start the quiz.

If the wizard has drifted past the point you rehearsed, close it and teach the five facts from the overview page. Do not debug in front of the room.
