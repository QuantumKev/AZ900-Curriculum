<!-- Copyright (c) 2026 Kevin Robinson. All Rights Reserved. -->

# Session 7 instructor guide — Describe Azure identity, access, and security

**Speak from this file.** It follows the current Microsoft Learn module in Microsoft's order. It is a consulting script for beginners, not a second copy of the documentation.

**Module:** [Describe Azure identity, access, and security](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/)

**Checked against the live module:** 20 October 2026

**Units, in the order you will teach them:**

1. [Introduction](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/1-introduction)
2. [Describe Azure directory services](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/2-directory-services)
3. [Describe Azure authentication methods](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/3-authentication-methods)
4. [Describe Azure external identities](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/4-external-identities)
5. [Describe Azure conditional access](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/5-conditional-access)
6. [Describe Azure role-based access control](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/6-role-based-access-control)
7. [Describe Zero Trust model](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/7-describe-zero-trust-model)
8. [Describe defense-in-depth](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/8-describe-defense-depth)
9. [Describe encryption and key management in Azure](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/9a-describe-encryption-key-management)
10. [Describe Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/9-describe-microsoft-defender-for-cloud)
11. Module assessment (students take this on Learn after class; do not project it)
12. [Summary](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/11-summary)

**Microsoft's learning objectives, from the module page:**

- Describe directory services in Azure, including Microsoft Entra ID and Microsoft Entra Domain Services
- Describe authentication methods in Azure, including single sign-on (SSO), multifactor authentication (MFA), and passwordless
- Describe external identities and guest access in Azure
- Describe Microsoft Entra Conditional Access
- Describe Azure Role Based Access Control (RBAC)
- Describe the concept of Zero Trust
- Describe the purpose of the defense in depth model
- Describe encryption concepts and key management options in Azure
- Describe the purpose of Microsoft Defender for Cloud

Encryption and key management are in the module. They are not a scored objective in this course. Teach the short block. Do not quiz it.

**Course objective IDs** (local to this curriculum, not printed by Microsoft): 2.4.1 through 2.4.8. Encryption has no local objective ID.

**How to use the concept blocks.** Say the instructor talk track. Use the card when a student asks why the organization would care, or when you need the exam wording. Do not read the card headings aloud.

**What this file does not replace.** The course still has `sessions/session-07-instructor-notes.md`, slides, `labs/session-07-lab.md`, and `quizzes/session-07-quiz.md`. This guide is the speak-from lecture. The clock below keeps the 30-minute lab and the 10-minute scored quiz. If you drop the lab, use the extra time on the Contoso recommendation pass. Do not drop the quiz.

Anything the current module does not say is in **Supplemental instructor context** at the end. Do not promote that material into the main script.

---

## The client for the whole lesson

Contoso Health is the same fictional organization as the networking session.

- Employees at headquarters, and nurses who work from home
- An on-premises Active Directory at headquarters
- A legacy application that still expects a domain join
- A supplier that needs access to one internal application
- A partner organization that collaborates in Teams
- Patients who sign in to the public website, who are customers, not employees
- A billing clerk who should see Azure resources and not change them
- Privileged administrators who sometimes sign in from outside the clinic network
- Patient records in Azure Storage and Azure SQL

At each decision, ask the room: **"What would we recommend to Contoso, and why?"**

---

## Two-hour lesson plan

| Time | Block | Leave this block when |
| --- | --- | --- |
| 0:00–0:10 | Warm-up, Session 7 set | The room has produced answers on shared responsibility, SaaS, storage, and a private endpoint |
| 0:10–0:35 | Directory services | Entra ID, Entra Connect, and Entra Domain Services are three different answers |
| 0:35–1:00 | Authentication, external identities, Conditional Access | MFA is not SSO. A guest in the directory is not a Teams shared channel, and neither is a patient account |
| 1:00–1:20 | RBAC, Zero Trust, defense in depth, a short encryption note, Defender for Cloud | Reader at subscription scope is understood as inheritance. Defender is not the sign-in decision |
| 1:20–1:50 | Lab | [Session 7 lab](../../labs/session-07-lab.md). Scope prediction and the layer sort are the required parts |
| 1:50–2:00 | Scored quiz | [Session 7 quiz](../../quizzes/session-07-quiz.md). Ten items. Review only what the room missed |

**If you are behind at 0:30.** Keep the three directory services. Skip replica sets, the one-way sync diagram detail, and who inside Microsoft uses Entra ID.

**If you are behind at 0:55.** Keep SSO versus MFA versus passwordless, the three external-identity names, and the Conditional Access sequence: signal, decision, enforcement. Skip FIDO2 hardware details and access reviews.

**If you are behind at 1:15.** Keep RBAC inheritance and the allow model, the three Zero Trust principles, and the seven layer names. Give encryption one sentence. Give Defender the secure-score sentence. Cut the multicloud list.

---

## Mention once, then move on

These ideas are in the module. They are useful. They are too implementation-specific for a long stop on AZ-900.

- Two domain controllers, a replica set, backups, and Azure Disk Encryption on those domain controllers
- Application Proxy, the My Apps portal, Intune, banned password lists, and smart lockout
- Access reviews for guests
- WebAuthn, Bluetooth, and NFC on a FIDO2 key
- Just-in-time VM access, adaptive application controls, kill-chain correlation, and Logic Apps
- Cloud Security Posture Management and the Microsoft cloud security benchmark, beyond the name
- Azure Arc, beyond "this is how non-Azure machines can be included"
- Key rotation alerts and managed identities reading Key Vault, beyond one sentence each

---

# 0. Warm-up

## What Microsoft wants students to know

Nothing new. This block retrieves earlier sessions so identity has something to sit on.

## Set the scene

**[0:00]** Read these six prompts. They are free recall. Do not project the answers. Accept the substance, not the wording. If two people miss the same prompt, re-teach that one fact in a minute and move on.

The prompts are the Session 7 set in `quizzes/warm-ups.md`.

## Instructor Talk Track

Before we talk about who may sign in, I need to know that the earlier ground is still there.

First. For a cloud SQL database offered as a managed service, who maintains the database engine, and who is responsible for the data in it? The provider maintains the database service. Contoso is responsible for the data they put in it.

Second. Name two ways the cloud helps with governance and compliance. Templates that make deployments meet a standard. Auditing that flags resources that drift. Automatic patching, depending on the service model.

Third. Match the workload to the storage service. A video file is Blob Storage. A shared drive for a team is Azure Files. Messages waiting to be processed are Queue Storage. A disk for a virtual machine is Azure Disk Storage.

Fourth. Give two examples of software as a service. Email, messaging, a productivity suite, or a finance application are all fair.

Fifth. A database should be reachable from inside a virtual network and not from the internet. What do you use? A private endpoint.

Sixth. Which storage service holds structured, non-relational data as a NoSQL store? Azure Table Storage.

Good. Hold the fifth answer. A private endpoint decided where the database could be reached. Today we decide who is allowed to ask, and what they are allowed to do after we believe them.

## Whiteboard / Visual

Leave a blank line under the warm-up. You will fill it in a moment with three words: **Who are you. Are you allowed in. What may you do.**

## Ask the Class

- Who owns the patient records if Microsoft runs the database service?
- Is a private endpoint the same thing as a user account?

## Exam Trap

Students will try to answer an identity question with a networking product. A private endpoint is where a service lives. It is not who the user is.

## Transition

Imagine Contoso is hiring, inviting a supplier, and letting patients open a website. Before I recommend a control, I need to know which of those people already exist in Contoso's directory, and which of them never should.

---

# 1. Introduction

## What Microsoft wants students to know

The module introduces directory services, authentication, access control, Zero Trust, defense in depth, encryption and key management, and Microsoft Defender for Cloud.

## Set the scene

**[0:10]** Contoso's director says, "Just turn on security." That sentence is not a design.

## Instructor Talk Track

Today is one story in Microsoft's order. First, where identities live. Then how a person or a service proves who they are. Then people who are not Contoso employees. Then the sign-in decision that depends on the situation. Then what an account may do to an Azure resource. Then the two security models Microsoft wants you to recognize: Zero Trust, and defense in depth. Then a short stop on encryption, because the module includes it and the exam objective list for this course does not score it. Last, the service that watches the estate and tells Contoso what to fix.

Here is the business problem. Contoso has employees, a supplier, and patients. Those are not one kind of account. An employee who has signed in is not automatically allowed to restart a virtual machine. A locked network is not a substitute for knowing who is at the keyboard.

Before we choose a service, ask yourself three questions. Who is this? Are they allowed to sign in under these conditions? What may they do to Azure resources after that?

If I were consulting with this company, the first question I would ask is not "Do you want multifactor authentication?" The first question is "Whose identities do you already have, and whose identities must stay outside your employee directory?"

Say "Microsoft Entra ID" every time. If someone says Azure AD, translate it once: that is the old name. This module's name is Microsoft Entra ID. Then move on.

## Whiteboard / Visual

```text
Who are you?          directory and authentication
Are you allowed in?   Conditional Access
What may you do?      Azure RBAC
What if a layer fails?  Zero Trust and defense in depth
What should we fix?   Defender for Cloud
```

## Ask the Class

- Which of those five lines is about a patient, and which is about a billing clerk inside Azure?
- Why is "turn on security" not a recommendation?

## Exam Trap

