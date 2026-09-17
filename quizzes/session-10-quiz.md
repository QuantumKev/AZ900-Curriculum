# Session 10 Quiz — Managing and Deploying Azure Resources

**Time:** 15 minutes · **Items:** 12 · **Composition:** 9 new, 3 carry-forward (S4–S9)
**Objectives:** 3.3.1, 3.3.2, 3.3.3, 3.3.4, 3.3.5
**Carry-forward objectives:** 2.2.4, 3.2.2, 3.2.3
**Target:** 80%

---

## Questions

**1.** Which statement about the Azure portal is correct?

- A. It is a downloadable desktop application for Windows only
- B. It is a web-based console for building, managing, and monitoring Azure resources, with support for custom dashboards
- C. It requires Azure PowerShell to be installed locally
- D. It is available in a single datacenter, so portal outages affect all customers globally

**2.** What is Azure Cloud Shell?

- A. A browser-based shell, authenticated to your Azure credentials, that supports both Azure PowerShell and the Azure CLI
- B. A local terminal emulator you install on Windows, macOS, or Linux
- C. A remote desktop session into an Azure virtual machine
- D. A cost analysis view in the Azure portal

**3.** What is the real difference between the Azure CLI and Azure PowerShell?

- A. The CLI can only read; PowerShell can write
- B. They are functionally equivalent, differing mainly in command syntax
- C. The CLI works only on Linux; PowerShell works only on Windows
- D. PowerShell runs in Cloud Shell; the CLI does not

**4.** An operations team must apply consistent Azure Policy assignments and inventory tracking to servers in their own datacenter and Kubernetes clusters running in another public cloud, managing everything from Azure. Which service enables this?

- A. Azure Migrate
- B. Azure Arc
- C. Azure Virtual Desktop
- D. Azure Monitor

**5.** Which resource types can Azure Arc currently manage outside of Azure? (Select all that apply.)

- A. Servers
- B. Kubernetes clusters
- C. SQL Server
- D. Azure data services
- E. Azure subscriptions

**6.** What does infrastructure as code mean?

- A. Writing application source code that runs on cloud infrastructure
- B. Managing and provisioning infrastructure through code and templates instead of manual configuration
- C. Storing infrastructure diagrams in a source control repository
- D. Running scripted health checks against deployed resources

**7.** Which statement about Azure Resource Manager is correct?

- A. Only the Azure portal communicates with Resource Manager; CLI and PowerShell bypass it
- B. Every request from the portal, CLI, PowerShell, SDKs, and APIs goes through Resource Manager, which authenticates and authorizes it before passing it to the service
- C. Resource Manager is a monitoring service for application telemetry
- D. Resource Manager is only used for template deployments

**8.** Which are benefits of using ARM templates? (Select all that apply.)

- A. Declarative syntax that defines what to deploy rather than how to deploy it
- B. Repeatable results when the same template is reused across environments
- C. Automatic handling of resource dependency order and parallel deployment
- D. Guaranteed lower cost for the deployed resources
- E. Modularity through reusable and nested templates

**9.** A team deploys the same environment to development, test, and production and needs the resources created in the correct dependency order every time, with no manual steps. Which approach fits best?

- A. Screenshot the portal configuration and repeat it manually
- B. Deploy from an ARM template
- C. Run ad hoc CLI commands from a chat log
- D. Use a resource lock on the production resource group

**10.** *(Carry-forward)* A team must host a web application with automatic scaling and no operating system to manage, and deploy it continuously from a Git repository. Which service fits best?

- A. Azure Virtual Machines
- B. Azure App Service
- C. Azure Data Box
- D. Azure Cloud Shell

**11.** *(Carry-forward)* Which combination correctly matches the requirement to the tool?

- A. Restrict deployments to approved regions → resource lock; prevent accidental deletion → Azure Policy
- B. Restrict deployments to approved regions → Azure Policy; prevent accidental deletion → resource lock
- C. Both requirements → Azure RBAC
- D. Both requirements → Azure Arc

**12.** *(Carry-forward)* You apply a ReadOnly lock to a resource group, then try to deploy a new resource into it from an ARM template. What happens?

