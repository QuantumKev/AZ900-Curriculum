# Session 11 slides — Monitoring and Cumulative Review

Each `##` heading is one slide. Notes: [session-11-instructor-notes.md](session-11-instructor-notes.md).

## 1. Monitoring, then a sweep

Session 11. Three monitoring tools, then a pass over everything from the first five weeks. No new product after the break.

## 2. Azure Advisor

Advisor looks at your subscription and recommends changes.

Categories you should be able to name: reliability, security, performance, operational excellence, and cost.

A recommendation is advice. It does not change the resource until someone acts on it.

## 3. Azure Service Health

Three views, three questions.

**Service issues and advisories, and planned maintenance**, in Service Health: things Microsoft is doing or suffering, filtered to services you use.

**Resource Health:** is this specific resource up, or is the platform reporting a problem on it?

**Azure status** is the public worldwide board. Service Health is yours. Do not send a learner to the public status page when the question is about their own virtual machine.

## 4. Azure Monitor is the platform

Azure Monitor collects and acts on telemetry: metrics and logs.

The objective then names three pieces. They are not synonyms.

## 5. Log Analytics

A workspace that holds log data, and a query language (Kusto Query Language, KQL) to ask questions of it.

"Show me failures in the last hour" is a query. It is not an alert until you attach a rule.

## 6. Alerts

An alert rule watches a signal: a metric threshold, a log query, an activity.

An **action group** is who or what gets told, or what runs, when the rule fires. The rule decides. The action group notifies.

## 7. Application Insights

Application performance telemetry: requests, failures, dependencies, for an application you instrument.

It lives under the Monitor umbrella. It is not Resource Health, and it is not a bill.

## 8. Three sentences that keep them apart

Advisor: what you should change.

Service Health: what Microsoft reports about the platform and your resources' health.

Monitor: your telemetry. Log Analytics queries it. Alerts fire from it. Application Insights collects it from an app.

## 9. Cumulative review

Objective checklist. Every Domain 1 and Domain 2 objective gets a mark:

- **Confident** — you could answer a scenario cold.
- **Shaky** — you recognize it and would hesitate.
- **Blank** — you cannot say what it is.

Blanks become the study list. Two weak spots from the Session 3 and Session 8 checkpoints get a short reteach before the quiz.

## 10. Quiz and homework

Today's quiz is the Domain 3 checkpoint. Monitoring in depth, plus a sweep of cost, governance, and management.

Before Session 12, take the official practice assessment once. Bring the score by domain, not just the total.

[Official AZ-900 practice assessment](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-900/practice/assessment?assessment-type=practice&assessmentId=23)

Also finish [Describe monitoring tools in Azure](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/).
