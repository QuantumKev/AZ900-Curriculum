<!-- Copyright (c) 2026 Kevin Robinson. All Rights Reserved. -->

# Session 11 instructor guide — Describe monitoring tools in Azure, then the cumulative review

**Speak from this file.** The first half follows the current Microsoft Learn module in Microsoft's order. The second half is the course's cumulative review of Domains 1 and 2. It is a consulting script for beginners, not a second copy of the documentation.

**Module:** [Describe monitoring tools in Azure](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/)

**Checked against the live module:** 29 October 2026

**Units, in the order you will teach them:**

1. [Introduction](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/1-introduction)
2. [Describe the purpose of Azure Advisor](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/2-describe-purpose-of-azure-advisor)
3. [Describe Azure Service Health](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/3-describe-azure-service-health)
4. [Describe Azure Monitor](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/4-describe-azure-monitor)
5. Module assessment (students take this on Learn after class; do not project it)
6. [Summary](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/6-summary)

**Microsoft's learning objectives, from the module page:**

- Describe the purpose of Azure Advisor
- Describe Azure Service Health
- Describe Azure Monitor, including Azure Log Analytics, Azure Monitor Alerts, and Application Insights

**Course objective IDs** (local to this curriculum, not printed by Microsoft): 3.4.1, 3.4.2, 3.4.3.

Log Analytics, alerts, and Application Insights are one short unit. Give each its own example or the quiz will treat them as one menu. That is the gap this session exists to close.

**How to use the concept blocks.** Say the instructor talk track. Use the card when a student asks why the organization would care, or when you need the exam wording. Do not read the card headings aloud.

**What this file does not replace.** The course still has `sessions/session-11-instructor-notes.md`, slides, `labs/session-11-lab.md`, and `quizzes/session-11-quiz.md`. This guide is the speak-from lecture. The clock keeps the lab, the Domain 1 and 2 checklist, and the Domain 3 checkpoint quiz.

There is no separate six-prompt warm-up. Teaching starts immediately. The cumulative review is the retrieval. If you want three sentences of Session 10 under their feet, they are in the introduction.

Anything the current module does not say is in **Supplemental instructor context** at the end. Do not promote that material into the main script.

**Next week** is the exam-readiness session, not this one. Assign the practice assessment at the end of today.

---

## The client for the whole lesson

Contoso Health is the same fictional organization.

- A virtual machine the nurses say is slow
- A rumor in the hallway that "Azure is down"
- A web application patients use, and a dependency that application calls
- An operations lead who wants an email when CPU stays high, and a different email when someone deletes a resource group
- A director who wants to know what the clinic should fix, not a raw log dump
- Servers and clusters outside Azure that Session 10 projected with Arc, which this module says monitoring can also see

At each decision, ask the room: **"What would we recommend to Contoso, and why?"**

---

## Two-hour lesson plan

| Time | Block | Leave this block when |
| --- | --- | --- |
| 0:00–0:18 | Advisor | Five categories are named. A recommendation is not applied for you. You can act, postpone, or dismiss |
| 0:18–0:32 | Service Health | Azure Status, Service Health, and Resource Health are three different scopes |
| 0:32–0:50 | Azure Monitor: Log Analytics, alerts, Application Insights | Each of the three has its own Contoso example. An action group is who gets told |
| 0:50–1:10 | Lab | [Session 11 lab](../../labs/session-11-lab.md). One recommendation classified. One query read as a query, not an alert |
| 1:10–1:45 | Cumulative review | Every learner has marked Domains 1 and 2 on the checklist. Two weak objectives are retaught |
| 1:45–2:00 | Scored quiz | [Session 11 quiz](../../quizzes/session-11-quiz.md). Twelve items. This is the Domain 3 checkpoint |

**If you are behind at 0:25.** Keep the five Advisor categories and the three health scopes. Skip notifications and historical-alert retention.

**If you are behind at 0:42.** Keep one sentence each for Log Analytics, the alert rule plus the action group, and Application Insights. Cut the availability-test detail to "a synthetic request, so you know the app answers."

**If you are behind at 1:05.** The lab can be your screen plus the query on paper. Do not skip the checklist. Do not shrink the quiz. Cut the second reteach to one objective if you must.

---

## Mention once, then move on

These ideas are in the module or sitting next to it. Say the sentence. Do not open a configuration blade.

- Advisor notifications when a new recommendation appears
- Filtering Advisor by subscription, resource group, or service
- Service Health links into support, and historical alerts kept so a trend is visible
- Action groups are reusable across Azure Monitor, Service Health, and Azure Advisor
- Application Insights can be added with an SDK or with an agent and no code change
- The list of what Application Insights can see: request rates, response times, failure rates, dependency calls, page views and sessions, server counters
- Azure Monitor can include Azure, on-premises, and multicloud. That is the sentence that connects to Arc. Do not onboard anything
- Microsoft Sentinel is not in this module. Do not add it

---

# 1. Introduction

## What Microsoft wants students to know

The module introduces tools that monitor the environment and applications, in Azure and in on-premises or multicloud environments.

## Set the scene

**[0:00]** Contoso can deploy and they can govern. They cannot yet tell a slow virtual machine from an Azure outage, or a suggestion from an incident.

## Instructor Talk Track

This morning we decided how Contoso asks Azure to do something, and how a server outside Azure still shows up for management. This afternoon the question is different. How do they know whether the result is healthy, and what they should improve?

