# Module 5 instructor guide — Describe Azure networking services

**Speak from this file.** It follows the current Microsoft Learn module in Microsoft's order. It is a consulting script for beginners, not a second copy of the documentation.

**Module:** [Describe Azure networking services](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/)

**Checked against the live module:** 9 October 2026

**Units, in the order you will teach them:**

1. [Introduction](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/1-introduction)
2. [Describe Azure virtual networking](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/2-virtual-network)
3. [Describe Azure virtual private networks](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/3-virtual-private-networks)
4. [Describe Azure ExpressRoute](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/4-expressroute)
5. [Describe Azure DNS](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/5-domain-name-system)
6. Module assessment (students take this on Learn after class; do not project it)
7. [Summary](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/7-summary)

**Microsoft's learning objectives, from the module page:**

- Describe Azure virtual networking, including subnets and endpoints
- Describe connectivity options with Azure VPN Gateway
- Describe when to use Azure ExpressRoute
- Describe Azure DNS capabilities
- Describe basic network access controls for Azure resources

The introduction and summary units use slightly different wording on the last objective: "Configure basic network access for an Azure resource." This class teaches students to **describe and recognize** those controls. We do not configure gateways, circuits, or firewall rules in this session.

**Course objective IDs** (local to this curriculum, not printed by Microsoft): 2.2.5, 2.2.6.

**How to use the concept blocks.** Each major concept has a short card and an instructor talk track. Say the talk track. Use the card when a student asks "why would anyone buy this?" or when you need the exam wording. Do not read the card headings aloud.

**What this file does not replace.** The course still has `sessions/session-05-instructor-notes.md`, slides, a Cloud Shell lab, and `quizzes/session-05-quiz.md`. This guide is the updated speak-from lecture for the current module. The 120-minute plan below is the lecture. It does not include the lab. If you insert the lab in this same session, cut the case-study replay to five minutes and assign the exit quiz as homework.

Anything the current module does not say is in **Supplemental instructor context** at the end. Do not promote that material into the main script.

---

## The client for the whole lesson

Contoso Health is fictional. Keep the same organization in every example.

- A headquarters clinic with on-premises systems and a VPN device
- Nurses and billing staff who work from home
- Virtual machines in Azure
- An Azure SQL database holding patient records
- An Azure Storage account holding images and documents
- A public website patients use
- Sensitive internal applications that must not sit on the public internet
- A compliance team that does not want critical patient-record transfers crossing the public internet
- A plan to connect the headquarters systems to Azure
- Later, a second Azure network for a research workload that must talk privately to the main Azure network
- A domain name they have already bought from a registrar: `contosohealth.org`

At each decision, ask the room: **"What would we recommend to Contoso, and why?"**

---

## Two-hour lesson plan

| Time | Block | Leave this block when |
| --- | --- | --- |
| 0:00–0:10 | Warm-up and the consulting question | The room can say who needs to talk to whom before anyone names a product |
| 0:10–0:25 | Networking big picture, using Contoso | They can separate "private network in Azure," "encrypted over the internet," and "private circuit that avoids the internet" |
| 0:25–0:55 | Virtual networking unit: VNet, subnets, endpoints, routing, filtering, peering | They can answer the six distinctions at the end of that section |
| 0:55–1:15 | VPN Gateway | Point-to-site, site-to-site, and network-to-network each have a who-is-connecting answer |
| 1:15–1:30 | ExpressRoute | Nobody in the room calls it "a faster VPN" |
| 1:30–1:42 | Azure DNS | They know Azure DNS hosts records and does not sell the domain name |
| 1:42–1:52 | Contoso case study, spoken as recommendations | The class makes the recommendation before you confirm it |
| 1:52–2:00 | Exit quiz and the ten takeaways | Items are reviewed, not just collected |

**If you are behind at 0:50.** Keep subnets, the three endpoints, NSGs, and peering. Shorten network virtual appliances to the one-sentence comparison. Shorten BGP to the one sentence in that block.

**If you are behind at 1:10.** Keep the three VPN scenarios and the route-based preference. Shorten high availability to active/standby plus "a VPN can fail over for ExpressRoute."

**If you are behind at 1:25.** Keep the VPN-versus-ExpressRoute comparison and the internet caveat about DNS. Cut Global Reach to the one Asia-and-Europe sentence, or skip it.

---

## Mention once, then move on

These ideas are in the module. They are useful. They are too implementation-specific for a long stop on AZ-900. Say the sentence. Do not open a portal blade.

- Gateway stock keeping units, and Standard public IP addresses versus Basic, for zone-redundant gateways
- Failover timing: connections typically return within a few seconds for planned maintenance and within 90 seconds for an unplanned disruption
- How active/active tunnels are built, including a second on-premises VPN device
- ExpressRoute connectivity models: any-to-any (IP VPN), point-to-point Ethernet, or a virtual cross-connection at a colocation facility. The unit says to focus on **when** to use ExpressRoute
- The service list ExpressRoute can reach, beyond one sentence
- ExpressRoute Global Reach, beyond the one example
- Border Gateway Protocol configuration, and Azure Route Server as anything more than a name
- Preshared keys as the authentication method
- Alias-record targets in detail
- The subnet name the portal expects for a gateway
- Address math, network security group priority numbers, and rule-building click paths

---

# 1. Introduction

## What Microsoft wants students to know

The module introduces Azure networking services that connect, secure, and route traffic. Students finish able to describe virtual networking, VPN Gateway options, when to use ExpressRoute, Azure DNS, and basic network access controls.

## Set the scene

**[0:00]** Contoso Health has already decided some workloads are moving to Azure. They have not decided how anything will talk. That decision comes before any product name.

## Instructor Talk Track

Welcome back. Last session we talked about compute: virtual machines, containers, and where an application runs. Today the question changes. An application that cannot be reached, or that is reached by the wrong people, is not a solution. It is a risk.

Imagine your organization is moving workloads into Azure. Before I recommend anything, I need to understand who needs to communicate with what, which traffic can use the public internet, which traffic must remain private, and how much control and reliability the organization requires.

Here is the business problem at Contoso Health. Patients need a website. Nurses at home need a secure way into internal systems. Headquarters already has servers that must keep talking to Azure. Patient records must not be casually exposed. Someone will also ask, "What is the name of our website," which is a different problem from "What is the private path to the database."

Before we choose a service, ask yourself four questions. Who is talking? Is the other party a person, a whole office, or another Azure network? Can that traffic use the public internet? Must it stay on a private path? How much consistency does the organization require when that path is busy or when a circuit fails?

If I were consulting with this company, the first question I would ask is not "Do you want a VPN?" The first question is "Draw me who needs to reach whom, and tell me which of those conversations are allowed to cross the public internet."

Today we will make those decisions in Microsoft's order. First the private network inside Azure. Then encrypted tunnels over the internet. Then a private connection that does not use the internet. Then names. Then we will stand back and recommend a set of choices for Contoso.

**Warm-up, two minutes.** Ask: "Name one Contoso conversation that can use the public internet, and one that should not." Take two answers. Do not correct product names yet. Write the two conversations on the board and leave them there all hour.

## Whiteboard / Visual

```text
CONTOSO HEALTH — who talks to whom?

Patients -------- website            (public is acceptable)
Nurse at home -- internal apps       (must be encrypted)
Headquarters ---- patient systems    (private, predictable)
Web servers ----- database           (inside Azure, segmented)
```

## Ask the Class

- Which of those four lines would you refuse to send across the public internet, and why?
- If two Azure networks need to talk, have we left Azure, or are we still inside Microsoft's network?
- What would you need to know before you told Contoso to buy a dedicated circuit?

## Exam Trap

The exam rarely asks you to build a gateway. It describes who is connecting, whether the traffic may use the public internet, and whether the path must be private and predictable. Choose the service that matches those constraints.

## Transition

Before we talk about VPNs or ExpressRoute, we need to understand the network we are connecting to. In Azure, that starting point is the virtual network.

---

# 2. Networking big picture

## What Microsoft wants students to know

Azure virtual networks let Azure resources communicate with each other, with users on the internet, and with on-premises computers. You can think of an Azure network as an extension of the on-premises network, with resources that link other Azure resources. The same unit names three ways to reach on-premises: point-to-site VPN, site-to-site VPN, and ExpressRoute. Peering connects virtual networks to each other on the Microsoft backbone.

## Set the scene

**[0:10]** Contoso's director asks for "the network design" in one slide. You give them the map, not the product catalog.

## Instructor Talk Track

Here is the map I would draw in the first meeting.

Inside Azure, Contoso gets a private network, called a virtual network. That is their space. We will divide it so the public website and the patient database are not sitting in the same segment. We will decide which doors face the internet, and which services are reached on a private address. We will also decide which traffic is allowed, and which road a packet takes. Allowing traffic and steering traffic are different jobs. Remember that. We will come back to it.

When Contoso needs to leave that private space, three different problems show up. A person at home is not a datacenter. Headquarters with its own VPN device is not a person. And "we need a private circuit that never touches the public internet" is not the same request as "encrypt a tunnel across the internet."

There is one more path that never leaves Azure. If Contoso later has two virtual networks, they can connect those networks directly. That traffic stays on Microsoft's backbone. It does not need a VPN just to make it private.

Azure DNS is not a path at all. It is how names become addresses. Contoso can buy a name from a registrar and still ask Microsoft to host the records. We will not mix that up with the private network.

Say this line, then leave it on the board: **"Private space in Azure. Encrypted tunnel over the internet. Private circuit that avoids the internet. A name that points at an address."** Everything today is one of those four.

## Whiteboard / Visual

```text
                    Internet
                       |
              +--------+---------+
              |                  |
         Public website     VPN tunnel
              |                  |
         +----+------------------+----+
         |  Contoso virtual network   |
         |   web segment | data segment|
         +----+------------------+----+
              |                  |
         Private services    Headquarters
         (private address)   (VPN or ExpressRoute)

Two Azure networks talking directly = peering
(on Microsoft's backbone, not the internet)
```

## Ask the Class

- Point at the board. Which box is the virtual network, and which line is only a tunnel?
- A nurse's laptop and the headquarters firewall both need to reach Azure. Why might those be two different recommendations?
- Is DNS a connection, or a way to find an address?

## Exam Trap

Students hear "private" and answer ExpressRoute for every private conversation. Peering is private and stays inside Microsoft's network. A VPN is private in the sense that the payload is encrypted, and the module says that encrypted traffic still crosses the internet. ExpressRoute is the option that does not travel over the public internet.

## Transition

We start where Microsoft starts: the virtual network, and the two kinds of endpoints the unit introduces immediately.

---

# 3. Describe Azure virtual networking

## What Microsoft wants students to know

From the virtual networking unit, students should be able to describe:

- Isolation and segmentation, including an address space that exists only inside the virtual network and is not internet-routable, divided into named subnets
- Internet communications, by a public IP address or a public load balancer
- Communication between Azure resources, including virtual machines and service endpoints for services such as Azure SQL and storage
- Communication with on-premises resources by point-to-site VPN, site-to-site VPN, or ExpressRoute
- Routing with route tables, Border Gateway Protocol, and user-defined routes
- Filtering with network security groups and network virtual appliances
- Virtual network peering, with traffic on the Microsoft backbone, including across regions
- Public endpoints and private endpoints, in the unit's definitions

Basic network access controls are this unit's filtering story. Microsoft does not give them a separate unit. Teach them here.

## Set the scene

**[0:25]** Contoso has virtual machines, a database, storage, a public website, and internal applications. Nothing has an address plan yet. You will not recommend a circuit until this room can describe the network those circuits attach to.

## Instructor Talk Track

Before we talk about VPNs or ExpressRoute, we need to understand the network we are connecting to. In Azure, that starting point is the virtual network, or VNet. Think of the VNet as the organization's private network space inside Azure.

I am going to walk Contoso's design in the same order Microsoft uses. Endpoints first, because the unit defines them before it defines subnets. Then the address plan. Then who can come in from the internet. Then how Azure resources reach each other. Then the three doors back to headquarters, which we will only preview. Then steering, then filtering, then connecting a second Azure network.

---

### Azure Virtual Network

**Microsoft Learn concept.** Azure virtual networks and subnets enable Azure resources, such as virtual machines, web apps, and databases, to communicate with each other, with users on the internet, and with on-premises client computers. The unit lists isolation and segmentation, internet communications, communication between Azure resources, communication with on-premises resources, routing, filtering, and connecting virtual networks.

**Plain English.** A VNet is Contoso's private network in Azure. Resources you place in it can talk. The rest of the world does not get that access unless you deliberately open a door.

**Consultant scenario.** Contoso is about to place web virtual machines, an internal scheduling application, and connectivity toward Azure SQL. What would we recommend to Contoso, and why? One virtual network as their private space in Azure. We do not start by buying a circuit.

**Instructor talk track.**

If I were consulting with this company, the first Azure networking object I would ask them to create is a virtual network. Not a VPN. Not ExpressRoute. A virtual network.

Here is the business problem. Contoso's website, internal applications, and future connections all need a place to live. That place has to be isolated from other customers. Azure runs many organizations on shared physical infrastructure. The virtual network is how Contoso gets its own network space anyway.

