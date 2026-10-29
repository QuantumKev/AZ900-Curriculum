<!-- Copyright (c) 2026 Kevin Robinson. All Rights Reserved. -->

# Session 10 instructor guide — Describe features and tools for managing and deploying Azure resources

**Speak from this file.** It follows the current Microsoft Learn module in Microsoft's order. It is a consulting script for beginners, not a second copy of the documentation.

**Module:** [Describe features and tools for managing and deploying Azure resources](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/)

**Checked against the live module:** 29 October 2026

**Units, in the order you will teach them:**

1. [Introduction](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/1-introduction)
2. [Describe tools for interacting with Azure](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/2-describe-interacting-azure)
3. [Describe the purpose of Azure Arc](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/3-describe-purpose-of-azure-arc)
4. [Describe Azure Resource Manager and Azure ARM templates](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/4-describe-azure-resource-manager-azure-arm-templates)
5. Module assessment (students take this on Learn after class; do not project it)
6. [Summary](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/6-summary)

**Microsoft's learning objectives, from the introduction and summary units:**

- Describe the Azure portal
- Describe Azure Cloud Shell, including Azure CLI and Azure PowerShell
- Describe the purpose of Azure Arc
- Describe Azure Resource Manager (ARM), ARM templates, and Bicep
- Describe how Copilot in Azure can assist with operations tasks while humans remain responsible for validation and approval

The module landing page still shortens the fourth objective to ARM and ARM templates. The introduction and summary units name Bicep, and the summary names Copilot. Teach both short blocks. Do not quiz them. The skills measured for this course still score the portal, Cloud Shell, CLI, PowerShell, Arc, infrastructure as code, and ARM templates. Bicep and Copilot are module content, not separate scored bullets, and they are not on today's quiz.

**Course objective IDs** (local to this curriculum, not printed by Microsoft): 3.3.1 through 3.3.5.

**How to use the concept blocks.** Say the instructor talk track. Use the card when a student asks why the organization would care, or when you need the exam wording. Do not read the card headings aloud.

**What this file does not replace.** The course still has `sessions/session-10-instructor-notes.md`, slides, `labs/session-10-lab.md`, and `quizzes/session-10-quiz.md`. This guide is the speak-from lecture. The clock below keeps the lab and the 15-minute scored quiz.

**Slide order.** The deck still shows Arc after the templates. This script follows the live module: tools, then Arc, then Resource Manager. When you reach Arc, jump to slide 7, then come back to slides 4 through 6 for Resource Manager.

Anything the current module does not say is in **Supplemental instructor context** at the end. Do not promote that material into the main script.

---

## The client for the whole lesson

Contoso Health is the same fictional organization as the networking and identity sessions.

- Nurses, billing clerks, and a small operations team
- A production resource group that people have deleted by accident, and a policy that already limits regions
- Development, test, and production environments that must come out the same
- Headquarters servers that are not in Azure
- A Kubernetes cluster running in another public cloud
- SQL Server and data services that also live outside Azure
- An operations lead who lives in the portal, and a second person who would rather type a command
- A director who wants the next environment created from a file the team can review, not from someone's memory of which buttons they clicked

At each decision, ask the room: **"What would we recommend to Contoso, and why?"**

---

## Two-hour lesson plan

| Time | Block | Leave this block when |
| --- | --- | --- |
| 0:00–0:08 | Warm-up | Locks and Policy are still two different answers. The room can name more than one way into Azure |
| 0:08–0:38 | Tools: portal, Cloud Shell, PowerShell, CLI, a short Copilot note | CLI and PowerShell are equivalent jobs with different syntax. Cloud Shell is not a local install |
| 0:38–0:52 | Azure Arc | "Projects into Azure management" is the sentence. Nobody says the server moved to Azure |
| 0:52–1:15 | Resource Manager, infrastructure as code, ARM templates, a short Bicep note | Every tool goes through Resource Manager. A template describes the end state |
| 1:15–1:45 | Lab | [Session 10 lab](../../labs/session-10-lab.md). The same task in two tools minimum, and a template's `parameters` and `resources` sections |
| 1:45–2:00 | Scored quiz | [Session 10 quiz](../../quizzes/session-10-quiz.md). Twelve items. Review only what the room missed |

**If you are behind at 0:30.** Keep the portal, Cloud Shell, and the one sentence that CLI and PowerShell are functionally equivalent. Give Copilot the validation sentence and stop.

**If you are behind at 0:48.** Keep "project non-Azure resources into Resource Manager" and the four resource types on the quiz: servers, Kubernetes clusters, SQL Server, Azure data services. Skip custom locations and the preview virtual-machine line.

**If you are behind at 1:10.** Keep the control-plane picture, declarative versus manual, and repeatable results. Give Bicep one sentence. Cut nested templates and deployment scripts.

---

## Mention once, then move on

These ideas are in the module. They are useful. They are too implementation-specific for a long stop on AZ-900.

- Portal accessibility options, beyond "the portal can be configured for the person using it"
- Custom locations as an abstraction on Arc-enabled Kubernetes clusters
- Virtual machines outside Azure as an Arc resource type, which the unit marks as preview
- Deployment scripts inside a template, beyond "a template can call a script before or after the resources exist"
- Nested templates and Bicep modules, beyond the word "reusable"
- Agent-like Copilot workflows, beyond "a person still approves the change"
- Installing the CLI or PowerShell on a laptop. Cloud Shell is enough for the lab

---

# 0. Warm-up

## What Microsoft wants students to know

Nothing new. This block retrieves governance and the ways into Azure, so the tools have something to sit on.

## Set the scene

**[0:00]** Read these prompts. They are free recall. Do not project the answers. Accept the substance, not the wording. If two people miss the same prompt, re-teach that one fact in a minute and move on.

