---
title: Claims Register
subtitle: Every substantive claim in the archive, with tier, supporting file, and test status
author: Robin
date: 2026-11-24
version: v1
status: active — seven candidates resolved; C1a weakened by the evidential audit
source_files: 00_method/research_frame_v1.md; 08_evidential_audit/proof_failure_modes_v1.md
---

# Purpose

A single register of what this archive actually asserts. Each claim has an ID, a tier, the
file that supports it, and a status. Nothing may be carried into a published synthesis
unless it appears here with a status of SUPPORTED or SUPPORTED-AS-INFERENCE.

Status values: `UNTESTED` · `SUPPORTED` · `SUPPORTED-AS-INFERENCE` · `WEAKENED` ·
`REJECTED`

# Outcome

Seven candidate claims were written before research began. Of those seven, **three were
rejected as stated** (C1, C2, C4), **one was split with half rejected** (C6), and **three
survived in narrowed or reworded form** (C3, C5, C7). Six narrower replacement claims were
written from what the evidence actually supported.

Not one of the seven survived in its original wording. The two the project considered
strongest going in — C1 and C2 — are both among the rejected.

# Register

| ID | Claim | Tier | File | Status |
|---|---|---|---|---|
| C1 | ~~ATLAS and CMS are presented as mutually independent confirmation while sharing simulation toolkits, event generators and methodology, so their systematic errors are correlated and agreement between them is weaker evidence than presented~~ | C | 04_software_algorithmic | **REJECTED** — see C1a, C1b |
| C1a | ~~…the true value for hadronisation is plausibly nearer 1 than 0.5~~ | C | 04_software_algorithmic | **WEAKENED** — see C1a′ |
| C1a′ | The correlation value is a documented choice resting on procedural rather than genealogical grounds — confirmed verbatim in the papers — but where it has been scanned the numerical consequence is small; no scan has been published for the 2012 discovery significance | A | 08_evidential_audit | SUPPORTED |
| C1b | Both general-purpose experiments' nominal hadronisation descends from one manual fit; CMS holds its parameters fixed and ATLAS tunes ten shower and multi-parton parameters on top of it | A | 04_software_algorithmic | SUPPORTED |
| C2 | ~~The Level-1 trigger encodes a theoretical prior at the point of irreversible data destruction, making some physics unobservable in principle rather than merely unmeasured~~ | C | 03_hardware_systems | **REJECTED** — see C2a, C2b |
| C2a | Trigger menus are built from theoretical expectation and discarded events are unrecoverable, so trigger error is structurally asymmetric: false positives cost measured, budgeted bandwidth while false negatives cost unrecoverable events and are never integrated over signature space | C | 03_hardware_systems | SUPPORTED-AS-INFERENCE |
| C2b | Trigger design has demonstrably prevented specific measurements, not merely delayed them | A | 03_hardware_systems | SUPPORTED |
| C3 | Generators tuned to data are used to compute the acceptance corrections through which new data is interpreted, and the field names the resulting risk in its own documentation | C | 04_software_algorithmic | SUPPORTED-AS-INFERENCE (narrowed) |
| C4 | ~~Hyperauthorship combined with collaboration-internal pre-review makes external peer review structurally incapable of auditing a result~~ | C | 05_publication_governance | **REJECTED** — wrong mechanism; see C4a |
| C4a | External audit of an LHC result is infeasible because the artefacts an audit requires are largely unreleased, not because of author counts or internal review quality | A | 05_publication_governance | SUPPORTED |
| C5 | A conflict-of-interest regime exists but is narrow in scope, and the cost figures in machine-justification documents are supplied by proponents to a panel barred from generating its own | A | 05_publication_governance | SUPPORTED (narrowed) |
| C6a | Supplier concentration in specialised components creates documented single points of failure | A | 03_hardware_systems | SUPPORTED |
| C6b | ~~Procurement balance rules mean some technical choices are downstream of political allocation rather than technical merit~~ | C | 03_hardware_systems | **REJECTED** |
| C7 | The retirement of naturalness is explicit in the theory literature and reflected unevenly in machine-justification documents — paraphrased with the vocabulary removed in one, restored in another | B | 02_theory_critique | SUPPORTED-AS-INFERENCE (reworded) |

# Resolution Notes

## C1 — rejected, and the narrower claim that replaced it

The original claim said combinations present ATLAS and CMS as independent while ignoring
systematic error correlated through shared software. That is false, and documented to the
contrary [A]. The top-quark mass combination assigns a correlation of 0.5 to hadronisation,
colour reconnection, underlying event, QCD radiation and matrix-element generator terms, and
0.85 to PDF and pile-up, and publishes a per-category scan showing modelling shifts of a few
MeV against a 0.33 GeV total. The Higgs combination correlates QCD-scale and parton-shower
terms and deliberately decorrelates acceptance-theory terms estimated by different methods.