You can think of an Azure network as an extension of the on-premises network. That is Microsoft's picture, and it is the right consulting picture. Headquarters does not throw away its network. Azure becomes another site on the map, once we choose how the two sites meet.

The unit says a virtual network can do seven jobs: isolate and segment, talk to the internet, let Azure resources talk to each other, talk to on-premises, route, filter, and connect to other virtual networks. We will touch every one of those. You do not need to memorize the list as a list. You need to recognize which job a scenario is describing.

**Analogy.** The virtual network is the organization's private campus inside Azure. The buildings on that campus can talk to each other. A visitor does not wander in because the campus exists.

**Why an organization would use it.** They are putting resources in Azure and need those resources to communicate on a private network they control.

**Problem it solves.** Without a virtual network, Contoso does not have an isolated, segmented space in which to place those resources and decide who may talk.

**Common confusion.** A virtual network is not a VPN, and it is not a subnet. The VNet is the whole private space. A subnet is a division inside it. A VPN is a tunnel from somewhere else into that space.

**AZ-900 exam clue.** Watch for wording like "resources need to communicate with each other, with the internet, and with on-premises." That is the virtual network. Also watch for isolation. If the only requirement is "our own private network in Azure," the answer is a VNet, not ExpressRoute.

**Check for understanding.** In one sentence, what does Contoso get from a virtual network that they do not get from simply creating a virtual machine?

**Transition.** Microsoft's next sentences define the two doors a resource can have: a public endpoint and a private endpoint.

---

### Public endpoints and private endpoints

**Microsoft Learn concept.** Public endpoints have a public IP address and can be accessed from anywhere in the world. Private endpoints exist within a virtual network and have a private IP address from within the address space of that virtual network.

**Plain English.** A public endpoint is a front door with a street address. A private endpoint is an internal address that only exists inside the virtual network's address plan.

**Consultant scenario.** Contoso's patient website must be reachable by people who are not on Contoso's network. The Azure SQL database that holds patient records must be reachable from inside Contoso's virtual network on a private address. What would we recommend to Contoso, and why? A public endpoint for the website. A private endpoint for the database.

**Instructor talk track.**

This is where students often mix up two services, so I want the definitions in Microsoft's words before we get clever.

A public endpoint has a public IP address. It can be accessed from anywhere in the world. Contoso's public website needs that. Patients are on the internet. They are not inside the virtual network. A public address, or a public load balancer in front of the site, is how those patients arrive. We will lock down what they are allowed to do when we get to network security groups. A public endpoint is not the same thing as "no security." It means the door faces the world. You still decide what may walk through it.

A private endpoint exists within a virtual network and has a private IP address from that virtual network's address space. Read that again. The private address comes from Contoso's own Azure address plan. The database is reached the way you would reach an internal server, on a private address, from inside the network.

Here is the business problem for the database. Patient records should not require a public street address just so Contoso's own virtual machines can talk to them. A private endpoint gives that service a private address inside the VNet.

If I were consulting with this company, I would ask one question for every Azure service. "Does a stranger on the internet need to open this, or do only Contoso's own systems need to open this?" Strangers: public endpoint. Only Contoso's network: private endpoint.

Do not say a private endpoint is a VPN. A VPN connects a remote network or a remote person. A private endpoint gives a specific Azure service a private address inside the virtual network you already have.

**Analogy.** The public website has a street address printed on a sign. The patient database has an internal extension. You can call the extension from inside the campus. Publishing the extension in the phone book is a separate, bad idea.

**Why an organization would use it.** Public, when the audience is the internet. Private, when an Azure service should be consumed from inside the virtual network on a private address from that network.

**Problem it solves.** It separates "the world may look up this address" from "this service lives on our private address plan."

**Common confusion.** Private endpoint versus service endpoint. We have not defined service endpoints yet, because Microsoft defines them a few paragraphs later. Hold the question. The private endpoint's defining fact, today, is the private IP from the VNet's address space.

**AZ-900 exam clue.** "Public IP" and "from anywhere in the world" means public endpoint. "Private IP from the virtual network's address space" means private endpoint. If the stem does not mention a private address from the VNet, do not assume private endpoint.

**Check for understanding.** Contoso's website is down unless patients on home broadband can open it. Public endpoint or private endpoint? Why?

**Transition.** A private address has to come from somewhere. That is the address space, and then the subnets we carve out of it.

---

### Isolation, segmentation, and address space

**Microsoft Learn concept.** Azure Virtual Network lets you create multiple isolated virtual networks. When you set one up, you define a private IP address space using either public or private IP address ranges. The IP range only exists within the virtual network and is not internet-routable. You divide that space into subnets and allocate part of the space to each named subnet. For name resolution you can use the service built into Azure, or you can configure an internal or an external DNS server.

**Plain English.** You pick the range of addresses Contoso will use inside this VNet. Those addresses are meaningful inside the VNet. They are not a public route on the internet. You then cut the range into named pieces called subnets.

**Consultant scenario.** Contoso wants web servers and the database separated, and they do not want their internal addresses published as internet routes. What would we recommend to Contoso, and why? Define an address space on the virtual network, then divide it. Isolation is the VNet. Segmentation inside it is the subnet plan.

**Instructor talk track.**

Isolation means Contoso can have its own virtual network, separate from other virtual networks. If they later build a research environment that must stay apart from the clinical systems, that can be a second virtual network. Separate VNets do not automatically talk. We will connect them only if we mean to, with peering.

Segmentation is what we do inside one VNet. Microsoft's mechanism is simple. You define an address space. You divide it into subnets. Each subnet gets a name and a piece of that space.

Here is a classroom example, not a Microsoft requirement. Suppose Contoso's clinical VNet uses a private range. We might give a slice to the web servers and a different slice to the data tier. The numbers are not the exam. The decision is the exam. The website and the patient data should not be one flat segment with no boundary.

Two facts from the unit surprise people. First, you may define the space with public or private ranges. Second, either way, that range only exists within the virtual network and is not internet-routable. So "we used an address that looks public" does not mean "the internet can route to it." Inside the VNet, it is Contoso's private plan.

Name resolution gets one sentence now, and a full conversation later. The virtual network can use Azure's built-in name resolution, or you can point it at an internal or an external DNS server. That is how resources in the VNet find each other by name. It is not the same decision as hosting the public domain `contosohealth.org`. We will make that second decision in the Azure DNS unit. Do not merge them.

**Analogy.** The address space is the campus phone plan. Extensions work inside the campus. Printing an extension on a billboard does not make the public telephone network responsible for it. Subnets are the wings of the building: clinic, records, research. Same campus, different halls.

**Why an organization would use it.** They need isolation from other networks, and they need internal boundaries so that different workloads do not share one undifferentiated segment.

**Problem it solves.** It gives Contoso a private, non-internet-routable plan, and a way to split that plan on purpose.

**Common confusion.** VNet versus subnet. Creating a second subnet does not create a second virtual network. Creating a second virtual network does not, by itself, connect the two.

**AZ-900 exam clue.** "Divide the network so these servers are separated from those servers" inside one Azure network is subnets. "A separate isolated network" is another VNet. "The addresses are not internet-routable" is the address space behavior, even when the numbers you chose look public.

**Check for understanding.** Contoso asks whether picking a private-looking address range automatically publishes those addresses on the internet. What do you tell them?

**Transition.** The split itself has a name. That name is the subnet.

---

### Subnets

**Microsoft Learn concept.** You divide the IP address space into subnets and allocate part of the defined address space to each named subnet.

**Plain English.** A subnet is a named slice of the VNet's address space. You place resources into a subnet.

**Consultant scenario.** Contoso needs the public web servers divided from the database servers. What would we recommend to Contoso, and why? Two subnets in the same virtual network. Not two VPNs. Not ExpressRoute.

**Instructor talk track.**

Before we choose a connection product, ask yourself whether the resources are even in the right segment.

Contoso's web servers answer the public. The database servers should not sit in that same segment just because it was easy. We create a web subnet and a data subnet. Both are inside the one clinical virtual network. Each subnet has a name and a portion of the address space.

Here is the business problem. A flat network means every filtering rule and every future connection has to treat all of those servers as one group. Segmentation gives us a place to attach different rules later. The subnet is not the rule. The subnet is the place. The rule will be the network security group. Hold that distinction. Students love to say "subnet" when they mean "block the traffic."

A subnet also does not encrypt anything, and it does not connect headquarters. It organizes the Azure network you already decided to create.

**Analogy.** If the VNet is the building, the subnet is a floor. Web on one floor, data on another. The floors do not, by themselves, hire a guard. They give the guard a place to stand.

**Why an organization would use it.** To segment workloads inside one virtual network and assign each group its own part of the address plan.

**Problem it solves.** Different jobs are no longer forced into a single unnamed pool of addresses.

**Common confusion.** VNet versus subnet. The exam phrase "separate the web tier from the data tier" inside one network is a subnet answer. The exam phrase "two Azure networks in different regions must communicate" is not a subnet answer. That will be peering.

**AZ-900 exam clue.** Watch for "segment," "divide the address space," or "place these resources in a different part of the virtual network." Recommend a subnet.

**Check for understanding.** What would we recommend to Contoso to divide web servers from database servers, and why is the answer not a second virtual network?

**Transition.** Some of those web servers must accept visitors from the internet. That is the next capability.

---

### Internet communication

**Microsoft Learn concept.** You can enable incoming connections from the internet by assigning a public IP address to an Azure resource, or by putting the resource behind a public load balancer.

**Plain English.** Inbound internet access is a choice. You assign a public IP, or you place the resource behind a public load balancer.

**Consultant scenario.** Patients must open the website. The internal scheduling application must not accept inbound internet connections. What would we recommend to Contoso, and why? A public IP or a public load balancer for the website. No public inbound path for the scheduling application.

**Instructor talk track.**

Here is the business problem. "We have a virtual network" does not mean "the internet can reach everything in it." Incoming connections from the internet are enabled when you assign a public IP address to a resource, or when you put that resource behind a public load balancer.

For Contoso, that is the website. Patients are internet users. Give that site a public address, or put it behind a public load balancer. Then we will filter what is allowed to hit it.

The internal scheduling application fails this test. Nobody outside Contoso needs to open it from a browser on the public internet. We do not give it a public inbound path just because the website has one.

I am not going to teach load-balancer rules today. The exam point at this level is the pair of options Microsoft names: a public IP on the resource, or a public load balancer in front of it.

**Analogy.** A public IP is a street door you chose to unlock. A load balancer is a staffed reception desk in front of several doors. Either way, you decided the public may approach. The internal clinic door stays off the street.

**Why an organization would use it.** Internet clients must initiate a connection to an Azure resource.

**Problem it solves.** The public website is reachable without making every internal system reachable.

**Common confusion.** Public endpoint versus "the virtual network is on the internet." The VNet's address space is not internet-routable. Internet reachability is the public IP or the public load balancer you add.

**AZ-900 exam clue.** "Users on the internet need to connect inbound" points at a public IP or a public load balancer. It does not point at ExpressRoute.

**Check for understanding.** Name Contoso's system that needs inbound internet access, and the system that should not have it.

**Transition.** Inside Azure, resources still need to talk to each other. Microsoft gives two patterns.

---

### Communication between Azure resources, including service endpoints

**Microsoft Learn concept.** Azure resources communicate in one of two ways. Virtual networks can connect not only virtual machines but other Azure resources, such as the App Service Environment, Azure Kubernetes Service, and Azure virtual machine scale sets. Service endpoints can connect to other Azure resource types, such as Azure SQL databases and storage accounts. This approach lets you link multiple Azure resources to virtual networks to improve security and provide optimal routing between resources.

**Plain English.** Virtual machines and several other compute resources talk by being on the virtual network. Some platform services, and the unit names Azure SQL and storage, can be linked to the virtual network with a service endpoint so the connection is more secure and the routing is optimal.

**Consultant scenario.** Contoso's web virtual machines must reach the storage account, and the team wants that path linked to the virtual network for security and optimal routing. What would we recommend to Contoso, and why? A service endpoint, using the unit's own reason. If the requirement is instead "a private IP from our VNet address space," that remains the private endpoint from earlier. We will compare them in a moment.

**Instructor talk track.**

Microsoft says Azure resources can communicate securely in two ways. I am going to keep the two ways separate.

First way: put the resources on the virtual network. The unit's examples are not only virtual machines. A virtual network can also connect resources such as the App Service Environment, Azure Kubernetes Service, and virtual machine scale sets. You do not need to design those products today. You need to know a VNet is not "only for virtual machines."

Second way: service endpoints. The unit says service endpoints can connect to other Azure resource types, such as Azure SQL databases and storage accounts. Linking those resources to the virtual network improves security and provides optimal routing.

Here is the business problem. Contoso's web tier in Azure needs the storage account. They want that service tied to their virtual network rather than left as a wide-open path. A service endpoint is the feature the unit names for that link: security and optimal routing, for services such as SQL and storage.

