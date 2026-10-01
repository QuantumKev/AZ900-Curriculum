# Session 5 slides — Azure Networking

Each `##` heading is one slide. Notes: [session-05-instructor-notes.md](session-05-instructor-notes.md).

## 1. Azure networking

Session 5. How resources talk, how you keep traffic in bounds, and how a private datacenter meets Azure.

## 2. Virtual networks

An Azure virtual network is a private network in a region. Resources inside it can talk. The internet does not get in unless you allow it.

You pick a private address range. You split it into **subnets**. A subnet is a segment of that range, and a place to attach rules.

## 3. What a virtual network is for

- Isolate your resources from other people's.
- Segment one network into subnets.
- Give resources private addresses.
- Control inbound and outbound traffic.
- Let Azure resources reach each other privately.

## 4. Traffic rules

**Network security group.** A filter on a subnet or a network interface. Rules allow or deny traffic by direction, port, and address. This is a filter, not a route.

**Route table and user-defined routes.** Change where packets go. Use this when the default path is wrong. Routing is not the same job as filtering.

## 5. Connecting networks

**Virtual network peering.** Two virtual networks talk privately over Microsoft's backbone, not out across the public internet. They can be in different regions.

**Azure DNS.** Hosts your DNS domain on Azure's name servers, or resolves names inside a virtual network.

## 6. Connecting to somewhere else

**Point-to-site VPN.** One computer connects in to the virtual network.

**Site-to-site VPN.** A whole on-premises network connects, through a VPN device, to an **Azure VPN Gateway**. Traffic is encrypted over the public internet.

**ExpressRoute.** A private connection from your network to Microsoft. It does not travel over the public internet. Choose it when the requirement says private connectivity, not "a VPN."

## 7. Which connection

One laptop from a café: point-to-site.

A branch office network, encryption over the internet is acceptable: site-to-site VPN.

Two Azure virtual networks: peering. Do not put a VPN in the middle if peering is enough.

Private circuit, not the internet: ExpressRoute.

## 8. Three endpoints — do not merge them

**Public endpoint.** A public IP. Reachable from the internet, if filters allow.

**Private endpoint.** A network interface in your virtual network, with a private IP, in front of a specific PaaS resource. That resource is reached on your private address. This is the Private Link idea.

**Service endpoint.** A different, older path: it extends your virtual network's identity to the service over the Microsoft backbone, but the service is still reached on its public address. It is not a private IP in your subnet.

Public means internet-reachable. Private endpoint means a private IP in your network. Service endpoint is not a private endpoint.

## 9. Lab and quiz

Create a virtual network with two subnets in Cloud Shell, then find it in the portal.

Then label nine descriptions: public endpoint, private endpoint, or service endpoint.

No Azure account: you will trace the same commands against the docs and still do the nine labels.

Assignment: [Describe Azure networking services](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/).
