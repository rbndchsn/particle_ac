---
title: Particle Acceleration — Critical Research Archive
subtitle: Folder architecture, file manifest, and the reasoning behind the structure
author: Robin
date: 2026-11-24
version: v1
status: active — research streams in progress, manifest summaries pending
source_files: all files in this archive
---

# What This Archive Is

A structured investigation into particle acceleration physics that examines the field at
five levels: the theoretical notions that motivate the machines, the instruments that
record the data, the software that converts signals into claims, the literature that
publishes those claims, and the governance that decides what gets built.

It is not a primer on particle acceleration. The physics baseline sits in
`01_foundations/` because the critique needs an accurate object to critique, but the
baseline is not the point of the archive.

# Read This First

`00_method/research_frame_v1.md` governs every other file. It defines the evidence tier
system, states the methodological trap built into this project's own premise, and sets the
falsifiability tests each level of critique must meet. No file in this archive should be
read or extended without it.

The short version of the frame:

- Every substantive claim carries a tier label — **[A]** documented and acknowledged inside
  the field, **[B]** contested with named advocates on both sides, **[C]** structural
  inference not yet assembled or tested by the field.
- Every research file must close with **Tier D** — claims examined and *not* supported.
  A file without that section is incomplete, not strong.
- Mundane explanations (budget, inertia, path dependence, technical conservatism) take
  priority over motivated ones. An interest-based explanation must beat the mundane
  explanation on evidence.

# Folder Architecture

The numbering is read order, not chronology. Each folder is one level of the stack, moving
from the abstract to the institutional.

```
research/
├── README.md                  <- this file: architecture and manifest
├── 00_method/                 <- how the investigation works; read first
├── 01_foundations/            <- the physics baseline; the object being examined
├── 02_theory_critique/        <- weaknesses in the motivating theory
├── 03_hardware_systems/       <- the instruments: who builds them, what they cannot see
├── 04_software_algorithmic/   <- theoretical priors encoded in code
├── 05_publication_governance/ <- whether the literature can audit itself; cui bono
└── 99_working/                <- session notes, scratch, unfiled material
```

Versioning convention, applied to every file: `<name>_v[x].md`. A closed version is never
edited in place. When a session changes structure or conclusions, the next integer version
is written and the change is logged in that file's Version Log. The YAML `status` field
marks whether a version is open (`active`) or `superseded by v[x+1]`.

# File Manifest

## 00_method/

**`research_frame_v1.md`** — The governing method document. Contains the research question
decomposed into five levels; the warning that "expose weaknesses" pre-commits to a
conclusion and is therefore the project's own principal vulnerability; a terminological
correction replacing "algorithmic bias" with the sharper and more defensible formulation
*theoretical prior encoded in instrumentation and code*; the four-tier evidence standard;
explicit falsifiability tests for each level of critique; and scope boundaries that
exclude unsupportable claims (fabricated results, invalid Standard Model) on the grounds
that including them would discredit the defensible material by association.

**`claims_register_v1.md`** — The single register of what this archive asserts. Each claim
carries an ID, tier, supporting file and status (`UNTESTED` / `SUPPORTED` /
`SUPPORTED-AS-INFERENCE` / `WEAKENED` / `REJECTED`). Seeded with seven candidate
structural claims identified before research began — on correlated systematics between
ATLAS and CMS, trigger-level data destruction, generator tuning circularity, peer review
under hyperauthorship, strategy panel composition, supplier concentration, and the
unacknowledged retirement of failed motivating arguments. All currently untested. Nothing
may enter a published synthesis unless it appears here as supported.

## 01_foundations/

**`particle_acceleration_research_v1.md`** — The physics baseline, carried over from the
first session. Core principle (only electric fields do work on a charged particle); the
engineered accelerator lineage from RF through the cyclotron's relativistic failure to
phase stability and strong focusing; the synchrotron radiation ceiling scaling as γ⁴/ρ²
and its consequences for machine design; plasma wakefield acceleration; astrophysical
mechanisms (Fermi stochastic and diffusive shock acceleration); and the two ceilings on
natural accelerators, the Hillas criterion and the GZK cutoff, with the unresolved
ultra-high-energy cosmic ray origin problem. Its reference list is recall-based and flagged
unverified — this must be corrected before the file is treated as closed.

