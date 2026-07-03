# The real NIST behind this lab

Meridian Pay is invented. The framework it is measured against is not. This page lists the real NIST material the lab draws on, so you can always go to the source. The exact, normative wording lives in the official documents at csrc.nist.gov. Everything here is public domain.

## The documents in play

| Short name | What it is | Where it shows up in the lab |
|---|---|---|
| Cybersecurity Framework 2.0 (CSWP 29) | The outcomes framework: 6 Functions, 22 Categories, 106 Subcategories | Episode 1, the CSF profile |
| SP 800-37 Rev. 2 | The Risk Management Framework: 7 steps | Episode 2, the RMF walkthrough |
| FIPS 199 | How to rate a system Low, Moderate, or High impact | Episode 3, categorisation |
| SP 800-53 Rev. 5 | The catalogue of controls, in 20 families | Episode 3, control selection |
| SP 800-53B | The control baselines (which controls are in Low, Moderate, High, Privacy) | reference/sp800-53B-baselines.xlsx |
| SP 800-53A | How to assess whether a control actually works | templates/control-assessment.xlsx |

## The numbers, and they are real

From the NIST OSCAL content (the machine-readable, authoritative source shipped in `reference/data`):

| Baseline | Controls | Used for |
|---|---|---|
| Low | 149 | Limited impact if breached |
| Moderate | 287 | The common middle. Meridian's portal sits here |
| High | 370 | Severe or catastrophic impact |
| Privacy | 96 | Added when a system processes personal information |

The counts include control enhancements. The full Moderate membership, all 287, is in the reference workbook, grouped by family and listed in full.

## The 20 control families

Every control belongs to a family, named by a two-letter code (AC for Access Control, IR for Incident Response, and so on). The families and what each covers are in the shipped data and the reference workbook. When you see a control like AC-2, the AC tells you the family and the 2 tells you the control. An enhancement looks like AC-2(1).

## How assessment fits (SP 800-53A)

Selecting and implementing a control is not proof it works. SP 800-53A gives you three ways to check:

- **Examine**: look at documents, settings, and records.
- **Interview**: talk to the people who run the control.
- **Test**: actually exercise it and watch what happens.

Each control ends up **Satisfied** or **Other than satisfied**. Every "other than satisfied" becomes a finding, and every finding becomes a line in the POA&M. That is the honest join between "we have controls" and "our controls work."

## Refreshing the data

The JSON in `reference/data` came from NIST's public OSCAL content. If NIST updates a baseline, that data can be refreshed from the source noted inside each file. The plain-language descriptions elsewhere in this lab are a teaching paraphrase, not the official text.
