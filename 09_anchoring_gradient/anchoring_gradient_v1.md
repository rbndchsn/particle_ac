---
title: The Anchoring Gradient
subtitle: Whether the external constraint on physics weakens as the stakes rise, whether money and advocacy run the other way, and whether the whole observation is a tautology
author: Robin
date: 2026-11-25
version: v1
status: active — capstone; claim tested, partly rejected, narrowed and carried forward as A1–A4
source_files: 00_method/research_frame_v1.md; 00_method/claims_register_v1.md; 07_epistemic_audit/closed_loop_v1.md; 07_epistemic_audit/known_versus_assumed_v1.md; 03_hardware_systems/trigger_data_destruction_v1.md; 04_software_algorithmic/software_stack_bias_v1.md; 05_publication_governance/publication_governance_v1.md; 08_evidential_audit/proof_failure_modes_v1.md
---

# What This Document Tests

The archive has been circling one structural claim without stating it. `07_epistemic_audit/closed_loop_v1.md`
ends by rejecting the proposition that the closed loop is equally closed everywhere, on the ground that
"its length and the strength of its external anchors vary enormously between a tandem doing backscattering
and a collider inferring a short-lived particle." That sentence contains an unexamined thesis. This document
examines it.

The claim, stated as sharply as it can be:

> **The external anchoring of physics is strongest where the stakes are lowest and weakest where they are
> highest. Low-energy domains are pinned by technology that fails visibly and expensively if the physics is
> wrong. High-energy domains are anchored progressively less. Beyond-the-Standard-Model searches have no
> external anchor at all, by construction, because they look for things nothing else in the world interacts
> with. Meanwhile funding, institutional defence and public justification run in the opposite direction from
> the anchoring.**

That is three separable claims, and they are not equally interesting:

- **A — the gradient exists.** External anchoring declines monotonically with energy scale and with
  distance from applied physics.
- **B — the gradient has a specifiable shape.** What remains anchored at high energy is identifiable, and
  it is not the part that carries discovery claims.
- **C — the opposing gradient exists.** Money, personnel, strategy advocacy and public justification
  increase as anchoring decreases.

Claim A is close to a definitional truth and will be treated as such. Claim B is the one with content.
Claim C is empirical, testable against budget documents, and **it fails at national scale** — a result
reported in full below, because a claim that cannot be falsified by a budget table is not worth making and
a claim that is falsified by one must be said to be.

# What an External Anchor Is

The definition is the whole argument. A loose definition makes the gradient appear by construction; a tight
one risks excluding every case and proving nothing. The definition used here is deliberately tight, and the
places where tightening it does the work are flagged.

**An external anchor on a physical claim is a constraint satisfying all four of the following.**

1. **Foreign origin.** The constraint originates outside the discipline that produced the claim — a
   different discipline, an industry, a regulator, a clinic, or a natural system nobody in the discipline
   controls.
2. **Costly failure.** If the claim is wrong, something in the world fails: a device does not work, a
   patient is not cured, a clock drifts, a target cracks, a yield is three times the prediction. The failure
   is visible, expensive and non-negotiable.
3. **Disinterested arbiter.** Whoever declares the failure has no stake in the claim's survival. A chip
   either yields or it does not. A reactor either goes critical where predicted or it does not.
4. **Non-absorbable.** The failure cannot be accommodated by adjusting the claim and keeping the practice.
   A free parameter that soaks up the discrepancy is not an anchor; it is a hinge.

**Explicitly not anchors**, and these exclusions are where the definition bites:

- **Internal consistency.** A theory agreeing with itself.
- **Agreement between two measurements inside the same framework.** Two LHC experiments agreeing is not
  external, however independent their hardware, because the framework, the generators and the correction
  procedures are shared — this archive has already documented the shared lineage in
  `04_software_algorithmic` (claim C1b, SUPPORTED).
- **Goodness-of-fit.** A model fitting data it was tuned on, or data within the range it was tuned over.
- **Novel prediction.** Argued at length in §5.6 below. A prediction made before measurement is a *severe
  test* in Mayo's sense (6) and is epistemically valuable, but both the predicting and the measuring happen
  inside the discipline, and the cost of failure is a theory, not a device. Severity and externality are
  different virtues and the archive must not conflate them.

**Classes of anchor.** Not all anchors are the same kind, and the distinction matters for the verdict:

| Class | Kind | Failure signature | Who pays |
|---|---|---|---|
| **E1** | Operational / technological | a device does not work | the manufacturer, the operator, the user |
| **E2** | Safety / clinical | a patient is harmed, a criticality excursion, a wrong yield | the patient, the worker, the public |
| **E3** | Metrological / legal | a unit, a standard, a trade or regulatory measurement is wrong | the measurement system and everyone downstream |
| **E4** | Cross-disciplinary natural | an independently constrained natural system contradicts the claim | nobody — a theory dies, nothing breaks |
| **E0** | None | the claim's falsity has no consequence outside the discipline | nobody |

**E1–E3 satisfy all four conditions. E4 satisfies conditions 1, 3 and 4 but not condition 2.** When
helioseismology constrains the solar model, or Oklo constrains the fine structure constant, or
non-observation of proton decay kills minimal SU(5), the constraint is genuinely foreign and genuinely
non-negotiable — but nothing in the world fails. No device stops, no patient is harmed, no money is lost.
E4 constraints are **epistemically strong and institutionally weak**: they do not impose a cost on being
wrong, and the claim under test here is ultimately about where the cost of being wrong lands. Calling E4 a
"foreign constraint" rather than an "external anchor" is this document's most contestable move, and §5.7
argues it both ways.

## Where the Definition Could Be Contested, and What Turns On It

Four honest edge cases.

**The transfer problem.** An anchor constrains the specific physical content a device uses, not the whole
framework in which that content is expressed [C — rests on the case analyses in §3; falsified by one device
whose operation depends on a high-energy observable]. GPS anchors relativistic time dilation and the
caesium hyperfine transition. It does not anchor QED at two loops, let alone QCD at a TeV. Someone defending
the field can say the framework — relativistic quantum field theory, gauge invariance, Lorentz invariance —
is anchored by every working device. The reply is that the framework is anchored only in the sense that
nothing built on it has failed, and nothing built on it uses its high-energy content. This is the weakest
form of support a claim can have while still having some.

**Adequacy, not truth.** An anchor forces the physics to be *right enough for the purpose*; it does not
force it to be true. Semiconductor manufacture is the cleanest demonstration (§3.3). This cuts both ways: it
weakens the inference "anchored, therefore known," and it strengthens the structural point, because what an
anchor actually disciplines is *accountability*, not *correctness*.

**Timing.** An anchor can arrive late. Nuclear physics was unanchored in 1930 and anchored by 1945. A
detected BSM particle could be exploited a century hence. So "no anchor" is a statement about now, never
about in principle — with the single exception argued in §3.8.

**Self-service.** The definition was written by someone looking for a gradient. Condition 2 is the one doing
the work: relax it and the gradient flattens considerably, because E4 constraints are abundant at the high
end. The defence is that condition 2 is the condition the original claim rested on — "a device that does not
work, a patient who is not cured, a clock that drifts" — and that §5.7 reports what happens when it is
relaxed rather than hiding it.

**On the regress.** The definition is a practical answer to Collins's experimenter's regress (2): you cannot
know an instrument works without knowing the right answer, and you cannot know the right answer without a
working instrument. Franklin's response is a list of strategies — calibration against known inputs,
independent confirmation, testing rivals' methods on one's own data, intervention — and his central
condition is that "calibration of the apparatus is independent of the phenomenon one wants to observe" (3).
Perović's reply, specifically about the LHC, is that in-situ calibrating and measurement procedures and
parameters there are "closely and systematically interrelated," so empiricists should "question their
insistence on the independence of calibration from the outcomes of the experiment" (4) [B — Franklin and
Perović are the named advocates; Perović does not conclude that the LHC is open to the regress, only that
the independence assumption is too crude]. Hacking's entity realism — manipulative success as grounds for
belief (1) — is the strongest available version of the anchoring intuition, and E1 is its operational form.

# The Gradient, Domain by Domain

## Atomic Physics and Low-Energy QED

**Anchor class: E1 + E3. Failure latency: microseconds to hours. The strongest anchor in physics.**

The second is *defined* by a caesium hyperfine transition, which makes atomic physics the only domain on
this list whose correctness is a matter of law rather than of opinion [A]. Optical clocks now report
systematic uncertainties of 1.3 × 10⁻¹⁸ (7), and two clocks of different species have been compared at
2.08 × 10⁻¹⁸ over a 1,350 km fibre link (8); an international roadmap toward redefining the second on an
optical transition is in progress (9) [A].

The anchoring is not the precision — precision alone is internal. The anchoring is that the timing chain is
load-bearing for systems with no interest in atomic physics. On 26 January 2016, after a decommissioned
satellite was removed from the GPS constellation, the UTC offset broadcast on some legacy signals was wrong
by 13 microseconds (10, 11) [A]. One telecommunications operator logged over 2,000 alarms; another generated
nearly 2,500, with roughly 40 network elements entering holdover because backup inputs were missing; about
two-thirds of one operator's GPS timing estate was affected; roughly 30% of another's units caused
downstream switches to enter free run *with no visible alarms*; clearing one customer's alarms took about
four hours two days later (10) [A].

Thirteen microseconds. Not a theory in dispute — an operational event, diagnosed by telecoms engineers, at a
cost measured in engineer-hours and network risk. That is condition 2 and condition 3 in a single incident.

**What is anchored:** transition frequencies, relativistic time dilation and gravitational redshift,
systematic shift budgets (blackbody, collisional, Zeeman), and the whole metrological chain. **What is not:**
QED's loop structure. The electron anomalous magnetic moment agrees with theory at the part-per-trillion
level, which is the most impressive number in physics, and it is an internal agreement — a calculation and a
measurement, both inside the discipline, with no device downstream.

## Nuclear Physics

