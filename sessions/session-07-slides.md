# Session 7 slides — Identity, Access, and Security

Each `##` heading is one slide. Notes: [session-07-instructor-notes.md](session-07-instructor-notes.md).

## 1. Identity, access, and security

Session 7. Eight objectives. Who the user is, what they may do, and how Azure watches the estate.

## 2. Three directory services

**Microsoft Entra ID.** The cloud directory. Users, groups, and applications for Azure and for Microsoft 365. This used to be called Azure Active Directory. Use the current name.

**Microsoft Entra Connect.** Syncs an on-premises Active Directory into Entra ID so people can be hybrid.

**Microsoft Entra Domain Services.** A managed domain (domain join, LDAP, Kerberos, NTLM) without you running domain controllers. It is not "Active Directory in a virtual machine," and it is not Entra ID itself.

## 3. Tenant, directory, subscription

The **tenant** is the organization's Entra directory. One identity boundary.

A **subscription** lives under that tenant and is still the billing and access boundary from Session 3.

You sign in to the directory. You are authorized against a subscription, a resource group, or a resource.

## 4. Authentication

**Single sign-on (SSO).** One authentication, many applications.

**Multifactor authentication (MFA).** More than one factor. Something you know, something you have, something you are.

**Passwordless.** Sign-in without a password as the primary secret. The phone prompt, a security key, or biometrics, depending on the method. It is still authentication. It is not "no identity."

## 5. External identities

**B2B collaboration.** A guest from another organization, in your tenant, for your apps.

**B2B direct connect.** Cross-tenant access, used for shared channels in Teams. The person is not a guest object the way B2B collaboration creates one.

**Microsoft Entra External ID for customers.** Your customer-facing sign-in, for apps you publish to your own customers.

Do not learn Azure AD B2C procedures. That product is closed to new customers. The exam name to use is External ID for customers.

## 6. Conditional Access

An if-then policy on the sign-in.

Signals include user, location, device state, application, and risk.

Outcomes include allow, require MFA, or block.

It is not a resource firewall. It decides whether this sign-in is acceptable.

## 7. Azure RBAC

Role-based access control answers: this identity, this role, this scope.

Scopes, broad to narrow: management group, subscription, resource group, resource.

A role assigned at a subscription applies to the resource groups and resources under it. Inheritance moves down.

**Reader** looks. **Contributor** changes resources but does not hand out access. **Owner** does both, including assigning roles.

## 8. Zero Trust

Three principles:

- Verify explicitly.
- Use least privilege.
- Assume breach.

Never trust a network location alone. A private IP is not a free pass.

## 9. Defense in depth

Layers, outer to inner. A failure at one layer is not a failure of the whole design.

1. Physical
2. Identity and access
3. Perimeter
4. Network
5. Compute
6. Application
7. Data

An NSG is network. MFA is identity. A lock on a storage account's data is data. We sort these in the lab.

## 10. Microsoft Defender for Cloud

A posture tool for your Azure estate (and, with more setup, beyond it).

It gives you a secure score and a list of recommendations. It is not the same product as endpoint antivirus, and it is not Azure Policy. Policy says what a resource may look like. Defender for Cloud tells you where security configuration is weak.

## 11. Lab and quiz

The quiz is 10 minutes today so the practice can breathe. Eight new items plus two carried forward.

Assignment: [Describe Azure identity, access, and security](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/).

Session 8 opens with the Domain 2 checkpoint. Everything from architecture through today is in scope.