Say the examples Microsoft uses. SQL and storage. If a scenario says "link this storage account or this Azure SQL database to the virtual network for security and optimal routing," you are in service-endpoint territory.

This is where students often mix up two services. A private endpoint, which we already defined, exists inside the virtual network and has a private IP from that virtual network's address space. A service endpoint, in this unit's words, links resource types such as SQL and storage to the virtual network for security and optimal routing. Same unit. Different sentences. Different exam clues.

If the stem's requirement is the private IP, recommend the private endpoint. If the stem's requirement is linking SQL or storage to the VNet for security and optimal routing, recommend the service endpoint. Do not upgrade a service-endpoint sentence into a private-endpoint answer because both sound "more private."

**Analogy.** A service endpoint is a designated staff corridor from your building to a specific partner service, built so the trip is controlled and direct. A private endpoint is the partner service receiving an internal extension on your own phone plan. Similar goal, different mechanism. Use the words in the question to decide which one they mean.

**Why an organization would use it.** To let Azure resources communicate, and to link services such as Azure SQL and storage to a virtual network for security and optimal routing.

**Problem it solves.** Those services are no longer left unrelated to the virtual network when the organization wants that tighter link.

**Common confusion.** Private endpoint versus service endpoint. Also, a service endpoint is not a VPN and not a subnet.

**AZ-900 exam clue.** Watch for "Azure SQL" or "storage account," plus "link to the virtual network," "security," or "optimal routing." That is the service endpoint passage. Watch for "private IP address from the address space of that virtual network" for the private endpoint.

**Check for understanding.** Read these two Contoso requests and pick a different feature for each. One: "Reach Azure SQL on a private IP that belongs to our VNet." Two: "Link the storage account to the VNet for security and optimal routing."

**Transition.** Those three endpoint words need one comparison, side by side, before we leave them.

---

### Endpoint comparison (classroom synthesis of this unit)

This comparison uses only the definitions in the virtual networking unit. A deeper platform detail that the unit does not state is in Supplemental instructor context. Do not add it unless a student asks.

**Instructor talk track.**

Let me put the three phrases on the board, because this is the mix-up I expect on the exam.

A public endpoint has a public IP and can be accessed from anywhere in the world. Contoso's patient website.

A private endpoint exists within the virtual network and has a private IP from that virtual network's address space. Contoso's database, when the requirement is that private address.

A service endpoint links Azure resource types such as Azure SQL and storage accounts to the virtual network, for security and optimal routing. Contoso's storage account, when the requirement is that link.

What would we recommend to Contoso, and why?

- Patients on the internet opening the website: public endpoint.
- Patient database reached on a private address from the VNet: private endpoint.
- Storage linked to the VNet for security and optimal routing: service endpoint.

If you can answer those three without swapping them, you have the endpoint objective.

**Check for understanding.** Which of the three would still be the answer if Contoso removed every public IP from the website? Trick question: the website would no longer have its public endpoint, and patients would not get in. Do not "fix" a public website by converting it to a private endpoint.

**Transition.** The website and the database are inside Azure. Headquarters is not. Microsoft names three ways to build that bridge. We will only name them now.

---

### Communication with on-premises resources (preview only)

**Microsoft Learn concept.** There are three ways. Point-to-site: a computer outside your environment initiates an encrypted VPN into the private network. Site-to-site: an on-premises VPN device or gateway links to the Azure VPN gateway; devices in Azure can appear local; the connection is encrypted and works over the internet. ExpressRoute: dedicated private connectivity that does not travel over the internet; useful when you need greater bandwidth and higher security.

**Plain English.** A person, a site, or a private circuit. We will study the first two in the VPN unit and the third in the ExpressRoute unit. Right now, Contoso only needs to see that all three are ways into the virtual network, and they are not interchangeable.

**Consultant scenario.** A nurse's laptop, the headquarters VPN device, and a compliance requirement that critical traffic avoid the public internet. Three requests. Three answers. We will not pretend one product covers all three.

**Instructor talk track.**

Azure virtual networks can link on-premises resources and Azure resources, so the network spans both places. The unit gives three methods. I am going to match them to Contoso and then refuse to design them yet.

Point-to-site is a computer outside the environment. The client initiates an encrypted VPN into the Azure virtual network. That is the nurse at home, on a laptop. It is not the whole hospital.

Site-to-site links an on-premises VPN device or gateway to the Azure VPN gateway. The connection is encrypted and works over the internet. Devices in Azure can appear as if they are on the local network. That is headquarters, where a network device represents the whole site. It is still the internet, with encryption.

ExpressRoute is dedicated private connectivity that does not travel over the internet. The unit says it is useful when you need greater bandwidth and even higher levels of security. That is the compliance conversation: critical traffic should not ride the public internet. We will define it properly in its own unit. Do not let anyone call it a faster VPN while we wait.

What would we recommend to Contoso, and why? We recommend nothing final yet. We recommend they stop treating "connect on-premises" as one product. A person, a site over the internet, and a private circuit are three designs.

**Analogy.** A person using a secured hallway through a public street, a guarded shuttle between two buildings that still uses public roads, and a private tunnel that never enters the public street. Three trips. Three constructions.

**Why an organization would use it.** Their data and users are not all in Azure.

**Problem it solves.** It extends the network across the local site and the cloud, using a method that matches the traffic.

**Common confusion.** Choosing ExpressRoute because the word "secure" appeared. Encryption over the internet is the VPN. Avoiding the internet is ExpressRoute.

**AZ-900 exam clue.** The VNet unit already contains the three definitions. A later question can be answered from this page alone if you listen for "client initiates," "on-premises VPN device" plus "over the internet," or "does not travel over the internet."

**Check for understanding.** Which Contoso person or place matches each of the three, in one phrase each?

**Transition.** Once traffic exists, someone has to decide which road it takes. That is routing. Filtering comes after, and it is not the same job.

---

### Route tables, user-defined routes, and BGP

**Microsoft Learn concept.** By default, Azure routes traffic between subnets on any connected virtual networks, on-premises networks, and the internet. Route tables let you define rules about how traffic should be directed. You can create custom route tables that control how packets are routed between subnets. Border Gateway Protocol works with Azure VPN gateways, Azure Route Server, or ExpressRoute to propagate on-premises BGP routes to Azure virtual networks. User-defined routes let you control the routing tables between subnets within a virtual network or between virtual networks.

**Plain English.** Azure already knows how to forward packets between subnets, connected networks, on-premises networks, and the internet. A route table is how you override that. A user-defined route is the custom route you put in that table. BGP is how on-premises route information can be shared into Azure when you are using VPN Gateway, Route Server, or ExpressRoute. You are not configuring BGP in this course.

**Consultant scenario.** Contoso assumes they must build routes before any virtual machines can talk across two subnets. What would we recommend to Contoso, and why? Start with Azure's default routing. Add a custom route table only when the default path is the wrong path.

**Instructor talk track.**

Here is the business problem. Packets need a road. Beginners hear "routing" and picture a project. In Azure, the default is already there. Azure routes traffic between subnets on connected virtual networks, between on-premises networks, and the internet. Contoso's web subnet can reach the data subnet without a weekend of router configuration.

You override that when the default road is not the road you want. A route table defines how traffic should be directed. A custom route table controls how packets are routed between subnets. User-defined routes are how you control those routing tables, between subnets in a virtual network or between virtual networks. At this level, treat "route table" and "user-defined route" as the same decision: we are steering, not filtering. The table holds the routes. The user-defined route is the route you added.

Border Gateway Protocol gets one minute, because the name shows up again on VPN and ExpressRoute. BGP works with Azure VPN gateways, Azure Route Server, or ExpressRoute to propagate on-premises BGP routes into Azure virtual networks. In plain language, it is a way for the on-premises network and Azure to exchange route information dynamically. You do not need to configure it for AZ-900. You need to recognize that Microsoft names BGP as that propagation method, and that ExpressRoute uses dynamic routing with BGP. If a question asks you to build a BGP policy, it has left this exam.

Routing is not security. A route decides where the packet is sent. It does not decide whether the packet is allowed. Contoso can steer traffic perfectly and still be wide open, or they can filter perfectly and still send traffic down the wrong road.

**Analogy.** A route is the turn-by-turn direction. A filter is the guard at the door. Changing the directions does not hire the guard. Hiring the guard does not change the directions.

**Why an organization would use it.** The default path is wrong, or on-premises routes need to be shared into Azure through BGP.

**Problem it solves.** Traffic goes where the organization intends, including across subnets and connected networks, without confusing that choice with allow-or-block.

**Common confusion.** Routing versus traffic filtering. Also, user-defined routes versus network security groups. If the question says "direct" or "route," do not answer with a security rule.

**AZ-900 exam clue.** "By default, Azure already routes between subnets, on-premises, and the internet." Custom route tables and user-defined routes are the override. BGP is the protocol name attached to VPN gateways, Route Server, and ExpressRoute when on-premises routes are propagated. Do not over-explain it.

**Check for understanding.** Contoso wants traffic between two subnets to take a different path than the default. Route table, or network security group?

**Transition.** Steering is settled. The guard comes next. This is Microsoft's "basic network access controls" objective, and it lives in this unit.

---

### Network security groups (basic network access controls)

**Microsoft Learn concept.** Network security groups are Azure resources that can contain multiple inbound and outbound security rules. You define these rules to allow or block traffic based on factors such as source and destination IP address, port, and protocol.

**Plain English.** An NSG is a list of allow and block rules. Each rule looks at where traffic came from, where it is going, which port it is using, and which protocol it is using. The list can cover inbound traffic and outbound traffic.

**Consultant scenario.** Contoso wants the web subnet to accept HTTPS from the internet, and they do not want the database subnet to accept inbound traffic from the internet. What would we recommend to Contoso, and why? Network security group rules. Allow the specific inbound web traffic. Deny the database inbound path they do not want.

**Instructor talk track.**

A network security group is like a security guard with a rule sheet. The guard is not deciding what application you are allowed to use. The guard is checking things such as where the traffic came from, where it is going, which port it is using, and whether the rule says allow or deny.

That analogy is accurate only if we keep the rule sheet honest. Microsoft says an NSG can contain multiple inbound and outbound rules. The factors in the unit are source and destination IP address, port, and protocol. Allow or block. That is the whole AZ-900 story.

Here is the business problem. Contoso's website should answer patients on the web port. It should not answer every other port because a public IP exists. The database subnet should not accept a connection from the internet just because a route to the internet exists. Remember the earlier point. A route is the road. The NSG is the guard.

I would tell Contoso: write the smallest set of rules you can explain. Inbound, who may come in. Outbound, where your servers may go. Name the address, the port, and the protocol. Allow what the application needs. Block what it does not.

We are not building the rule priority list in the portal today. If someone asks "which number wins," tell them that is an implementation detail below this exam, and bring them back to allow, block, direction, address, port, and protocol.

The guard does not replace segmentation. The subnet gave us a place to attach the guard. The NSG is the sheet the guard reads.

**Analogy.** The guard at the clinic door checks the list: who is asking, which department they want, which door number, and whether the list says yes or no. The guard does not choose the medical procedure. That is the application, not the network rule.

**Why an organization would use it.** They need basic allow and block control for a subnet or a network interface, in both directions.

**Problem it solves.** Opening a public path, or having a route, no longer means every packet is accepted.

**Common confusion.** NSG versus route table. NSG versus network virtual appliance, which is next. NSG versus a product named Azure Firewall, which is not this module. If a student says Azure Firewall, use the supplemental sentence at the end of this guide and come straight back.

**AZ-900 exam clue.** Watch for "allow or block," "inbound or outbound," "source and destination IP," "port," and "protocol." That is a network security group. If the stem says "direct the traffic" or "change the route," it is not.

**Check for understanding.** What would we recommend to Contoso to allow only the web port from the internet to the web subnet, and which four things does the guard look at?

**Transition.** Sometimes the organization wants a whole virtual machine whose job is a network function, not a list of allow and block rules. That is a network virtual appliance.

---

### Network virtual appliances

**Microsoft Learn concept.** Network virtual appliances are specialized virtual machines that can be compared to a hardened network appliance. A network virtual appliance carries out a particular network function, such as running a firewall or performing WAN optimization.

**Plain English.** An NVA is a virtual machine whose job is a network job. The unit's examples are a firewall and WAN optimization. It is not the rule list. It is a machine that performs a network function.

**Consultant scenario.** Contoso's network lead says, "We already use a hardened firewall appliance on premises, and we want that kind of function in Azure." What would we recommend to Contoso, and why? Recognize that Microsoft's name for a specialized virtual machine doing that job is a network virtual appliance. Do not redesign their appliance. Do not confuse it with the NSG.

**Instructor talk track.**

This is where students often mix up two services. They hear "firewall" and assume every filter in Azure is the same object.

A network security group is Azure's rule resource: inbound and outbound, allow or block, by address, port, and protocol.

A network virtual appliance is a specialized virtual machine, compared in the unit to a hardened network appliance. It carries out a particular network function. The examples Microsoft gives are running a firewall, or WAN optimization.