The prompts are the Session 10 set in `quizzes/warm-ups.md`. If you are short, ask only the first, the fourth, and the fifth.

## Instructor Talk Track

Before we talk about how Contoso operates Azure, I need the last two controls to still be separate in the room.

One team keeps deleting a production resource group. Another keeps deploying virtual machines in regions the clinic did not approve. Which tool solves which problem? A resource lock stops the accidental deletion. Azure Policy stops the unapproved region. They are not interchangeable.

What is an Azure Policy initiative? A group of related policy definitions, assigned and tracked together toward one compliance goal.

Name three ways to host an application. A web app on App Service, a container, and a virtual machine are the three this course uses.

You are an Owner, and a ReadOnly lock is on the resource. Can you change it? Not until someone removes the lock. A lock applies even to an Owner.

Name three ways to interact with Azure. Portal, Azure CLI, Azure PowerShell, Cloud Shell, a REST API, or an SDK. Any three.

Give three tag names worth standardizing. Environment, Owner, and CostCenter are enough, if the person can say what question each one answers.

Good. Hold the lock and the three ways in. A lock decides whether a change is allowed to land. Today we decide which door the operations team uses to ask for that change, and how they ask for a whole environment at once instead of clicking it from memory.

## Whiteboard / Visual

Leave a blank line under the warm-up. You will fill it with four doors and one desk: **Portal. Cloud Shell. CLI. PowerShell. All of them talk to Resource Manager.**

## Ask the Class

- If Policy already blocks the unapproved region, why would Contoso still put a lock on the production group?
- Is Cloud Shell a fifth Azure service that holds patient records, or a way to send a command?

## Exam Trap

Students will answer a "how do I stop a delete" question with a deployment tool, or a "how do I create the same environment again" question with a lock. A lock blocks a change. A template describes a change. They are different jobs.

## Transition

Contoso's operations lead wants to see the estate, and the second person wants to type. Both of them are still talking to the same Azure. The first unit is the doors.

---

# 1. Introduction

## What Microsoft wants students to know

The module introduces features and tools for managing and deploying Azure resources: the portal, command-line and scripting tools, and services that manage on-premises and multicloud environments from inside Azure.

## Set the scene

**[0:08]** Contoso can already create a resource. They cannot yet say, as a team, how that request should be made the second time, or how a server that is not in Azure gets the same management.

## Instructor Talk Track

Last session we decided what Contoso is allowed to deploy, and what they are not allowed to delete. Today the question changes. Who clicks, who types, and what happens when the thing they need to manage is not an Azure resource at all.

The module gives you four outcomes. Describe the portal. Describe Cloud Shell, including the CLI and PowerShell. Describe why Azure Arc exists. Describe Resource Manager, ARM templates, and Bicep. The summary adds one more: Copilot in Azure can help an operator, and a person still validates and approves.

If I were consulting with this clinic, I would not start by picking a favorite shell. I would ask who is going to do the work next month when the person who remembers the clicks is on leave.

## Whiteboard / Visual

```text
Contoso's problem today

See it and click it            -> portal
Type it, with no install       -> Cloud Shell
Repeat a command you can read  -> CLI or PowerShell
Govern a server that is not
  in Azure                     -> Arc
Describe the whole environment
  in a file                    -> ARM template
```

## Ask the Class

- Which of those five lines is a person looking at a screen, and which is a file the team can review?
- Which line is about a machine that does not live in Azure?

## Exam Trap

The exam describes a situation and asks which tool fits. It does not ask you to rank the portal as worse than the command line. A one-off look is a fair reason to open the portal. A repeated environment is a fair reason to use a template.

## Transition

Start with the door everyone already recognizes.

---

# 2. Describe tools for interacting with Azure

## What Microsoft wants students to know

Azure gives you more than one tool for the same management job: the portal, Azure PowerShell, and the Azure CLI. Cloud Shell runs PowerShell and the CLI in the browser, already authenticated, with no local install. Copilot in Azure can help an operator explore, understand options, and draft commands. A person still validates recommendations, confirms permissions, and reviews changes before they land in production.

## Set the scene

**[0:12]** The operations lead is in the portal. The second person wants a command they can run again next week. Neither of them should get a different Azure because they used a different door.

---

### Azure portal

**Microsoft Learn concept.** The Azure portal is a web-based, unified console and an alternative to command-line tools. You manage the subscription through a graphical interface. You can build, manage, and monitor from simple web apps to complex deployments, create custom dashboards, and configure accessibility options. The portal is designed for resiliency and continuous availability. It maintains a presence in every Azure datacenter, so it can survive an individual datacenter failure and stay close to users. It updates continuously and does not require downtime for maintenance.

**Plain English.** The portal is the website where Contoso looks at Azure and clicks.

**Consultant scenario.** A billing clerk needs to see what the clinic already has, once, and does not write scripts. What would we recommend to Contoso, and why? The Azure portal. Not a local install, and not a claim that the portal lives in only one datacenter.

**Instructor talk track.**

The Azure portal is a web-based, unified console. It is the alternative to the command line. With it, Contoso manages the subscription through a graphical interface.

What the unit says they can do there. Build, manage, and monitor, from a simple web app to a complicated deployment. Make a custom dashboard so the operations lead sees the clinic's resources in one view. Configure accessibility options so the console works for the person using it.

Here is the reliability sentence, because the exam likes to trap it. The portal keeps a presence in every Azure datacenter. That makes it resilient to an individual datacenter failure, and it avoids a long trip across the network by being close to the user. It updates continuously. Maintenance of the portal does not mean the portal goes down.

Say that, then stop. We are not touring blades.

**Analogy.** The portal is the front desk. You can see the building and ask for something. The front desk is staffed in every building, so one building being closed does not close the desk everywhere.