The exam describes a person and a constraint. A nurse, a guest, a customer, a reader, a risky sign-in, a layer of defense. Pick the control that matches the constraint.

## Transition

The directory comes first. If Contoso has two copies of every employee, every later control gets twice as hard.

---

# 2. Describe Azure directory services

## What Microsoft wants students to know

Microsoft Entra ID is Microsoft's cloud-based identity and access management service. People sign in and reach Microsoft cloud applications and applications the organization develops. Microsoft Entra Connect synchronizes on-premises Active Directory with Microsoft Entra ID so the organization is not maintaining two identity sets. Microsoft Entra Domain Services provides managed domain services — domain join, group policy, LDAP, and Kerberos or NTLM — without domain controllers the organization has to deploy and patch.

## Set the scene

**[0:18]** Headquarters already has Active Directory. A clinic application from 2014 still wants to join a domain. Nurses also need Microsoft 365. You will not solve those three facts with one product name.

---

### Microsoft Entra ID

**Microsoft Learn concept.** Cloud-based identity and access management. IT administrators control access. Developers add sign-in to apps they build, including single sign-on against credentials the user already has. Users manage their own identity, including self-service password reset. Subscribers to Microsoft 365, Office 365, Azure, and Dynamics CRM Online are already authenticating with Microsoft Entra ID. The service provides authentication, single sign-on, application management, and device management.

**Plain English.** Entra ID is the cloud directory. It is the place Contoso's cloud accounts live, and the place Microsoft 365 already looks for them.

**Consultant scenario.** Contoso's nurses open Microsoft 365 and an internal application. What would we recommend to Contoso, and why? Microsoft Entra ID as the cloud directory. They are likely already using it if they have Microsoft 365.

**Instructor talk track.**

Microsoft Entra ID is Microsoft's cloud-based identity and access management service. It lets people sign in and reach both Microsoft's cloud applications and applications Contoso builds.

If you have used on-premises Active Directory, this will feel familiar. The difference the unit wants you to hear is this. Contoso controls the identity accounts. Microsoft keeps the service available globally.

Here is the business problem. Every nurse, billing clerk, and administrator who touches Microsoft 365 or Azure needs an identity in the cloud. Microsoft 365, Office 365, Azure, and Dynamics CRM Online subscribers are already using Entra ID to authenticate. Contoso does not stand up a second cloud directory beside the one Microsoft 365 is already using.

Who it is for, in four short pictures. Administrators control access to applications and resources. Developers add sign-in to an application, including single sign-on with credentials the user already has. Users reset their own password. And the online-service subscribers I just named are already in it.

What it does, at this level. Authentication, which verifies identity before access, including self-service password reset, multifactor authentication, banned password lists, and smart lockout. Single sign-on, so one identity reaches many applications. We will define that properly in the next unit. Application management, for cloud and on-premises apps. Device management, so a Conditional Access decision can later care about whether the device is known.

You do not configure banned passwords or smart lockout today. You recognize that those are authentication features of the directory, not a separate product.

**Analogy.** Entra ID is the employee badge system for the cloud campus. Microsoft runs the badge service. Contoso decides who gets a badge.

**Why an organization would use it.** People need one cloud identity for Microsoft cloud applications and for applications the organization develops.

**Problem it solves.** Cloud sign-in has a directory, without Contoso operating that directory as a set of servers.

**Common confusion.** Entra ID versus Entra Domain Services versus Entra Connect. Entra ID is the cloud directory. The other two are how an older directory, or an older application, relates to it.

**AZ-900 exam clue.** "Cloud identity," "sign in to Microsoft 365 and Azure," "self-service password reset" points at Microsoft Entra ID. If the stem requires domain join, group policy, LDAP, or Kerberos, do not answer Entra ID by itself.

**Check for understanding.** A classmate says Contoso needs a new cloud directory because they bought Microsoft 365. What do you tell them?

**Transition.** Headquarters still has the old directory. Leaving it disconnected means every person exists twice.

---

### Microsoft Entra Connect

**Microsoft Learn concept.** Without a connection, on-premises Active Directory and cloud Entra ID are two identity sets. Entra Connect synchronizes user identities between them. Changes flow between both, so people get a consistent experience, including single sign-on, multifactor authentication, and self-service password reset, for on-premises and cloud resources. Connecting also lets Microsoft detect suspicious sign-ins, such as an unexpected location or an unknown device, which on-premises Active Directory by itself does not do, and the unit says this detection is at no extra cost.

**Plain English.** Entra Connect is the sync. One person, one identity story, in both places.

**Consultant scenario.** Contoso's headquarters Active Directory is the list of employees the clinic already trusts. What would we recommend to Contoso, and why? Microsoft Entra Connect, so those identities synchronize to Entra ID. Not a second set of accounts typed in by hand.

**Instructor talk track.**

Here is the business problem. If the on-premises directory and Entra ID are not connected, Contoso maintains two sets of people. A nurse who leaves has to be removed twice. A password reset in one place does not help the other place.

Microsoft Entra Connect synchronizes user identities between on-premises Active Directory and Microsoft Entra ID. Changes flow between both systems. The person gets a consistent experience, including single sign-on, multifactor authentication, and self-service password reset, whether the resource is on-premises or in the cloud.

The unit adds one security reason. On-premises Active Directory by itself does not monitor sign-in behavior. Once it is connected to Entra ID, Microsoft can detect suspicious sign-in attempts, such as an unexpected location or an unknown device, and the unit says that detection comes at no extra cost.

What would we recommend to Contoso, and why? Entra Connect, because the employee list already exists at headquarters. We are not inventing a second workforce in the cloud.

This is where students often mix up two services. Connect does not replace Entra ID. Connect feeds it. Connect also does not join a virtual machine to a domain. That is the next service.

**Analogy.** Entra Connect is the courier that keeps the headquarters staff list and the cloud badge list the same. The courier is not the badge system, and the courier is not the old domain controller.

**Why an organization would use it.** They already have Active Directory on-premises and they need those people in Entra ID without a second manual list.

**Problem it solves.** Two identity sets, and sign-in protections that the on-premises directory does not provide alone.

**Common confusion.** Entra Connect versus Entra Domain Services. Connect synchronizes identities. Domain Services hosts a managed domain for applications.

**AZ-900 exam clue.** Watch for "synchronize," "on-premises Active Directory," "hybrid," or "one identity in both places." That is Entra Connect.

**Check for understanding.** Contoso hires a billing clerk in the on-premises directory. What has to be true for that clerk to show up in Entra ID without someone retyping the account?

**Transition.** Some applications do not speak modern sign-in at all. They want a domain. Contoso should not have to babysit domain controllers in Azure to get one.

---

### Microsoft Entra Domain Services

**Microsoft Learn concept.** Managed domain services: domain join, group policy, LDAP, and Kerberos/NTLM authentication, without deploying or maintaining domain controllers in the cloud. Useful for legacy applications that cannot use modern authentication. You define a namespace, the domain name. Two Windows Server domain controllers are deployed in the selected region. That deployment is a replica set. You do not manage, configure, or update those domain controllers. The platform handles them, including backups and encryption at rest with Azure Disk Encryption. Synchronization from Entra ID to Domain Services is one-way. Objects you create in the managed domain are not synchronized back to Entra ID. In a hybrid environment, Entra Connect syncs on-premises identity to Entra ID, and that then syncs to the managed domain. Users can sign in to the managed domain with their existing credentials. Groups and user accounts carry over.

**Plain English.** Domain Services is a domain Microsoft operates for you, so an old application can join it. Accounts flow in from Entra ID. They do not flow back.

**Consultant scenario.** Contoso has a clinic application that requires domain join and cannot use modern authentication. They do not want to patch domain controllers in Azure. What would we recommend to Contoso, and why? Microsoft Entra Domain Services. Not a pair of virtual machines they manage themselves, and not Entra ID alone.

**Instructor talk track.**

Microsoft Entra Domain Services provides managed domain services. The list you should be able to say is domain join, group policy, LDAP, and Kerberos or NTLM authentication. Contoso does not deploy or maintain the domain controllers.

Here is the business problem. A legacy application cannot use the modern sign-in we just described. Lifting it into Azure still leaves it asking for a domain. Standing up domain controllers means patching, backing up, and watching those servers. Domain Services is the managed domain for that application.

You define a unique namespace. That namespace is the domain name. Two Windows Server domain controllers land in the region you select. Microsoft calls that pair a replica set. You do not manage, configure, or update them. The platform handles them, including backups and encryption at rest using Azure Disk Encryption. Say "replica set" once so the phrase is familiar. Do not design it.

The sync direction matters. A managed domain performs a one-way synchronization from Microsoft Entra ID to Microsoft Entra Domain Services. You can create something in the managed domain, and it is not synchronized back to Entra ID. In Contoso's hybrid picture, Entra Connect brings headquarters identities into Entra ID, and those identities then synchronize into the managed domain. Users sign in to that domain with the credentials they already have. Groups and accounts carry over.

Applications, services, and virtual machines in Azure that connect to the managed domain can then use domain join, group policy, LDAP, and Kerberos or NTLM.

What would we recommend to Contoso, and why? Domain Services for the legacy application. Entra ID remains the cloud directory. Entra Connect remains the sync from headquarters. Domain Services does not replace either one.