Here is the business problem. Some organizations want a network function that is a product running on a machine, the way a physical appliance was a box in the rack. Azure can host that as a virtual machine built for the job. That is the NVA. It is a different decision from attaching an NSG rule sheet.

You will not be asked to size an appliance or to pick a vendor on AZ-900. You will be asked not to call an NSG a virtual appliance, and not to call a routing change a firewall.

One sentence on routing, then we leave. If traffic must be steered toward a device like that, steering is still a route. Filtering is still a filter. The appliance is the function. We are not designing that path today.

**Analogy.** The NSG is the guard with a clipboard. The NVA is a specialist hired to sit in a room and perform a network job, such as a dedicated firewall unit or a WAN optimizer. You might send people past the specialist. The clipboard and the specialist are not the same employee.

**Why an organization would use it.** They need a network function that runs as a specialized virtual machine, such as a firewall function or WAN optimization.

**Problem it solves.** That function has a place in the Azure network without pretending the NSG rule sheet is a full appliance.

**Common confusion.** NSG versus NVA. The NSG is rules. The NVA is a specialized VM that performs a network function.

**AZ-900 exam clue.** "Specialized VM," "hardened appliance," "firewall function," or "WAN optimization" points at a network virtual appliance. "Allow or deny this port from this address" points at an NSG.

**Check for understanding.** Contoso wants to block TCP 1433 from the internet. NSG or NVA? Why is the NSG enough for that sentence?

**Transition.** We have one network. Contoso's research team will eventually need a second virtual network, and those two networks will need to talk without crossing the public internet.

---

### Virtual network peering

**Microsoft Learn concept.** Peering allows two virtual networks to connect directly. Traffic between peered networks is private and travels on the Microsoft backbone network, never entering the public internet. Resources in each virtual network can communicate. The virtual networks can be in separate regions, which lets you create a global interconnected network through Azure.

**Plain English.** Peering joins two VNets directly. The traffic stays on Microsoft's own backbone. It does not go out to the public internet and back. The VNets may be in different regions.

**Consultant scenario.** Contoso's research virtual network must communicate with the clinical virtual network. Both are in Azure. The traffic must stay off the public internet. What would we recommend to Contoso, and why? Virtual network peering. Not a site-to-site VPN, and not ExpressRoute. Those are for on-premises connectivity. Peering is for two Azure virtual networks.

**Instructor talk track.**

Here is the business problem. Two private spaces in Azure need to behave like one conversation, and Contoso does not want that conversation to hairpin through the public internet.

Virtual network peering connects two virtual networks directly. Network traffic between them is private. It travels on the Microsoft backbone and never enters the public internet. Resources on each side can communicate. The virtual networks can be in separate regions. That last sentence matters. "They are in two regions" does not force you into a VPN.

What would we recommend to Contoso, and why? Peer the research VNet to the clinical VNet. They are both Azure virtual networks. Peering is the direct private path the unit describes.

This is where students often mix up two services. Peering versus VPN. A network-to-network VPN, which we will define in the next unit, encrypts traffic inside a tunnel as it crosses the internet. Peering does not take that internet path. The module says peering traffic never enters the public internet. It is already on the Microsoft backbone.

Peering is also not a subnet. A subnet divides one VNet. Peering connects two VNets.

Peering is not a private endpoint. A private endpoint gives one service a private IP inside a VNet. Peering connects the networks themselves.

**Analogy.** Peering is an internal corridor between two buildings that Contoso already owns inside the Azure campus. The corridor never dumps people onto the public street. A VPN would be an encrypted ride along the public street between two places. If both buildings are already on Microsoft's campus, build the corridor.

**Why an organization would use it.** Two virtual networks must communicate privately, including when they are in different regions.

**Problem it solves.** Those networks can talk without sending the traffic onto the public internet and without pretending they are one subnet.

**Common confusion.** VNet peering versus VPN. Peering versus subnet. Peering versus private endpoint.

**AZ-900 exam clue.** Watch for "two virtual networks," "Microsoft backbone," "never enters the public internet," and "separate regions." That is peering. If one side of the connection is an on-premises datacenter, peering is the wrong answer.

**Check for understanding.** The research VNet is in another Azure region. A student recommends a VPN "so it stays private." What do you say?

**Transition.** We have the Azure network, the segments, the doors, the guard, and a way to join two Azure networks. Now we can talk about the encrypted tunnel, because we finally know what we are connecting to.

## Whiteboard / Visual

Draw this once, about halfway through the section, and keep pointing at it.

```text
Internet
   |
Public IP          (public endpoint: the website)
   |
+---------------- Contoso VNet ----------------+
|  address space exists only inside this VNet  |
|                                               |
|  Web subnet              Data subnet          |
|  website VMs             internal apps        |
|  NSG: allow HTTPS in     NSG: block internet  |
|                                               |
|  private endpoint = private IP in this space  |
|  service endpoint = link SQL/storage          |
|     for security and optimal routing          |
+----------------------+------------------------+
                       |
            second VNet (research)
            peered, Microsoft backbone
            traffic does not enter the internet
```

Under the box, write three words in a row: **Route = steer. NSG = allow or block. NVA = specialized VM.**

## Ask the Class

- What would we recommend to Contoso to divide web servers from database servers, and why?
- The storage account must be linked to the VNet for security and optimal routing. Which feature is that, and which feature would you choose instead if the requirement were a private IP from the VNet address space?
- Two Azure VNets, different regions, traffic must stay off the public internet. Peering or site-to-site VPN?

## Exam Trap

The highest-risk swaps in this unit are: subnet versus VNet, public endpoint versus private endpoint, private endpoint versus service endpoint, route versus NSG, NSG versus network virtual appliance, and peering versus VPN. If a stem contains "private," read the next six words before you answer. Private IP in the VNet, private backbone between VNets, and private circuit from on-premises are three different recommendations.

## Transition

The nurse at home and the headquarters VPN device are still waiting. Both of them need an encrypted tunnel across a network they do not trust. That is the VPN unit.

---

# 4. Describe Azure virtual private networks

## What Microsoft wants students to know

A VPN uses an encrypted tunnel within another network, typically to connect trusted private networks over an untrusted network such as the public internet. Traffic is encrypted to prevent eavesdropping. Azure VPN Gateway is a virtual network gateway deployed in a dedicated subnet. It supports site-to-site, point-to-site, and network-to-network connections. Data is encrypted inside a private tunnel as it crosses the internet. One VPN gateway per virtual network can connect to multiple locations. Policy-based and route-based differ in how they choose what to encrypt. Route-based is the preferred method for on-premises devices and is more resilient when the topology changes. High availability includes active/standby by default, active/active with BGP, VPN as a failover for ExpressRoute, and zone-redundant gateways where availability zones exist.

## Set the scene

**[0:55]** Contoso has accepted the virtual network. They now have two internet-based connection problems, plus a possible future connection between Azure networks that they might wrongly try to solve with a tunnel. You are choosing the shape of the tunnel, not the size of the gateway.

## Instructor Talk Track

A virtual private network uses an encrypted tunnel inside another network. We deploy VPNs when trusted private networks need to share sensitive information across an untrusted network. That untrusted network is typically the public internet. Encryption is there to prevent eavesdropping and similar attacks.

Say that before any Azure product name. A VPN is not "a private wire." The wire is still the internet. The privacy is the encryption.

Contoso has three pictures that often get shoved into the word VPN. A nurse's laptop. A headquarters device that represents the whole building. Two networks that both need to share a tunnel. Azure VPN Gateway can do all three. ExpressRoute is still not one of the three. Peering remains the better Azure-to-Azure answer when the requirement is the Microsoft backbone rather than a tunnel across the internet.

---

### What a VPN is

**Microsoft Learn concept.** A VPN uses an encrypted tunnel within another network. VPNs typically connect two or more trusted private networks over an untrusted network, typically the public internet. Traffic is encrypted while it travels over that untrusted network to prevent eavesdropping or other attacks.

**Plain English.** Take a network you do not trust, usually the internet. Build an encrypted tunnel through it so the private networks on each end can share sensitive information.

**Consultant scenario.** Contoso will not pay for a dedicated private circuit this year, but nurses and headquarters still need to reach Azure without sending readable patient data across the open internet. What would we recommend to Contoso, and why? A VPN. Encryption over the internet. Not ExpressRoute, because they have not required a private circuit that avoids the internet.

**Instructor talk track.**

Here is the business problem. The internet is a shared, untrusted network. Contoso still has to use it for some people and some sites. A VPN does not remove the internet from the path. It builds an encrypted tunnel through that path so outsiders cannot read the traffic.

If I were consulting with this company, I would say: use a VPN when encryption across the internet is the requirement, and you do not have a requirement for a private dedicated circuit. The moment the requirement becomes "this traffic must not travel over the public internet," you have left the VPN unit. We will go there next. Do not arrive early.

**Analogy.** A VPN is an armored car on a public highway. The highway is still public. The cargo is protected. It is not a private road.

**Why an organization would use it.** Sensitive traffic must cross an untrusted network, and encryption is the control they are willing to use.

**Problem it solves.** Eavesdropping on that path. The module's phrase is to prevent eavesdropping or other attacks.

**Common confusion.** "VPN" versus "ExpressRoute." Encrypted tunnel across the internet, versus private connectivity that bypasses the internet.

**AZ-900 exam clue.** "Encrypted," "tunnel," "public internet," "untrusted network" is the VPN definition. Do not answer ExpressRoute unless the stem says the traffic does not travel over the public internet.

**Check for understanding.** In one sentence, what does a VPN protect, and what network does that protection still cross?

**Transition.** Azure's product for terminating that tunnel into a virtual network is VPN Gateway.

---

### Azure VPN Gateway

**Microsoft Learn concept.** A VPN gateway is a type of virtual network gateway. Instances are deployed in a dedicated subnet of the virtual network. They connect on-premises datacenters site-to-site, individual devices point-to-site, and virtual networks to other virtual networks. All data transfer is encrypted inside a private tunnel as it crosses the internet. You can deploy only one VPN gateway in each virtual network, but one gateway can connect to multiple locations, including other virtual networks or on-premises datacenters. For both policy-based and route-based types, authentication is a preshared key.

**Plain English.** VPN Gateway is the Azure end of the tunnel. It lives in its own subnet inside the VNet. One VNet gets one of these gateways, and that one gateway may talk to many places. Everything that crosses the internet through it is encrypted inside the tunnel.

**Consultant scenario.** Contoso wants headquarters and several clinics, each with its own network, to reach the same Azure virtual network. What would we recommend to Contoso, and why? One VPN gateway in that virtual network, used to connect multiple locations. Not one gateway per clinic.

**Instructor talk track.**

Azure VPN Gateway is a virtual network gateway deployed in a dedicated subnet of the virtual network. That dedicated subnet is a requirement you should recognize. We are not going to spend the hour naming the subnet or picking a gateway size. Those are implementation details. The exam point is that the gateway sits in the virtual network, in a subnet set aside for it.

All data transfer is encrypted inside a private tunnel as it crosses the internet. I am going to repeat that because it is the difference from peering and from ExpressRoute. VPN traffic crosses the internet. The tunnel is what makes the crossing private.

You can deploy only one VPN gateway in each virtual network. You can use that one gateway to connect to multiple locations. Headquarters and a second clinic do not mean two gateways in the same VNet. They mean one gateway with more than one connection.

Authentication, for either VPN type, is a preshared key. That is the only authentication fact in the unit. Do not build a lecture on certificates. If someone asks, say the module's method for both types is a preshared key, and move on.

**Analogy.** The gateway is the secure loading dock on Contoso's Azure building. There is one dock for that building. Many armored trucks can pull up to the same dock. The dock is not the highway, and it is not the private tunnel bored under the city.

**Why an organization would use it.** They need the Azure end of an encrypted tunnel into a specific virtual network, for sites, people, or other networks.

**Problem it solves.** The virtual network has a place to terminate those encrypted connections, including more than one location on a single gateway.

**Common confusion.** "One gateway" versus "one location." One gateway per VNet. Many locations per gateway. Also, the gateway subnet is not the web subnet. Do not place the website in the gateway's dedicated subnet in a design conversation.

**AZ-900 exam clue.** Watch for "only one VPN gateway per virtual network" and "one gateway, multiple locations." Both are true. A wrong answer will claim you need a separate gateway resource for every site.

**Check for understanding.** Contoso has one clinical VNet and three sites. How many VPN gateways does this unit allow in that VNet?

**Transition.** Who is on the other end of the tunnel changes the name of the connection. There are three names.

---

### Site-to-site, point-to-site, and network-to-network

**Microsoft Learn concept.** Site-to-site connects on-premises datacenters to virtual networks. Point-to-site connects individual devices to virtual networks. Network-to-network connects virtual networks to other virtual networks. In the virtual networking unit, point-to-site is initiated by the client computer, and site-to-site links an on-premises VPN device or gateway to the Azure VPN gateway over the internet, with Azure devices able to appear local.

**Plain English.** Site-to-site is a place. Point-to-site is a person or a single device. Network-to-network is Azure network to Azure network, using a VPN tunnel that still crosses the internet.

**Consultant scenario.** Use three Contoso requests, and make the room answer before you do.

