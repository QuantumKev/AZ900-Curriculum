# Session 4 Quiz — Azure Compute

**Time:** 15 minutes · **Items:** 12 · **Composition:** 9 new, 3 carry-forward (S1–S3)
**Objectives:** 2.2.1, 2.2.2, 2.2.3, 2.2.4 (plus 1.1.7 second pass)
**Carry-forward objectives:** 1.1.7, 1.3.1, 2.1.4
**Target:** 80%

Scenario-selection level begins here. Distractors are adjacent compute services.

---

## Questions

**1.** A team needs to run multiple instances of a lightweight application on a single host, starting and stopping instances quickly, without managing a separate operating system for each instance. Which compute option fits best?

- A. Virtual machines
- B. Containers
- C. Azure Virtual Desktop
- D. Availability sets

**2.** Which statement correctly distinguishes Azure Container Instances from Azure Kubernetes Service?

- A. Container Instances orchestrates the lifecycle of a fleet of containers; AKS runs a single container
- B. Container Instances is the fastest, simplest way to run a container in Azure; AKS is a container orchestration service for managing fleets
- C. Container Instances runs only Windows containers; AKS runs only Linux containers
- D. Container Instances is IaaS; AKS is SaaS

**3.** A retailer wants identical, load-balanced virtual machines that increase in number automatically during traffic spikes and decrease afterward. Which option should they use?

- A. An availability set
- B. A virtual machine scale set
- C. Azure Virtual Desktop
- D. A single larger virtual machine

**4.** What do update domains and fault domains belong to?

- A. Availability zones
- B. Region pairs
- C. Availability sets
- D. Virtual network subnets

**5.** A company needs to give 200 distributed contractors access to a standardized Windows desktop and a fixed set of applications, managed centrally, with data staying in Azure rather than on personal laptops. Which service fits best?

- A. Azure Virtual Desktop
- B. Virtual machine scale sets
- C. Azure App Service
- D. Azure Container Apps

**6.** Which of these must you select or configure when you create an Azure virtual machine? (Select all that apply.)

- A. Size (family, vCPU count, and RAM)
- B. Storage disks
- C. Virtual network and network interface
- D. A Log Analytics query
- E. An Azure Policy initiative

**7.** In the VM name `D2s_v5`, what does the `D` indicate?

- A. The number of data disks attached
- B. The VM family, in this case general purpose
- C. The datacenter the VM runs in
- D. That the VM is deallocated

**8.** A development team wants to host a web application and a REST API in the language of their choice, with automatic scaling, built-in load balancing, and deployment from a Git repository — without managing operating systems. Which service fits best?

- A. Azure Virtual Machines
- B. Azure App Service
- C. Azure Virtual Desktop
- D. Azure Data Box

**9.** Which statement about Azure Functions is correct?

- A. Functions must run continuously to be able to receive events
- B. Functions are stateful by default, and Durable Functions makes them stateless
- C. An event triggers the function, Azure runs the code, then deallocates resources, and you are charged for the CPU time used while it runs
- D. Functions can only be triggered by an HTTP request

**10.** *(Carry-forward)* Which requirement most strongly suggests a serverless approach rather than a virtual machine?

- A. A line-of-business application that must run 24 hours a day at steady load
- B. Short tasks triggered by messages that arrive unpredictably, finishing in seconds
- C. A legacy application that needs a specific OS build and custom drivers
- D. A standardized desktop image for remote workers

**11.** *(Carry-forward)* Which scenario is the clearest example of IaaS?

- A. Subscribing to a hosted email service
- B. Deploying virtual machines you patch and configure yourself
- C. Using a managed analytics service with built-in tooling
- D. Using an event-triggered function service

**12.** *(Carry-forward)* You want to delete a temporary development environment consisting of a VM, its disk, its network interface, and a public IP address, all created together. What is the cleanest way to remove everything?

- A. Delete the virtual machine; the dependent resources are always removed with it
- B. Delete the resource group that contains them
- C. Apply a ReadOnly lock, then delete the subscription
- D. Move the resources to a second resource group, then delete the original

---

## Answer key

| Q | Answer | Objective | Why | Source |
| --- | --- | --- | --- | --- |
| 1 | B | 2.2.1 | Containers are lightweight, share the host operating system, and are designed to be created, scaled out, and stopped dynamically. VMs each carry their own OS to manage. | [Azure containers](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/5-containers) |
| 2 | B | 2.2.1 | Container Instances is the fastest and simplest way to run a container without managing VMs; AKS is the orchestration service that manages container lifecycle at fleet scale. Container Apps sits between them, adding built-in load balancing and scaling. | [Azure containers](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/5-containers) |
| 3 | B | 2.2.2 | Scale sets create and manage groups of identical, load-balanced VMs and scale out or in on demand or schedule. Availability sets improve resiliency but do not scale instance counts. | [Azure virtual machines](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/2-virtual-machines) · [VM Scale Sets](https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/overview) |
| 4 | C | 2.2.2 | Availability sets group VMs by update domain (rebooted together during planned maintenance) and fault domain (shared power or network failure point). | [Azure virtual machines](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/2-virtual-machines) |
| 5 | A | 2.2.2 | Azure Virtual Desktop is the desktop and application virtualization service; it centralizes delivery, integrates with Microsoft Entra ID, keeps data in Azure-hosted sessions, and supports single- and multi-session Windows. | [Azure virtual desktop](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/4-virtual-desktop) |
| 6 | A, B, C | 2.2.3 | VM provisioning requires size, storage disks, and networking (virtual network, NIC, optionally a public IP). D and E are unrelated management and governance features. | [Azure virtual machines](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/2-virtual-machines) |
| 7 | B | 2.2.2 | The base name carries the family (purpose), then vCPU count, then feature and hardware-generation indicators — `D` general purpose, `2` vCPUs, `s` premium SSD support, `v5` hardware generation. | [Azure virtual machines](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/2-virtual-machines) |
| 8 | B | 2.2.4 | App Service hosts web apps, API apps, WebJobs, and mobile back ends in multiple languages with automatic scaling, built-in load balancing, and deployment from GitHub, Azure DevOps, or any Git repo. | [Application hosting options](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/7-describe-application-hosting-options) |
| 9 | C | 2.2.1, 1.1.7 | Functions are event-driven and serverless: the event wakes the function, Azure deallocates resources when it finishes, and charging is based on CPU time used. Functions are stateless by default; Durable Functions adds state. Triggers include timers and messages from other services, not only HTTP. | [Azure functions](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/6-functions) |
| 10 | B | 1.1.7 (carry-forward) | Serverless fits short, event-triggered work with variable arrival rates, because nothing needs to stay provisioned between events. A, C, and D all imply continuously running or OS-controlled infrastructure. | [Azure functions](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/6-functions) |
| 11 | B | 1.3.1 (carry-forward) | IaaS means renting infrastructure and managing the OS and installed software yourself. A is SaaS; C and D are PaaS-style managed services. | [IaaS](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/2-describe-infrastructure-service) |
| 12 | B | 2.1.4 (carry-forward) | Deleting the resource group deletes everything in it, which is exactly why temporary environments are grouped. Deleting a VM does not reliably remove its disk, NIC, and public IP — the cost-management module names those leftovers as a real source of waste. | [Azure management infrastructure](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/6-describe-azure-management-infrastructure) · [Cost factors](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/2-describe-factors-affect-costs-azure) |

**Instructor note on item 12:** this item deliberately links architecture to cost. It
previews Session 8's maintenance cost factor and is a good place to reinforce the one
resource group per session lab convention.
