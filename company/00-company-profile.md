# Meridian Pay: the company you are securing

> Everything in this lab is fictional. Meridian Pay is a made-up company invented for teaching. The policies, systems, and data are examples to practise on, not real security advice for any real organisation. Any resemblance to a real company is coincidental.

You cannot practise a framework in the abstract. So the Field Notes Lab gives you one company to point everything at. Read this page once, then keep it open while you work through the episodes.

## The one-paragraph version

Meridian Pay is a small, mobile-first digital bank. Customers open a current account and a savings account from their phone in a few minutes, get a debit card, send money to friends, and see simple budgeting. There are no branches. Everything runs in the cloud. The company is four years old, it has about 140,000 customers, and it employs around 180 people, most of them working remotely with one small head office.

## The facts to hold on to

| Item | Detail |
|---|---|
| Legal name | Meridian Digital Bank Ltd. |
| Trades as | Meridian Pay |
| Founded | 2021 |
| Size | About 180 employees |
| Customers | About 140,000 retail customers |
| Product | Mobile current and savings accounts, a debit card, person-to-person payments, budgeting |
| Offices | One small head office (staff and network gear only, no servers) |
| Where the systems live | The public cloud (AWS). No data centre of its own. |
| Corporate tools | Microsoft 365 for email and documents; laptops for staff |

## Who does what (the small security team)

Meridian Pay is too small to have a large security department. That is deliberate, and it is realistic. Most organisations you will ever advise look like this.

- **Head of Security (the CISO).** One person. Owns the security programme, reports to the Chief Technology Officer. This is who signs things off.
- **Two security engineers.** They run the day-to-day: monitoring, patching, reviews.
- **A platform (DevOps) team of six** who actually build and run the systems, and who own most of the technical controls in practice.
- **A Head of Risk and Compliance** on the business side, who cares about regulators and audits.

Notice already how this maps to GRC. The Head of Risk and Compliance lives in the G and the C. The security team lives in the R and the technical controls. Keep that in the back of your mind.

## The third parties Meridian relies on

A modern bank is not one system. It is a handful of its own systems stitched to a set of outside providers. These matter because your risk does not stop at your own edge.

- **AWS**: hosts all of Meridian's systems.
- **CardaX** (fictional): the card processor that issues the debit cards and moves card transactions.
- **VerifyNow** (fictional): the identity-verification vendor that checks a new customer is who they say they are (the "know your customer" check).
- **A messaging provider** (fictional): sends the one-time passcodes over SMS and the transactional emails.

When you reach the supply-chain and third-party parts of the framework, these are the names you will be reasoning about.

## Why a bank is a good thing to practise on

Three reasons, and they are the same reasons a real regulator pays attention to a bank.

1. **The data is sensitive.** Names, addresses, dates of birth, national ID numbers, account balances, and transactions. If this leaks, real people are harmed.
2. **The integrity has to hold.** A balance that silently changes, or a payment that is altered in flight, is a direct loss. It is not just embarrassing, it is money.
3. **It has to be available.** If customers cannot reach their money, that is a serious incident on its own.

Those three words, confidentiality, integrity, and availability, are going to come back in Episode 3 when you categorise a system. You just met them in plain language first.

## Where to go next

- The systems Meridian runs: see [01-system-inventory.md](01-system-inventory.md).
- The data Meridian holds and how sensitive each kind is: see [02-data-classification.md](02-data-classification.md).
- A picture of how it all fits together: see [diagrams/](diagrams/).

Then start with Episode 1, and build Meridian's Cybersecurity Framework profile.