- A nurse's laptop at home needs encrypted access. Point-to-site.
- Headquarters, with its own VPN device, needs the whole site connected, encrypted, over the internet. Site-to-site.
- Two networks need a secure encrypted connection. If both are Azure VNets and the requirement is the Microsoft backbone, peering is the better match. If the requirement is an encrypted VPN tunnel, the gateway feature is network-to-network.

**Instructor talk track.**

Before we choose a service, ask yourself who initiates the connection, and whether the other side is a device, a site, or another network.

Point-to-site connects an individual device to the virtual network. The virtual networking unit says the client computer initiates the encrypted VPN. That is the remote employee. The nurse opens the connection from the laptop. Contoso does not install a datacenter firewall in the nurse's kitchen. What would we recommend to Contoso, and why? Point-to-site VPN.

Site-to-site connects an on-premises datacenter to the virtual network. The on-premises side is a VPN device or gateway. The connection is encrypted and works over the internet. Devices in Azure can appear as if they are on the local network. That is headquarters. The building already has a network device that can represent everyone inside it. What would we recommend to Contoso, and why? Site-to-site VPN, as long as crossing the internet inside an encrypted tunnel is acceptable.

Network-to-network connects a virtual network to another virtual network through the VPN gateway. All of that data is still encrypted inside a private tunnel as it crosses the internet. Hear the internet in that sentence.

This is where students often mix up two services. Network-to-network VPN versus peering. Both can connect two Azure virtual networks. Peering keeps the traffic on the Microsoft backbone and never puts it on the public internet. The VPN path crosses the internet inside the tunnel. If Contoso's research network and clinical network are both in Azure, and the requirement is private backbone connectivity, I still recommend peering. I recommend the network-to-network VPN when the requirement in front of me is the encrypted VPN connection itself.

Also refuse the swap between point-to-site and site-to-site. "A laptop" is not a site. "The headquarters firewall" is not a point.

**Analogy.** Point-to-site is one employee with a key to a secured door. Site-to-site is a bridge between two office buildings, guarded at each end. Network-to-network is that same kind of guarded bridge when both ends are Azure networks. Peering, which we already drew, is the indoor corridor that never uses the bridge.

**Why an organization would use it.** The shape of the far end is different, so the connection type is different.

**Problem it solves.** People, sites, and networks are not forced into one connection style.

**Common confusion.** Point-to-site versus site-to-site. Network-to-network VPN versus VNet peering. Any of them versus ExpressRoute.

**AZ-900 exam clue.** "Individual device," "laptop," "client initiates" is point-to-site. "On-premises datacenter," "VPN device," "encrypted over the internet" is site-to-site. "Virtual network to virtual network" plus a VPN or a tunnel that crosses the internet is network-to-network. "Microsoft backbone" and "never enters the public internet" between two VNets is peering, not this list.

**Check for understanding.** Call out three Contoso sentences and have the class answer with only the connection type.

**Transition.** The gateway still has a type: policy-based or route-based. You need the difference at a fundamentals level, and you need to know which one Microsoft prefers for almost every modern case in this unit.

---

### Policy-based versus route-based

**Microsoft Learn concept.** Policy-based gateways statically specify the IP addresses of packets that should be encrypted through each tunnel. The device evaluates every packet against those sets of addresses to choose the tunnel. Route-based gateways model IPSec tunnels as a network interface or virtual tunnel interface. IP routing, static or dynamic, decides which tunnel interface to use. Route-based VPNs are the preferred connection method for on-premises devices. They are more resilient to topology changes, such as the creation of new subnets. Use a route-based gateway for connections between virtual networks, point-to-site connections, multisite connections, and coexistence with an ExpressRoute gateway.

**Plain English.** Policy-based means "here is the exact list of addresses whose traffic I will encrypt." Route-based means "treat the tunnel like a network path, and use routing to decide what goes into it." Route-based is the one you recommend when subnets will change, when a person connects, when there are multiple sites, when two VNets connect by VPN, or when the VPN must coexist with ExpressRoute.

**Consultant scenario.** Contoso will add subnets as new clinics onboard. They also need point-to-site for nurses and more than one site. What would we recommend to Contoso, and why? A route-based VPN gateway.

**Instructor talk track.**

When you set up a VPN gateway, you specify policy-based or route-based. The unit says the primary distinction is how they determine which traffic needs encryption.

A policy-based gateway specifies, statically, the IP addresses of packets that should be encrypted through each tunnel. Every packet is evaluated against those sets. It works when the list of addresses is fixed and known. It is brittle when Contoso adds a subnet next month, because the interesting traffic was defined as a frozen list.

A route-based gateway models the tunnel as a network interface, sometimes called a virtual tunnel interface. Routing, either static routes or dynamic routing protocols, decides which tunnel to use for each packet. The unit says route-based VPNs are the preferred connection method for on-premises devices, and they are more resilient to topology changes such as the creation of new subnets.

I am not going to draw IPSec headers. I am going to give you Microsoft's "use route-based if you need any of these" list. Connections between virtual networks. Point-to-site connections. Multisite connections. Coexistence with an ExpressRoute gateway.

Look at Contoso. Nurses are point-to-site. Headquarters plus another clinic is multisite. New subnets are coming. If they later add ExpressRoute and want the VPN as a companion, coexistence is on that list too. What would we recommend to Contoso, and why? Route-based.

Policy-based is the one you recognize when the stem says the addresses to encrypt are specified statically, and each packet is checked against that list. It is not Contoso's general recommendation.

**Analogy.** Policy-based is a courier who will only carry envelopes addressed to a typed list. Add a new department, and you must retype the list. Route-based is a courier who follows the road signs. When you open a new wing, you update the signs. You do not reissue the courier.

**Why an organization would use it.** Route-based, when the network will change or when they need the connection types in Microsoft's list. Policy-based, only when you are recognizing the static address-list behavior.

**Problem it solves.** The gateway knows which packets enter which tunnel, in a way that either freezes the address list or follows routing.

**Common confusion.** Thinking "policy" means Azure Policy, or a network security group. This policy is "which addresses get encrypted." It is not a governance policy and it is not an allow rule.

**AZ-900 exam clue.** "New subnets," "topology changes," "point-to-site," "multisite," "between virtual networks," or "coexist with ExpressRoute" all point at route-based. "Statically specify the IP addresses to encrypt" points at policy-based.

**Check for understanding.** Contoso adds a new subnet every quarter. Which VPN type survives that change with less pain, and why?

**Transition.** A tunnel that is down is not a design. Microsoft's high-availability story is short. We will keep it short.

---

### High availability

**Microsoft Learn concept.** By default, VPN gateways are deployed as two instances in an active/standby configuration, even if you see only one gateway resource. On failure, the standby takes over without user intervention. Connections are interrupted, then typically restored within a few seconds for planned maintenance and within 90 seconds for unplanned disruptions. Active/active uses BGP, assigns a unique public IP to each instance, and uses separate tunnels from the on-premises device to each IP. You can add a second on-premises VPN device. A VPN gateway can be a secure failover path for ExpressRoute, using the internet as the alternate path, because a circuit can still be affected by a cable cut or a location outage. In regions with availability zones, VPN and ExpressRoute gateways can be zone-redundant. Those gateways use different SKUs and Standard public IP addresses instead of Basic.

**Plain English.** The default is active/standby: two instances, one resource, automatic failover, a short interruption. Active/active means both instances have their own public IP and their own tunnel, and it depends on BGP. A VPN can also be the backup path if an ExpressRoute circuit fails. Zone-redundant gateways exist in regions that have availability zones. Do not memorize SKUs.

**Consultant scenario.** Contoso is worried that planned maintenance on the gateway will require someone to rebuild the tunnel by hand. What would we recommend to Contoso, and why? Rely on the default active/standby pair. Failover does not wait for a person. If their later design uses ExpressRoute for the main path, the VPN can be the secure failover over the internet. Say that once. We will define ExpressRoute next.

**Instructor talk track.**

If you are configuring a VPN to keep information safe, you also want it highly available. Four ideas. None of them is a configuration lab.

Active/standby is the default. Azure deploys two instances even when you see one VPN gateway resource. If planned maintenance or an unplanned disruption hits the active instance, the standby takes the connections without a person stepping in. Connections do drop during that failover. The unit says they are typically restored within a few seconds for planned maintenance and within 90 seconds for unplanned disruptions. I would not build a quiz around those two numbers. I would remember "automatic, brief interruption, standby already exists."

Active/active is optional. It exists because BGP is supported. Each instance gets its own public IP. The on-premises device builds a separate tunnel to each IP. You can add a second on-premises VPN device if you want the on-premises side highly available too. The exam point is the shape: both sides active, unique public IP per instance, BGP in the picture. Not the click path.

ExpressRoute failover is the idea you should be able to say in a full sentence. ExpressRoute circuits have resiliency built in, and they are still not immune to a cut cable or an outage of an entire ExpressRoute location. You can provision a VPN gateway that uses the internet as an alternate path. The VPN is the secure backup. It is not the definition of ExpressRoute.

Zone-redundant gateways, in regions that support availability zones, apply to both VPN gateways and ExpressRoute gateways. They separate the gateway across zones so a zone failure does not take the on-premises connectivity with it. They require different gateway SKUs and Standard public IPs rather than Basic. That sentence is the entire SKU conversation. Do not open a pricing page.

**Analogy.** Active/standby is a second pilot already in the seat. Active/active is two planes flying the route at the same time, each with its own call sign. The ExpressRoute failover is a public highway you can still use, in an armored car, if the private road is closed.

**Why an organization would use it.** The connection is important enough that a single gateway instance, or a single ExpressRoute location, should not be a single point of failure.

**Problem it solves.** Maintenance and failures have a defined backup: standby, a second active instance, another zone, or a VPN when the private circuit fails.

**Common confusion.** Thinking active/standby means they must create two gateway resources. The unit says two instances, and you may see only one resource. Also, thinking the VPN failover means ExpressRoute traffic suddenly stops using encryption rules. The failover path is a VPN, so that backup path is the encrypted internet tunnel.

**AZ-900 exam clue.** "Default high availability" is active/standby. "BGP" plus "a public IP on each instance" is active/active. "Backup if the ExpressRoute circuit fails" is a VPN gateway using the internet as the alternate path. SKUs and Basic versus Standard are the zone-redundant detail. Recognize them. Do not design them.

**Check for understanding.** Contoso sees one VPN gateway in the portal and worries there is no standby. What does the unit say is already deployed?

**Transition.** We have used the internet as a path, on purpose, with encryption. Contoso's compliance lead is about to say that the internet is not an acceptable path for the patient-record sync. That is ExpressRoute, and it is not a faster VPN.

## Whiteboard / Visual

```text
Nurse laptop
    \
     \  point-to-site (client initiates, encrypted)
      \
       +-- VPN Gateway --+          one gateway in a dedicated subnet
      /                    \         one per VNet, many locations
     /  site-to-site        \
Headquarters VPN device      internet, inside an encrypted tunnel

Research VNet ==== network-to-network VPN ==== also crosses the internet
Research VNet ---- peering ------------------- Microsoft backbone
                                              (not this unit's tunnel)
```

Write under it: **Route-based if the network will grow, if people connect, if there are many sites, or if ExpressRoute must coexist.**

## Ask the Class

- Remote employee, encrypted access. What would we recommend to Contoso, and why?
- Headquarters has a VPN device. Encrypted connectivity is required. A private circuit is not required. Which connection type?
- Two Azure VNets must communicate with traffic staying on the Microsoft backbone. Why is the answer not a VPN?

## Exam Trap

The trap is the word "private." A VPN is a private tunnel across the public internet. Peering is private on the backbone between VNets. ExpressRoute is private because it does not use the public internet. Read which privacy the question bought.

## Transition

Contoso's compliance requirement is the one we have been postponing. They need the on-premises network extended into Microsoft's cloud on a private connection. The traffic must not travel over the public internet.

---

# 5. Describe Azure ExpressRoute

## What Microsoft wants students to know

ExpressRoute extends on-premises networks into the Microsoft cloud over a private connection, with the help of a connectivity provider. That connection is an ExpressRoute circuit. It can reach services such as Azure and Microsoft 365. Connections do not go over the public internet, so they offer more reliability, faster speeds, consistent latencies, and higher security than typical internet connections. Choose it for private consistent connectivity, strict compliance or data-transfer requirements, predictable latency and high throughput, or to keep critical traffic off the public internet. Even with ExpressRoute, DNS queries, certificate revocation list checking, and Azure Content Delivery Network requests still go over the public internet. At this level, focus on when to use it, not on connectivity models.

## Set the scene

**[1:15]** Contoso's compliance lead has one non-negotiable sentence: the headquarters copy of the patient records must not cross the public internet on its way to Azure. They also want the latency to be predictable. You are deciding whether a dedicated private circuit is justified.

## Instructor Talk Track

Azure ExpressRoute lets you extend your on-premises network into the Microsoft cloud over a private connection, with the help of a connectivity provider. This connection is called an ExpressRoute circuit.

