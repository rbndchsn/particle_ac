---
title: The Closed Loop
subtitle: Can a machine, its software and its theory confirm one another without ever touching reality? A hypothesis, its strongest form, and what would break it
author: Robin
date: 2026-11-24
version: v1
status: active — hypothesis stated and partly tested; field test proposed; references compiled in a voice session and pending verification except where marked
source_files: 07_epistemic_audit/known_versus_assumed_v1.md; 04_software_algorithmic/software_stack_bias_v1.md; 00_method/claims_register_v1.md
---

# Origin

This document began on a laboratory tour. At the Université de Montréal's ion-beam facility, a physicist showed how ions are accelerated into a target such as aluminium or steel and pointed to the result on a computer screen. The obvious question followed: how do you know the screen shows what is happening inside the machine? The answer — because the software displays what the machine is doing — did not settle it. It moved the question one step back.

# The Hypothesis

Stated in the author's own terms:

Science moves from hypothesis to observation to the next hypothesis, filtering out what does not match and keeping what does, and writing down equations that approximate what is seen. Software is then programmed on those equations and assumptions, with defined inputs and outputs, and optimised as more data arrives. That software is installed alongside an accelerator. The machine produces a signal, the software interprets it, and the output confirms the theory the software was built from.

If this is right, the apparatus can only hand the theory back to itself. Call it **the closed-loop hypothesis**: theory → equations → software → interpretation of the machine → confirmation of theory.

# This Is a Recognised Problem, Not a Fringe One

The hypothesis has a serious pedigree [A]:

- **Theory-ladenness of observation.** What an observer records is shaped by the theory they already hold (1).
- **Duhem's holism.** No experiment tests a hypothesis alone; it tests the hypothesis together with every auxiliary assumption about the instrument (2).
- **The experimenter's regress.** To know whether an instrument works you need the correct result; to know the correct result you need a working instrument (3). This is the closed loop in its sharpest published form.

Philosophers of experiment have spent decades on how the regress is broken in practice rather than in principle (4, 5).

# Where the Loop Is Real

The archive has already documented one place where it partly closes [A]. At the LHC, event generators are tuned on data and then used to compute the acceptance corrections through which new data is interpreted; in unfolding, the simulation's own prediction serves as the regularising prior (see `04_software_algorithmic`, claim C3 in the register). ATLAS's own tuning documentation warns that over-tuning may hide new physics.

So the hypothesis is not imaginary. It describes a real mechanism, and the further a measurement sits from the raw signal, the more of the chain is model-dependent (see `07_epistemic_audit/known_versus_assumed_v1.md`).

# Where the Loop Is Broken

A loop is broken by anything that reaches in from outside it. Four kinds of contact matter:

1. **Predictions made before measurement that could have failed.** A theory that only ever accommodates data is in the loop. One that risks a specific number in advance is not.
2. **Calibration against references whose answer is fixed independently.** If a sample of known composition is run and the software reports it correctly, the software's interpretation has touched something it did not create.
3. **Independent methods.** Two techniques resting on different physics agreeing on the same sample.
4. **Working technology.** If an interpretation were wrong, things built on it would fail.

# The Université de Montréal Case

The facility runs a 1.7 MV Tandetron and a 6 MV Pelletron Tandem; the larger machine is the first commercial tandem prototype in the world, built for Chalk River in 1954 and moved to Montréal in 1966 (6, 7) [A]. They accelerate ions, not electrons, into material targets.

The most likely technique on the screen is Rutherford backscattering: an ion strikes a nucleus in the target and rebounds, and the energy it returns with depends on the mass of the atom it hit (8, 9) [A]. Applied to the four tests above:

- The kinematics are two-body collision physics, predicted in 1911, before the instrument existed (8).
- Spectra are calibrated against certified reference samples [A].
- Composition can be cross-checked by independent methods resting on different physics [A].
- Ion implantation, the same family of beam, is how semiconductor chips are manufactured. If beam-material interpretation were invented, the chips would not work [A].

On this evidence the loop at a low-energy ion facility is short, externally anchored, and broken in all four ways [C — inference from the facts above; falsified by a blind test that fails].

# A Proposed Field Test

The decisive move is cheap. Bring the physicist a sample whose composition you know and he does not. If the screen reports it correctly, the loop touches reality at that facility. If it cannot, something has been found. The same logic, scaled up, is exactly what blind analysis does in particle physics: hide the answer from the people interpreting the data until the method is frozen (5).

# Where the Hypothesis Bites Hardest

The loop is longest where the chain from signal to claim is longest — the LHC, where an observed "particle" passes through trigger selection, reconstruction, simulation-derived corrections and statistical models before it becomes a claim. That is the terrain the rest of this archive examines, and it is where the closed-loop hypothesis retains real force [B].

# Claims Examined and Not Supported

**That accelerator results are "all made up" or a racket.** Rejected [D]. The machines produce effects that are used outside the loop that interprets them, most plainly in semiconductor manufacture, and low-energy ion-beam analysis is calibrated against references its software did not create. The intuition behind the claim — that software can encode the theory it then confirms — survives and is documented above. The conclusion that the results are fabricated does not.

**That the loop is equally closed everywhere.** Rejected [D]. Its length and the strength of its external anchors vary enormously between a tandem doing backscattering and a collider inferring a short-lived particle.

# Version Log

| Version | Date | Status | Change |
|---|---|---|---|
| v1 | 2026-11-24 | active | Hypothesis stated from the Université de Montréal lab visit; strongest form, documented instances, what breaks the loop, field test proposed. |

# References

Entries 6–7 verified from the facility's own pages on 2026-11-24. Entries 1–5 and 8–9 were compiled from recall in a voice session and must be verified before this document is treated as closed.

1. Hanson, N.R. (1958). *Patterns of Discovery*. Cambridge University Press.
2. Duhem, P. (1906). *La Théorie physique : son objet, sa structure*. Paris: Chevalier et Rivière.
3. Collins, H.M. (1985). *Changing Order: Replication and Induction in Scientific Practice*. London: Sage.
4. Franklin, A. (1986). *The Neglect of Experiment*. Cambridge University Press.
5. Galison, P. (1987). *How Experiments End*. University of Chicago Press.
6. CCPAC — Université de Montréal ion-beam facilities. https://ion.lps.umontreal.ca/
7. Laboratoire Technologique Avancé, Université de Montréal — Ion beams facility. https://wiki.umontreal.ca/spaces/LTA/pages/215585026/Ion+beams+facility
8. Rutherford, E. (1911). The scattering of α and β particles by matter and the structure of the atom. *Philosophical Magazine*, 21, 669–688.
9. Chu, W.-K., Mayer, J.W. & Nicolet, M.-A. (1978). *Backscattering Spectrometry*. New York: Academic Press.
