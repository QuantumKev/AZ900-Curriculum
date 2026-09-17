# Session 7 Quiz — Azure Identity, Access, and Security

**Time:** 10 minutes · **Items:** 10 · **Composition:** 8 new, 2 carry-forward (S1–S6)
**Objectives:** 2.4.1, 2.4.2, 2.4.3, 2.4.4, 2.4.5, 2.4.6, 2.4.7, 2.4.8
**Carry-forward objectives:** 1.1.2, 1.2.3
**Target:** 80%

Shortened to 10 minutes so the guided project keeps its full 30 minutes. One item per new
objective, deliberately rapid.

---

## Questions

**1.** An organization has applications that require traditional domain features — domain join, group policy, LDAP, and Kerberos or NTLM authentication — but does not want to deploy and maintain domain controllers in Azure. Which service fits?

- A. Microsoft Entra ID
- B. Microsoft Entra Domain Services
- C. Microsoft Entra Connect
- D. Microsoft Defender for Cloud

**2.** Which three passwordless authentication options does Microsoft Entra ID support?

- A. SMS codes, security questions, and email links
- B. Windows Hello for Business, the Microsoft Authenticator app, and FIDO2 security keys
- C. Smart cards, RADIUS tokens, and one-time passwords
- D. Password managers, biometrics, and CAPTCHA

**3.** A supplier's staff need access to one internal application using their own work identities, and they should appear in your directory as guests. Which capability is this?

- A. B2B collaboration
- B. B2B direct connect
- C. Microsoft Entra External ID for customers
- D. Microsoft Entra Domain Services

**4.** During sign-in, Conditional Access performs which sequence?

- A. Encrypt, transmit, decrypt
- B. Collect signals, make a decision, enforce the decision
- C. Authenticate, authorize, audit
- D. Assess, secure, defend

**5.** You assign the Reader role to a group at subscription scope. What can members of that group do?

- A. Read every resource group and resource in that subscription
- B. Read only the resources created after the assignment
- C. Read and modify resources in the subscription
- D. Nothing until the role is also assigned at each resource group

**6.** Which statement about Azure RBAC is correct?

- A. RBAC uses a deny model, so the most restrictive assignment wins
- B. RBAC uses an allow model, so permissions from multiple assignments combine
- C. RBAC enforces permissions inside applications and at the data level
- D. RBAC assignments do not inherit to child scopes

**7.** Which three principles guide the Zero Trust model?

- A. Trust but verify, defend the perimeter, encrypt everything
- B. Verify explicitly, use least privilege access, assume breach
- C. Authenticate, authorize, account
- D. Detect, respond, recover

**8.** In the defense-in-depth model, which layer uses DDoS protection to filter large-scale attacks before they cause a denial of service for users?

- A. The network layer
- B. The perimeter layer
- C. The compute layer
- D. The identity and access layer

**9.** *(Carry-forward)* A security team wants a single place to see a score representing their security posture, receive prioritized hardening recommendations aligned to a security benchmark, and get alerts on detected threats — covering Azure, on-premises servers, and workloads in AWS. Which service provides this?

- A. Azure Monitor
- B. Microsoft Defender for Cloud
- C. Azure Policy
- D. Microsoft Entra Conditional Access

**10.** *(Carry-forward)* For a platform-as-a-service database, which responsibilities remain with the customer?

- A. Patching the database engine and the underlying operating system
- B. The data stored in the database, and the identities and access granted to it
- C. The physical hosts and physical network
- D. Nothing; PaaS transfers all responsibility to the provider

---

## Answer key

| Q | Answer | Objective | Why | Source |
| --- | --- | --- | --- | --- |
| 1 | B | 2.4.1 | Microsoft Entra Domain Services provides a managed domain — domain join, group policy, LDAP, Kerberos/NTLM — without deploying domain controllers. Entra ID is the cloud identity service; Entra Connect synchronizes on-premises Active Directory with Entra ID. | [Azure directory services](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/2-directory-services) |
| 2 | B | 2.4.2 | The three supported passwordless options are Windows Hello for Business, the Microsoft Authenticator app, and FIDO2 security keys. SMS and one-time codes are additional MFA factors, not passwordless methods. | [Azure authentication methods](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/3-authentication-methods) |
| 3 | A | 2.4.3 | B2B collaboration lets external users sign in with their preferred identity and represents them in your directory, typically as guests. B2B direct connect users are not represented in your directory. External ID for customers (formerly Azure AD B2C) is for consumer-facing apps. | [Azure external identities](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/4-external-identities) |
| 4 | B | 2.4.4 | Conditional Access collects signals such as user, location, device, and application, decides based on them, and enforces by allowing, blocking, or challenging for MFA. D is the Defender for Cloud framing. | [Azure conditional access](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/5-conditional-access) |
| 5 | A | 2.4.5 | RBAC is hierarchical: a role assigned at a parent scope is inherited by all child scopes, so Reader at subscription scope covers every resource group and resource beneath it, existing and future. | [Azure role-based access control](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/6-role-based-access-control) |
| 6 | B | 2.4.5 | RBAC uses an allow model — if one assignment grants read and another grants write on the same scope, you have both. It is enforced through Azure Resource Manager and does not reach inside applications or data. | [Azure role-based access control](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/6-role-based-access-control) |
| 7 | B | 2.4.6 | Verify explicitly, use least privilege access, assume breach. Zero Trust replaces the assumption that a location inside the network is inherently safe. | [Zero Trust model](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/7-describe-zero-trust-model) |
| 8 | B | 2.4.7 | The perimeter layer uses DDoS protection and perimeter firewalls to filter and alert on large-scale attacks. The network layer limits communication between resources through segmentation and access controls. | [Defense in depth](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/8-describe-defense-depth) |
| 9 | B | 2.4.8 | Defender for Cloud provides security posture management with a secure score, recommendations aligned to the Microsoft cloud security benchmark, and security alerts, spanning Azure, hybrid via Azure Arc, and other clouds including AWS and GCP. | [Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/9-describe-microsoft-defender-for-cloud) |
| 10 | B | 1.1.2, 1.2.3 (carry-forward) | Data, identities, and access always remain the customer's responsibility. In PaaS the provider maintains the platform and operating system, and the physical layers are always the provider's. | [Shared responsibility model](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/4-describe-shared-responsibility-model) · [Platform as a Service](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/3-describe-platform-service) |

**Instructor note:** items 5 and 6 are the two most valuable in this set. RBAC inheritance
and the allow model reappear in Session 9 as the contrast case for Azure Policy and
resource locks, and in the Session 10 carry-forward block.
