# Session 4 Quiz — Azure Compute

**Name:** <span class="blank"></span>  **Session:** <span class="blank"></span>

**Time:** 15 minutes · **Items:** 12 · **Target:** 80%

Answer every question. For *select all that apply*, mark every correct option. For
matching questions, write the matching term next to each numeral. For yes/no sets,
write yes or no next to each numeral. Your instructor reviews every answer in class
immediately afterward.

---

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

**10.** Which requirement most strongly suggests a serverless approach rather than a virtual machine?

- A. A line-of-business application that must run 24 hours a day at steady load
- B. Short tasks triggered by messages that arrive unpredictably, finishing in seconds
- C. A legacy application that needs a specific OS build and custom drivers
- D. A standardized desktop image for remote workers

**11.** Which scenario is the clearest example of IaaS?

- A. Subscribing to a hosted email service
- B. Deploying virtual machines you patch and configure yourself
- C. Using a managed analytics service with built-in tooling
- D. Using an event-triggered function service

**12.** You want to delete a temporary development environment consisting of a VM, its disk, its network interface, and a public IP address, all created together. What is the cleanest way to remove everything?

- A. Delete the virtual machine; the dependent resources are always removed with it
- B. Delete the resource group that contains them
- C. Apply a ReadOnly lock, then delete the subscription
- D. Move the resources to a second resource group, then delete the original

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
