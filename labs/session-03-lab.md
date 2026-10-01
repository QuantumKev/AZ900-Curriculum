# Session 3 lab — Geography vocabulary, resource group, hierarchy

**Time:** 30 minutes
**Objectives practiced:** 2.1.1–2.1.7, and a second look at the portal (3.3.1)
**You need:** this sheet. Parts A and C need no subscription. Part B needs an Azure account, or the no-cost stop point.

---

## Part A — Name the scope (10 minutes)

Write one of: **datacenter**, **region**, **availability zone**, **region pair**, **sovereign region**.

1. A physical facility with its own power and security staff.
2. A group of datacenters in a latency-defined area. You select it when creating a virtual machine.
3. One of at least three physically separate locations inside that area, with independent power, cooling, and networking.
4. Two regions in the same geography that the platform pairs for replication and staged updates.
5. A cloud boundary operated for a specific government or compliance regime, not the public commercial regions.
6. You did not choose it. Azure defined which other region is its partner.
7. You pin a virtual machine to this when you want it in a specific hall of the region, not spread across them.
8. The word for the building, not the area and not the zone.

## Part B — Resource group (12 minutes)

1. In the portal, create a resource group named `az900-s03-lab` in the region the instructor names.
2. Open the group. Add two tags: `course` = `az900`, `session` = `s03`.
3. Optional, only if the instructor says the subscription is safe to bill: create one low-cost resource in that group. Stop at **Review + create** if they say to stop. A resource group alone does not incur compute charges. A resource inside it might.
4. Open the group and point at the tag, the region, and the list of resources.
5. Delete the resource group before you leave class. Confirm the delete. This is the habit for every later lab.

### No-cost stop

Do steps 1, 2, and 5 only if creating an empty resource group is allowed. If you have no account, draw the group as a box labeled `az900-s03-lab` with the two tags written on it, and skip create and delete.

## Part C — Draw the hierarchy (8 minutes)

On the back of the sheet, draw five levels from broadest to narrowest:

root management group → management group → subscription → resource group → resource

Mark with an arrow where an access role or a policy assigned at a subscription shows up on a resource inside a resource group. The arrow points down.

Write the two jobs of a subscription under the drawing.

<div class="pagebreak"></div>

## Instructor key

### Part A

1. Datacenter
2. Region
3. Availability zone
4. Region pair
5. Sovereign region
6. Region pair
7. Availability zone
8. Datacenter

### Part B

Empty resource groups are the safe default. If a resource was created, the group delete must finish before the quiz. Tags: `course=az900`, `session=s03`.

### Part C

Order: root management group, management group, subscription, resource group, resource.

Inheritance arrow points from the subscription down through the resource group to the resource.

A subscription is a billing boundary and an access-control boundary.
