# Session 11 instructor notes — Monitoring and Cumulative Review

**Objectives taught:** 3.4.1, 3.4.2, 3.4.3
**Slides:** [session-11-slides.md](session-11-slides.md)
**Lab:** [../labs/session-11-lab.md](../labs/session-11-lab.md)
**Quiz:** [../quizzes/session-11-quiz.md](../quizzes/session-11-quiz.md) — this is the Domain 3 checkpoint
**Domain minutes:** Domain 1 — 40, Domain 2 — 30, Domain 3 — 50

There is no separate warm-up. Teaching starts immediately. The cumulative review is the retrieval.

## Run of show

| Min | Block | Leave it when |
| --- | --- | --- |
| 0–20 | Advisor and Service Health | Advisor categories named. Service Health vs Resource Health vs public status separated |
| 20–45 | Monitor, Log Analytics, alerts, Application Insights | Each of the three named pieces has its own example. Gap G9 |
| 45–70 | Lab | A recommendation classified, or the docs walkthrough done. One query read |
| 70–105 | Cumulative review | Every learner has marked the Domain 1 and 2 checklist. Two weak objectives retaught |
| 105–120 | Quiz | Domain 3 checkpoint submitted |

## Teach A

Advisor categories: cost, security, reliability, operational excellence, performance. If the portal shows an extra category the week you teach, add it and do not insist the slide is exhaustive. **NEEDS VERIFICATION** against the Advisor blade that week. The behavior to teach does not change: recommendations, grouped, not auto-applied.

Service Health: issues, planned maintenance, health advisories, scoped to your services. Resource Health: one resource. Public Azure status: the world. Learners mix these constantly. Use three questions:

- "Is Microsoft having a problem with a service I use?" Service Health.
- "Is this VM's host unhealthy?" Resource Health.
- "Is Azure down for everyone, as a press story?" The public status page.

## Teach B — do not stack them (G9)

The official unit covers Log Analytics, alerts, and Application Insights in a few minutes. Give each a concrete example or the quiz will treat them as one menu.

- Log Analytics: you already have logs; you query them. Example question: which errors hit this workspace in the last hour?
- Alert: a rule plus an action group. Example: when CPU stays over a threshold, email the owner. The email target is the action group, not the rule.
- Application Insights: the app was instrumented; you see requests and failures. Example: this web app's dependency calls slowed down. It is not how you check whether Azure Storage had a platform incident. That is Service Health.

Azure Monitor is the family name over metrics, logs, alerts, and Application Insights. Say the family name and the three given names. Do not add Sentinel. It is not in this objective.

## Lab

Prefer the classification of Advisor recommendations and one provided query over a full alert-rule create, if time slips. The guided project is the right homework for alerts:
[Monitor Azure with Service Health and Activity Log alerts](https://learn.microsoft.com/en-us/training/modules/guided-project-monitor-service-health-activity-alerts/).

Activity Log alerts are about control-plane events ("who deleted the resource group"). Say that once so they are not confused with a CPU alert. Both are alerts. The signal differs.

## Cumulative review

Hand the objective checklist. Confident / shaky / blank. Walk Domains 1 and 2 only; Domain 3 is the quiz. Collect the blank counts into the readiness tracker if you can do it without killing the clock: even a show of hands per objective ID you suspect is weak.

Reteach the two IDs you wrote down at the Session 3 and Session 8 checkpoints. Five minutes each. If those IDs were actually fine and the checklist shows a different hole, teach the hole the room just marked. Data beats the plan.

## Homework

Official practice assessment, timed, once, before Session 12. They bring domain scores. You will not have time in Session 12 to watch people log in for the first time.

Module: [Describe monitoring tools in Azure](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/).

## If you are short on time

Cut the alert-rule create. Keep the three-sentence separation. Keep the checklist marks. The quiz is the Domain 3 checkpoint and does not shrink.

## Sources

[Monitoring module](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/) · [Advisor](https://learn.microsoft.com/en-us/azure/advisor/advisor-overview) · [Service Health](https://learn.microsoft.com/en-us/azure/service-health/overview) · [Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/overview) · [Log Analytics](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-overview) · [Alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview) · [Application Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview)