**Anchor class: E2 + E1. Failure latency: milliseconds to months. The most consequential anchor.**

The single clearest case in the whole gradient is Castle Bravo, 1 March 1954. The predicted yield was 6
megatons. The device yielded about 15, roughly 250% above prediction, because the designers assumed only one
of the two lithium isotopes in the fusion fuel would be reactive and both were (12) [A]. The consequences:
fallout over inhabited Marshall Islands atolls after a wind shift, evacuation and long-term health
monitoring with serious long-term effects among islanders; a Japanese fishing vessel sailing into the plume,
returning with a sick crew, radioactive tuna and one dead fisherman; a diplomatic crisis with Japan; and the
first public acknowledgement of multi-megaton capability (12) [A].

A nuclear cross section was wrong. People died, islands were contaminated, and a government had to explain
itself. Conditions 1 through 4, without qualification.

The institutional response is the anchoring regime that now exists. Evaluated nuclear data libraries are
validated against an international benchmark set of critical and subcritical configurations — the ICSBEP
Handbook — maintained outside any single laboratory (13), and the libraries are revised against it (14) [A].
The stockpile has been certified annually since 1992 without explosive testing, which makes simulation the
load-bearing element of a weapons-certification decision (17) [A]. In inertial confinement, the National
Ignition Facility missed its ignition goal for a decade after 2009 before achieving target gain above unity
in December 2022 — a public, expensive, dated failure of a high-energy-density prediction, followed by a
public, dated success (18) [A].

Two honest qualifications.

**Tokaimura was not a physics failure.** The 1999 criticality accident killed two workers, exposed 24 others
to up to 48 mSv, evacuated about 161 people and produced an estimated 13 billion yen liability against a 1
billion yen insurance limit — and it was caused by a procedural change made three years earlier without
regulatory permission, workers tipping uranyl nitrate from stainless steel buckets into a precipitation tank
that bypassed the criticality-safe geometry, with no understanding of the risk at 18.8% enrichment (16) [A].
The IAEA attributed it to "human error and serious breaches of safety principles." The criticality physics
was right; the practice was not. An anchor disciplines the *system*, and most of what it catches is
procedure, not theory. This weakens any simple reading of "anchored, therefore the physics is known."

**The anchored domain corrects itself under measurement, and the correction propagates upward.** Measured
reactor antineutrino fluxes at short baselines sit about 6% below the Huber+Mueller prediction, with a
world-average ratio of 0.943 ± 0.008 (experimental) ± 0.023 (model), and several experiments see a localised
4–6 MeV excess at about 4.4σ local significance in Daya Bay (15) [A]. Daya Bay's fuel-evolution measurement
found the predicted yield per fission for ²³⁵U significantly too high while ²³⁹Pu agreed, disfavouring a
uniform deficit at 2.8σ (15) [A]. The conservative reading is that the *nuclear data* were wrong, not that
there is a sterile neutrino (15) [B — the sterile interpretation retains advocates and global fits exist
that favour revised ²³⁵U plus a sterile state]. Note the direction of travel: a discrepancy in a
weakly-anchored domain (neutrino oscillation phenomenology) was most plausibly resolved by a correction in a
strongly-anchored one (fission beta spectra). The gradient has a slope, and information runs down it.

## Solid State and Semiconductors

**Anchor class: E1. Failure latency: one process run. The most economically brutal anchor — and the one
that proves anchoring is not truth.**

Here the gradient claim meets its most instructive complication. Semiconductor manufacture is the most
unforgiving E1 anchor in existence: a wrong dopant profile is a dead wafer lot, and the cost is immediate
and attributable. And yet the first-principles physics used in the domain is known to be wrong by large
factors.

Plain semilocal density functional theory underestimates semiconductor band gaps by roughly half: a
benchmark of 56 compounds gives PBEsol a mean absolute error of 1.99 eV and a mean percentage error of
−48.8%. Hybrid functionals (HSE06) reduce this to about 0.78 eV MAE and −14.7% mean percentage error, and
G₀W₀ to about 0.57 eV MAE and −12.5% — still "a noticeable underestimation of the band gaps by about 14% on
average" (19) [A].

A 14–50% error in the most basic electronic property of the material, in a domain where errors cost millions
per lot. The resolution is that production does not use first-principles band structure to set process
parameters. It uses process simulators calibrated against measured profiles — TCAD calibration of
ultra-shallow junctions against SIMS data is a documented industrial practice (20) [A]. Implantation range
distributions are computed with Monte Carlo codes whose parameters are fitted over the ion, energy and
substrate ranges in use.

**The lesson, and it governs the rest of this document:** an E1 anchor does not force the physics to be
true. It forces the *predictive pipeline* to be adequate over the operating range, and it permits — indeed
rewards — empirical calibration that absorbs theoretical error. What the anchor guarantees is not knowledge.
It is **accountability**: somebody finds out, fast, at a cost they cannot argue with, and must change
something [C — rests on the band-gap and TCAD facts above; falsified by a production process whose
parameters are set from uncalibrated first-principles calculation].

This is why the gradient matters even though anchoring is not truth. The claim under test is not "high-energy
physics is wrong." It is that the mechanism which forces anyone to find out and pay for it weakens as the
stakes rise.

## Accelerator Engineering — and the Distinction That Decides Everything

**Anchor class: E1, strong. Scope: the machine, not the physics done with it.**

Accelerator physics is anchored as hard as semiconductor physics and the failures are on the public record.
Strong focusing (21) is the enabling theoretical result of the whole field and it works. But the interesting
material is where predictions failed.

**At the LHC** [A, all from (22)]: the nominal design peak luminosity was 1.0 × 10³⁴ cm⁻²s⁻¹ and the machine
routinely exceeds twice that, with 2.2 × 10³⁴ tabulated as achieved against 1.0 × 10³⁴ design, and 60 events
per crossing against 27 nominal. Design energy is 7 TeV; running has been at 3.5, 4, 6.5 and 6.8 TeV,
limited by magnet retraining. Sectors trained more slowly than expected and *lost training memory after
thermal cycles*, which the operations literature calls a surprise; sector 23 needed 54 extra quench events
to reach 6.8 TeV, each recovery costing 8–12 hours. Arc heat loads ran significantly above what impedance
and synchrotron radiation predict, attributed mainly to higher secondary electron yield from surface
chemistry changes, to the point that post-LS2 degradation makes the HL-LHC nominal configuration
incompatible without surface treatment in LS3; cryogenic capacity is about 10 kW per arc against an 8 kW
design. Dust-induced beam losses ("UFOs") were the main cause of beam-induced quenches in Runs 2 and 3. The
original integrated-luminosity design goal was 300 fb⁻¹; Runs 1 and 2 delivered about 160 fb⁻¹ and 2024
alone delivered 122.2 fb⁻¹ to ATLAS and CMS.

**At LEP**, stray currents from trains running between Geneva Cornavin and French destinations leaked into
the earth and returned through the LEP tunnel, using the vacuum chamber as a conductor, interacting with the
dipole field and raising the beam energy by up to 12 MeV over a 14-hour fill (23) [A].

**At the Spallation Neutron Source**, the mercury target vessel's calculated lifetime was about 5,000 MWh.
Two vessels failed back-to-back in 2014 after about 100 and about 600 MWh. **None of the 11 targets used
since 2006 reached the predicted lifetime.** Each cost about $1 million; the failures plus an unrelated
fault cost 1,000 hours of operating time, about half recovered by rescheduling, with net available operating
time for the fiscal year down about 10%. The cause was not fully identified: both failed at welds, one at
the same weld that failed in 2012–13, with cyclic thermal and mechanical fatigue suspected (24) [A].

These are genuine, documented, expensive failures of prediction in a domain where GeV protons meet matter.
Which is exactly why the next sentence is the hinge of this document.

**These anchors constrain accelerator physics, not particle physics** [C — rests on the content of the
predictions that failed; falsified by showing that a machine performance prediction depends on a rare-process
observable]. The physics in a dynamic aperture calculation, a secondary electron yield, a weld fatigue model
or a stray-current field perturbation is classical and relativistic electrodynamics, materials science and
thermomechanics. Whether the collisions at the interaction point are correctly interpreted as Higgs
production is logically independent of whether the magnets quench where predicted. A machine that reaches
design luminosity has demonstrated that its builders understand beams. It has demonstrated nothing about
what the detectors' inferences mean.

The one serious exception is energy deposition from the collisions themselves, which is a hadronic
high-energy observable and which *does* fail visibly. It is treated as the document's strongest
counterexample in §5.2.

## Hadron Physics and QCD

**Anchor class: E1 and E2 at the low-GeV end, thinning rapidly with energy. The genuine middle of the
gradient.**

QCD is where the gradient stops being a step function and becomes a slope.

**What is internal.** The lattice calculation of the light hadron spectrum from first principles (25) is one
of the field's genuine achievements and it is entirely internal — a calculation reproducing measured masses.
The lattice has also made pre-measurement predictions that could have failed: the B_c mass was calculated as
6304 ± 12 (+18, −0) MeV and later measured by CDF at 6287 ± 5 MeV, agreeing at slightly over 1σ, with the
lattice paper posted before the measurement was announced; f_D+ was calculated as 201 ± 3 ± 17 MeV and
CLEO-c announced 223 ± 17 ± 3 MeV a few days later (26) [A]. These are severe tests in Mayo's sense (6).
They are not external anchors: the predicting and measuring communities overlap, and failure would have cost
a lattice action, not a device.

**What is external, and this is real.** Three independent E1/E2 anchors reach into hadronic physics:

- **Hadron therapy.** Carbon-ion treatment planning depends on nuclear fragmentation cross sections, and the
  models are measurably imperfect. Against reference data, Geant4 overestimates the total inelastic
  ¹²C + ²⁷Al cross section by about 5–10%; at 300 MeV/u the beryllium partial cross section worsened by
  roughly 10–15% between releases while boron improved to under 20% model difference; and the authors'
  recommendation for hadrontherapy is a specific physics list, QGSP_BIC_HP with the Opt4 electromagnetic
  constructor (27) [A]. Proton range uncertainty propagates directly into clinical margins (70) [A]. Proton
  therapy centres grew from 52 in 2015 to 128 by early 2026 (61) [A]. A wrong fragmentation cross section is
  a wrong dose to a real patient: condition 2, condition 3.