I want that sentence to be the one you can say without notes. Private connection. Connectivity provider. Circuit. On-premises extended into Microsoft's cloud.

With ExpressRoute, you can establish connections to Microsoft cloud services such as Microsoft Azure and Microsoft 365. Each location Contoso connects — an office, a datacenter, another facility — would have its own circuit.

Here is the comparison I want on the board before anyone offers a slogan.

VPN Gateway is an encrypted tunnel across the public internet.

ExpressRoute is private dedicated connectivity that bypasses the public internet.

Do not describe ExpressRoute as a faster VPN. The unit does say ExpressRoute offers more reliability, faster speeds, consistent latencies, and higher security than typical internet connections. "Typical internet connection" is the comparison Microsoft wrote. A VPN is not a typical unprotected internet connection. It is an encrypted tunnel. ExpressRoute's defining fact is that the connection does not go over the public internet. Speed and consistency are benefits of that private path. They are not a reason to collapse the two products into one adjective.

---

### What ExpressRoute is, and when Contoso would use it

**Microsoft Learn concept.** Private connection through a connectivity provider, called a circuit. Not over the public internet. More reliability, faster speeds, consistent latencies, and higher security than typical internet connections. Connectivity can be from an any-to-any (IP VPN) network, a point-to-point Ethernet network, or a virtual cross-connection through a provider at a colocation facility. Benefits named in the unit: connectivity to Microsoft cloud services across regions in the geopolitical region; Global Reach; dynamic routing with BGP; built-in redundancy at every peering location; you can add multiple circuits. Direct access examples: Microsoft Office 365, Dynamics 365, Azure virtual machines, Cosmos DB, and Azure Storage. Choose it when you need private consistent connectivity, strict compliance or data-transfer requirements, predictable latency and high throughput, or you want to avoid the public internet for critical traffic. Security consideration: data does not travel over the public internet, which reduces internet risk. Caveat: DNS queries, certificate revocation list checking, and Azure CDN requests are still sent over the public internet.

**Plain English.** A partner provides a private circuit from Contoso's site into Microsoft's cloud. Patient-record traffic on that circuit does not ride the public internet. The organization pays for that privacy, consistency, and throughput because the internet, even with a VPN, is the wrong kind of path for that traffic.

**Consultant scenario.** Headquarters must sync patient records into Azure with private, predictable connectivity, and the compliance requirement is that this critical traffic avoid the public internet. What would we recommend to Contoso, and why? ExpressRoute. Not site-to-site VPN.

**Instructor talk track.**

If I were consulting with this company, I would not start with bandwidth numbers. I would start with the path.

Contoso can already encrypt headquarters traffic over the internet with a site-to-site VPN. That solves eavesdropping. It does not solve "this traffic must not be on the public internet." It also does not, by itself, give them the consistent latency and high throughput the unit associates with ExpressRoute.

ExpressRoute uses a connectivity provider. Contoso does not string a private cable to a Microsoft datacenter by themselves. The provider's private connection is the circuit. Each Contoso location that needs this relationship gets its own circuit.

The unit lists ways that provider connection might be built: an any-to-any IP VPN network, point-to-point Ethernet, or a virtual cross-connection at a colocation facility. I am naming those so they sound familiar if you read the module. We will not design them. Microsoft's own unit says that at this level you focus on when to use ExpressRoute rather than on detailed connectivity models.

When, in four lines, from the unit:

- You need private, consistent connectivity between on-premises and Azure.
- The team has strict compliance or data-transfer requirements.
- You need predictable latency and high-throughput performance.
- You want critical traffic kept off the public internet.

Contoso's patient-record sync hits more than one of those. What would we recommend to Contoso, and why? ExpressRoute for that sync. Keep point-to-site for the nurse. Keep site-to-site only if some other traffic is allowed to use an encrypted internet tunnel. One organization can have more than one answer.

A few benefits, one sentence each, then we stop.

ExpressRoute can reach Microsoft cloud services across regions in the geopolitical region. The unit's examples of direct access include Office 365, Dynamics 365, virtual machines, Cosmos DB, and Azure Storage. You are recognizing breadth, not designing Microsoft 365.

Global Reach lets Contoso connect ExpressRoute circuits so on-premises sites can exchange data through Microsoft's network. The unit's example is an office in Asia and a datacenter in Europe. They communicate without transferring that data over the public internet. Say the example. Do not invent a second one.

Dynamic routing uses BGP between the on-premises network and Microsoft. You already met BGP. This is the same protocol name, now on the circuit.

Every peering location has built-in redundancy, and Contoso can add multiple circuits. That is why the unit can say the circuit is highly available, and why the VPN unit can still say a cable cut or a whole location outage is possible. Both statements fit. Built-in redundancy is not immortality. The VPN over the internet remains a valid failover story from the previous unit.

Now the caveat I will not let you skip. Even if Contoso has ExpressRoute, DNS queries, certificate revocation list checking, and Azure Content Delivery Network requests are still sent over the public internet. The circuit is private. It does not swallow every kind of internet dependency. If a test item says "nothing from this environment ever touches the public internet because ExpressRoute is connected," that item is false.

**Analogy.** ExpressRoute is a private road, built with a connectivity provider, from Contoso's gate to Microsoft's gate. The public highway is not part of that drive. A VPN is still the armored car on the public highway. A private road can be faster and calmer than highway traffic. That does not turn the armored car into a private road, and it does not turn the private road into a faster armored car.

**Why an organization would use it.** Private connectivity, predictable latency, high throughput, consistency, compliance or data-transfer rules, and a need to keep specific traffic off the public internet.

**Problem it solves.** Critical on-premises-to-Microsoft traffic no longer depends on the public internet for its path.

**Common confusion.** Calling it a faster VPN. Forgetting the DNS, certificate revocation, and CDN caveat. Using it for a single nurse's laptop. Using it to connect two Azure VNets when peering is the backbone answer. Forgetting that a provider and a circuit are part of the definition.

**AZ-900 exam clue.** Watch for "connectivity provider," "circuit," "does not travel over the public internet," "predictable latency," "high throughput," "compliance," and "consistent." Those are ExpressRoute. Watch for a false absolute: "no traffic of any kind uses the internet." DNS queries, certificate revocation list checks, and Azure CDN requests still do.

**Check for understanding.** Why is "a faster VPN" the wrong definition, even though the unit mentions faster speeds?

**Transition.** Four short scenarios. Answer with the service, then with the constraint that decided it.

## Whiteboard / Visual

```text
VPN Gateway                         ExpressRoute
encrypted tunnel                    private dedicated connection
across the public internet          bypasses the public internet
no provider circuit required        connectivity provider + circuit
nurse, or a site that can           critical site traffic that must
  accept the internet                 stay off the public internet

Still on the internet even with ExpressRoute:
  DNS queries | certificate revocation checks | Azure CDN
```

## Ask the Class

Read each line and wait for a recommendation.

- A billing laptop at a kitchen table needs encrypted access to Azure. What would we recommend to Contoso, and why?
- Headquarters can use the internet if the tunnel is encrypted, and they will not buy a circuit this quarter. What would we recommend, and why?
- Two Azure virtual networks in two regions must stay on the Microsoft backbone. What would we recommend, and why?
- The patient-record sync must avoid the public internet and needs predictable latency. What would we recommend, and why?
- Contoso has ExpressRoute and believes their DNS lookups now avoid the internet. What do you tell them?

## Exam Trap

The most likely wrong answer is site-to-site VPN whenever the stem sounds expensive, important, or "more secure." Encryption is not the same requirement as "does not travel over the public internet." The second trap is believing ExpressRoute privatizes DNS, certificate revocation, and CDN traffic. It does not.

## Transition

Contoso can move packets. They still cannot tell a patient to open `10.1.1.4`. Computers use IP addresses. Humans prefer names. That is DNS.

---

# 6. Describe Azure DNS

## What Microsoft wants students to know

Azure DNS is a hosting service for DNS domains. It provides name resolution using Azure infrastructure. You manage records with the same credentials, APIs, tools, and billing as other Azure services. Benefits in the unit: reliability and performance through global anycast name servers; security through Azure Resource Manager, including RBAC, activity logs, and resource locks; ease of use in the portal, PowerShell, the CLI, and REST or SDKs; private DNS domains so custom names work in a private VNet; alias records that follow an Azure public IP, a Traffic Manager profile, or a CDN endpoint. You cannot buy a domain name with Azure DNS.

## Set the scene

**[1:30]** Contoso bought `contosohealth.org` from a domain registrar last year. The website team wants Microsoft Azure to manage the DNS records. Someone in the room is about to say Azure DNS sells domains. Stop that before it spreads.

## Instructor Talk Track

Computers use IP addresses. Humans prefer names. DNS is the system that turns a name into an address. When a patient types Contoso's website name, some DNS service has to answer with the address of the public endpoint. When a virtual machine inside the VNet looks up the name of an internal system, some DNS service has to answer that too. Those can be related, and they are not the same product decision.

Earlier, in the virtual network unit, Microsoft said you can use Azure's built-in name resolution, or you can point the VNet at an internal or an external DNS server. That is how names work inside the network. This unit is Azure DNS, the hosting service. Do not collapse "the VNet can resolve names" into "Azure DNS registered our domain."

---

### Azure DNS as a hosting service

**Microsoft Learn concept.** Azure DNS hosts DNS domains and provides name resolution using Microsoft Azure infrastructure. Hosting domains in Azure lets you manage DNS records with the same credentials, APIs, tools, and billing as your other Azure services. You cannot use Azure DNS to buy a domain name. For an annual fee you can buy one with App Service domains, or you can buy from a third-party registrar. Once purchased, the domain can be hosted in Azure DNS for record management.

**Plain English.** The registrar sells the name. Azure DNS hosts the records that make the name useful. Contoso already bought the name. They want Azure to run the records. That is Azure DNS.

**Consultant scenario.** "Contoso buys contosohealth.org from a registrar but wants Microsoft Azure to manage the DNS records." What would we recommend to Contoso, and why? Azure DNS. Not a second purchase of the same name, and not a virtual network.

**Instructor talk track.**

Here is the business problem. The name `contosohealth.org` already belongs to Contoso because a registrar sold it to them. The website, and anything else that should answer to that name, needs DNS records: the addresses and related answers for that name. Contoso wants those records managed in Azure, with the same credentials, the same APIs, the same tools, and the same billing relationship as their other Azure services.

That is Azure DNS. It is a hosting service for DNS domains. Name resolution runs on Azure infrastructure.

This is where students often mix up two services. Buying a domain and hosting a domain. I am going to say Microsoft's warning verbatim in plain speech. You cannot use Azure DNS to buy a domain name. You can buy a name, for an annual fee, by using App Service domains, or you can buy it from a third-party registrar. After the purchase, you host the domain in Azure DNS and manage the records there.

So if the stem says "purchase the domain," Azure DNS is the wrong button. App Service domains or a registrar is the purchase. If the stem says "the domain is already purchased; host and manage the records in Azure," Azure DNS is the answer.

Contoso's case is the second one. They bought the name. They want Azure to manage the records. Recommend Azure DNS.

**Analogy.** A registrar is the county office that lets you claim a street name. Azure DNS is the directory service that tells visitors which building number that street name currently means. Owning the name and publishing the directions are two errands. Azure DNS is the second errand.

**Why an organization would use it.** They want their DNS records hosted on Azure and managed with the rest of their Azure estate.

**Problem it solves.** Name resolution and record management have a home in Azure, without pretending Azure DNS is a domain store.

**Common confusion.** Azure DNS sells or registers the domain. It does not. Also, Azure DNS is not a private endpoint and not a VPN. It answers names. It does not carry the patient-record sync.

**AZ-900 exam clue.** "Host the zone," "manage the records," "name resolution using Azure infrastructure" is Azure DNS. "Buy," "purchase," or "register the domain name" is not Azure DNS by itself. The unit's purchase paths are App Service domains, for an annual fee, or a third-party registrar.

**Check for understanding.** Contoso already owns the name and wants the records in Azure. What do you recommend, and what do you tell the person who tries to buy the name again inside Azure DNS?

**Transition.** The unit gives five reasons organizations accept that hosting service. We will treat them as recognition items, not as a configuration class.

---

### What you get when Azure hosts the records

**Microsoft Learn concept.** Reliability and performance: domains are hosted on Azure's global network of DNS name servers; anycast networking means the closest available DNS server answers each query. Security: Azure DNS is based on Azure Resource Manager, which provides RBAC, activity logs, and resource locks. Ease of use: manage records for Azure services and for external resources; the portal uses the same credentials, support contract, and billing; you can also use PowerShell, the CLI, and, for automation, the REST API and SDKs. Private DNS domains: use your own custom domain names in private virtual networks instead of the Azure-provided names. Alias records: an alias record set can refer to an Azure public IP address, a Traffic Manager profile, or a CDN endpoint; if the underlying IP changes, the alias updates itself during DNS resolution because it points at the service instance.

**Plain English.** The answers come from a global, nearby DNS server. Access to the records is controlled with the same Azure management features you will meet again later in this course: roles, logs, and locks. You edit records in the portal or with command-line tools. Inside a VNet you can use your own names. An alias can follow an Azure resource when its address changes.

