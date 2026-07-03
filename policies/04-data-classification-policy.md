# Data Classification Policy

> Fictional. Meridian Pay teaching example. Not real advice.

Document owner: Head of Risk and Compliance
Version: 1.0
Review: once a year

## Purpose

You cannot protect everything to the same degree, and trying to is how small teams burn out. This policy sets how Meridian labels information by sensitivity, so that the strongest controls land on the data that matters most.

## Scope

All information Meridian creates, receives, or holds, in any system, including copies held by providers.

## The four levels

| Level | Meaning | Handling in short |
|---|---|---|
| Restricted | Loss causes serious harm to customers or Meridian | Encrypted at rest and in transit, access strictly limited and logged, never on personal devices |
| Confidential | Internal, damaging if leaked, not catastrophic | Access limited to those who need it, kept in approved systems |
| Internal | Everyday internal information | Kept inside Meridian's approved tools |
| Public | Meant to be seen by anyone | No restriction |

## Policy

1. **Everything has an owner.** Each significant set of data has a named owner who decides its classification.
2. **Classify at the highest level that applies.** If a document mixes levels, it takes the highest one in it.
3. **Restricted data gets the strongest handling.** Encryption, tight access, logging, and no copies to unapproved places. This covers customer identity data, account and transaction data, authentication data, and card data.
4. **Copies inherit the label.** A copy of Restricted data in the data warehouse is still Restricted. Reporting convenience does not lower the sensitivity.
5. **Label where practical.** Documents and stores are labelled so people know what they are handling.
6. **Card data carries extra rules.** Beyond this policy, card data is subject to the card scheme rules, which are stricter.

## Roles

- **Data owners**: set and review classifications.
- **Head of Risk and Compliance**: owns the scheme and resolves disputes.
- **Platform team**: enforce the technical handling (encryption, access, logging).

## How this maps to NIST

This policy is the bridge between two framework ideas. It supports the **Identify** function (you cannot manage data risk you have not classified) and it directly feeds the **Categorize** step of the Risk Management Framework. When Episode 3 asks how bad it would be if a system's data were exposed, altered, or lost, the answer starts from the labels set here. See the worked example in [company/02-data-classification.md](../company/02-data-classification.md).
