# Episode 3 solution walkthrough: Categorize and Select, explained

You categorised the portal and picked its controls. Here is the reasoning behind the worked answer, so you can check not just your result but how you got there. Open [fips199-categorization.xlsx](fips199-categorization.xlsx) and [control-selection.xlsx](control-selection.xlsx) alongside.

## Part 1: the categorisation

### The method, in one line

Rate each kind of information the system handles for three things, confidentiality, integrity, and availability. Then the system takes the highest rating in each column. That "highest wins" rule is called the high-water mark, and it exists so that one very sensitive piece of data cannot be hidden behind a pile of harmless data.

### Why each information type is rated the way it is

**Customer profile data shown in the portal: Moderate / Moderate / Moderate.** The portal shows name, contact, and masked account details. A leak would harm customers (so not Low), but the portal shows masked and limited data, and the full sensitive record lives elsewhere. That lands it at Moderate, not High.

**Account balances and history, displayed: Moderate / Moderate / Moderate.** This is the row people want to rate High, and here is the key idea: the portal displays this data, but it is not the authoritative store. The real account data lives in Core Banking (S3), which is categorised separately and higher. At the portal's boundary, the exposure is serious but bounded, so Moderate.

**Session and login tokens: Moderate / Moderate / Moderate.** If someone steals a live session, they get into one account for a while. Bad, but scoped, and the identity service (S5) carries the heavier authentication risk. Moderate.

**Portal content and configuration: Low confidentiality, Moderate integrity and availability.** The pages themselves are not secret (Low confidentiality), but if someone altered them or took them down (integrity and availability), that matters more. This row is a good reminder that the three ratings can differ for the same data.

### The result, and the lesson inside it

High-water mark across all rows: Confidentiality Moderate, Integrity Moderate, Availability Moderate. Overall: **Moderate**.

The lesson is the "why not High" note in the workbook. A bank sounds like it should be High everywhere, and its crown-jewel systems are. But the portal is Moderate because of a deliberate scoping decision: it handles masked, limited data and hands the truly sensitive operations to Core Banking, which is categorised High on its own. Writing that boundary down is the entire reason categorisation exists, so the eventual sign-off is about a defined system, not a vague feeling.

If you rated the portal High because it "touches account data," you were not wrong to think about it, you just scoped the boundary differently. In a real assessment, that is exactly the conversation worth having out loud, and writing down which way you decided and why is the professional move.

## Part 2: the control selection

### Why the Moderate baseline

The categorisation came out Moderate, so you start from the SP 800-53B Moderate baseline, which is 287 controls (the real number, see the reference workbook). You do not invent controls, and you do not start from a blank page. You start from a known-good set and then tailor.

### How to read the worked statuses

The worked sheet marks each control Implemented as Yes, Partly, or No. The pattern mirrors Episode 1 exactly, which is the point: the profile predicted where the gaps would be, and the control detail confirms it.

- **The technical controls are mostly Yes.** IA-2 (MFA), SC-8 and SC-13 (encryption in transit and at rest), AC-3 (access enforcement), CP-9 (backups). Meridian built these early.
- **The process controls are Partly or No.** AU-6 (audit review) is No, because logs are collected but nobody reads them. CA-7 (continuous monitoring) is No, because the programme is not defined yet. AC-2 (account management) is Partly, because joiner-mover-leaver works but the quarterly review does not exist yet.

### Where the gaps go next

Filter the control sheet to the No and Partly rows. Those are precisely the items that flow into the [POA&M](../templates/poam-tracker.xlsx), and the ones you would test in the [control assessment](../templates/control-assessment.xlsx). The chain is: categorise, select, implement, assess, and everything that fails becomes a tracked plan. You have now seen the whole loop on one real system.

## The one check on your own work

Did you try to mark controls "not applicable" to make the list shorter? Be careful. Tailoring a control out is a real, legitimate step, but it needs a reason you would defend to an assessor. "We do not need it" is not a reason. "This control is inherited from the shared identity service and assessed there" is. The discipline is not in shortening the list, it is in justifying every change to it.