**Consultant scenario.** Contoso's public site address will change when they rebuild the front end. They do not want a manual DNS edit to be the thing that breaks the name. They also want the internal clinical app to use a Contoso name inside the VNet, not an Azure-generated name. What would we recommend to Contoso, and why? Azure DNS, including an alias record for the public resource that may change, and a private DNS domain for the internal name.

**Instructor talk track.**

I am going to attach each benefit to a Contoso worry, then stop.

Reliability and performance. The domain is hosted on Azure's global network of DNS name servers. Azure DNS uses anycast, which means the closest available DNS server answers the query. Patients in different places are not all waiting on one lonely server Contoso racked in a closet. You do not need to explain anycast beyond "the closest available server answers."

Security, in this unit, means Azure Resource Manager. Because the DNS zone is an Azure resource, you get role-based access control, activity logs, and resource locks. The people who may change `contosohealth.org` can be limited. You can see that a change happened. You can lock the resource against accidental deletion. This is not a network security group. An NSG filters packets. RBAC controls who may manage the DNS resource.

Ease of use. The portal, the same credentials, the same support contract, and the same bill as the rest of Azure. PowerShell and the Azure CLI when they are ready for commands. Applications that must automate DNS can use the REST API and SDKs. You also are not limited to naming Azure resources. The unit says Azure DNS can provide DNS for external resources as well.

Private DNS domains. This is the sentence that connects back to the VNet without mixing up the public website. Azure DNS supports private DNS domains so you can use your own custom names in a private virtual network, instead of the names Azure would otherwise provide. Contoso's internal scheduling app can be a Contoso name inside the clinical VNet. That private name is not automatically the public website name, and it is not a domain purchase.

Alias records. An alias record set refers to an Azure resource, such as a public IP address, a Traffic Manager profile, or a CDN endpoint. If the IP address of the underlying resource changes, the alias updates itself during DNS resolution. It points at the service instance, and the service instance is associated with an address. Contoso's worry — "we will rebuild the public front end and the address will change" — is the reason an alias exists. Recognize the three examples. Do not configure Traffic Manager or a CDN today.

What would we recommend to Contoso, and why? Host `contosohealth.org` in Azure DNS. Use a private DNS domain for internal names inside the VNet. Use an alias where the public Azure resource behind the name may change its address. Buy nothing in Azure DNS. They already bought the name.

**Analogy.** Anycast is asking the nearest information desk instead of phoning one desk on the other coast. A lock on the DNS zone is a lock on the directory book, not a guard on the clinic door. An alias is a directory card that says "ask for the current address of this service," rather than a card with a number copied in pen.

**Why an organization would use it.** They want fast, resilient answers, Azure-native control of who can edit records, their own names inside a VNet, and records that can follow an Azure resource.

**Problem it solves.** Names stay accurate and manageable, in public and in private, without a separate DNS business on the side.

**Common confusion.** Private DNS domain versus private endpoint. A private DNS name lets you call a resource by a custom name inside the VNet. A private endpoint gives a service a private IP from the VNet address space. They are often used in the same design in the real world. This module defines them in different places. Answer the sentence you were asked. Name, or private IP.

**AZ-900 exam clue.** "Closest DNS server" or anycast is the performance benefit. RBAC, activity logs, and resource locks are the security benefit, because Azure DNS uses Azure Resource Manager. "Custom names in a private virtual network" is private DNS, not a domain purchase. "The address changes and the record follows an Azure public IP, Traffic Manager, or CDN endpoint" is an alias record.

**Check for understanding.** Which Azure DNS feature answers each Contoso line: "closest server," "do not let everyone edit the zone," "our own name inside the VNet," "the public IP may change"?

**Transition.** We have a full set of recommendations. I want the class to make them again, in one pass, as if the director just walked in.

## Whiteboard / Visual

```text
Registrar (or App Service domains)   =  buys contosohealth.org
Azure DNS                             =  hosts the records

Public name  -> public endpoint of the website
                (alias if that Azure address may change)

Private DNS domain -> custom name inside the VNet
                      (not a second purchase)

VNet built-in DNS or your own DNS server
    = the earlier unit's name-resolution choice
    = not the same sentence as "buy a domain"
```

## Ask the Class

- Contoso bought the name from a registrar and wants Azure to manage the records. What would we recommend, and why?
- A classmate says Azure DNS is where you purchase `contosohealth.org`. What is the correction, including where a purchase can happen?
- The internal app needs a Contoso name inside the virtual network. Which Azure DNS capability is that?

## Exam Trap

The trap is "Azure DNS" as the answer to "register a new domain name." Hosting is Azure DNS. Purchasing is App Service domains or a third-party registrar, and then you host in Azure DNS. The second trap is answering "Azure DNS" when the stem is really about a private IP for Azure SQL. That private IP is a private endpoint.

## Transition

The module's next unit is the assessment. We will not read Microsoft's questions aloud. We will do our own case review, then a short quiz. After class, each of you should complete the module on Learn, including its assessment.

---

# 7. Consultant case study

## What Microsoft wants students to know

The summary unit says students should now be able to make better connectivity decisions for cloud-only and hybrid scenarios: virtual networking, subnets, public and private endpoints, VPN Gateway, ExpressRoute, Azure DNS, and basic network access.

## Set the scene

**[1:42]** You are in the recommendation meeting. The director does not want a vocabulary list. The director wants a decision and a reason. Ask the class before you confirm each line.

## Instructor Talk Track

I am going to read Contoso's requirements the way a client would actually say them. You answer with the Azure concept and one reason. If you answer with a product that is "also private" or "also secure," I am going to ask you which constraint you ignored.

**What would we recommend to Contoso, and why?**

Contoso needs a private network space in Azure for the clinical systems.
Recommend a virtual network. That is the isolated space. A VPN is only a tunnel into a space that must already exist.

They need the web servers divided from the database servers.
Recommend subnets. Same VNet, separate named slices of the address space. A second VNet would isolate them so hard that you would then need peering to let them talk. They asked to divide, not to build a second network.

Patients on the internet must reach the website.
Recommend a public endpoint: a public IP, or a public load balancer in front of the site. Then an NSG so "public" does not mean "every port."

The Azure SQL database must be reached on a private IP from the VNet's address space.
Recommend a private endpoint. Not a public IP, and not the service-endpoint sentence.

The storage account must be linked to the virtual network for security and optimal routing.
Recommend a service endpoint. The unit names storage, and it names that purpose. If someone says private endpoint, ask them where the private IP requirement was. It was not in this sentence.

Only HTTPS from the internet should reach the web subnet, and the data subnet should not accept internet inbound.
Recommend network security group rules. Inbound and outbound, allow or block, by address, port, and protocol. A route does not allow or block. It steers.

They might later want a specialized virtual machine that runs a firewall function or WAN optimization.
Recognize a network virtual appliance. Do not call the NSG an appliance.

The research VNet, in another region, must talk to the clinical VNet with traffic staying on the Microsoft backbone.
Recommend virtual network peering. Not a VPN. A VPN between those VNets would cross the internet inside a tunnel. They asked for the backbone.

A nurse's laptop must open an encrypted connection into Azure.
Recommend point-to-site VPN. The client initiates it. One device is not a site.

Headquarters has a VPN device. Encrypted connectivity is enough, and they are not buying a private circuit for this traffic.
Recommend site-to-site VPN, route-based, because sites will be added and subnets will change. One VPN gateway in the VNet can serve more than one location.

The patient-record sync must stay off the public internet, with predictable latency and high throughput, because of compliance.
Recommend ExpressRoute, through a connectivity provider, as a circuit. Not a faster VPN. A private path that bypasses the public internet. Remind the room that DNS queries, certificate checks, and CDN requests still use the internet.

They already bought `contosohealth.org` and want Azure to manage the records, including a name that can follow a changing public IP, and a custom name inside the VNet.
Recommend Azure DNS. Hosting, not purchasing. An alias record for the changing Azure address. A private DNS domain for the internal name.

If they later fear an ExpressRoute location outage, the VPN over the internet can be the secure failover. That does not redefine ExpressRoute. It backs it up.

That is the engagement. Every recommendation came from a constraint. If you remember the constraint, you will remember the service.

## Whiteboard / Visual

Leave the earlier drawings up. Add only the recommendation words next to each Contoso line. Do not draw a new architecture.

## Ask the Class

- Which recommendation changes if the compliance lead withdraws the "no public internet" rule and accepts encryption instead?
- Which recommendation changes if the database requirement drops the words "private IP from our address space" and becomes "link it for optimal routing"?
- Which recommendation is wrong if someone peers the nurse's laptop to Azure?

## Exam Trap

The case study fails when students pick the most expensive private option every time. Make them quote the constraint before they quote the service.

## Transition

Ten minutes from now you will close. Use the exit quiz in this guide. Assign the Microsoft Learn module assessment as homework. Do not project Microsoft's items in the room.

---

# 8. Module assessment and summary

## What Microsoft wants students to know

The summary restates the same objectives: virtual networking including subnets and endpoints, VPN Gateway connectivity options, when to use ExpressRoute, Azure DNS, and basic network access. The summary's wording of the last objective is "configure." Your close is still "describe and recognize."

## Set the scene

**[1:52]** You have eight minutes. Five of them belong to the exit quiz. Three belong to the ten sentences you want remembered on the way out.

## Instructor Talk Track

Microsoft's module ends with an assessment and a short summary. Complete that assessment on Learn after class, signed in, so the module is actually finished. I am not going to use their questions as our quiz. You should see those questions fresh.

Here is the summary I would say to Contoso's director, and it is the summary I want you to leave with.

We gave you a private network in Azure and we segmented it. We chose public doors and private addresses on purpose. We separated steering traffic from allowing traffic. We joined a second Azure network on Microsoft's backbone. We used encrypted internet tunnels for people and for sites that can accept the internet. We used a private circuit only where the internet itself is unacceptable. We hosted the names you had already bought. None of those are the same decision.

## If you remember only 10 things

1. A virtual network is Contoso's isolated private network in Azure. Its address space exists only inside that VNet and is not internet-routable.
2. A subnet is a named slice of that address space. Dividing web servers from database servers is a subnet decision.
3. A public endpoint has a public IP and can be reached from anywhere. Inbound internet access is a public IP or a public load balancer.
4. A private endpoint exists inside the VNet and has a private IP from that VNet's address space.
5. A service endpoint links resource types such as Azure SQL and storage to the VNet for security and optimal routing. That sentence is not the private-IP sentence.
6. A route steers. A network security group allows or blocks by source, destination, port, and protocol, inbound or outbound. A network virtual appliance is a specialized VM, such as a firewall function or WAN optimization.
7. VNet peering connects two virtual networks directly. Traffic stays on the Microsoft backbone, never enters the public internet, and the VNets may be in different regions.
8. A VPN is an encrypted tunnel across an untrusted network, typically the public internet. Point-to-site is a device. Site-to-site is an on-premises network. Network-to-network VPN also crosses the internet. One VPN gateway per VNet can serve many locations. Prefer route-based when subnets change, for point-to-site, for multisite, for VNet-to-VNet VPN, and for ExpressRoute coexistence.
9. ExpressRoute is a private connection from a connectivity provider, called a circuit. It does not travel over the public internet. It is not "a faster VPN." DNS queries, certificate revocation checks, and Azure CDN requests still use the public internet. A VPN can be the failover path.
10. Azure DNS hosts and manages DNS records, including private names in a VNet and alias records. It does not sell or register the domain name. Buy the name from a registrar or with App Service domains, then host it in Azure DNS.

## Rapid-fire instructor questions

Ask these verbally. Accept the concept name and one constraint. Do not open a debate.

1. What is the difference between a VNet and a subnet?
2. Which endpoint has a public IP that can be reached from anywhere?
3. Which endpoint uses a private IP from the VNet address space?
4. Which feature does the unit name for linking storage or Azure SQL to a VNet for security and optimal routing?
5. What does an NSG look at when it allows or blocks?
6. Two Azure VNets, traffic must stay off the public internet. What do you recommend?
7. A laptop initiates an encrypted connection. Which VPN?
8. An on-premises VPN device, encrypted over the internet. Which VPN?
9. Critical traffic must not use the public internet, and latency must be predictable. What do you recommend?
10. The company already bought the domain and wants Azure to manage the records. What do you recommend, and what will Azure DNS refuse to do?

## Exit quiz

Ten original questions. They are not the Microsoft module assessment and not the course file `quizzes/session-05-quiz.md`. Use them in the last minutes, or as the door quiz if the case study ran long.

**1.** Contoso Health places patient-portal virtual machines and database virtual machines in one Azure network. The security lead wants those two groups in different parts of the address space so rules can be applied separately. Which recommendation fits?

- A. A second VPN gateway
- B. A subnet for each group
- C. Azure DNS alias records
- D. ExpressRoute Global Reach

**Answer:** B.

**Why correct:** The virtual networking unit says you divide the VNet address space into named subnets and allocate part of the space to each subnet. Separate parts of one network are subnets.

