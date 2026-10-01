# Session 9 instructor notes — Governance and Compliance

**Objectives:** 3.2.1, 3.2.2, 3.2.3
**Also practiced:** 3.1.4 (tags, inside the project)
**Slides:** [session-09-slides.md](session-09-slides.md)
**Lab:** [../labs/session-09-lab.md](../labs/session-09-lab.md)
**Quiz:** [../quizzes/session-09-quiz.md](../quizzes/session-09-quiz.md)
**Warm-up:** Session 9 set, weighted to hierarchy, RBAC scope, tags, and the security-and-governance benefit
**Domain minutes:** Domain 1 — 5, Domain 2 — 5, Domain 3 — 110

## Run of show

| Min | Block | Leave it when |
| --- | --- | --- |
| 0–10 | Warm-up | Inheritance and "Reader does not restart a VM" are available |
| 10–35 | Policy | Audit vs deny, and Policy vs RBAC, in their own words |
| 35–60 | Locks and Purview | CanNotDelete vs ReadOnly. Purview scoped to data governance, not a tour |
| 60–90 | Lab | Triage done. Lock failure seen, or the no-cost read done |
| 90–105 | Quiz | |
| 105–120 | Wrap | The five-tool table reconstructed from the room, not from the slide |

## Teach A

Policy definition, initiative, assignment, scope, compliance state. Keep the verbs. An initiative is a bundle of definitions so you assign one thing. Compliance state is what you read afterward: compliant or not.

Audit vs deny is the exam contrast. Audit is visibility. Deny is prevention. There are other effects (modify, append). Name them only if the module you re-read this week still lists them, and do not quiz beyond audit and deny unless the quiz file already does.

Worked example: a policy denies virtual machines outside two regions. A Contributor's RBAC still says they may create a VM. The create fails because the resource shape is illegal. Write both sentences on the board.

## Teach B

Locks. Portal says Delete. API and some CLI say `CanNotDelete`. Teach both words or the lab output will look like a different feature.

Read-only means no writes. A lock on a resource group applies to resources in it. Inheritance again.

Why locks exist: RBAC's Owner can delete. A lock is the guardrail against a tired Owner. Removing the lock is a separate permission decision. Do not imply a lock survives an owner who is determined and allowed to remove locks. It survives the delete call, not a governance bypass.

Purview, gap G7. Purpose: data governance and compliance — discover and classify data, support requirements. Out of scope: walking the Purview portal, Microsoft Fabric, or a product catalog. If the module name has shifted, teach the purpose the study guide states and say the portal may have been reorganized.

Service Trust Portal: context, one minute, "Microsoft's paperwork about Microsoft," not your resource compliance.

## Lab

The failure to delete is the moment that makes locks real. Rehearse it. If the room has no subscription, the no-cost path reads a built-in policy definition and does the triage on paper. Do not spend 20 minutes on permission errors.

Guided project: [Organize and protect resources with tags and locks](https://learn.microsoft.com/en-us/training/modules/guided-project-organize-resources-tags-locks/).

## Wrap

Make them rebuild the five-row table with books closed. Policy vs RBAC vs locks is the predictable confusion named in the six-week plan. Management-group assignment vs subscription assignment is the second one: broader scope, more inheritance, same tools.

## If you are short on time

Cut the Service Trust Portal. Cut Purview to the purpose sentence plus "not Policy." Do not cut audit vs deny or the lock demo.

## Sources

[Governance module](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/) · [Purview](https://learn.microsoft.com/en-us/purview/purview) · [Azure Policy](https://learn.microsoft.com/en-us/azure/governance/policy/overview) · [Locks](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources)
