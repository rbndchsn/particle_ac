---
title: Claims Register
subtitle: Every substantive claim in the archive, with tier, supporting file, and test status
author: Robin
date: 2026-11-24
version: v1
status: active — trigger stream resolved; six streams outstanding
source_files: 00_method/research_frame_v1.md
---

# Purpose

A single register of what this archive actually asserts. Each claim has an ID, a tier, the
file that supports it, and a status. Nothing may be carried into a published synthesis
unless it appears here with a status of SUPPORTED or SUPPORTED-AS-INFERENCE.

Status values: `UNTESTED` · `SUPPORTED` · `SUPPORTED-AS-INFERENCE` · `WEAKENED` ·
`REJECTED`

# Candidate Structural Claims

These were identified before research began. They are the project's working hypotheses and
are all currently UNTESTED. Several may not survive.

| ID | Claim | Tier | File | Status |
|---|---|---|---|---|
| C1 | ATLAS and CMS are presented as mutually independent confirmation while sharing simulation toolkits, event generators, analysis frameworks and methodology, so their systematic errors are correlated and agreement between them is weaker evidence than presented | C | 04_software_algorithmic | UNTESTED |
| C2 | ~~The Level-1 trigger encodes a theoretical prior at the point of irreversible data destruction, making some physics unobservable in principle rather than merely unmeasured~~ | C | 03_hardware_systems | **REJECTED** — see C2a |
| C2a | Trigger menus are built from theoretical expectation and discarded events are unrecoverable, so trigger error is structurally asymmetric: false positives cost measured, budgeted bandwidth while false negatives cost unrecoverable events and are never integrated over signature space | C | 03_hardware_systems | SUPPORTED-AS-INFERENCE |
| C2b | Trigger design has demonstrably prevented specific measurements, not merely delayed them | A | 03_hardware_systems | SUPPORTED |
| C3 | Event generators are tuned to data and then used to compute the acceptance corrections through which new data is interpreted, creating a circularity in which the correction depends on the model under test | C | 04_software_algorithmic | UNTESTED |
| C4 | Hyperauthorship combined with collaboration-internal pre-review makes external peer review structurally incapable of auditing a result | C | 05_publication_governance | UNTESTED |
| C5 | Strategy and feasibility panels are composed substantially of prospective beneficiaries, so machine-justification documents cannot be read as independent assessment | C | 05_publication_governance | UNTESTED |
| C6 | Supplier concentration in specialised components creates single points of failure, and procurement balance rules mean some technical choices are downstream of political allocation rather than technical merit | C | 03_hardware_systems | UNTESTED |
| C7 | Motivating arguments whose predictions failed (naturalness, WIMP parameter space) were retired without the retirement being reflected in the justification for successor machines | B | 02_theory_critique | UNTESTED |

# Register

Populated as research files land. One row per substantive claim, tier-labelled, traceable
to its source file and references.

# Resolution Notes

## C2 — rejected, and why that matters

The original claim said some physics is **unobservable in principle** because the trigger
destroys data irreversibly under a theory-laden menu. That is wrong, and the research
stream rejected it rather than defending it.

Reason [A]: ATLAS and CMS run zero-bias, enhanced-bias and pileup streams which are not
selected on physics signatures. These give an effective prescale of roughly 40,000 — an
unbiased sample of order 0.5–1 fb⁻¹, enough to set limits around the 3 fb level. Physics
outside the menu is therefore *badly sampled*, not *unobservable*. The strong version of
the claim is false and has been struck from the register.

Three further supporting arguments were also rejected: that the bandwidth constraint is a
hard physical limit (LHCb and ALICE abandoned hardware triggers entirely, so it is an
engineering choice); that the astrophysical detectors face the same problem (IceCube
archives all raw waveforms); and that the field does not acknowledge the issue (it does,
in print).

What survives is narrower, documented, and sharper — C2a and C2b above. The replacement
claim is falsifiable by a single coverage integral over signature space with a stated
measure. No such integral appears to exist.

This resolution is the frame working as designed. A register that only accumulated
confirmations would be worthless.
