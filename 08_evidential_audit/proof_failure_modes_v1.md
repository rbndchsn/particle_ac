---
title: Where the Proofs Could Fail
subtitle: A failure-mode audit of eight load-bearing proofs in particle physics — what each rests on, how it could return the expected answer while being wrong, what would detect that, and whether anyone has looked
author: Robin
date: 2026-11-24
version: v1
status: complete — eight proofs audited, framework established from primary philosophy of science, Tier D closing section written and binding
source_files: 07_epistemic_audit/known_versus_assumed_v1.md; 07_epistemic_audit/closed_loop_v1.md; 04_software_algorithmic/software_stack_bias_v1.md; 03_hardware_systems/trigger_data_destruction_v1.md; 00_method/claims_register_v1.md
---

# What This Document Is, and What It Is Not

This is a failure-mode audit. For each of eight proofs it asks five questions: what is claimed, what the claim rests on, how the apparatus could return the expected answer while the claim is false, what would detect that, and whether anyone has checked.

The distinction between the fourth question and an allegation is the whole document.

Establishing that a proof has a failure mode is not evidence that the failure occurred. A bridge has load limits whether or not it has ever collapsed. The engineering value of knowing the limit is entirely separate from any claim that the bridge is falling down. A proof whose failure mode has been probed and closed is a *stronger* proof than one whose failure mode has never been named — and the deliverable here is a map of which is which, not a verdict on physics.

Two failures would destroy this document. Manufacturing doubt where a proof is well anchored would make it dismissible by any specialist in one paragraph. Softening a genuine gap would make it worthless. Several of the eight proofs below turn out to be anchored far better than a critic would expect, and that is reported as a finding. Several have specific, named, unprobed failure modes, and that is reported without hedging.

Every substantive claim carries a tier:

- **[A]** Documented in primary literature.
- **[B]** Contested, with named advocates on both sides.
- **[C]** Structural inference — the reasoning is stated, together with what would falsify it. A Tier C item is never a finding.

A closing Tier D section lists claims examined and *not* supported, including the claim this document most needs to reject.

# The Governing Framework

The questions this audit asks are not novel and not fringe. They are the standing subject matter of the philosophy of experiment, and the field's sharpest formulations come from inside it.

## Duhem: no hypothesis is tested alone

Pierre Duhem argued in *The Aim and Structure of Physical Theory* (1906) that a physicist cannot separate one hypothesis from the others it depends on; the attempt is "a chimera" (1). When a predicted phenomenon fails to appear, doubt falls on "the whole theoretical scaffolding used by the physicist," and the experiment shows that at least one premise is wrong, but "where the error lies is just what the experiment does not tell us" (1) [A].

Duhem drew the consequence that physics has no crucial experiments: hypotheses do not come in exhaustive pairs, so an experiment cannot establish one of two rivals (1) [A]. Quine's 1953 "Two Dogmas of Empiricism" credited Duhem and pushed further, claiming "any statement can be held true come what may"; the combined view is the Duhem–Quine thesis. Duhem's own claim was the weaker and more defensible one — that what an anomaly refutes is ambiguous — and he would not have accepted Quine's version (1) [A].

For this audit, Duhem supplies the method: the "What it rests on" heading under each proof is an attempt to enumerate the theoretical group that the experiment actually tests. That list is the core of each section.

## Hanson: observation is theory-laden

Norwood Hanson argued in *Patterns of Discovery* (1958) that seeing is "a theory laden undertaking" (2) [A]. The point extends directly to instrument-generated observation: reading a number off a detector is an inference through a model of the detector.

The mainstream assessment is worth stating precisely, because it is frequently misquoted in both directions. The Stanford Encyclopedia's current treatment holds that theory-ladenness does not by itself show results cannot be objectively useful; that assuming the theory under test is sometimes benign; and that circularity can be mitigated by identifiable strategies (6) [A]. Theory-ladenness is a feature to be managed, not a reason for scepticism. It tells you where to look, not what you will find.

## Collins: the experimenter's regress

Harry Collins stated the problem in its sharpest form in *Changing Order* (1985): "a correct outcome is one obtained with a good experimental apparatus," and "a good experimental apparatus is one that gives the correct outcome" (3, 4) [A]. Collins argued that no formal criteria break the circle, that calibration with a surrogate signal cannot independently establish reliability, and that the circle is in practice closed by community negotiation shaped by career and social interest (5) [A]. His principal case was Joseph Weber's claimed detection of gravitational waves against six null experiments.

Allan Franklin's rebuttal is the other half of the mainstream position and is equally primary. Franklin accepted the regress as a genuine problem — "experimental work can only be used as a test if some way is found to break into the circle" — and then showed how the circle was in fact broken in the Weber case (4) [A]. The critics shared data and analysis programs; they ran Weber's own preferred non-linear algorithm on their own data and still found nothing; they searched for the specific error Weber's hypothesis predicted; and they injected known pulses and observed the output, which Weber's procedure failed to detect (4) [A]. Douglass found a programming error that had generated nearly all the claimed coincidences on one four-day tape, and Weber had reported a coincidence between detectors whose data were recorded four hours apart (4) [A]. Franklin's conclusion: "the regress can be broken by reasonable argument," and "there are no grounds for belief in the experimenters' regress" (4) [A].

Note what Franklin concedes in passing, because this audit leans on it: calibration "was not decisive in the case of gravity wave detectors, nor should it have been," though it is often legitimate and important elsewhere (4) [A]. Whether calibration breaks a loop is a question to be answered case by case, not a general licence.

## Pickering, Hacking, Galison: mutual adjustment and self-vindication

Andrew Pickering's *Constructing Quarks* (1984) describes the material apparatus, its theoretical model and the phenomenal model as "plastic resources" brought into mutual support: "Achieving such relations of mutual support is, I suggest, the defining characteristic of the successful experiment" (5) [A]. Ian Hacking later generalised this as "self-vindication": stable science arises when ideas, things and marks are brought into mutual consistency (5) [A].

Pickering's own case study is the one every section of this audit should be read against. Giacomo Morpurgo searched for fractional charges, adjusted his apparatus until it returned integral charges, and then reported finding no fractional charges — while William Fairbank, with a different apparatus, claimed the opposite (5) [A]. This is the failure mode this document is about, in its purest documented form: an apparatus tuned until it returns the expected answer, then used to report that answer.

The standard critique of Pickering is that the natural world drops out of his account, and that the Morpurgo case in fact turned on a failed known-value check rather than on theory alone (5) [A]. Robert Ackermann's counter is that the apparatus is less plastic than the theory, which gives an asymmetry the mutual-adjustment picture misses (5) [A]. That asymmetry is the main reason several of the proofs below come out well.

Peter Galison's *How Experiments End* (1987) (8) adds the point that experiments end when experimenters believe the result will "stand up in court," that different members of one collaboration may find different evidence decisive, and — most relevant here — that theory shapes what counts as an effect and what counts as background (5) [A]. Background elimination is not peripheral to an experimental claim; it is central to it. Galison's weak-neutral-current case turned on excluding a neutron background (5) [A]. Every simulation-derived background in sections 2 and 5 below is an instance.

## Klein and Roodman: the bias is measurable in the record

One empirical result belongs in the framework rather than in any single section. Klein and Roodman surveyed blind analysis in nuclear and particle physics and documented the signature of experimenter bias in the Particle Data Group record itself. For the neutron lifetime, the K⁰S lifetime, a particle mass and g_A/g_V, successive measurements clustered nearer the *prior published averages* than the final values: χ² of 131.2 for 83 degrees of freedom around the prior averages, against 249.7 for about 82 around the final average (10) [A]. Measurements of the speed of light from 1930 to 1940 sit 17 km/s from the later accepted value, with a post-mortem speculating that an investigator "continues to search until he gets a result close to the accepted value" (10) [A]. Dunnington warned in 1932 that it is "easier than is generally realized to unconsciously work toward a certain value" (10) [A].

Their methodological conclusion is the one that matters for this audit: experimenter bias differs from other biases because "the size of an experimenter's bias cannot be estimated," so it can only be prevented, not corrected (10) [A]. The authors are careful, and so is this document: they state that they "cannot say conclusively whether bias has influenced measurements," and that the clustering could reflect unrecognised systematics or physical corrections instead (10) [A].

The practical consequence is that **whether a given result was blinded is a first-order question about its strength**, and it is asked below wherever the answer is on record.

# Proof 1 — The Electron Anomalous Magnetic Moment

## The claim

The electron's magnetic moment is the most precisely measured property of an elementary particle, and its agreement with the Standard Model calculation is the field's showpiece.

The 2023 measurement gives g/2 = 1.001 159 652 180 59 (13), a fractional uncertainty of 1.3 parts in 10¹³, or 0.13 parts per trillion (11, 12) [A]. Equivalently a_e^exp = 1 159 652 180.59(13) × 10⁻¹² (15) [A].

The Standard Model prediction is dominated by QED, with the known hadronic and electroweak terms small but no longer negligible at this precision: hadronic vacuum polarisation at leading order 1.89(3) × 10⁻¹², next-to-leading order −0.2263(35) × 10⁻¹², next-to-next-to-leading order 0.02799(17) × 10⁻¹², hadronic light-by-light 0.0351(23) × 10⁻¹², and electroweak 0.03053(23) × 10⁻¹² (15) [A].

And here the showpiece stops being a test. The prediction is a function of the fine-structure constant α, which must be imported. With the two best independent α determinations the prediction splits:

- Caesium-based α: SM = 1 159 652 181.59(23) × 10⁻¹², giving experiment − theory = −1.00(26), a **−3.8σ** disagreement (15) [A].
- Rubidium-based α: SM = 1 159 652 180.24(9) × 10⁻¹², giving +0.35(16), a **2.3σ** disagreement (15) [A].

The two α values are α⁻¹(Rb) = 137.035 999 2052(97) and α⁻¹(Cs) = 137.035 999 045(27), which **disagree with each other by 5.5σ** (15) [A]. The review's own reading is that the spread from −3.8σ to +2.3σ is "a manifestation of discrepant measurements of α rather than a hint of a possible deviation from the SM" (15) [A].

Gabrielse and Venanzoni state the position without euphemism: the main obstacle to an electron-based Standard Model test is "not theoretical" but obtaining an accurate measured α; two determinations have the needed precision but "disagree by more than 5 standard deviations"; and the achievable test is therefore limited to about 0.7 × 10⁻¹², half the α discrepancy (12) [A].

So the headline claim should be stated as: **the electron g−2 comparison is currently a 0.7 ppt-level consistency check limited by an imported constant whose two best determinations are mutually incompatible at 5.5σ.** It is not a 0.13 ppt test of QED. CODATA 2022 handles the inconsistency by inflating uncertainties: "The recommended value includes an expansion factor of 2.5 on the uncertainties of both the measurement input data and the QED theory of the electron anomaly," applied so that all values lie within two expanded standard deviations of the CODATA value (16) [A]. The recommended α⁻¹ = 137.035 999 177(21) (16) [A].

## What it rests on

**On the measurement side:**

1. A single-electron quantum cyclotron in a cylindrical Penning trap, and a theoretical model of that cavity. The cavity shift is the *only* correction applied to the directly measured value, and it uses a renormalised calculation assuming a perfect cylinder with one quality factor Q for TE modes and another for TM modes; the authors fit trap dimensions to observed frequencies, subtract ideal-mode shifts for the 72 observed modes and add back contributions using measured frequencies and Q values (11) [A].
2. A lineshape model for the cyclotron and anomaly resonances.
3. Corrections for nuclear paramagnetism, anomaly power shift and magnetic field drift (11) [A].
4. Quantum electrodynamics of the bound electron in the trap field — the very theory under test — to relate measured frequency ratios to g.

**On the theory side:**

5. Five orders of QED perturbation theory. The tenth order comprises **12,672 vertex diagrams**, of which 6,318 contain at least one electron loop and 6,354 have none; the no-loop set is "Set V" (14) [A].
6. Mass-dependent terms involving the muon and tau masses, imported.
7. Hadronic vacuum polarisation and hadronic light-by-light contributions, taken from data-driven evaluations (15) [A] — so the electron's "pure QED" showpiece carries a hadronic term inherited from exactly the input class that destabilised the muon result (section 8).
8. The electroweak contribution, hence the full Standard Model gauge structure.
9. The imported α, hence the entire atom-interferometry chain: atomic masses, photon recoil measurements, and the theory of the recoil measurement.
10. The assumption that the perturbation series is usefully truncated at five loops. No sixth-order (twelve-loop) calculation exists; the review states plainly that "no actual calculations have been performed" at that order (15) [A].

## How it could fail

**(a) The α tension is physical rather than a systematic error in one atom-interferometry experiment.** If so, both the Cs and Rb α values are "correct" measurements of different things, and no α imported into a_e is the right one. The apparatus would return a_e correctly, the calculation would be right, and the comparison would still be meaningless — while appearing, after CODATA's 2.5 expansion factor, to be consistent. Note what the expansion factor does: it is applied to the *QED theory uncertainty of the electron anomaly* as well as to the measurements (16) [A]. An inconsistency in the α inputs is thereby converted into an enlarged error bar on the theory, which guarantees apparent consistency. This is not fraud; it is standard metrological practice for inconsistent input data. But it means **the consistency of a_e with the Standard Model at the CODATA level is partly an artefact of the procedure that handled the inconsistency** [C — inference from the stated procedure; falsified if CODATA's documentation shows the expansion factor does not affect the a_e comparison, or if the comparison is quoted using unexpanded inputs].

**(b) A correlated error across both a_e measurements from the same group.** All modern high-precision a_e values come from one lineage: Washington in 1987, then the Gabrielse group at Harvard (2006, 2008) and Northwestern (2023) (12) [A]. The 2023 paper explicitly advises **against averaging the 2008 and 2023 results "because their correlations are hard to determine"** (11) [A]. That is a statement, by the authors, that the two numbers are not independent in a quantifiable way. A systematic rooted in the trap design, the cavity-mode model, or the lineshape treatment would propagate to every member of the lineage, and would show up as consistency between measurements rather than as disagreement.

**(c) The cyclotron lineshape mismatch is a real physical effect rather than field noise.** This is the specific, documented soft spot. In the 2023 measurement **the anomaly lineshape matches the prediction but the cyclotron lineshape does not** (11) [A]. The authors suspect unwanted magnetic field fluctuations, averaged differently in the two measurements, which could account for the observed 0.5–0.8 ppb broadening; the cyclotron-broadening entry is the single largest systematic at 0.94 × 10⁻¹³, against a total of 1.3 × 10⁻¹³ (11) [A]. If the mismatch instead reflects an unmodelled interaction between electron and trap, the correction derived from the field-fluctuation hypothesis would be the wrong size, and the error would be in the dominant term. The quoted number would shift while remaining self-consistent.

**(d) A common-mode error in the five-loop QED coefficient.** This failure mode is not hypothetical. It happened, and it is documented in detail below.