**Why an organization would use it.** Someone needs to see, create, or check a resource without writing a command, and they want a dashboard of their own.

**Problem it solves.** Azure has a graphical console, and that console is not a single datacenter that can take the whole portal down.

**Common confusion.** The portal is not a desktop application you install, and it does not require PowerShell on the laptop. It is also not "the only door." The command-line tools do the same management work with different syntax.

**AZ-900 exam clue.** "Web-based console," "dashboards," "resilient to a single datacenter failure," or "no downtime for portal maintenance" points at the Azure portal. If the stem says the portal exists in only one datacenter, that statement is false.

**Check for understanding.** A classmate says a portal outage in one datacenter takes the Azure portal down for every customer. What does the unit say instead?

**Transition.** The second person does not want to install a shell just to list a resource group. They are already in the browser.

---

### Azure Cloud Shell

**Microsoft Learn concept.** Azure Cloud Shell is a browser-based shell for creating, configuring, and managing Azure resources. It supports Azure PowerShell and the Azure CLI, which uses Bash. You open it from the portal. It needs no local installation or configuration. It is authenticated to your Azure credentials, so it already knows who you are and what you may do. You choose the shell you know.

**Plain English.** Cloud Shell is a command line in the browser, already signed in as you.

**Consultant scenario.** The second operator is on a clinic PC that they are not allowed to install software on. What would we recommend to Contoso, and why? Azure Cloud Shell. Not a local terminal they have to set up, and not a remote desktop into a virtual machine.

**Instructor talk track.**

Azure Cloud Shell is a browser-based shell. From it, you create, configure, and manage Azure resources. It supports both Azure PowerShell and the Azure CLI. The unit describes the CLI here as the Bash shell.

Open it from the portal, from the Cloud Shell icon. Three features are the exam sentence.

First, it is in the browser. No local installation and no local configuration.

Second, it is already authenticated to your Azure credentials. When you sign in, it knows who you are and what permissions you have. You do not do a separate "log the shell into Azure" dance.

Third, you pick the shell you know. PowerShell or the CLI.

Cloud Shell is not a place patient records live. It is a door. The storage it uses behind the scenes is in the supplemental note, and you do not need it for the quiz.

**Analogy.** Cloud Shell is a phone at the front desk that is already logged in as you. You did not bring your own phone, and you do not introduce yourself again.

**Why an organization would use it.** The person needs a command line and cannot, or does not want to, install one.

**Problem it solves.** Command-line management without a workstation setup, and without a second sign-in.

**Common confusion.** Cloud Shell versus the Azure CLI. The CLI is a tool. Cloud Shell is one place that tool can run. The CLI can also be installed on Windows, Linux, and Mac. Cloud Shell is the browser place. Cloud Shell is also not a remote desktop session into a virtual machine.

**AZ-900 exam clue.** "Browser-based," "no local install," "already authenticated," "PowerShell or the CLI" is Cloud Shell. If the stem says you must install it on the laptop, that is not Cloud Shell.

**Check for understanding.** Name the two shells Cloud Shell can run, and say what you do not have to install.

**Transition.** Those two shells are real products. They are not nicknames for the same command.

---

### Azure PowerShell

**Microsoft Learn concept.** Azure PowerShell is a shell in which developers, DevOps, and IT professionals run commands called cmdlets. Cmdlets call the Azure REST API to perform management tasks. They can run alone for a one-off change, or be combined to set up, tear down, and maintain resources, or to deploy an infrastructure of many resources from imperative code. Putting the commands in a script makes the process repeatable and automatable. You can run Azure PowerShell in Cloud Shell, or install it on Windows, Linux, and Mac.

**Plain English.** PowerShell is the command style that uses cmdlets. A script of those cmdlets can be run again.

**Consultant scenario.** The second operator already writes PowerShell for the on-premises servers. What would we recommend to Contoso, and why? Azure PowerShell, in Cloud Shell or installed locally. Not a requirement that they learn a second language for the same job.

**Instructor talk track.**

Azure PowerShell is a shell. The commands are called cmdlets. Those cmdlets call the Azure REST API. That is the management task actually happening. The shell is how you ask.

A cmdlet can be one change. Or you combine them for the routine setup, teardown, and maintenance of one resource or of several that belong together. You can also deploy a whole infrastructure, dozens or hundreds of resources, from imperative code. "Imperative" here means the script says the steps. We will contrast that with a template in a few minutes. Do not camp on the word yet.

The sentence that matters for the business: capturing the commands in a script makes the process repeatable and automatable. Next month, the person on leave is not the only one who knows which buttons to press.

You can use it in Cloud Shell. You can also install and configure it on Windows, Linux, and Mac. Say that, because a common wrong answer is "PowerShell is Windows only."

**Analogy.** A cmdlet is one instruction to the building. A script is the checklist of instructions, so the next person does not invent the checklist again.

**Why an organization would use it.** The team already thinks in PowerShell, and they want one-off commands or a script they can run again.

**Problem it solves.** Management tasks through commands that call Azure, including work that is too repetitive to click.

**Common confusion.** PowerShell versus the portal. The portal is the graphical console. PowerShell is commands. Both can manage Azure. PowerShell is also not "the only tool that can write." The CLI can write too.

**AZ-900 exam clue.** "Cmdlets," "script," "Windows, Linux, and Mac," or "runs in Cloud Shell" points at Azure PowerShell. Do not choose it because the stem says the CLI cannot run there. The CLI runs there too.

**Check for understanding.** Can the clinic install Azure PowerShell on a Mac, or only use it in the browser?

**Transition.** The other command style does the same work. The words on the line change.

---

### Azure CLI

