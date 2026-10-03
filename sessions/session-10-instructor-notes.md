# Session 10 instructor notes — Managing and Deploying Azure Resources

**Objectives:** 3.3.1, 3.3.2, 3.3.3, 3.3.4, 3.3.5
**Slides:** [session-10-slides.md](session-10-slides.md)
**Lab:** [../labs/session-10-lab.md](../labs/session-10-lab.md)
**Quiz:** [../quizzes/session-10-quiz.md](../quizzes/session-10-quiz.md)
**Warm-up:** Session 10 set, weighted to hosting choices, RBAC, Policy, locks, and manageability (of vs in)
**Domain minutes:** Domain 1 — 5, Domain 2 — 5, Domain 3 — 110

## Run of show

| Min | Block | Leave it when |
| --- | --- | --- |
| 0–10 | Warm-up | Management of vs management in is still clean. It is the door into "four front ends, one control plane" |
| 10–35 | Portal, Cloud Shell, CLI, PowerShell | They can match a task to a tool without ranking CLI above PowerShell |
| 35–60 | ARM, templates, infrastructure as code | Declarative and idempotent are sayable. Bicep is labeled context |
| 60–75 | Arc | "Projects into management" is the sentence. Not "moves the VM to Azure" |
| 75–105 | Lab | The same task identified in two tools minimum. A template's resources section was pointed at |
| 105–120 | Quiz | |

## Teach A

Portal: discover and one-off. Cloud Shell: browser, authenticated, CLI or PowerShell, backed by storage. CLI: `az`, cross-platform. PowerShell: `Az` cmdlets.

Say functional equivalence out loud. The exam item writes a task and offers both tools as competent answers, then distinguishes them by syntax or by scenario (already in the portal, already in a script, no local install because Cloud Shell).

Copilot: context, not quizzed. One sentence.

## Teach B

Draw four boxes (portal, CLI, PowerShell, REST) with arrows into one box labeled Resource Manager, then arrows out to resource providers. That picture is 3.3.5.

Infrastructure as code: files, review, repeat. Declarative vs imperative: "a network with these two subnets" versus "click add subnet, click add subnet." Idempotent: the second run converges; it is not a second copy by accident.

ARM template: JSON, parameters, resources. Bicep, gap G8: current authoring practice, compiles toward ARM, not in the skills measured, not in the quiz. If a learner wants Bicep, point them at the module after the exam objective is secure.

## Teach C

Arc: on-premises or another cloud, projected into Azure so Policy, inventory, and monitoring can apply. Hybrid and multicloud from Sessions 1 and 5 finally get a management answer. Do not demo server onboarding. It will not finish in 15 minutes and it needs a machine outside Azure.

## Lab

[Session 10 lab](../labs/session-10-lab.md). The task is "show the resource group," not "build a landing zone." Three ways is the objective. If PowerShell startup in Cloud Shell is slow, do portal and CLI live and have them read the PowerShell cmdlet on the slide.

Exporting a template from an existing resource is enough. Redeploying into a second group is optional and must be deleted. The no-cost path reads a sample template and still finds `parameters` and `resources`.

Guided project for anyone who wants the longer CLI practice: [Manage Azure resources with Cloud Shell and the Azure CLI](https://learn.microsoft.com/en-us/training/modules/guided-project-manage-resources-cloud-shell-cli/).

## If you are short on time

Cut the redeploy. Cut Arc onboarding stories. Keep the control-plane picture and the Bicep boundary.

## Sources

[Managing and deploying module](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/) · [Portal](https://learn.microsoft.com/en-us/azure/azure-portal/azure-portal-overview) · [Cloud Shell](https://learn.microsoft.com/en-us/azure/cloud-shell/overview) · [CLI](https://learn.microsoft.com/en-us/cli/azure/what-is-azure-cli) · [PowerShell](https://learn.microsoft.com/en-us/powershell/azure/what-is-azure-powershell) · [Arc](https://learn.microsoft.com/en-us/azure/azure-arc/overview) · [Infrastructure as code](https://learn.microsoft.com/en-us/devops/deliver/what-is-infrastructure-as-code) · [ARM](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview) · [Templates](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/overview)