**(e) Truncation.** If the series is less convergent than assumed, a twelve-loop term could matter at the precision now reached. Nobody knows, because nobody has computed it (15) [A].

## What would detect it

- A third α determination of comparable precision, by a method sharing neither the Cs nor the Rb systematics. Gabrielse and Venanzoni say exactly this is needed, resting on atomic masses and atom recoils (12) [A].
- An a_e measurement by a second group with a different trap geometry, cavity-mode structure and lineshape treatment.
- An independent attack on the cyclotron lineshape — a direct measurement of the field fluctuations the authors hypothesise, rather than an inference from the lineshape itself.
- A third, methodologically different computation of the tenth-order coefficient.
- A twelve-loop estimate, even a crude bound.

## Has anyone looked

**The five-loop dispute: looked at, found an error, and resolved — and this is the most instructive episode in the whole document.**

The tenth-order coefficient has been computed numerically by exactly **two** efforts: Aoyama–Hayakawa–Kinoshita–Nio (AHKN) and Sergey Volkov (14) [A]. Volkov's independent recalculation of the no-loop Set V disagreed with AHKN at **5σ** (13) [A]. The numbers:

| Source | Set V value |
|---|---|
| AHKN 2019 | 7.668 (159) |
| AHKN 2020 | 7.604 (140) |
| Volkov 2019 | 6.793 (90) |
| Volkov 2024 | 6.857 (81) |
| Volkov combined | 6.828 (60) |
| AHKN 2024 (revised) | 6.800 (128) |

(14) [A]. The original AHKN2020 − Volkov2019 difference was +0.780 (165), about 4.7σ; AHKN2020 against Volkov2024 was about 4.5σ (14) [A].

AHKN then audited their own calculation diagram by diagram, found no inconsistency in method, and traced the discrepancy to **98 integrals, each containing a single second-order self-energy subdiagram, affected by insufficient Monte Carlo statistics**. Recomputing them with more sampling lowered AHKN2020 by 0.803 (72) and resolved the tension (14) [A]. The current total is A₁⁽¹⁰⁾ = 5.887(55), a weighted average of Volkov's 5.891(61) and AHKN's revised 5.870(128) (15) [A].

The brief for this document asked whether Volkov's 5σ disagreement is live. **It is not: the dispute is resolved, in Volkov's favour, and the reviews now report the two calculations as consistent (14, 15) [A].** Reporting it as an open 5σ crack in QED would be false.

What it is instead is more interesting, and it is a finding:

> For five years, from 2019 to 2024, the canonical value of the five-loop QED coefficient used in the field's showpiece precision test was wrong by roughly 0.8 in Set V — an error of about five times its own quoted uncertainty. It was wrong because of under-sampled Monte Carlo integration in 98 of 6,354 diagrams. It was detected **only** because one person, outside the originating group, redid the calculation. Had Volkov not done so, there is no mechanism in the field that would have found it. [A — the sequence of papers (13, 14) establishes every step.]

That is the strongest available empirical argument for exactly the kind of auditing this archive does, and it comes from inside the field.

The residual exposure is that **n = 2**. Two numerical efforts now agree. There is no third. Agreement between two is enough to detect an error in one, as it did, but it is not enough to detect an error common to both — and both use diagrammatic numerical integration, which is the shared element.

**A genuinely different route is being attempted and is nowhere near sufficient precision.** A lattice-QED numerical perturbative calculation describes itself as "an intermediate step toward giving the five-loop coefficient independently of the preceding studies," explicitly motivated by the discrepancy; the authors reached toward five-loop coefficients but state "we refrain from presenting the values of our result because they are not conclusive ones," with roughly 40% error on the two-loop point and 20–30% systematic uncertainty on the photon-mass extrapolation, and estimate that lattices of L ≈ 128 would be needed for a meaningful result (18) [A]. The orders below five are in better shape: the sixth-order term has an analytic result by Laporta and Remiddi agreeing with Kinoshita's numerical evaluation, and the eighth order has Laporta's near-analytic result agreeing with an independent numerical calculation (15) [A]. The thinness is specific to the tenth order.

**The α tension: looked at, open.** CODATA 2022 includes all three determinations (the a_e-derived value, the Rb recoil h/m and the Cs recoil h/m) as input data and applies the 2.5 expansion factor rather than excluding any of them (16) [A]. The review states the discrepancy was unresolved as of 2025 (15) [A]. This is a known, named, actively worked problem, not a hidden one. Advocates on both sides are the Berkeley (Cs, Parker et al. 2018) and LKB (Rb, Morel et al. 2020) groups [B].

**The cyclotron lineshape mismatch: named by the authors, not independently investigated.** The 2023 paper identifies the mismatch, offers the field-fluctuation hypothesis, and folds the effect into the cyclotron-broadening systematic (11) [A]. **No published independent investigation of this mismatch exists** — no second group, no alternative lineshape model from outside the collaboration, no direct measurement of the hypothesised fluctuations. [A on the absence, from a literature search returning nothing; the claim is falsified by the production of any such study.] Given that this is the largest single systematic in the most precise measurement of any elementary-particle property, that gap is the most consequential unexamined item in this section.

**A second a_e apparatus: none.** A new Gabrielse-group measurement aiming for ten times better precision is underway (12) [A] — the same lineage. No second group is pursuing a_e at this precision.

**Twelve-loop QED: nobody has looked, and the review says so** (15) [A].

## Verdict on Proof 1

Well anchored in a specific and unusual way: **this proof's weaknesses are documented by its own practitioners, in print, in numbers.** The reviews state that the test is α-limited, the measurement paper states that its lineshape model fails on the cyclotron resonance and that its own two results should not be averaged, CODATA states that it expanded the uncertainties to absorb an inconsistency, and the g-2 review states that no twelve-loop calculation exists. Nothing in this section was dug out against resistance.

What is genuinely thin: n = 2 on the five-loop coefficient with a shared method, n = 1 group on the modern measurement, and no independent work on the dominant systematic.

# Proof 2 — The Higgs Discovery

## The claim

ATLAS reported a local significance of 5.9σ, reduced from 6.0σ by including energy-scale and resolution systematics, corresponding to a background fluctuation probability of 1.7 × 10⁻⁹; the global significance after look-elsewhere correction was approximately **5.1σ for a local excess anywhere in 110–600 GeV, rising to 5.3σ for 110–150 GeV**. The mass was 126.0 ± 0.4 (stat) ± 0.4 (sys) GeV and the signal strength μ̂ = 1.4 ± 0.3 (19) [A].

CMS reported a local significance of **5.0σ**, against an expected 5.8σ for a Standard Model Higgs at that mass, with the excess most significant in γγ and ZZ; mass 125.3 ± 0.4 (stat) ± 0.5 (syst) GeV (20) [A].

The combined ATLAS+CMS signal strength relative to the Standard Model is 1.09 ± 0.11, with ATLAS at 1.20 and CMS at 0.97 (26) [A].

## What it rests on

1. **A fitted background in the highest-weight channel.** For H→γγ, ATLAS fitted the diphoton mass spectrum in 100–160 GeV in each category with shape and normalisation free; simulation was used for bias studies and cross-checks, not for the main estimate. The functional forms were a fourth-order Bernstein polynomial, an exponential of a second-order polynomial, or a plain exponential, depending on category (19) [A]. This is a strength, and it should be said so: the dominant-sensitivity channel does not take its background from simulation.
2. **A simulation-derived background in the other high-resolution channel.** For H→ZZ*→4ℓ, the irreducible ZZ* background was **estimated from Monte Carlo simulation, normalised to the theoretical cross section**; only the reducible Z+jets and tt̄ components came from data control regions (19) [A].
3. **Simulated signal acceptance and efficiency.** ggF and VBF signal samples from POWHEG+PYTHIA, WH/ZH/ttH from PYTHIA, all passed through full Geant-based ATLAS detector simulation to obtain acceptances and efficiencies; the cross sections themselves from separate theoretical calculations (19) [A]. The signal strength μ is a ratio to a theoretically computed denominator.
4. **Trigger acceptance.** The excess exists only among events the trigger kept. Trigger menus are built from theoretical expectation, and discarded events are unrecoverable (see `03_hardware_systems/trigger_data_destruction_v1.md`).
5. **A choice of look-elsewhere search region.** 110–600 GeV or 110–150 GeV, which moves the global significance from 5.1σ to 5.3σ (19) [A].
6. **The Standard Model Higgs signal hypothesis as the template.** The spin-parity and coupling structure assumed in the fit.
7. **Geant4's hadronic and electromagnetic shower modelling**, common to both experiments.
8. **The parton distribution functions** entering every production cross section.
9. **A correlation model** when the two experiments are combined.

## How it could fail

**(a) Background functional-form bias in H→γγ.** If the true background shape departs from the chosen family in a way that mimics a narrow peak near 125 GeV, the fit returns a signal. The mechanism is concrete: a smooth falling spectrum fitted with a low-order polynomial over a wide window will absorb genuine structure and can also generate apparent structure, and which happens depends on the form chosen.

**(b) ZZ* normalisation error in the four-lepton channel.** The irreducible background is normalised to a theoretical cross section (19) [A]. If that cross section is low by a modest factor in the relevant kinematic region, the four-lepton excess is inflated. The apparatus returns an excess; the excess is a background deficit in the model.

**(c) Correlated simulation error across both experiments.** ATLAS and CMS share Geant4 and share generator lineages. Geant4's agreement with calorimeter test-beam data is good but not perfect: both Geant4 alone and Geant4 with the FLUKA.CERN interface **overestimate the HEC π/e ratio by up to a few percent**, and Geant4 hadronic models underestimate longitudinal shower length while FLUKA overestimates it, especially above 120 GeV (29) [A]. An error in a shared shower model shifts both experiments' acceptances in the same direction, and their agreement then confirms the shared model rather than the physics.

**(d) Look-elsewhere under-correction.** If the effective number of independent trials is larger than the mass scan implies — because channels, categories, and analysis variants multiply the search space — the global significance is overstated. This is the mechanism Hooper quantifies for the 750 GeV case (section 8).

**(e) Signal-template dependence.** If the particle were not a Standard Model Higgs, the SM-template fit would still report an excess but the mass, strength and significance would be biased by the template.

## What would detect it

- Spurious-signal tests: fit a signal to background-only control regions and background-only simulation, and quantify the bias each functional form induces.
- A data-driven ZZ* normalisation from a control region rather than a theory cross section.
- Independent determination of the mass in a channel with different background construction, and consistency between them.
- Model-independent spin-parity and coupling tests after the fact.
- A correlation model for the combination, with sensitivity tests on the assumed correlations.
- Blinding, so that selection and background model are fixed before the signal region is seen.
- Test-beam validation of the shared shower simulation.

## Has anyone looked

**Almost all of it, and this is where the audit must be honest: Proof 2 is the best-probed of the eight.**

**Spurious signal: formalised, with a published numerical criterion.** ATLAS selects the H→γγ background functional form so that the bias in the extracted yield is small relative to the experimental precision. The bias — the "spurious signal" — is estimated as the largest absolute fitted signal yield when a signal with mass between 121 and 129 GeV is fitted to background control regions. The acceptance criterion at 95% CL is that the spurious signal be **less than 10% of the expected SM signal yield or less than 20% of the expected statistical uncertainty**; among forms that pass, the one with fewest parameters is chosen; the chosen model is then tested against one with an extra degree of freedom using sidebands only, with the simpler model rejected below a p-value of 5%; and the residual spurious-signal yield is carried as a systematic uncertainty (25) [A]. This closes failure mode (a) to the stated level. The residual exposure is that the test uses simulated background templates (Sherpa γγ, with γj and jj shapes obtained by reweighting using fractions measured in data) whose fidelity to the real background shape is not itself quantified in that context (25) [A] [C — the circularity is real but bounded by the data-driven fraction measurement; falsified by a demonstration that the Sherpa shape error is small compared with the spurious-signal threshold].

**Spin and parity: tested against specific alternatives, with the model dependence stated.** ATLAS excluded 0⁻ at 97.8% CL, 1⁺ at 99.97% CL, 1⁻ at 99.7% CL, and a graviton-inspired 2⁺ model at more than 99.9% CL for every tested gluon-fusion/quark-antiquark admixture (24) [A]. Crucially, signal yields for each alternative were treated as free nuisance parameters, so the exclusions **do not depend on assumed coupling strengths** (24) [A]. The paper does not claim a fully model-independent test: the alternatives are specific models, chosen because "given the large number of possible spin-2 models" one had to be, the 2⁺ result depends on the quark-antiquark fraction with the gluon-fusion fraction set by leading-order QCD, and the 1⁺/1⁻ cases invoke the Landau–Yang theorem to restrict production (24) [A]. So failure mode (e) is substantially closed for the hypotheses tested and open in principle for untested ones.

**Blinding: in use, with the lock-in point not precisely documented.** CMS states that it blinds Higgs property measurements so they are not tuned toward deviations from Standard Model expectations; that analysts do not look at the blinded region while adjusting selection criteria; that simulations and background methods are optimised before unblinding; that at least two independent teams carry out the analysis steps and the collaboration signs off before the signal region is unblinded (30) [A]. The page never says "finalised" or "frozen," so the exact lock-in point is not on record (30) [A].

**The correlation model: constructed, documented, and sensitivity-tested — and the test substantially weakens a claim this archive previously advanced.** In the ATLAS+CMS Higgs combination, theoretical uncertainties on the signal yield, some background theory uncertainties, and the beam-current component of luminosity are treated as **fully correlated**; PDF uncertainties are correlated between experiments per production process; QCD scale and underlying-event uncertainties are correlated within a process; signal acceptance and efficiency uncertainties are treated as uncorrelated because each experiment estimates them differently; experimental systematics are independent except for luminosity; and the analysis assumes a Standard-Model-like Higgs at a fixed 125.09 GeV, with the authors noting that reliance on the SM-based model is negligible for small deviations but could matter for large ones (26) [A].

The decisive numbers come from the ATLAS+CMS top-mass combination, which published its correlation assignments and a full scan. Shared-modelling categories are assigned ρ = 0.5 — matrix-element generator, QCD radiation, hadronisation, colour reconnection and underlying event — justified by the experiments using different generators and different variation schemes, with the paper acknowledging "no clear one-to-one mapping" for hadronisation. PDFs get ρ = 0.85, "driven by the same input data in PDF extractions." And explicitly: **"No category was identified to have ρ=1"** (27) [A]. The scan found the central value and uncertainty vary linearly with each correlation, with changes below 30 MeV; the shared-modelling half-variations are roughly 1–7 MeV on the central value and at most about 4 MeV on the uncertainty; the largest single sensitivity is b-JES at 26 MeV; and assuming adverse signs for mixed-impact categories changes the central value by at most 41 MeV and the uncertainty by 7 MeV — against a total combined uncertainty of 0.33 GeV (27) [A]. The ATLAS+CMS tt̄ cross-section combination similarly assigns LOW = 0.25 to tt̄ generator modelling, with the explicit justification that "since the methods and generators used to obtain them are different, the correlation is assumed to be LOW," chooses signs to maximise the total as "a conservative estimate," and reports that scanning the correlations produces no significant change, the largest effect being 0.15% from luminosity (28) [A].