Three outcomes from the module. Describe Azure Advisor. Describe Azure Service Health. Describe Azure Monitor, including Log Analytics, alerts, and Application Insights.

Hold one picture from this morning, in one sentence, so the new tools have a floor. Resource Manager is the desk every request goes through. Arc projects outside resources into that management story. Neither of those is a health report.

I am not running a separate warm-up. If the room cannot say what Resource Manager does, repair it in two sentences and move. The long retrieval is the checklist after the lab.

Here is the business problem. A nurse says the clinic application is slow. Someone in the hallway says Azure is down. The director wants to know what to fix next month. Those are three different questions, and they have three different tools. If you answer all three with "Azure Monitor," you will miss the exam and you will give Contoso the wrong work.

## Whiteboard / Visual

```text
What should we improve?          Advisor
Is Azure itself having a problem? Service Health
What are our resources and apps doing? Azure Monitor
```

Leave that box up for the whole hour.

## Ask the Class

- Which of those three questions is a suggestion, and which is an incident?
- If the hallway rumor is "Azure is down worldwide," which line do you check first?

## Exam Trap

Students collapse Advisor, Service Health, and Monitor into "the monitoring blade." The exam separates a recommendation, a platform health event, and telemetry from your own resources.

## Transition

Start with the suggestion, because it is the one that is not an emergency.

---

# 2. Describe the purpose of Azure Advisor

## What Microsoft wants students to know

Azure Advisor evaluates your Azure resources and recommends how to improve reliability, security, performance, and cost. The dashboard groups recommendations into five categories: Reliability, Security, Performance, Operational Excellence, and Cost. Each recommendation includes an action you can take now, postpone, or dismiss. You can be notified when new recommendations appear, and you can filter the dashboard.

## Set the scene

**[0:05]** The director does not want a raw list of virtual machines. They want a prioritized list of what the clinic should change.

---

### Azure Advisor

**Microsoft Learn concept.** Azure Advisor evaluates your Azure resources and makes recommendations that help you improve reliability, security, performance, and cost efficiency. The unit calls it a personalized best-practices guide in the portal. Each recommendation includes a suggested action you can take right away, postpone, or dismiss. You can set notifications for new recommendations. The dashboard covers your subscriptions and can be filtered by subscription, resource group, or service. The five categories: Reliability flags configuration risks that threaten whether applications keep running. Security detects threats and vulnerabilities that could lead to breaches. Performance identifies changes that can speed applications up. Operational Excellence suggests workflow and deployment improvements. Cost finds ways to reduce Azure spending.

**Plain English.** Advisor looks at what Contoso already has and suggests improvements. It does not make the change for them.

**Consultant scenario.** Contoso has virtual machines that are larger than the workload, and a configuration that puts a clinic application at risk of going down. What would we recommend to Contoso, and why? Azure Advisor, and then a person decides whether to act, postpone, or dismiss. Not Service Health, which answers whether Azure itself is having an incident.

**Instructor talk track.**

Azure Advisor evaluates your resources and makes recommendations. The unit's purpose line is reliability, security, performance, and cost efficiency. Think of it as a personalized best-practices guide that already lives in the portal.

Each recommendation comes with a suggested action. Contoso can take it now, postpone it, or dismiss it. Say those three verbs. Advisor is not an autopilot. A recommendation to resize a virtual machine does not resize it.

You can turn on notifications so Advisor tells you when a new recommendation appears. The dashboard shows recommendations across your subscriptions. You can filter by subscription, resource group, or service. That is how a clinic with more than one subscription stays sane. Say it once.

Five categories. Write them as you say them.

Reliability helps keep applications running by flagging configuration risks.

Security detects threats and vulnerabilities that could lead to a breach.

Performance identifies changes that can speed applications up.

Operational Excellence suggests improvements to workflow and deployment.

Cost finds ways to reduce spending.

The purpose sentence says reliability, security, performance, and cost. The category list adds Operational Excellence as the fifth. Both are in the unit. If a student counts four from the first sentence and five from the list, they are both looking at the same page. The quiz expects the five categories, including Operational Excellence.

If the portal, on the day you teach, shows an extra category, add it on the board and do not insist the slide is the whole world. The behavior does not change. Recommendations, grouped, not auto-applied.

What would we recommend to Contoso, and why? Advisor for the director's "what should we fix" question. A person still chooses the action.

**Analogy.** Advisor is a building inspector's punch list. The inspector does not remodel the clinic while you are reading the list.

**Why an organization would use it.** They want best-practice recommendations against the resources they already run, sorted so a person can prioritize.

**Problem it solves.** An estate with no organized list of what to improve.

**Common confusion.** Advisor versus Service Health. Advisor talks about your configuration and your spending. Service Health talks about Azure's platform. Advisor versus a cost calculator. Advisor looks at what you have. The pricing calculator estimates what you might buy. Advisor versus Defender for Cloud. Security is one Advisor category. Defender for Cloud was the posture product in the identity session. Do not merge the product names.

**AZ-900 exam clue.** "Recommendations," "best practices," and the five category names point at Azure Advisor. "Is Azure down" does not.

**Check for understanding.** Advisor recommends a cheaper virtual machine size. Has the size changed?

## Whiteboard / Visual

```text
Advisor categories
  Reliability
  Security
  Performance
  Operational Excellence
  Cost

Each item: act, postpone, or dismiss
```