**Analogy.** Entra ID is the cloud badge system. Domain Services is a managed reception desk that still speaks the old building's language, so the 2014 application can sign in. The desk reads the badge list. It does not become the master copy of that list.

**Why an organization would use it.** A workload needs domain services, and the organization does not want to operate domain controllers.

**Problem it solves.** Legacy authentication in Azure without a domain-controller project.

**Common confusion.** Domain Services versus Entra ID. If the requirement is domain join, group policy, LDAP, or Kerberos, the answer is Domain Services. If the requirement is the cloud directory for Microsoft 365, the answer is Entra ID. Also, one-way sync. Creating a user in the managed domain does not create that user in Entra ID.

**AZ-900 exam clue.** Watch for "managed domain," "do not want to maintain domain controllers," and the four protocols or features: domain join, group policy, LDAP, Kerberos or NTLM.

**Check for understanding.** Someone creates a test account inside the managed domain and expects it to appear in Entra ID. What does the unit say happens?

**Transition.** We know where identities live. Next is how someone proves they are that identity. A password is only the starting point.

## Whiteboard / Visual

```text
Headquarters AD  --Entra Connect-->  Microsoft Entra ID
                                         |
                                         | one-way
                                         v
                                 Entra Domain Services
                                 (domain join, GPO, LDAP,
                                  Kerberos/NTLM)
```

## Ask the Class

- What would we recommend to Contoso to keep headquarters employees and cloud accounts as one set of people?
- The 2014 application needs Kerberos and a domain join. Which service, and why is it not Entra Connect?
- A new group is created only inside Domain Services. Does Entra ID learn about it?

## Exam Trap

The three names share "Entra." The exam is testing the job. Directory. Sync. Managed domain. If you answer with the product that shares the most words, you will miss it.

## Transition

Proving identity is authentication. One sign-in for many applications, an extra factor, and sign-in with no password are three different recommendations.

---

# 3. Describe Azure authentication methods

## What Microsoft wants students to know

Authentication establishes the identity of a person, service, or device by requiring credentials. Methods in the unit include passwords, single sign-on, multifactor authentication, and passwordless sign-in. Passwordless is the high-security, high-convenience end of the unit's comparison. Passwords alone are convenient and weak. Single sign-on is only as secure as the first sign-in. Multifactor authentication adds a factor from something you know, something you have, or something you are. Passwordless removes the password and uses a trusted device plus a biometric or a PIN. Entra ID's three passwordless options are Windows Hello for Business, the Microsoft Authenticator app, and FIDO2 security keys.

## Set the scene

**[0:35]** A nurse uses email, the clinic application, and Azure. A stolen password should not be enough. You are choosing how they prove who they are, not what files they may open.

---

### Single sign-on

**Microsoft Learn concept.** The user signs in once and reaches multiple trusted applications. SSO reduces the number of passwords, which lowers credential incidents and reduces lockouts and resets. Access is tied to one identity, so removing the person removes the access. SSO is only as secure as the initial authenticator, because later connections rely on that first sign-in.

**Plain English.** One successful sign-in, many applications. The strength of that first sign-in is the strength of all of them.

**Consultant scenario.** Nurses complain about a different password for email, the schedule, and the clinic app. What would we recommend to Contoso, and why? Single sign-on, and then a strong first factor. SSO alone does not make a weak password safe.

**Instructor talk track.**

Authentication establishes who a person, a service, or a device is, by asking for credentials. In this unit the common methods are passwords, single sign-on, multifactor authentication, and passwordless sign-in.

Single sign-on lets a user sign in once and use multiple trusted applications. Contoso wants that. Fewer passwords means fewer credential incidents, fewer lockouts, and less time resetting passwords. When the nurse changes jobs, access is tied to one identity, so updating or removing that identity updates the applications.

Here is the sentence I will not let you skip. Single sign-on is only as secure as the initial authenticator. Everything after that trusts the first sign-in. If the first sign-in was only a password written on a sticky note, SSO has just handed that sticky note to every application.

So SSO is convenience and cleaner administration. It is not, by itself, a strong factor.

**Analogy.** SSO is one key that opens several doors in the clinic. If someone copies the key, they have all of those doors. The key ring is not a second lock.

**Why an organization would use it.** People need many applications, and the organization wants one identity to grant and remove that access.

**Problem it solves.** Password sprawl, and the mess of turning access off in ten places.

**Common confusion.** SSO versus MFA. They are not alternatives. A user can sign in once to many apps, and that one sign-in can still demand a second factor.

**AZ-900 exam clue.** "Sign in once, many applications" is SSO. "Only as secure as the initial authenticator" is the limit the unit puts on it.

**Check for understanding.** Contoso enables SSO and tells the staff they no longer need multifactor authentication. What is wrong with that announcement?

**Transition.** The stolen password is still the story we have to close. That is a second factor.

---

### Multifactor authentication

**Microsoft Learn concept.** MFA asks for an extra factor so a password alone is not enough. Something the user knows, such as a password or a challenge question. Something the user has, such as a code sent to a phone. Something the user is, such as a fingerprint or a face scan. Microsoft Entra multifactor authentication is the Microsoft service for this. Users can choose an additional form during sign-in, such as a phone call or a mobile app notification.

**Plain English.** Two different kinds of proof. A stolen password still fails if the attacker does not have the phone or the fingerprint.

**Consultant scenario.** A billing password shows up in a dump of leaked passwords. What would we recommend to Contoso, and why? Multifactor authentication, so the password is not sufficient.

**Instructor talk track.**

Multifactor authentication prompts for an extra factor during sign-in. A compromised password is no longer enough.

The factors fall into three categories. Something the user knows: a password or a challenge question. Something the user has: a code sent to a mobile phone. Something the user is: a fingerprint or a face scan. Say those three. The exam likes the categories more than a brand name.

Microsoft Entra multifactor authentication is the service that provides this. The user can choose an additional form, such as a phone call or a mobile app notification.

What would we recommend to Contoso, and why? MFA for the accounts that can reach patient systems, and especially for administrators. We will let Conditional Access decide when the extra factor is required. The factor itself is this unit. The "when" is the next one after external identities.

MFA still uses a password in the classic setup. Passwordless is the step that removes the password. Do not call a text message passwordless.

**Analogy.** The clinic door needs your badge and your face. A copied badge is not enough. The face is a different kind of proof, not a second copy of the badge.

**Why an organization would use it.** Passwords get stolen. A second, different factor stops that theft from becoming a sign-in.

**Problem it solves.** Access that depended on a single secret.

**Common confusion.** MFA versus passwordless. MFA adds a factor. Passwordless removes the password. Also, a code sent to a phone is "something you have," not "something you are."

**AZ-900 exam clue.** Watch for the three categories: know, have, are. Watch for "password alone is not enough."

**Check for understanding.** Name one example of each factor, using a Contoso nurse, not a product brochure.

**Transition.** MFA is stronger, and the password is still there to be phished. Passwordless takes the password out of the sign-in.

---

### Passwordless authentication

**Microsoft Learn concept.** Passwordless replaces the password with a trusted device plus a biometric signal or a PIN. After registration, the user signs in with something they know or are, such as a PIN or a fingerprint, instead of typing a password. Entra ID supports Windows Hello for Business, the Microsoft Authenticator app, and FIDO2 security keys. Windows Hello for Business fits a person with their own Windows PC. The biometric and PIN are tied to that PC. It can integrate with public key infrastructure and supports single sign-on to on-premises and cloud resources. The Authenticator app makes an iOS or Android phone a passwordless factor: the user gets a notification, matches a number on the screen, and confirms with a biometric or a PIN. FIDO2 is an open standard on the WebAuthn specification. The keys are hardware, typically USB, also Bluetooth or NFC. The user selects the key at sign-in. There is no password to expose or guess. The unit calls them unphishable hardware devices.

**Plain English.** No password is typed. A device the person has, plus a PIN or a biometric, completes the sign-in. Contoso's three named options are Windows Hello for Business, Authenticator, and a FIDO2 key.

**Consultant scenario.** Contoso wants administrators to stop typing passwords. The administrators have company Windows PCs. What would we recommend to Contoso, and why? Windows Hello for Business for those designated PCs. A FIDO2 key if the requirement is a hardware device that is not tied to one PC. Authenticator if the phone should be the factor. All three are passwordless. Pick from the person's device, not from a ranking you invent.

**Instructor talk track.**

Passwords remain a usability problem and a theft problem even when MFA sits on top of them. Passwordless authentication removes the password. The replacement is a trusted device plus a biometric signal or a PIN.

After the person registers, they sign in with something they know or something they are, such as a PIN or a fingerprint. They do not type a password.

Microsoft Entra ID supports three passwordless options. I want the three names, and one picture each.

Windows Hello for Business is for an information worker with their own designated Windows PC. The biometric and the PIN are tied to that PC, so someone else cannot use them on a different machine. It supports single sign-on to work resources on-premises and in the cloud. The unit also mentions public key infrastructure integration. You do not need to explain a certificate chain.

The Microsoft Authenticator app turns an iOS or Android phone into a passwordless credential. The user receives a notification, matches a number displayed on the screen, and confirms with a fingerprint, a face, or a PIN. No password.

FIDO2 security keys are hardware. Typically USB. Also Bluetooth or NFC. FIDO2 is an open standard built on WebAuthn. The user registers the key and selects it at the sign-in screen. The hardware performs the authentication. There is no password to guess. The unit describes these keys as unphishable. That is the word to remember, not the radio details.

