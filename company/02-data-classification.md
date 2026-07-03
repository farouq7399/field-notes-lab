# Meridian Pay: data classification

> Fictional. For teaching only.

Controls cost time and money, so you do not protect everything to the same degree. You protect data according to how much harm its loss would cause. That sorting is called data classification, and it is the quiet foundation under every later decision. If you get this right, categorising a system later is almost easy.

Meridian uses four simple levels. Simple is the point. A scheme nobody can remember is a scheme nobody uses.

## The four levels

| Level | Meaning | Example at Meridian |
|---|---|---|
| Restricted | Loss causes serious harm to customers or the bank | Account numbers, balances, transactions, national ID numbers, card data, passwords |
| Confidential | Internal, and damaging if leaked, but not catastrophic | Employee records, internal reports, contracts |
| Internal | Everyday internal information | Team documents, meeting notes, most email |
| Public | Meant to be seen by anyone | The marketing site, published fees |

## The data Meridian actually holds

| Data type | Level | Why | Lives mainly in |
|---|---|---|---|
| Customer identity data (name, address, date of birth, national ID) | Restricted | Directly identifies a person and enables fraud if leaked | S3, S6 |
| Account and transaction data (balances, transfers) | Restricted | It is the customer's money and financial history | S3, S4, S6 |
| Authentication data (password hashes, multi-factor secrets) | Restricted | The keys to every account | S5 |
| Payment card data (card numbers, held as tokens) | Restricted | Strictly regulated, high fraud value | S4 |
| Support notes and tickets | Confidential | Often contain snippets of customer detail | S7 |
| Employee and payroll records | Confidential | Sensitive personal data about staff | S9 |
| Internal reports and analytics | Confidential | Reveal how the business runs | S6 |
| Team documents and email | Internal | Everyday work | S8 |
| The marketing website and published fees | Public | Deliberately public | Public site |

## How to read this like a professional

**Most of Meridian's crown-jewel data is Restricted, and it clusters in a few systems.** That is normal, and it is good news. It means your strongest controls have a small number of places to defend: the core banking platform, the payments service, the identity service, and the data warehouse copy. Follow the Restricted data and you find the systems that matter.

**Watch the copies.** The data warehouse (S6) is not where the data is born, but it is where a lot of it ends up, copied for reporting. Copies are easy to forget and just as sensitive as the original. A recurring real-world lesson: the breach is often not the guarded original, it is the forgotten copy.

**Card data is a special case.** Because it is card data, a separate industry rule set (the card scheme rules) applies on top of anything NIST says. This lab stays focused on the NIST way of thinking, but it is worth knowing that real financial systems answer to more than one rule book at once.

## How this feeds the next steps

When Episode 3 asks you to categorise the Customer Web Portal, the first question is "what is the worst thing that happens if the data it touches is exposed, altered, or made unavailable." You have already answered most of that here. Classification is the homework that makes categorisation quick.

## Where to go next

- Back to the [system inventory](01-system-inventory.md)
- On to Episode 1 and build Meridian's Cybersecurity Framework profile