**Why the others are wrong:** A second VPN gateway does not segment address space, and the unit allows only one VPN gateway per VNet. Alias records follow a changing Azure address; they do not segment a network. Global Reach connects on-premises sites through ExpressRoute circuits; it does not divide a VNet.

**Source:** [Describe Azure virtual networking](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/2-virtual-network)

**2.** Patients who are not on Contoso's network must open the public website from the internet. Which capability matches that requirement?

- A. A private endpoint
- B. A public endpoint, using a public IP or a public load balancer
- C. Virtual network peering
- D. A private DNS domain

**Answer:** B.

**Why correct:** Public endpoints have a public IP and can be accessed from anywhere. The same unit says incoming internet connections are enabled with a public IP or a public load balancer.

**Why the others are wrong:** A private endpoint uses a private IP from the VNet address space, which internet patients do not have a route to. Peering connects virtual networks to each other. A private DNS domain supplies custom names inside a private VNet; it does not publish the site to the internet.

**Source:** [Describe Azure virtual networking](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/2-virtual-network)

**3.** Contoso wants Azure SQL reachable from the clinical virtual network on a private IP address that comes from that virtual network's address space. Which choice matches the requirement as stated?

- A. A public endpoint
- B. A service endpoint
- C. A private endpoint
- D. A user-defined route

**Answer:** C.

**Why correct:** The unit defines a private endpoint as existing within a virtual network and having a private IP from that virtual network's address space.

**Why the others are wrong:** A public endpoint is a public IP reachable from anywhere, which is the opposite address type. A service endpoint is how the unit describes linking SQL or storage to a VNet for security and optimal routing; this stem asked for a private IP from the VNet address space, which is the private-endpoint definition. A user-defined route steers packets; it does not give SQL a private address.

**Source:** [Describe Azure virtual networking](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/2-virtual-network)

**4.** Contoso wants the storage account linked to the clinical virtual network to improve security and provide optimal routing. The request does not ask for a new private IP from the VNet address space. Which feature matches the unit's description?

- A. Service endpoint
- B. Site-to-site VPN
- C. ExpressRoute
- D. Network security group

**Answer:** A.

**Why correct:** The unit says service endpoints connect to Azure resource types such as Azure SQL databases and storage accounts, linking them to virtual networks for security and optimal routing.

**Why the others are wrong:** Site-to-site VPN links an on-premises VPN device to Azure over the internet. ExpressRoute is a provider's private circuit and is not how this unit describes linking a storage account. An NSG allows or blocks by address, port, and protocol; it is not the linking feature named for storage.

**Source:** [Describe Azure virtual networking](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/2-virtual-network)

**5.** Contoso's web subnet may receive HTTPS from the internet. The database subnet must not. Traffic that is not allowed should be blocked. Which feature matches?

- A. A route table
- B. A network security group
- C. VNet peering
- D. An alias record

**Answer:** B.

**Why correct:** Network security groups contain inbound and outbound rules that allow or block traffic based on source and destination IP address, port, and protocol.

**Why the others are wrong:** A route table directs how packets are routed; it does not allow or block them. Peering connects two virtual networks; it is not a port filter. An alias record updates a DNS answer when an Azure resource's address changes.

**Source:** [Describe Azure virtual networking](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/2-virtual-network)

**6.** A radiologist working from home must initiate an encrypted connection from a laptop into the Azure virtual network. Contoso will not install a site VPN device at the home. Which option fits?

- A. Point-to-site VPN
- B. ExpressRoute
- C. VNet peering
- D. A public endpoint on the database

**Answer:** A.

**Why correct:** Point-to-site connects an individual device. The client computer initiates an encrypted VPN into the virtual network.

**Why the others are wrong:** ExpressRoute is a provider circuit for a location, not a laptop, and it is not an encrypted internet tunnel. Peering joins two virtual networks, and the laptop is not a VNet. A public endpoint on the database would expose a public IP, which is not an encrypted client VPN.

**Source:** [Describe Azure virtual private networks](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/3-virtual-private-networks) and the on-premises methods in [Describe Azure virtual networking](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/2-virtual-network)

**7.** Contoso headquarters has an on-premises VPN device. The clinic accepts an encrypted connection that works over the internet, and Azure resources should be able to appear local. A private circuit is not required. Which option fits?

- A. Site-to-site VPN
- B. Point-to-site VPN
- C. ExpressRoute
- D. A network virtual appliance

**Answer:** A.

**Why correct:** Site-to-site links an on-premises VPN device or gateway to the Azure VPN gateway. The connection is encrypted and works over the internet, and devices in Azure can appear local.

**Why the others are wrong:** Point-to-site is for an individual device that initiates the VPN, not for a site device representing headquarters. ExpressRoute does not travel over the public internet, and this stem says the internet path is acceptable and a private circuit is not required. A network virtual appliance is a specialized VM that performs a network function; it is not the site-to-site tunnel.

**Source:** [Describe Azure virtual networking](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/2-virtual-network) and [Describe Azure virtual private networks](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/3-virtual-private-networks)

**8.** Contoso will add subnets several times this year, must support nurses with point-to-site access, and may later run the VPN alongside an ExpressRoute gateway. Which VPN gateway type does the unit tell you to use?

- A. Policy-based
- B. Route-based
- C. Neither type can coexist with ExpressRoute
- D. A public load balancer

**Answer:** B.

**Why correct:** Route-based VPNs are preferred for on-premises devices and are more resilient to topology changes such as new subnets. The unit says to use route-based for point-to-site, multisite, connections between virtual networks, and coexistence with an ExpressRoute gateway.

**Why the others are wrong:** Policy-based gateways statically list the addresses to encrypt and evaluate each packet against that list; they are not the resilient choice for new subnets. The unit explicitly lists coexistence with an ExpressRoute gateway as a route-based case, so "neither type can coexist" is false. A public load balancer enables inbound internet connections; it is not a VPN type.

**Source:** [Describe Azure virtual private networks](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/3-virtual-private-networks)

**9.** Contoso's compliance team requires the headquarters patient-record transfer into Azure to use private, consistent connectivity that does not travel over the public internet, with predictable latency and high throughput. Which recommendation fits?

- A. Site-to-site VPN, because it is a faster private circuit
- B. ExpressRoute
- C. VNet peering from headquarters into Azure
- D. Azure DNS

**Answer:** B.

**Why correct:** ExpressRoute extends the on-premises network over a private connection with a connectivity provider. Connections do not go over the public internet. The unit says to choose it for private consistent connectivity, strict compliance or data-transfer requirements, predictable latency and high throughput, and to avoid the public internet for critical traffic.

**Why the others are wrong:** Site-to-site VPN is encrypted and works over the internet. It is not a private circuit, and "faster VPN" is the wrong description of ExpressRoute. Peering connects two Azure virtual networks; headquarters is on-premises, not a VNet. Azure DNS hosts name records; it does not carry the data transfer.

**Source:** [Describe Azure ExpressRoute](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/4-expressroute)

**10.** Contoso bought `contosohealth.org` from a third-party registrar. The team wants Azure to host the DNS records, limit who can edit them, and keep a record aligned if the website's Azure public IP changes. They also believe ExpressRoute will stop DNS queries from using the public internet. Which statement is accurate?

- A. Buy the domain again in Azure DNS, and ExpressRoute will carry the DNS queries
- B. Host the domain in Azure DNS, control it with Azure RBAC and resource locks, use an alias record for the public IP, and expect DNS queries to use the public internet even when ExpressRoute is in place
- C. Use a network security group as the DNS host
- D. Use point-to-site VPN to register the domain name

**Answer:** B.

**Why correct:** Azure DNS hosts domains and cannot sell the name. Because it uses Azure Resource Manager, it has RBAC, activity logs, and resource locks. An alias record set can refer to an Azure public IP and updates during resolution if that address changes. The ExpressRoute unit says DNS queries are still sent over the public internet.

**Why the others are wrong:** Azure DNS is not where you buy the domain, and ExpressRoute does not pull DNS queries off the internet. An NSG filters traffic by address, port, and protocol; it is not a DNS hosting service. Point-to-site VPN connects a device; it does not register a domain name.

**Source:** [Describe Azure DNS](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/5-domain-name-system) and [Describe Azure ExpressRoute](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/4-expressroute)

---

## Service recognition table

| Business requirement | Azure concept / service | Why | Common wrong answer |
| --- | --- | --- | --- |
| Own isolated private network in Azure for resources that must communicate | Virtual network | Isolation and segmentation; the space where Azure, internet, and on-premises communication is designed | ExpressRoute, which connects an on-premises site and does not replace the VNet |
| Divide web servers from database servers inside that network | Subnet | Named part of the VNet address space | A second VNet, or an NSG (the NSG filters; it does not create the segment) |
| Patients on the internet must reach the website | Public endpoint | Public IP, reachable from anywhere; inbound internet via public IP or public load balancer | Private endpoint, which has no public street address |
| Azure SQL must use a private IP from the VNet address space | Private endpoint | The unit's definition: inside the VNet, private IP from that address space | Service endpoint, when the stem actually requires the private IP |
| Link storage or Azure SQL to the VNet for security and optimal routing | Service endpoint | The unit's purpose and examples for service endpoints | Private endpoint, when the stem does not require a private IP from the VNet |
| Allow or block by address, port, and protocol, inbound or outbound | Network security group | The unit's filtering resource | A route table, which steers and does not allow or block |
| Two Azure VNets, including across regions, traffic on the Microsoft backbone and not the public internet | VNet peering | Direct private connectivity on the backbone | Site-to-site or network-to-network VPN, which crosses the internet inside a tunnel |
| One remote laptop initiates an encrypted connection | Point-to-site VPN | Individual device; client initiates the encrypted VPN | Site-to-site, which expects an on-premises VPN device |
| Headquarters VPN device, encrypted over the internet, Azure can appear local | Site-to-site VPN | On-premises device or gateway to Azure VPN Gateway, over the internet | ExpressRoute, if the stem still accepts the internet and does not ask for a private circuit |
| Private, predictable, high-throughput path that does not travel the public internet, often for compliance | ExpressRoute | Provider-backed circuit that bypasses the public internet | "A faster VPN." A VPN still uses the internet |
| Domain already purchased; Azure should host and manage the records | Azure DNS | Hosting and name resolution on Azure. Does not sell the name | Using Azure DNS to buy or register the domain |

---

# Supplemental instructor context

Do not teach this section as part of the module. Use it only when a student asks, or when you need to stop a wrong product name. Say that you are stepping outside the module, then come back.

**Private endpoint versus service endpoint, beyond the unit.** The virtual networking unit defines a private endpoint as a private IP from the VNet address space, and a service endpoint as a way to link services such as Azure SQL and storage for security and optimal routing. It does not describe the platform mechanics. Current service-endpoint documentation, outside this module, says service endpoints extend the virtual network's identity to the service, send that service traffic over the Azure backbone, and switch the source address of that traffic to the subnet's private addresses. The same page says DNS entries for those services still resolve to the public IP addresses of the service. It also says Microsoft recommends Azure Private Link and private endpoints when you want private access: Private Link places a network interface in your virtual network for services such as Storage or Azure SQL. If a student asks how the mechanisms differ, you may say that, and you must label it as documentation beyond the module. For the exam, stay with the unit's wording. Do not teach "always choose a private endpoint" as an AZ-900 rule. Source: [Azure virtual network service endpoints](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview).

**Azure Firewall.** Azure Firewall is not a topic in this module. If a student offers it as the answer to an allow-or-block question, say: "Azure Firewall is a separate managed firewall product. This module's rule resource is the network security group. This module's specialized virtual machine for a firewall function is the network virtual appliance." Then return to the NSG.

**Office 365 and Microsoft 365.** The ExpressRoute unit says you can connect to services such as Microsoft Azure and Microsoft 365, and the direct-access list still says Microsoft Office 365. Use the unit's names in class. Do not spend time on the branding history.

**"Configure" versus "describe."** The module home page says "Describe basic network access controls for Azure resources." The introduction and summary say "Configure basic network access for an Azure resource." This session teaches recognition of NSG allow and block rules. It does not include a configuration lab. The course lab file remains available if you add practice on another day.

**Forcing traffic through a network virtual appliance.** Production designs often put a user-defined route on a route table so traffic is steered at a network virtual appliance. This module presents route tables, user-defined routes, and network virtual appliances as separate capabilities. It does not spell out that pairing. If you mention it, call it a common way the two ideas are used together, not a module requirement.

**Gateway subnet name.** The VPN unit says the gateway is deployed in a dedicated subnet. It does not spend time on the subnet's name. Do not make the name an exam fact in this session.

---

## Sources

Every recommendation in the main script is taken from these pages. Checked 9 October 2026.

- [Module: Describe Azure networking services](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/)
- [Introduction](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/1-introduction)
- [Describe Azure virtual networking](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/2-virtual-network)
- [Describe Azure virtual private networks](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/3-virtual-private-networks)
- [Describe Azure ExpressRoute](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/4-expressroute)
- [Describe Azure DNS](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/5-domain-name-system)
- [Summary](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/7-summary)
