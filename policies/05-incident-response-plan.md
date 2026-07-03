# Incident Response Plan

> Fictional. Meridian Pay teaching example. Not real advice.

Document owner: Head of Security (CISO)
Version: 1.0
Review: once a year, and after every real incident

## Purpose

Something will go wrong eventually. This plan says what Meridian does when it does, so that in the worst moment people are not inventing a process under pressure. A plan you rehearsed beats a clever plan you improvised.

## Scope

Any event that could harm the confidentiality, integrity, or availability of Meridian systems or data. This ranges from a phished laptop to a suspected breach of the core banking platform.

## The six phases

Meridian uses the well-known incident lifecycle, in plain words.

1. **Prepare.** Keep the tools, contacts, and access ready before anything happens. Keep this plan current and rehearsed.
2. **Detect and report.** Anyone who notices something wrong reports it to the security team, day or night, through the on-call channel. Monitoring alerts feed the same place.
3. **Assess and triage.** The security team decides: is this a real incident, and how bad. Severity is set from Low to Critical, which decides who gets woken up.
4. **Contain.** Stop it spreading. Isolate the affected system or account. For a suspected account takeover, disable the account first and investigate second.
5. **Eradicate and recover.** Remove the cause, restore clean systems from known-good backups, and confirm the service is healthy before calling it done.
6. **Learn.** Within two weeks, hold a blameless review. What happened, what worked, what to change. Update this plan and the controls.

## Severity and who responds

| Severity | Example | Who is involved |
|---|---|---|
| Low | One phished laptop, contained | Security engineer on call |
| Medium | Suspected exposure of Confidential data | Security team, system owner |
| High | Suspected exposure of Restricted customer data | CISO, platform team, Head of Risk |
| Critical | Core banking or payments compromised, or funds at risk | CISO, CTO, executive team, legal |

## Roles

- **Incident lead**: runs the response, usually a senior security engineer or the CISO.
- **CISO**: owns the plan, decides on High and Critical, and handles the executive line.
- **Head of Risk and Compliance**: handles regulator and reporting obligations.
- **Platform team**: does the containment and recovery.
- **Communications**: one named person owns what is said, internally and to customers.

## Contacts

Kept in a separate, always-reachable contact sheet: on-call security, CISO, CTO, key providers (AWS, CardaX), and legal. The contact sheet is not stored only inside a system that an incident might take down.

## How this maps to NIST

This plan is the **Respond** and **Recover** functions of the Cybersecurity Framework, made concrete. The six phases mirror the incident-handling lifecycle in NIST's incident guidance. The "Learn" phase is what turns a bad day into a better programme, and it is the step teams most often skip. In the control catalogue this is the Incident Response (IR) family.