This archive's claim C1a held that the inter-experiment correlation applied to shared modelling terms "appears calibrated on procedural difference between collaborations rather than on shared model lineage, where the true value for hadronisation is plausibly nearer 1 than 0.5." The first half is **confirmed verbatim** — the justification given is procedural difference, in the papers' own words (27, 28) [A]. The second half is **weakened**: the published sensitivity scans show that even adverse correlation choices move the top-mass combination by at most about 12% of its total uncertainty (27) [A]. C1a should be restated: the correlation value is a documented choice resting on procedural rather than genealogical grounds, and for the combinations where it has been scanned the numerical consequence is small. [A]

**What has not been looked at:** the sensitivity scans exist for the top mass and the tt̄ cross section. **No published scan of correlation assumptions exists for the 2012 discovery significance itself** — the quantity for which the two experiments' independence was rhetorically load-bearing. [A on the absence; falsified by production of such a study.] This is a narrow but real gap: the robustness demonstrated for a precision combination in 2024 is being borrowed, implicitly, by a discovery claim from 2012.

**The look-elsewhere region: contested in the philosophy literature, with a named advocate.** Richard Dawid's "Higgs Discovery and the Look Elsewhere Effect" (*Philosophy of Science* 82, 2015) is the primary treatment (21) [B]. Hooper's independent analysis of the general problem is the other (22) [B]. The physics papers state the region they used and the resulting global number (19) [A]; what they do not do is justify the region choice on principled grounds, and 110–600 against 110–150 is a 0.2σ swing (19) [A].

**The ZZ* theory normalisation: not independently replaced.** The 2012 discovery took the irreducible four-lepton background from simulation normalised to theory (19) [A]. No published data-driven cross-check of that normalisation, contemporaneous with the discovery, was located. Later measurements with much more data constrain it well, which retrospectively closes the gap but does not retrospectively close it *for the 2012 claim*. [C — inference from the 2012 paper's own method description; falsified by a 2012-era data-driven ZZ* determination.]

## Verdict on Proof 2

**Strongly anchored, and anchored by probes the field built itself.** The spurious-signal criterion, the blinding protocol, the independent-team requirement, the spin-parity exclusions with free-floating yields, and the published correlation scans are exactly the measures a hostile auditor would ask for. Someone was already asking.

The two residual items are narrow and specific: no correlation-sensitivity study for the discovery significance, and a theory-normalised irreducible background in one of the two high-resolution channels at the time of the claim.

# Proof 3 — Lattice QCD: Nine Hadron Masses from Three Inputs

## The claim

Dürr et al. (BMW collaboration, *Science* 2008) computed the light hadron spectrum from first-principles QCD. **Twelve** light hadrons are involved; **ten** are reported in Table 1 — the octet baryons N, Σ, Λ, Ξ; the decuplet Δ, Σ*, Ξ*, Ω; and the vector mesons ρ and K*. The π and K masses are *inputs*, not predictions (31) [A].

The bare parameters are fixed by three quantities: the isospin-averaged light quark mass m_ud, the strange quark mass m_s, and the overall lattice scale. The quark masses are fixed by the ratios M_π/M_Ξ and M_K/M_Ξ, and the scale by the Ξ mass — or, in a second independent analysis, by M_π/M_Ω, M_K/M_Ω and the Ω mass (31) [A].

This is where the familiar headline "nine masses from three inputs" comes from, and it needs stating precisely: **all three inputs are themselves hadron masses** (π, K, and either Ξ or Ω), and because the scale-setter is one of the ten tabulated hadrons, each analysis predicts **nine**. The authors report "Our results completely agree with experimental observations," with "fully controlled uncertainties" (31) [A]. Quoted uncertainties are at the 1–3% level; the nucleon in the Ξ-scale set is 0.936(25)(22) GeV (31) [A].

## What it rests on

This list is long because the question "what exactly is being tested versus assumed" has a long answer.

1. **The lattice action, which is QCD by construction.** Tree-level O(a²)-improved Symanzik gauge action with tree-level clover-improved Wilson fermions, six levels of stout link smearing, 2+1 flavours — degenerate u and d sea quarks plus a strange sea quark (31) [A]. The action *is* the hypothesis. Nothing in the calculation could return a non-QCD answer.
2. **Three lattice spacings**, a ≈ 0.125, 0.085 and 0.065 fm, with volumes reaching about (4 fm)³ and temporal extents about 8 fm; 14 simulation points (31) [A].
3. **A continuum extrapolation assumed linear in a².** The justification that discretisation errors are under about 1% at a ≈ 0.125 fm and scale linearly in a² rests on the authors' **own earlier scaling study** (31) [A]. This is the most important single auxiliary assumption in the calculation and its support is internal.
4. **A chiral extrapolation.** Pion masses down to about 190 MeV, with two functional strategies: a "chiral fit" linear in M_π² plus an M_π³ term following chiral perturbation theory, and a "Taylor fit" expanding around a non-singular point in M_π² with a quartic term (31) [A].
5. **An analysis-choice marginalisation.** The central value for each mass is the **median of 432 fit-procedure results**, weighted by fit quality, combining two normalisation methods, three pion-mass cuts and the two extrapolation strategies; statistical error by bootstrap; systematic and statistical errors added in quadrature (31) [A]. The 432 procedures are not independent measurements; they are a spread over analysis choices, converted into a systematic.
6. **Finite-volume control**, checked with a volume series at one point only (M_π ≈ 320 MeV, M_πL ≈ 3.5–7) (31) [A].
7. **Neglect of isospin breaking and electromagnetism.** Experimental masses are isospin-averaged; EM and isospin-breaking effects are described as "typically a fraction of 1%"; π and K masses use Dashen's theorem; higher-order corrections are neglected as "expected to be below the 3 per mil level" (31) [A].
8. **The Lüscher resonance formalism**, assumed (31) [A].
9. **One excluded data point:** the lowest-energy point for ρ and Δ at a ≈ 0.085 fm, dropped because the mass could not be extracted reliably there (31) [A].

## What is tested and what is assumed

This deserves its own paragraph because the brief asks for it directly.

**Assumed:** that the degrees of freedom are quarks and gluons with the QCD Lagrangian; that the lattice discretisation converges to that theory; the specific improvement scheme; the functional form of both extrapolations; Dashen's theorem; the Lüscher formalism; and the a²-linearity of the continuum limit.

**Tested:** that the *assumed* theory, with three experimental inputs, reproduces nine further measured numbers that it was not fitted to. That is a real test and a non-trivial one. A wrong theory of the strong interaction would not generically land nine hadron masses within 1–3%.

**Not tested, and this is the structural point:** the calculation cannot discriminate QCD from a rival theory of the strong interaction, because no rival is implemented in the action. It is a test of the *arithmetic and the extrapolations*, conditional on QCD, plus a consistency test of QCD's parameter economy. The honest framing is that lattice QCD demonstrates **QCD's internal sufficiency**, not QCD's uniqueness. [C — follows from the construction of the action; falsified by the existence of a lattice calculation that implements a non-QCD strong-interaction theory and compares.]

Richard Sommer's review supplies the companion point in the field's own words: **only dimensionless ratios are predictions. The overall scale must come from experiment, and every theory scale needs a phenomenological input** (32) [A].

## How it could fail

**(a) A wrong continuum extrapolation that happens to land near the right answer.** Three spacings constrain a linear-in-a² fit weakly if the true approach contains an a² ln a or a⁴ term of comparable size over that range. The fit would return masses consistent with experiment across the whole set, because the normalisation is fixed by a hadron mass in the same set — an error in the scale propagates to all masses coherently and partially cancels in the ratios that are actually compared.

**(b) Chiral extrapolation form error.** Extrapolating from 190 MeV to 135 MeV with a form whose higher orders are poorly convergent. The review literature states that at NNLO the contribution to meson masses is nearly as large as the NLO term, suggesting poor convergence, with omitted higher-order terms estimated at 3–5%, and that NNLO fits depend on phenomenological priors for the new low-energy constants (36) [A]. 3–5% is larger than the quoted 1–3% uncertainties.

**(c) Scale-setting error absorbed into agreement.** Because the scale is set by a hadron mass and the predictions are hadron masses, a systematic in the scale shifts everything together.

**(d) Analysis-choice selection.** The median of 432 procedures is a defensible estimator, but the *set* of 432 was chosen by the authors. If procedures that would have given discrepant answers were excluded as poor fits, and "poor fit" is partly judged by proximity to expectation, the spread understates the systematic. This is the Morpurgo mechanism (5) applied to a fit ensemble.

**(e) An approximation that is wrong but small enough to hide.** This has already happened once, demonstrably, and it is the single most valuable piece of evidence in this section.

## What would detect it

- Finer lattice spacings, to discriminate a² from other forms.
- Simulation *at* the physical pion mass, removing the chiral extrapolation.
- The same spectrum computed with a **different fermion discretisation** — the only check that probes the discretisation itself rather than the extrapolation within one scheme.
- Multiple scale-setting quantities, with the spread as a systematic.
- Independent collaborations on independent gauge ensembles.
- Explicit inclusion of QED and isospin breaking.

## Has anyone looked

**The quenched case is a documented, historical instance of the exact failure mode, and it was caught.** CP-PACS found that the quenched light hadron spectrum deviates systematically from experiment: "The magnitude of the discrepancy is at most 10%," reaching up to **7σ** for several particles, and "Our results unambiguously establish a discrepancy between the quenched hadron masses and the experimental values" (34) [A]. Moving to two dynamical flavours significantly reduced the K* and φ discrepancies in the continuum limit, and the quenched discrepancy was "consistent with phenomenological estimates of the quenching error" (34) [A].

Read that carefully. For years, quenched lattice QCD returned a hadron spectrum that was *approximately* right — within 10% — while resting on an approximation now known to be wrong. It looked like confirmation. It was detected only by relaxing the approximation and doing the much more expensive calculation. **That is proof, from inside lattice QCD, that an uncontrolled approximation can return the expected answer to within 10% and that the field will not notice until someone removes it.** [A] The relevant question for the 2008 result is therefore not whether its approximations are plausible but whether any remaining one could be wrong at the 1–3% level — and nobody can answer that for an approximation nobody has removed.

**Different discretisations: yes, and this is the strongest anchor in the section.** The light hadron spectrum has been computed by BMW (improved Wilson), the Hadron Spectrum Collaboration (anisotropic clover), PACS-CS (improved Wilson near the physical point), LHPC (mixed action, domain-wall valence on improved staggered sea), MILC (improved staggered) and ETMC (twisted mass), with RBC-UKQCD and QCDSF-UKQCD reporting preliminary nucleon results; the review states the results are "consistent among each other and reproduce the experimentally measured values" (36) [A]. Different fermion formulations have genuinely different discretisation errors, so agreement between them is meaningful evidence about the continuum limit, not merely agreement about a shared method. This is the kind of external contact Franklin's account requires (4).

**But the independence is partial, and the reviews say so.** The same review notes that Aubin et al. use MILC's staggered configurations and LHPC uses an Asqtad (MILC-type) sea, and that **all the analyses fix the quark masses using the pion and kaon masses** (36) [A]. FLAG is blunter and its statements are the single best evidence in this section:

> Calculations sharing gauge ensembles "are not really independent"; FLAG assumes 100% correlation where a source of error is shared, using the Schmelling prescription (33) [A].
>
> FLAG's colour-coding criteria are **"subjective and evolving,"** and systematic errors "are by their nature often subjective and difficult to estimate" (33) [A].
>
> Confidence in a lattice average **"cannot be quantified"** and **"is not reflected in the quoted errors"** (33) [A].

Those are the field's own words about its own error bars, and they are stronger than any external critic's formulation.

FLAG's quality thresholds are concrete: for a green star on the chiral extrapolation, M_π,min below 200 MeV with three or more pion masses; for the continuum limit, at least three lattice spacings with at least two below 0.1 fm and a range satisfying [a_max/a_min]² ≥ 2; averages are χ²-weighted with error bars stretched by √(χ²/dof) when χ²/dof > 1; updates using the same ensembles are not averaged with their originals; and different N_f are averaged separately because no way to estimate their difference is known (33) [A].

**Scale setting: looked at, and the disagreements are unresolved.** Sommer's review documents that static actions with different smearing give different r₀ and r₁ at finite spacing; that Lüscher's Wilson-clover and Wilson-plaquette definitions of t₀ differ by about **6%** in t₀/r₀² at a = 0.1 fm; that ALPHA's Λ-parameter changed by roughly **20%** after they computed r₀/a themselves, and HPQCD's f_Ds changed after a reanalysis of r₁; that for N_f = 2 the continuum-extrapolated r₀ values from ALPHA and ETM differ by a few sigma at the smaller pion mass; and that this disagreement is **"unexplained at present"** (32) [A]. The 2009 review independently reports that Sommer-scale estimates can differ by up to about 10% (36) [A].

**A foundational gap that is acknowledged and unclosed.** Rooted staggered fermions — the formulation underlying MILC and several of the "independent" cross-checks — are "in the wrong universality class in the strictly massless case," with only "numerical indication" of correct continuum behaviour away from the chiral limit; the rooting procedure rests on the assumption that a local operator with the same determinant exists, which **"is not established for the interacting case,"** though analytic arguments suggest non-local terms vanish in the continuum limit (35) [A] [B — this has named advocates on both sides and has been argued in the literature for two decades].

**QED and isospin breaking: now included by some groups, not by the 2008 calculation.** RBC-UKQCD included electromagnetic effects via quenched QED; up/down mass-splitting estimates were preliminary, with MILC giving m_u/m_d ≈ 0.432 against Aubin et al.'s 0.39 (36) [A].

**What has not been looked at:** no published external audit of the 432-procedure selection in the BMW analysis exists — no reanalysis of the same ensembles by an outside group using a differently-constructed procedure set. [A on the absence; falsified by production of such a reanalysis.] Given that the procedure set generates the quoted systematic error, and that FLAG itself calls systematic-error estimation subjective (33), this is a real and specific gap.

## Verdict on Proof 3

**Well anchored on the question it can answer, and the headline overstates what that question is.** Nine masses from three inputs is a genuine, non-trivial consistency test of QCD's parameter economy, strengthened substantially by agreement across genuinely different fermion discretisations. It is not, and cannot be, a discrimination of QCD against alternatives, because the action encodes QCD by construction.

The documented quenching episode shows that a wrong approximation can return a 10%-correct spectrum. The unclosed items are the rooting-locality assumption, the internally-justified a²-linearity, the unexplained r₀ disagreement, and the unaudited procedure ensemble.

# Proof 4 — Jets as Proxies for Partons

## The claim

A hadronic jet — a collimated spray of hadrons in a detector — licenses inference to a coloured point particle, a quark or gluon, that was never observed and in principle cannot be.

The confinement premise is stated flatly by the Particle Data Group: QCD predicts that quarks "cannot be observed as freely propagating particles"; they are confined inside hadrons or deconfined only in quark-gluon plasma; **"Experiments have produced no evidence for free propagating quarks"**; and every known charged system has charge an integer multiple of 1/3 e while quarks carry 1/3 or 2/3 (39) [A]. The sole exception is the top quark, observed decaying while still effectively free because its lifetime is too short for hadronisation (39) [A].

## What it rests on

1. **A jet algorithm with free parameters.** Gavin Salam's review states that "there is no single optimal way of defining jets"; a jet definition is an algorithm, its parameters (such as the radius R), and a recombination scheme taken together, and the choice should depend on the analysis (37) [A].
2. **Infrared and collinear safety.** Without IRC safety, tree-level and loop divergences fail to cancel and perturbation theory can give "infinite cross sections"; IRC-unsafe algorithms can have a single soft gluon turn two jets into one, and such unsafety can make higher-order predictions meaningless (37) [A].
3. **Perturbative QCD at the hard scale**, hence asymptotic freedom and factorisation.
4. **A hadronisation model**, which is non-perturbative and fitted. The underlying event is "a major cause of degradation" of jet energy resolution, and DØ found "rather large non-perturbative corrections from the underlying event" with R = 1, with CDF later attributing the size to the large R (37) [A].
5. **Parton distribution functions**, fitted to data.
6. **A jet energy scale calibration derived substantially from simulation.** The ATLAS calibration comes from the calorimeter response to single particles, measured in both data and simulation, and is derived separately for quark- and gluon-induced jets with correlations retained; the total JES uncertainty is about 2.5% at 20 GeV, 0.5% at 300 GeV and 0.7% at 4 TeV, improving to about 0.3% at 300 GeV when combined with in-situ p_T-balance measurements (41) [A].
7. **The parton concept itself**, which Salam calls ambiguous because divergent branching probabilities in perturbative QCD mean a prescription is needed to define it (37) [A].

## How it could fail

**(a) The jet-parton map is many-to-one or one-to-many in a way that biases the inference.** Salam names this directly: a boosted W or Z can give one jet from two partons, and QCD radiation gives jets substructure (37) [A].

**(b) "Quark jet" and "gluon jet" have no hadron-level referent, so measurements of their properties measure the labelling scheme.** This is the sharpest published statement of the problem and it comes from inside the field. Komiske, Metodiev and Thaler: **"there is no unambiguous definition of 'quark' or 'gluon' jets at the hadron-level"**; "no precise, practical, and hadron-level definition of jet flavor presently exists"; common practice "rel[ies] on ill-defined or unphysical parton-level information" such as parton shower event records; a per-jet flavour label is a "troublesome and potentially impossible notion"; individual jets "do not carry intrinsic flavor labels," and in data "one only ever has access to mixed samples"; and Pythia's flavour fractions "are not fully well-defined hadron-level concepts," shown only as a heuristic (38) [A].

**(c) Hadronisation-model error compensated by tuning.** If the hadronisation model is wrong in a way the tune absorbs, jets are reconstructed to the right energy with the wrong physical picture, and the calibration transfers the error into every derived quantity. This is the mechanism already documented in `04_software_algorithmic` as claim C3.

**(d) Flavour-composition error in the energy scale.** If the simulated quark/gluon mixture is wrong, the flavour-dependent calibration is applied in the wrong proportions.

**(e) Underestimated parton distribution uncertainties.** Every jet cross section is a convolution of a partonic calculation with fitted PDFs. Courtoy, Huston, Nadolsky and co-authors argue that uncertainties from common PDF ensembles "can be underestimated" in high-stake LHC and Tevatron measurements, that sampling of acceptable solutions is often unrepresentative, and that uncertainties "can reflect fitting methodology about as much as the strength of experimental constraints"; they report that their alternative scans give larger uncertainties on key 13 TeV cross sections than the nominal NNPDF4.0 values, and note that in the PDF4LHC21 reduced-data exercise NNPDF3.1's uncertainties were systematically smaller than CT18's and MSHT20's (42) [B — NNPDF's published response disputes the work, arguing many alternative solutions fail its smoothness requirements, which the authors say remains unclear (42)]. If the PDF uncertainty is understated, a jet-based measurement can agree with prediction inside an error bar that is too small, which is agreement manufactured by the error budget rather than by the physics.

