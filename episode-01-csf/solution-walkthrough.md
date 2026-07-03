# Episode 1 solution walkthrough: the CSF profile, explained

You filled in the blank profile. Now check your thinking against this. There is no single right answer for a profile, it is a judgement, but the reasoning matters, and that is what this page shows. Open [meridian-csf-profile.xlsx](meridian-csf-profile.xlsx) alongside it.

## First, how to read the shape

Do not look at individual rows first. Look at the summary by function, and at where the red gaps cluster. For Meridian the pattern is the story:

- **Strong where a young cloud company is usually strong.** Identity and access (PR.AA), data security (PR.DS), and policy (GV.PO) are rated 3. A four-year-old bank built on AWS tends to get encryption, MFA, and role-based access right early, because the cloud makes them easy and the business demands them.
- **Weak where a young company is usually weak.** The lowest scores, a Current of 1, land on Oversight (GV.OV), adverse-event analysis (DE.AE), improvement (ID.IM), and incident analysis (RS.AN). These are the muscles that take time and maturity, not a switch you flip. They need process, review, and people, which a fast-growing team has not built yet. Note that monitoring itself (DE.CM) is a 2, because Meridian does collect signals; it is the analysis of them (DE.AE) that sits at 1.

If your profile showed a similar shape, strong technical controls, weaker governance and detection, you read Meridian correctly. That shape is extremely common in real small companies.

## Why specific ratings

A few rows are worth explaining, because the reasoning transfers.

**GV.OV Oversight, Current 1.** Meridian has policies (GV.PO is 3), but no regular rhythm where leadership actually looks at security metrics and adjusts. Having policy is not the same as governing. That gap between "we wrote it down" and "we check and steer it" is exactly what a low Oversight score captures.

**GV.SC Supply Chain, Current 2, Target 4.** Meridian depends on AWS, CardaX, and VerifyNow. If one of them is breached, Meridian is exposed. Today the company uses them but has not formally assessed them, so Current is 2. The Target is 4, not 3, because for a bank, provider risk is not a nice-to-have, it is central. When you set a Target, ask how much this outcome matters to this business. For a bank, supply chain matters a lot.

**PR.AA Identity, Current 3, Target 4.** Already good (MFA everywhere, role-based access), so Current is high. But Target is 4, because for the system that guards every account, "good" is not the finishing line. Not everything needs a Target of 4, but the crown-jewel outcomes do.

**DE.CM and DE.AE, Current 2 and 1.** Meridian collects logs and has some monitoring (so DE.CM is 2, not 1), but nobody reviews the alerts in a consistent way (so DE.AE, the analysis, is only 1). Splitting "we collect signals" from "we actually make sense of them" is a real and useful distinction. Many teams have data and no eyes on it.

## Why the gaps, not the scores, are the point

The Gap column is the actual output. A category sitting at Current 3, Target 3 needs no attention right now, even though 3 is not a perfect score. A category at Current 1, Target 3 has a gap of 2 and is shaded red, and that is where a roadmap starts.

Meridian's biggest gaps (2 or more) land on oversight, detection, supply chain, platform security, incident management, and recovery testing. Read as a sentence: Meridian is good at building securely and bad at watching, steering, and rehearsing. That single sentence is worth more than the 22 numbers that produced it.

## What a good next move looks like

From this profile, Meridian's first three moves would be:

1. Start a simple quarterly security review with the CTO (closes the Oversight gap, and Oversight pulls up everything else).
2. Put eyes on the monitoring: a defined process to actually read and triage alerts (closes the Detection gap).
3. Assess the three key providers (closes the Supply Chain gap).

None of these is a tool purchase. All three are process and attention. That is usually where a young company's biggest, cheapest wins are.

## The one check on your own work

Did your Targets come out almost all 4? If so, go back. A profile where everything is Target 4 is a wish, not a plan. The skill is deciding what genuinely needs to be excellent, what only needs to be solid, and being honest about the difference. That judgement is the real deliverable.
