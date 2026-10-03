# Session 7 instructor notes — Identity, Access, and Security

**Objectives:** 2.4.1–2.4.8
**Slides:** [session-07-slides.md](session-07-slides.md)
**Lab:** [../labs/session-07-lab.md](../labs/session-07-lab.md)
**Quiz:** [../quizzes/session-07-quiz.md](../quizzes/session-07-quiz.md) — 10 items, 10 minutes
**Warm-up:** Session 7 set, weighted to shared responsibility, security and governance benefits, SaaS, and the networking and storage those controls sit on
**Domain minutes:** Domain 1 — 10, Domain 2 — 100, Domain 3 — 10

Eight objectives. The plan is deliberate: they are one story (directory, then sign-in, then what you may do, then posture), and the lab hits several at once. Do not add encryption and key management as a scored topic. The module teaches it; the skills measured do not list it. One sentence of context is enough.

## Run of show

| Min | Block | Leave it when |
| --- | --- | --- |
| 0–10 | Warm-up | |
| 10–35 | Directory services | Entra ID, Connect, and Domain Services are three answers |
| 35–60 | Authentication, external identities, Conditional Access | MFA is not SSO. B2B collaboration is not External ID for customers |
| 60–80 | RBAC, Zero Trust, defense in depth, Defender for Cloud | Reader at subscription scope is understood as inheritance. Defender is not Policy |
| 80–110 | Lab | Scope prediction done. Layer sort done |
| 110–120 | Quiz | 10 minutes, then a short review. If review overflows, cut the demo, not the quiz |

## Teach A (2.4.1)

Say "Microsoft Entra ID" every time. If someone says Azure AD, translate it once and move on. Gap G6 is the naming trap; do not teach B2C click-paths.

Entra Connect is hybrid sync. Domain Services is a managed domain for workloads that still need domain join or legacy protocols. Neither replaces Entra ID. Entra ID is the directory the others relate to.

Tenant vs subscription: identity boundary vs billing and RBAC boundary. Draw both. People will otherwise hear "tenant" as a synonym for subscription for the rest of the course.

## Teach B (2.4.2–2.4.4)

SSO: one sign-in, many apps. MFA: an extra factor. Passwordless: the password is not the thing you type. A user can have SSO and MFA together. They are not alternatives.

External identities, three names only:

- B2B collaboration — guests in your directory.
- B2B direct connect — cross-tenant, Teams shared channels.
- External ID for customers — your app's customers, CIAM. Formerly B2C. Closed to new B2C customers as of May 1, 2025. Do not assign B2C labs.

Conditional Access: signals in, decision out. Example: if the user is an owner and the location is unfamiliar, require MFA. It does not replace RBAC. A blocked sign-in never gets to the role check.

## Teach C (2.4.5–2.4.8)

RBAC sentence: security principal + role + scope. Inheritance down the hierarchy from Session 3. Worked example you will reuse in the lab: Reader on the subscription means Reader on every resource group in it. Contributor does not grant role assignments. Owner does.

Zero Trust, the three principles, verbatim enough to recall: verify explicitly, least privilege, assume breach. Tie least privilege to RBAC scope in one sentence.

Defense in depth: seven layers on the slide. The lab places controls. Do not invent an eighth.

Defender for Cloud: secure score and recommendations. Distinguish it from Azure Policy (Session 9) now, or Session 9 will be muddy: Policy evaluates resource configuration against a rule you assign; Defender for Cloud recommends security improvements and scores posture.

Encryption: context only. "Azure can encrypt data at rest and in transit; key services exist; not an objective we quiz." Then stop.

## Lab

The guided project is the right at-home follow-through. In class, prioritize the paper scope prediction and the layer sort. Those two do not depend on a tenant where guests and role assignments are allowed. Many learner tenants cannot create Conditional Access policies (licensing). Read templates, do not require a saved policy.

## If you are short on time

Cut the Defender portal tour before you cut the RBAC inheritance example. Cut B2B direct connect detail before you cut the three-way external-identity distinction. The quiz is already short. Do not shorten it further.

## Sources

[Identity module](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/) · [Entra ID](https://learn.microsoft.com/en-us/entra/fundamentals/whatis) · [Domain Services](https://learn.microsoft.com/en-us/entra/identity/domain-services/overview) · [Conditional Access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview) · [RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview) · [Zero Trust](https://learn.microsoft.com/en-us/security/zero-trust/zero-trust-overview) · [Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction)
