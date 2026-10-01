# Session 10 slides — Managing and Deploying Azure Resources

Each `##` heading is one slide. Notes: [session-10-instructor-notes.md](session-10-instructor-notes.md).

## 1. How you manage Azure

Session 10. The portal, the shells, the control plane under them, and how a non-Azure machine shows up in the same place.

## 2. Four ways in

**Azure portal.** The website. Best when you are learning a service or doing a one-off task.

**Azure Cloud Shell.** A shell in the browser, already signed in, with the CLI and PowerShell available. It keeps a storage account so your files persist.

**Azure CLI.** Cross-platform commands, `az`. Scripts and Cloud Shell.

**Azure PowerShell.** Cmdlets, the `Az` module. Same jobs as the CLI, different syntax.

CLI and PowerShell are equivalent in power for this exam. Neither is "the advanced one." You pick the syntax your team already writes.

## 3. Copilot in Azure is context

The portal can offer a copilot that helps you along. It is module content, not a bulleted objective as of July 20, 2026. We do not quiz it.

## 4. Azure Resource Manager

Azure Resource Manager (ARM) is the control plane.

The portal, Cloud Shell, CLI, PowerShell, and REST all call Resource Manager. Resource Manager talks to the service that creates the virtual machine or the storage account.

You do not bypass it by picking a different tool. You send the same kind of request through a different front door.

## 5. Infrastructure as code

Infrastructure as code means the environment is described in files you can review, repeat, and run again.

**Declarative:** you say what should exist. You do not write every click.

**Idempotent:** running it again brings the environment to the described state, instead of blindly creating a second copy of everything.

That is the practice. The template format the objective names is next.

## 6. ARM templates

An ARM template is a JSON description of resources and of parameters you fill in at deploy time.

You already downloaded one in Session 4 from a virtual-machine review page. Deploying that file calls Resource Manager.

**Bicep** is a language that produces ARM deployments and is what many teams author now. Bicep is not named in the skills measured. Hear the name. The examinable objects are infrastructure as code, Resource Manager, and ARM templates.

## 7. Azure Arc

Arc projects resources that are not in Azure — on-premises servers, or resources in another cloud — into Azure management.

Once projected, you can apply Policy, inventory, and monitoring more consistently. It is how multicloud and hybrid estates stay under one set of tools.

Arc does not turn a foreign virtual machine into an Azure-region virtual machine. It attaches management.

## 8. Lab and quiz

One task, three ways: portal, CLI, PowerShell.

Then export a template from a resource you already have, find the parameters and the resources sections, and see that it could deploy into another resource group.

No account: trace the three commands the instructor used, and read a sample template.

Assignment: [Describe features and tools for managing and deploying Azure resources](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/).
