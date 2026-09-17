# Session 5 Quiz — Azure Networking

**Name:** <span class="blank"></span>  **Session:** <span class="blank"></span>

**Time:** 15 minutes · **Items:** 12 · **Target:** 80%

Answer every question. For *select all that apply*, mark every correct option. For
matching questions, write the matching term next to each numeral. For yes/no sets,
write yes or no next to each numeral. Your instructor reviews every answer in class
immediately afterward.

---

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

- i. A public endpoint has a public IP address and can be accessed from anywhere in the world. &nbsp; <span class="blank"></span>
- ii. A private endpoint uses a private IP address from the virtual network's address space. &nbsp; <span class="blank"></span>
- iii. Adding a private endpoint automatically removes all public access to every resource in the subscription. &nbsp; <span class="blank"></span>

**9.** A team wants to restrict inbound traffic to a subnet so that only HTTPS from a specific address range is allowed. Which capability of Azure virtual networking handles this?

- A. Virtual network peering
- B. Network security groups
- C. Azure DNS alias records
- D. ExpressRoute Global Reach

**10.** An organization wants to keep a regulated database on infrastructure it controls while running a public-facing application in Azure, with the two connected. Which cloud model is this, and which Azure connectivity option would support it?

- A. Public cloud; virtual network peering
- B. Hybrid cloud; site-to-site VPN or ExpressRoute
- C. Private cloud; point-to-site VPN
- D. Multicloud; Azure DNS

**11.** A design requires that a workload survive the loss of one datacenter inside a single Azure region. Which capability should the design use?

- A. Region pairs
- B. Availability zones
- C. Sovereign regions
- D. Virtual network peering

**12.** Which option provides resiliency for a group of virtual machines against a single hardware failure or planned maintenance event within a region, at no additional charge for the grouping itself?

- A. An availability set
- B. A second subscription
- C. A public endpoint
- D. Azure Data Box

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