## Ask the Class

- A recommendation says the clinic could save money by shutting down an idle machine. Which category, and who decides?
- Why is Advisor the wrong place to confirm a worldwide Azure outage?

## Exam Trap

The category names are the item. Students who remember only "cost and security" miss Operational Excellence and Reliability. Students who think Advisor remediates for you miss postpone and dismiss.

## Transition

Suggestions are not outages. The hallway rumor needs a different tool, and that tool has three zoom levels.

---

# 3. Describe Azure Service Health

## What Microsoft wants students to know

Azure Service Health is how you stay informed about the health of Azure itself and of the specific resources you run. Three views narrow from global, to the services and regions you use, to one resource. You can alert on Service Health. Historical alerts are kept. When an event hits a workload, the unit says you get links into support.

## Set the scene

**[0:18]** Someone says Azure is down. You need to know whether that is the whole platform, a service Contoso uses, or one virtual machine.

---

### Three health views

**Microsoft Learn concept.** Azure Status is the global picture of Azure health across all services and regions. You check it when you hear about a widespread outage and you want to know whether it affects Azure. Service Health focuses on the services and regions you actually use. Because you are signed in, it knows which services matter and shows outages, planned maintenance, and health advisories for your environment. You can set alerts. Resource Health zooms to one resource, such as a specific virtual machine. It tells you whether that resource is running normally or having a problem, and whether the issue is on Azure's side or yours. Together the three views run from a broad service event down to a single resource. Historical alerts are retained so you can see recurring trends. When an event affects a workload, Service Health provides links to support.

**Plain English.** Status is the world. Service Health is your services. Resource Health is one resource, and it will say whether the problem looks like Azure's or yours.

**Consultant scenario.** Three calls arrive at once. A news story says Azure is having a global incident. The clinic's own region shows a planned maintenance window on a service they use. One virtual machine looks unhealthy and nobody else does. What would we recommend to Contoso, and why? Azure Status for the news story. Service Health for the maintenance window on services they use. Resource Health for that one virtual machine. Not Advisor, and not a guess from Twitter.

**Instructor talk track.**

Azure Service Health keeps you informed about the health of Azure itself and about the specific resources you run. The unit's structure is three views, and they narrow.

Azure Status is the global picture, across services and regions. This is the page for the widespread-outage rumor. Does this affect Azure at all? You do not have to be looking at your own subscription to ask that question.

Service Health is the signed-in view. It knows which services and regions you use. It shows outages, planned maintenance, and health advisories that are relevant to your environment. You can set alerts so you hear about those without refreshing the page. When the event hits a workload, the unit says you also get links to support so you can respond.

Resource Health is one resource. The unit's example is a specific virtual machine. It tells you whether that resource is running normally or having a problem, and whether the issue is on Azure's side or on yours. That last split matters. A platform problem and a disk the clinic filled are not the same phone call.

Used together, you can start wide and end on a single resource. Historical alerts stay, so a maintenance window that keeps returning is visible as a trend. Say that once.

Put the three questions on the board and do not leave this unit until the room can point.

Is Azure down for everyone, as a public story? Azure Status.

Is Microsoft having a problem with a service and region Contoso actually uses, including planned maintenance or a health advisory? Service Health.

Is this one virtual machine unhealthy, and is that Azure's problem or ours? Resource Health.

What would we recommend to Contoso, and why? All three views, used in that order when the rumor is vague, and Resource Health first when the complaint is one named machine.

**Analogy.** Azure Status is the citywide traffic report. Service Health is the report for the roads your clinic uses. Resource Health is the report for one van.

**Why an organization would use it.** They need to know whether a problem is the platform, the services they depend on, or a single resource, and they need that without guessing.

**Problem it solves.** "Azure is down" as a sentence that could mean three different scopes.

**Common confusion.** Service Health versus Resource Health. Service Health is services and regions you use. Resource Health is one resource. Azure Status versus Service Health. Status is global and does not know which clinic you are. Service Health does, because you are signed in. None of these query your application logs. That is the next unit.

**AZ-900 exam clue.** "Global outage" is Azure Status. "Outages, planned maintenance, and health advisories for the services and regions you use" is Service Health. "This virtual machine, and is it Azure's issue or yours" is Resource Health. A recommendation to save money is still Advisor.

**Check for understanding.** The public status page says Azure is healthy, and one Contoso virtual machine is unavailable. Which view do you open next, and what question are you asking it?

## Whiteboard / Visual

```text
Wide ---------------------------------------- Narrow

Azure Status     all services, all regions, the rumor
Service Health   your services and regions
                 outage, planned maintenance, health advisory
Resource Health  one resource
                 Azure's problem, or yours?
```

## Ask the Class

- Planned maintenance in a region where Contoso runs a service. Which view?
- The resource is unhealthy and the unit says you can tell the issue is on your side. Which view said that?
- Why is the public status page the wrong place to check one virtual machine?

## Exam Trap

The product family is named Service Health, and one of the three views is also called Service Health. If you say "Service Health" without a scope, students mix the family and the middle view. Say the three names every time.

## Transition

Health of the platform is not the same as what Contoso's own application is doing. A slow page can be entirely the clinic's code, on a perfectly healthy Azure.

---

# 4. Describe Azure Monitor

## What Microsoft wants students to know