**Microsoft Learn concept.** The Azure CLI is functionally equivalent to Azure PowerShell. The primary difference is syntax. PowerShell uses PowerShell commands. The CLI uses Bash commands. The CLI handles discrete tasks or orchestrates complex operations through code, and it is installable on Windows, Linux, and Mac, and available in Cloud Shell. Because the capabilities and the access are so similar, the choice is mainly which language you know.

**Plain English.** The CLI does the same management job as PowerShell. You type Bash-style commands instead of cmdlets.

**Consultant scenario.** A contractor knows Bash and does not know PowerShell. What would we recommend to Contoso, and why? The Azure CLI. Not a claim that the contractor can only read, or that they must switch to PowerShell to be allowed to change something.

**Instructor talk track.**

Say this sentence slowly. The Azure CLI is functionally equivalent to Azure PowerShell. The primary difference is the syntax of the commands.

PowerShell uses PowerShell commands. The CLI uses Bash commands. Same benefits: a single task, or a larger operation expressed in code. Same places to run it: installed on Windows, Linux, and Mac, or inside Cloud Shell.

The unit's advice is the exam's advice. It comes down to which language you already know. We do not tell Contoso that one of these is the grown-up tool.

What would we recommend to Contoso, and why? Whichever of the two the person can read next month. If the team is split, Cloud Shell lets each person pick.

**Analogy.** Two order pads at the same front desk. One pad is printed in PowerShell, one in Bash. The kitchen receives the same kind of order.

**Why an organization would use it.** The team knows Bash, or they want a script that is not a PowerShell script, for the same Azure management tasks.

**Problem it solves.** Command-line management for people whose syntax is not PowerShell, without giving them a weaker tool.

**Common confusion.** "Functionally equivalent" does not mean the commands look alike. `az group show` and `Get-AzResourceGroup` are not the same text. They are the same kind of request. Also, the CLI is not Linux-only, and it does run in Cloud Shell.

**AZ-900 exam clue.** If the stem asks for the real difference, the answer is syntax, not capability. Reject "CLI can only read," "CLI is Linux-only," and "only PowerShell runs in Cloud Shell."

**Check for understanding.** In one sentence, what is the same about the CLI and PowerShell, and what is different?

**Transition.** There is one more assistant in this unit. It drafts. It does not get the last word.

---

### Copilot in Azure

**Microsoft Learn concept.** Copilot in Azure is an AI assistant that helps administrators work faster with contextual guidance in natural language. Some workflows can be agent-like and help coordinate multi-step tasks. At a fundamentals level, treat it as an operational assistant. You still validate recommendations, confirm permissions, and review deployment changes before applying them in production. The summary says Copilot can assist with discovery, guidance, and multistep operational workflows while administrators stay in control of the final decision.

**Plain English.** Copilot can explain a blade, draft a command, or help walk a task. A person still checks it and approves it.

**Consultant scenario.** The operations lead asks Copilot how to list the production resource group, and Copilot drafts a command. What would we recommend to Contoso, and why? Use the draft as a starting point. Read it, confirm the account is allowed to run it, and do not apply a production change because an assistant suggested it.

**Instructor talk track.**

Many teams use Copilot in Azure to move faster on ordinary operations: exploring a service, understanding a configuration option, and drafting a command or a script. Depending on the environment, some of that help can coordinate more than one step. The unit calls those workflows agent-like.

Here is the line you want them to leave with. Copilot is an operational assistant. You validate the recommendation. You confirm the permissions. You review the deployment change before it is applied in production. The summary says the same thing in the learning objective: humans remain responsible for validation and approval.

This block is in the module. It is not a separate skills-measured bullet, and it is not on today's quiz. One minute is the right length.

**Analogy.** Copilot is a colleague who drafts the order. The operations lead still signs it.

**Why an organization would use it.** People spend less time hunting for the right command or the right blade, and a person still owns the change.

**Problem it solves.** Slow discovery and first-draft commands, without handing production decisions to the assistant.

**Common confusion.** A drafted command is not an approved change. Copilot is also not a substitute for Resource Manager, Policy, or a lock.

**AZ-900 exam clue.** You are unlikely to see Copilot as the keyed product for a skills-measured item. If a scenario says "an assistant recommended this deployment," the scored habit is still: a person validates, checks permission, and reviews before production.

**Check for understanding.** Copilot drafts a command that deletes a resource group. What does the unit say the administrator still has to do?

**Transition.** All of those doors manage Azure resources. Contoso also has servers that are not in Azure. That is the next unit, and it is a different product.

## Whiteboard / Visual

```text
Same management job, different door

Portal          look, click, dashboard
Cloud Shell     browser, already signed in
PowerShell      cmdlets, scriptable
Azure CLI       Bash-style commands, scriptable
Copilot         drafts and explains; a person approves

PowerShell and CLI: equivalent job, different syntax
Both run in Cloud Shell and on Windows, Linux, and Mac
```

## Ask the Class

- The clinic PC cannot have software installed. Which door still gives you a command line?
- Why would we refuse to call the CLI "the read-only one"?
- What would we recommend to Contoso when the person who knows the clicks is on leave?

## Exam Trap

The exam pairs these tools. Equivalent does not mean identical syntax. Browser-based does not mean installed. A presence in every datacenter does not mean the portal is a desktop app.

## Transition

The tools so far assume the resource is already an Azure resource. Headquarters is not Azure, and neither is the other cloud. Azure Arc is how those still show up in the same management story.

---

# 3. Describe the purpose of Azure Arc

## What Microsoft wants students to know

Hybrid and multicloud estates get complicated because Azure's management tools apply to Azure resources. Azure Arc works with Azure Resource Manager to extend Azure compliance and monitoring to those other environments. It projects existing non-Azure resources into Resource Manager so you can manage them together. Outside Azure, the unit's current list is servers, Kubernetes clusters, Azure data services, SQL Server, and virtual machines in preview.