What would we recommend to Contoso, and why? For nurses who have a personal clinic PC, Windows Hello for Business. For an administrator who wants a key they can carry, a FIDO2 security key. For a phone-first sign-in, Authenticator. Do not recommend SMS as passwordless. SMS can be an MFA factor. It is not on this list of three.

**Analogy.** Passwordless is proving who you are with your own device and your face or your PIN, instead of a word that can be copied. The key fob is the hardware version of that idea.

**Why an organization would use it.** They want high security without asking people to invent and retype passwords.

**Problem it solves.** The password as a thing that can be phished, reused, or guessed.

**Common confusion.** The three passwordless options versus MFA methods in general. Also, Authenticator can be used as an MFA prompt and as a passwordless method. If the stem says the password is eliminated, you are in passwordless. If the stem says an extra factor on top of a password, you are in MFA.

**AZ-900 exam clue.** The three names: Windows Hello for Business, Microsoft Authenticator app, FIDO2 security keys. "Unphishable hardware" is the FIDO2 key. "Tied to the user's PC" is Windows Hello for Business. "Match a number on the phone" is Authenticator.

**Check for understanding.** Which passwordless option would you recommend for a shared front-desk PC that many nurses use, and why is Windows Hello for Business a weak fit there?

**Transition.** Everyone so far has been a Contoso person. The supplier in the lobby is not. Neither is the patient on the website.

## Whiteboard / Visual

```text
Password          convenient, weak
SSO               one sign-in, many apps
                  only as strong as the first sign-in
MFA               know + have + are
Passwordless      no password
                  Hello | Authenticator | FIDO2 key
```

## Ask the Class

- Can Contoso use SSO and MFA together? What does each one add?
- Which three passwordless options does the unit name?
- A text message with a code arrives. Is that passwordless?

## Exam Trap

Students hear "more secure" and answer passwordless for a stem that only says "a second factor." Read whether the password is still in the sign-in.

## Transition

External identities are people, devices, or services outside Contoso's tenant. They can sound like single sign-on. They are not the same problem.

---

# 4. Describe Azure external identities

## What Microsoft wants students to know

An external identity is a person, device, or service outside your tenant. Microsoft Entra External ID is the set of capabilities for working with those users. They use credentials they already have. Contoso still decides what they may access. The external identity provider authenticates them. Contoso authorizes them with Microsoft Entra ID, or, in the unit's words, Azure AD B2C. Three capabilities: B2B collaboration, B2B direct connect, and Microsoft Entra External ID for customers, formerly Azure AD B2C. Guests can be reviewed over time, and access that is no longer needed can be removed.

## Set the scene

**[0:48]** A supplier needs one internal application. A partner's clinicians want a Teams shared channel. Patients need accounts on the public website. Three requests. Three different external identities.

## Instructor Talk Track

An external identity is a person, a device, or a service that exists outside your tenant. Microsoft Entra External ID is how Contoso interacts with users beyond that boundary.

Here is the business problem. Partners, suppliers, vendors, and contractors need approved resources. Contoso should not create a local username and password for each of them. External identities let those people use credentials they already have, while Contoso still enforces access policy.

This is where students often mix up two services. External identities can sound like single sign-on, because the person is not typing a brand-new Contoso password. The unit draws the line. External identities are for cross-tenant and consumer scenarios. The person brings a work account, a government identity, or a social identity such as Google or Facebook. Their identity provider authenticates them. Contoso authorizes them to Contoso's applications.

Three capabilities. Do not collapse them.

B2B collaboration. External users sign in to Contoso's Microsoft applications or other applications, including SaaS apps and custom apps, with the identity they prefer. They are represented in Contoso's directory, typically as guest users. That is the supplier who needs one internal application. What would we recommend to Contoso, and why? B2B collaboration.

B2B direct connect. A mutual, two-way trust with another Microsoft Entra tenant. The unit says it currently supports Teams shared channels. The external person uses Contoso's resources from their own Teams. They are not represented in Contoso's directory. They are visible in the shared channel, and they can be monitored in Teams admin center reports. That is the partner clinic. What would we recommend to Contoso, and why? B2B direct connect. If the stem says "guest in your directory," this is the wrong answer.

Microsoft Entra External ID for customers. The unit still says "formerly Azure AD B2C." This one publishes modern SaaS apps or custom apps to consumers and customers. The unit excludes Microsoft apps from this capability. Patients on Contoso's website are customers, not employees, and not guests in the employee directory. What would we recommend to Contoso, and why? Microsoft Entra External ID for customers.

You can combine them. A supplier and a patient are allowed to need different capabilities in the same company.

One more operational sentence. Guest users can be invited by administrators or by authorized users. Social identities such as Microsoft accounts are included. Over time, Contoso can ask the guest, or a decision maker, to take part in an access review and attest that the guest still needs access. When the review finishes, access for people who no longer need it can be removed. Recognize "access review." Do not build the review workflow in class.

**Analogy.** B2B collaboration is a visitor badge with the visitor's name written in your logbook. B2B direct connect is an agreement that lets a partner walk a shared hallway while they keep their own badge system, and your logbook does not gain a new employee page. External ID for customers is the public clinic portal, where patients are customers of an application, not visitors to the staff directory.

**Why an organization would use it.** People outside the tenant need access, and the organization does not want a homemade account for each of them.

**Problem it solves.** Collaboration and customer sign-in across a tenant boundary, with Contoso still in charge of authorization.

**Common confusion.** Guest in the directory versus not in the directory. Customer application versus a Microsoft app such as Teams. External identity versus SSO.

**AZ-900 exam clue.** "Guest in your directory" is B2B collaboration. "Teams shared channel" and "not in your directory" is B2B direct connect. "Customers of your app," "consumers," or "formerly Azure AD B2C" is Microsoft Entra External ID for customers.

**Check for understanding.** Three Contoso sentences. Supplier in one app. Partner in a Teams shared channel. Patient on the website. Answer with only the capability name.

## Whiteboard / Visual

```text
B2B collaboration     guest in YOUR directory
B2B direct connect    other tenant, Teams shared channel
                      NOT in your directory
External ID customers your app's customers
                      (formerly Azure AD B2C)
                      not for Microsoft apps
```

## Ask the Class

- Why is the supplier not a candidate for External ID for customers?
- Why is the patient not a guest in the employee directory?
- Who authenticates the external user, and who authorizes them to Contoso's application?

## Exam Trap

"They use their own username" is true of all three. The exam is asking where the account lives, and whether the app is a Microsoft app or a customer app.

## Transition

We can name the person. We still have to decide whether this sign-in, from this place, on this device, is acceptable. That decision is Conditional Access.

---

# 5. Describe Microsoft Entra Conditional Access

## What Microsoft wants students to know

Conditional Access allows or denies access based on identity signals: who the user is, where they are, and what device they are using. During sign-in it collects signals, makes a decision, and enforces that decision by allowing access, denying access, or challenging for multifactor authentication. It is useful when MFA should depend on role, location, or network; when only approved client applications should connect; when users must come from managed devices; and when untrusted sources, such as unexpected locations, should be blocked.

## Set the scene

**[0:54]** An administrator signing in from the clinic network is not the same risk as that same administrator signing in from an unfamiliar network. Contoso wants productivity, and they want the extra proof when the situation is unusual.

## Instructor Talk Track

Conditional Access is the tool Microsoft Entra ID uses to allow or deny access based on identity signals. The signals in the unit are who the user is, where the user is, and what device the user is requesting access from. The diagrams also include the application the user is trying to reach.

Here is the business problem. If Contoso requires a second factor on every single sign-in, clinicians will fight it. If Contoso never requires it, a stolen administrator password from a cafe is enough. Conditional Access is the policy in the middle. Users stay productive. Critical assets get more proof when the signals look wrong.

The sequence is the exam sentence. During sign-in, Conditional Access collects signals, makes a decision, and enforces that decision. Enforcement means allow the access, deny the access, or challenge for multifactor authentication.

A concrete picture from the unit. At a known location, the user might not be challenged for a second factor. At an unusual location, or a location marked high risk, access might be blocked, or it might be granted only after a second factor.

When the unit says you would use it:

- Require MFA depending on the requester's role, location, or network. Administrators. People outside trusted network locations.
- Require approved client applications. Limit which email applications can connect to email.
- Require managed devices, meaning devices that meet Contoso's security and compliance standards.
- Block untrusted sources, such as unknown or unexpected locations.

What would we recommend to Contoso, and why? A Conditional Access policy that requires MFA for administrators, and for anyone connecting from outside the clinic's trusted locations. We are not building that policy in a tenant today. Many tenants cannot save one without a license. If we open the portal, we read a template. We find one signal and one enforcement. Then we close it.

This is where students often mix up two services. Conditional Access decides whether the sign-in proceeds. Azure RBAC decides what the account may do to Azure resources after the management request hits Azure Resource Manager. A blocked sign-in never reaches the role check. A Reader role does not decide that the cafe network is suspicious.

**Analogy.** Conditional Access is the receptionist who looks at the badge, the time of night, and whether the person is at the front door or on a video call. Some nights the receptionist asks for a second proof. Some nights the receptionist says no. The receptionist is not the list of which filing cabinets the person may open. That list is RBAC.

