# Lab guides

Phase 4. One guide per session. Each guide is the practice block from the
[six-week plan](../curriculum/six-week-plan.md), written as steps, with a no-cost
variant that does not require an Azure subscription.

| Session | Guide | Hands-on | No-cost variant |
| --- | --- | --- | --- |
| 1 | [session-01-lab.md](session-01-lab.md) | Sorting, then a read-only portal tour | Instructor-shared screen |
| 2 | [session-02-lab.md](session-02-lab.md) | Service-type and pricing triage; Function App demo | Paper triage; instructor demo only |
| 3 | [session-03-lab.md](session-03-lab.md) | Resource group, tag, hierarchy diagram | Diagram and vocabulary drill |
| 4 | [session-04-lab.md](session-04-lab.md) | Functions guided project; VM and App Service flows compared | Stop at Review + create and discard |
| 5 | [session-05-lab.md](session-05-lab.md) | Virtual network with two subnets in Cloud Shell | Trace the commands against the docs |
| 6 | [session-06-lab.md](session-06-lab.md) | Storage guided project and a pricing comparison | Pricing calculator only |
| 7 | [session-07-lab.md](session-07-lab.md) | Entra ID and RBAC guided project | Docs-based RBAC scope exercise |
| 8 | [session-08-lab.md](session-08-lab.md) | Cost guardrails project and a calculator estimate | Pricing calculator, no sign-in |
| 9 | [session-09-lab.md](session-09-lab.md) | Tags, locks, and an audit policy | Read a built-in policy definition |
| 10 | [session-10-lab.md](session-10-lab.md) | Same task in portal, CLI, and PowerShell | Cloud Shell if any Azure account exists; otherwise trace |
| 11 | [session-11-lab.md](session-11-lab.md) | Service Health, Advisor, one log query | Sample walkthrough from the docs |
| 12 | [session-12-lab.md](session-12-lab.md) | Timed readiness set under exam conditions | The set and the official practice assessment are free |

## Rules for every lab

- One resource group per session, named `az900-sNN-lab`, so teardown is a single delete.
- Tag anything you create: `course=az900`, `session=sNN`, `owner=<learner>`.
- Delete the resource group before learners leave, unless the next session's lab says to keep it. Resource groups themselves do not bill; resources inside them can.
- Portal labels drift. If a button name does not match, follow the closest current label and do not invent a menu. Note the drift in the session log.
- The instructor key sits at the bottom of each guide, after a page-break marker. Print or hand out only the learner pages.

Exact Azure free-account credit and which services are free must be re-checked on the
[Azure free account page](https://azure.microsoft.com/en-us/free/) before the cohort.
Treat those terms as **NEEDS VERIFICATION** (validation log item V9).

Print:

```bash
bash tools/build-teaching-pdfs.sh
```