## Set the scene

**[0:38]** Contoso has Azure, a datacenter at headquarters, and a Kubernetes cluster in another public cloud. The director does not want three policy stories.

---

### Azure Arc

**Microsoft Learn concept.** Azure Arc works with Azure Resource Manager to extend compliance and monitoring to hybrid and multicloud configurations. It is a centralized, unified way to manage the whole environment by projecting existing non-Azure resources into Resource Manager; to manage multicloud and hybrid virtual machines, Kubernetes clusters, and databases as if they are running in Azure; to use familiar Azure services and management wherever the resources live; to keep traditional operations while introducing DevOps practices; and to configure custom locations on Arc-enabled Kubernetes clusters. The practical scenario in the unit is an organization that runs workloads in Azure, an on-premises datacenter, and another public cloud, and applies consistent governance, policy, and inventory from Azure. Resource types the unit says Arc can manage outside Azure: servers, Kubernetes clusters, Azure data services, SQL Server, and virtual machines (preview).

**Plain English.** Arc makes an outside machine or cluster show up in Azure management. The machine does not move.

**Consultant scenario.** Contoso must apply the same policy and inventory tracking to headquarters servers and to a Kubernetes cluster in another cloud, from Azure. What would we recommend to Contoso, and why? Azure Arc. Not Azure Migrate, which is about moving workloads, and not a claim that those servers now run in an Azure datacenter.

**Instructor talk track.**

Managing hybrid and multicloud gets complicated fast. Azure already has tools to provision, configure, and monitor Azure resources. The question the unit asks is: what about the on-premises resources, and what about the resources in another public cloud?

Azure Arc works with Azure Resource Manager. It extends Azure compliance and monitoring to those configurations. It simplifies governance and management by giving you one management platform for multicloud and on-premises, not a different tool for each building.

The verb is project. You project existing non-Azure resources into Azure Resource Manager. You then manage them together. The unit says you can manage multicloud and hybrid virtual machines, Kubernetes clusters, and databases as if they are running in Azure. "As if" is doing the work in that sentence. They are not relocated.

The practical picture in the unit is exactly Contoso's picture. Workloads in Azure, in their own datacenter, and in another public cloud. Operations applies consistent governance, policy, and inventory from Azure, instead of a disconnected tool per environment.

What the unit says you can manage outside Azure, today. Servers. Kubernetes clusters. Azure data services. SQL Server. Virtual machines, marked preview. The quiz uses the first four. Say "virtual machines, in preview" once so a careful student is not surprised, then do not design an onboarding.

Custom locations are an abstraction on top of Arc-enabled Kubernetes clusters and cluster extensions. Name them once. Do not draw the abstraction.

What would we recommend to Contoso, and why? Arc for the headquarters servers and the other cloud's cluster, so policy and inventory have one place to land. We are not migrating those machines in this session.

**Analogy.** Arc is a badge that lets the headquarters server and the other cloud's cluster appear on Azure's management board. The server stays in its own building. The badge is not a moving truck.

**Why an organization would use it.** They already run machines, clusters, or databases outside Azure and they want Azure governance and inventory on those resources too.

**Problem it solves.** Disconnected management tools for hybrid and multicloud estates.

**Common confusion.** Arc versus Migrate. Arc projects a resource into management. Migrate is about moving a workload. Arc versus "the VM now runs in Azure." It does not. Also, an Azure subscription is not one of the resource types on the list. You do not "Arc a subscription."

**AZ-900 exam clue.** "On-premises or another cloud," "project into Resource Manager," "policy and inventory from Azure," "servers, Kubernetes, SQL Server, data services" is Azure Arc. If the stem says the server was moved into an Azure region, that is a migration story, not Arc.

**Check for understanding.** Contoso enables Arc on a headquarters server. In which building is that server still running?

## Whiteboard / Visual

```text
Azure Resource Manager
   ^            ^              ^
   |            |              |
 Azure VM    HQ server     other cloud
             (Arc)         Kubernetes (Arc)

Arc projects. It does not move the server.
```

## Ask the Class

- What would we recommend to Contoso for a SQL Server that must stay at headquarters and still show up for inventory in Azure?
- Why is Azure Migrate the wrong answer to that sentence?
- Which of these is not an Arc resource type: a server, a Kubernetes cluster, an Azure subscription?

## Exam Trap

The exam describes where the resource lives and what the team wants to apply from Azure. Location outside Azure, plus governance or inventory from Azure, is Arc. "Move the workload into Azure" is not this unit.

## Transition

We have doors, and we have a way for outside resources to appear in Azure management. Every one of those requests still has to land somewhere. That somewhere is Azure Resource Manager.

---

# 4. Describe Azure Resource Manager and ARM templates

## What Microsoft wants students to know

Azure Resource Manager is the deployment and management service for Azure. Any request from any tool, API, or SDK is received by Resource Manager, authenticated and authorized, then sent to the Azure service that does the work. You get consistent results across tools because they share that API. Templates are declarative JSON that describe what you want. Infrastructure as code is managing that infrastructure through code and templates instead of manual configuration, starting with the CLI or PowerShell and growing into ARM templates and Bicep.

## Set the scene

**[0:52]** Development, test, and production must come out the same, in the right order, even when a different person runs the deployment. Clicking from memory will not survive the next leave.

---

### Azure Resource Manager

**Microsoft Learn concept.** Azure Resource Manager is the deployment and management service for Azure. It is the management layer that creates, updates, and deletes resources in your Azure account. Whenever you do anything with Azure resources, Resource Manager is involved. A request from any Azure tool, API, or SDK is received by Resource Manager, which authenticates and authorizes it, then sends it to the Azure service that takes the action. Results and capabilities stay consistent across tools because all requests go through the same API. Benefits named in the unit: manage infrastructure through declarative templates rather than scripts; deploy, manage, and monitor the resources of a solution as a group; redeploy through the development life cycle and get a consistent state; define dependencies so resources deploy in the correct order; apply access control because RBAC is built into the management platform; apply tags to organize the subscription and support cost reporting.

