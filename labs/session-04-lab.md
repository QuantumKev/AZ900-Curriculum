# Session 4 lab — Compare VM and App Service, glimpse a template

**Time:** 30 minutes
**Objectives practiced:** 2.2.1–2.2.4, 1.1.7, 3.3.5
**You need:** an Azure subscription to open the wizards, or the no-cost path.

Do not finish a virtual machine deployment unless the instructor explicitly says this subscription is meant to be billed. The learning is in the questions the wizard asks.

---

## Part A — Two create flows (20 minutes)

Use one resource group name in your head, `az900-s04-lab`, but you should not need to create it if you stop before deploy.

1. Portal search **Virtual machines**. Start **Create**.
2. Write down every decision the first two pages force. At a minimum, look for: resource group, region, image (operating system), size, administrator account, disks, and networking (virtual network, subnet, public IP).
3. Go as far as **Review + create**. Do not select Create.
4. If the review page offers a link to download a template for automation, download it. You will not edit it. Note that it is a template Azure Resource Manager can deploy. Close the wizard. Discard.
5. Portal search **App Services** (or **App Service**). Start a web app create.
6. Write down the decisions this wizard treats as central: runtime stack or code vs container, operating-system family if asked, region, and an App Service plan (the pricing tier of the platform).
7. Go to **Review + create**. Do not select Create. Discard the wizard.

Then answer, in pairs:

- Which wizard asked you to patch an operating system you chose? 
- Which wizard asked you for a platform plan instead of a virtual-machine size?
- Which one is IaaS, and which one is PaaS?

## Part B — Serverless, only if time remains (10 minutes)

The official project is [Build a simple website endpoint with Azure Functions](https://learn.microsoft.com/en-us/training/modules/guided-project-build-basic-website-endpoint-with-functions/).

In class, do not start it cold. Either the instructor runs the slice they rehearsed, or you start the project after class and stop when a function URL answers.

If you deploy anything, it goes in `az900-s04-lab`, tagged `course=az900` and `session=s04`, and the group is deleted before you leave.

### No-cost path

Part A on the instructor's screen. You fill the same two lists from what you see. Nobody selects Create.

For the template, the instructor opens a sample ARM template from the docs
([ARM templates overview](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/overview))
and you only need to see that it declares resources. You do not author one.

<div class="pagebreak"></div>

## Instructor key

VM flow is IaaS: image, size, OS administration, disks, network.

App Service flow is PaaS: runtime and a plan; you are not patching that OS.

The downloaded file is an ARM template (objective 3.3.5, first exposure). Do not grade JSON.

Nothing should remain deployed. If a learner selected Create, delete `az900-s04-lab` before the quiz.
