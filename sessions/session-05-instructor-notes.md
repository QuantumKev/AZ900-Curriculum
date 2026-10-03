# Session 5 instructor notes — Azure Networking

**Objectives:** 2.2.5, 2.2.6
**Also practiced:** 3.3.2 (Cloud Shell and Azure CLI)
**Slides:** [session-05-slides.md](session-05-slides.md)
**Lab:** [../labs/session-05-lab.md](../labs/session-05-lab.md)
**Quiz:** [../quizzes/session-05-quiz.md](../quizzes/session-05-quiz.md)
**Warm-up:** Session 5 set, weighted to cloud models (setup for hybrid connectivity) and compute types
**Domain minutes:** Domain 1 — 5, Domain 2 — 95, Domain 3 — 20

## Run of show

| Min | Block | Leave it when |
| --- | --- | --- |
| 0–10 | Warm-up | Hybrid is a model they can define again; VM vs container vs function is still available |
| 10–35 | VNets, subnets, NSGs, routes | They can say a subnet segments a VNet, and an NSG filters while a route steers |
| 35–60 | Peering, DNS, VPN, ExpressRoute | Point-to-site, site-to-site, peering, and ExpressRoute each have a "when" |
| 60–75 | Endpoints | Public, private, and service endpoint are three answers, not two |
| 75–105 | Lab | VNet exists or the commands were traced. Nine labels done |
| 105–120 | Quiz | Reviewed |

Gap G4 is the endpoint block. Do not fold it into the VNet lecture. It has its own 15 minutes because the official unit gives it a short paragraph and learners merge service endpoints with private endpoints.

## Teach A

Virtual network: private address space in a region, isolation, segmentation. Subnet: a slice of that space. Resources land in a subnet.

Say what they get: private addresses, a boundary, a way for Azure resources to talk, and a place to decide whether internet inbound or outbound is allowed. Do not draw a production hub-and-spoke. One VNet, two subnets, is the whole picture.

Network security group: allow or deny. Route table / user-defined route: where the packet is sent. Put both on the board as verbs. Filter. Steer. The exam uses both, and beginners call every rule a firewall.

## Teach B

Peering: VNet to VNet, Microsoft backbone, not a VPN you have to build. Cross-region peering exists. You do not hairpin peering traffic through a VPN gateway to "make it private." It is already private.

Azure DNS: hosting a public DNS zone, or private name resolution for a VNet. One sentence plus the name. Do not configure a zone unless the demo is already rehearsed.

VPN Gateway:

- Point-to-site — one client computer.
- Site-to-site — site to site, a network on each end, encrypted over the internet.

ExpressRoute: private, not the public internet. Higher commitment, used when "over the internet" is the wrong design. Hybrid from Session 1 is the scenario: on-premises private cloud or datacenter connected to Azure.

Decision order, say it as a script they can reuse:

1. Both ends already in Azure? Peering.
2. One computer? Point-to-site.
3. A site, and the internet is acceptable? Site-to-site.
4. The internet is not acceptable? ExpressRoute.

## Teach C — endpoints (G4)

Public endpoint: public IP, internet can reach it if you allow that.

Private endpoint: a NIC in your subnet, private IP, mapped to one PaaS resource (a storage account, a database). Users in the VNet use the private address. You can refuse the public path.

Service endpoint: traffic to the service goes over the backbone from the VNet, and you can lock the service to accept that VNet, but the destination address is still the service's public endpoint. There is no private IP in your subnet.

The discrimination exercise is the teaching. Do not add Private Link SKUs or DNS zone design.

## Lab

Cloud Shell is the first real use of 3.3.2. If Cloud Shell setup wants a storage account and that stalls the room, switch everyone to the no-cost trace. A stuck storage-account create is not the objective.

Peering and DNS stay an instructor demo of the portal blades, two minutes, or a screenshot. Do not have twenty people peer networks.

## If you are short on time

Shorten Azure DNS to the definition. Keep ExpressRoute vs VPN. Keep the nine endpoint labels. Keep the quiz.

## Sources

[Networking module](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/) · [Virtual Network](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview) · [Peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-peering-overview) · [Azure DNS](https://learn.microsoft.com/en-us/azure/dns/dns-overview) · [VPN Gateway](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpngateways) · [ExpressRoute](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction) · [Private endpoints](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)
