# Session 3 slides — Azure Architecture

Each `##` heading is one slide. Notes: [session-03-instructor-notes.md](session-03-instructor-notes.md).

## 1. Azure architecture

Session 3 of 12. Where things physically live, and how Azure organizes them for billing, access, and policy.

## 2. Domain 1 checkpoint first

12 items. All 15 cloud-concept objectives. 15 minutes, then a short review.

Misses become the warm-up focus in Sessions 4 and 5. This is a diagnostic, not a grade.

## 3. Datacenter, region, zone

**Datacenter.** A physical facility. Power, cooling, hosts, security.

**Region.** A set of datacenters deployed inside a latency-defined area. You choose a region when you create most resources.

**Availability zone.** A physically separate datacenter (or group of them) inside a region, with independent power, cooling, and networking. Regions that offer zones have a minimum of three.

A datacenter is a building. A region is an area. A zone is a separated location inside that region.

## 4. Region pairs and sovereign regions

**Region pair.** Two regions in the same geography that Azure treats as a pair for platform-level replication and for staged updates. You do not pick the pair. Azure defines it.

**Sovereign region.** A region operated under a specific compliance or government boundary, separate from the public commercial cloud. You use one when the requirement says the workload cannot sit in the public commercial regions.

## 5. Zonal, zone-redundant, non-regional

**Zonal.** The resource is pinned to one zone you choose.

**Zone-redundant.** The service spreads replicas across zones in the region.

**Non-regional.** Some services are not tied to a single region. Microsoft Entra ID is the example to remember. Do not go looking for its region dropdown.

## 6. Resources and resource groups

A **resource** is one manageable item: a virtual machine, a storage account, a virtual network.

A **resource group** is a container for resources that share a lifecycle. You delete the group when the experiment is over.

A resource belongs to one resource group. Resource groups are not nested.

## 7. Subscriptions

A subscription is two boundaries at once.

**Billing boundary.** The invoice for the resources inside it.

**Access boundary.** A place you can grant or refuse permission.

It is not a region, and it is not a single resource group.

## 8. Management groups

A management group holds subscriptions, or other management groups, so you can apply governance above the subscription.

Every tenant has a root management group. You do not create the root. You organize under it.

## 9. The hierarchy

From broad to narrow:

1. Root management group
2. Management groups you create
3. Subscriptions
4. Resource groups
5. Resources

Policy and role-based access assigned higher up are inherited lower down. We use that fact again in Sessions 7 and 9.

## 10. What you will do in the lab

Name eight statements as datacenter, region, zone, region pair, or sovereign region.

Create a resource group, put one low-cost resource in it or stop before you create one, add a tag, and delete the group.

Draw the hierarchy from the root management group down to a resource, and mark where access and policy inherit.

## 11. Quiz

12 items. Nine on today, three carried forward from Domain 1.

Assignment: [Describe the core architectural components of Azure](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/).
