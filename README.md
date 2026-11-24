---
title: Particle Acceleration — Critical Research Archive
subtitle: Folder architecture, file manifest, and the reasoning behind the structure
author: Robin
date: 2026-11-24
version: v2
status: active — five of seven research streams landed; site generator live
source_files: all files in this archive
---

# What This Archive Is

A structured investigation into particle physics that examines the field at five levels:
the theoretical notions that motivate the machines, the instruments that record the data,
the software that converts signals into claims, the literature that publishes those claims,
and the governance that decides what gets built.

Almost every fact in it is drawn from the field's own technical documents, strategy
reports, published papers and court records. It is not an argument from outside physics.

**It does not claim that the machines fail to work, that results are fabricated, or that
the Standard Model's confirmed predictions are invalid.** Those claims were examined and
rejected. The scope boundary is in `00_method/research_frame_v1.md` and is binding.

# Read This First

`00_method/research_frame_v1.md` governs every other file. The short version:

- Every substantive claim carries a tier — **[A]** documented and acknowledged inside the
  field, **[B]** contested with named advocates on both sides, **[C]** structural inference
  not yet assembled or tested by the field.
- Every research file closes with **Tier D** — claims examined and *not* supported. A file
  without that section is incomplete, not strong.
- Mundane explanations (budget, inertia, path dependence, technical conservatism) take
  priority. An interest-based explanation must beat the mundane one on evidence.

## The headline result so far

Both of the strongest hypotheses this project started with were **rejected by its own
research**:

- **C1** — that inter-experiment combinations ignore systematic error correlated through
  shared software. False. Combinations model it explicitly and publish per-category scans.
  What survives is narrower: the correlation coefficient appears calibrated on procedural
  difference between collaborations rather than on shared model lineage.
- **C2** — that trigger selection makes some physics unobservable *in principle*. False.
  Unbiased data streams exist at an effective prescale near 40,000. What survives is the
  structural asymmetry of trigger error, which is falsifiable by a coverage calculation
  that does not appear to exist.

More than forty further claims were tested and struck out across the research files. That
is the frame working as designed, and it is the reason the surviving claims are worth
anything.

# Folder Architecture

Numbering is read order, not chronology — each folder is one level of the stack.

```
particle_ac/
├── README.md                  <- this file: architecture and manifest
├── 00_method/                 <- how the investigation works; read first
├── 01_foundations/            <- the physics baseline; the object being examined
├── 02_theory_critique/        <- weaknesses in the motivating theory
├── 03_hardware_systems/       <- the instruments: what they cannot see, who builds them
├── 04_software_algorithmic/   <- theoretical priors encoded in code
├── 05_publication_governance/ <- whether the literature can audit itself; cui bono
├── 06_dissent_register/       <- who has challenged the field, and on what grounds
├── 07_epistemic_audit/        <- what is known, inferred, and assumed
├── 99_working/                <- session notes, scratch, unfiled
├── site/                      <- the website: generator, stylesheet, landing page source
└── docs/                      <- generated site, served by GitHub Pages
```

Versioning, applied to every research file: `<name>_v[x].md`. A closed version is never
edited in place. The YAML `status` field marks open (`active`) or `superseded by v[x+1]`.

# File Manifest

## 00_method/

**`research_frame_v1.md`** — The governing method document. The research question split
across five levels; the warning that a brief to "expose weaknesses" pre-commits to its
conclusion and is therefore the project's own principal vulnerability; a terminological
correction replacing "algorithmic bias" with *theoretical prior encoded in instrumentation
and code*; the four-tier evidence standard; falsifiability tests for each level; and the
scope boundary excluding unsupportable claims.

**`claims_register_v1.md`** — The single register of what this archive asserts: claim ID,
tier, supporting file, status. Includes the resolution notes recording why C1 and C2 were
rejected and what replaced them.

## 01_foundations/

**`particle_acceleration_research_v1.md`** — The physics baseline. Only electric fields do
work on a charged particle; the lineage from RF acceleration through the cyclotron's
relativistic failure to phase stability and strong focusing; the synchrotron radiation
ceiling scaling as γ⁴/ρ²; plasma wakefield acceleration; Fermi and diffusive shock
acceleration; the Hillas and GZK ceilings and the unresolved ultra-high-energy cosmic ray
origin problem. **Its reference list is recall-based and flagged unverified** — the one
outstanding correctness debt in the archive.

## 02_theory_critique/

**`theoretical_weaknesses_v1.md`** — 56 KB, 44 references, 52 Tier A claims, 18 Tier D
rejections. The central finding: naturalness carried a *pre-registered falsification
condition* set inside the field — an explicit sub-TeV bound, published with the statement
that failure to find such phenomena would mean the criterion failed. The condition was met
and the point conceded in the theory literature. The 2023 US strategy report contains zero
instances of "naturalness", "hierarchy problem", "fine-tuning" or "unnatural" across its
entire length while still paraphrasing the argument. Also: the fine-tuning threshold moving
by stipulation across three decades against gluino limits rising nearly an order of
magnitude; the 750 GeV diphoton episode; measured clustering in the Particle Data Group
record. Rejects, among others, the claim that naturalness was *merely* aesthetic, that
no-lose rhetoric is empty, and that axion research was funding-suppressed.

