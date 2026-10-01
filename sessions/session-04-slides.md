# Session 4 slides — Azure Compute

Each `##` heading is one slide. Notes: [session-04-instructor-notes.md](session-04-instructor-notes.md).

## 1. Azure compute

Session 4. Virtual machines, containers, functions, and where a web app should live.

## 2. Three compute types

**Virtual machine.** A full operating system you manage. Infrastructure as a service.

**Container.** A packaged app that shares the host operating system. Starts fast. You still choose how much platform you want under it.

**Function.** Your code, triggered by an event. Serverless. You do not manage the server.

## 3. Containers, three Azure services

**Azure Container Instances.** Run a container without building a cluster. The simple end.

**Azure Container Apps.** Run containers with scaling and revisions, without operating your own orchestrator.

**Azure Kubernetes Service (AKS).** A managed Kubernetes cluster, when you need that orchestrator.

You do not need to configure any of the three today. You need to know which problem each name is for.

## 4. Virtual machine options

**Azure Virtual Machines.** One machine you configure.

**Virtual Machine Scale Sets.** A group of identical machines behind a load balancer, which can grow and shrink.

**Availability sets.** Spread machines across update domains and fault domains inside one datacenter experience, so one hardware fault or one host update does not take every copy down. This is not the same thing as availability zones.

**Azure Virtual Desktop.** Desktop and app virtualization in Azure. A desktop service, not a website host.

## 5. What a virtual machine needs

You choose more than "Windows or Linux."

- Size. A family and a name such as a D-series general-purpose size. The pattern `D2s_v5` encodes family, capacity, and generation. You do not memorize the catalog.
- Disks. The operating-system disk, and any data disks.
- A virtual network and subnet.
- A network interface.
- Often a public IP address, if it must be reached from the internet.

No network, no packet. The machine is not only CPU and memory.

## 6. Application hosting

**Azure App Service.** Host web apps, API apps, WebJobs, and mobile back ends. You deploy code or a container. You do not patch the operating system. This is platform as a service.

**Containers.** When you already ship a container and want Container Apps, Container Instances, or AKS.

**Virtual machines.** When you need the operating system, a custom driver, or a lift-and-shift of an existing server.

## 7. How to choose

Need the OS or a lift-and-shift: virtual machine.

Web app or API, and you do not want the OS: App Service.

A container, and you do not want a cluster: Container Instances or Container Apps.

Kubernetes, because the team already works that way: AKS.

Event in, result out, no idle server: Functions. That is the serverless idea from Session 2, now as a service you can point at.

## 8. Lab, then quiz

Start a virtual-machine create and an App Service create. Compare the questions each one asks. Stop at Review + create unless the instructor says to deploy.

If a virtual machine wizard offers an automation template on the review step, download it and close. That file is an ARM template. We deploy from one in Session 10.

Quiz: compute, plus two items on serverless.

Assignment: [Describe Azure compute services](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/).