## What would detect it

- Direct observation of a free quark. Never achieved, and QCD says it cannot be (39).
- Agreement between jet measurements and perturbative QCD predictions in regimes where hadronisation corrections are small and independently constrained.
- An operational, hadron-level definition of jet flavour that does not route through parton-shower records.
- Evidence for point-like spin-½ constituents from a channel that does not involve jets at all.

## Has anyone looked

**The decisive point: the parton inference does not rest on jets, and it never did.** This is where a critique of jet reasoning must concede the ground, because the primary evidence is strong, old, and independent of jet algorithms.

Kendall's Nobel lecture documents the chain. Bjorken predicted scaling; the first SLAC-MIT data showed it, and "It was immediately clear that the Bjorken scaling hypothesis was, to a good approximation, correct," holding approximately even at q² ≳ 1 GeV² and W ≳ 2.6 GeV (40) [A]. The inference ran from scaling and a weak q² dependence to point-like charged constituents scattering incoherently, following Feynman's parton model (40) [A].

The spin test is the part that matters most here, because it excludes alternatives rather than accommodating data. For spin-½ partons the naive parton model predicts R = σ_L/σ_T = q²/ν²; **spin-0 or spin-1 constituents would instead give a nonzero R in the Bjorken limit**. The measured quantity that vanishes when the Callan-Gross relation holds was consistent with zero apart from expected deviations at low q² and low x, establishing parton spin as ½ (40) [A]. The small measured R was also "totally incompatible" with Vector Meson Dominance, and diffractive models and bootstrap "nuclear democracy" were found inconsistent with the data by 1972; fractional rather than integral charges, and three valence quarks, were confirmed by neutrino measurements (40) [A].

So: **the licence for inferring point-like spin-½ fractionally-charged constituents comes from inclusive deep inelastic scattering structure functions and neutrino scattering, which involve no jet algorithm, no hadronisation model, and no jet energy scale.** Three named alternative frameworks were excluded. That is Duhemian discrimination of the kind Duhem thought impossible, achieved by a measurement that distinguishes spin hypotheses through a cross-section ratio. [A]

Jets are a *downstream convenience* for studying partons whose existence is established elsewhere. The audit question therefore narrows sharply: not "does the jet license the parton," but "what do jet-based measurements inherit from the jet-parton ambiguity?" On that:

**The ambiguity is named in the review literature, repeatedly, by the people who build the tools.** Salam: one "should never forget how ambiguous this association really is" (37) [A]. He treats partons as unobservable and jets as a practical representation, and says that "neither the photons… nor the jets… are of interest" in themselves — what matters is what jets help reveal (37) [A]. The 1990 Snowmass accord listed the properties a jet definition should have; Salam notes the title "Toward a standardization" signalled the standard was not settled, that by 2000 the community had "almost" met the requirements, that recommendations were only partly followed, and that some algorithms still failed them (37) [A].

**The flavour-label problem has been attacked constructively.** Komiske, Metodiev and Thaler propose a distribution-level operational definition: take two samples at fixed p_T, one more quark-like (Z+jet) and one more gluon-like (dijet), estimate reducibility factors from the extrema of the mixed-sample likelihood ratio, and define the quark and gluon distributions to be mutually irreducible — implemented with CWoLa classifiers and jet topics, with per-jet labels assignable only probabilistically (38) [A]. The approach is explicitly designed to avoid depending on "specific theoretical constructs such as factorization theorems" (38) [A]. This is the field diagnosing and then repairing its own definitional gap in print.

**The direct search for the thing that would break confinement has been run and reported null.** PDG maintains a standing Free Quark Searches review; it reports no evidence (39) [A]. And the history of that search contains Pickering's Morpurgo case: an apparatus adjusted until it returned integral charges, then used to report no fractional charges, against Fairbank's contrary claim (5) [A]. The Morpurgo episode is the documented instance of the failure mode for *this* proof — and the reason the community eventually discounted Morpurgo was a failed known-value check, not theory preference (5) [A].

**What is open:** the jet energy scale's flavour-response uncertainty depends on the simulated quark/gluon mixture, and the calibration is derived separately for the two classes (41) [A]. Since the two classes have no hadron-level definition (38) [A], the flavour-response uncertainty is an uncertainty with respect to a label that does not refer. This is not a hidden problem — both papers are explicit — but **no published study was located that propagates the Komiske-Metodiev-Thaler definitional critique into the jet energy scale flavour uncertainty.** [A on the absence; falsified by production of such a study.] That is a specific, tractable, unexamined item.

## Verdict on Proof 4

**Strongly anchored, via a route the question's framing obscures.** The inference to point-like spin-½ fractionally-charged constituents rests on inclusive deep inelastic scattering and neutrino data that excluded three named alternatives — not on jets. The jet-parton map is genuinely ambiguous, and the field says so in its own reviews in unusually candid language.

The open item is narrow: a flavour-dependent calibration keyed to a label with no hadron-level referent, with no published study of what that costs.

# Proof 5 — Missing Transverse Energy as Inference of Invisible Particles

## The claim

An imbalance in the vector sum of transverse momenta is read as evidence that something left the detector unseen — a neutrino, or a dark matter candidate. An absence is read as a presence.

ATLAS states the construction and its limits in one breath: missing transverse momentum is "an experimental proxy" for undetected particles; non-zero values can come from neutrinos or possible dark matter, but **fake MET from mismeasurement and pile-up can mimic it**, which is why a significance variable is used to separate real from fake; and the authors conclude that MET reconstruction is "well understood and reliably modelled by simulation" (43) [A].

## What it rests on

1. **The calibration of every other object in the event.** MET is built from fully calibrated electrons, photons, hadronically decaying taus, muons and jets, each with its own calibration, so analysis-level object systematics propagate directly into MET (43) [A].
2. **An ambiguity-resolution procedure** that removes detector signals already used by a higher-priority object, with specific rules for muon overlap with pile-up jets, muon energy loss, final-state radiation photons, and electron/photon-jet overlap (43) [A].
3. **A track-based soft term**, built from inner-detector tracks linked to the hard-scatter vertex and not used by any hard object. Tracks were chosen over calorimeter deposits because they resist pile-up better. The consequence is explicit: **neutral soft particles are therefore missed, which biases MET at low values, and reconstructed MET overestimates truth MET at low truth values** (43) [A].
4. **An assumption that object-type uncertainties are uncorrelated.** ATLAS states that "uncertainties for different object types are treated as uncorrelated" (43) [A].
5. **Event cleaning.** Jet-quality criteria on pulse shape, EM fraction, sampling fraction and charged fraction; events with any jet failing loose criteria discarded; tight quality plus a charged-fraction cut on the leading jet to suppress non-collision muons; Δφ(jet, p_T^miss) > 0.4 for every selected jet to reject mismeasurement; a lepton veto; and a primary vertex requirement (44) [A].
6. **A simulated irreducible background.** In the ATLAS monojet search, the dominant Z(→νν̄)+jets background is simulated with Sherpa, normalised to NNLO and reweighted for higher-order QCD and electroweak effects, with its normalisation constrained in a global fit to W→μν, W→eν, Z→μμ and top control regions. The fit returns a W/Z+jets normalisation factor of **1.27**. For the loosest signal region, Z(→νν̄) supplies about 138,000 of 245,900 predicted events; multijet and non-collision backgrounds together are about 1,060 of 245,900, roughly 0.4%; **almost all of the remainder comes from simulated samples**, and diboson yields are taken directly from simulation (44) [A].
7. **The calibration sample has zero signal by construction.** The main performance sample is Z→ℓℓ, which has no genuine MET; it is used to measure fake-MET behaviour, pile-up dependence, and the scale and resolution of the soft term, with the soft-term uncertainties set by the maximal data-MC difference (43) [A]. W→μν and tt̄, which do have real MET, are used to study response and bias against truth MET (43) [A].

Item 7 is the structural heart of this proof. The scale and resolution of the quantity used to claim an invisible particle are calibrated in a sample defined by the absence of invisible particles. That is not a flaw — it is the only sensible way to isolate the instrumental contribution — but it means **the calibration can validate the detector's behaviour in the absence of signal and cannot validate the inference drawn from the presence of signal.** [C — follows from the construction; falsified by a calibration sample with known, independently-determined non-zero MET.]

## How it could fail

**(a) A tail in the mismeasurement distribution that the Z→ℓℓ sample does not populate.** Fake MET arises from the tail of the jet response distribution. If that tail has a component absent in Z→ℓℓ topologies — a rare calorimeter pathology, a crack, dead material, a punch-through — the fake-MET estimate derived from Z→ℓℓ underestimates it in the signal topology, and the apparatus reports an excess of events with large MET. The excess is real as a measurement and false as an inference about particles.

**(b) The Z(→νν̄) normalisation is wrong.** A 1.27 normalisation factor is being applied to the background that constitutes over half the prediction (44) [A]. The factor is fitted in leptonic control regions, so it corrects jointly for generator mismodelling and acceptance. If the correction needed differs between the control topology and the signal topology — different jet multiplicity, different boson p_T spectrum — the extrapolation is biased, and the bias appears as an excess or deficit in MET.

**(c) The uncorrelated-object-uncertainty assumption fails.** If jet and soft-term mismeasurement share a common cause, the MET uncertainty is understated because the terms are added as if independent (43) [A].

**(d) Non-collision background underestimated in the extreme tail.** Beam-induced background and cosmic muons are rare but have no kinematic ceiling, so they populate the highest-MET bins where signal would appear.

**(e) The neutral soft component.** The track-based soft term misses neutral soft particles by construction (43) [A]. If the neutral fraction differs between calibration and signal topologies, a systematic MET offset results.

## What would detect it

- A validation sample with known, non-zero, independently-determined MET — W→ℓν with the lepton measured precisely enough to predict the neutrino momentum, which ATLAS does use for response and bias studies (43) [A].
- Data-driven measurement of non-collision background in the signal region.
- Correlation of a putative excess with detector geometry. A real invisible particle is uniform in azimuth and in detector region; a mismeasurement artefact is not.
- An independent signature for the same physics: mono-photon, mono-Z, vector-boson-fusion plus MET, which share the MET inference but have different fake-MET pathologies.
- A non-collider experiment. For dark matter, direct detection and indirect detection do not use MET at all.

## Has anyone looked

**Non-collision background: measured from data, with a 100% uncertainty, and that is the right answer.** ATLAS defines a region enriched in beam-induced background by inverting the tight jet-quality cut on the leading jet and uses the fraction of events with leading-jet timing |t_j| > 5 ns. The result is "almost negligible contribution from non-collision backgrounds in the signal regions," with predicted yields of **360 ± 360 for the loosest region, 51 ± 51, 4 ± 4, and zero for the tightest two** (44) [A]. Assigning 100% uncertainty to a data-driven estimate of a background with no good model is honest practice, and it closes failure mode (d) at the stated level.