**Why an organization would use it.** The same account should be treated differently when the role, the place, the device, or the application changes the risk.

**Problem it solves.** A single sign-in rule for every situation, which is either too harsh or too loose.

**Common confusion.** Conditional Access versus MFA. MFA is a factor. Conditional Access is the policy that may require that factor, or may block, or may allow. Conditional Access versus RBAC. Signal and sign-in, versus permission on a resource.

**AZ-900 exam clue.** Watch for "signals," then "decision," then "allow, block, or require MFA." Watch for "administrators," "outside the trusted network," "managed device," "approved client app," and "unexpected location."

**Check for understanding.** An administrator is at home. A billing clerk is on the clinic network, reading a schedule. Which sign-in should the policy challenge, and which three words describe the mechanism?

**Transition.** The administrator got in. That still does not mean they may delete a storage account. Least privilege is the next decision, and Azure's mechanism is role-based access control.

## Whiteboard / Visual

```text
Signals          who, where, device, app
      |
Decision         allow, block, or require MFA
      |
Enforcement      the action that carries out the decision
```

## Ask the Class

- Name one signal and one enforcement for Contoso's administrators.
- Why is "always MFA for everyone, with no policy" not the same design as Conditional Access?
- A sign-in is blocked. Does RBAC still get a chance to allow the storage account?

## Exam Trap

The sequence "assess, secure, defend" belongs to Defender for Cloud. The sequence "signals, decision, enforcement" belongs here. Students swap them because both sound like a process.

## Transition

Least privilege says the billing clerk who needs to read one storage account should not be able to rewrite the subscription. Azure RBAC is how that limit is applied.

---

# 6. Describe Azure role-based access control

## What Microsoft wants students to know

Least privilege means you grant only the access needed for the task. Azure RBAC assigns built-in or custom roles to people or groups. Each role carries permissions. Access is applied at a scope: management group, subscription, resource group, or a single resource. Permissions granted at a parent scope are inherited by every child scope. The unit's examples are Owner at a management group, who can manage everything in all subscriptions in that management group, and Reader at a subscription, whose members can view every resource group and resource in the subscription. Azure RBAC is enforced on actions that pass through Azure Resource Manager. It does not enforce permissions inside an application or at the data level. It uses an allow model. If one assignment grants read and another grants write on the same scope, the person has both.

## Set the scene

**[1:00]** A new billing clerk joins next Monday. Contoso wants that person to see the finance resources and not change them. They also do not want to edit fifty individual permissions.

## Instructor Talk Track

When several teams share one Azure environment, the question is what each team may do. The principle of least privilege says you grant access only up to the level needed for the task. If someone needs to read one storage blob, they get read access to that blob. They do not get write access. They do not get the other blobs. That is the practice. Doing it person by person, resource by resource, becomes tedious as people and resources change.

Azure RBAC is how Azure lets you control that access with roles instead of a private list for every person. Built-in roles describe common access rules. You can also define your own roles. Each role has a set of permissions. Assign a person, or a group, to a role, and they receive those permissions.

Here is the business problem, in the unit's own hiring picture. You add a new engineer to the group that already has the engineer role. That engineer gets the same access as the others. You add a new resource in that scope, and the group has permissions on the new resource too. Contoso's billing clerk should join a group. The group should already have the right role. We should not build a one-off permission list on Monday morning.

A role is applied at a scope. The scope is the resource, or the set of resources, the access applies to. Four scopes. A management group, which is a collection of subscriptions. A single subscription. A resource group. A single resource.

Azure RBAC is hierarchical. Grant access at a parent scope, and child scopes inherit it. Two examples, in the unit's words. Assign Owner to a user at the management group scope, and that user can manage everything in all subscriptions in the management group. Assign Reader to a group at the subscription scope, and the members can view every resource group and resource in the subscription.

What would we recommend to Contoso, and why? Put the billing clerks in a group. Assign Reader at the finance subscription if they must see everything in that subscription. Assign Reader at one resource group if they must see only that group. Do not assign Owner because they only need to look.

The lab you are about to do also uses Contributor. The unit you just heard names Owner and Reader. Contributor is the built-in role the lab uses for "can change resources in this scope, and cannot grant roles to other people." I am telling you that so question three in the lab is not a surprise. The module sentences you must be able to repeat are inheritance, and the allow model. The Contributor contrast is the bridge into the lab, and it is marked again in the supplemental section.

How enforcement works. Azure RBAC applies to an action against an Azure resource that passes through Azure Resource Manager. You reach Resource Manager from the portal, Cloud Shell, PowerShell, and the CLI. RBAC does not enforce permissions inside an application, and it does not enforce them at the data level. If the clinic application has its own roles, that is the application's problem. Azure RBAC will not police rows inside the patient database.

The allow model. When you are assigned a role, Azure RBAC allows the actions in that role's scope. If one assignment gives you read on a resource group and another gives you write on the same resource group, you have both. There is not a "most restrictive wins" rule in this unit. Permissions combine.

**Analogy.** A role is a job title. A scope is which floor the job title applies to. Reader for the whole building can look into every room. Reader for one room cannot wander. Two job titles on the same floor add up. The title does not reach into the patient chart inside an application. That chart has its own rules.

**Why an organization would use it.** They need least privilege for teams, including people who join later and resources that get created later.

**Problem it solves.** Either everyone is an administrator, or someone is maintaining a private permission list that breaks every time the team changes.

**Common confusion.** RBAC versus Conditional Access. RBAC versus an application role. Inheritance versus "you must assign the role again on every resource." Allow versus "the strictest role wins."

**AZ-900 exam clue.** "Reader at the subscription can view every resource group and resource." "Owner at the management group can manage everything in the subscriptions under it." "Permissions inherit down." "Allow model: read plus write means both." "Not inside the application or the data."

**Check for understanding.** Reader is assigned at the finance subscription. A new virtual machine is created tomorrow in a resource group in that subscription. Can the billing group see it? Why?

**Transition.** RBAC limits what a trusted assignment can do. Zero Trust asks us not to treat the network, or a previous sign-in, as trust that lasts all day.

## Whiteboard / Visual

```text
Management group     Owner here manages every subscription under it
    Subscription      Reader here sees every resource group and resource
        Resource group
            Resource

Allow model: read assignment + write assignment = both
RBAC stops at Resource Manager. Not inside the app. Not inside the data.
```

## Ask the Class

- What would we recommend to Contoso for a clerk who must see finance resources and must not change them?
- One role grants read. Another grants write. Same resource group. What can the person do?
- Can Azure RBAC stop a nurse from opening a patient row inside the clinic application? Where does that control live?

## Exam Trap

Students think a role at a parent scope does not cover new resources, or that a second role cancels the first. Inheritance covers the children, including resources added later. The allow model adds permissions. It does not pick a winner.

## Transition

The old network assumed that if you were inside the building, you were safe. Contoso's nurses are not inside the building. Zero Trust is the model that starts from the opposite assumption.

---

# 7. Describe the Zero Trust model

## What Microsoft wants students to know

Zero Trust assumes breach and verifies each request as though it came from an uncontrolled network. Three principles: verify explicitly, use least privilege access, and assume breach. The old model trusted the internal network. Zero Trust requires authentication and then grants access based on that authentication rather than on location. A user on an unmanaged device on a public network is still evaluated. Low-risk apps might be allowed. Sensitive systems might require MFA. High risk might be blocked.

## Set the scene

**[1:08]** A nurse signs in from a home laptop on a public network and asks for the scheduling application. "They are on the VPN, so they are fine" is the old answer. It is not this model.

## Instructor Talk Track

Zero Trust assumes the worst case and protects resources with that expectation. It assumes breach from the start, and then verifies each request as though the request came from an uncontrolled network.

Here is the business problem. The clinic network is no longer a wall around every device. People work from home. Applications and data are not all in one building. A model that trusts you because of your location does not match the way Contoso works.

Microsoft's three guiding principles:

Verify explicitly. Always authenticate and authorize based on all available data points.

Use least privilege access. Limit access with just-in-time and just-enough access, risk-based adaptive policies, and data protection. You already met least privilege as the reason RBAC exists. This principle is that idea as a security model, not only as a role assignment.

Assume breach. Limit the blast by segmenting access. Verify encryption end to end. Use analytics to see what is happening, detect threats, and improve defenses.

The old picture was a restricted perimeter. Only managed computers joined the network. VPN access was tightly controlled. Personal devices were often blocked. Inside the perimeter, the device was assumed safe. Zero Trust flips that. Everyone authenticates. Access is granted based on authentication, not based on being "inside."

The unit's example. A user signs in from an unmanaged device on a public network. Zero Trust still evaluates identity signals, device state, and risk. You might allow a low-risk app, require MFA for a sensitive system, or block the sign-in when the risk is too high. That example is Conditional Access doing Zero Trust's job at sign-in. The model is bigger than one policy. At this level, the point is that the decision is continuous and depends on context. It is not "the request came from inside, so allow it."

What would we recommend to Contoso, and why? Treat the home laptop as untrusted until the signals say otherwise. Verify the nurse. Give least privilege to the schedule, not to the subscription. Assume that some sign-in, someday, will be hostile, and segment so that one hostile sign-in is not the whole clinic.