**Plain English.** Resource Manager is the desk every door talks to. It checks who you are and whether you may do the thing, then it asks the service to do it.

**Consultant scenario.** Someone says the CLI bypasses the portal's rules. What would we recommend to Contoso, and why? Trust Resource Manager as the common layer. A portal click and a CLI command are both requests. Both are authenticated and authorized there. A lock or a policy does not disappear because the person used a shell.

**Instructor talk track.**

Azure Resource Manager is the deployment and management service for Azure. It is the layer that lets you create, update, and delete resources. Anytime you do anything with an Azure resource, Resource Manager is involved. That includes the portal, PowerShell, the CLI, an API, and an SDK.

Walk the request. A person sends it from a tool. Resource Manager receives it. Resource Manager authenticates and authorizes it. Then Resource Manager sends it to the Azure service, and that service does the work. You see the same capabilities in every tool because every tool is handled through the same API.

Put the picture on the board now. Four doors, one desk, then the services.

The unit's benefit list is worth saying as benefits, not as a configuration lab.

You can manage infrastructure through declarative templates rather than scripts. A Resource Manager template is a JSON file that defines what you want to deploy.

You can deploy, manage, and monitor the resources of a solution as a group, instead of handling each one by itself.

You can redeploy through the development life cycle and expect a consistent state.

You can define dependencies so the resources come out in the correct order.

You can apply access control to services because RBAC is part of this platform. That is the callback to Session 7. We are not re-teaching roles.

You can apply tags, so the subscription stays organized and cost reporting has something to group on. That is the callback to cost and governance.

**Analogy.** Resource Manager is the one service desk behind every door. The door changes. The desk does not. The desk checks your badge before it calls the department that actually does the work.

**Why an organization would use it.** They want every tool to land on the same management layer, with the same authentication, authorization, and results.

**Problem it solves.** Four tools that would otherwise be four different Azures.

**Common confusion.** Resource Manager is not only for templates. A portal click goes through it too. It is not a monitoring product for application telemetry. That is a later session. And the CLI does not get a private side door around it.

**AZ-900 exam clue.** "Every request," "authenticates and authorizes," "same result from portal, CLI, and PowerShell" is Resource Manager. Reject any option that says only the portal talks to it, or that it is only used when you deploy a template.

**Check for understanding.** A contractor uses the CLI and an operator uses the portal to ask for the same kind of change. Which layer sees both requests?

**Transition.** The desk can take a clicked request or a typed request. Contoso's director wants the request written down as the outcome, not as a list of clicks.

---

### Infrastructure as code and ARM templates

**Microsoft Learn concept.** Infrastructure as code means managing infrastructure through code and templates instead of manual configuration. At this level it can start with the Azure CLI or Azure PowerShell and grow into repeatable deployments with ARM templates and Bicep. An ARM template describes the desired resources in declarative JSON. Azure validates the template before deployment, then orchestrates creation in the right order and in parallel when it can. The team defines the end state. Resource Manager handles the execution. Templates can also call PowerShell or Bash deployment scripts when setup is needed before or after the resources exist. Benefits the unit lists: declarative syntax, repeatable results, orchestration, modularity through reusable and nested templates, and extensibility through deployment scripts.

**Plain English.** You describe the environment you want in a file. Azure checks the file, then builds that environment in the right order. Running the same file again is how development, test, and production stay aligned.

**Consultant scenario.** Contoso needs the same environment in development, test, and production, with dependencies created in the right order, and no one reconstructing it from screenshots. What would we recommend to Contoso, and why? An ARM template. Not a screenshot of the portal, and not a chat log of one-off commands.

**Instructor talk track.**

Infrastructure as code means you manage the infrastructure through code and templates instead of manual configuration. The unit is honest about the starting point. This can begin with the CLI or with PowerShell. A script you can run again is already a step away from clicking. It grows into repeatable environment deployments when you use ARM templates and Bicep.

An ARM template describes the Azure resources you want in declarative JSON. Declarative means the file says what the end state is. It does not say "click here, then click here."

Azure validates that file before it deploys. Then it orchestrates the creation, in the right order, and in parallel when the resources do not have to wait on each other. The team defines the end state. Resource Manager does the execution.

The benefits, in the unit's words. Declarative syntax: what to deploy, not the step-by-step commands. Repeatable results: the same template across environments. Orchestration: dependency order and parallel deployment. Modularity: split the template into reusable pieces and nested templates. Extensibility: a deployment script can run before or after, when something still needs a command.

Say "repeatable" and "consistent state" out loud. Those are the module's words. The second run is there to reach the same end state, not to accidentally build a second copy of the clinic. If you want one extra word for that idea, idempotent belongs to the Bicep paragraph in a moment. Do not make the room memorize two slogans.

What would we recommend to Contoso, and why? An ARM template for the environment that has to exist three times. Parameters so the name and the region can change. The resources section so the team can see what will be created before anyone deploys it. You will point at those two sections in the lab. You will not write a template from a blank page.

**Analogy.** A template is the recipe card for the environment. The recipe says what the finished clinic setup contains. It does not say "now wander the kitchen and see what you feel like adding."

**Why an organization would use it.** The same environment has to be created more than once, reviewed before it runs, and produced in a consistent state.

**Problem it solves.** Environments that drift because each one was clicked by a different person.

**Common confusion.** A template is not application source code. It does not, by itself, make the resources cheaper. A lock does not deploy an environment. A chat log of CLI commands is not the same as a validated template, even though the CLI can be a starting point for infrastructure as code.

