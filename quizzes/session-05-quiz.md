# Session 5 Quiz — Azure Networking

**Time:** 15 minutes · **Items:** 12 · **Composition:** 9 new, 3 carry-forward (S1–S4)
**Objectives:** 2.2.5, 2.2.6
**Carry-forward objectives:** 1.1.4, 2.1.1, 2.2.2
**Target:** 80%

Only two objectives, assessed in depth. Networking is where beginner cohorts lose the most
marks, and the endpoint item set targets a known confusion (gap G4).

---

## Questions

**1.** What is the primary purpose of an Azure virtual network?

- A. To store unstructured data accessible over HTTP
- B. To let Azure resources communicate with each other, with the internet, and with on-premises networks
- C. To replicate data across region pairs
- D. To assign role-based permissions to users

**2.** A team needs two virtual networks in different Azure regions to communicate privately, with traffic staying on the Microsoft backbone rather than crossing the public internet. What should they configure?

- A. A site-to-site VPN
- B. Virtual network peering
- C. A private endpoint
- D. Azure DNS

**3.** An employee working from a home office needs an encrypted connection from their laptop into an Azure virtual network. Which connectivity option is this?

- A. Site-to-site VPN
- B. Point-to-site VPN
- C. ExpressRoute
- D. Virtual network peering

**4.** An organization requires a dedicated private connection between its datacenter and Azure that does not travel over the public internet, with predictable latency and high throughput. Which option meets this?

- A. Site-to-site VPN over the internet
- B. Azure ExpressRoute
- C. Point-to-site VPN
- D. Network security groups

**5.** Which statements about Azure VPN Gateway are correct? (Select all that apply.)

- A. You can deploy only one VPN gateway per virtual network
- B. One VPN gateway can connect to multiple locations
- C. VPN gateways are deployed by default as two instances in an active/standby configuration
- D. VPN gateway traffic is unencrypted because it uses the Microsoft backbone
- E. A VPN gateway can serve as a failover path for an ExpressRoute connection

**6.** Which statement about Azure DNS is correct?

- A. You can purchase domain names directly in Azure DNS
- B. Azure DNS hosts DNS domains and provides name resolution, and supports private DNS zones for virtual networks
- C. Azure DNS replaces the need for public IP addresses
- D. Azure DNS is only available in sovereign regions

**7.** What is the defining characteristic of a private endpoint?

- A. It has a public IP address reachable from anywhere in the world
- B. It exists within a virtual network and uses a private IP address from that network's address space
- C. It encrypts all traffic between two virtual networks
- D. It is a firewall rule applied at the subnet level

**8.** (For each statement, answer yes or no.)

- i. A public endpoint has a public IP address and can be accessed from anywhere in the world.
- ii. A private endpoint uses a private IP address from the virtual network's address space.
- iii. Adding a private endpoint automatically removes all public access to every resource in the subscription.

**9.** A team wants to restrict inbound traffic to a subnet so that only HTTPS from a specific address range is allowed. Which capability of Azure virtual networking handles this?

- A. Virtual network peering
- B. Network security groups
- C. Azure DNS alias records
- D. ExpressRoute Global Reach

**10.** *(Carry-forward)* An organization wants to keep a regulated database on infrastructure it controls while running a public-facing application in Azure, with the two connected. Which cloud model is this, and which Azure connectivity option would support it?

- A. Public cloud; virtual network peering
- B. Hybrid cloud; site-to-site VPN or ExpressRoute
- C. Private cloud; point-to-site VPN
- D. Multicloud; Azure DNS

**11.** *(Carry-forward)* A design requires that a workload survive the loss of one datacenter inside a single Azure region. Which capability should the design use?

- A. Region pairs
- B. Availability zones
- C. Sovereign regions
- D. Virtual network peering

**12.** *(Carry-forward)* Which option provides resiliency for a group of virtual machines against a single hardware failure or planned maintenance event within a region, at no additional charge for the grouping itself?

- A. An availability set
- B. A second subscription
- C. A public endpoint
- D. Azure Data Box

---

## Answer key

| Q | Answer | Objective | Why | Source |
| --- | --- | --- | --- | --- |
| 1 | B | 2.2.5 | Virtual networks enable communication between Azure resources, with the internet, and with on-premises clients, and provide isolation, segmentation, routing, and filtering. | [Azure virtual networking](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/2-virtual-network) |
| 2 | B | 2.2.5 | Peering connects virtual networks directly; traffic stays private on the Microsoft backbone and never enters the public internet. Peered networks can be in separate regions. | [Azure virtual networking](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/2-virtual-network) · [VNet peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-peering-overview) |
| 3 | B | 2.2.5 | Point-to-site connects an individual device from outside the environment into the virtual network. Site-to-site connects a whole on-premises network through a VPN device or gateway. | [Azure virtual private networks](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/3-virtual-private-networks) |
| 4 | B | 2.2.5 | ExpressRoute provides dedicated private connectivity that bypasses the public internet, with more reliability, faster speeds, and consistent latency. Note that DNS queries, certificate revocation checks, and CDN requests still traverse the internet. | [Azure ExpressRoute](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/4-expressroute) |
| 5 | A, B, C, E | 2.2.5 | One VPN gateway per virtual network, but it can serve multiple locations; the default deployment is two instances in active/standby; and a VPN gateway can back up an ExpressRoute circuit. D is false — VPN traffic is encrypted inside a tunnel across the internet. | [Azure virtual private networks](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/3-virtual-private-networks) |
| 6 | B | 2.2.5 | Azure DNS hosts domains, resolves names on Microsoft's anycast network, and supports private DNS zones plus alias records. You cannot buy a domain name in Azure DNS — that requires App Service domains or a registrar. | [Azure DNS](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/5-domain-name-system) |
| 7 | B | 2.2.6 | A private endpoint lives inside a virtual network with a private IP from that network's address space. A describes a public endpoint. | [Azure virtual networking](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/2-virtual-network) · [Private endpoints](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview) |
| 8 | i–yes, ii–yes, iii–no | 2.2.6 | The first two restate the definitions. The third is false: a private endpoint applies to the resource it is created for and does not change public access across a subscription. Score one point per statement. | [Azure virtual networking](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/2-virtual-network) |
| 9 | B | 2.2.5 | Network security groups contain inbound and outbound rules that allow or block traffic by source and destination address, port, and protocol. Peering connects networks; it does not filter. | [Azure virtual networking](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/2-virtual-network) |
| 10 | B | 1.1.4 (carry-forward) | Private infrastructure plus Azure, interconnected, is hybrid; site-to-site VPN or ExpressRoute are the two ways to link on-premises networks to a virtual network. | [Define cloud models](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/5-define-cloud-models) · [Azure virtual networking](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/2-virtual-network) |
| 11 | B | 2.1.1 (carry-forward) | Availability zones are the in-region protection against a datacenter-level failure. Region pairs protect against the loss of a whole region. | [Azure physical infrastructure](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/5-describe-azure-physical-infrastructure) |
| 12 | A | 2.2.2 (carry-forward) | Availability sets spread VMs across update and fault domains and add no cost for the set itself — you pay for the VM instances. In zone-enabled regions, zone-based designs are often preferred because they isolate larger failures. | [Azure virtual machines](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/2-virtual-machines) |

**Instructor note on items 7–8:** the same unit that defines public and private endpoints
also mentions service endpoints, which connect Azure service types such as Azure SQL and
storage accounts to a virtual network. If a learner offers "service endpoint" for item 7,
use it to draw the three-way distinction rather than marking it simply wrong.