**Analogy.** Zero Trust is a hospital that checks identification at every door, even for people who already work there. A coat and a hallway are not proof. The three rules on the wall are: check every time, give only the access this task needs, and assume someone may already be where they should not be.

**Why an organization would use it.** Users, devices, and data are no longer inside one trusted network.

**Problem it solves.** Trust that was based on location.

**Common confusion.** Zero Trust versus a product name. It is a model. Conditional Access and least-privilege RBAC are how pieces of it show up. Also, "assume breach" does not mean "do not bother authenticating." It means design as if an attacker may already have a foothold.

**AZ-900 exam clue.** The three principles, in words close to these: verify explicitly, least privilege access, assume breach. A stem that says "the internal network is trusted" is describing the model Zero Trust replaces.

**Check for understanding.** Say the three principles without looking at the board.

**Transition.** Zero Trust is the attitude. Defense in depth is the stack of layers around the data, so one failure is not the end of the story.

## Whiteboard / Visual

```text
Old: inside the network = trusted
Zero Trust:
  1. Verify explicitly
  2. Least privilege
  3. Assume breach
```

## Ask the Class

- Which principle did we already use when we refused to make the billing clerk an Owner?
- A nurse is on the clinic Wi-Fi. Does Zero Trust say that is enough?
- What would we recommend if the device is unmanaged and the application is the patient record system?

## Exam Trap

A familiar trio is "authenticate, authorize, account," or "detect, respond, recover." Those are not the three Zero Trust principles in this unit.

## Transition

Defense in depth puts the data in the center and stacks protections around it. If one layer fails, the next layer is already there.

---

# 8. Describe defense in depth

## What Microsoft wants students to know

The objective is to protect information and prevent unauthorized people from stealing it. A series of mechanisms slows an attack. Data sits at the center. The layers, in the unit's order, are physical security, identity and access, perimeter, network, compute, application, and data. If one layer is breached, the next is already in place. No single layer is the whole strategy. The layers also produce alerts. Azure offers controls at each layer. The unit's emphasis at each layer is listed in the talk track. Attackers are after data in a database, on a disk in a virtual machine, in a SaaS application such as Office 365, or in cloud storage.

## Set the scene

**[1:12]** Contoso asks which one security product to buy. The honest answer is that no one product is the strategy. The strategy is the set of layers, with the patient records in the middle.

## Instructor Talk Track

The objective of defense in depth is to protect information and to prevent people who are not allowed to have it from stealing it. The strategy uses a series of mechanisms to slow an attack that is trying to reach data.

Picture the data in the center. Every other layer exists to protect that center. If one layer is breached, a later layer is already there. Contoso does not rely on a single control. The layers also give the security team alerts they can act on.

I am going to name the seven layers in the unit's order, and one job each. This is the list. Do not add an eighth.

Physical security. The building and the hardware in the datacenter. This is the first line of defense. Microsoft provides the physical safeguards in its datacenters so the other layers cannot simply be walked around. Contoso does not install Microsoft's badge readers. Contoso still owns physical security for headquarters.

Identity and access. Identities are secure, access is only what is needed, and sign-ins and changes are logged. The unit tells you to control access to infrastructure and change control, to use single sign-on and multifactor authentication, and to audit events and changes. That is this session, sitting as a layer.

Perimeter. Network attacks from the outside. Use DDoS protection to filter large-scale attacks before users lose the service. Use perimeter firewalls to identify and alert on malicious attacks. DDoS is the perimeter, not the network layer. Students swap those two constantly.

Network. Limit communication to what is required. Deny by default. Restrict inbound internet access and limit outbound access where that is appropriate. Implement secure connectivity to on-premises networks. You already did this job with subnets, network security groups, and the choice between a VPN and ExpressRoute. Those are network-layer controls. Do not re-teach them. Place them.

Compute. Malware, missing patches, and loose systems. Secure access to virtual machines. Put endpoint protection on devices. Keep systems patched.

Application. Build security into how the application is written. Keep vulnerabilities out of the code. Store sensitive application secrets in a secure place. The unit names Azure Key Vault. Make security a design requirement, not a coat of paint.

Data. The people who store the data and control access to it are responsible for securing it. Regulations often dictate the controls. Protect data with encryption at rest and encryption in transit. We will say a little more about that in a moment, because the module has a unit for it. Azure services provide encryption. Key Vault can secure the keys and secrets the applications use.

The unit's last warning. In almost all cases, attackers are after data. Data in a database. Data on a disk inside virtual machines. Data in a SaaS application such as Office 365. Data in cloud storage.

What would we recommend to Contoso, and why? Stop looking for the one product. Place each control you already know on a layer. Physical is Microsoft's datacenter plus the clinic's own doors. Identity is Entra ID, MFA, and Conditional Access. Perimeter is DDoS protection. Network is the segmentation and the filters from the networking session. Compute is patching and who can reach a virtual machine. Application is secure code and secrets out of the source code. Data is access control plus encryption, with the patient records as the thing all of this is for.

**Analogy.** Defense in depth is a clinic that does not trust one locked door. There is a fence, a receptionist, a locked ward, a locked cabinet, and a rule about who may read the chart. The chart is the point. The doors exist so that one broken lock is not the chart walking out.

**Why an organization would use it.** Any single control will fail sometime. The data still has to be there when it does.

**Problem it solves.** A design that bets everything on the network, or everything on a password.

**Common confusion.** Perimeter versus network. DDoS and perimeter firewalls are perimeter. Segmentation, deny by default, and limiting internet access are network. Also, identity is its own layer. It is not "part of the network."

**AZ-900 exam clue.** "DDoS" and "large-scale attacks before a denial of service" are the perimeter layer. "Limit communication between resources" is the network layer. "Endpoint protection" and "patched virtual machines" are compute. "Secrets in Key Vault" is called out at the application layer. The data is the center, and it is also the last layer in the list.

**Check for understanding.** I will name a control. You name the layer. Badge reader at the datacenter. MFA. DDoS protection. A network security group. A patched virtual machine. A connection string stored in Key Vault. Encryption of the database.

**Transition.** The data layer just asked for encryption. The module gives that its own short unit. We will honor the unit, and we will not pretend it is one of the eight scored objectives.

## Whiteboard / Visual

Draw concentric rings. Label from the outside in:

```text
Physical
Identity and access
Perimeter          DDoS, perimeter firewall
Network            segment, deny by default
Compute            VM access, patch, endpoint protection
Application        secure code, secrets in Key Vault
Data               the patient records
```

## Ask the Class

- Which layer is DDoS protection, and which layer is an NSG?
- Why does the unit put data in the center and also name data as a layer?
- What would we recommend if Contoso wants to buy "one firewall" and call the design finished?

## Exam Trap

The network layer is where students put every security product they remember. Make them say the job. Filter a giant attack before it becomes a denial of service: perimeter. Limit which resources may talk: network.

## Transition

Encryption is how stored data and moving data stay unreadable to someone who should not have them. Key Vault is where Contoso keeps the keys and the secrets.

---

# 9. Describe encryption and key management

## What Microsoft wants students to know

Encryption protects confidentiality by making data unreadable to unauthorized users. Encryption at rest protects stored data, such as databases, disks, and storage accounts. Encryption in transit protects data while it moves between services, applications, and users. A strong posture includes both. Azure Key Vault stores and controls access to secrets, encryption keys, and certificates, so those values are not sitting in application code or configuration files. Key management lets the organization control who can access them, rotate them, and audit their use. Duties can be separated. The unit also mentions rotation policies and alerts before keys expire, and applications retrieving secrets at runtime with managed identities. At this level, Key Vault is the primary Azure service for secure key and secret storage.

This unit is module content. It is not one of the scored objectives 2.4.1 through 2.4.8. Teach it. Do not build a quiz around it.

## Set the scene

**[1:16]** Patient records sit in Azure Storage and Azure SQL. The application also has a connection string. Contoso wants the records unreadable to the wrong person, and they want that connection string out of the source code.

## Instructor Talk Track

Encryption makes data unreadable to someone who is not allowed to read it. That is confidentiality.

Two forms. Encryption at rest protects data when it is stored: databases, disks, storage accounts. Encryption in transit protects data while it moves between services, applications, and users. A serious design uses both. Encrypting the disk and then sending the record across the network in the clear is half a design. Encrypting the network and storing the file in the clear is the other half.

Contoso's line-of-business application stores patient records in Azure Storage and Azure SQL. Those records should be encrypted where they sit, and encrypted while they move between the application, its APIs, and the user's device.

Azure Key Vault is the service that securely stores and controls access to secrets, such as connection strings and passwords; encryption keys; and certificates. The point is to stop putting those values in application code or in a configuration file someone copies into a repository.

Why it matters. Contoso can control who accesses keys and secrets, rotate them over time, and audit how they are used. They can separate duties, so the person who can view a key is not automatically the person who can rotate it. The unit also says teams set rotation policies and alerts so someone is told before a key expires. That avoids an outage without giving up the rotation. And applications can retrieve secrets from Key Vault at runtime by using managed identities, which reduces hard-coded credentials.

What would we recommend to Contoso, and why? Encrypt the stored records and the path they travel. Put the connection string and the keys in Key Vault. Do not paste them into the application.

I am stopping there. This is the module's encryption unit. This course does not score it as its own objective. If a question on the scored quiz is about Key Vault, it will be because defense in depth named Key Vault as the place for application secrets. You do not need key types, or a rotation schedule, today.