**The soft-term scale and resolution: measured, with the uncertainty set by the worst data-MC disagreement.** ATLAS computes the soft-term uncertainties from the maximal data-MC difference — for example, the parallel scale uncertainty in the 30–35 GeV bin is 0.47 GeV — and reports them reduced by up to 76% (scale) and 51% (resolution) relative to the earlier lower-luminosity calculation. Tighter working points improve resolution at high pile-up by up to 39%. Data and simulation agree within uncertainties for the overall distribution and the hard term; the soft term shows a slight data excess in the tails, with Powheg+Pythia modelling it worse than Sherpa (43) [A]. Setting the uncertainty to the maximal disagreement rather than the average is the conservative choice.

**The low-MET bias: named explicitly by ATLAS** (43) [A]. Not hidden.

**The control-region design: deliberately constructed to mimic the signal.** The Z→μμ control region is used **"because the muons are not added back into E_T^miss, so it mimics the invisible neutrinos"** (44) [A]. This is the loop-breaking move done correctly: a sample in which the instrumental response to a genuine momentum imbalance can be measured, because the imbalance was manufactured by the analyst removing known objects. The answer is fixed independently of the model.

**The systematic budget is dominated by object calibration, not by MET-specific effects.** For the monojet search: jet and MET energy scale and resolution 0.5% (loosest) to 5.3% (tightest); lepton efficiencies and scales 0.2–2.3%; jet quality, pile-up and corrections 0.9–1.8%; soft MET contributions 0.4–1.7%; W/Z+jets theory 0.4–2%; total Standard Model uncertainty 2.4% to 9.7% (44) [A].

**Independent signatures: yes, routinely.** Mono-photon, mono-Z and VBF+MET channels are standard and published. Direct and indirect dark matter detection are entirely independent of MET; the archive's own `07_epistemic_audit/known_versus_assumed_v1.md` records LZ at 4.2 tonne-years among the null results.

**What has not been looked at.** Two items:

First, **no published study was located that tests the uncorrelated-object-uncertainty assumption** by deriving a correlation matrix between jet and soft-term mismeasurement and propagating it. ATLAS states the assumption; nothing was found that tests it. [A on the absence; falsified by production of such a study.] Unlike the inter-experiment correlation case in section 2, there is no published sensitivity scan here.

Second, and more consequential: **the fake-MET tail is characterised in Z→ℓℓ and validated against W→ℓν and tt̄, all of which are Standard Model topologies with modest jet activity. No published study was located that characterises the fake-MET tail in a high-jet-multiplicity, high-MET topology using data alone, independent of simulation.** [A on the absence.] In the regime where the search has its sensitivity, the dominant background is simulated and normalised by extrapolation from a different topology (44) [A], and the fake component is constrained by extrapolation from a topology with no signal. Both extrapolations are reasonable; neither has an independent check in the regime that matters.

## Verdict on Proof 5

**Mid-ranked, with one genuine unexamined item.** The instrumental side is handled better than a critic would expect: non-collision background measured from data with 100% uncertainty, soft-term uncertainties set by the worst disagreement, low-MET bias declared, and a control region built specifically to manufacture a known momentum imbalance.

The exposure is the extrapolation stack in the signal regime — a simulated irreducible background normalised by a factor of 1.27 fitted in a different topology, plus a fake-MET estimate extrapolated from a signal-free topology, with no independent data-only characterisation of the fake tail where the sensitivity lives. The absence as presence is, structurally, the most model-dependent of the eight inferences audited here.

# Proof 6 — Ion-Beam Analysis, and How Far the Calibration Regress Goes

## The claim

Rutherford backscattering spectrometry and particle-induced X-ray emission measure the elemental composition and areal density of a sample from first principles. The Rutherford cross-section is calculable analytically from the Coulomb potential, predicted in 1911, before any of the instruments existed. Accuracy at the **1% level** is claimed for areal density, and RBS has been put forward as a **primary direct reference method** for quantity of material.

This is the proof where the regress question bites hardest, because the certified reference materials that calibrate ion-beam analysis were themselves characterised by other techniques — and the brief asks how far the regress goes, where it is anchored, and whether any genuinely theory-independent anchor exists. The answer is more specific and more interesting than either a sceptic or an advocate would predict.

## What it rests on

The published uncertainty budget resolves this precisely. For a 1.5 MeV He RBS measurement of an Sb implant in silicon, three laboratories (Surrey, Lisbon, Budapest) reported combined standard uncertainties of 0.92%, 1.34% and 1.01%, with a grand-average fluence of 4.588 TFU and a coefficient of variation of 0.37% (45) [A]. The budget:

| Term | Contribution | Origin |
|---|---|---|
| Electronic stopping power (Si, 1.5 MeV He) | **0.80%** — dominant | semi-empirical database, pinned to CRM |
| Energy calibration | 0.20% (Surrey, Lisbon), 0.13% (Budapest) | resonance measurement |
| Code uncertainty | 0.21% | software implementation |
| Rutherford / screened cross-section | **0.10%** | calculable from first principles |
| Electronics gain | 0.07–0.11% | calibration samples |
| Scattering angle | dominant for near-150° detectors | laser/goniometer measurement |
| Pile-up correction | up to 17% correction (Lisbon, no rejector) | model |
| Charge × solid angle (QΩ) | absorbed, not separately determined | in-situ via Si internal standard |

(45) [A].

Read the first and fourth rows together. **The term that is calculable from first principles contributes 0.10%. The term that requires empirical input contributes 0.80%, eight times as much.** The theoretically pristine part of the measurement is not the part that limits it.

Two further facts complete the picture of what the method actually requires:

- **QΩ, the product of beam charge and detector solid angle, is "notoriously difficult to determine" at high accuracy, so RBS quantification is usually done relative to a standard** (45) [A]. Budapest's nominal charge agreed with the spectrum-derived QΩ to 0.7%; Surrey and Lisbon normalise to the amorphous-silicon signal (45) [A].
- Beam energy was checked against the ¹⁶O(α,α) resonance at 3038 keV; detector gain and pulse-height defect were calibrated with multi-element samples, with dead layers measured using an Am-241 source; the scattering angle was measured with a laser and goniometer (45) [A].

## The regress, traced step by step

This is the section's main contribution, and it is built entirely from the published traceability statement.

**Step 1.** The RBS fluence result (≈1%) is traceable **to an Sb-implanted certified reference material through the silicon electronic stopping power**, which carries 0.8% (45) [A].

**Step 2.** The Sb CRM is certified at 0.6% (1σ) (45) [A].

**Step 3.** The Sb CRM's fluence **was certified using ICP-MS and other methods** (45) [A]. Inductively coupled plasma mass spectrometry rests on different physics from ion backscattering: ion mass-to-charge separation in a mass spectrometer, not elastic Coulomb scattering kinematics.

**Step 4.** ICP-MS is not itself primary. Its quantification runs through calibration solutions, which are described in the metrology literature as "a (usually gravimetric) mixture of two primary transfer standards," and the practical quantity is mass fraction (kg/kg) chosen partly for "practical access to mass using a balance" (48) [A].

**Step 5.** The primary transfer standards are high-purity metals certified either by the primary difference method — subtracting summed impurity mass fractions from ideal purity — or by classical primary methods such as gravimetry, titrimetry and coulometry. The PDM can reach relative uncertainty below 10⁻⁴ (48) [A].

**Step 6.** The chain terminates, in the metrology literature's own words, at **"the abstract definition of the SI unit (with uncertainty zero)"** (48) [A].

## Where it bottoms out, and whether the anchor is theory-independent

**The regress has a bottom, and it is four links down: weighing.** The chain runs RBS → Sb implant CRM → ICP-MS → gravimetric calibration solution → high-purity metal certified by mass → the SI definition. At no point does the chain return to ion-beam physics or to the Rutherford cross-section. That is a genuine external anchor and it answers the central worry directly: **the calibration standards for ion-beam analysis were not characterised by techniques resting on the same atomic physics. They were characterised by mass spectrometry calibrated against weighed quantities of pure metal.** [A]

Is the anchor theory-independent? Not completely, and the honest answer has three parts.

**It is independent of the theory under test.** The Rutherford scattering cross-section, electronic stopping powers, screening corrections and ion kinematics play no role in weighing a metal or in gravimetric dilution. Whatever is wrong with ion-beam physics cannot propagate into the balance. This is the asymmetry Ackermann identified against Pickering: the apparatus is less plastic than the theory (5) [A].

**It is not independent of all theory.** Comparing masses on a balance involves a theory of the balance; the kilogram since 2019 is defined via the Planck constant; and the step from mass to amount of substance requires molar masses, which the metrology literature flags as a "very often negligible uncertainty" — an assumption, as it says (48) [A]. Purity assessment by the primary difference method requires measuring impurities, and those measurements use ICP-MS, glow discharge mass spectrometry, hot extraction and nuclear methods, each with its own theory; below-quantitation impurities are handled by estimates such as w_LOQ/2 ± w_LOQ/2 (48) [A].

**And the metrology literature names the correlated-anchor failure mode itself.** It states that PDM impurity quantification relies on calibrants "not necessarily fully SI traceable themselves"; that in an EDTA titration the titrant is calibrated against a Zn standard which must itself be characterised by PDM, so the result "cannot have a smaller uncertainty than the (Zn⁰) standard"; and — the sentence that matters most in this entire section — it warns of undetected correlations such as national metrology institutes all using **"the same wrongly certified starting material"** (48) [A].

That is the chemical-metrology community stating, in its own strategy literature, the precise failure mode this document is built to map. The regress bottoms out, but the bottom is a small number of shared physical artefacts, and the people who maintain them know it.

## How it could fail

**(a) A wrong stopping power compensated by a fitted standard.** This is the specific, live exposure. Stopping power is the dominant uncertainty at 0.8%, it is semi-empirical, and in this protocol it is **pinned to the CRM** (45) [A]. If the tabulated electronic stopping power for He in Si is biased, and the protocol determines it by requiring the CRM to come out right, the bias is absorbed. Every subsequent measurement on a similar sample then returns the correct areal density, because the error was calibrated away — and would return a biased answer for any sample where the stopping power's energy or composition dependence differs. The IAEA intercomparison states the magnitude of the exposure plainly: **He stopping in Si is currently uncertain at about 2%** (46) [A].

**(b) Code agreement mistaken for physical verification.** The failure mode is documented quantitatively. In the IAEA intercomparison of seven IBA packages (DEPTH, GISA, DataFurnace/NDF, RBX, RUMP, SIMNRA and the Monte Carlo code MCERD), **the total oxygen amounts in a hafnium oxide sample scattered 5.3% across codes but only 0.8% among the three codes using the same cross sections** (46) [A]. Agreement between codes is substantially agreement about shared databases. The authors identify stopping power databases as "the largest source of differences," with examples including GISA's SRIM91 against SRIM03 in the others (46) [A].

**(c) Mutual calibration mistaken for traceability in the thin-film regime.** Also documented, and this is the sharpest instance of the regress in a metrology document. In CCQM-P190, measuring HfO₂ films of 1.24 to 2.57 nm, **the reference thicknesses were set by mutual calibration** — MEIS intensity ratios supplied the zero-offset data and averaged XRR thicknesses from PTB, NMIJ and NIST (KRISS excluded) supplied the length-unit data (47) [A]. The spread among participating techniques was large: TEM slopes ranged 0.742 to 1.308, about 22% relative standard deviation, with a mean offset of 0.418 nm; spectroscopic ellipsometry offsets ranged 0.568 to 1.085 nm, which the report calls "largely different"; XPS slopes before re-analysis ranged 1.045 to 1.198; and the report concludes that XPS has "some problem as a zero offset method" and that TEM is "difficult to be used as a length unit traceable method" (47) [A]. The techniques were **not mutually consistent**, and the reference value against which each was assessed was constructed from a subset of them. That is Collins's regress, in a BIPM key-comparison report, closed by selecting which participants define the answer (3, 5) [A].

**(d) Pile-up and multiple scattering mismodelling.** Lisbon required a pile-up correction of up to 17% for want of a hardware rejector (45) [A]; the IAEA exercise found pile-up effects of −0.3% and −0.8% at two detectors, double scattering adding roughly +0.25–0.28%, and that for heavy-ion ERDA with multiple scattering the single-scattering codes disagreed with the Monte Carlo code, a regime the authors state is "not yet well understood" (46) [A].

**(e) PIXE's fundamental-parameter dependence.** PIXE quantification requires ionisation cross sections, fluorescence yields, attenuation coefficients and stopping powers — a larger set of tabulated inputs than RBS, with correspondingly more room for a compensating error. In practice PIXE yields are frequently calibrated using thin-film standards rather than computed from fundamental parameters, which converts the problem into the same stopping-power-pinned-to-standard structure as (a) [C — inference from the structure of the technique and the existence of a calibration literature; falsified by a demonstration that standardless PIXE reaches comparable accuracy from fundamental parameters alone].

## What would detect it

- A blind measurement of a sample whose composition was fixed by gravimetry or ICP-MS *before* the ion-beam measurement, with the ion-beam result compared afterwards.
- Measurement of the same sample at several beam energies, which varies the stopping power's contribution while leaving the true areal density fixed — the cleanest internal discriminator against (a).
- Direct measurement of electronic stopping power by a route not involving a CRM-pinned fit.
- Comparison across techniques with genuinely independent traceability chains, with the reference value fixed outside the participant set.
- Code intercomparison in which the databases are deliberately varied rather than shared.

## Has anyone looked

**The blind test exists, and it passed.** This is the best single piece of loop-breaking evidence in the document. In the IAEA intercomparison, the codes analysed a **certified** Sb implant whose fluence had been fixed independently at 0.6%. Using SRIM03 stopping, the codes' fluence values had a standard deviation of 0.11% and the average sat at **−0.18 ± 0.11% from the certified value** (46) [A]. The analysis software, resting on Rutherford kinematics and tabulated stopping powers, hit a number that had been fixed beforehand by a mass-spectrometric chain anchored in weighing. The authors draw the right conclusion: the Sb result shows SRIM03 Si stopping is consistent with the 0.6% certified value (46) [A].

That is contact with something the software did not create. It is precisely the second of the four loop-breaking tests set out in `07_epistemic_audit/closed_loop_v1.md`, and it is satisfied with numbers. **The closed-loop hypothesis fails for low-energy RBS areal-density measurement on implanted standards.** [A]

**Code intercomparison: done thoroughly, with the shared-database limitation identified by the authors themselves.** Seven codes, 28 simulation calculations and four experimental analyses. Agreement on identical input was 0.12–0.26% standard deviation on yields and peak heights for ⁴He RBS, with edge positions within 0.1–0.7 keV; 0.2–0.7% for ⁷Li RBS; 0.5–1.3% across all codes for ⁴He ERDA, tightening to 0.03–0.21% for the three main codes. Demonstrable calculation accuracy "can reach the 0.1% level" in most cases, the exception being non-Rutherford resonances. The authors say independent implementations giving similar results is "very strong evidence for the reliability of the codes as a whole" — and in the same paper report the 5.3%-versus-0.8% hafnium oxide result that bounds how much of that reliability is physical rather than shared-database (46) [A]. They did not rank the codes (46) [A].