- **Atmospheric-neutron single event effects.** Soft error rates in microelectronics from atmospheric
  neutrons are standardised and measured by industry (29), and the models rest on proton- and
  neutron-induced nuclear reaction cross sections up to the GeV range (30) [A]. The arbiter is a data centre
  or an avionics bay.
- **Muon radiography.** Cosmic-ray muon flux and transport models are load-bearing for imaging that has
  located a large void in Khufu's pyramid (31) and produced three-dimensional images of the interior of a
  damaged reactor at Fukushima Daiichi (32) [A].

Medical isotope production belongs here too: yields depend on charged-particle reaction cross sections, and
the IAEA runs coordinated data projects precisely because wrong data means no isotope reaches a clinic (33)
[A].

**The energy ceiling of the anchor.** Every one of these operates at or below roughly a GeV per nucleon.
Above that, the external constraint thins to energy deposition and shielding — which is where the
counterexample in §5.2 lives — and the character of what is anchored changes from exclusive to inclusive.

## Electroweak Precision

**Anchor class: E0, with one E4 constraint. The first domain with no device downstream.**

Nothing in the world fails if the electroweak global fit is wrong. No clock drifts, no patient is harmed, no
wafer is scrapped. What pins electroweak precision is the fit's own internal consistency across many
observables, plus two things worth separating.

**Severe internal tests, which are real.** Global analyses constrained the top mass to roughly 140–190 GeV
before its 1995 discovery at the Tevatron, against a present value near 172.9 GeV; early fits favoured a
light Higgs of order 100 GeV rather than order 1 TeV, and later fits made successful predictions of M_H
before the 2012 observation at 125.1 GeV (34) [A]. These were risky and they could have failed. They are the
best evidence in the archive that a domain can be unanchored and still well-tested. §5.6 argues both ways on
whether they count.

**One E4 constraint.** Big Bang nucleosynthesis bounded the number of light neutrino species from
primordial abundances before LEP measured the Z invisible width (38) [A]. A foreign discipline constrained an
electroweak parameter and agreed. Nothing broke when it did.

**The diagnostic case.** In 2022 CDF reported the W mass as 80,433.5 ± 9.4 MeV, seven standard deviations
above a Standard Model prediction of 80,353 ± 6 MeV; CMS in 2024 reported 80,360.2 ± 9.9 MeV, consistent
with the prediction and with previous LHC results (35) [A]. A 7σ outlier against both theory and the rest of
the field was adjudicated over years by *more measurements of the same kind, by the same discipline*. The
muon anomalous magnetic moment tells the same story from the other side: the Fermilab experiment reached 127
ppb and the world average 124 ppb (36), while the Standard Model prediction moved under a reassessment of the
hadronic vacuum polarisation in which lattice and data-driven determinations disagreed (37) [B — the
lattice/R-ratio dispute has named advocates and the 2025 white paper's resolution is itself a theory-side
adjudication].

In an E1 domain the arbiter is the device and the timescale is a production run. Here the arbiter is the
discipline and the timescale is a decade. That difference, not any claim about correctness, is the gradient.

## The Higgs Sector

**Anchor class: E0. No anchor exists outside the collider programme.**

The question in the brief is whether there is any anchor outside the collider programme. The answer is no,
and the field says so itself. Asked in 2012 what the Higgs boson would be used for, Sean Carroll justified
the expense "by the purely intellectual reward associated with understanding the missing piece of the
Standard Model," noted the historical pattern that applications follow curiosity-driven work, and invited
readers to speculate about what a cheap tabletop Higgs would be good for — offering no application himself
(39) [A].

There is no metrological role: nothing in the SI depends on the Higgs. No clinical role. No device. The
Higgs couples to mass, and everything that interacts with the Higgs field already does so whether or not
anyone understands the mechanism, which is precisely why the mechanism's correctness has no operational
consequence. Vacuum stability, electroweak phase transition cosmology and the hierarchy problem are
constraints *from other theory*, not from the world.

This is not a criticism of the Higgs discovery, which is the best-tested piece of the last fifty years of
collider physics. It is a statement about where the cost of being wrong would have landed: nowhere outside
the discipline.

## Beyond-the-Standard-Model Searches

**Anchor class: E0, and uniquely, E0 by construction rather than by circumstance.**

This is the only place in the document where "no anchor" can be argued *in principle* and not merely as a
matter of present fact.

The argument: an E1 anchor requires that something in use depends on the phenomenon. A BSM particle is
defined by a coupling small enough to have escaped every existing measurement. Any particle feeble enough to
be undiscovered is, by that same feebleness, too feeble for anything to depend on. **The absence of an
external anchor on an undetected BSM particle is therefore not contingent; it is entailed by the search
condition** [C — rests on the definition of the search region; falsified by a technology whose operation
requires a not-yet-discovered particle, which would be self-contradictory]. The qualifier is temporal:
anchoring becomes available *after* detection, never before. Nuclear physics in 1930 was in exactly this
position.

The state of the searches [A]:

- **WIMP direct detection.** LZ's 4.2 tonne-year exposure reports no evidence for an excess over expected
  backgrounds, with a best-fit WIMP count of zero at every mass tested from 9 GeV to 100 TeV, and a
  world-leading spin-independent limit of 2.2 × 10⁻⁴⁸ cm² at 40 GeV (40). The irreducible background is now
  coherent elastic neutrino-nucleus scattering from solar and atmospheric neutrinos (40), and XENONnT has
  reported a first indication of solar ⁸B neutrinos via that channel (41) — the detectors have become
  neutrino instruments on the way to their limit.
- **Extra dimensions.** Limits only; no signal (42).
- **Supersymmetry.** Simplified-model bounds reach about 2.4 TeV for first- and second-generation gluinos and
  squarks, 1.3 TeV for stops and sbottoms, 1 TeV for electroweakinos — and the interpretation is contested:
  in the pMSSM, gluinos near 1 TeV and stops near 400 GeV remain viable, and a named body of work (Baer,
  Barger and Savoy on practical naturalness; Arkani-Hamed and Dimopoulos and Giudice and Romanino on split
  SUSY; Hall and Nomura on high-scale SUSY) holds that the principle is not excluded and that "no currently
  feasible collider can definitely exclude SUSY" (43) [B — this is the clearest Tier B in the document, with
  advocates named in the source].

Note what the last item shows about condition 4. The exclusion of SUSY parameter space is real work and it
has cost the theory something. But the response available to the theory — move to a corner of parameter
space the bound does not cover — is exactly the absorption that condition 4 excludes. An E1 anchor cannot be
answered that way. A wafer does not yield in a different corner of parameter space.

## Astrophysical and Cosmological Particle Claims

**Anchor class: E4 only — and E4 here is at its strongest anywhere in physics.**

The archive must not understate this. Astrophysics and cosmology have killed particle-physics theories, and
this is the only part of the high-energy landscape where any outside agency has ever done so.

- **Minimal SU(5) is dead, killed from outside the accelerator programme.** Georgi-Glashow minimal SU(5)
  predicted a proton lifetime of about 10³⁰–10³¹ years. IMB set a limit of 5.5 × 10³² years, Kamiokande
  2.6 × 10³², and the present Super-Kamiokande limit on p → e⁺π⁰ is 2.4 × 10³⁴ years at 90% CL — the model
  is ruled out, by a detector in a mine, by non-observation (44) [A].
- **The solar neutrino problem was a conflict between a particle-physics assumption and an astrophysical
  model, and the astrophysics won.** Helioseismology independently constrained the solar interior, closing
  the escape route that the Sun was wrong (45), and the resolution was that neutrinos have mass (46) [A].
  This is the single best case in the archive of a foreign discipline overturning a particle-physics
  assumption.
- **SN 1987A bounds axions and other weakly coupled particles** by the cooling argument, and those bounds
  constrain parameter space no terrestrial experiment reaches (47) [A].
- **Oklo** constrains variation in fundamental constants through the burn-up record of a natural reactor that
  operated two billion years ago (48) [A].
- **Neutrino mass** is now bounded directly at below 0.45 eV by KATRIN (49) and indirectly, more tightly and
  more model-dependently, by cosmology [A].
- **Dark energy** is the weakest link: the preference for evolving dark energy over a cosmological constant
  in recent survey data is actively contested on statistical grounds (50) [B].

Every one of these satisfies conditions 1, 3 and 4. None satisfies condition 2. When minimal SU(5) died,
nothing stopped working and nobody paid. That is why they sit in E4 and why §5.7 treats the boundary as the
document's most contestable line.

# The Gradient in One Table

| Domain | Anchor class | What is actually anchored | Failure latency | Arbiter |
|---|---|---|---|---|
| Atomic / low-energy QED | **E1 + E3** | transition frequencies, relativistic corrections, shift budgets | µs – hours | telecom and navigation operators; the SI |
| Nuclear | **E2 + E1** | cross sections, criticality, yields, decay heat, dose | ms – months | regulators, clinics, weapons certifiers, the public |
| Solid state | **E1** | calibrated process pipelines (not first-principles band structure) | one process run | wafer yield |
| Accelerator engineering | **E1** | beam optics, materials, thermomechanics, energy deposition | hours – years | the machine's own availability record |
| Hadron / QCD ≲ 1 GeV/u | **E2 + E1** | fragmentation and reaction cross sections, muon transport | days – years | patients, chip failure rates, imaging results |
| Hadron / QCD at TeV | **E1, narrow** | inclusive soft production, shower development, energy deposition | months – years | machine downtime (see §5.2) |
| Electroweak precision | **E0 + one E4** | nothing operational; BBN agreement on N_ν | a decade | the discipline |
| Higgs sector | **E0** | nothing outside the collider programme | — | the discipline |
| BSM searches | **E0 by construction** | nothing, entailed by the search condition | — | the discipline |
| Astro / cosmo particle claims | **E4** | theories die; nothing breaks | years – decades | other disciplines' observations |

