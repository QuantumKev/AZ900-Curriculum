# Session 2 slides — Cloud Benefits, Pricing Models, and IaaS/PaaS/SaaS

Each `##` heading is one slide. Talk track is in
[session-02-instructor-notes.md](session-02-instructor-notes.md).

This is the first full teaching session if Session 1 was an introduction. The recovery
of Session 1 ideas is in the instructor notes, not on these slides.

## 1. Benefits, pricing, and service types

AZ-900, Session 2 of 12.

Today: why organizations move, how the three service types split responsibility, and which pricing offer fits a workload.

## 2. Warm-up

Six questions, out loud, from Session 1. No notes.

Shared responsibility, public vs private vs hybrid, capital expenditure vs operating expenditure.

If you cannot say it, we teach it before we move on.

## 3. High availability

High availability means the service keeps answering.

You get it by removing single points of failure: more than one copy, more than one location inside a region.

Availability zones, next week, are Azure's version of this idea. Today the exam wants the benefit, not the product.

## 4. Scalability — two directions

**Scale up (vertical):** make one resource stronger. More CPU, more memory.

**Scale out (horizontal):** add more copies of the resource, and remove copies when demand drops.

Cloud matters here because scaling out can be fast, and you can scale back in. You are not stuck with hardware you already bought.

## 5. Reliability

Reliability is the ability to recover from failures and keep working.

High availability tries to stay up. Reliability is what you still have after something breaks: another copy, another zone, a restore.

## 6. Predictability has two meanings

**Performance predictability.** Autoscaling and load balancing keep response times steady while traffic moves.

**Cost predictability.** You can see usage and forecast the bill. The pricing calculator, in Session 8, is the tool. Today, know that "predictable" is not only about speed.

## 7. Security and governance

The cloud does not make you compliant by itself. It gives you tools that make a standard repeatable.

- Deploy from a template so every resource starts from the same baseline.
- Audit resources that drift from that baseline.
- Update many resources when the standard changes.
- Patching, and who does it, still follows the shared responsibility model.

## 8. Manageability — two phrases

**Management of the cloud:** what you do to your resources. Autoscale them, deploy them from a template, replace a failed one, alert on a metric.

**Management in the cloud:** how you talk to Azure. Portal, command-line interface, PowerShell, APIs.

The exam splits these on purpose. "Portal" is management in the cloud. "Autoscale" is management of the cloud.

## 9. Sustainability is context

Microsoft Learn discusses the emissions benefit of shared, efficient datacenters.

That discussion is not a bulleted exam objective as of July 20, 2026. Hear it. We will not quiz it.

## 10. Three service types

| | IaaS | PaaS | SaaS |
| --- | --- | --- | --- |
| You manage | OS, middleware, apps, data | Apps and data | Data and access |
| Provider manages | Physical gear, virtualization, often the host fabric | That, plus OS and runtime | That, plus the application |
| You would say | "Give me a virtual machine" | "Give me a place to run my code" | "Give me the finished application" |

Infrastructure as a service. Platform as a service. Software as a service.

## 11. IaaS

You rent infrastructure. A virtual machine is the picture to keep.

You control the operating system, what is installed, and when you patch. The provider runs the physical hosts and the virtualization.

Fits lift-and-shift, custom drivers, a specific OS build, and test machines you want to mirror exactly.

## 12. PaaS

You bring the application. The provider runs the platform under it, including the operating system.

You do not patch that OS. You also do not choose an arbitrary kernel.

Fits a web API, a development framework, analytics where the engine is managed.

## 13. SaaS

You subscribe to a finished application. Email, chat, expense tracking.

You do not patch the app. You do manage users, and you still own the data you put in it.

## 14. Serverless is not a fourth type

Serverless means you do not provision or maintain servers.

An event triggers your code. Resources are allocated around that run. You pay for the execution, not for an idle server.

Azure Functions is the example. It sits next to platform as a service. It is not a fourth deployment model beside public, private, and hybrid.

There are still servers. You are not the one managing them.

## 15. Four pricing models

| Model | You commit to | You give up | Fits |
| --- | --- | --- | --- |
| Pay-as-you-go | Nothing | The discount | New, spiky, or unknown workloads |
| Reservation | A specific resource, 1 or 3 years | Flexibility on that resource | Steady, known virtual machine size |
| Azure savings plan for compute | An hourly spend, 1 or 3 years | Some flexibility of spend | Steady compute across several services |
| Spot | Nothing; you use spare capacity | Guaranteed runtime; you can be evicted | Work that can stop and restart |

All four are cheaper or more flexible than buying hardware. Only the last three trade something for a lower compute rate. Pay-as-you-go trades nothing; it is the default.

## 16. How to choose a price

Steady and specific for years: reservation.

Steady spend, but the mix of virtual machines, containers, and functions may change: savings plan.

Can be interrupted: spot.

Anything else: pay-as-you-go.

We teach this again in Session 8, next to the bill. The comparison is an exam objective now, not only then.

## 17. Practice

Twelve workloads, sorted into IaaS, PaaS, or SaaS, each with one reason.

Six workload profiles, matched to a pricing model. One of them is a batch job that may be interrupted.

Then a short look at a Function App, so serverless is a screen and not only a definition.

## 18. Quiz and assignment

12 items. 15 minutes. Two of them are from Session 1.

Then, before next time:

- [Describe the benefits of using cloud services](https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/)
- [Describe cloud service types](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/)

Session 3 opens with a Domain 1 checkpoint covering all 15 cloud-concept objectives, including today.