## 02_theory_critique/

**`theoretical_weaknesses_v1.md`** — *Research in progress.* Examines whether the notions
motivating the machines are falsifiable and what happens to a motivating argument when its
prediction fails. Covers naturalness and the hierarchy problem as aesthetic versus
empirical criteria and whether their post-LHC retirement was explicit; supersymmetry mass
limit drift; the 750 GeV diphoton episode as a quantifiable case study in community
response incentives; WIMP paradigm persistence through successive null results; string
landscape predictive content; no-lose theorem rhetoric in proposal documents; the 5-sigma
convention; and documented confirmation-bias clustering in Particle Data Group historical
measurements. Cites inside-field critics and the field's rebuttals from their own writing.

## 03_hardware_systems/

**`hardware_supply_chain_v1.md`** — *Research in progress.* Who physically builds the
machines, in detail: magnet and superconducting cable manufacturers, niobium supply
concentration, SRF cavity fabricators, RF power, cryogenics and the global helium
chokepoint, silicon sensors, photomultipliers, scintillating crystals, FPGA vendors and
rad-hard ASIC foundries, and computing. Includes CERN's industrial-return procurement
policy and how contribution-proportional contract allocation interacts with technical
merit in supplier selection. Maps single-vendor dependencies and geopolitical exposure.
Covers astrophysical instruments and the light-source commercial tail.

**`trigger_data_destruction_v1.md`** — *Research in progress.* The strongest single line of
argument in the archive. The LHC collides at 40 MHz and records roughly 1 kHz; discarded
events are destroyed in real time by hardware and cannot be recovered. The trigger menu is
built from theoretical expectation, so the apparatus encodes a prior at the exact point
where data loss becomes irreversible. Establishes the rates and rejection factors,
catalogues systematically disfavoured signatures (long-lived, displaced, soft, high
multiplicity), assesses mitigations (data scouting, trigger-level analysis, parked streams,
LHCb's software trigger), and tests whether "unobservable in principle" survives or must be
softened.

## 04_software_algorithmic/

**`software_stack_bias_v1.md`** — *Research in progress.* Theoretical assumptions encoded
in simulation and analysis code that is then used to test those assumptions. Monte Carlo
generators and the physics models they hardcode; the tuning procedure and the circularity
of tuning on data then computing acceptance corrections used to interpret new data; whether
generator-comparison systematic uncertainties underestimate true model uncertainty when the
compared generators share lineage; GEANT4 validation gaps; ROOT monoculture and maintainer
dependency; unfolding regularisation as injected prior; machine learning trained on
simulation and applied to data. The central question: whether ATLAS and CMS systematic
errors are correlated through shared software, and what official LHC combination papers
actually do about inter-experiment correlation.

## 05_publication_governance/

**`publication_governance_v1.md`** — *Research in progress.* Whether the literature can
audit itself, and whose interest shapes what gets built. Hyperauthorship and accountability
diffusion; collaboration-internal review and what external peer review can audit after
3,000 authors have signed; null result publication practice (possibly a HEP strength rather
than weakness — tested honestly); arXiv moderation; what replication means with two
detectors; the composition and conflict-of-interest structure of the European Strategy for
Particle Physics, FCC Feasibility Study and Snowmass/P5 panels; the 1993 SSC cancellation;
the FCC cost debate with both sides cited from their own writing; funding figures; and
career incentive structure.

## 99_working/

Session notes, scratch material and anything not yet filed. Nothing here is load-bearing.

# Current State

| Item | Status |
|---|---|
| Method frame and evidence tiers | Complete (v1) |
| Claims register | Seeded, all claims untested |
| Physics baseline | Complete (v1), references unverified |
| Five research streams | In progress |
| Claims register population | Pending stream completion |
| Synthesis document | Not started |

# Next Steps

1. Research streams land; each file reviewed against the frame, particularly for a genuine
   rather than token Tier D section.
2. Claims register populated from stream findings. Candidate claims C1–C7 resolved to
   supported, weakened or rejected.
3. Reference verification pass on `01_foundations/particle_acceleration_research_v1.md`.
4. Synthesis only after the register is populated. Writing a synthesis before knowing which
   claims survived would reproduce exactly the failure this archive is built to document.