Azure Monitor collects, analyzes, and acts on data from Azure, on-premises, and multicloud environments. It gathers logs and metrics from applications, operating systems, and the network, stores them, and shows them through dashboards, queries, and alerts. Log Analytics is where you query. Alerts are a rule plus an action group. Application Insights watches a web application's performance and usage.

## Set the scene

**[0:32]** Azure is healthy. The patient website is still slow, CPU has been high all morning, and nobody noticed that a resource group was deleted yesterday. Three different jobs.

---

### The platform

**Microsoft Learn concept.** Azure Monitor is a platform for collecting, analyzing, and acting on data from your Azure resources and applications. It works with Azure, on-premises, and multicloud environments. It gathers logs and metrics from applications, operating systems, and network layers, stores that data centrally, and makes it available through dashboards, queries, and alerts.

**Plain English.** Azure Monitor is the family name. It collects the numbers and the logs, and then something queries them or alerts on them.

**Consultant scenario.** Contoso wants one place for resource metrics, logs, and the web app, including machines that are not only in Azure. What would we recommend to Contoso, and why? Azure Monitor as the platform. Then name the specific tool inside it. Do not answer every follow-up question with the family name alone.

**Instructor talk track.**

Azure Monitor is the platform for collecting, analyzing, and acting on data from your resources and applications. The unit says it works with Azure, with on-premises, and with multicloud. That is the one connection back to this morning. Arc was how outside resources join Azure management. Monitor is how telemetry from Azure, on-premises, and other clouds can be collected. You do not have to wire that up today.

What it gathers: logs and metrics, from applications, from operating systems, and from the network. It stores that data, and you get to it through dashboards, queries, and alerts.

Say the family name, then refuse to stop there. The unit immediately splits into three tools students must not stack. Log Analytics. Alerts. Application Insights.

**Analogy.** Azure Monitor is the clinic's records room for operational data. Querying the chart, paging the doctor, and watching one patient's website are three different errands inside that building.

**Why an organization would use it.** They need metrics and logs in one platform, and a way to look at them or be told when something crosses a line.

**Problem it solves.** Each resource having its own unread counter, and no common place to ask a question.

**Common confusion.** Azure Monitor versus Service Health. Monitor is about your telemetry. Service Health is about Azure's health. Azure Monitor versus Advisor. Monitor does not hand you the five recommendation categories.

**AZ-900 exam clue.** If the stem says "collect and analyze logs and metrics," the family name is Azure Monitor. Then read the rest of the stem. A query, a notification, and an application trace are three different answers inside that family.

**Check for understanding.** In one sentence, what does Azure Monitor collect, and from which kinds of environments?

**Transition.** The first errand in the records room is a question you type.

---

### Azure Log Analytics

**Microsoft Learn concept.** Log Analytics is the tool in the Azure portal where you write and run queries against the data Azure Monitor collects. You can filter simply, such as finding all errors in the last hour, or run analysis that visualizes trends over time.

**Plain English.** Log Analytics is where you ask the collected data a question. The question is a query. A query does not email anyone.

**Consultant scenario.** Contoso wants to know which errors landed in the last hour, and whether resource-group deletes showed up yesterday. What would we recommend to Contoso, and why? A query in Log Analytics. Not an alert, not yet. They asked to look, not to be paged.

**Instructor talk track.**

Log Analytics is the tool in the portal where you write and run queries against what Azure Monitor has collected.

Two shapes, so they see the range. A simple filter: all errors in the last hour. Or analysis that shows a trend over time. You are not teaching the query language today. You are teaching that this is a question you run, and that it returns rows.

The lab query looks for resource-group deletes in the activity log over the last day, and it projects the time, the caller, and the resource group. Read it as a sentence. It is a query. It does not send mail. If a student calls it an alert, stop and fix that word before you move on.

**Analogy.** Log Analytics is asking the records room a question and reading the answer. Nobody has been paged yet.

**Why an organization would use it.** They already have logs and they need to ask a question or see a trend.

**Problem it solves.** Data that was collected and never examined.

**Common confusion.** A query versus an alert. Looking is not notifying. Log Analytics versus Application Insights. You can query application data too, but Application Insights is the feature aimed at the web application's own performance and usage. Do not make students write Kusto.

**AZ-900 exam clue.** "Write and run a query," "errors in the last hour," "see a trend" is Log Analytics. If the stem adds "email someone," you have left this tool.

**Check for understanding.** Is the delete query in the lab an alert? What would you have to add before anyone is emailed?

**Transition.** Looking is voluntary. The operations lead wants the clinic to be told.

---

### Azure Monitor alerts

**Microsoft Learn concept.** Alerts notify you when Azure Monitor detects that a condition you defined has been met. You create an alert rule that specifies the condition, and an action group that controls who gets notified and what happens next. Alerts can be metric-based or log-based. A metric example in the unit: email when a virtual machine's CPU stays above 80 percent. A log example: watch for a specific error pattern across resources. Action groups are reusable across Azure Monitor, Service Health, and Azure Advisor.

**Plain English.** The alert rule is the condition. The action group is who is told and what happens next. You need both.

**Consultant scenario.** Contoso wants an email when CPU stays above 80 percent, and they want to reuse the same notification list later for a Service Health advisory. What would we recommend to Contoso, and why? An alert rule for the CPU condition, and an action group for the email. The action group is the reusable piece. The rule is not the mailbox.

**Instructor talk track.**

Alerts notify you when a condition you defined has been met. Two objects. Do not let them fuse.