- A. The deployment succeeds, because template deployments bypass locks
- B. The deployment fails, because a ReadOnly lock prevents updates to the locked scope until the lock is removed
- C. The deployment succeeds but the new resource is created without tags
- D. The deployment succeeds only if run from Cloud Shell

---

## Answer key

| Q | Answer | Objective | Why | Source |
| --- | --- | --- | --- | --- |
| 1 | B | 3.3.1 | The portal is a web-based unified console with custom dashboards and accessibility options, and it maintains a presence in every Azure datacenter so it is resilient to individual datacenter failures. | [Tools for interacting with Azure](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/2-describe-interacting-azure) |
| 2 | A | 3.3.2 | Cloud Shell is browser-based with no local installation, is already authenticated to your credentials and permissions, and supports both Azure PowerShell and the Azure CLI. | [Tools for interacting with Azure](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/2-describe-interacting-azure) |
| 3 | B | 3.3.2 | Both call the same Azure APIs with equivalent capability; the CLI uses Bash-style commands and Azure PowerShell uses cmdlets. Both install on Windows, Linux, and macOS, and both run in Cloud Shell. | [Tools for interacting with Azure](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/2-describe-interacting-azure) |
| 4 | B | 3.3.3 | Azure Arc works with Azure Resource Manager to project non-Azure resources into Azure, delivering consistent governance and management across hybrid and multicloud estates. Azure Migrate moves workloads; it does not govern them in place. | [Purpose of Azure Arc](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/3-describe-purpose-of-azure-arc) |
| 5 | A, B, C, D | 3.3.3 | Arc currently manages servers, Kubernetes clusters, Azure data services, SQL Server, and virtual machines (in preview) outside Azure. Subscriptions are an Azure construct, not an Arc-managed resource type. | [Purpose of Azure Arc](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/3-describe-purpose-of-azure-arc) |
| 6 | B | 3.3.4 | Infrastructure as code means managing infrastructure through code and templates rather than manual configuration, starting with CLI or PowerShell and growing into repeatable template-based deployments. | [Azure Resource Manager and ARM templates](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/4-describe-azure-resource-manager-azure-arm-templates) |
| 7 | B | 3.3.5 | Resource Manager is the deployment and management layer for Azure. Every tool, API, and SDK request passes through it and is authenticated and authorized there, which is why results are consistent across interfaces. | [Azure Resource Manager and ARM templates](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/4-describe-azure-resource-manager-azure-arm-templates) |
| 8 | A, B, C, E | 3.3.5 | Declarative syntax, repeatable results, orchestration of dependency order and parallel deployment, modularity, and extensibility are the stated benefits. Templates do not change resource pricing. | [Azure Resource Manager and ARM templates](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/4-describe-azure-resource-manager-azure-arm-templates) |
| 9 | B | 3.3.4, 3.3.5 | An ARM template describes the desired end state; Azure validates it, then creates resources in the correct order and in parallel where possible. That is exactly the repeatability requirement. | [Azure Resource Manager and ARM templates](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/4-describe-azure-resource-manager-azure-arm-templates) |
| 10 | B | 2.2.4 (carry-forward) | App Service provides managed hosting with automatic scaling, high availability, and automated deployment from GitHub, Azure DevOps, or any Git repo, with no OS to manage. | [Application hosting options](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/7-describe-application-hosting-options) |
| 11 | B | 3.2.2, 3.2.3 (carry-forward) | Policy governs which configurations are permitted, including allowed locations; locks prevent deletion or modification. Option A reverses them. | [Purpose of Azure Policy](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/3-describe-purpose-azure-policy) · [Purpose of resource locks](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/4-describe-purpose-resource-locks) |
| 12 | B | 3.2.3 (carry-forward) | ReadOnly blocks updates to the locked scope for all authorized users, and locks apply regardless of how the request arrives or which role the caller holds. The lock must be removed first. | [Purpose of resource locks](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/4-describe-purpose-resource-locks) |

**Note on Bicep and Copilot in Azure:** the official module also covers Bicep as a
declarative language for ARM deployments, and introduces Copilot in Azure among the tools
for interacting with Azure. Neither is named in the current skills measured, so both are
demonstrated in Session 10 and excluded from this bank. If a learner names Bicep in item
6 or 9, accept it in discussion and note that ARM templates are what the objective asks
about.