**Verdict on claim A:** the gradient is real and maps cleanly, with one structural refinement and one
discontinuity. The refinement is that it is not a function of energy alone — it is a function of *whether
anything in use depends on the observable*, which correlates with energy because cross sections for usable
processes fall with energy. The discontinuity is at TeV-scale QCD, where a narrow E1 anchor survives on
inclusive observables while exclusive ones have none [A for the domain facts; C for the ordering].

# The Opposing Gradient: Money, People, Advocacy

Claim C says funding, institutional defence and public justification run opposite to the anchoring. This is
the empirically testable half of the thesis. It was tested against budget records. **It fails at national
scale, and it fails inside the high-energy programme on the most obvious cut. What survives is a narrower
and more interesting claim about what the justification documents actually count.**

## Spending Does Not Correlate Inversely With Anchoring

US Department of Energy appropriations, in thousands of dollars (51) [A]:

| Programme | FY2025 enacted | FY2026 enacted | FY2027 request | Anchor class of its core science |
|---|---|---|---|---|
| NNSA Weapons Activities (total) | 19,293,000 | 20,378,000 | 27,441,159 | **E2** |
| Basic Energy Sciences | 2,588,285 | 2,678,486 | 2,146,137 | **E1** |
| Advanced Scientific Computing Research | 1,036,235 | 1,116,328 | 1,104,446 | mixed |
| High Energy Physics | 1,224,570 | 1,235,156 | 1,120,458 | **E0 / E4** |
| Nuclear Physics | 825,600 | 866,141 | 791,434 | **E2 / E1** |
| Fusion Energy Sciences | 790,000 | 805,657 | 755,251 | **E1** |

The most heavily anchored science in the United States — weapons physics, where being wrong means Castle
Bravo — receives about **16 times** the High Energy Physics appropriation, and the ratio widens in the FY2027
request to about 24. Basic Energy Sciences, which funds the photon and neutron sources on which materials,
chemistry and structural biology depend, receives about **2.1 times** HEP. HEP's own appropriation declines
in the FY2027 request while NNSA's rises by about 35%.

**The claim that spending runs inversely to external anchoring is false** [A]. It is not weakly supported or
contested; it is contradicted by the appropriation table. This is reported as a Tier D rejection in §8 (D4)
and it is the most important negative result in this document, because it is what proves the overall thesis
is not a tautology (§7).

## Nor Inside the High-Energy Programme, On the Obvious Cut

DOE High Energy Physics by subprogram, FY2025 request, in thousands (52) [A]:

| Line | FY2023 enacted | FY2025 request |
|---|---|---|
| Energy Frontier Experimental Physics (ATLAS/CMS) | 180,833 | 150,268 |
| Intensity Frontier Experimental Physics | 273,199 | 275,209 |
| Cosmic Frontier Experimental Physics | 109,102 | 98,011 |
| Theoretical, Computational and Interdisciplinary Physics | 171,746 | 186,714 |
| Advanced Technology R&D | 133,120 | 115,566 |
| Construction — LBNF/DUNE-US | 176,000 | 280,000 |
| Construction — PIP-II | 120,000 | 125,000 |
| HL-LHC ATLAS detector upgrade (MIE) | 10,000 | 16,200 |
| HL-LHC CMS detector upgrade (MIE) | 10,000 | 17,500 |
| **Total, High Energy Physics** | **1,166,000** | **1,230,768** |

Energy Frontier plus Cosmic Frontier plus Theory is about $435M in the FY2025 request. Intensity Frontier
plus LBNF/DUNE plus PIP-II is about $680M. **The largest single investment in US high energy physics is the
neutrino programme — the sub-domain with the strongest E4 foreign constraints and the only one with a
cross-disciplinary record of overturning theory** [A]. The HL-LHC detector upgrades, serving the least
anchored physics, receive about $34M, roughly 2.7% of the programme.

Two caveats that cut in opposite directions. DUNE is itself substantially a BSM and symmetry-violation
search, so project-level anchoring is mixed rather than high [C]. And the $280M DUNE line is construction of
a facility rather than exploitation of one, so the comparison mixes capital and operating money. Both
caveats weaken the cut without rescuing the inverse correlation.

## Facility Cost at the Unanchored End

FCC-ee: an estimated **15 billion Swiss francs** for the electron-positron stage including tunnel and
infrastructure, a ring of about 90.7 km circumference, costs "distributed over a period of about 12 years
starting from the early 2030s," with a possible Council decision around 2028, and — the operative sentence —
"the majority of the funding would come from CERN's current annual budget," as with the LHC (55) [A].

CERN's 2026 Member State contributions total about **CHF 1,232.15 million** (54) [A]. The FCC-ee estimate is
therefore of order **twelve years of the entire Member State contribution**, committed to a programme whose
anchor class is E0. The European Strategy Group has recommended FCC-ee as the preferred option for CERN's
next flagship collider, with a descoped FCC-ee — removing the top-quark run, two interaction regions instead
of four, reduced RF power, about 15% less construction cost — as the preferred fallback, on the grounds that
other electron-positron options offer "substantially reduced precision programmes and no viable path to 10
TeV" (56) [A]. This archive's `05_publication_governance` file records the descoping savings line by line.

The P5 process on the US side sets its project thresholds at >$250M for large projects and works within
scenarios assuming 3% and 2% annual increases, declining to recommend one project (Spec-S5) because its cost
estimate "was not sufficiently mature" (57) [A].

## What the Justification Documents Actually Count — the Core Finding

This is where claim C survives, and it survives in documented form rather than as inference.

The published cost-benefit analysis of the LHC decomposes total benefits of €16.4bn against €13.5bn of
costs, giving a net present value of €2.9bn and a 92% probability that benefits exceed costs, as follows
(58) [A]:

| Benefit category | Mean value (€bn) | Share |
|---|---|---|
| Scientific knowledge | 0.28 | **1.7%** |
| Technological spillover | 5.4 | 32.8% |
| Human capital formation | 5.5 | 33.3% |
| Existence value | 3.2 | 19.5% |
| Cultural benefits | 2.1 | 12.7% |

**The field's own economic appraisal of its flagship instrument assigns 1.7% of the benefit to the physics
and 66.1% to technology transfer and training** [A]. The quasi-option value of future discoveries is set to
zero and applied-research benefits are excluded (58).

The critique of that appraisal is as important as the numbers. Scientific output is valued at the salaries
of the researchers who produced it and citations at reading time — so a discovery's value is made
proportional to the time and wages spent on it; publication and citation counts are unreliable because
erroneous papers attract citations and per-author metrics are meaningless in multi-thousand-author
collaborations; only 10% of CERN's general administrative costs are charged to the LHC, and at 75% the total
would rise by several billion euros, which the author notes is an uncertainty roughly the size of the NPV
itself; and the conclusion is that the method "cannot really evaluate the benefit of new scientific
knowledge," nor does any other current method do so quantitatively (58) [A].

The UK national evaluation shows the same structure independently. UK subscription was about £144m in 2019,
16% of Member State subscriptions, with total UK investment averaging about £152m a year over the decade;
about 500 UK firms won roughly £183.3m in CERN contracts over 2009–18, with surveyed suppliers
self-reporting an average +4% turnover boost extrapolated to about £1.05bn of additional turnover; young UK
researchers who engaged with CERN earn an estimated 12% more, worth about £489m in wages over the decade;
public willingness to pay is estimated at about £1.2bn, extrapolated from a French survey. **Knowledge is
valued at over £495m "based on UK authorship and citation of CERN papers"** (59) [A].

Both official appraisals value the *physics* bibliometrically — by authorship, citation and researcher
salary — and the *technology* by procurement and wages. In other words, at the unanchored end of the
gradient, the quantified justification for the instrument is composed almost entirely of things that are not
the physics claims, and the one component that is the physics claims is measured by an index internal to the
discipline [A].

**That is the defensible form of claim C.** Not "money runs opposite to anchoring" — the budget tables refute
that. But: **as external anchoring falls, the justification for expenditure shifts from the physics to
proxies (spillover, training, prestige, existence value), and the physics component is assessed by
discipline-internal metrics** [C — rests on (58) and (59); falsified by an official appraisal of a major
collider that monetises the physics knowledge by an external measure and finds it dominant].

## The Demand Asymmetry

A sharper way to put the same point, using user counts. Basic Energy Sciences user facilities reported about
11,606 users in FY2021 — 7,617 at light sources, 685 at neutron scattering facilities, 3,304 at nanoscale
science research centres — having peaked near 12,000 at the light sources alone in FY2014 (53) [A].

That is comparable in magnitude to the LHC user community. The difference is composition. BES facility users
are overwhelmingly from outside the discipline that built the facility: chemists, structural biologists,
materials engineers, industrial crystallographers whose own careers fail if the beamline misreports. LHC
users *are* the discipline. **Anchored facilities are funded by external demand; unanchored facilities are
funded by internal advocacy** [C — rests on the composition of the two user bases; falsified by showing a
substantial non-particle-physics user base whose work depends on collider data]. This is the structural
asymmetry the money tables fail to capture, and it is why the money tables refuting claim C do not dispose
of the thesis.

## Where the Sources Do Not Allow Quantification

Stated plainly, as the frame requires.

- **Career mass.** No verified current headcount for the ATLAS, CMS or total LHC user communities was
  obtained for this document; CERN's and the collaborations' own demographic documents were not retrievable.
  Any figure quoted from memory would be unsourced. The claim that career mass concentrates at the
  unanchored end is therefore **untested here** and must not be asserted.
