# Access Control Policy

> Fictional. Meridian Pay teaching example. Not real advice.

Document owner: Head of Security (CISO)
Version: 1.0
Review: once a year

## Purpose

Most breaches come down to someone, or something, having access they should not have had. This policy sets how Meridian grants, reviews, and removes access so that people and systems can reach what they need and nothing more.

## Scope

Every Meridian system in the [inventory](../company/01-system-inventory.md), and every account on them, human or machine.

## Policy

1. **Least privilege.** Access is granted at the lowest level that still lets the person or system do its job. Broad or standing admin rights are avoided.
2. **Role based.** Access is assigned to roles (for example, "support agent" or "payments engineer"), and people are placed in roles. Access is not granted person by person on a whim.
3. **Strong authentication.** All staff and all customers use multi-factor authentication. Passwords alone are never enough for any Restricted system.
4. **Unique identity.** Every person has their own account. Shared logins are not allowed. Machine accounts are named and owned by a person.
5. **Joiners, movers, leavers.** Access is granted when someone joins a role, changed when they move, and removed the same day they leave. This process is owned jointly by HR and the platform team.
6. **Privileged access is extra careful.** Administrative access to crown-jewel systems (S3, S4, S5) requires separate approval, is logged, and is reviewed monthly.
7. **Access is reviewed.** Every quarter, system owners confirm that the people with access still need it. Access that cannot be justified is removed.

## Roles

- **System owners**: approve access to their systems and run the quarterly review.
- **Platform team**: implement grants and removals.
- **HR**: triggers the joiner, mover, and leaver process.
- **CISO**: owns the policy and approves privileged-access exceptions.

## How this maps to NIST

This is mostly the **Protect** function, and specifically the Identity Management, Authentication, and Access Control area of the Cybersecurity Framework Core. The joiner-mover-leaver rule and the quarterly review are the kind of concrete, testable controls an assessor looks for. In the control catalogue, this policy is where the Access Control (AC) and Identification and Authentication (IA) families come to life.