**AZ-900 exam clue.** "Same environment in dev, test, and production," "correct dependency order," "define what, not the click path" is an ARM template. "Managing infrastructure through code and templates instead of manual configuration" is the definition of infrastructure as code.

**Check for understanding.** Why does the unit say Azure validates the template before it creates anything?

**Transition.** The module offers a second way to write that same declaration. It is shorter. It is still ARM underneath.

---

### Bicep

**Microsoft Learn concept.** Bicep is a declarative language for deploying Azure resources through ARM. Compared with JSON templates, it is generally simpler and more concise. The unit lists: support for current Azure resource types and API versions, simpler syntax, repeatable deployments because Bicep files are idempotent, orchestration by Resource Manager, and modularity through Bicep modules.

**Plain English.** Bicep is a cleaner language that deploys through the same Resource Manager. The idea is still "describe the end state."

**Consultant scenario.** A student asks if Contoso should stop using JSON and rewrite everything in Bicep before the exam. What would we recommend? Be able to describe Bicep. Do not rewrite anything today. Today's quiz asks about ARM templates and infrastructure as code.

**Instructor talk track.**

Bicep is a declarative language for deploying Azure resources through ARM. Compared with a JSON template, it is simpler and shorter to read.

The benefits the unit names. It supports current resource types and API versions. The syntax is easier than the equivalent JSON. The deployments are repeatable, and the unit uses the word idempotent: you can run the file across the life cycle and get a consistent result. Resource Manager still orchestrates the dependencies. You can reuse logic by organizing the deployment into Bicep modules.

That is the whole block. The introduction and the summary both say you should be able to describe Bicep. The skills measured for this course still name ARM and ARM templates, not Bicep as its own bullet. Bicep is not a question on today's quiz. If someone answers a template question by saying Bicep, tell them the idea is right and the objective's name is the ARM template. Then move on.

**Analogy.** Bicep is the same recipe written in plainer handwriting. The kitchen is still Resource Manager.

**Why an organization would use it.** The team wants a shorter declarative file and still wants ARM to deploy it.

**Problem it solves.** JSON templates that are correct and unpleasant to read.

**Common confusion.** Bicep does not replace Resource Manager. It deploys through it. It is not a separate cloud.

**AZ-900 exam clue.** If a stem asks you to describe the language that is simpler than JSON and deploys through ARM, that is Bicep, and you now know it because the module teaches it. If the stem asks for the JSON file that defines what to deploy, that is an ARM template. Do not swap them.

**Check for understanding.** Does a Bicep file skip Resource Manager?

## Whiteboard / Visual

```text
Portal / CLI / PowerShell / API / SDK
                 |
                 v
        Azure Resource Manager
        authenticate, authorize
                 |
                 v
            Azure service

Template = declarative JSON of the end state
Bicep    = a shorter declarative language, still through ARM
```

## Ask the Class

- What would we recommend to Contoso for an environment that must be rebuilt the same way in three places?
- A ReadOnly lock is on the production group, and someone deploys a template into it. Does the template get a special pass?
- Why does the CLI not "bypass" a policy you set in the portal?

## Exam Trap

Students treat Resource Manager as "the template engine" and miss that every tool uses it. Students treat a template as a cost tool. Students treat Bicep as a different control plane. One desk. The file describes the end state. The lock from last session still applies to a deployment.

## Transition

You can close the module in four lines, then they will do the small version with their hands.

---

# 5. Close the lecture

## Instructor Talk Track

**[1:12]** Four lines, then the lab.

The portal is the web console, present in every datacenter, with dashboards. Cloud Shell is the browser shell, already signed in, and it runs PowerShell or the CLI. Those two are the same job in different syntax, and both can be installed on Windows, Linux, and Mac.

Azure Arc projects non-Azure resources into Resource Manager so governance and inventory can apply. It does not move the server.

Every request goes through Resource Manager. An ARM template declares the end state in JSON. Bicep is the shorter declarative language for that same path, and a person still approves anything Copilot drafts.

## Ask the Class

What would we recommend to Contoso, in one minute, for the operator who clicks, the operator who types, the headquarters server, and the environment that must exist three times?

Take one student's four-part answer. Correct only a wrong product. Then start the lab.

---

# Lab

**[1:15]** [Session 10 lab](../../labs/session-10-lab.md). Thirty minutes. The task is a resource group, not a landing zone.

Part A is the same group three ways if the room is moving: portal, `az group show`, and `Get-AzResourceGroup`. If PowerShell is slow to start in Cloud Shell, do the portal and the CLI live, and have them read the PowerShell cmdlet on the slide. Two tools is the minimum. Ask which box in the control-plane picture all of them called. The answer is Resource Manager.

Part B is reading a template. They find `parameters` and `resources` and they say why the file is infrastructure as code, using "declarative" or "repeatable" correctly. Exporting a template is enough. Redeploying into a second group is optional and must be deleted before they leave. The no-cost path uses the public sample template only.

Do not demo Arc server onboarding. It will not finish, and it needs a machine outside Azure.

---

# Quiz

**[1:45]** [Session 10 quiz](../../quizzes/session-10-quiz.md). Twelve items, fifteen minutes. It is already written. Do not replace it with questions you invent in the room. Review only the items several people missed.

Items 11 and 12 are carry-forward. If the room swaps Policy and locks, stop and repair that pair before you dismiss them. A template does not bypass a ReadOnly lock.

If someone names Bicep on the infrastructure-as-code or template items, accept the idea in discussion and tell them the keyed name on this quiz is the ARM template.

After class, each student can complete the module on Learn, including the module assessment. Do not project Microsoft's assessment items. You teach Session 11 later today, so do not assign a long homework block between the two sessions. The practice assessment for next week's exam session is assigned at the end of Session 11.