- **Institutional defence as a measurable quantity.** Strategy-document advocacy can be read (56, 57) but
  not quantified against anchoring on any scale this document could construct. The qualitative dispute is
  live and has named advocates: Hossenfelder argues that the field has reached the end of a line and that
  the case for a larger collider is being constructed after the fact (65), and Butterfield's review replies
  that the diagnosis mistakes a methodological debate about naturalness for institutional self-interest (66)
  [B]. This document takes no side on it, because neither position is settled by anything in the budget
  records examined here.
- **Within-HEP anchoring weights.** Assigning a single anchor class to a budget line like "Intensity
  Frontier" is a judgement, not a measurement. The §6.2 cut should be read as indicative, not as a
  correlation coefficient.
- **DOE HEP subprogram figures** are FY2023 enacted and FY2025 request; the FY2025 *enacted* subprogram split
  was not retrieved, so the subprogram table and the appropriation table in §6.1 are not from the same
  fiscal vintage.

# Attempts to Break the Claim

This is the section the document exists for. Each candidate counterexample was run down to the question: does
it anchor the *particle physics claims*, or only the engineering?

## Spin-offs, One at a Time

**Hadron therapy.** The strongest of the medical cases. CERN hosted the 1996–2000 PIMMS study, which
produced the optimised proton and carbon-ion synchrotron design behind CNAO in Pavia and the basis for
MedAustron, and an ultra-compact 750 MHz RFQ built on Linac 4 experience accelerates protons to 5 MeV in
about 2 m, licensed to a spin-off (60) [A]. Patients are treated; a wrong dose harms them. **Verdict: a
genuine E2 anchor — on Bethe stopping power, nuclear fragmentation cross sections below about 400 MeV/u, and
accelerator engineering. Not on TeV-scale particle physics.** The physics it tests is the physics of §3.2 and
§3.5, which the gradient already places at the anchored end.

**MRI superconducting magnets.** This is the most-repeated claim in the public case for colliders, and it is
weaker than its reputation. CERN's own review of its impact on medical technology does not claim MRI magnets
at all; its superconducting magnet work is for ion-therapy facilities, including a toroidal gantry design,
and its magnetic-field-related medical product is a handheld radiation survey meter usable near PET-MRI
scanners — explicitly "not an MRI magnet" (60) [A/B — the broader industrial claim that accelerator demand
built the NbTi wire industry is real but is a claim about superconductor manufacturing capacity, not about
physics]. **Verdict: anchors materials and magnet engineering. Not particle physics.**

**The World Wide Web.** Anchors nothing physical. It was written at a particle physics laboratory; its
success is independent of whether any particle physics claim is true. The UK evaluation's citation of the
Web as adding 2.9% to global GDP is a global figure offered as context (59) [A]. **Verdict: no anchor.**

**Grid and distributed computing.** Engineering. **Verdict: no anchor.**

**Detector technology in imaging.** Medipix and Timepix hybrid pixel chips derive from LHC tracking
detectors; Medipix3 sorts photons into energy bins, enabling spectral X-ray imaging, and a MARS Bioimaging
scanner using Medipix3 produced the first 3D colour X-ray images of human extremities in 2018; Crystal Clear
crystals feed time-of-flight PET; Charpak's multiwire proportional chamber, invented at CERN in 1968, led to
a radiography technology used in orthopaedics (60) [A]. **Verdict: a real E1/E2 anchor on detector
engineering and on photon-matter interaction at keV energies. The clinical images do not depend on any
TeV-scale claim being true.**

A general note on this whole family. Every spin-off anchors the layer of physics the device *uses*, which is
always lower-energy than the physics the laboratory was built to study. That is not an accident of this
sample; it follows from the fact that a device must operate at energies and cross sections where effects are
large enough to exploit [C — rests on the case-by-case verdicts above; falsified by one deployed device whose
operation depends on a TeV-scale exclusive observable].

## The Strongest Counterexample: Radiation to Electronics and Machine Protection

This is the one that nearly breaks the claim, and it deserves to be stated at full strength before it is
qualified.

At the LHC, the physics of the collisions themselves produces a radiation field in the tunnel that destroys
electronics, and the cost is counted in machine availability. Over Run 2, radiation-to-electronics faults
caused **80 beam dumps**: 24 in 2015, 8 in 2016, 14 in 2017 and 34 in 2018, attributed to power converters
(35), the Quench Protection System (28), magnet circuits (10), RF (4) and other systems (3). Each dump costs
about three hours to re-establish stable beams with collisions. The dump rate stayed below 0.5 per fb⁻¹
except in 2015. Total ionising dose measured by the RadMon system at IP1 in 2017 and 2018 is reported as "in
good agreement with the predictions," which are FLUKA Monte Carlo simulations (62) [A]. Separately, the
machine carries about 362 MJ of stored beam energy at nominal LHC design and about 677 MJ at HL-LHC nominal
(22) [A], and machine protection depends on getting energy deposition right.

**This satisfies all four conditions.** The constraint is foreign to the physics analysis (it is enforced by
accelerator operations and equipment groups), the failure is visible and expensive (lost beam time,
destroyed hardware, in the limit a damaged magnet), the arbiter is disinterested (the availability record),
and it cannot be absorbed by a parameter.

**And it is an anchor on high-energy hadronic physics.** The radiation field in the tunnel is produced by
TeV-scale proton-proton collisions. If inelastic particle production at those energies were badly
mis-modelled, the shielding and the equipment placement would be wrong, and the machine would be unavailable
in ways its operators could not explain.

**The qualification, which is the crux of this document.** What this anchor constrains is *inclusive, bulk,
high-cross-section* observables: minimum-bias multiplicity, forward particle flux, shower development and
energy deposition. It cannot constrain the rare-process tail, for a reason that is structural rather than
practical: a process rare enough to require a discovery claim is, by that same rarity, far too rare to
deposit a measurable dose. The anchor's reach is proportional to cross section, and discovery physics lives
where the cross section is smallest [C — rests on the proportionality of dose to cross section and on the
R2E facts in (62); falsified by a machine-protection or shielding calculation whose outcome depends
materially on a rare-process cross section].

Supporting evidence on how accurate the anchored part actually is, which is more interesting than either
extreme would predict: against ATLAS calorimeter beam tests at 20–160 GeV, both Geant4 and the
Geant4-FLUKA.CERN combination overestimate the pion-to-electron response ratio by "up to a few percent";
Geant4 with FTFP_BERT reproduces the roughly 10% response difference between pion and proton showers in
TileCal at 16–30 GeV; and on longitudinal shower length the two codes **disagree in opposite directions**,
Geant4 underestimating and FLUKA.CERN overestimating, especially above 120 GeV (28) [A]. So at the anchored
frontier of high-energy hadronic physics the accuracy is percent-level on bulk response and the two leading
codes do not agree with each other on shape. That is precisely what a narrow anchor looks like: tight where
the money is, loose immediately outside it.

And the SNS targets (§3.4) show what happens when a GeV-scale prediction in this same family is tested
hard: eleven targets, not one reaching the calculated 5,000 MWh lifetime, two failing at about 100 and 600
MWh, cause not fully identified (24) [A]. The anchor fired, the prediction lost, and the field could not
immediately say why.

## The Spallation and Soft-Error Family

Treated in §3.5 and §5.2; the verdict is recorded here for completeness. Atmospheric-neutron single event
effects (29, 30), medical isotope production yields (33) and muon radiography (31, 32) are genuine E1/E2
anchors reaching up to roughly a GeV. They anchor nuclear reaction and transport physics. They do not reach
the electroweak or Higgs sectors at all, and they reach QCD only in its inclusive, low-energy regime.

## Did Any High-Energy Result Ever Get Overturned by an External Constraint?

Searched for specifically. **No case was found in which an E1–E3 anchor overturned a particle-physics
claim** [C — an absence of evidence, stated as such; falsified by one documented case, which would be a
major result and should be sought actively]. The nearest candidates and why each falls short:

- **OPERA's superluminal neutrino claim of 2011.** Retracted after instrumental faults were identified in the
  timing chain. The contradicting evidence was a theoretical argument from vacuum-Cherenkov-type energy loss
  (64) and a measurement by another detector in the same tunnel (63) [A]. Both internal. Nothing in the
  world failed; the claim failed.
- **Minimal SU(5).** Killed by proton-decay non-observation (44) — a genuine foreign constraint, but E4.
- **The reactor antineutrino anomaly.** The closest thing to the anchored domain correcting the less-anchored
  one, and it runs downhill: nuclear fission data correcting neutrino phenomenology (15) [A/B]. Still not a
  device failing.
- **Castle Bravo and the SNS targets.** Real anchored failures of prediction — in nuclear and accelerator
  physics, not in particle physics (12, 24) [A].
- **The pentaquark Θ⁺ and the CDF W mass.** Both corrected, both internally (35, and the Θ⁺ case recorded in
  `05_publication_governance`) [A].

The honest summary: the field self-corrects, repeatedly and on the record, and in no documented case has the
correcting agent been something outside it that stopped working.

## Precision Electroweak Prediction as an Anchor — Argued Both Ways

The brief asks whether pre-measurement predictions of the W and Z masses, the top mass from loop
corrections, and the Higgs mass range count as anchors. The question deserves both answers in full.

**The case that they do count.** These predictions were risky and specific. The top mass was constrained to
roughly 140–190 GeV before the particle existed as an observation, and came in near 172.9 GeV; fits favoured
a light Higgs of order 100 GeV against the then-live alternative of order 1 TeV, and the boson arrived at
125.1 GeV (34) [A]. On Mayo's severity criterion, a test is severe when the hypothesis would probably have
failed it if false (6), and these qualify. Worrall's use-novelty criterion is also satisfied: the top and
Higgs masses were not used to construct the theory being tested (5). Under predictivism in any of its
versions — Maher's reliable-method argument, Worrall's conditional-versus-unconditional confirmation,
Hitchcock and Sober's overfitting guard (5) — this is strong confirmation, and much stronger than "the model
fits." A critic who dismisses it is not being rigorous; they are being hostile.

