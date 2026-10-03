# Session 11 lab — Advisor, Service Health, one query

**Time:** 25 minutes
**Objectives practiced:** 3.4.1, 3.4.2, 3.4.3
**You need:** a subscription with any recommendations, or the no-cost walkthrough.

---

## Part A — Classify Advisor (8 minutes)

Open Advisor. If it has recommendations, write three of them and the category each one sits in (cost, security, reliability, performance, operational excellence, or whatever category the blade actually shows).

If Advisor is empty, write "no recommendations," and use three examples the instructor reads. Still name the category.

## Part B — Service Health vs Resource Health (7 minutes)

1. Open Service Health. Note whether you see a service issue, planned maintenance, or a health advisory. "Nothing active" is a valid note.
2. Open Resource Health for any one resource, or look at the Resource Health blade. Write whose health it describes: one resource, or the whole service.
3. One sentence: why the public Azure status page is the wrong place to check your own virtual machine.

## Part C — Read a query (10 minutes)

If a Log Analytics workspace exists, the instructor pastes a query and you read the result columns out loud.

If none exists, read this sample as if it had returned rows, and answer the questions under it. You are not expected to write KQL today.

```kusto
AzureActivity
| where TimeGenerated > ago(1d)
| where OperationNameValue has "Microsoft.Resources/subscriptions/resourceGroups/delete"
| project TimeGenerated, Caller, ResourceGroup
```

- Is this an alert, or a query?
- What control-plane action is it looking for?
- What would you add, outside this query, so someone gets an email when it happens?

### No-cost path

The whole lab can be the instructor's screen plus Part C on paper. Guided project after class:
[Monitor Azure with Service Health and Activity Log alerts](https://learn.microsoft.com/en-us/training/modules/guided-project-monitor-service-health-activity-alerts/).

<div class="pagebreak"></div>

## Instructor key

Part C: it is a query, not an alert. It looks for resource-group deletes in the activity log. An alert rule plus an action group is what sends the email. Advisor categories must match the blade you showed; do not mark a learner wrong for a category Microsoft has added if they placed the recommendation with the blade.
