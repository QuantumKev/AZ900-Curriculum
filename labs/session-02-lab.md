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

Rehearse before class. The current portal opens **Create Function App (Flex Consumption)**. That title is the serverless plan. Stay on the **Basics** tab. Do not tour the other tabs. Stop without selecting Create. Delete anything you accidentally create before learners leave.

Say this while the Basics page is up: "The extra boxes are settings. They are not a virtual machine. We are not patching an operating system, and we are not choosing disks or a network."

| Field on Basics | What to do | What to say |
| --- | --- | --- |
| Subscription | Leave the class subscription | "Whose bill this would land on. Not today's idea." |
| Resource group | **Create new**, name it `az900-s02-demo` | "A folder, so we can delete this in one step. The Storage tab stays empty until this name exists." |
| Function App name | Any unique name | "A name. The `.azurewebsites.net` ending is an address the platform gives it. You did not create a server." |
| Region | The region you will use all course | "You pick a region. You do not buy a datacenter. Regions are Session 3." |
| Runtime stack and Version | Pick one language, any current version | "This is the platform-as-a-service point. You chose a language. Microsoft patches the operating system under it." |
| Instance size | **2048 MB** if it is listed. That is the documented default | "This is memory for one short-lived instance: 512, 2048, or 4096 MB. It is not a virtual-machine size. You still have no operating system, no disks, and no network to manage. There is compute under here. You do not run it." |
| Zone redundancy | Leave **off** | "That checkbox is high availability, copies in separate zones. Session 3. Turning it on also keeps instances warm, so you pay while idle. Off means the app can sit at zero until an event runs it." |

Do not open these tabs in class. One sentence each if a learner asks:

- **Storage.** The platform needs a storage account for its own keys and code package. That is Session 6. The red message "Select a resource group first" means the Basics resource group was not actually created. Click **Create new** and name it. Then leave diagnostics on **Configure later**. "Configure now" builds a monitoring workspace from Session 11.
- **Azure OpenAI.** Not an exam objective.
- **Networking.** Session 5.
- **Monitoring.** Session 11.
- **Durable Functions.** Not on this exam.
- **Deployment.** How code gets uploaded. Skip.
- **Authentication.** Session 7.
- **Tags.** Session 8.

The five facts, pointed at this screen:

1. It is a Function App. The runtime is a language, not an operating-system image you patch.
2. The plan name is Flex Consumption. That is the consumption-style plan.
3. An event would trigger the code (HTTP, timer, queue). You are not creating the function today, so say the trigger rather than clicking into it.
4. With zone redundancy off, you pay around the run. The instance size is memory per run, not a server left powered on.
5. Servers still exist. Instance size is the evidence. Serverless is not a fourth model next to public, private, and hybrid.

Discard the wizard. If a resource was created, delete the resource group `az900-s02-demo` before the quiz.

Source for the instance sizes and the default: [Flex Consumption plan hosting](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan). Confirm the size list on the day if the dropdown has changed.
