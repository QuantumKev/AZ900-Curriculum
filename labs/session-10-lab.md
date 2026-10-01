# Session 10 lab — One task, three tools, then a template

**Time:** 30 minutes
**Objectives practiced:** 3.3.1–3.3.5
**You need:** Cloud Shell, or the no-cost trace.

The task is small on purpose: list what is in a resource group, then create an empty one if you have permission. Empty groups are free. Do not create a virtual machine.

---

## Part A — Three front doors (15 minutes)

Pick a name: `az900-s10-lab`.

**Portal.** Search **Resource groups**. Create `az900-s10-lab` in the instructed region, or open it if it exists. Tags: `course=az900`, `session=s10`.

**CLI, in Cloud Shell.**

```bash
az group show --name az900-s10-lab --output table
```

**PowerShell, in Cloud Shell.** Switch the shell to PowerShell.

```powershell
Get-AzResourceGroup -Name az900-s10-lab
```

Answer:

- Which two tools queried Azure without a mouse?
- Which box in the control-plane picture did all three call?

## Part B — Read a template (15 minutes)

If the group or any resource has an **Export template** command, open it. Otherwise open the sample the instructor has, from
[ARM template structure](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/syntax).

1. Find the `parameters` section. Name one parameter, or write "none in this file."
2. Find the `resources` section. Name one resource type written there.
3. Say why running this file is infrastructure as code, in one sentence. Use "declarative" or "repeatable" correctly.

Optional, only with instructor approval: deploy that template into a second empty group, then delete both groups.

```bash
az group delete --name az900-s10-lab --yes --no-wait
```

### No-cost path

Do not create a group. The instructor runs `az group show` and `Get-AzResourceGroup` on the projector, or you read both commands and write what each returns.

Part B uses the public sample template only.

Guided project after class: [Manage Azure resources with Cloud Shell and the Azure CLI](https://learn.microsoft.com/en-us/training/modules/guided-project-manage-resources-cloud-shell-cli/).

<div class="pagebreak"></div>

## Instructor key

All three tools call Azure Resource Manager. CLI and PowerShell are the two without the mouse. The portal is the third.

A correct Part B sentence: the file declares the resources you want, and you can run it again to reach that state. Bicep is not required and is not the exam answer.

Delete `az900-s10-lab` if it was created.