**Analogy.** Encryption is a locked case. At rest, the case is in the storeroom. In transit, the case is in the courier's hand. Key Vault is the lockbox where the key to that case is kept, instead of being taped to the bottom of the case.

**Why an organization would use it.** Confidentiality of stored and moving data, and a single controlled place for secrets and keys.

**Problem it solves.** Readable copies of data, and secrets living in code.

**Common confusion.** Key Vault versus encryption itself. Encryption is the protection. Key Vault is where keys, secrets, and certificates are stored and controlled. Also, this is not Azure RBAC inside the database. RBAC does not police data. Encryption and the application's own access do that work.

**AZ-900 exam clue.** If a stem asks for at rest versus in transit, answer the form that matches stored versus moving. If a stem asks where to keep keys, secrets, and certificates, answer Azure Key Vault. Do not let that become a long configuration conversation.

**Check for understanding.** The database file is encrypted, and the API sends patient JSON with no protection. Which half is missing?

**Transition.** We have designed controls. Contoso still needs something that looks at the estate, scores the posture, and alerts when a threat shows up. That is Microsoft Defender for Cloud.

## Whiteboard / Visual

```text
At rest     stored: database, disk, storage account
In transit  moving: service, app, user

Key Vault   secrets, keys, certificates
            not in source code
```

## Ask the Class

- Which Contoso data needs both forms of encryption?
- Where does the connection string go, and where does it not go?

## Exam Trap

Students answer "Key Vault" when the question is "how is stored data made unreadable," and they answer "encryption" when the question is "where do we keep the key." Split the two.

## Transition

Defender for Cloud is the posture and threat service. It is not the sign-in policy, and it is not the role assignment.

---

# 10. Describe Microsoft Defender for Cloud

## What Microsoft wants students to know

Defender for Cloud is a security posture management and threat protection service. It monitors cloud, on-premises, hybrid, and multicloud resources and gives recommendations and alerts. In Azure it is native and can be enabled quickly. It can cover Azure PaaS such as App Service, Azure SQL, and Storage; data security assessments; and network exposure such as just-in-time VM access. Hybrid machines are included by deploying Azure Arc and enabling the enhanced security features. AWS and Google Cloud can be included. For AWS, the unit names posture recommendations, containers on Amazon EKS, and servers on EC2. Three needs: continuously assess, secure, and defend. Assess includes vulnerability findings. Secure builds on Azure Policy, aligns recommendations to the Microsoft cloud security benchmark, groups them into security controls, and calculates a secure score. Defend raises security alerts with affected resources, suggested remediation, and sometimes a Logic App. Related alerts can be correlated. Advanced protection covers virtual machines, SQL databases, containers, web applications, and networks.

## Set the scene

**[1:18]** Contoso's security lead wants one place that says how they are doing, what to fix first, and when something looks like an attack. The estate is not only Azure. Headquarters servers and a small AWS footprint exist too.

## Instructor Talk Track

Microsoft Defender for Cloud is a security posture management and threat protection service. It monitors cloud, on-premises, hybrid, and multicloud resources. It gives recommendations and alerts so the posture gets better.

Here is the business problem. Contoso can set every control we named today and still not know which one is missing, or which virtual machine is being attacked. Defender for Cloud is the service that watches and advises. It is not a replacement for Entra ID, Conditional Access, or RBAC.

Because it is Azure-native, many Azure services can be monitored without a separate deployment, and it can be enabled quickly. For a hybrid or multicloud estate, it extends that view so the team works from one place. When it needs data collection, it can deploy those components. Azure Arc can extend Defender plans to machines that are not in Azure. The unit also says posture capabilities can assess multicloud resources without an agent. Remember Arc as the bridge for non-Azure machines. Do not architect Arc today.

What it helps detect, in Azure. Threats on platform services such as App Service, Azure SQL, and Storage. Data security assessments and recommendations for services such as Azure SQL and Storage. Network exposure, including just-in-time virtual machine access and tight port policies. Just-in-time access is a defend feature. One sentence. Do not configure it.

Outside Azure. On-premises servers, by deploying Azure Arc and turning on the enhanced security features. Other clouds, and the unit names AWS and Google Cloud. For a connected AWS environment, the unit lists three extensions: posture recommendations and compliance assessments, container protection for Amazon EKS, and server protection for EC2. If you remember "Azure, on-premises, AWS, and Google Cloud," you have the coverage sentence.

Three needs. The unit's headings are assess, secure, and defend.

Continuously assess. Know the posture. Find and track vulnerabilities. Virtual machines, container registries, and SQL servers are in that assessment story. Defender for servers can integrate with Microsoft Defender for Endpoint so vulnerability findings show up in the same experience. You are recognizing "vulnerability assessment," not buying a second product in class.

Secure. Harden resources. The unit says Defender for Cloud builds on Azure Policy, so controls can be scoped at a management group, a subscription, or a tenant. New resources get evaluated against best practices. Recommendations are prioritized, and they align to the Microsoft cloud security benchmark. Recommendations are grouped into security controls. Defender for Cloud calculates a secure score so the team can see posture and choose what to fix first.

Hear that Azure Policy sentence carefully. Defender uses Azure Policy as part of how it evaluates resources. Azure Policy as its own governance tool is the next session. Today, if the question is a score, a recommendation, or a threat alert, the answer is Defender for Cloud. If the question is "enforce a rule that every resource must have a tag," that is Policy, and we are not teaching it yet.

Defend. Security alerts and advanced threat protection. An alert describes the affected resources, suggests remediation, and in some cases can trigger a Logic App. Alerts can be exported. The unit says Defender for Cloud uses kill-chain analysis to correlate related alerts, so you can see where an attack started and what it touched. Advanced protection covers virtual machines, SQL databases, containers, web applications, and networks, including just-in-time VM access and adaptive application controls. Recognize the list. Do not implement it.

What would we recommend to Contoso, and why? Enable Defender for Cloud on the Azure subscriptions, look at the secure score, and work the recommendations. Extend it to headquarters servers with Azure Arc if those servers must be in the same view. Connect AWS only if that footprint is real. Do not tell them Defender for Cloud replaces Conditional Access. One watches and recommends. The other decides a sign-in.

**Analogy.** Defender for Cloud is the clinic's safety inspection plus the alarm company. The inspection posts a score and a punch list. The alarm calls when something is happening. The inspection does not decide who may walk through the door. That is still the receptionist, Conditional Access, and the badge system.

**Why an organization would use it.** They need posture, prioritized fixes, and threat alerts across Azure and, when required, hybrid and other clouds.

**Problem it solves.** Security work with no score, no ordered list, and no alert when an attack starts.

**Common confusion.** Defender for Cloud versus Azure Policy. Defender for Cloud versus Conditional Access. Defender for Cloud versus Microsoft Defender for Endpoint. Endpoint is the vulnerability integration the unit names inside the server story. The service the objective asks for is Defender for Cloud. Also, the old name Security Center is not the name you teach.

**AZ-900 exam clue.** "Secure score," "recommendations," "security alerts," "Azure and on-premises and other clouds." Assess, secure, defend. A stem about signals at sign-in is Conditional Access. A stem about a rule you assign to force resource configuration is leaning toward Azure Policy, which is not this session's product answer.

**Check for understanding.** Contoso wants a score and a list of hardening steps for Azure SQL and for a few headquarters servers. What do you recommend, and what extra piece do the headquarters servers need?

**Transition.** That is the module. We will make the Contoso recommendations in one pass, then you will do the lab, then the short quiz.

## Whiteboard / Visual

```text
Defender for Cloud
  Assess   vulnerabilities, posture
  Secure   recommendations, benchmark, secure score
           (uses Azure Policy; Policy itself is next session)
  Defend   alerts and threat protection

Covers Azure, and can include on-premises (Azure Arc) and other clouds
```

## Ask the Class

- What would we recommend to Contoso if they want a secure score?
- Which sequence is Defender, and which sequence is Conditional Access?
- Does a secure score assign the Reader role? What does?

## Exam Trap

"Continuously assess, secure, and defend" is Defender for Cloud. "Collect signals, decide, enforce" is Conditional Access. Both are three-step stories. The nouns in the stem tell you which one.

## Transition

Stand up. We are in the recommendation meeting. Answer before I confirm.

---

# 11. Consultant pass, lab, and quiz

## What Microsoft wants students to know

The summary says students can now describe directory services, authentication, external identities, Conditional Access, RBAC, Zero Trust, defense in depth, encryption and key management, and the purpose of Defender for Cloud.

## Set the scene

**[1:20]** Five minutes of recommendations if you are on time. If you are late, ask only the eight scored ones and send them to the lab.

## Instructor Talk Track

What would we recommend to Contoso, and why?

Employees who already use Microsoft 365 need a cloud directory. Microsoft Entra ID. They are already authenticating with it.

Headquarters Active Directory must not become a second, hand-maintained list. Microsoft Entra Connect.

The 2014 application needs domain join, group policy, LDAP, or Kerberos, and Contoso will not run domain controllers. Microsoft Entra Domain Services. Remember the sync is one-way, from Entra ID into that domain.

Nurses use several applications and should sign in once. Single sign-on. That first sign-in has to be strong, because SSO is only as secure as the initial authenticator.

A leaked password must not be enough. Multifactor authentication. Something you know, something you have, something you are.