**Cross-technique comparison: done, and the finding is negative in the thin-film regime.** CCQM-P190 compared XPS (8 labs), XRR (4), TEM (4), spectroscopic ellipsometry (3), XRR+XRF (PTB) and RBS (Surrey), with MEIS as the zero-offset method (47) [A]. Its conclusions: the techniques are not yet mutually consistent; XRR is the best-supported length-unit traceable anchor, slope near 1.005; **RBS provides absolute quantity-of-material traceability**, slope 0.9906 ± 0.0111 with offset fixed at zero and a combined standard uncertainty of 6.3%; and combining RBS quantity-of-material with XRR thickness gives an HfO₂ density of about 8.23 g/cm³, well below bulk (47) [A]. The last item is a genuine physical result that neither technique could produce alone, obtained because their traceability chains are different.

**Multi-energy consistency: no published systematic study was located.** The measurement that would most directly discriminate a stopping-power bias from a true areal density — repeating on the same sample across a range of beam energies and testing whether the inferred fluence is energy-independent — was not found as a dedicated published check for the 1%-accuracy protocol. [A on the absence; falsified by production of such a study.] Given that stopping power is the dominant uncertainty, is energy-dependent, and is pinned to a standard, **this is the most valuable unexamined check identified anywhere in this document.** It is cheap, it requires no new apparatus, and it would convert the largest term in the budget from an assumption into a measurement.

**Direct stopping-power determination independent of CRM pinning: partially available but not used in this protocol.** The protocol explicitly pins stopping to the CRM (45) [A]. Independent stopping-power measurements exist in the literature, and the 2% figure for He in Si (46) [A] reflects their spread rather than their absence; what is missing is a demonstration that the 1% protocol holds when stopping is taken from an independent determination instead of being fitted.

## Verdict on Proof 6

**The regress genuinely bottoms out, and it bottoms out outside ion-beam physics — in mass spectrometry calibrated against weighed high-purity metal, terminating at the SI definitions.** That is the clearest answer this audit produced to the archive's founding question, and it is favourable to the field.

But the anchor is reached through a chain whose dominant link is a semi-empirical stopping power fitted to the standard, and the field's own documents establish three things that qualify the picture: code agreement is substantially database agreement (5.3% versus 0.8%); in the nm-film regime the reference value is set by mutual calibration between non-consistent techniques; and chemical metrology warns in its own strategy document about institutes sharing "the same wrongly certified starting material."

The blind Sb-implant result at −0.18 ± 0.11% against a 0.6% certified value is real external contact. The unexamined multi-energy check would be worth more than anything else on this list.

# Proof 7 — "The Technology Works, Therefore the Theory Is Right"

## The claim

Ion implantation manufactures every semiconductor device in use. Proton therapy deposits dose in tumours and spares tissue beyond. If the physics of ion-matter interaction were invented, these would not work. Therefore the physics is right.

This is the argument most often deployed to close discussion, and it is the one that requires the most care, because it is partly sound and the sound part is narrower than its usual use.

## What it rests on

1. **A functional success criterion.** The device works; the tumour responds; the patient survives.
2. **An inference from success to truth** — in philosophy of science, the no-miracles argument, attributed to Putnam: our best theories are extraordinarily successful, and the best explanation of that success is that they are true or approximately true, since otherwise the success would be miraculous (7) [A].
3. **A manipulation argument.** Hacking's entity realism ties belief in an entity to the ability to manipulate it causally (7) [A].
4. **The tacit premise that the technology could have failed** had the theory been wrong — that the success was a risked prediction rather than an engineered outcome.

Premise 4 is where the argument is weakest, and the weakness is documentable with numbers rather than philosophy.

## How it could fail

**(a) Co-design: the technology was tuned until it worked, so its working is not a test.** The theory supplied an approximate model; the engineering added empirical corrections, calibration tables and safety margins until the output matched the requirement. The system then works, and it works whether or not the underlying model is correct in the places the margins cover. This is Hacking's "self-vindication" applied to industry: ideas, things and marks brought into mutual consistency (5) [A].

The evidence for this mechanism in proton therapy is explicit and quantitative.

- **The clinically used range uncertainty from CT-number-to-stopping-power conversion is "generally taken as 3.5%"** (49) [A]. A 3.5% range margin on a 20 cm depth is 7 mm. Any theoretical error smaller than that is invisible to clinical outcome.
- The intrinsic physics contribution is handled by assumption, not measurement: for 230 MeV protons the peak spread is about 0.7 g/cm² **assuming a 10% I-value uncertainty** (49) [A].
- The mean excitation energy of water, the single parameter governing proton stopping, has **literature values ranging from about 61 eV to more than 80 eV**, with ICRU 49 recommending 75 eV (50) [A]. That is a ±13% spread on the parameter the whole dose calculation turns on.
- Stopping power compilations — ICRU 49, Ziegler 1977, 1985, 2000 — are all fits to experimental data, and the lack of consensus in deriving them is itself a source of what the authors call epistemic uncertainty, "uncertainties due to lack of knowledge" in the physics modelling (50) [A].
- And the decisive sentence: **"this adjustment hides any shifts in the Bragg peak location"** — the routine clinical calibration absorbs the theoretical disagreement (50) [A].
- Palta's assessment of the empirical margin-and-smearing approaches used clinically: they are "questionable," and **"No real data exist to support any of these approaches"** (49) [A]. His summary of proton plan evaluation: "What you see is not what you always get" (49) [A].

The same structure appears in ion implantation. SRIM, the standard range-and-stopping code, is a semi-empirical fit, and a published study of electronic-stopping deficiencies in SRIM for high-energy nickel implantation into nickel and iron exists in the materials literature; the IAEA work independently establishes that He stopping in Si carries about 2% uncertainty (46) [A]. Meanwhile implant doses in production are controlled by dosimetry — measured charge — and by downstream electrical test, not by predicted range profiles. The functional criterion is "does the transistor have the specified threshold voltage," and the process recipe is tuned empirically until it does.

**(b) Underdetermination of the theory by the technology.** The technology constrains only the parts of the theory it exercises. Ion implantation exercises ion kinematics, electronic and nuclear stopping, and channelling at keV-to-MeV energies. It says nothing whatever about quark substructure, the Higgs mechanism, supersymmetry, or TeV-scale physics. **An argument from the working of a chip to the correctness of the Standard Model's electroweak sector is a non-sequitur**, and it is made constantly [C — follows from the energy and process range the technologies exercise; falsified by identifying a deployed technology whose function depends on a TeV-scale prediction].

**(c) The base-rate fallacy.** This is the formal defect in the no-miracles argument and it is established in the philosophy literature. Howson, Lipton, and Magnus and Callender argue that the argument commits the base-rate fallacy: their illustration is a disease test with no false negatives and a 10% false-positive rate, where a positive result does not imply a 90% chance of disease because the result also depends on the base rate. Likewise, **a theory's success does not show it is approximately true without knowing the base rate of approximately true theories** (7) [A]. Worrall and Menke contest this framing and Sober raises a separate likelihood objection (7) [B].

**(d) The historical record.** Laudan's "A Confutation of Convergent Realism" (1981) argues that the history of science contains many empirically successful theories later rejected, whose unobservable terms did not refer (7) [A]. Realist replies restrict the inductive base to mature, non-ad-hoc theories, or point to continuity in the components that did the explanatory work (7) [B].

**(e) Entity realism does not carry theories.** Hacking's manipulation argument licenses belief in the *entity*, not in the theories describing it (7) [A]. And Morrison and Resnik argue that believing in entities while withholding belief in the theories that describe them may not even be coherent (7) [B]. The Stanford Encyclopedia's summary is the precise statement of the limit: **success supports reference only through causal knowledge of specific entities, not through success in general** (7) [A].

## Where the argument is strong

It must be said clearly, because the preceding list reads one-sidedly and the argument does real work.

**It is strong where the technology makes a quantitative prediction that was risked in advance, at a precision the margins do not cover.** Three cases qualify:

1. **The Rutherford cross-section.** Two-body Coulomb scattering kinematics were predicted in 1911, before any accelerator existed, and they are used today with a 0.10% uncertainty contribution in a 1% measurement (45) [A]. Nothing about the technology was adjusted to make the 1911 formula come out right; the formula had no free parameters to adjust. The archive's own closed-loop file identifies this as the first loop-breaking test, and it is satisfied.
2. **The Bragg peak's existence and approximate position.** That a heavy charged particle deposits most of its energy at the end of its track, at a depth set by its energy, is the entire clinical rationale for proton therapy and is a prediction of the Bethe stopping theory. The 3.5% margin covers the *fine* position; it does not cover the existence of the peak or its gross depth-energy relation. A theory that got that wrong would produce no clinical benefit at all.
3. **Hacking's manipulation criterion, properly scoped.** Steering a beam of individual ions into a target and recovering the predicted mass-dependent recoil spectrum is causal manipulation of the entity. On the Stanford Encyclopedia's reading this licenses belief in the entity via causal knowledge of it (7) [A]. It does not license the Standard Model.

**And where the technology makes a risked quantitative prediction, the margins must be checked against the claim's precision.** This is the general rule the section yields: a functional success criterion establishes that the theory is correct to within the engineering margin, in the regime the technology exercises, for the quantities the technology's output is sensitive to. Outside those three qualifiers it establishes nothing.

Applied: proton therapy establishes proton stopping theory to roughly 3.5% in water-like tissue at therapeutic energies. It does not establish it to 0.5%. Ion implantation establishes keV-MeV ion-solid interaction to the tolerance of the device recipe. Neither establishes anything about particle physics above a few MeV.

## What would detect the failure

- Tighten the margin and see whether the technology still works. If range margins were cut from 3.5% to 1%, a theoretical bias in the stopping-power model would produce clinical failures. This is an available experiment that the clinical ethics of the field correctly forbid in that form — but range verification by prompt gamma imaging or proton radiography performs it diagnostically.
- Identify a technology whose function is sensitive to the theory at the precision in dispute.
- Blind prediction of a device characteristic from theory alone, with no recipe tuning, and comparison with the manufactured result.
- Comparison of SRIM-predicted implant profiles with measured profiles from SIMS and RBS across a wide range of ions and energies, which has been done in the materials literature (51) [A].

## Has anyone looked

**Yes, and the looking is largely inside medical physics, which has been more candid about this than particle physics has.** The explicit separation of epistemic uncertainty — "uncertainties due to lack of knowledge" in physics modelling — from statistical and systematic uncertainty, and the explicit demonstration that routine calibration "hides any shifts in the Bragg peak location," is medical physics auditing its own theory dependence in print (50) [A]. The authors treat the epistemic uncertainties as reducible and argue that quantitative evaluation "provides insight for the design of experiments suitable to reduce, or cancel their effects" (50) [A]. Palta's "No real data exist to support any of these approaches" about the clinical margin methods is a practitioner saying the margins are conventional (49) [A].

**SRIM has been validated against SIMS and RBS depth profiles**, and deficiencies in its electronic stopping have been published for specific ion-target combinations (51) [A].

**What has not been looked at:** no study was located that attempts the inverse audit — taking a deployed technology and asking, quantitatively, what range of theoretical parameter values would still yield a functioning device or an acceptable clinical outcome. That number is the actual evidential content of "the technology works," and as far as this search could determine **nobody has computed it for any particle-physics-adjacent technology.** [A on the absence; falsified by production of such a study.] The I-value case is the one place where the ingredients exist: the parameter spread is known (61 to >80 eV) (50) and the clinical margin is known (3.5%) (49), so the calculation is tractable and has not been published as such.

## Verdict on Proof 7

**This is the weakest of the eight as usually stated, and the weakness is structural rather than evidential.** The technologies work, nobody disputes it, and they do establish the physics they exercise to the precision their margins expose. But the margins are large, the stopping-power parameter they depend on has a ±13% literature spread, the clinical calibration explicitly absorbs theoretical disagreement, the field says in print that no data support the margin conventions, and the inference from technological success to theoretical truth is a known formal fallacy without a base rate.

The 1911 Rutherford cross-section is the genuine exception: a parameter-free prediction, made before the apparatus existed, used today at 0.10% in a 1% measurement. That is as clean a loop-break as the archive has found.

# Proof 8 — Prediction Failures as Loop-Breakers

## The claim

A closed confirmatory loop could not generate unwanted surprises. If the apparatus, software and theory merely handed the theory back to itself, the field would never produce results it did not want. It produces them constantly. Therefore the loop is open.

This is the strongest single argument against the closed-loop hypothesis, and it deserves to be tested rather than asserted. Four cases.

## Case A — OPERA's superluminal neutrinos: the argument at its strongest

**What happened.** OPERA's preliminary March 2011 analysis found neutrinos arriving about 60.7 ns earlier than light; the result was announced in September 2011 after six months of cross-checks, at six-sigma significance; the November refined analysis gave 57.8 ns, a relative speed difference of about one part in 42,000, at **6.2σ**, with a repeat run giving 62.1 ns (56) [A].

**The two errors.** A loose fibre-optic link from the GPS receiver to the master clock added delay, shortening the apparent flight time by 73 ns; and an oscillator clock ran faster than its specified 10 MHz, lengthening the apparent flight time and partly offsetting the first (56) [A]. Both were instrumental, both were outside specification, and together they produced a stable, reproducible, 6σ result.

**How it ended.** ICARUS measured seven neutrinos from the same beam at light speed. LVD found a timing shift for 2008–2011 that agreed with the OPERA anomaly, and LVD photographs later showed the fibre cable loose by 13 October 2011. In June 2012 CERN announced that OPERA, ICARUS, LVD and BOREXINO all measured speeds consistent with light, with MINOS reporting similar preliminary results the same day. OPERA's final July 2012 result was 6.5 ± 15 ns, consistent with zero (56) [A].

**Why this is the strongest case.** The apparatus produced a 6σ result that contradicted special relativity. The collaboration published it rather than suppressing it. It was corrected within nine months by independent detectors on the same beam, and the mechanism of the error was physically identified down to a photographed loose connector. Every element Franklin's account requires is present: independent confirmation attempts, identification of the specific error source, and a known-value check (4) [A]. **A closed loop could not have done this** [C — inference from the sequence; falsified only by showing the correction was itself an artefact].

## Case B — The 750 GeV diphoton bump: the look-elsewhere limit, quantified

**What happened.** Local significances of 3.9σ at ATLAS (p ≈ 0.00005) and 3.4σ at CMS (p ≈ 0.0003). **After look-elsewhere correction the global significances fell to 2.1σ (p = 0.0179) and 1.6σ (p = 0.0548)** (22) [A]. About 500 arXiv papers appeared in the following months (22) [A]. The excess faded with more data.