**The case that they do not count, which is this document's position.** Three reasons, each tied to a
condition.

*Condition 1, foreign origin, fails.* The predicting and the measuring were done by one discipline with
overlapping personnel, shared software lineage, shared systematic-uncertainty conventions and shared
correction procedures. This archive has documented the shared lineage quantitatively (claims C1a′, C1b,
SUPPORTED, in `04_software_algorithmic` and `08_evidential_audit`). An agreement between two parts of one
community is not a foreign constraint, however severe it is.

*Condition 2, costly failure, fails.* Had the top mass come in at 400 GeV, the cost would have been borne by
a theory and by some careers. No clock would have drifted and no patient would have been harmed. There is no
price signal.

*Condition 4, non-absorbability, fails.* The electroweak framework has designed-in latitude for exactly this
contingency: S, T and U parameters, and now effective-field-theory operators, exist to parameterise
deviations. A discrepancy becomes a measurement of a new coefficient. That is the correct scientific
response and it is also precisely the absorption condition 4 excludes.

**Resolution.** Severe internal testing and external anchoring are distinct virtues and electroweak physics
has the first in abundance and the second not at all. **The archive must therefore never write "unanchored"
and mean "untested."** Making that slide would be the single fastest way to discredit the defensible
material here, and §8 records it as a rejected claim (D2). What the distinction buys is a sharper question
than "is it true?": *who finds out, how fast, and at whose expense?* In the electroweak sector the answer is
the discipline, over a decade, at its own expense — as the W mass episode demonstrates in detail (35).

## Neutrino Physics Through Solar and Atmospheric Observation — the Hardest Case

The brief asks whether neutrino physics is anchored through astrophysical cross-checks produced outside
accelerator laboratories. This is the document's most contestable line and both readings are stated.

**The case for calling it anchored.** The solar neutrino problem was resolved against a particle-physics
assumption. The Sun's interior was independently constrained by helioseismology, which removed the option of
blaming the astrophysical model (45); detectors in mines, built and operated by a community that was not the
accelerator community, measured a deficit; and the resolution was that neutrinos have mass (46) [A]. Proton
decay non-observation killed minimal SU(5) outright (44). Big Bang nucleosynthesis counted neutrino species
before LEP did (38). SN 1987A bounds axion couplings no laboratory reaches (47). Oklo bounds constant
variation over two billion years (48). These constraints are foreign in origin, disinterested, and
non-absorbable — three of four conditions, and the three that matter most epistemically. On any ordinary
usage, neutrino physics *is* externally constrained, and more so than any other part of high-energy physics.

**The case for calling it a foreign constraint rather than an anchor.** Condition 2 fails in every case.
When minimal SU(5) died, nothing stopped working. No manufacturer lost a lot, no patient was mistreated, no
operator logged 2,000 alarms. The arbiter was disinterested but also *unharmed*, and an arbiter who bears no
cost imposes no cost. The claim under test is about where the price of error lands, and E4 constraints send
no invoice.

**Verdict.** Neutrino physics occupies a genuine intermediate class — E4-strong, E1-absent — and it is the
reason the gradient is a slope and not a cliff. Calling it unanchored full stop would be false. Calling it
anchored in the sense that semiconductor physics is anchored would also be false. The archive should carry
both facts: **neutrino physics has the strongest foreign constraints and none of the operational ones**, and
the funding data (§6.2) show it is also the best-funded part of US high energy physics, which is a point
*against* claim C and is recorded as such.

# The Tautology Objection

The strongest counterargument to this entire document, stated without softening:

> The gradient is simply what "frontier" means. A frontier is by definition the region where nothing yet
> built depends on the phenomenon, because if something depended on it, it would be applied physics. You
> cannot have external technological anchors for phenomena nobody can yet exploit. So "external anchoring is
> weakest at the frontier" is true the way "the newest thing is the least established thing" is true — a
> definition wearing the clothes of a critique. Worse, it is a critique that would have condemned nuclear
> physics in 1930, semiconductor physics in 1945 and laser cooling in 1975, each of which later became the
> anchored domain the argument now uses as its standard.

This objection is correct about claim A and must be conceded in full. **The existence of the gradient is
near-tautological and is not presented here as a finding.** The historical point is also conceded: every
anchored domain in §3 was unanchored once, and the document's own §2 edge case on timing says so. Anyone
reading claim A as a criticism of high-energy physics has read it wrong.

Three things survive the objection, and they are the document's actual content.

**First, the opposing gradient is empirical and it was falsified.** A tautology cannot be refuted by an
appropriation table. Claim C was tested against DOE appropriations and **failed**: the most anchored science
is the best funded, by a factor of 16 (51), and inside HEP the best-funded line is the sub-domain with the
strongest foreign constraints (52). A thesis whose second half can be — and was — destroyed by budget
records is not a tautology. It is a conjunction of a near-definitional observation with a contingent
empirical claim, and the empirical claim lost. That result is worth more than the thesis would have been if
it had won.

**Second, the shape of the surviving anchor is not tautological.** That TeV-scale physics retains a narrow E1
anchor on inclusive soft production through radiation-to-electronics and machine protection (62), that this
anchor's reach is proportional to cross section and therefore cannot extend to discovery physics, and that at
its own frontier the two leading simulation codes disagree in opposite directions on shower shape (28) —
none of that follows from the meaning of "frontier." It is a specific, checkable claim about which
observables are disciplined by cost and which are not, and it is falsifiable by a single counterexample
(§5.2).

**Third, what the justification documents count is not tautological.** That the official cost-benefit
analysis of the LHC assigns 1.7% of benefit to scientific knowledge and 66% to spillover and human capital
(58), and that both it and the UK national evaluation monetise the physics by authorship and citation (58,
59), is a documented property of the appraisal literature. A field could have been anchored only weakly and
still have justified itself primarily by its physics. These ones do not.

**Does the claim survive?** **Partly, and not in the form it was stated.** As stated — "anchoring is weakest
where the stakes are highest, and funding runs the other way" — it does not survive: the first half is
near-definitional and the second half is false at national scale. What survives is narrower and sharper:

> **Accountability does not travel with claim-strength.** As external anchoring falls, the entity that
> determines whether a claim was wrong converges on the entity that made it; the anchoring that remains at
> the high-energy end covers bulk inclusive observables and, for structural reasons tied to cross section,
> cannot cover the rare-process claims that carry discovery weight; and the quantified public justification
> for instruments at that end rests on proxies for the physics rather than on the physics, with the physics
> component itself assessed by discipline-internal metrics.

That formulation is testable, partly documented, partly inferential, and it is not a tautology. It is also
considerably less dramatic than the claim this document was asked to test, which is the usual outcome when
a structural intuition is made to meet budget tables and primary literature.

# What Survives, as Register Entries

Proposed for `00_method/claims_register_v1.md`. Nothing below should be carried into a published synthesis
in any other wording.

| ID | Claim | Tier | Status |
|---|---|---|---|
| A1 | External anchoring, defined as a foreign, costly, disinterested and non-absorbable constraint, declines monotonically across the domains surveyed, and the ordering tracks whether anything in use depends on the observable rather than energy scale as such | C | SUPPORTED-AS-INFERENCE — near-definitional; must never be presented as a finding |
| A2 | The external anchoring that survives at TeV energies operates on inclusive, high-cross-section observables (particle production, shower development, energy deposition) via radiation-to-electronics and machine protection, and its reach is proportional to cross section, so it cannot extend to the rare-process claims that carry discovery weight | C | SUPPORTED-AS-INFERENCE — falsified by one shielding or machine-protection calculation whose outcome turns on a rare-process cross section |
| A3 | Both official economic appraisals of CERN's programme value scientific knowledge at a small fraction of total benefit (1.7% of €16.4bn in the LHC CBA) and assess that fraction by discipline-internal bibliometrics, with technology transfer and human capital carrying two-thirds of the quantified case | A | SUPPORTED |
| A4 | No case exists in the record searched in which a particle-physics claim was overturned by an operational, clinical or metrological failure outside the discipline; corrections have come from within the discipline or from cross-disciplinary observation that imposes no cost | C | SUPPORTED-AS-INFERENCE — an absence; falsified by one documented case |
| A5 | ~~Funding, facility cost and institutional defence run inversely to external anchoring~~ | — | **REJECTED** — see §6.1 and D4 |
| A6 | ~~Accelerator and detector technology spin-offs anchor the particle-physics claims~~ | — | **REJECTED** — see §5.1 and D6 |
| A7 | Precision electroweak prediction constitutes severe internal testing and not external anchoring, and the two must be held apart | C | SUPPORTED-AS-INFERENCE — definitional, argued both ways in §5.6 |
| A8 | Neutrino physics occupies an intermediate class: the strongest foreign constraints in high-energy physics (solar, atmospheric, proton decay, BBN, SN 1987A, Oklo) and no operational ones | A/C | SUPPORTED — the classification is an inference, the constraints are documented |

# Falsification Conditions

Each is a genuine test and some may be passed.

- **A1 fails** if a deployed technology is identified whose operation depends on a TeV-scale exclusive
  observable, or if the ordering in §4 can be inverted by a defensible alternative anchor definition that
  still excludes internal consistency, inter-experiment agreement and goodness-of-fit.
- **A2 fails** if a machine-protection, shielding or radiation-to-electronics calculation is shown to depend
  materially on a rare-process cross section, or if the dose-to-cross-section proportionality argument is
  shown to be wrong.
- **A3 fails** if an official appraisal of a major collider monetises the physics knowledge by a measure
  external to the discipline and finds it dominant among the benefit categories.
- **A4 fails** on one documented case. This should be actively sought, not assumed absent.
- **The whole document fails as a critique** if the tautology objection in §7 is judged to defeat the
  narrowed formulation as well as the original — in which case the correct conclusion is that the gradient
  is a description of frontier science and nothing more, and the archive should say so.

# Claims Examined and Not Supported

