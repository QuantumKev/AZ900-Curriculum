# Session 10 Quiz — Managing and Deploying Azure Resources

**Name:** <span class="blank"></span>  **Session:** <span class="blank"></span>

**Time:** 15 minutes · **Items:** 12 · **Target:** 80%

Answer every question. For *select all that apply*, mark every correct option. For
matching questions, write the matching term next to each numeral. For yes/no sets,
write yes or no next to each numeral. Your instructor reviews every answer in class
immediately afterward.

---

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

**10.** A team must host a web application with automatic scaling and no operating system to manage, and deploy it continuously from a Git repository. Which service fits best?

- A. Azure Virtual Machines
- B. Azure App Service
- C. Azure Data Box
- D. Azure Cloud Shell

**11.** Which combination correctly matches the requirement to the tool?

- A. Restrict deployments to approved regions → resource lock; prevent accidental deletion → Azure Policy
- B. Restrict deployments to approved regions → Azure Policy; prevent accidental deletion → resource lock
- C. Both requirements → Azure RBAC
- D. Both requirements → Azure Arc

**12.** You apply a ReadOnly lock to a resource group, then try to deploy a new resource into it from an ARM template. What happens?

- A. The deployment succeeds, because template deployments bypass locks
- B. The deployment fails, because a ReadOnly lock prevents updates to the locked scope until the lock is removed
- C. The deployment succeeds but the new resource is created without tags
- D. The deployment succeeds only if run from Cloud Shell

<!-- pagebreak -->

## Answer sheet

| # | Your answer | # | Your answer |
| --- | --- | --- | --- |
| 1 |  | 7 |  |
| 2 |  | 8 |  |
| 3 |  | 9 |  |
| 4 |  | 10 |  |
| 5 |  | 11 |  |
| 6 |  | 12 |  |

**Score:** ____ / 12

**Objectives to review:** <span class="blank blank-wide"></span>
