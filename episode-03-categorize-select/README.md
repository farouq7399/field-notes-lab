# Episode 3 lab: Categorize and Select, with worked examples

> Pairs with the Field Notes article "The two steps everyone gets stuck on."

Steps 2 and 3 of the RMF are where beginners freeze, because they feel abstract. They are not, once you have done them once on a real system. So you are going to do them on Meridian's Customer Web Portal.

## What is in here

- **fips199-categorization.xlsx**: the Categorize step. Rate each information type for confidentiality, integrity, and availability. The workbook takes the high-water mark and tells you the system's overall impact. Worked for the portal (result: Moderate), with the scoping reasoning written out.
- **fips199-categorization-BLANK.xlsx**: the empty version to practise on.
- **control-selection.xlsx**: the Select step. Starting from the Moderate baseline, a representative set of controls with status and owners. See how a real control tracker is shaped.
- **control-selection-BLANK.xlsx**: the empty version.
- **solution-walkthrough.md**: the answer key. Why each FIPS rating, why the portal is Moderate and not High, and how to read the control statuses. Check your reasoning here after you try the blanks.

## Do this (about 45 minutes)

1. Open the worked FIPS 199 sheet. Read down the information types and the ratings. Then read the "Why Moderate and not High" note. That note is the most important thing in this episode: categorisation is a written, defensible judgement about a defined boundary, not a gut feeling.
2. Open the blank FIPS 199 sheet. It is generic on purpose: you fill in the information types yourself. Try a different system, the Internal Admin Console (S7). To get started, its information types include: the customer records staff can view, the account changes staff can make, and internal support notes. Rate each for confidentiality, integrity, and availability, and write your reason. Would S7 come out higher or lower than the portal, and why? (Hint: unlike the portal, S7 lets staff see and change real customer data directly, so think hard about confidentiality and integrity.)
3. Open the control-selection sheet. Notice it starts from a baseline and then tailors. You are never choosing controls from a blank page.
4. Filter the control sheet to the "No" and "Partly" rows. Those are exactly what would flow into the POA&M in [templates/](../templates/).

## The one idea to take away

Categorize is "how much does this system matter." Select is "so here is the sensible starting set of controls." Neither is guesswork once you anchor them to impact and a baseline. The freezing stops the moment you do it on something real.

Next: use the [POA&M and gap-assessment templates](../templates/) to turn your findings into a plan.