**D1 — That weak external anchoring implies a claim is false, fabricated, or probably wrong.** Rejected [D].
There is no inferential route from "nothing outside the discipline would break if this were wrong" to "this
is wrong." The Higgs discovery, the electroweak fit and the measured exclusion of large volumes of SUSY
parameter space are unanchored in this document's sense and also, as far as any evidence shows, correct.
This archive's binding scope boundary already excludes fabrication claims (`00_method/research_frame_v1.md`)
and nothing here reopens them.

**D2 — That unanchored means unjustified, or untested.** Rejected [D], and this is the most important rejection
in the document. Electroweak physics predicted the top mass in a 140–190 GeV window before the particle was
observed and favoured a light Higgs against a heavy one before 125 GeV was measured (34). Those are severe
tests on Mayo's own criterion (6) and satisfy use-novelty (5). Lattice QCD predicted the B_c mass and f_D+
before measurement (26). A domain can be unanchored and rigorously tested, and conflating the two would
discredit everything defensible in this file. §5.6 argues the point at length precisely so that it cannot be
read any other way.

**D3 — That this gradient is unique to particle physics.** Rejected [D]. Tested honestly against three other
frontier fields.

*Cosmology.* The same gradient, steeper. Nothing in the world depends on dark energy's equation of state;
the preference for an evolving one over a cosmological constant is contested on statistical grounds (50)
[B]. Cosmology's constraints are E4 throughout, and its appeal to a disinterested arbiter is weaker than
neutrino physics's, because its independent probes share systematics and a single sky.

*String theory.* E0 everywhere, and the field has produced an explicit methodological response rather than
denying the problem: a sustained argument over whether a research programme with no risky prediction can be
assessed non-empirically at all, conducted in the open between the programme's methodologists and its
critics (67) [B — the dispute has named advocates on both sides and is not resolved].
The gradient's endpoint is therefore occupied not by particle physics but by a neighbouring field that has
openly argued for changing the standard of evidence in response.

*Deep-time geology.* This one is instructive because it is anchored at its shallow end and not at its deep
end — the same shape, driven by the same mechanism. Radiocarbon is calibrated against dendrochronology and
tied to absolutely dated cosmogenic spikes in tree rings at 774 and 993 CE (68, 69) [A], and basin and
petroleum-system modelling is paid for in dry wells, which is as clean an E1 anchor as semiconductor yield
(70-adjacent industrial practice) [C]. Hadean geology has no such anchor at all. Nobody drills for the
Hadean.

**Conclusion: the gradient is a general feature of frontier science, not a pathology of particle physics.**
Particle physics is distinctive only in the *ratio of expenditure to anchor* at the unanchored end — a CHF
15bn instrument (55) against an E0 anchor class — and even that distinction is partly beaten by cosmology
per unit of anchor, and entirely beaten by string theory on anchor though not on cost.

**D4 — That funding, facility cost and institutional defence run inversely to external anchoring.** Rejected [D],
with numbers. NNSA Weapons Activities, the most heavily anchored physics in the United States, received
$19.293bn in FY2025 against High Energy Physics's $1.225bn, and the FY2027 request widens the ratio from
about 16 to about 24; Basic Energy Sciences received about 2.1 times HEP (51) [A]. Inside HEP, the
neutrino programme — the sub-domain with the strongest foreign constraints — is the largest single
investment, at roughly $680M against about $435M for Energy Frontier, Cosmic Frontier and theory combined
(52) [A]. The narrower claim that survives concerns the *composition of the justification*, not the
magnitude of the spend (A3), and the demand asymmetry between externally-populated and internally-populated
user communities (§6.6) is an inference, not a measurement.

**D5 — That accelerator engineering's anchors extend to the particle physics done with the machines.**
Rejected [D], but with a carved-out exception that must travel with the rejection. Beam optics, magnet training,
electron-cloud heat loads, stray-current field perturbations and target fatigue are anchored hard and have
demonstrably failed against prediction (22, 23, 24) [A], and none of that bears on the interpretation of
collision data. The exception is radiation-to-electronics and machine protection (62), which genuinely
anchor inclusive high-energy hadronic production (A2). Stating the rejection without the exception would
misrepresent the evidence.

**D6 — That spin-offs anchor the physics.** Rejected [D], case by case (§5.1). Hadron therapy, Medipix, PET
crystals, the multiwire chamber, the Web, grid computing and superconducting magnet technology each anchor
either engineering or a layer of physics below the one the laboratory was built to study. CERN's own review
of its medical impact does not even claim MRI magnets (60) [A], which is worth noting given how often the
public argument does.

**D7 — That BSM searches' lack of an external anchor is a defect of those searches, or a reason not to
fund them.** Rejected [D]. An undetected particle's feebleness is the search condition; anchoring is
structurally unavailable before detection, not withheld (§3.8). The honest reading is that BSM searches
must be justified on grounds other than anchoring, which is what the field does, and the archive's question
is whether those grounds are stated candidly — a question for
`02_theory_critique` and `05_publication_governance`, not for this file.

**D8 — That novel prediction is an external anchor.** Rejected [D] as definitional (§5.6, A7). Recorded here so
it is not re-litigated: predictive success is a severe test and a real epistemic virtue, and it is not what
condition 2 asks for.

**D9 — That the LHC has no external anchor at all.** Rejected [D]. 80 radiation-induced beam dumps in Run 2,
FLUKA dose predictions tested against RadMon measurements, 362 MJ of stored beam requiring correct energy
deposition (62, 22) [A]. The LHC is externally anchored on bulk inclusive observables. The claim is about
the reach of that anchor, not its existence, and overstating it would have been the easiest error in this
document to make.

**D10 — That the claim as originally stated is a finding of this archive.** Rejected [D]. It is near-tautological
in its first half (§7) and false in its second (D4). Only the narrowed formulation at the end of §7 and the
register entries A1–A4, A7 and A8 may be carried forward.

**D11 — That the anchored domains are therefore "known" in a way the unanchored ones are not.** Rejected [D], and
this is the subtlest of the rejections. Plain DFT underestimates semiconductor band gaps by about 49%, and
even G₀W₀ by about 14% on average (19) [A], in the most ruthlessly anchored domain in science. Eleven of
eleven SNS targets missed their calculated lifetime (24). Castle Bravo was off by 250% (12). What an anchor
produces is not correctness but **accountability under cost** — somebody finds out quickly, at a price they
cannot argue with, and must change something. The gradient is a gradient of accountability, and saying
otherwise would make the archive claim far more than its evidence supports.

# Version Log

| Version | Date | Status | Change |
|---|---|---|---|
| v1 | 2026-11-25 | active | Claim stated, anchor definition built with E0–E4 classes, gradient mapped over nine domains, opposing gradient tested against DOE and CERN budget records and **rejected at national scale**, counterexamples run down individually with radiation-to-electronics identified as the strongest, tautology objection given full weight and conceded for claim A, claim narrowed to accountability rather than anchoring, eleven claims recorded as not supported. |

# References

Entries were retrieved and read between 2026-11-24 and 2026-11-25 except where noted. Entries 9, 13, 14, 17,
21, 29, 33, 63 and 68 were identified by title and bibliographic record but their full text was not
retrieved for this version; claims resting on them are limited to what the title or record states and are
marked where load-bearing.