## 03_hardware_systems/

**`trigger_data_destruction_v1.md`** — 47 KB, 30 references, 78 Tier A claims. 40 MHz
crossings against roughly 1 kHz stored; full readout would be 40 TB/s against about 1 GB/s
written. Rejected events are, in the field's own words, lost forever. Menus are built from
theoretical expectation and simulation, with rate allocated by committee in roughly equal
thirds. Documents a case where trigger design *prevented* specific measurements rather
than delaying them. Rejects the strong "unobservable in principle" claim, the astrophysical
analogy, and the premise that trigger bandwidth is a hard physical limit.

**`hardware_supply_chain_v1.md`** — *Research in progress.* Who physically builds the
machines: magnet and superconductor manufacturers, niobium concentration, cavity fabricators,
cryogenics and the helium chokepoint, sensors, photomultipliers, crystals, FPGA vendors and
rad-hard foundries, and CERN's contribution-proportional procurement policy.

## 04_software_algorithmic/

**`software_stack_bias_v1.md`** — 73 KB, 42 references, 126 Tier A claims, 11 Tier D
rejections. Both general-purpose experiments' nominal hadronisation descends from one manual
fit whose authors describe subjective choices and set a shower parameter to mimic a missing
calculation. A published study shows the two-generator spread does not bound the spread to a
third. In unfolding, the simulation's own prediction serves as the regularising prior — the
field states this openly. The key answer on correlated systematics: combinations *do* model
inter-experiment correlation, assigning roughly one half to shared modelling terms, which
refutes the strong version of C1. What survives is what that coefficient is calibrated on.

## 05_publication_governance/

**`publication_governance_v1.md`** — 77 KB, 55 references, 54 Tier A claims, 12 Tier D
rejections. The field's own reinterpretation inventory records full likelihoods released for
two analyses, efficiency maps in very few cases, and machine-learning analyses that cannot be
reproduced outside the collaboration that produced them; a 2025 assessment finds some earlier
searches' reproducibility already lost *inside* those collaborations. Authorship is earned by
a service threshold and the granting committee disclaims responsibility for content. Cost and
schedule movement on the proposed next machine, and the SSC precedent. Rejects null-result
suppression (the reverse holds), the absence of a conflict-of-interest regime, and the claim
that critics are professionally punished.

## 06_dissent_register/

**`legitimacy_confrontations_v1.md`** — *Research in progress.* Who has confronted the
legitimacy of particle accelerators: who, when, why, and how many. Sorted into validity,
priority, safety, epistemological and specific-result challenges, with an actual count by
category — the central question being how many critics dispute the physics rather than the
priorities.

## 07_epistemic_audit/

**`known_versus_assumed_v1.md`** — *Research in progress.* What is confirmed and to what
precision; where the inferential chain from detector signal to theoretical entity becomes
model-dependent; theory-ladenness of observation; competing frameworks status-rated honestly;
live anomalies; and fringe claims assessed and rejected.

## site/ and docs/

**`site/build.py`** — Static site generator. Reads the research markdown, parses the YAML
frontmatter, renders to `docs/`, and converts inline tier markers into styled badges so the
epistemic status of every claim is visible on the page. Re-run after any research change:

```bash
python3 site/build.py
```

**`site/content/index.md`** — The landing page source. **This is the single file holding the
site's argument and message.** Edit it here, not in the generated HTML.

**`site/assets/style.css`** — Stylesheet. Serif body for long technical reading, sans for
structure, tier badges colour-coded by evidence class.

**`docs/`** — Generated output, served by GitHub Pages. Never edit by hand; it is overwritten
on every build.

## 99_working/

Scratch and unfiled material. Nothing here is load-bearing.

# Current State

| Item | Status |
|---|---|
| Method frame and evidence tiers | Complete (v1) |
| Claims register | Complete — all seven resolved; three rejected as stated |
| Physics baseline | Complete (v1), **references unverified** |
| Theory critique | Complete (v1) |
| Trigger systems | Complete (v1) |
| Software stack | Complete (v1) |
| Publication and governance | Complete (v1) |
| Hardware supply chain | In progress |
| Dissent register | In progress |
| Epistemic audit | In progress |
| Website | Live, generated from the archive |
| Synthesis document | Not started — deliberately |

# Next Steps

1. Two remaining streams land; each reviewed against the frame for a genuine rather than
   token Tier D section.
2. Claims register completed. Remaining candidate claims resolved to supported, weakened or
   rejected.
3. Reference verification pass on the foundations file — the outstanding correctness debt.
4. Synthesis only after the register is complete. Writing it earlier would reproduce exactly
   the failure this archive documents.
