# The RMF, walked through one system, start to finish

> Pairs with the Field Notes article "RMF without the jargon." Fictional Meridian Pay.

The Risk Management Framework can sound like a bureaucratic checklist. It is easier to understand as one story: how a single system goes from "we are thinking about this" to "a responsible person has formally accepted the risk, and we are keeping an eye on it." So we will follow one system, the Customer Web Portal (S2), through all seven steps.

Keep the [system-boundary diagram](../company/diagrams/system-boundary.png) open while you read. And track the same steps in [rmf-step-tracker.xlsx](rmf-step-tracker.xlsx).

## Step 1: Prepare

Before anything formal, you get your bearings. Who owns this system. What does it do. Who are its users. What is Meridian's risk appetite, and what common controls does the portal inherit from the platform it runs on (for example, the cloud's physical security, or the company-wide identity service).

For the portal: the platform team owns it, a data owner is named, and it inherits identity and logging from shared services. Prepare is the step people skip and later regret, because everything after it assumes you did.

## Step 2: Categorize

Now you rate the system's impact: what is the worst that happens if its data is exposed, altered, or made unavailable. You do this against confidentiality, integrity, and availability, using FIPS 199, and the system takes the highest of the three (the high-water mark).

For the portal, the answer is **Moderate**. That surprises some people, because a bank sounds like it should be High everywhere. The reason it is Moderate is a scoping decision: the portal shows masked and limited data and hands the truly sensitive operations to the Core Banking system. The authoritative account data, which is High, is categorised separately with Core Banking (S3). Writing the boundary down is what makes this defensible. See the worked [FIPS 199 workbook](../episode-03-categorize-select/fips199-categorization.xlsx).

## Step 3: Select

The category picks your starting set of controls. A Moderate system starts from the SP 800-53B Moderate baseline. Then you tailor: some controls do not apply, some need to be stronger, some are inherited from shared services so you do not re-do them.

You are not inventing controls from nothing. You start from a known-good baseline and adjust it with reasons written down. See the [control-selection workbook](../episode-03-categorize-select/control-selection.xlsx).

## Step 4: Implement

Put the controls in place, and just as importantly, write down how each one is actually implemented. That written description is the beginning of the System Security Plan, the document that says "here is how this system meets each control." For the portal, most technical controls already exist (encryption, MFA, a web firewall). Implement is largely about documenting them honestly, including the gaps.

## Step 5: Assess

Someone independent enough to be objective tests whether the controls really work, not whether they are written down. They produce a findings report. Anything that fails, or is only partly there, becomes an entry on the Plan of Action and Milestones (the POA&M), the master list of weaknesses and how they get fixed. See [poam-tracker.xlsx](../templates/poam-tracker.xlsx).

Assess is where "compliant on paper" and "actually secure" are forced to meet. It is the honest step.

## Step 6: Authorize

A responsible leader, at Meridian the CISO, looks at the assessment and the remaining risks and makes a decision: I accept this risk and authorise the system to operate, or I do not. This is a real signature by a real person who is accountable. It is not a rubber stamp, and it is not the security team marking its own homework.

The output is an authorisation decision, often with conditions ("operate, but close these three POA&M items within 90 days").

## Step 7: Monitor

Authorisation is not the end. Systems change, threats change, and controls drift. So you keep watching: monitor the controls, re-assess when something significant changes, and feed what you learn back in. A modern programme aims for continuous monitoring rather than a once-a-year scramble.

And then, quietly, the loop connects back to the top. What you learn monitoring the portal updates Meridian's CSF profile from Episode 1, which changes the priorities, which changes what you do next.

## The whole thing in one breath

Prepare so you know what you are dealing with. Categorize so effort matches impact. Select a sensible starting set of controls and tailor it. Implement them and write it down. Assess whether they actually work. Authorize with a real, accountable signature. Monitor so it stays true. Seven steps, one system, from idea to accountable sign-off.