The alert rule specifies the condition. CPU stayed above 80 percent. Or a log query found an error pattern. Or, in the lab's language, a resource group was deleted. The rule is the "when."

The action group controls who gets notified and what happens next. The email address lives here. The rule does not contain the mailbox. Say that twice if you have to.

The unit splits alerts into metric-based and log-based. The metric example is the CPU email. The log example is a specific error pattern across more than one resource. Both are alerts. The signal is different. You do not need a third product name for that split.

One more sentence from the unit, because it ties the afternoon together. Action groups are reusable across Azure Monitor, Service Health, and Azure Advisor. The same notification list can serve a CPU alert, a service-health advisory, and a new Advisor recommendation. That is why we did not invent a separate email system inside each tool.

What would we recommend to Contoso, and why? A metric alert rule for the hot CPU, an action group that emails the operations lead, and the same action group available when Service Health has something to say. Creating the rule in the portal is homework if you are out of time. The guided project is the right place for the click path. Do not burn the review on a wizard.

**Analogy.** The alert rule is the smoke detector's setting. The action group is the call list. A detector with no call list never reaches a person. A call list with no detector never rings.

**Why an organization would use it.** Someone needs to be told when a condition is met, without watching a dashboard.

**Problem it solves.** A condition that was true at 2 a.m. and nobody knew.

**Common confusion.** The rule versus the action group. Students put the email on the rule. The action group is also not a resource lock, and it is not Advisor. Advisor can share the action group. Advisor is still the recommendation engine.

**AZ-900 exam clue.** "Notify when CPU stays above a threshold" is a metric alert. "Watch logs for an error pattern" is a log alert. "Who gets the email and what runs next" is the action group. If the stem only says "I want to look at yesterday's deletes," that is a query, not an alert.

**Check for understanding.** Which object holds the email address, and which object holds the CPU threshold?

**Transition.** CPU is the virtual machine. Contoso also has a website, and the complaint might be inside the application.

---

### Application Insights

**Microsoft Learn concept.** Application Insights is an Azure Monitor feature that monitors the performance and usage of web applications, whether they run in Azure, on-premises, or in another cloud. You add an SDK to the application, or you enable the Application Insights agent without code changes. It can monitor request rates, response times, and failure rates; dependency calls and their performance; page load times, user counts, and session trends; and server counters such as CPU, memory, and network. Availability tests send synthetic requests so you know the application is responding, including during quiet periods.

**Plain English.** Application Insights watches the web application itself: requests, failures, dependencies, and whether a test request still gets an answer.

**Consultant scenario.** The patient website is slow, and the slowness is in a dependency the application calls. Azure Status is green. What would we recommend to Contoso, and why? Application Insights. Not Service Health, because the platform is not the thing that failed, and not Advisor, because this is not a best-practice punch list.

**Instructor talk track.**

Application Insights is a feature of Azure Monitor. It monitors performance and usage of your web applications. Those applications might run in Azure, on-premises, or in another cloud. Same reach as the platform sentence.

Two ways to turn it on, and you are only naming them. Add an SDK to the application code. Or enable the Application Insights agent without changing code. Do not pick one for Contoso in this room.

What it can see. Request rates, response times, and failure rates. Dependency calls, and how those calls perform. Page load times, user counts, and session trends. Server counters: CPU, memory, and network. That last list is why a student will try to use Application Insights as the only CPU tool. A virtual machine that is not this web app still uses the metric alert from the previous block. Application Insights is aimed at the application.

Availability tests send synthetic requests to the application so you know it is responding, even when real patients are not on the site. A synthetic request is a test you send on purpose. It is not a user. Say that once.

What would we recommend to Contoso, and why? Application Insights on the patient website, so a slow dependency is visible. Service Health stays the tool for a platform incident. Advisor stays the punch list. Log Analytics stays the place you query. Alerts stay the way a person gets told.

**Analogy.** Application Insights is a monitor on the website's front door and on the rooms that door calls. It is not the city traffic report, and it is not the building inspector.

**Why an organization would use it.** They need to know how a web application is performing and being used, including its dependencies, wherever that application runs.

**Problem it solves.** A slow or failing application that platform health will not explain, because the platform is fine.

**Common confusion.** Application Insights versus Service Health. Green platform, slow app: Application Insights. Application Insights versus Log Analytics. Insights is the application feature. Log Analytics is the query tool. You can care about both. Availability tests versus real traffic. A test request is synthetic. It runs even when the site is quiet.

**AZ-900 exam clue.** "Web application," "requests, failures, dependencies," "on-premises or another cloud," "availability test" is Application Insights. "Is Storage having a platform incident" is Service Health, not Application Insights.

**Check for understanding.** The website's dependency got slow, and Azure Status is healthy. Which feature, and why not Service Health?

## Whiteboard / Visual

```text
Azure Monitor
  Log Analytics     you ask a question (a query)
  Alerts            rule = the condition
                    action group = who is told
  Application Insights
                    the web app: requests, failures,
                    dependencies, availability tests

Not these:
  Advisor           what should we improve
  Service Health    is the platform unhealthy
```

## Ask the Class

- CPU above 80 percent should email the lead. Which two objects?
- Which tool answers "what did we delete yesterday" if nobody was emailed?
- Why can the same action group serve a Service Health alert and a CPU alert?

## Exam Trap

