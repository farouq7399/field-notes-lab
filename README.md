# Field Notes Lab

A hands-on companion to the Field Notes series. You read the article, then you come here and actually do it: categorise a system, build a Cybersecurity Framework profile, walk a system through the Risk Management Framework, and track the gaps, all on one fictional company you can practise on freely.

If the articles are the map, this is the terrain.

> **Everything here is fictional.** Meridian Pay is a made-up digital bank invented for teaching. The policies, systems, diagrams, and data are examples to learn from, not real security advice for any real organisation. The NIST structure (the Cybersecurity Framework, FIPS 199, the Risk Management Framework, the SP 800-53 families) is real; the company is not.

## Start here

1. **Meet the company.** Read the [company profile](company/00-company-profile.md), skim the [system inventory](company/01-system-inventory.md) and [data classification](company/02-data-classification.md), and look at the [architecture diagram](company/diagrams/architecture.png). Fifteen minutes, and everything afterwards will make sense.
2. **Then follow the episodes below in order.** Each one pairs with a Field Notes article and gives you something to open, fill in, and keep.

## The lab, episode by episode

| Episode | You will | Open this |
|---|---|---|
| 1. The CSF profile | Rate where Meridian is and where it wants to be, across all 22 CSF categories | [episode-01-csf](episode-01-csf/README.md) |
| 2. The RMF, one system | Walk the Customer Web Portal through all seven RMF steps | [episode-02-rmf](episode-02-rmf/README.md) |
| 3. Categorize and Select | Categorise the portal (FIPS 199) and pick its controls | [episode-03-categorize-select](episode-03-categorize-select/README.md) |
| Ongoing | Track weaknesses to closure, and plan the roadmap | [templates](templates/README.md) |

Most workbooks come in two versions: a **worked example** (see what "done" looks like) and a **BLANK** (the one you fill in).

## What is inside

```
field-notes-lab/
  company/                     the fictional bank: profile, systems, data, diagrams
  policies/                    five example security policies, each mapped to NIST
  episode-01-csf/              CSF 2.0 current-vs-target profile (worked + blank)
  episode-02-rmf/              the seven-step walkthrough + a progress tracker
  episode-03-categorize-select/ FIPS 199 categorisation + control selection (worked + blank)
  templates/                   POA&M and gap-assessment workbooks
  build/                       the scripts that generate the workbooks
```

## The policies

Five example policies, written for Meridian, each ending with how it maps back to the framework:

- [Information Security Policy](policies/01-information-security-policy.md) (the umbrella)
- [Access Control Policy](policies/02-access-control-policy.md)
- [Acceptable Use Policy](policies/03-acceptable-use-policy.md)
- [Data Classification Policy](policies/04-data-classification-policy.md)
- [Incident Response Plan](policies/05-incident-response-plan.md)

## How it all connects

The whole point is that these pieces are one loop, not separate exercises:

- The **CSF profile** tells you where your big gaps are.
- The **RMF** takes one system and gets it to an accountable sign-off.
- **Categorize** and **Select** are the two RMF steps where the real judgement happens.
- The **POA&M** tracks every weakness you find until it is closed.
- What you learn feeds back into the profile, and round it goes.

Do all of it on Meridian first. Then do it on a system you actually know. That second pass is where it stops being theory.

## Regenerating the workbooks

Everything is built from scripts, so it is reproducible and easy to audit.

```
cd build && python build_workbooks.py          # all the Excel artifacts
cd company/diagrams && python build_diagrams.py # the diagrams
```

Requires Python with `openpyxl` (workbooks) and `Pillow` (diagrams).

## A note on sources

The NIST material referenced here is real and public: the Cybersecurity Framework 2.0 (CSWP 29), FIPS 199, the Risk Management Framework (SP 800-37 Rev. 2), and the SP 800-53 control families and baselines. The exact, normative wording always lives in the official documents at csrc.nist.gov. The plain-language descriptions in this lab are a teaching paraphrase, and the company they are applied to is invented.
