# Meridian Pay: system inventory

> Fictional. For teaching only.

Before you can secure anything you have to know what you have. This is Meridian's list of systems. In the framework this list is part of the Identify function, and it is the single most useful thing a small team can actually finish.

Read the table, then read the notes under it. The notes are where the real thinking is.

| # | System | What it is | Who uses it | Sensitivity (plain words) |
|---|---|---|---|---|
| S1 | Mobile App | The iOS and Android app customers bank from | Customers | High. It is the front door to everything. |
| S2 | Customer Web Portal | The website version of the app | Customers | High. Same data as the app, exposed to the internet. |
| S3 | Core Banking Platform | The service and database that hold accounts, balances, and transactions | Internal systems | Highest. This is the crown jewels. |
| S4 | Payments Service | Moves money and talks to the card processor | Internal systems | Highest. Touches money directly. |
| S5 | Identity and Access Service | Logs customers and staff in, runs multi-factor | Everyone | Highest. If this falls, everything falls. |
| S6 | Data Warehouse | A copy of data used for reporting and analytics | Analysts, Risk team | High. It is a large pile of copied customer data. |
| S7 | Internal Admin Console | Where staff service customer accounts | Support and operations staff | High. Powerful, and a favourite target. |
| S8 | Corporate IT (M365, laptops) | Email, documents, staff devices | All staff | Medium to high. The way most attacks actually start. |
| S9 | HR System (a SaaS product) | Payroll and employee records | HR | Medium. Employee data, not customer data. |

## The notes that matter

**The crown jewels are S3, S4, and S5.** If you only had time to protect three things, it would be the core banking platform, the payments service, and the identity service. A useful habit: for any organisation, find the two or three systems that would end the company if they failed, and make sure they get the most attention. Everything else is triage after that.

**The internet-facing systems are S1, S2, and S7.** These are the ones an outsider can reach. The mobile app and the web portal are meant to be public. The admin console should not be, and one of the classic mistakes is leaving an internal console reachable from the internet. When you get to the framework, "know what is exposed" is a specific outcome, and this is why.

**S8 is the boring one that gets you.** Corporate IT, email and laptops, is not glamorous, but the majority of real breaches start with a phished employee or a stolen laptop, not a clever attack on the core banking system. Do not let the exciting systems pull all your attention.

**S9 holds employee data, not customer data.** It still matters, but the impact if it leaks is different, and that difference is exactly the kind of judgement the categorisation step in Episode 3 is going to make you write down on purpose.

## The system we will follow all the way through

For the Risk Management Framework in Episode 2, we take one system and walk it from idea to sign-off: the **Customer Web Portal (S2)**. It is a good teaching choice because it is exposed to the internet, it touches sensitive data, and it is small enough to reason about in one sitting. Keep an eye on S2.

## Where to go next

- How sensitive each kind of data is: [02-data-classification.md](02-data-classification.md)
- The picture: [diagrams/](diagrams/)
