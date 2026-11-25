---
title: The Closed Loop
subtitle: Can a machine, its software and its theory confirm one another without ever touching reality? A hypothesis, its strongest form, and what would break it
author: Robin
date: 2026-11-24
version: v1
status: active — hypothesis stated and partly tested; field test proposed; references verified against primary sources on 2026-11-25 (entries 6–7 stand on the 2026-11-24 check)
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

The decisive move is cheap. Bring the physicist a sample whose composition you know and he does not. If the screen reports it correctly, the loop touches reality at that facility. If it cannot, something has been found. The same logic, scaled up, is exactly what blind analysis does in particle physics: hide the answer from the people interpreting the data until the method is frozen (10).

# Where the Hypothesis Bites Hardest

The loop is longest where the chain from signal to claim is longest — the LHC, where an observed "particle" passes through trigger selection, reconstruction, simulation-derived corrections and statistical models before it becomes a claim. That is the terrain the rest of this archive examines, and it is where the closed-loop hypothesis retains real force [B].

# Claims Examined and Not Supported

**That accelerator results are "all made up" or a racket.** Rejected [D]. The machines produce effects that are used outside the loop that interprets them, most plainly in semiconductor manufacture, and low-energy ion-beam analysis is calibrated against references its software did not create. The intuition behind the claim — that software can encode the theory it then confirms — survives and is documented above. The conclusion that the results are fabricated does not.

**That the loop is equally closed everywhere.** Rejected [D]. Its length and the strength of its external anchors vary enormously between a tandem doing backscattering and a collider inferring a short-lived particle.

# Version Log

| Version | Date | Status | Change |
|---|---|---|---|
| v1 | 2026-11-24 | active | Hypothesis stated from the Université de Montréal lab visit; strongest form, documented instances, what breaks the loop, field test proposed. |
| v1 | 2026-11-25 | active | Reference list verified against primary sources. Corrected (1) missing subtitle, (2) title and publisher — the entry carried the 1914 second-edition title under the 1906 first-edition year — and (8) missing series, issue, article number and DOI. Added ISBNs/DOIs to (3), (4), (5) and (9). Added (10) Klein & Roodman 2005 and re-pointed the blind-analysis citation in “A Proposed Field Test” from (5) to (10): blind analysis dates from c. 1990 and is not documented in Galison 1987. Entries 6–7 not re-checked — no network route to umontreal.ca from this session. |

# References

Entries 1–5, 8 and 9 were verified against primary sources on 2026-11-25 — library catalogue records (Michigan State, Texas A&M, TU München, Open Library, WorldCat), publisher records (Cambridge University Press, University of Chicago Press, Academic Press/Elsevier, Princeton University Press) and journal and DOI metadata — and corrected where they were wrong; entry 10 was added on the same date. Entries 6–7 were verified from the facility's own pages on 2026-11-24 and could not be re-checked on 2026-11-25, because this session had no network route to umontreal.ca; they stand on the earlier check and are the only entries in this list not confirmed on 2026-11-25.

1. Hanson, N.R. (1958). *Patterns of Discovery: An Inquiry into the Conceptual Foundations of Science*. Cambridge: Cambridge University Press. (First edition; pre-ISBN. Record: https://openlibrary.org/books/OL6263737M)
2. Duhem, P. (1906). *La Théorie physique : son objet et sa structure*. Paris: Chevalier et Rivière. (2nd, revised and enlarged ed., Paris: M. Rivière, 1914, whose title drops the “et”. The holism argument cited at (2) above is located in the 1914 2nd ed. at p. 303 and in the standard English translation — Duhem, P. (1954). *The Aim and Structure of Physical Theory*, trans. P.P. Wiener. Princeton: Princeton University Press — at pp. 199–200; Part II, ch. VI, “Physical Theory and Experiment”. The translation is made from the 1914 2nd ed., so an English-reading checker should use Wiener’s pagination, not the 1906 first edition’s.)
3. Collins, H.M. (1985). *Changing Order: Replication and Induction in Scientific Practice*. London and Beverly Hills: Sage Publications. ISBN 0-8039-9717-5 / 0-8039-9757-4. (2nd ed., Chicago: University of Chicago Press, 1992, ISBN 978-0-226-11376-0. Nothing cited here is page-specific — the experimenter’s regress is set out in both editions — so either edition answers the citation.)
4. Franklin, A. (1986). *The Neglect of Experiment*. Cambridge: Cambridge University Press. ISBN 0-521-32016-X.
5. Galison, P. (1987). *How Experiments End*. Chicago: University of Chicago Press. ISBN 978-0-226-27915-2.
6. CCPAC — Université de Montréal ion-beam facilities. https://ion.lps.umontreal.ca/
7. Laboratoire Technologique Avancé, Université de Montréal — Ion beams facility. https://wiki.umontreal.ca/spaces/LTA/pages/215585026/Ion+beams+facility
8. Rutherford, E. (1911). LXXIX. The scattering of α and β particles by matter and the structure of the atom. *The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science*, Series 6, 21(125), 669–688. DOI: 10.1080/14786440508637080
9. Chu, W.-K., Mayer, J.W. & Nicolet, M.-A. (1978). *Backscattering Spectrometry*. New York: Academic Press. ISBN 0-12-173850-7.
10. Klein, J.R. & Roodman, A. (2005). Blind analysis in nuclear and particle physics. *Annual Review of Nuclear and Particle Science*, 55, 141–163. DOI: 10.1146/annurev.nucl.55.090704.151521