## If you remember only 10 things

1. The Azure portal is a web-based console for building, managing, and monitoring, with custom dashboards. It has a presence in every Azure datacenter and updates without portal downtime.
2. Azure Cloud Shell is browser-based, needs no local install, is already authenticated, and runs Azure PowerShell or the Azure CLI.
3. Azure PowerShell uses cmdlets. The Azure CLI uses Bash-style commands. They are functionally equivalent. Both run in Cloud Shell and install on Windows, Linux, and Mac.
4. Copilot in Azure can explore, explain, and draft. A person validates, confirms permissions, and reviews production changes. It is module content, not a scored bullet on today's quiz.
5. Azure Arc projects non-Azure resources into Resource Manager so you can govern and inventory them from Azure. It does not move the resource into Azure.
6. Outside Azure, Arc's list includes servers, Kubernetes clusters, Azure data services, SQL Server, and virtual machines in preview. A subscription is not an Arc resource type.
7. Azure Resource Manager receives every management request, authenticates and authorizes it, and sends it to the service. Portal, CLI, PowerShell, APIs, and SDKs all go through it.
8. Infrastructure as code means managing infrastructure through code and templates instead of manual configuration. It can start with the CLI or PowerShell.
9. An ARM template is declarative JSON. Azure validates it, then creates resources in dependency order and in parallel when it can. Benefits include repeatable results and modularity. A template does not guarantee a lower price.
10. Bicep is a simpler declarative language that deploys through ARM. Describe it. Do not quiz it today. A ReadOnly lock still blocks a deployment until the lock is removed.

## Rapid-fire instructor questions

Ask these out loud if the lab finishes early. Do not grade them.

1. Where does the Azure portal keep a presence?
2. What do you not have to install to use Cloud Shell?
3. What is the real difference between the CLI and PowerShell?
4. Name four resource types Arc can manage outside Azure.
5. Does Arc move a headquarters server into an Azure region?
6. What does Resource Manager do before it passes a request to a service?
7. What does "declarative" mean for a template?
8. Why is a screenshot of the portal a weak way to build dev, test, and production?
9. What does a person still do after Copilot drafts a command?
10. A ReadOnly lock is on the group. Will an ARM deployment into that group succeed?

## Service recognition table

| Business requirement | Azure concept / service | Why | Common wrong answer |
| --- | --- | --- | --- |
| See and manage resources in a browser, with a dashboard | Azure portal | Web-based unified console; present in every datacenter | A desktop app, or a portal that lives in one datacenter |
| A command line on a PC where you cannot install software | Azure Cloud Shell | Browser-based, already authenticated, PowerShell or CLI | A local install, or a remote desktop into a VM |
| The team already writes PowerShell | Azure PowerShell | Cmdlets that call Azure; scripts are repeatable | "PowerShell is Windows only" |
| The team already writes Bash | Azure CLI | Functionally equivalent to PowerShell; different syntax | "The CLI can only read" |
| Draft a command or explain a blade, then a person approves it | Copilot in Azure | Operational assistant; humans validate | Letting the draft run in production unreviewed |
| Policy and inventory for servers and clusters that are not in Azure | Azure Arc | Projects non-Azure resources into Resource Manager | Azure Migrate, or "the server moved" |
| Every tool gets the same management layer and the same authorization | Azure Resource Manager | Receives, authenticates, authorizes, then calls the service | "Only the portal goes through it" |
| The same environment, three times, in the right order | ARM template | Declarative JSON of the end state; validated, then orchestrated | Screenshots, or a lock |
| A shorter file for that same declaration | Bicep | Declarative language that deploys through ARM | A different control plane |
| Stop an accidental delete | Resource lock | Blocks the change regardless of role or tool | A template, or Arc |
| Allow only approved regions | Azure Policy | Governs configuration | A lock, which does not choose regions |

---

# Supplemental instructor context

Do not teach this section as part of the module. Use it only when a student asks, or when the lab needs a sentence the unit does not spell out. Say that you are stepping outside the unit, then come back.

**Cloud Shell storage.** The tools unit says Cloud Shell needs no local install and is authenticated. It does not, in the pages checked today, spend the unit on the storage account behind the shell. If a student hits a first-run prompt to create storage, that prompt is real and it can cost a small amount. For this class, prefer the no-cost path if that prompt appears. Do not turn the lab into a storage lesson.

**Idempotent.** The Bicep section of the unit uses "idempotent" for repeatable life-cycle deployments. The template section says "repeatable results" and the Resource Manager section says "consistent state." Teach those as the same idea in plain speech: the next run converges on the end state. Do not open a second lecture on failure modes.

**Azure Policy, locks, and RBAC.** They already had Sessions 7 and 9. This module mentions RBAC and tags as Resource Manager benefits. It does not restate locks. The quiz carry-forward does. The one sentence you may need in the quiz review: a ReadOnly lock blocks updates at that scope no matter which door sent the request, including a template, until the lock is removed.

**Virtual machines in preview.** The Arc unit lists them. The quiz's select-all item does not offer them as a choice. Mention the preview line once so the list on the page and the list on the quiz do not look like a contradiction.

---

## Sources

Checked 29 October 2026. The talk track follows these units. It does not reproduce them.

- [Module: Describe features and tools for managing and deploying Azure resources](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/)
- [Introduction](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/1-introduction)
- [Describe tools for interacting with Azure](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/2-describe-interacting-azure)
- [Describe the purpose of Azure Arc](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/3-describe-purpose-of-azure-arc)
- [Describe Azure Resource Manager and Azure ARM templates](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/4-describe-azure-resource-manager-azure-arm-templates)
- [Summary](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/6-summary)
