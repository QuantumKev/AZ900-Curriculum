# Session 9 slides — Governance and Compliance

Each `##` heading is one slide. Notes: [session-09-instructor-notes.md](session-09-instructor-notes.md).

## 1. Governance

Session 9. Policy, locks, and what Microsoft Purview is for. Tags and RBAC are already on the table. Today we separate them.

## 2. Azure Policy

Policy checks what a resource looks like, and can stop a resource that does not comply.

You assign a definition, or an initiative (a group of definitions), at a scope: management group, subscription, or resource group.

**Audit** reports noncompliance and leaves the resource alone.

**Deny** blocks the create or update that would break the rule.

Policy inherits down the hierarchy, the same direction as RBAC.

## 3. Policy is not RBAC

**RBAC** answers: may this person do this action?

**Policy** answers: may this resource look like this?

A Contributor can be blocked by a deny policy. They are allowed to create resources, and still forbidden to create a resource in the wrong region. Permission and shape are different questions.

## 4. Resource locks

A lock stops an action even when RBAC would allow it.

**Delete** (in the API: `CanNotDelete`). The resource can be read and changed. It cannot be deleted.

**Read-only.** The resource can be read. It cannot be changed or deleted.

Locks inherit down. An Owner who did not remove the lock cannot delete the resource. The lock is the point.

## 5. Microsoft Purview

Purview is the data-governance portfolio: know what data you have, classify it, and help meet compliance requirements.

For this exam, stop at that purpose. You do not need product-by-product configuration.

Purview is not Azure Policy, and it is not the Service Trust Portal.

## 6. Service Trust Portal is context

The Service Trust Portal is where Microsoft publishes audit reports and compliance information about Microsoft's own services.

It is not a bulleted objective. Know it exists so you do not call it Purview. We will not quiz it.

## 7. Five tools, five jobs

| Tool | Job |
| --- | --- |
| RBAC | Who may do an action |
| Policy | What a resource may look like |
| Lock | Block delete or block change, even for an Owner |
| Tag | Describe a resource so you can report on it |
| Purview | Govern the data itself |

## 8. Lab and quiz

Assign an audit policy if you can, and read the compliance state.

Put a delete lock on a resource group and try to delete it. The failure is the lesson. Then remove the lock and delete the group for real.

Nine short requirements, matched to the five tools.

Assignment: [Describe features and tools for governance and compliance](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/).