1. Hacking, I. (1983). *Representing and Intervening: Introductory Topics in the Philosophy of Natural Science*. Cambridge University Press. See also: Entity realism. https://en.wikipedia.org/wiki/Entity_realism
2. Collins, H. M. (1985). *Changing Order: Replication and Induction in Scientific Practice*. London: Sage.
3. Franklin, A. (1994). How to avoid the experimenters' regress. *Studies in History and Philosophy of Science* 25(3), 463–491. https://physics.yale.edu/sites/default/files/files/3_1%20franklin.pdf
4. Perović, S. (2017). Experimenter's regress argument, empiricism, and the calibration of the Large Hadron Collider. *Synthese* 194. https://doi.org/10.1007/s11229-015-0749-6
5. Stanford Encyclopedia of Philosophy. Prediction versus Accommodation. https://plato.stanford.edu/entries/prediction-accommodation/
6. Mayo, D. G. (1991). Novel evidence and severe tests. *Philosophy of Science* 58(4), 523–552. https://errorstatistics.com/wp-content/uploads/2021/02/mayo-1991_novel-evid-severe-tests.pdf
7. Ytterbium lattice clock with systematic uncertainty of 1.3×10⁻¹⁸ and instability at the 10⁻¹⁹ level. arXiv:2606.10514. https://arxiv.org/html/2606.10514v2
8. Yb/Sr optical clock comparison at 2.08×10⁻¹⁸ uncertainty over a 1350-km fibre link. arXiv:2610.34250. https://arxiv.org/pdf/2610.34250
9. Dimarcq, N. et al. (2024). Roadmap towards the redefinition of the second. *Metrologia* 61, 012001. https://doi.org/10.1088/1681-7575/ad17d2 (title and record only; site blocked automated retrieval)
10. Chronos Technology / Resilient Navigation and Timing Foundation. Case study: the 26 January 2016 GPS event. https://rntfnd.org/wp-content/uploads/26-January-2016-GPS-Event.pdf
11. NIST. The effects of the January 2016 UTC offset anomaly on GPS-controlled clocks. https://tf.nist.gov/general/pdf/2886.pdf
12. Wellerstein, A. (2014). Castle Bravo at 60. *Restricted Data: The Nuclear Secrecy Blog*. https://blog.nuclearsecrecy.com/2014/02/28/castle-bravo-at-60/
13. OECD Nuclear Energy Agency. International Criticality Safety Benchmark Evaluation Project (ICSBEP) Handbook. https://oecd-nea.org/jcms/pl_20291/international-criticality-safety-benchmark-evaluation-project-icsbep-handbook
14. ENDF/B-VIII.1: updated nuclear reaction data library for science and applications. arXiv:2511.03564. https://arxiv.org/pdf/2511.03564
15. Roskovec, B. (2018). Reactor neutrino spectrum and flux. NuPhys2017 proceedings. arXiv:1804.00027. https://arxiv.org/pdf/1804.00027
16. World Nuclear Association. Tokaimura criticality accident, 1999. https://world-nuclear.org/information-library/safety-and-security/safety-of-plants/tokaimura-criticality-accident
17. US National Nuclear Security Administration. Fiscal Year 2025 Stockpile Stewardship and Management Plan. https://www.energy.gov/sites/default/files/2024-10/FY2025%20Stockpile%20Stewardship%20and%20Management%20Plan.pdf
18. American Institute of Physics FYI (2022). National Ignition Facility achieves long-sought fusion goal. https://www.aip.org/fyi/2022/national-ignition-facility-achieves-long-sought-fusion-goal
19. A benchmark of first-principles methods for accurate prediction of semiconductor band gaps. arXiv:2211.14644. https://arxiv.org/pdf/2211.14644
20. TCAD calibration of ultra-shallow-junction profiles for advanced deep sub-µm CMOS processes. *Nuclear Instruments and Methods in Physics Research B*. https://www.sciencedirect.com/science/article/abs/pii/S0168583X01009090
21. Courant, E. D., Livingston, M. S. & Snyder, H. S. (1952). The strong-focusing synchrotron — a new high-energy accelerator. *Physical Review* 88, 1190. https://doi.org/10.1103/PhysRev.88.1190
22. LHC operation and the High-Luminosity LHC upgrade project. arXiv:2505.03535. https://arxiv.org/html/2505.03535v1
23. A newly observed effect affects the LEP beam energy. EPAC96 proceedings, THP022G. https://proceedings.jacow.org/e96/PAPERS/THPG/THP022G.PDF
24. *Physics Today*. Oak Ridge officials are puzzled by failure of targets at Spallation Neutron Source. https://physicstoday.aip.org/news/oak-ridge-officials-are-puzzled-by-failure-of-targets-at-spallation-neutron-source
25. Dürr, S. et al. (2008). Ab initio determination of light hadron masses. *Science* 322, 1224. arXiv:0906.3599. https://arxiv.org/pdf/0906.3599
26. Predictions from lattice QCD. FERMILAB-CONF-05-428-T, arXiv:hep-lat/0509169. https://arxiv.org/html/hep-lat/0509169
27. Experimental validation of Geant4 nuclear interaction models in dose calculations of therapeutic carbon ion beams. *Medical Physics* (2025). https://www.osti.gov/pages/servlets/purl/2575025
28. Validating Geant4 and its FLUKA.CERN interface against calorimeter beam tests. CALOR2024, *EPJ Web of Conferences*. https://www.epj-conferences.org/articles/epjconf/pdf/2025/05/epjconf_calor2024_00027.pdf
29. JEDEC JESD89. Measurement and reporting of alpha particle and terrestrial cosmic ray-induced soft errors in semiconductor devices. http://gpc.pnpi.nrcki.ru/images/files/docs/JEDEC_Standart.pdf
30. Proton and neutron induced SEU cross section modelling and simulation: a unified analytical approach. arXiv:2402.12983. https://arxiv.org/pdf/2402.12983
31. Morishima, K. et al. (2017). Discovery of a big void in Khufu's Pyramid by observation of cosmic-ray muons. arXiv:1711.01576. https://arxiv.org/pdf/1711.01576
32. 3D imaging of a nuclear reactor using muography measurements. *Science Advances*. https://doi.org/10.1126/sciadv.abq8431
33. International Atomic Energy Agency. ISOTOPIA: simulation of medical isotope production with accelerators. https://nds.iaea.org/talys/tutorials/isotopia.pdf
34. Electroweak precision tests of the Standard Model after the discovery of the Higgs boson. arXiv:1902.05142. https://arxiv.org/pdf/1902.05142
35. *CERN Courier*. W mass snaps back. https://cerncourier.com/a/w-mass-snaps-back/
36. Muon g−2 Collaboration. Final report on the measurement of the positive muon anomalous magnetic moment at Fermilab to 127 ppb. arXiv:2606.17323. https://arxiv.org/pdf/2606.17323
37. Muon g−2 Theory Initiative. White Paper (2025). https://muon-gm2-theory.illinois.edu/white-paper-25/
38. The Big-Bang nucleosynthesis limit to the number of neutrino species. arXiv:astro-ph/9606059. https://arxiv.org/abs/astro-ph/9606059
39. Carroll, S. (2012). Technological applications of the Higgs boson. *Preposterous Universe*. https://www.preposterousuniverse.com/blog/2012/03/20/technological-applications-of-the-higgs-boson/
40. LZ Collaboration. Dark matter search results from 4.2 tonne-years of exposure of the LUX-ZEPLIN experiment. arXiv:2410.17036. https://arxiv.org/html/2410.17036v3
41. XENON Collaboration. First indication of solar ⁸B neutrinos via coherent elastic neutrino-nucleus scattering with XENONnT. arXiv:2408.02877. https://arxiv.org/pdf/2408.02877
42. Particle Data Group (2025). Extra dimensions listing. https://pdg.lbl.gov/2025/listings/rpp2025-list-extra-dimensions.pdf
43. The LHC has ruled out supersymmetry — really? arXiv:2505.11251. https://arxiv.org/pdf/2505.11251
44. Ohlsson, T. (2023). Proton decay. arXiv:2306.02401. https://arxiv.org/pdf/2306.02401
45. Helioseismology and solar neutrinos: an update. arXiv:astro-ph/0012239. https://arxiv.org/html/astro-ph/0012239
46. The Sun, neutrinos and Super-Kamiokande. https://pmc.ncbi.nlm.nih.gov/articles/PMC7298169/
47. Raffelt, G. (1997). Astrophysical axion bounds: an update. arXiv:astro-ph/9707268. https://arxiv.org/pdf/astro-ph/9707268
48. Investigation of the stability of fundamental constants based on the Oklo reactor burn-up analysis. arXiv:1010.6299. https://arxiv.org/html/1010.6299
49. Max Planck Institute for Nuclear Physics (2025). KATRIN sets new limit for the neutrino mass: below 0.45 eV. https://www.mpi-hd.mpg.de/mpi/en/public-relations/news/news-item/katrin-sets-new-limit-for-neutrino-mass
50. A Bayesian perspective on evidence for evolving dark energy. arXiv:2511.10631. https://arxiv.org/abs/2511.10631
51. US Department of Energy. FY 2027 statistical table by appropriation (FY2025 and FY2026 enacted, FY2027 request). https://www.energy.gov/documents/doe-fy-2027-statistical-table-appropriation
52. US Department of Energy Office of Science. High Energy Physics FY 2025 congressional justification. https://science.osti.gov/-/media/budget/pdf/sc-budget-request-to-congress/2025/High-Energy-Physics-3_15_24---Final.pdf
53. US Department of Energy Office of Science. Number of users reported by BES user facilities. https://science.osti.gov/-/media/bes/suf/pdf/BES_Facilities_Number_of_Users.pdf
54. CERN Finance and Administrative Processes. 2026 annual contributions to the CERN budget. https://fap-dep.web.cern.ch/2026-annual-contributions-to-cern-budget/
55. CERN (2025). CERN releases report on the feasibility of a possible Future Circular Collider. https://home.cern/cern-releases-report-feasibility-possible-future-circular-collider/
56. *CERN Courier*. European Strategy Group recommends FCC-ee. https://cerncourier.com/european-strategy-group-recommends-fcc-ee/
57. Particle Physics Project Prioritization Panel (2023). *Exploring the Quantum Universe*, Section 8: Budgetary considerations. https://www.usparticlephysics.org/2023-p5-report/budgetary-considerations.html
58. Some remarks concerning the cost/benefit analysis applied to the LHC at CERN. arXiv:1511.05477. https://arxiv.org/pdf/1511.05477 (reports and critiques Florio, Forte & Sirtori's CBA)
59. UK Research and Innovation / STFC (2021). Evaluation of the benefits that the UK has derived from CERN: main report. https://www.ukri.org/wp-content/uploads/2021/12/091221-STFC-EvaluationOfBenefitsUKDerivesFromCERN-MainReport.pdf
60. *CERN Courier*. CERN's impact on medical technology. https://cerncourier.com/a/cerns-impact-on-medical-technology/
61. Particle Therapy Co-Operative Group. Global development of particle therapy centres. https://ptcog.online/global-development-of-particle-therapy-centers/
62. Radiation to electronics impact on CERN LHC operation: Run 2 overview and HL-LHC outlook. https://inspirehep.net/files/8364ca66e5b626a7b7ac03d696693d29
63. *MIT Press Reader*. The OPERA experiment and the value of high-profile scientific blunders. https://thereader.mitpress.mit.edu/when-science-fails-opera-neutrinos/ (title and record only)
64. Constraint on superluminal neutrinos from vacuum Cherenkov processes. arXiv:1111.2725. https://arxiv.org/pdf/1111.2725
65. Hossenfelder, S. (2019). Particle physics may have reached the end of the line. *Backreaction*. http://backreaction.blogspot.com/2019/01/particle-physics-may-have-reached-end.html
66. Butterfield, J. (2019). Lost in Math? arXiv:1902.03480. https://arxiv.org/pdf/1902.03480
67. String theory and general methodology: a reciprocal evaluation. arXiv:0912.3160. https://arxiv.org/pdf/0912.3160
68. Reimer, P. J. et al. (2020). The IntCal20 Northern Hemisphere radiocarbon age calibration curve (0–55 cal kBP). *Radiocarbon* 62(4), 725–757. https://doi.org/10.1017/RDC.2020.41
69. Tree rings reveal globally coherent signature of cosmogenic radiocarbon events in 774 and 993 CE. *Nature Communications* 9, 3605. https://www.nature.com/articles/s41467-018-06036-0
70. Dosimetric impact of range uncertainty in passive scattering proton therapy. https://pmc.ncbi.nlm.nih.gov/articles/PMC8130244/