**What it shows, both ways.** Hooper's analysis is precise: combining the two as if ATLAS confirmed CMS gives about 5 × 10⁻⁶, roughly 4.6σ, "only slightly below" 5σ; assuming a trials factor of about 10⁴ raises the odds of such a fluctuation to roughly 5%, which he calls "a bit unlikely" but "far from implausible"; and "Even the most enthusiastic proponents of this excess treated this likelihood to be on par with that of a coin toss" (22) [A].

So the loop-breaking reading — the field reported an excess it could not explain and then retracted it — is correct and is evidence of openness. But the case simultaneously establishes the **limit** on how much weight the loop-breaking argument can bear: the apparatus *did* produce a wrong answer at nearly 5σ local significance, 500 theory papers were written on it, and what corrected it was simply more data. If the excess had been at a mass where more data was not forthcoming, nothing in the system would have resolved it. **The correction mechanism is luminosity, not logic.** [C — inference from the case; falsified by identifying a non-statistical mechanism that resolved it.]

## Case C — The CDF-II W mass: an unresolved disagreement, four years on

**What happened.** The 2022 CDF-II measurement sits **seven standard deviations above the Standard Model prediction**, with a stated precision of 9.4 MeV. All other measurements are statistically compatible with the Standard Model. The most recent CMS measurement is compatible with the Standard Model, slightly higher, and almost matched CDF's precision (55) [A].

**Status.** Not resolved. CDF is maintaining its result. A new analysis by Kotwal studies possible geometrical defects in the drift chamber that could bias measured lepton momenta, and a separate analysis using cosmic-ray muons verifies the claimed 25 ppm momentum resolution by constraining possible biases. The 2022 measurement used only the drift chamber, discarding silicon vertex detector information as offering only marginal gains. Spokesperson David Toback says the paper lays out the tracking "warts and all" and argues the result should be taken seriously despite disagreeing with both the Standard Model and the silicon-tracker-based LHC measurements (55) [A].

**Why this case cuts both ways.** For the loop-breaking argument: a collaboration is publicly standing behind a 7σ disagreement with the Standard Model, four years on, against the rest of the field. That is not a closed loop. Against the argument: the disagreement persists without resolution, and the suspected cause is detector-specific — drift chamber geometry — which means the field's response has been to look for an instrumental error in the outlier rather than to revise anything. That is the *correct* response if the outlier is wrong. It is indistinguishable, from outside, from the response if the outlier is right. **This is Collins's regress in a live case: the question of whether CDF's chamber worked properly and the question of what the W mass is cannot be separated** (3, 5) [B — named advocates on both sides, CDF versus the LHC measurements].

## Case D — The muon g−2: the hardest case, and the one that limits the argument most

**What happened on the experimental side.** Fermilab's final result, to 127 ppb: a_μ = 116 592 070.5 ± 11.4 (stat) ± 9.1 (syst) ± 2.1 (ext) × 10⁻¹¹, fully consistent with Brookhaven, giving a world average of 116 592 0715(145) × 10⁻¹² at 124 ppb (52, 54) [A].

**What happened on the theory side, and this is the crux.** The 2025 Theory Initiative white paper gives a_μ = (116 592 033 ± 62) × 10⁻¹¹, uncertainty 530 ppb (54) [A]. The measurement agrees closely with it. But:

- **WP25 is statistically incompatible with WP20 at about three standard deviations** (54) [A].
- The change is entirely methodological. WP20 computed hadronic vacuum polarisation by a data-driven method based on electron-positron cross-section measurements. **WP25 uses lattice QCD** (54) [A].
- **The data-driven HVP value has not yet been updated, so it is unknown whether it will agree with the lattice result** (54) [A].
- CERN Courier's assessment: the anomaly is **"severely undermined, but not yet definitively resolved"** (54) [A]. Aida El-Khadra: "There still are puzzles to resolve, particularly around the experimental measurements" — referring to the data-driven method, not the lattice (54) [A].

**Why this is the hardest case for the loop-breaking argument.** For roughly fifteen years the muon g−2 anomaly was the field's leading hint of physics beyond the Standard Model, at 3.5σ and later more. It was removed not by a new measurement of the muon but by **replacing a theory input with a different theory input**, where the two inputs disagree at about 3σ and the disagreement is unresolved. The experimental number did not move; the prediction moved to meet it.

That is, structurally, precisely the pattern the closed-loop hypothesis predicts: an anomaly resolved by adjusting the theoretical input through which data is interpreted.

**And the rigorous counter, which must be given equal weight.** Three things make this not a simple accommodation:

1. The lattice HVP calculation is an ab-initio computation from the QCD action, not a fit to the discrepancy. It was not tuned to produce agreement.
2. The lattice result predicted a higher HVP — and therefore a smaller anomaly — **before** the final Fermilab measurement confirmed the experimental value at 127 ppb. The lattice took a position that could have been falsified.
3. The e⁺e⁻ data the lattice now disagrees with is itself experimental data. So the field does not have a theory moving to meet an experiment; it has **two experimental routes to the same quantity disagreeing with each other**, with one of them (lattice, computed from first principles) agreeing with the muon measurement. That is a problem in hadronic cross-section measurement, not a case of theory accommodation. [A on items 1–3 from (53, 54); B on which route is right, with named advocates]

**What remains, after that counter.** Even granting all three points, the case establishes a limit on the loop-breaking argument: **the magnitude of a claimed anomaly in this field can change by 3σ through a change in theoretical method, with no new data about the particle in question.** Any argument that reads a surprise as proof of openness must be able to say what would have happened had the lattice and the data-driven methods agreed on the WP20 value. Nobody knows.

## Testing the argument itself

**Where the loop-breaking argument is strong.**

It is strong where a surprise was (i) produced by the apparatus, (ii) published against the field's expectation, (iii) corrected by an independent apparatus or an identified physical mechanism, and (iv) correctable in a bounded time. OPERA satisfies all four completely. That single case is sufficient to refute the strong form of the closed-loop hypothesis — a system that could only hand the theory back to itself could not have produced a published, reproducible, 6σ violation of special relativity and then located the loose cable. [A]

It is further strengthened by two structural facts documented elsewhere in this audit: blinding is in routine use, with independent-team requirements and sign-off before unblinding (30) [A]; and the five-loop QED error was found by exactly the kind of outside recalculation that a closed loop would not accommodate (13, 14) [A].

**Where the argument's limits are.**

1. **It is an existence proof, not a rate.** Four surprises do not establish that surprises occur whenever they should. Klein and Roodman's PDG clustering result — χ² of 131.2 for 83 d.o.f. around prior published averages against 249.7 around final values (10) [A] — is direct evidence that measurements are pulled toward expectation in the aggregate, and the authors' own conclusion that the size of experimenter bias "cannot be estimated" (10) [A] means the rate cannot be computed. The loop can be open and leaky at the same time.
2. **The correction mechanism in three of four cases was more data or more computing, not an independent principle.** 750 GeV faded with luminosity; the five-loop error was found by brute recalculation; the muon anomaly shifted with lattice compute. Only OPERA was corrected by an independent apparatus.
3. **It says nothing about what the trigger discarded.** Every surprise above was a surprise in recorded data. The trigger-level literature establishes that standard LHC triggers "often result in low trigger efficiency for unconventional BSM signatures" because they are "primarily designed to target prompt decays of heavy particles"; that displaced decay products "can be misidentified as pile-up or fail standard quality criteria"; that long-lived particles can produce signals resembling noise; that models with many low-energy charged particles "can be difficult to differentiate from pile-up"; with quantified losses — above 2 GeV thresholds the two-track Higgs-portal efficiency falls "below 20%" for all scalar masses, SUEP efficiency is negligible, barrel-only tracking cuts stau acceptance "by approximately 50% or more," and HSCP efficiency drops from ~90% to ~30% (57) [A]. The authors' own counter is worth quoting because it is correct: "Triggering on 20% of events is infinitely better than triggering on none" (57) [A]. But the structural asymmetry recorded as claim C2a in this archive's register stands: false positives cost measured bandwidth, while false negatives cost unrecoverable events and are never integrated over signature space.
4. **A case where the anomaly persists and is unresolved is not evidence either way.** CDF-II has been open for four years.

**Net assessment.** The strong closed-loop hypothesis is refuted, primarily by OPERA and secondarily by the Volkov episode. The weak form — that the system is biased toward expectation at a rate nobody can quantify, and is structurally blind to signatures the trigger was not designed for — survives all four cases and is independently supported by the PDG clustering data and the trigger-efficiency literature. [A on the refutation of the strong form; A on the survival of the weak form, from (10) and (57)]

# Summary Table

| Proof | Strength of anchoring | Most serious unexamined failure mode |
|---|---|---|
| 1. Electron g−2 | Strong on measurement precision; **the test itself is α-limited and the field says so** | No independent work on the cyclotron lineshape mismatch, the dominant systematic; n=1 group, n=2 calculations |
| 2. Higgs discovery | **Strongest of the eight** — spurious-signal criterion, blinding, independent teams, spin-parity exclusions, published correlation scans | No correlation-sensitivity scan for the 2012 discovery significance itself |
| 3. Lattice QCD | Strong as a test of QCD's internal sufficiency; cannot discriminate QCD from alternatives by construction | Rooting locality unproven; a²-linearity justified internally; 432-procedure ensemble unaudited externally |
| 4. Jets→partons | **Strong, via inclusive DIS and neutrino data, not via jets** | Flavour-dependent JES keyed to a label with no hadron-level referent |
| 5. Missing transverse energy | Instrumental side handled well; inference is the most model-dependent of the eight | No data-only characterisation of the fake-MET tail in the high-multiplicity signal regime; uncorrelated-object assumption untested |
| 6. Ion-beam analysis | **Regress genuinely bottoms out, outside ion-beam physics**; blind CRM test passed at −0.18 ± 0.11% | **No multi-energy consistency check** of the stopping power that dominates the budget and is pinned to the standard |
| 7. "Technology works" | Weakest as stated; strong only for the 1911 Rutherford cross-section and gross Bragg-peak behaviour | Nobody has computed what range of theoretical parameters would still yield a working device or acceptable clinical outcome |
| 8. Prediction failures | Refutes the strong closed-loop hypothesis (OPERA) | Establishes an existence proof, not a rate; silent on what the trigger discarded |