The exam uses the family name and the child name in the same item. Azure Monitor is the platform. Log Analytics, alerts, and Application Insights are the three names inside the objective. Answering every stem with "Azure Monitor" is how this objective is missed.

## Transition

You have the three tools. They will classify one recommendation and read one query, and then we stop adding products and find out what from the last ten sessions is actually still in the room.

---

# 5. Close the monitoring lecture

## Instructor Talk Track

**[0:48]** Three sentences, then the lab.

Advisor tells Contoso what to improve, in five categories, and a person acts, postpones, or dismisses.

Service Health tells them whether the problem is global, their services and regions, or one resource.

Azure Monitor is the telemetry platform. Log Analytics queries it. An alert rule plus an action group notifies. Application Insights watches the web application.

## Ask the Class

A nurse says the site is slow, the hallway says Azure is down, and the director wants next month's fix list. Give me the three tools, in that order.

Take one answer. Then start the lab.

---

# Lab

**[0:50]** [Session 11 lab](../../labs/session-11-lab.md). About twenty minutes if the lecture ran long. Twenty-five if you are on time. Prefer classification over building an alert rule.

Part A. Open Advisor, or use three examples you read aloud if the blade is empty. They name the category the blade actually shows. Do not mark them wrong for a category Microsoft has added if they placed the recommendation with the blade.

Part B. Service Health versus Resource Health. "Nothing active" is a valid note. One sentence on why the public status page is the wrong place to check their own virtual machine.

Part C. Read the query. It is a query, not an alert. It looks for resource-group deletes. The email requires an alert rule plus an action group, which are outside the query.