What survives is C1a, which is a question about *grounds* rather than about neglect: the
coefficient looks calibrated on how differently the two collaborations work, not on how much
model ancestry they share. For the top mass the distinction is numerically immaterial because
the response is linear. Whether it matters anywhere else is untested, because no published
study scans correlation and model variance together.

## C2 — rejected, and why that matters

The original claim said some physics is **unobservable in principle**. That is wrong [A]:
zero-bias, enhanced-bias and pileup streams are not selected on physics signatures and give
an effective prescale near 40,000 — an unbiased sample of order 0.5–1 fb⁻¹. Physics outside
the menu is *badly sampled*, not unobservable.

Three supporting arguments also failed: that bandwidth is a hard physical limit (LHCb and
ALICE abandoned hardware triggers, so it is an engineering choice); that astrophysical
detectors share the problem (IceCube archives all raw waveforms); and that the field does not
acknowledge the issue (it does, in print).

C2a is falsifiable by one coverage integral over signature space with a stated measure. No
such integral appears to exist.

## C3 — supported, narrowed

The circularity is real and the field names it. ATLAS's own tuning documentation warns that
over-tuning non-perturbative parameters may hide new physics [A]. In iterative unfolding the
start values are the simulation's own truth, and the field states plainly that this
dependence *is* the regularisation [A]. The two-generator spread used to estimate model
uncertainty is documented as not bounding the spread to a third [A].

Two stronger versions were rejected: that tunes are fitted to the signals they correct, and
that unfolded spectra are prior-driven artefacts. Data-driven background estimation and
control-region validation exist precisely to reduce simulation dependence, and they work.

## C4 — rejected on mechanism, conclusion rebuilt

Hyperauthorship is not what prevents external audit. Internal review as a rubber stamp was
rejected, and the OPERA episode cuts the other way: a collaboration of that size published
its own anomaly and then its own refutation.

The conclusion survives by a different route, and a better documented one [A]. The field's own
2020 reinterpretation inventory recorded full statistical likelihoods released for two
analyses, efficiency maps in very few cases, data for refits often not provided, and
machine-learning analyses that cannot be reproduced outside the collaboration that produced
them; the 2025 follow-up records 41 statistical-model records and a CMS commitment to
systematic release, so the artefact deficit is narrowing and the claim must be dated. By 2025 the
reproducibility of some earlier searches had been lost *inside* those collaborations. An
outsider cannot audit because the artefacts are not there, not because three thousand people
signed the paper.

## C5 — supported, narrowed

Two strong versions were rejected: that there is no conflict-of-interest regime (there is),
and that no panel member lacks a stake (at least one documented counterexample).

What is documented [A]: the regime recuses four of thirty-two members, for national-laboratory
employment, from a single acceptance vote; all thirty-two are particle or accelerator
physicists; the European strategy mandate carries no conflict-of-interest provisions at all;
and cost figures are taken from proponents, with the subcommittee barred from producing
estimates of its own. The sharpest point is the last one, and it is not about anyone's motives.

## C6 — split

C6a holds [A]: one qualified Nb₃Sn supplier at HL-LHC specification against eight for ITER;
roughly 93% of world niobium mine production from one country and 77–90% of that from one
firm; two companies worldwide making helium turbo-expanders of the required size; zero US
niobium production.

C6b does not. Member states receive 94% of direct contracts but 77% of value added, and
Germany and the United Kingdom are documented as poorly balanced — that is, under-returned.
Capture of procurement by the largest contributors was examined and rejected.

## C7 — supported, reworded

The original wording said the retirement was not reflected in successor-machine
justifications. That overstates it. The retirement is explicit and on the record in the
theory literature [A]: a sub-TeV bound published in 2008 with a stated failure condition, and
the same author conceding a "post-naturalness era" in 2017.

What is uneven is the reflection. The 2023 US strategy report contains zero instances of
"naturalness", "hierarchy problem", "fine-tuning" or "unnatural" across 379,741 characters
while paraphrasing the argument those words name; the 2025 European briefing book restores
the term. Also rejected: that naturalness was merely aesthetic (its effective-field-theory
grounding is a real argument), and that the goalposts moved only after exclusions (split
supersymmetry abandoned naturalness in 2004, before the LHC ran).

## C1a — weakened by the evidential audit, and restated

The first half of C1a is confirmed in the papers' own words: shared-modelling categories are
assigned ρ = 0.5 and the justification given is that the experiments use different generators
and different variation schemes — procedural difference, not shared lineage [A].

The second half does not survive. The published sensitivity scans show the top-mass central
value moving by at most 41 MeV under adverse correlation assumptions, against a 0.33 GeV total
uncertainty, and the combination states explicitly that "No category was identified to have
ρ=1" [A]. Whatever the grounds, the numerical consequence where it has been tested is small.

What remains is narrower and is now C1a′: **no published scan of correlation assumptions exists
for the 2012 discovery significance** — the one quantity for which the independence of the two
experiments was rhetorically load-bearing. Robustness demonstrated for a 2024 precision
combination is being borrowed, implicitly, by a 2012 discovery claim. Falsified by production
of such a study.