**The three with the most serious unexamined failure modes:** Proof 6 (the multi-energy check on a CRM-pinned stopping power — cheapest to do, largest payoff), Proof 1 (the cyclotron lineshape mismatch, unexamined by anyone outside the measuring group, and the largest systematic in the field's most precise measurement), and Proof 5 (no data-only fake-MET characterisation in the regime where searches have their sensitivity).

**The three most strongly anchored:** Proof 2, Proof 4, and Proof 6 — the last for its traceability chain, notwithstanding the unexamined check.

# Claims Examined and Not Supported

Tier D. These were considered and are rejected or withdrawn, with reasons. Nothing in this document may be read as supporting any of them.

**D1 — That the failure modes mapped above are evidence that results are fabricated. REJECTED, and this rejection is the condition of the document having any value.**

Mapping a failure mode is not evidence that the failure occurred, and conflating the two would destroy everything above. The two operations are different in kind. Establishing that a 3.5% clinical range margin could absorb a stopping-power bias is a statement about the sensitivity of a measurement. It is not a statement that the bias exists, and it supplies no evidence whatever that it does. Establishing that the Z→ℓℓ calibration sample contains no genuine missing energy is a statement about what that calibration can validate. It is not a claim that anyone misrepresented it — ATLAS says it in the paper (43).

Three specific points make the rejection firm rather than formal:

First, **in every case in this document where a failure mode was probed, it was probed by the field, usually in print, usually in the paper making the claim.** The five-loop error was found by a physicist redoing the calculation and corrected by the originating group publishing its own mistake (13, 14). The quenching error was found by lattice physicists doing the harder calculation (34). CODATA states its own expansion factor (16). FLAG states that its confidence "cannot be quantified" and "is not reflected in the quoted errors" (33). Salam says never to forget how ambiguous the jet-parton association is (37). Komiske, Metodiev and Thaler say there is no unambiguous hadron-level definition of jet flavour (38). Palta says no real data support the clinical margin conventions (49). Chemical metrology warns about institutes sharing the same wrongly certified starting material (48). This is not the documentary record of a field fabricating results. It is the record of a field auditing itself in public, imperfectly and unevenly, but in writing.

Second, **the direction of the known errors is wrong for fabrication.** The AHKN five-loop error made the Standard Model prediction *worse*, not better. The quenched spectrum was *discrepant* with experiment at up to 7σ and was published as discrepant (34). OPERA published a 6σ violation of special relativity (56). CDF-II is publicly maintaining a 7σ disagreement with the Standard Model against the rest of the field (55). Fabrication produces agreement; the record contains published disagreement.

Third, **the one documented case in this archive's framework of an apparatus adjusted until it gave the expected answer — Morpurgo's fractional-charge search — was identified, published and discounted by the community on the basis of a failed known-value check** (5). The mechanism is real, it has occurred, and it was caught.

A proof with an unexamined failure mode is a weaker proof. It is not a false proof, and it is not a dishonest one. Every "no published check exists" finding above is a research recommendation, not an accusation.

**D2 — That the Volkov–AHKN five-loop disagreement is a live 5σ crack in QED. REJECTED.** It was live from 2019 to 2024 and is now resolved, in Volkov's favour: AHKN traced the discrepancy to 98 under-sampled integrals, revised Set V downward by 0.803 (72), and the reviews report the two calculations as consistent, with A₁⁽¹⁰⁾ = 5.887(55) (14, 15). Presenting the dispute as open would be a factual error. The finding is the five-year latency and the n=2 dependence, not an ongoing disagreement.

**D3 — That the electron g−2 discrepancy with the caesium α value (−3.8σ) is evidence of new physics. REJECTED.** The Cs and Rb α determinations disagree with each other at 5.5σ, and the review's assessment is that the spread from −3.8σ to +2.3σ is "a manifestation of discrepant measurements of α rather than a hint of a possible deviation from the SM" (15). A discrepancy whose sign and size depend on which of two incompatible inputs you choose is not evidence about physics beyond the Standard Model. It is evidence about α.

**D4 — That ATLAS and CMS are presented as independent while sharing enough software that their agreement is worthless. REJECTED as stated; this was the archive's claim C1, already rejected in the register, and this audit confirms the rejection with the specific numbers.** The combinations publish their correlation assignments, state explicitly that "No category was identified to have ρ=1," justify the values, and scan them: the top-mass central value moves by at most 41 MeV against a 330 MeV total uncertainty under adverse assumptions (27). The surviving narrow claim is C1a as restated in section 2 — the correlation values rest on procedural rather than genealogical grounds, and no scan has been published for the discovery significance.

**D5 — That the muon g−2 resolution shows the theory was adjusted to fit the data. REJECTED as stated.** The lattice HVP is an ab-initio computation from the QCD action, not a fit; it took a falsifiable position before the final Fermilab measurement; and the quantity it disagrees with is itself experimental data (e⁺e⁻ cross sections). What the field has is two experimental routes to the same hadronic quantity disagreeing at about 3σ, not theory accommodating experiment (53, 54). The surviving claim is narrower and is retained in section 8: a 15-year anomaly was removed by a change of theoretical method rather than by new data about the muon, which bounds how much loop-breaking weight the case can carry.

**D6 — That the experimenter's regress makes instrumental knowledge impossible. REJECTED, on Franklin's grounds and on the evidence of section 6.** Franklin's rebuttal is primary literature and it is correct in the Weber case: the critics shared data, ran Weber's own algorithm, searched for his predicted error, and injected known pulses that his procedure failed to detect; "the regress can be broken by reasonable argument" (4). Section 6 exhibits a break with numbers: IBA codes reproduced a certified Sb implant fluence to −0.18 ± 0.11% against a value fixed beforehand by an independent chain terminating in weighed high-purity metal (46, 48). The regress is a question to ask of each case, not a general impossibility result.

**D7 — That the technology-works argument is worthless. REJECTED.** It is narrower than usually claimed, not empty. It establishes the theory to within the engineering margin, in the regime the technology exercises, for the quantities the output is sensitive to. For the 1911 Rutherford cross-section — parameter-free, predicted before any apparatus existed, contributing 0.10% to a 1% measurement (45) — the argument is decisive. The rejected version is the unscoped one that reads a working transistor as confirmation of the electroweak sector.

**D8 — That trigger design makes some physics unobservable in principle. REJECTED; this was the archive's claim C2, already rejected in the register.** The trigger-level literature documents large, quantified efficiency losses for unconventional signatures (57) — "below 20%" for Higgs-portal two-track, ~50% acceptance loss for barrel-only stau tracking — but losses are not impossibilities, and the authors' own point stands: "Triggering on 20% of events is infinitely better than triggering on none" (57). The surviving claim is C2a's structural asymmetry, not unobservability.

**D9 — That lattice QCD confirms QCD. WITHDRAWN as a formulation.** It confirms that QCD, given three measured hadron masses, reproduces nine more to 1–3%, across several genuinely different fermion discretisations. It cannot discriminate QCD from a rival strong-interaction theory, because no rival is implemented in the action. The distinction is between internal sufficiency and uniqueness, and the headline framing elides it.

**D10 — That "no published check exists" indicates concealment. REJECTED wherever it appears above.** Each such finding was reached by literature search and means only that the search found nothing. Absence of a published check is a gap in the literature, open to anyone with the apparatus and the motive. In three of the cases identified — the multi-energy RBS consistency test, the correlation scan for the discovery significance, and the parameter-range calculation for clinical margins — the check appears straightforwardly doable with existing data, which is itself the reason to state the absence plainly rather than to hedge it.

# References

1. Stanford Encyclopedia of Philosophy, "Pierre Duhem" — on *La Théorie Physique: Son Objet, Sa Structure* (1906; trans. *The Aim and Structure of Physical Theory*, 1954). https://plato.stanford.edu/entries/duhem/
2. Stanford Encyclopedia of Philosophy, "Theory and Observation in Science" — on Hanson, *Patterns of Discovery* (1958). https://plato.stanford.edu/entries/science-theory-observation/
3. H. M. Collins, *Changing Order: Replication and Induction in Scientific Practice* (University of Chicago Press, 1985). https://press.uchicago.edu/ucp/books/book/chicago/C/bo3623576.html
4. A. Franklin, "How to Avoid the Experimenters' Regress," *Studies in History and Philosophy of Science* (1994). https://physics.yale.edu/sites/default/files/files/3_1%20franklin.pdf
5. Stanford Encyclopedia of Philosophy, "Experiment in Physics" — on Collins (1985), Franklin (1986, 2002, 2013), Galison, *How Experiments End* (1987) and *Image and Logic* (1997), Pickering, *Constructing Quarks* (1984), Hacking (1992), Ackermann (1991), and the Morpurgo–Fairbank fractional-charge case. https://plato.stanford.edu/entries/physics-experiment/
6. Stanford Encyclopedia of Philosophy, "Theory and Observation in Science," sections on theory-ladenness and its mitigation (Woodward 2011; Laymon 1988; Elder 2023). https://plato.stanford.edu/entries/science-theory-observation/
7. Stanford Encyclopedia of Philosophy, "Scientific Realism" — on Putnam's no-miracles argument, Laudan, "A Confutation of Convergent Realism" (1981), the base-rate objection (Howson 2000; Lipton 2004; Magnus and Callender 2004), Hacking's entity realism (1982, 1983), Worrall's structural realism (1989), and Morrison (1990) and Resnik (1994). https://plato.stanford.edu/entries/scientific-realism/
8. P. Galison, *How Experiments End* (University of Chicago Press, 1987); *Image and Logic* (1997). Cited via (5).
9. A. Pickering, *Constructing Quarks: A Sociological History of Particle Physics* (University of Chicago Press, 1984). Cited via (5).
10. J. R. Klein and A. Roodman, "Blind Analysis in Nuclear and Particle Physics," *Annual Review of Nuclear and Particle Science* 55 (2005) 141. https://www.pp.rhul.ac.uk/~cowan/stat/annurev.nucl.55.090704.pdf
11. X. Fan, T. G. Myers, B. A. D. Sukra, G. Gabrielse, "Measurement of the Electron Magnetic Moment," *Phys. Rev. Lett.* 130 (2023) 071801. arXiv:2209.13084. https://arxiv.org/pdf/2209.13084
12. G. Gabrielse and G. Venanzoni, "Measured Lepton Magnetic Moments" (2026). https://cfp.physics.northwestern.edu/documents/2026-measured-lepton-magnetic-moments.pdf
13. S. Volkov, "Calculation of the total 10th order QED contribution to the electron magnetic moment," *Phys. Rev. D* 110 (2024) 036001. arXiv:2404.00649. https://doi.org/10.1103/PhysRevD.110.036001
14. T. Aoyama, M. Hayakawa, A. Hirayama, M. Nio, "Verification of the Tenth-Order QED Contribution to the Anomalous Magnetic Moment of the Electron from Diagrams without Fermion Loops," arXiv:2412.06473. https://arxiv.org/pdf/2412.06473
15. "Lepton anomalous magnetic moments: Theory," review, arXiv:2512.18382. https://arxiv.org/pdf/2512.18382
16. P. J. Mohr et al., "CODATA Recommended Values of the Fundamental Physical Constants: 2022," arXiv:2409.03787. https://arxiv.org/pdf/2409.03787 — and the CODATA 2022 summary values, https://physics.nist.gov/cuu/pdf/wallet_2022.pdf
17. S. Volkov, "Calculating the five-loop QED contribution to the electron anomalous magnetic moment: Graphs without lepton loops," arXiv:1909.08015. https://arxiv.org/pdf/1909.08015
18. "QED on the lattice and numerical perturbative computation of g−2," arXiv:2210.05569. https://arxiv.org/html/2210.05569
19. ATLAS Collaboration, "Observation of a new particle in the search for the Standard Model Higgs boson with the ATLAS detector at the LHC," *Phys. Lett. B* 716 (2012) 1. arXiv:1207.7214. https://arxiv.org/pdf/1207.7214
20. CMS Collaboration, "Observation of a new boson at a mass of 125 GeV with the CMS experiment at the LHC," *Phys. Lett. B* 716 (2012) 30. arXiv:1207.7235. https://arxiv.org/abs/1207.7235
21. R. Dawid, "Higgs Discovery and the Look Elsewhere Effect," *Philosophy of Science* 82 (2015) 76. https://philsci-archive.pitt.edu/10791/
22. D. Hooper, "What Makes A Discovery?", 182nd Nobel Symposium proceedings, arXiv:2312.00672. https://arxiv.org/pdf/2312.00672
23. P. Mättig and M. Stöltzner, "Model Choice and Crucial Tests. On the Empirical Epistemology of the Higgs Discovery," arXiv:1806.09201. https://arxiv.org/abs/1806.09201
24. ATLAS Collaboration, "Evidence for the spin-0 nature of the Higgs boson using ATLAS data," arXiv:1307.1432. https://arxiv.org/pdf/1307.1432
25. ATLAS Collaboration, "Measurements of Higgs boson properties in the diphoton decay channel with 36 fb⁻¹ of pp collision data at √s = 13 TeV," *Phys. Rev. D* 98 (2018) 052005. arXiv:1802.04146. https://arxiv.org/pdf/1802.04146
26. ATLAS and CMS Collaborations, "Measurements of the Higgs boson production and decay rates and constraints on its couplings from a combined ATLAS and CMS analysis," *JHEP* 08 (2016) 045. arXiv:1606.02266. https://arxiv.org/pdf/1606.02266
27. ATLAS and CMS Collaborations, "Combination of measurements of the top quark mass from data collected by the ATLAS and CMS experiments at √s = 7 and 8 TeV," arXiv:2402.08713. https://arxiv.org/pdf/2402.08713
28. ATLAS and CMS Collaborations, "Combination of inclusive top-quark pair production cross-section measurements using ATLAS and CMS data at √s = 7 and 8 TeV," arXiv:2205.13830. https://arxiv.org/pdf/2205.13830
29. "Validating Geant4 and its FLUKA.CERN interface against calorimeters beam tests," *EPJ Web of Conferences*, CALOR2024. https://www.epj-conferences.org/articles/epjconf/pdf/2025/05/epjconf_calor2024_00027.pdf
30. CMS Collaboration, "Blinding and unblinding analyses." https://cms.cern/physics/cms-higgs-search/blinding-and-unblinding-analyses
31. S. Dürr et al. (Budapest–Marseille–Wuppertal), "Ab initio determination of light hadron masses," *Science* 322 (2008) 1224. arXiv:0906.3599. https://arxiv.org/pdf/0906.3599v1
32. R. Sommer, "Scale setting in lattice QCD," arXiv:1401.3270. https://arxiv.org/pdf/1401.3270
33. Flavour Lattice Averaging Group, "FLAG Review 2024," arXiv:2411.04268. https://arxiv.org/pdf/2411.04268
34. CP-PACS Collaboration, "The CP-PACS Project and Lattice QCD Results," arXiv:hep-lat/0002024. https://arxiv.org/pdf/hep-lat/0002024
35. "Light Hadron Masses from Lattice QCD," review, arXiv:1203.4789. https://arxiv.org/pdf/1203.4789
36. "Light Hadron Masses and Decay Constants," Lattice 2009 plenary review, arXiv:0911.2191. https://arxiv.org/pdf/0911.2191
37. G. P. Salam, "Towards Jetography," *Eur. Phys. J. C* 67 (2010) 637. arXiv:0906.1833. https://arxiv.org/pdf/0906.1833v2
38. P. T. Komiske, E. M. Metodiev, J. Thaler, "An operational definition of quark and gluon jets," *JHEP* 11 (2018) 059. arXiv:1809.01140. https://arxiv.org/pdf/1809.01140
39. Particle Data Group, "Free Quark Searches," *Review of Particle Physics* 2026. https://pdg.lbl.gov/2026/reviews/rpp2026-rev-free-quark-searches.pdf
40. H. W. Kendall, "Deep Inelastic Scattering: Experiments on the Proton and the Observation of Scaling," Nobel Lecture, 1990. https://www.nobelprize.org/uploads/2018/06/kendall-lecture-1.pdf
41. ATLAS Collaboration, jet energy scale calibration from single-particle response, arXiv:2407.15627. https://arxiv.org/abs/2407.15627
42. A. Courtoy, J. Huston, P. Nadolsky, K. Xie, M. Yan, C.-P. Yuan, "Parton distributions need representative sampling," arXiv:2205.10444. https://arxiv.org/pdf/2205.10444
43. ATLAS Collaboration, "Performance of missing transverse momentum reconstruction with the ATLAS detector in Run 2," arXiv:2402.05858. https://arxiv.org/pdf/2402.05858
44. ATLAS Collaboration, "Search for dark matter and other new phenomena in events with an energetic jet and large missing transverse momentum," arXiv:1711.03301. https://arxiv.org/pdf/1711.03301
45. C. Jeynes et al., "Accurate Determination of Quantity of Material in Thin Films by Rutherford Backscattering Spectrometry," *Analytical Chemistry* 84 (2012) 6061. https://doi.org/10.1021/ac300904c — full text: https://www.surrey.ac.uk/sites/default/files/2021-03/accurate-determination-quantity-material-thin-films-rutherford-backscattering-spectrometry.pdf
46. N. P. Barradas et al., "International Atomic Energy Agency intercomparison of ion beam analysis software," *Nucl. Instr. Meth. B* 262 (2007) 281. https://mam.home.ipp.mpg.de/Barradas-Nuclear-Instruments-Methods-B-262-(2007)-281.pdf
47. CCQM-P190, "Thickness Measurement of nm HfO₂ Films," BIPM Consultative Committee for Amount of Substance, Surface Analysis Working Group. https://www.bipm.org/documents/20126/46087117/CCQM-P190.pdf
48. "On the way to SI traceable primary transfer standards for amount of substance measurements in inorganic chemical analysis," *Accreditation and Quality Assurance* (2023). https://pmc.ncbi.nlm.nih.gov/articles/PMC10287771/
49. J. R. Palta, "Perils of Proton Therapy," AAPM. https://www.aapm.org/meetings/09PRS/documents/Palta.pdf
50. M. Batic, G. Hoff, M. G. Pia, P. Saracco, "Epistemic and systematic uncertainties in Monte Carlo simulation: an investigation in proton Bragg peak simulation," arXiv:1012.3329. https://arxiv.org/pdf/1012.3329
51. "Evaluation of the accuracy of stopping and range of ions in matter simulations through secondary ion mass spectrometry and Rutherford backscattering spectrometry for low energy heavy ion implantation," OSTI 1830531. https://www.osti.gov/servlets/purl/1830531
52. Muon g−2 Collaboration, "Final Report on the Measurement of the Positive Muon Anomalous Magnetic Moment at Fermilab to 127 ppb," arXiv:2606.17323. https://arxiv.org/pdf/2606.17323
53. Muon g−2 Theory Initiative, "The anomalous magnetic moment of the muon in the Standard Model: an update," arXiv:2505.21476. https://arxiv.org/pdf/2505.21476
54. CERN Courier, "Fermilab's final word on muon g−2." https://cerncourier.com/fermilabs-final-word-on-muon-g-2/
55. CERN Courier, "CDF addresses W-mass doubt." https://cerncourier.com/a/cdf-addresses-w-mass-doubt/
56. OPERA Collaboration, "Measurement of the neutrino velocity with the OPERA detector in the CNGS beam," arXiv:1109.4897 (https://arxiv.org/pdf/1109.4897); timeline and error diagnosis as compiled at https://en.wikipedia.org/wiki/2011_OPERA_faster-than-light_neutrino_anomaly
57. "Optimizing Trigger-Level Track Reconstruction for Sensitivity to Exotic Signatures," arXiv:2211.05720. https://arxiv.org/pdf/2211.05720