The no-cost path is your screen plus Part C on paper. The click-path homework, if anyone wants it before next week, is the guided project [Monitor Azure with Service Health and Activity Log alerts](https://learn.microsoft.com/en-us/training/modules/guided-project-monitor-service-health-activity-alerts/). An activity-log alert is still an alert. The signal is a control-plane event, such as a delete, rather than CPU.

---

# 6. Cumulative review — Domains 1 and 2

## What this block is for

**[1:10]** Thirty-five minutes. No new products. The quiz in fifteen minutes is Domain 3, so you do not reteach cost, governance, deployment, or monitoring here unless a checklist mark forces a one-sentence repair.

Hand out the objective checklist if they do not have it: `handouts/objective-checklist.md`. They mark only Domain 1 and Domain 2 right now.

- **C — Confident.** They could explain it and pick it out of a scenario.
- **S — Shaky.** They recognize it and would not bet on it.
- **B — Blank.** They cannot say what it is.

Tell them the marks are for next week's clinic. A blank is useful. A polite "confident" is not.

## How to run it

**[1:12]** Two minutes of instructions. Then they mark in silence for eight minutes. You walk. You do not answer the items while they mark. If you answer, the mark is yours.

**[1:20]** Show of hands. Ask: "Blank on shared responsibility. Blank on availability zones. Blank on the compute choices. Blank on VPN versus ExpressRoute. Blank on the three Entra products. Blank on RBAC versus Policy versus locks." Write the two loudest blanks on the board. Those are the two you reteach. Five minutes each. If the room is healthy on your guesses and sick somewhere else, teach the hole they just marked. The checklist beats your plan.

Use the one-sentence repairs below. Do not reopen the full lecture.

## One-sentence repairs

Say the sentence only if that row is one of the two holes, or if a hand went up. Then ask one person to say it back.

**Domain 1**

| If they blank on | Say this, then stop |
| --- | --- |
| Cloud computing | On-demand resources, delivered over the internet, with the provider running the infrastructure so the clinic does not buy the datacenter. |
| Shared responsibility | The provider and the customer split the stack. The customer always owns their data and their identities. IaaS puts the most on the customer. SaaS puts the most on the provider. PaaS sits between them. |
| Public, private, hybrid | Public is the shared cloud. Private is dedicated to one organization. Hybrid is both, connected. |
| Consumption-based | You pay for what you use. You stop paying when you stop using it. |
| Pricing models | Pay as you go is the list price with no commitment. A reservation and a savings plan trade a commitment for a lower compute price. Spot is unused capacity that can be interrupted. |
| Serverless | You run code without managing a server. Azure Functions is the example. The provider scales it and you pay for the execution. |
| High availability and scalability | Availability means it keeps serving. Scalability means you can grow. Elasticity means that growth can shrink again when the load leaves. |
| Reliability and predictability | Reliability means it keeps working, including across failure. Predictability means performance and cost are close to what you expected. |
| Security and governance | Cloud services give you tools to require a standard and to see when something drifts. |
| Manageability | You can manage from a portal or a command, and you can deploy from a template instead of a one-off click. |
| IaaS, PaaS, SaaS | IaaS is the virtual machine and the network, and you patch the guest. PaaS is the platform, such as App Service, and you bring the app. SaaS is the finished software, such as Microsoft 365. |

**Domain 2**

| If they blank on | Say this, then stop |
| --- | --- |
| Region, region pair, sovereign region | A region is a geography of datacenters. A region pair is two regions in the same geography, paired for replication and staged updates. A sovereign region is a special region for a legal or government boundary. |
| Availability zone | Separate datacenters inside one region, with independent power, cooling, and networking. |
| Datacenter | The physical building. A region contains one or more of them. |
| Resource and resource group | A resource is the thing you create. A resource group is the container you manage and delete together. |
| Subscription | The billing and access boundary that holds resource groups. |
| Management group | A container of subscriptions, for policy and access above the subscription. |
| Hierarchy | Management group, then subscription, then resource group, then resource. What you assign above is inherited below. |
| Compute types | A virtual machine is an operating system you manage. A container is the app and its dependencies, without a full VM per app. A function is code that runs when an event happens, without a server you manage. |
| VM options | A VM is one machine. A scale set is many VMs behind one definition. An availability set uses update domains and fault domains so one fault or one update does not hit every VM. It is an older single-datacenter tool. It is not an availability zone. Azure Virtual Desktop is a desktop in Azure, not a server SKU. |
| What a VM needs | A size, a disk, a network, and you still patch the guest. |
| Hosting an app | App Service for a web app without an OS to manage. A container when you need the packaged app. A VM when you need the operating system. |
| Networking | A virtual network is the private space. A subnet divides it. Peering connects two virtual networks on Microsoft's backbone. VPN Gateway encrypts a tunnel over the internet. ExpressRoute is a private circuit that does not use the internet as the path. Azure DNS hosts records. It does not sell the domain name. |
| Public and private endpoints | A public endpoint is reachable from the internet. A private endpoint gives the service a private IP from the virtual network's address space. A service endpoint links services such as Azure SQL and storage to the virtual network for security and optimal routing. Private IP means private endpoint. "Link SQL or storage for security and optimal routing" means service endpoint. |
| Storage services | Blob is files and objects. Files is a share. Queue is messages. Table is simple NoSQL. Disk is the disk on a virtual machine. |
| Tiers and redundancy | Hot, cool, cold, and archive are how often you touch the data. LRS, ZRS, GRS, and GZRS are how many copies and where. Access tier is not redundancy. |
| Migration tools | Azure Migrate assesses and moves. Data Box moves bulk data offline. File Sync keeps a Windows file server and Azure Files aligned. AzCopy and Storage Explorer copy. None of them are Arc. |
| Entra ID, Connect, Domain Services | Entra ID is the cloud directory. Entra Connect synchronizes on-premises Active Directory with it. Domain Services is the managed domain for domain join, group policy, LDAP, and Kerberos or NTLM, and the sync into it is one-way. |
| SSO, MFA, passwordless | SSO is one sign-in for many apps, only as secure as that first sign-in. MFA adds a factor: know, have, or are. Passwordless removes the password: Windows Hello for Business, Authenticator, or a FIDO2 key. |
| External identities | A guest in your directory is B2B collaboration. A Teams shared channel where the user is not in your directory is B2B direct connect. Patients in your own application are External ID for customers. |
| Conditional Access | Signals, then a decision, then enforcement: allow, block, or require MFA. |
| RBAC | A role at a scope, inherited by child scopes. Reader at a subscription can see everything under it. Permissions combine. RBAC does not see inside the application data. |
| Zero Trust | Verify explicitly, least privilege, assume breach. Being on the network is not trust. |
| Defense in depth | Data at the center. Physical, identity, perimeter, network, compute, application, data. DDoS is perimeter. An NSG is network. |

## The two reteaches

**[1:28]** Five minutes on the first hole. One scenario, spoken, not a slide reread. Ask "what would we recommend to Contoso, and why?" Take two answers. Give the one-sentence repair if they miss. Ask one person to repeat the repair.

**[1:33]** Five minutes on the second hole. Same shape.

**[1:38]** Two minutes. "Anything you marked blank that I did not touch, write the objective ID on the corner of the checklist. Bring it next week. I will build the clinic from those IDs and from the practice-assessment scores, not from my memory of what I enjoyed teaching."

If the room is strong and you have five minutes left, use the rapid-fire list at the end of this guide. Do not start a new topic.

---

# Quiz

**[1:45]** [Session 11 quiz](../../quizzes/session-11-quiz.md). Twelve items, fifteen minutes. It is already written. This is the Domain 3 checkpoint. Items 7 through 9 sweep cost, governance, and deployment. Do not skip the quiz to extend the review.

Review only the items several people missed. If they swap the three health views, repair that with the wide-to-narrow picture before they leave. If they stack Log Analytics, alerts, and Application Insights, repair it with the three errands.

After class, each student completes the monitoring module on Learn, including the module assessment. Do not project Microsoft's assessment items.

## Homework before next week's exam session

Say this out loud. Do not leave it as a slide they might not read.

Before next week, each person takes the official AZ-900 practice assessment once, timed, and brings the domain scores. You will not have time next week to watch people sign in for the first time. They also bring the checklist. A blank is more useful than a kind confident.

Next week is the readiness session: a timed set, a debrief, and a clinic on the holes. It is not a new module.

## If you remember only 10 things

1. Azure Advisor evaluates your resources and recommends improvements. The five categories are Reliability, Security, Performance, Operational Excellence, and Cost. You act, postpone, or dismiss. Advisor does not apply the change.
2. Azure Status is global health. Service Health is outages, planned maintenance, and health advisories for the services and regions you use. Resource Health is one resource, and whether the problem is Azure's or yours.
3. Azure Monitor collects, analyzes, and acts on logs and metrics from Azure, on-premises, and multicloud environments.
4. Log Analytics is where you run a query. A query is not an email.
5. An alert rule is the condition. An action group is who is notified and what happens next. Action groups are reusable across Azure Monitor, Service Health, and Advisor.
6. A CPU threshold is a metric alert. An error pattern in the logs is a log alert. A resource-group delete is a control-plane signal. All three can be alerts. The signal changes.
7. Application Insights watches a web application's requests, failures, dependencies, usage, and availability tests, in Azure or elsewhere. It is not how you check a platform incident.
8. Advisor, Service Health, and Azure Monitor answer three different questions: what should we improve, is Azure unhealthy, and what are our resources and applications doing.
9. Domains 1 and 2 were marked today. Blanks come back next week. Shared responsibility, the region and zone picture, compute choices, VPN versus ExpressRoute, the three Entra products, and RBAC versus Policy versus locks are the usual holes.
10. Next week is exam readiness. The practice assessment is timed, once, before that session. Microsoft Learn is not available during the Fundamentals exam.

## Rapid-fire instructor questions

Ask these if the review finishes early. Do not grade them.

1. Name the five Advisor categories.
2. Advisor recommends a change. Has the change happened?
3. Which health view is the global rumor?
4. Which health view knows the services you use?
5. Which health view can say the problem is yours, not Azure's?
6. What do you run in Log Analytics?
7. Which object holds the email address on an alert?
8. What does an availability test send?
9. The platform is healthy and the website's dependency is slow. Which feature?
10. Management group, subscription, resource group, resource: which way does inheritance run?

## Service recognition table

| Business requirement | Azure concept / service | Why | Common wrong answer |
| --- | --- | --- | --- |
| A best-practice list for reliability, security, performance, operations, and cost | Azure Advisor | Evaluates your resources and recommends; you act, postpone, or dismiss | Service Health, or a pricing calculator |
| Is Azure having a worldwide incident? | Azure Status | Global view across services and regions | Resource Health |
| Outage, planned maintenance, or a health advisory for a service you use | Service Health | Signed-in view of your services and regions; you can alert | The public status page, which does not know your subscription |
| Is this one virtual machine unhealthy, and whose fault is it? | Resource Health | One resource; Azure's side or yours | Advisor |
| Ask a question of collected logs | Log Analytics | Queries against Azure Monitor data | An alert, which notifies |
| Email me when CPU stays over a line | Metric alert rule, plus an action group | The rule is the condition; the action group is who is told | Putting the email on the rule, or using Advisor |
| Watch a log pattern across resources | Log alert | The signal is a query, the shape is still rule plus action group | Log Analytics alone, if they also wanted to be notified |
| See requests, failures, and dependency calls for a web app | Application Insights | Application performance and usage, including synthetic availability tests | Service Health, when the platform is healthy |
| Same notification list for Monitor, Service Health, and Advisor | Action group | Reusable across those services | A separate mailbox product per tool |
| Who may change a resource | Azure RBAC | Role at a scope | A lock, or Policy |
| Which configurations are allowed | Azure Policy | Governance of properties, such as region | A lock |
| Block a delete even for an Owner | Resource lock | Applies regardless of role and regardless of portal or template | RBAC |
| Project a non-Azure server into management | Azure Arc | Does not move the server | Azure Migrate |

---

# Supplemental instructor context

Do not teach this section as part of the module. Use it only when a student asks. Say that you are stepping outside the unit, then come back.

**Activity Log.** The monitoring unit's alert examples are CPU and an error pattern in logs. The lab query uses `AzureActivity`, which is the activity log: control-plane actions such as deleting a resource group. An alert on that signal is still an Azure Monitor alert. The condition is the control-plane event. You do not need a new product name. The guided project is where that click path lives.

**Microsoft Sentinel.** It is not in this module and it is not an AZ-900 objective in this course. If a student names it, say it is a separate security product and come back to Log Analytics, alerts, and Application Insights.

**Advisor categories on the day.** Checked 29 October 2026, the unit lists five: Reliability, Security, Performance, Operational Excellence, and Cost. The older "needs verification" note in the instructor notes can be retired for that list. If the portal shows another category in class, add it. Do not drop Operational Excellence to make the list match an older slide.

**Defender for Cloud and Advisor's security category.** Session 7 taught Defender for Cloud as posture, secure score, and alerts. Advisor also has a Security category. They are not the same blade. You do not need to reconcile the products unless someone asks. If they ask: Advisor's security category is a recommendation group. Defender for Cloud is the security posture product from the identity module.

**Exam logistics, if someone asks today.** Forty-five minutes of exam time inside a sixty-five minute seat. Seven hundred or higher to pass. Fundamentals exams do not include Microsoft Learn access during the exam. The certification does not expire. A first retake is allowed 24 hours after a failed attempt; later retakes wait longer. Next week's session is where this gets the full block. Do not spend the checklist time on it. These figures are the ones already in the course overview, cited to Microsoft Learn.

---

## Sources

Checked 29 October 2026. The talk track follows these units. It does not reproduce them.

- [Module: Describe monitoring tools in Azure](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/)
- [Introduction](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/1-introduction)
- [Describe the purpose of Azure Advisor](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/2-describe-purpose-of-azure-advisor)
- [Describe Azure Service Health](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/3-describe-azure-service-health)
- [Describe Azure Monitor](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/4-describe-azure-monitor)
- [Summary](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/6-summary)
- Course checklist for the review block: [handouts/objective-checklist.md](../../handouts/objective-checklist.md)
- Course lab and checkpoint: [labs/session-11-lab.md](../../labs/session-11-lab.md), [quizzes/session-11-quiz.md](../../quizzes/session-11-quiz.md)
