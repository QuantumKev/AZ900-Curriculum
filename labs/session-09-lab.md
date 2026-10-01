# Session 9 lab — Policy, a lock, and a five-way triage

**Time:** 30 minutes
**Objectives practiced:** 3.2.1, 3.2.2, 3.2.3, 3.1.4
**You need:** paper for Part A. An Azure subscription for Parts B and C, or the no-cost path.

---

## Part A — Which tool? (12 minutes)

Write **Policy**, **RBAC**, **lock**, **tag**, or **Purview**.

1. Only people on the help desk may restart virtual machines in this resource group.
2. Virtual machines may be created only in two regions. A create anywhere else must fail.
3. You want a report of storage accounts that are not encrypted at rest, without blocking the accounts.
4. This resource group must not be deletable during the term, even by an owner.
5. Finance needs the invoice split by department.
6. The company needs to classify files that contain personal data.
7. A resource may be changed but must not be deleted.
8. A person may view a storage account and must not modify it.
9. You want to know which lab session created a resource, without affecting access or price.

## Part B — Read a policy (8 minutes)

If you can assign policy:

1. At resource group `az900-s09-lab`, assign a built-in policy the instructor names, effect **Audit** if you can choose. Do not choose Deny on a shared subscription.
2. Open compliance for that assignment. A new group may say not started. Write the state you actually see.

### No-cost path

Open [Azure Policy overview](https://learn.microsoft.com/en-us/azure/governance/policy/overview) and a built-in definition the instructor has on screen. Write: the definition's goal, in one line, and whether the effect you were shown is audit or deny.

## Part C — See a lock fail (10 minutes)

1. Create resource group `az900-s09-lab` if it does not exist. Tag it `course=az900` and `session=s09`.
2. Add a **Delete** lock named `term-guard`.
3. Try to delete the resource group. Read the error. Paste or copy the sentence onto your sheet.
4. Remove the lock. Then delete the group. A lock left behind is how next week's lab gets stuck.

### No-cost path

The instructor does steps 2 and 3 on the projector. You write the error sentence and the API name `CanNotDelete` next to the portal word Delete.

Guided project for after class: [Organize and protect resources with tags and locks](https://learn.microsoft.com/en-us/training/modules/guided-project-organize-resources-tags-locks/).

<div class="pagebreak"></div>

## Instructor key

### Part A

1. RBAC
2. Policy (deny)
3. Policy (audit)
4. Lock (delete / CanNotDelete)
5. Tag
6. Purview
7. Lock (delete). Read-only would also block changes, which the sentence allows.
8. RBAC (Reader)
9. Tag

### Part C

The delete attempt fails while the lock exists. After the lock is removed, the group delete succeeds. Portal label Delete, API `CanNotDelete`.