Administrators with their own Windows PCs should stop typing a password. Windows Hello for Business. The other two passwordless names are the Authenticator app and a FIDO2 security key.

A supplier uses their own work account and must appear as a guest. B2B collaboration.

A partner uses Teams shared channels and must not become a guest object. B2B direct connect.

Patients sign in to Contoso's own website. Microsoft Entra External ID for customers. Not a guest account. Not a domain join.

Administrators off the clinic network must prove a second factor. Conditional Access. Signals, then a decision, then allow, block, or MFA.

Billing clerks must see finance resources and not change them. Reader, at the narrowest scope that matches the job. That assignment inherits downward.

The home laptop is not trusted because it is on a VPN. Zero Trust. Verify explicitly, least privilege, assume breach.

No single product is the whole defense. Seven layers, data in the center. DDoS is perimeter. Segmentation is network.

Encrypt the records at rest and in transit. Keep keys and secrets in Key Vault. That unit is real. It is not a scored objective today.

One place for a secure score, recommendations, and threat alerts, including headquarters servers if they deploy Azure Arc. Microsoft Defender for Cloud.

## Lab

**[about 1:25, or 1:20 if the pass ran long]** Open [the Session 7 lab](../../labs/session-07-lab.md).

Part A is the scope prediction. Reader at the subscription is visible on the virtual machine and still cannot restart it. Contributor on one resource group does not reach a different resource group. Contributor does not assign roles. Owner at the management group includes the resource group underneath it. Reader on one storage account does not open the virtual machine beside it.

Part B is portal only if this tenant can do it. Read a Reader role. Read a Conditional Access template and find one signal and one enforcement. Do not require anyone to save a policy. Licensing blocks that in many learner tenants. Glance at Defender for Cloud far enough to see a secure score or a recommendation. If the blade is empty, say so and move on. The no-cost path is to skip Part B.

Part C is the layer sort. Physical, identity, perimeter, network, compute, application, data. Use the board. DDoS is perimeter. An NSG is network.

## Quiz

**[1:50]** [Session 7 quiz](../../quizzes/session-07-quiz.md). Ten items, ten minutes. It is already written. Do not replace it with questions you invent in the room. Review only the items several people missed. If the review runs long, you already spent the lab. Do not skip the quiz to extend the lab.

After class, each student completes the module on Learn, including the module assessment. Do not project Microsoft's assessment items.

## If you remember only 10 things

1. Microsoft Entra ID is the cloud directory. Entra Connect synchronizes on-premises Active Directory with it. Entra Domain Services is the managed domain for domain join, group policy, LDAP, and Kerberos or NTLM, and the sync into that domain is one-way.
2. Single sign-on is one sign-in for many apps, and it is only as secure as the first sign-in.
3. Multifactor authentication adds a factor: something you know, something you have, or something you are. A password alone is not enough.
4. Passwordless removes the password. The three options are Windows Hello for Business, the Microsoft Authenticator app, and FIDO2 security keys.
5. B2B collaboration puts a guest in your directory. B2B direct connect is a two-way trust for Teams shared channels, and those users are not in your directory. External ID for customers is for your application's consumers, formerly Azure AD B2C.
6. Conditional Access collects signals, decides, and enforces: allow, block, or require MFA.
7. Azure RBAC assigns a role at a scope. Child scopes inherit it. Reader at a subscription can view every resource underneath. The model is allow: permissions combine. RBAC does not police the inside of an application or the data.
8. Zero Trust means verify explicitly, use least privilege, and assume breach. Location inside a network is not trust.
9. Defense in depth puts data at the center. The layers are physical, identity and access, perimeter, network, compute, application, and data. DDoS is perimeter. Segmentation is network.
10. Defender for Cloud assesses posture, secures through recommendations and a secure score, and defends with alerts. It can include Azure, on-premises, and other clouds. Encryption at rest and in transit, with keys and secrets in Key Vault, is the module's data-protection unit and is not a separate scored objective in this course.

## Rapid-fire instructor questions

Ask these out loud if the lab finishes early. Do not grade them.

1. Which service synchronizes headquarters Active Directory to the cloud directory?
2. Which service gives you domain join without domain controllers you maintain?
3. Why is SSO not a substitute for MFA?
4. Name the three passwordless options.
5. A supplier is a guest in your directory. Which external identity capability?
6. A Teams shared channel, and the user is not in your directory. Which capability?
7. Say the Conditional Access sequence in three words.
8. Reader is assigned at the subscription. What can that group see?
9. Say the three Zero Trust principles.
10. Which defense-in-depth layer uses DDoS protection?

## Service recognition table

| Business requirement | Azure concept / service | Why | Common wrong answer |
| --- | --- | --- | --- |
| Cloud directory for Microsoft 365, Azure, and apps Contoso builds | Microsoft Entra ID | Cloud identity and access management; subscribers are already using it | Entra Domain Services, which is a managed domain, not the cloud directory |
| Stop maintaining two employee lists, on-premises and cloud | Microsoft Entra Connect | Synchronizes on-premises Active Directory and Entra ID | Domain Services, which does not sync the on-premises directory by itself |
| Legacy app needs domain join, group policy, LDAP, or Kerberos, with no domain controllers to maintain | Microsoft Entra Domain Services | Managed domain services; one-way sync from Entra ID | Entra ID alone, which does not provide those domain features |
| One sign-in, many applications | Single sign-on | Access follows one identity | MFA, which is an extra factor, not the "many apps" feature |
| A stolen password must not be enough | Multifactor authentication | A second category of factor: know, have, or are | SSO, which trusts the first sign-in |
| No password is typed | Passwordless | Windows Hello for Business, Authenticator, or a FIDO2 key | An SMS code, which can be an MFA factor and is not one of the three passwordless options |
| Supplier uses their own work account and appears as a guest | B2B collaboration | External user in your directory, typically a guest | B2B direct connect, whose users are not in your directory |
| Partner collaborates in Teams shared channels from their own tenant | B2B direct connect | Two-way trust; not represented in your directory | B2B collaboration |
| Patients sign in to Contoso's application | Microsoft Entra External ID for customers | Consumer and customer apps; formerly Azure AD B2C | A guest account in the employee directory |
| MFA for administrators, or for sign-ins outside the trusted network | Conditional Access | Signals, decision, enforcement | Defender for Cloud, which scores and alerts rather than deciding the sign-in |
| A clerk may view every resource in a subscription and not change them | Reader role at that subscription | RBAC inheritance covers child scopes | Assigning Reader separately on every future resource |
| Do not trust a device just because it is on the network | Zero Trust | Verify explicitly, least privilege, assume breach | A perimeter firewall as the whole strategy |
| Slow an attacker with more than one control, data at the center | Defense in depth | Seven layers; one failure is not total exposure | "One firewall" |
| A score, prioritized recommendations, and threat alerts | Microsoft Defender for Cloud | Assess, secure, defend; Azure, hybrid, and other clouds | Conditional Access, or Azure Policy as the product name for the score |

---

# Supplemental instructor context

Do not teach this section as part of the module. Use it only when a student asks, or when the lab needs a sentence the unit does not spell out. Say that you are stepping outside the unit, then come back.

**Contributor and role assignment.** The RBAC unit names Owner and Reader and describes inheritance and the allow model. It does not name Contributor. The Session 7 lab asks whether a Contributor on a resource group can assign Reader to someone else. Azure's built-in roles documentation is the source for that contrast: Owner can manage resources and assign roles, Contributor can manage resources and cannot assign roles, Reader can view. If you say that in the lecture, label it as the bridge into the lab. Source: [Azure built-in roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles).

**Azure AD B2C closure.** The external-identities unit says Microsoft Entra External ID for customers was formerly Azure AD B2C, and one sentence still says authorization may be managed with Microsoft Entra ID or Azure AD B2C. The unit does not give a retirement date. This course's gap note is that Azure AD B2C is closed to new customers and that you do not teach B2C click-paths. Use the current name in class. Do not assign a B2C lab.

**Azure Policy.** Defender for Cloud's unit says it builds on Azure Policy. Session 9 teaches Azure Policy as its own objective. Do not preview Policy rules, initiatives, or exemptions today. One sentence is enough: a secure score and recommendations are Defender for Cloud; a configuration rule you assign is a later session.

**Tenant and subscription.** The module uses "tenant" as the identity boundary, especially for external users. The subscription and management group are RBAC scopes from the role unit, and they are the hierarchy from Session 3. A tenant is not a synonym for a subscription. That contrast is a course callback, not a new definition in this module.

---

## Sources

Checked 20 October 2026. The talk track follows these units. It does not reproduce them.

- [Module: Describe Azure identity, access, and security](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/)
- [Introduction](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/1-introduction)
- [Describe Azure directory services](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/2-directory-services)
- [Describe Azure authentication methods](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/3-authentication-methods)
- [Describe Azure external identities](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/4-external-identities)
- [Describe Azure conditional access](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/5-conditional-access)
- [Describe Azure role-based access control](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/6-role-based-access-control)
- [Describe Zero Trust model](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/7-describe-zero-trust-model)
- [Describe defense-in-depth](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/8-describe-defense-depth)
- [Describe encryption and key management in Azure](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/9a-describe-encryption-key-management)
- [Describe Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/9-describe-microsoft-defender-for-cloud)
- [Summary](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/11-summary)
