---
title: Known, Inferred, Assumed
subtitle: What the precision actually is, where the inferential chain becomes model-dependent, and an honest status rating of every competing framework and live anomaly
author: Robin
date: 2026-11-24
version: v1
status: draft - stream 07 (epistemic audit), first full pass; Tier D section closed
source_files:
  - PDG 2024/2025/2026 reviews and listings (Z boson, W mass, Higgs, Vud-Vus, axions, extra dimensions, compositeness, free quark searches, electroweak model)
  - arXiv:2506.03069, arXiv:2606.17323 (Fermilab Muon g-2 final result)
  - arXiv:2505.21476 (Muon g-2 Theory Initiative White Paper 2025)
  - PhysRevLett 130, 071801 (Fan et al., electron magnetic moment)
  - Atoms 7 (2019) 28 (Aoyama, Kinoshita, Nio); arXiv:2412.06473 (tenth-order verification)
  - arXiv:2412.13872 (CMS W mass); arXiv:2506.01887 (W mass status)
  - arXiv:2608.07332 (ATLAS Higgs combination); arXiv:2407.13554 (CMS Higgs self-coupling)
  - arXiv:2410.05380 (NuFit-6.0); arXiv:0906.3599 (lattice light hadron masses)
  - arXiv:2407.15627 (ATLAS jet energy scale); arXiv:2402.05858 (ATLAS missing transverse momentum)
  - EJPS 11 (2021) 101 (Antoniou, What is a data model?); arXiv:2312.00672 (Hooper, What Makes A Discovery)
  - arXiv:1806.09201 (Maettig and Stoeltzner); SEP entries on Experiment in Physics and Theory and Observation
  - arXiv:2505.11251 (Constantin, Kraml, Mahmoudi on SUSY); arXiv:2402.01087 (lattice strong dynamics)
  - arXiv:1911.02967 (Donoghue, Critique of Asymptotic Safety); arXiv:2501.17006 (Famaey and Durakovic on MOND)
  - arXiv:2503.13594 (sterile neutrino exclusion); arXiv:2406.11438 (KamLAND-Zen)
  - arXiv:2503.14738 (DESI DR2); arXiv:2410.17036 (LZ 4.2 tonne-years); arXiv:2105.13858 (Borexino)
  - arXiv:2009.06864 (Junk and Lyons on reproducibility); arXiv:2003.07868 (LHC reinterpretation report)
  - astro.ucla.edu/~wright/lerner_errors.html (Wright on plasma cosmology)
---

## What this stream is for, and why it must cut both ways

This file exists to calibrate the rest of the archive. Its job is not to find weakness. Its
job is to find the *location* of weakness, which requires first establishing, with real
numbers, where there is none.

Two failure modes are equally fatal here. The first is to understate the Standard Model's
empirical standing, which would make every other file in this archive dismissible in a
sentence. The second is to accept the field's own framing of its inferential chain without
examining it, which would make the archive pointless. The sections below are written so
that a hostile specialist and a hostile sceptic would both find something they did not want
to read.

Three structural findings, stated up front:

1. **The precision is real and, in places, understated in popular accounts.** The Z boson
   mass is known to 2.2 parts in 100,000. Nine hadron masses were computed from three inputs
   to 1-3%. These are not interpretive claims.
2. **The inferential chain is robustly instrumental up to the calibrated physics object and
   becomes irreducibly model-dependent at exactly two later steps** - the mapping from object
   to theoretical entity, and the acceptance factor that converts a yield into a rate. Naming
   those two steps precisely is worth more than a general complaint about theory-ladenness.
3. **The field's own literature contains the sharpest available statements of its epistemic
   limits.** Any critique that claims the field is unaware is refuted by that literature, and
   should instead ask whether the acknowledgement is assembled anywhere, by anyone, into an
   auditable whole.

---

## Part 1 - What is confirmed, and to what precision

### The electron anomalous magnetic moment: the strongest single test, with a caveat the field states openly

The measurement is **g/2 = 1.001 159 652 180 59(13)**, a fractional uncertainty of 0.13 parts
per trillion, which is fifteen significant figures (1). **[A]** The Standard Model prediction,
dominated by QED, agrees with it at about one part in 10^12 (1). **[A]**

The theory side is a five-loop calculation. The tenth-order QED contribution involves
**12,672 Feynman diagrams** in 32 gauge-invariant subsets (2). **[A]** The predicted value is
a_e = 1 159 652 181.606(11)(12)(229) x 10^-12, where the three uncertainties are tenth-order
QED (0.011), hadronic (0.012), and the input value of the fine structure constant (0.229) (2).
**[A]**

That last number is the whole epistemic story of this test, and it cuts against the popular
framing. **The comparison is not limited by QED. It is limited by alpha, which must be
imported from an independent measurement, and the two best independent determinations of
alpha disagree with each other.** The alpha inferred from g/2 plus the SM differs by 2.1 sigma
from the Paris rubidium determination and 3.9 sigma from the Berkeley caesium determination (1).
**[A]** Until that is resolved, predicted and measured values agree only to about
delta(g/2) = 0.7 x 10^-12 (1). **[A]**

A second calibrating detail: the two independent calculations of the tenth-order QED
coefficient disagreed at about **5 sigma** until 2024-2025, when the discrepancy was traced to
98 diagrams sharing a common structure whose Monte Carlo integration errors accumulated
non-randomly; rerunning those with higher statistics resolved it (3). **[A]** The theory side
of the most precise test in physics required an independent recomputation to find an error.
That is the system working, and it is also evidence that a single calculation at this depth is
not self-certifying.

The wider alpha picture is a strong independent argument for the framework: alpha^-1 is
determined to 10^-9 from the electron g-2, to 10^-8 from rubidium atom recoil, and to 10^-8
from the quantum Hall effect, by apparatus with nothing physical in common, and the values
agree to within about 10 parts in 10^9 (4). **[A]**

### The muon anomalous magnetic moment

Fermilab's final result, Runs 1-6, is **a_mu = 116 592 070.5(14.8) x 10^-11, a precision of
127 ppb**, about four times better than Brookhaven E821 (5)(8). **[A]** The experimental world
average is 116 592 071.5(14.5) x 10^-11, 124 ppb (5). **[A]**

The 2025 Theory Initiative White Paper gives **a_mu^SM = 116 592 033(62) x 10^-11**, a relative
uncertainty of 530 ppb, and a difference from experiment of **38(63) x 10^-11, about
0.6 sigma** (6)(7). **[A]**

The theory precision is four times worse than the experimental precision. That asymmetry is
the live issue, and it is treated in Part 5.

### Z boson: the most precisely measured massive particle

PDG values: **m_Z = 91.1880 +/- 0.0020 GeV** (relative precision 2.2 x 10^-5),
**Gamma_Z = 2.4955 +/- 0.0023 GeV** (9.2 x 10^-4), and invisible width
**Gamma_inv = 499.2 +/- 1.5 MeV** (3.0 x 10^-3) (13). **[A]** PDG notes the Breit-Wigner mass
parameter is 34 MeV above the propagator-pole real part - a definitional, not experimental,
subtlety, and the field states it (13). **[A]**

### W boson mass: precise, and contested

| Measurement | m_W (MeV) | In PDG average |
|---|---|---|
| CDF-II (2022) | 80433.5 +/- 9.4 | no |
| CMS (2025) | 80360.2 +/- 9.9 | no (new) |
| ATLAS (2024) | 80366.5 +/- 15.9 | no (supersedes earlier) |
| ATLAS (earlier) | 80370 +/- 19 | yes |
| D0 | 80383 +/- 23 | yes |
| LHCb | 80354 +/- 32 | yes |
| LEP2 | 80376 +/- 33 | yes |

(14)(15) **[A]** PDG world average: **80369.2 +/- 13.3 MeV**, chi^2/dof = 0.5/3 (14). **[A]**
The electroweak fit, excluding m_W and Gamma_W, predicts 80356 +/- 6 MeV (14), and the Gfitter
indirect prediction is 80354 +/- 7 MeV (17). **[A]** CMS alone is 9.9 MeV, i.e. 1.2 x 10^-4
relative, and its authors describe it as in agreement with the SM (15). **[A]**

### Higgs boson

Mass: ATLAS combines diphoton and four-lepton channels to **125.11 +/- 0.11 GeV, a relative
precision of 0.09%** (18). **[A]**

Couplings, ATLAS Run 2 combination, kappa framework at 68% CL (20): **[A]**

| Modifier | Value | Approx. precision |
|---|---|---|
| kappa_W | 1.01 +0.09/-0.07 | ~8% |
| kappa_Z | 0.99 +0.09/-0.07 | ~8% |
| kappa_t | 0.93 +0.09/-0.07 | ~9% |
| \|kappa_b\| | 0.92 +0.13/-0.11 | ~13% |
| \|kappa_tau\| | 0.95 +0.10/-0.08 | ~9% |
| \|kappa_mu\| | 1.09 +0.28/-0.32 | ~27% |
| \|kappa_g\| | 1.00 +0.11/-0.09 | ~10% |
| \|kappa_gamma\| | 1.00 +0.10/-0.08 | ~9% |

In the two-modifier fit, **kappa_V = 1.002 +0.027/-0.026** (20). **[A]** Inclusive signal
strength mu = 0.990 +0.053/-0.051, p_SM = 77-78% (20). **[A]** PDG states the gamma-gamma, ZZ,
WW, bb and tau-tau branching fractions are measured to **10% precision**, with ATLAS
mu = 1.023 +0.056/-0.053 and CMS mu = 1.014 +0.055/-0.053 (19). **[A]**

Where it is weak, and the field says so: the charm coupling is only bounded, kappa_c < 4.1 at
95% CL (20); undetected branching fraction B_u < 18-32% depending on assumptions (20); and the
**self-coupling is barely constrained at all, -1.2 < kappa_lambda < 7.5** at about 95% CL (21).
**[A]** The shape of the Higgs potential - the thing the mechanism is about - is essentially
unmeasured. The theoretical uncertainty on the signal is now the largest single contributor to
the uncertainty on mu, larger than statistics or experimental systematics (19). **[A]**

### CKM unitarity: a real and acknowledged tension

PDG 2025: |V_ud| = 0.97367 (superallowed beta decays), |V_us| = 0.22431(85) **with a scale
factor S = 2.5 applied because the Kl3 and Kmu2 determinations disagree**, and the first-row
sum **|V_ud|^2 + |V_us|^2 + |V_ub|^2 = 0.9983(6)(4)** (22). **[A]** That is about **2 sigma from
unity, rising to about 3 sigma if nuclear-structure uncertainties are ignored** (22). **[A]**
PDG's own list of candidate causes is radiative or nuclear-structure corrections to V_ud, the
lattice determination of f+(0), or new physics - in that order (22). **[A]**

### Neutrino oscillations: established, parameters moderately precise

NuFit-6.0 3-sigma relative precisions: theta_12 about 13%, theta_13 about 8%, delta m^2_21
about 15%, |delta m^2_3l| about 6% (23). **[A]** Unresolved: the theta_23 octant, with "no
clear indication of whether it is larger or smaller than 45 degrees," and the mass ordering,
where the global fit gives nearly equally good fits for both orderings until the
Super-Kamiokande atmospheric chi^2 table is added, which shifts the preference to normal
ordering with delta chi^2 = 6.1 (23). **[A]** For inverted ordering, CP-violating values near
270 degrees are favoured over CP conservation at more than 3.6 sigma (23). **[A]**

This is a different epistemic class from the electroweak sector: the *existence* of oscillation
is established beyond argument, the parameters are known to 6-15%, and two discrete properties
remain undetermined.

### Lattice QCD: the strongest answer to any claim that quarks are bookkeeping

The Budapest-Marseille-Wuppertal calculation took as input **only the light quark mass, the
strange quark mass, and the gauge coupling**, fixed by the pion and kaon masses plus one scale,
and then predicted the rho, K*, N, Lambda, Sigma, Delta, Sigma*, Xi* and Omega masses - about
nine genuine predictions - to within **1-3% of experiment** (24). **[A]**

Three numbers in, nine out, at percent level. Any account in which quarks are a calculational
fiction has to explain this result, and no such account attempts to.

### Global electroweak consistency

Gfitter: **chi^2/dof = 16.62/15, p-value 0.34** (17). **[A]** Largest pulls: A_FB^b at 2.4
sigma, the SLD leptonic left-right asymmetry at -2.1 sigma, m_W at -0.8 (17). **[A]** The
indirect prediction for the top mass, with m_t excluded from the fit, is 175.15 +2.37/-2.39 GeV
against a direct combination of 172.47 +/- 0.46 GeV (17). **[A]**

### Plain statement

The Standard Model's confirmed sector is the most precisely tested theoretical structure in
the history of science, and the margin is not close. A fifteen-significant-figure measurement
matched by a 12,672-diagram calculation; a particle mass known to two parts in 100,000; nine
hadron masses predicted from three inputs; a 15-parameter global fit with p = 0.34. **[A]**
Any critique of this field that does not begin by conceding this is not a critique; it is an
error. Everything in the remainder of this file is a claim about what *surrounds* that core -
its motivation, its inferential plumbing, its auditability, and the frameworks that have been
proposed to extend it.

---

## Part 2 - The inferential chain, step by step

The chain is: **electronic signal -> reconstructed hit -> track or cluster -> physics object ->
theoretical entity**, with a rate or cross-section at the end.

### Where it is not model-dependent, and why that matters

Steps one to three are instrumental and anchored outside the theory under test. The ATLAS jet
energy scale is a useful worked example precisely because it is the step most often alleged to
be circular.

The first calibration step **is** simulation-based, and the collaboration says so: the baseline
correction is MC-derived and corrects for the calorimeter's lower hadron response, energy
outside the jet, and dead material (27). **[A]** But the target of that correction is stated
explicitly: it ensures that "the reconstructed jet energy equals, on average, the energy of the
corresponding jet formed by **stable particles**" (27). **[A]** The field calibrates jets to
*particle level*, not parton level. The simulation is then corrected against data by in-situ
techniques - pT balance in Z/gamma+jet events, dijet eta-intercalibration - and against
single-particle test-beam response via a deconvolution method (27). **[A]** The resulting
combined uncertainty is **0.3% at pT = 300 GeV and 0.6% at 4 TeV** for anti-kT R = 0.4 jets at
|eta| < 0.8 (27). **[A]**

Generator dependence is present and is treated as an uncertainty rather than hidden: "Jet
fragmentation effects are addressed by comparing the results obtained with the Pythia MC event
generator" against Sherpa (27). **[A]**

A 0.3% energy scale anchored on test-beam single-particle response and in-data momentum balance
is not a theory-laden artefact. Calibration against independently established quantities is the
oldest item on Franklin's list of epistemological strategies, and this is a textbook instance
of it (33). **[A]**

### Where it becomes irreducibly model-dependent: two specific steps

**Step 4 -> 5, object to entity.** This is the real hinge, and it has two signature cases.

*Jets as proxies for partons.* The calibrated object is a four-vector defined by an algorithm
over particle-level energy flow. Calling it "a quark" or "a gluon" is a mapping licensed by QCD
factorisation, not a measurement. The field's own strongest statement of the underlying fact is
PDG's: **"Experiments have produced no evidence for free propagating quarks"** (25). **[A]**
QCD predicts exactly this - quarks are confined in hadrons or deconfined in quark-gluon plasma
- and PDG notes the one partial exception, that the top quark decays while still effectively
free because its lifetime is shorter than the hadronisation time (25). **[A]**

The honest formulation: *the parton is never the object of a measurement; the particle-level
jet is. Unfolding from particle level to parton level is a further, separately labelled,
model-dependent step, and the field performs it as such.* Stated that way the claim is correct
and survives specialist reading. Stated as "jets are just assumed to be quarks" it is false,
because it ignores the particle-level calibration target.

What would falsify the strong version of the critique: a confinement-free formulation of
hadronic physics that reproduced Bjorken scaling, R = 11/3, and the lattice hadron spectrum.
None exists. **[C]**

*Missing transverse energy as inference of invisible particles.* ATLAS defines pT^miss as the
magnitude of the negative vector sum over reconstructed objects and calls it, in its own words,
**"a proxy for momentum carried by undetected particles"** (28). **[A]** It is built from hard
terms (electrons, photons, hadronic taus, muons, jets) and a soft term consisting of
hard-scatter vertex tracks not assigned to any hard object - which means **neutral soft energy
is simply absent from the construction** (28). **[A]**

The soft term is where the theory input is explicit: "The uncertainty in the soft term is
assumed to be dominated by how well it is modelled by Monte Carlo simulation," and the
uncertainty is *defined* as the maximal data-MC difference across three Z->ll generators (28).
**[A]** Fake pT^miss arises from mismeasurement, resolution effects and pile-up, and pile-up
jets can pass the jet-vertex tagger when a muon track inflates their hard-scatter score, whose
"stochastic nature degrades the pT^miss response and resolution" (28). **[A]**

So: the imbalance is measured, with quantified resolution, improved up to 30% at high pile-up
by tighter working points (28). The *interpretation* of the imbalance as an invisible particle
is a model-licensed step, and the generator-spread-defined soft-term uncertainty is a case
where a theoretical prior sets the size of an experimental error bar. Both halves of that
sentence are true and the second is the defensible critical claim.

**Step 5 -> rate, the acceptance factor.** Antoniou's analysis of the LHCb R_K measurement is
the clearest published account of the full chain: detection and reconstruction; triggering,
which cuts the rate from roughly 13 MHz to about 12.5 kHz and discards most data irretrievably;
cut-based selection guided by theoretical knowledge of the decays and backgrounds; efficiency
calculation by simulation, corrected by tag-and-probe on calibration data; maximum-likelihood
fits to invariant mass distributions; and uncertainty assignment with systematics estimated by
varying models and parameters (29). **[A]**

His two load-bearing conclusions: **"raw data in their pure form are practically useless for
the comparison of experimental results with theory,"** and real and simulated data are combined
into the final data model and **cannot easily be separated** (29). **[A]** Theory enters at
three levels - general physical principles, the physics of particle-detector interaction, and
the specific aims of the experiment (29). **[A]**

The efficiency factor is the step that cannot be purified. A yield becomes a branching fraction
only by division by an acceptance computed under a hypothesis about the signal's kinematics.
When the hypothesis is the thing being tested, the circularity is real; the field's mitigations
are blind analysis and explicit uncertainty inclusion, which Antoniou judges to make the
theory-ladenness non-vicious rather than absent (29). **[A]**

The trigger step is prior-laden and irreversible, and is treated in this archive's
`03_hardware_systems/trigger_data_destruction_v1.md`; it is not re-litigated here.

### Resonance peaks as inference of particle existence

The sharpest available case study is one the field produced itself. The 750 GeV diphoton excess
was reported in December 2015 at **3.9 sigma local (ATLAS) and 3.4 sigma local (CMS)**, which
after accounting for the mass range searched fell to **2.1 sigma and 1.6 sigma global** (30)(31).
**[A]** About **500 theoretical papers** appeared between the December 2015 and August 2016
results (31). **[A]** More data showed it was a fluctuation, and a Bayesian analysis that found
"substantial" evidence for it on the 2015 data became evidence against it with 2016 data
included (31). **[A]**

Hooper's reading is the one to carry forward: declaring a discovery is a social judgement, not a
mechanical threshold, and the textbook view that 5 sigma equals discovery **"does not hold up
to historical scrutiny"** (30). **[A]** He notes DAMA's annual modulation quoted at 8.9 sigma
is not regarded as a dark matter detection, and argues the LHC's search volume justifies a
trials factor near 10^4, which would make a 750-GeV-like anomaly roughly a 5% occurrence (30).
**[A]** His contrast with the Higgs is explicit: both ATLAS and CMS reported about 5 sigma in
2012 and it was immediately treated as a discovery, which he attributes **mainly to the strong
prior expectation** that the LHC would find a Higgs-like boson, an expectation with no analogue
at 750 GeV (30). **[A]**

This cuts both ways and must be reported that way. The prior-dependence of discovery
declaration is real and a named physicist in the field says so in print. And the 750 GeV
episode is simultaneously the best evidence available that the system is not fabricating
results: the field published a bump, 500 theorists built on it, and the collaborations killed
it with more data.

### How much of "we observed particle X" is observation

Maettig and Stoeltzner's questionnaire and interview study of LHC physicists found that after
the 2012 announcement physicists first treated the object as **"a" Higgs boson**, and that
calling it the SM Higgs required precision property measurements that were then still marginal
(32). **[A]** They also note the 5 sigma threshold is explicitly conventional - "By convention
in particle physics" - with different thresholds for evidence, observation and exclusion (32).
**[A]** They nonetheless defend the discovery as a crucial experiment in an appropriate sense,
arguing that locating the LHC within the tradition of earlier precision experiments keeps
Duhemian underdetermination at bay (32). **[A]**

A defensible decomposition of "we observed the Higgs boson," as of 2026:

- *Observed*: an excess of events at 125.11 +/- 0.11 GeV in diphoton and four-lepton invariant
  mass, in two independently designed detectors, reproduced in five decay channels at 10%
  precision (18)(19). **[A]**
- *Inferred with high confidence*: that the excess is a single narrow scalar resonance coupling
  to W, Z, t, b and tau with SM-proportional strengths, kappa_V = 1.002 +/- 0.027 (20). **[A]**
- *Assumed, or at best weakly constrained*: that its potential has the SM shape. The
  self-coupling is bounded only to -1.2 < kappa_lambda < 7.5 (21). **[A]** The statement "the
  Higgs mechanism as described in the SM is confirmed" is therefore stronger than the data on
  the single parameter that defines the mechanism's shape. **[C]** It rests on the self-coupling
  and charm-coupling bounds above and would be falsified by an HL-LHC self-coupling measurement
  landing on kappa_lambda = 1.

### The field's own statement that its results are published model-dependently

The LHC reinterpretation report is explicit: **"Reinterpretation is only possible with the
provision of detailed analysis information by the experiments"**; two-dimensional exclusion
lines are not useful for reinterpretation because they encode one model's assumptions; when
combined results are shown "the relative contribution of each topology or final state is fixed
and cannot be varied"; and some analyses, especially ML-based ones, **cannot currently be
reproduced outside the collaborations** (37). **[A]** Simplified models cannot capture the full
phenomenology of UV-complete models, and when a signal spreads across many channels the derived
limits "tend to be highly conservative and often far too weak" (37). **[A]**

This is the single most important Tier A fact in the audit. The published form of an LHC
exclusion is a statement about a simplified model, not about nature, and the community that
produces them says so in a joint report with a list of what would have to be published for the
results to be reusable.

---

## Part 3 - Theory-ladenness of observation: strongest version, strongest reply

### The strongest version of the argument

The classical form is Hanson's claim **"that seeing is a theory laden undertaking,"** extended
by later writers to instrument-generated data such as thermometer readings (34). **[A]** Kuhn
and Feyerabend sharpened it: observations and experimental results are already part of a
theoretical framework, so they cannot confirm that framework independently, and no
theory-neutral observation language exists (33)(34). **[A]** Kuhn drew on the Bruner and Postman
card experiment, in which subjects "saw" a black four of hearts as red (34). **[A]**

Applied to this field, the strong version has three distinct limbs, and they are not equally
strong.

1. **Pickering's contingency thesis.** High-energy physics "could have developed in... a
   nonquarky way" and been equally successful; Hacking's summary is that the outcome was "not
   fully predetermined" by the world, technology, or social practice (33). **[A]**
2. **Galison's selection thesis.** Theory determines what counts as a real effect and what
   counts as background; his muon example shows how the Oppenheimer-Carlson calculation changed
   which phenomenon was treated as unexplained (33). **[A]** This is the limb that transfers
   most directly to trigger menus and analysis cuts.
3. **Antoniou's inseparability thesis**, the strongest *contemporary* version because it is
   derived from a current experiment rather than a historical case: real and simulated data are
   combined into the final data model and cannot easily be separated (29). **[A]** Morrison
   reinforces it from the other side: the Higgs results **logically** depend on simulations used
   in data analysis and **causally** depend on simulations used to design the detectors (35).
   **[A]**

Limb 3 is where a serious critique of this field should live. Limb 2 is correct and bounded.
Limb 1 is the weakest, and should not be leaned on.

### The strongest reply

- **Data versus phenomena.** Bogen and Woodward: raw data are idiosyncratic and shaped by
  irregular causal factors, so theories rarely predict individual data points; investigators
  use data to infer facts about *phenomena*, which are regular enough for systematic prediction,
  and theories are tested against those (34). **[A]** This dissolves much of the force of
  "observation is theory-laden," because the test is not against observation reports.
- **Assuming a theory is not always vicious.** Laymon argues the Michelson-Morley experiments
  did not depend on the theory under test; Woodward argues the same for Millikan's oil drop
  experiment (34). **[A]**
- **Theory-ladenness comes in degrees.** Karaca's position, cited in both SEP entries, is that
  theory-ladenness varies across different parts of a theory - which converts the issue from a
  blanket objection into an empirical question to be settled case by case (33). **[A]**
- **Robustness and intervention.** Hacking: observations stay robust across changes in apparatus
  theory, and intervention strengthens belief in apparatus and observation together (33). **[A]**
  Galison concedes that instruments can keep the same readings after a theory change (33). **[A]**
- **The world constrains outcomes.** The standard rationalist reply to Pickering is that no
  successful theory of light could yield a different speed of light; Weinberg's remark is that
  "no mountaineer would ever name a book Constructing Everest" (33). **[A]**
- **Morrison, who establishes the dependence, is not a sceptic about the result**, partly because
  test runs of the apparatus gave data for an independent check on the simulations (35). **[A]**
- **The decisive empirical reply.** Three inputs produce nine hadron masses to 1-3% (24);
  R = 11/3 rather than 11/9 supplies the factor of three for colour (26); alpha^-1 agrees to
  10^-9-10^-7 across caesium recoil, rubidium recoil, the quantum Hall effect and the electron
  g-2 (4). A contingency thesis has to explain that convergence, and no version of it attempts
  to. **[C]** Falsified by: a demonstration that any of these agreements is an artefact of shared
  calibration, which would require shared physical dependence between apparatus that have none.

### Where this leaves the audit

The defensible position is the one both SEP entries converge on: theory-ladenness in this field
is **pervasive, acknowledged, mostly correctable, and concentrated in identifiable steps** -
acceptance and efficiency factors, trigger and selection priors, and the object-to-entity
mapping. The indefensible position is that it is global and vitiating. The useful critical
question is not "is observation theory-laden" but "is the theory-ladenness *accounted for* in
the uncertainty budget, and are the correlations between experiments that share generators and
PDFs treated correctly" - which is a question with an answer, and which the reinterpretation
report (37) and Junk and Lyons (36) both show the field has only partially addressed. **[C]**

---

## Part 4 - Competing frameworks, status-rated

Ratings: **alive** (viable, testable, actively constrained), **constrained** (surviving only in
corners of parameter space, or surviving at the cost of its original motivation), **effectively
dead** (its characteristic predictions are excluded), **untestable** (no foreseeable experiment
discriminates).

### Technicolor (original, QCD-like) - EFFECTIVELY DEAD

*Claims*: electroweak symmetry breaking by a new strong gauge interaction, with no elementary
Higgs; condensing technifermions give W and Z their masses; extended technicolor gives quarks
and leptons theirs (38).

*Tests and outcomes*: the S parameter estimated in QCD-like technicolor is "significantly
greater than the experimentally allowed value"; ETC interactions induce mu->e gamma and
K_L->mu e unless Lambda_ETC exceeds roughly 1000 TeV, or 10^4 TeV with CP violation; and
technipions are then at most a few GeV, conflicting with LEP searches at the Z (38). **[A]**
The 125 GeV scalar is the finishing blow - technicolor does not generically predict a boson
that light, and "the original models are largely ruled out" (38). **[A]**

Do not present this as a live contender.

### Composite Higgs / walking and conformal technicolor / strong-dynamics EWSB - CONSTRAINED

*Claims*: the 125 GeV scalar is a composite pseudo-Nambu-Goldstone boson of a new strong sector
with decay constant f.

*Status*: viable, and naturalness requires f below O(TeV) (40). **[A]** The measured
kappa_V = 1.002 +/- 0.027 (20) already pushes f up; HL-LHC projections reach f >~ 2 TeV and a
future collider f >~ 6 TeV (40). **[A]**

Lattice results are the honest discriminator and they are not encouraging. SU(4) with 2
fundamental + 2 sextet fermions sits deep in the chirally broken phase and is "likely ruled out
as a realistic model for composite-Higgs and top partial compositeness"; SU(4) with 4+4 appears
IR-conformal but its chimera-baryon anomalous dimension is about 0.5 against a
phenomenologically preferred value of about 2; Sp(4) has only quenched results; and for SU(3)
with N_f = 8 the conformal status is "not fully confirmed yet" (39). **[A]** The reviewer's own
bottom line is that no realistic composite model has been confirmed (39). **[A]** It is also
noted that no string-derived composite Higgs model exists (40). **[A]**

Verdict: a live research programme with no realised model. That is a weaker position than its
presence in collider-physics motivation documents suggests.

### Preon models / quark and lepton compositeness - EFFECTIVELY DEAD at accessible scales

PDG 2025: dijet contact-interaction limits put Lambda above 9.2-29.5 TeV depending on model;
CMS inclusive-jet plus HERA SMEFT gives Lambda^-_LL > 24 TeV; Drell-Yan llqq limits are
Lambda > 23.9-36.4 TeV; excited quarks are excluded to **6.7 TeV** (ATLAS dijet) and 6.3 TeV
(CMS); excited electrons to 5.6 TeV, muons to 5.7 TeV, taus to 4.7 TeV (42). **[A]** "Over a
wide range of chi and dijet mass the data are well described by the SM predictions" (42). **[A]**

A compositeness scale above about 30 TeV is beyond any approved machine. The framework is not
logically dead; it is dead as a near-term experimental proposition, and new preon papers
continue to appear without a route to test. Treat as **untestable** in practice.

### Supersymmetry - SPLIT VERDICT, and this is the honest one

The split matters because conflating the two halves is how both sides of this argument go wrong.

*SUSY as a framework*: **alive and partly untestable.** Constantin, Kraml and Mahmoudi argue
directly that the LHC has not ruled out SUSY, and they are specific. Simplified-model limits
reach about **2.4 TeV for gluinos and first/second-generation squarks, about 1.3 TeV for stops
and sbottoms, and about 1 TeV for electroweakinos** - but these assume only two or three new
particles with simple decays (41). **[A]** In the pMSSM, **gluinos as light as about 1 TeV and
stops as light as about 400 GeV remain viable**, and a combined SModelS likelihood analysis
excludes only a small region of electroweakino parameter space (41). **[A]** High-scale SUSY
remains possible, so no currently feasible collider can rule out SUSY entirely (41). **[A]**

*SUSY as the solution to naturalness*: **failing on its own terms.** The authors note the Higgs
sector tension directly - reaching 125 GeV in the MSSM requires either a stop scale around
3 TeV or more, or large stop mixing, which **conflicts with the naturalness motivation for
light stops** (41). **[A]** The surviving sharp prediction is higgsinos with mu <~ 200-400 GeV
(41). **[A]** That is a testable, falsifiable, narrow claim, and it is the right thing to hold
the programme to.

The authors also report small consistent excesses in soft-dilepton and monojet searches which
could hint at light electroweakinos but need Run 3 data (41). **[B]** Named advocates: Baer
et al. on electroweak fine-tuning versus the hierarchy problem, cited approvingly in (41);
against, the large body of "LHC has ruled out SUSY" commentary the paper's title responds to.

### Large extra dimensions (ADD) - EFFECTIVELY DEAD in the TeV-gravity form

PDG 2025: ADD with six extra dimensions is excluded below **M_D = 9.4 TeV** from quantum
black hole thresholds in ATLAS dijets at 139 fb^-1, with 9.2 TeV from lepton+jet and 8.2 TeV
from CMS dijet angular distributions; and the radius is bounded at **R < 37 micrometres** for
delta = 2 from torsion-pendulum experiments (43). **[A]**

The original motivation was to put the fundamental Planck scale at about a TeV so that the
hierarchy problem dissolves. Nine-plus TeV removes that motivation.

### Warped extra dimensions (Randall-Sundrum) - CONSTRAINED

RS1 with k/M_P = 0.1: the lightest KK graviton is excluded below **4.8 TeV** (CMS diphoton,
138 fb^-1), with a similar 4.78 TeV from dilepton (43). **[A]** The framework survives in
variants with smaller curvature or different localisation, which is a weaker form of survival
than it is usually presented as.

### Asymptotic safety - ALIVE, CONTESTED, NOT CURRENTLY TESTABLE

*Claim*: gravity is non-perturbatively renormalisable at an ultraviolet fixed point.

Donoghue's critique is the serious opposition and must be cited whenever the programme is
described as established. His objections: the running G(k) and Lambda(k) are "incomplete"
couplings whose k-dependence disappears once contributions below k are restored; power-law
corrections depend on Mandelstam variables with differing signs so no single G(E) describes all
processes; gravitational corrections mostly generate new higher-derivative operators rather
than renormalising G; the running originates in heat-kernel coefficients corresponding to
tadpole diagrams with no external momentum flow, which vanish in dimensional regularisation for
massless particles; and the one-loop curvature-squared truncation yields a spin-zero tachyon and
a spin-two ghost whose propagator pole obstructs Euclidean-to-Lorentzian continuation (44).
**[B]**

His own summary of the evidential situation: "The existence of a Euclidean UV fixed point is not
sufficient by itself"; he does not claim the fixed point is ruled out (44). **[B]** Advocates on
the other side are the functional-renormalisation-group community whose reviews report fixed
points across truncations. This is a genuine Tier B dispute with no experimental discriminant.

### MOND and modified gravity versus particle dark matter - MOND: ALIVE AS GALAXY PHENOMENOLOGY, EFFECTIVELY DEAD AS A REPLACEMENT

Famaey and Durakovic, writing as MOND's own expositors, are the right source because they
concede what matters.

*Successes*, which should not be understated: flat rotation curves follow from the baryonic
distribution alone; the baryonic Tully-Fisher relation is one of the tightest astrophysical
relations with intrinsic scatter about **6%**; the radial acceleration relation extends to
ellipticals and to weak lensing at very low accelerations; and the inner shape of rotation
curves depends on baryonic surface density as MOND predicts (45). **[A]**

*Failures, in their own words*: **"the apparent failure of MOND is most evident in galaxy
clusters,"** where a residual missing-mass problem roughly comparable to the observed baryonic
mass remains; for the Bullet Cluster, a relativistic theory reducing to AQUAL or QUMOND in the
quasi-static limit "is not sufficient"; Cassini tracking of the quadrupole anomaly disfavours the
simplest interpolating functions; ultra-faint Milky Way satellites appear too dark-matter
dominated for MOND; pure MOND is "mostly mute on cosmology"; and **TeVeS "has thus been ruled
out after GW170817"** because its tensor-mode speed generically differs from c (45). **[A]**
AeST can reproduce the CMB angular power spectrum for some choices of its free function (45).
**[B]**

*Particle dark matter*: the evidence for a non-baryonic gravitating component is strong and
multiply sourced, and a current community assessment treats dark matter as "established by
multiple independent datasets" (61). **[A]** The *WIMP* in particular is heavily constrained:
LZ's 4.2 tonne-year exposure gives a spin-independent limit of **2.1 x 10^-48 cm^2 at
36 GeV/c^2** with no excess over background and a best-fit WIMP count of zero at all tested
masses (54). **[A]**

The correct rating is therefore asymmetric and both halves must be reported: the dark matter
*inference* is robust; the WIMP *candidate* is in serious trouble; MOND works where dark matter
is least needed and fails where it is most needed.

### Axions - ALIVE, BEST-MOTIVATED, UNDETECTED

PDG 2025: the neutron EDM bound |d_n| < 1.8 x 10^-26 e cm implies |theta-bar| <~ 10^-10, which
is the fine-tuning the Peccei-Quinn mechanism addresses (46). **[A]** The QCD axion window is
bounded below by black hole superradiance at roughly 10^-11 eV and above by neutron star
cooling at roughly 15-30 meV (46). **[A]** ADMX and CAPP have reached DFSZ-benchmark sensitivity
over much of the 2.7-4.91 microeV range; CAST gives |g_a gamma gamma| < 5.8 x 10^-11 GeV^-1;
globular cluster R2 data give < 4.7 x 10^-11 GeV^-1; SN 1987A implies f_a above about
4 x 10^8 GeV (46). **[A]** **No detection.** The review reports only exclusion limits, with a
few weak hints - marginal non-standard stellar cooling, a small tip-of-the-red-giant-branch
extra-cooling hint, pulsar spectral irregularities that are in tension with CAST (46). **[A]**

Axions are the best-rated item in this section: a sharp motivation, a defined target window,
instruments now inside the theoretically preferred band, and no detection. That is what a
healthy open question looks like.

### Sterile neutrinos - eV-SCALE 3+1: EFFECTIVELY DEAD AS AN ANOMALY EXPLANATION; HEAVIER: ALIVE

MicroBooNE excludes MiniBooNE's entire 2.3 sigma preferred region in the full three-dimensional
3+1 parameter space at greater than that confidence, rising to 2.4 sigma with PROSPECT included;
at delta m^2_41 = 0.41 eV^2, MiniBooNE's entire 4 sigma region is excluded with PROSPECT (47).
**[A]** The authors note that apparent compatibility between experiments in the standard
profiled projection is an artefact of a degeneracy between nu_mu -> nu_e appearance and nu_e
disappearance caused by the beam's intrinsic 0.5% nu_e component (47). **[A]** SBND and ICARUS
at 6.6 x 10^20 POT could cover MiniBooNE's entire 3 sigma region at more than 3 sigma (47). **[A]**

KATRIN excludes the gallium anomaly's best-fit sterile neutrino at **96.6%** confidence, and the
community reading is "two strikes, and you're out" (48). **[A]**

But the gallium deficit itself - about 20%, confirmed by BEST in 2022 - **remains statistically
strong at more than five sigma even under conservative assumptions about nuclear cross sections
and systematics, and is still unexplained** (48). **[A]** That is the honest position: the
*explanation* is dead, the *anomaly* is not. Heavier sterile neutrinos remain a motivated
possibility (48). **[A]**

### Serious alternatives to the quark model - NONE

There is no framework in the refereed literature that replaces quarks and reproduces Bjorken
scaling, the neutrino-antineutrino cross-section ratio, the 5/18 rule, R = 11/3, and the lattice
hadron spectrum. **[C]** This rests on the evidence assembled in (24)(25)(26) and on the absence
of any such construction in the primary literature; it would be falsified by one paper that did
the arithmetic. Claims that quarks do not exist appear only outside the refereed literature and
are assessed in Part 6.

---

## Part 5 - Live anomalies, with those that have dissolved marked as such

### Muon g-2 and the hadronic vacuum polarisation dispute - DISPLACED, NOT RESOLVED

The headline is that the anomaly is gone: experiment 116 592 071.5(14.5) x 10^-11 against WP25
theory 116 592 033(62) x 10^-11, a difference of 38(63) x 10^-11, about 0.6 sigma (6)(7). **[A]**

What actually happened is more interesting and is the correct thing to record. WP25 **switched
the leading-order HVP from the data-driven dispersive method to a lattice QCD average**, and
the two white papers are **statistically incompatible at about three standard deviations** (8).
**[A]** WP25 adopts a lattice LO HVP of 7132(61) x 10^-11 and a combined total LO HVP of
7045(61) x 10^-11 (7). **[A]**

The reason for the switch is a breakdown on the data side, which the Theory Initiative states
plainly: the CMD-3 measurement of e+e- -> pi+pi- "increased the tensions among data-driven
dispersive evaluations" to the point where it is **"impossible to combine the results in a
meaningful way"** (6). **[A]** KLOE and CMD-3 are incompatible at the **5 sigma** level (10).
**[A]** BMW/DMZ's lattice HVP reaches 0.45% total uncertainty, Mainz and RBC/UKQCD independently
confirm it with larger errors, and the intermediate window (0.4-1.0 fm) is where data-driven
tension is greatest and where lattice groups agree with each other (11). **[A]**

Named advocates. Zoltan Fodor (BMW) argues the 0.9 sigma agreement between experiment and
lattice has probably postponed the discovery of new physics here (10). **[B]** Aida El-Khadra,
Theory Initiative chair, says puzzles in the e+e- data still block a new data-driven prediction
and that "we are confident we will soon know what the data-driven method has to say about HVP"
(8). **[B]** Alex Keshavarzi, who works on both the experiment and the Theory Initiative, states
that **"the origin of the CMD-3 tension remains unknown"** and poses the open question directly:
"Why do lattice QCD and CMD-3 agree, while both conflict with decades of experimental data?"
(9). **[B]** CERN Courier's summary - the anomaly is "severely undermined, but not yet
definitively resolved" - is the fair one (8). **[A]**

Audit verdict: this is not an anomaly that was explained. It is an anomaly that was **relocated
into an unexplained conflict between two classes of hadronic input**, with a 5 sigma
experimental inconsistency at its centre. Reporting it as "resolved" overstates; reporting it as
"still a 5 sigma new-physics signal" also overstates. Both errors are common.

### CDF-II W mass - A MEASUREMENT DISPUTE, NOT EVIDENCE OF NEW PHYSICS

CDF-II reported 80433.5 +/- 9.4 MeV (14). PDG **excludes it from the world average**, and states
the arithmetic: including it gives a compatibility probability of **0.5%**, so the combination is
"disfavoured," whereas removing it gives **91%** (14). **[A]** CMS's 80360.2 +/- 9.9 MeV
explicitly disagrees with CDF, by about 73 MeV, while agreeing with the SM (15). **[A]**

The dedicated status review quantifies it further: CDF sits **4.6 sigma from the SM expectation,
7.2 sigma using CDF's published uncertainties, and about 3.6 sigma from the other hadron-collider
measurements**; the earlier CDF result is compatible with the new one only at the few-percent
level, with the discrepancy driven mainly by the muon channel (16). **[A]** In Gfitter, including
CDF collapses the global fit from chi^2/dof = 16.62/15 (p = 0.34) to **62.6/15 (p = 8.9 x 10^-8)**,
with CDF differing from the indirect prediction by 6.8 sigma and the fit then demanding
m_t = 184.2 +/- 1.7 GeV (17). **[A]**

The review's own framing is that this is an unresolved tension rather than a simple outlier: new
physics is hard to reconcile with the rest of the data, and modelling errors are unlikely since
the same modelling was applied across experiments, so it "might be resolved only by new
measurements or an independent reanalysis" of the CDF dataset, with background modelling the
exception not covered by that argument (16). **[A]**

Audit verdict: a single-experiment result in irreducible conflict with four others and with the
global fit. It is **real as a measurement disagreement and dead as a new-physics signal**, and
the honest critical point is not about the physics but about the governance - an unresolvable
dispute over a decade-old dataset from a decommissioned detector is a structural auditability
problem, and the field's own proposed remedy is an independent reanalysis that has not happened.
**[C]** Falsified by: a published independent reanalysis of the CDF-II dataset.

### B-meson anomalies - R(K) DISSOLVED; b->s mu mu PARTLY SURVIVING

**R(K) and R(K*): dissolved, and the cause is identified.** The 2022 LHCb measurements show
overall agreement with the SM at **0.2 standard deviations**, against the earlier 3.1 sigma
evidence for lepton universality violation (59). **[A]** The collaboration attributes the shift
to **tighter electron identification criteria and better modelling of residual misidentified
hadronic backgrounds**, with statistical fluctuation contributing less because the same data
were reused (59). **[A]**

This is the single most important calibrating fact in Part 5, and it cuts against this archive's
own premise. A 3.1 sigma anomaly that generated a large theory literature was removed by the
*same collaboration* reanalysing the *same data* with better background modelling, and the
collaboration published the reason. A field that does this is not structurally incapable of
self-correction.

**b -> s mu mu angular observables and branching fractions: surviving, with hadronic
explanations gaining.** P5' is a long-standing anomaly that LHCb has confirmed, and new results
hint at a non-zero S7 (60). **[B]** The authors' position is that a non-zero S7 **cannot be
explained by heavy new physics** and requires a sizeable hadronic contribution carrying a strong
phase, and that under plausible assumptions that same hadronic effect is about the right size to
account for P5' (60). **[B]** They do not claim new physics is ruled out, and a combined fit of
hadronic parameters and Wilson coefficients retains sensitivity and gives strong bounds on the
imaginary parts (60). **[B]**

### Neutrino masses - ESTABLISHED; ABSOLUTE SCALE UNKNOWN; A REAL COSMOLOGY TENSION

Direct kinematic bound: KATRIN's 0.45 eV (49). **[A]** Majorana nature: KamLAND-Zen's complete
dataset gives a 136-Xe 0 nu beta beta half-life limit of **3.8 x 10^26 yr** at 90% CL, an
effective Majorana mass limit of **28-122 meV** depending on nuclear matrix elements, with a
best-fit signal of **zero events** (50). **[A]**

Cosmology is where it gets interesting and should not be smoothed over. DESI's published limits
are < 0.064 eV in LCDM and < 0.16 eV in dynamical dark energy models; a joint analysis of DESI
DR2 with DES-Y5 and DES-Y1 in w0waCDM with free N_eff reports a **positive neutrino mass at
about 2.7 sigma**, sum m_nu = 0.098 +0.016/-0.037 eV, a result that depends on the weak lensing
data and on freeing N_eff and that **disappears if DES-Y1 is dropped or DES-Y5 is swapped for
Pantheon+** (53). **[B]** The same paper records DESI's finding that in an unphysical
negative-mass extension most cosmological data prefer a negative total mass, creating a tension
of up to about **3 sigma with oscillation results**, which dynamical dark energy can relieve
(53). **[B]**

Audit verdict: oscillation requires sum m_nu >~ 0.06 eV (normal) or >~ 0.10 eV (inverted) (53);
the tightest LCDM cosmological bound is 0.064 eV. The two are at the edge of compatibility and
the resolution depends on the dark energy model. This is a genuine live tension between two
independent lines of evidence and it is under-advertised relative to muon g-2.

### Strong CP problem - A REAL UNEXPLAINED FINE-TUNING, NOT A DATA ANOMALY

|theta-bar| <~ 10^-10 from |d_n| < 1.8 x 10^-26 e cm (46). **[A]** There is no measurement in
conflict with the SM here. There is a dimensionless parameter the SM permits to be O(1) and
nature has set to within 10^-10 of zero, with no mechanism in the SM to explain it. It belongs
in a different category from g-2 or the W mass, and conflating the categories is a common error
in both directions.

### Baryon asymmetry - A REAL SHORTFALL, WITH A CONTESTED CLAIM AGAINST IT

Observed baryon-to-entropy ratio Y_B = (8.718 +/- 0.004) x 10^-11 (51). **[A]** Electroweak
baryogenesis with SM CP violation yields an asymmetry about **ten orders of magnitude smaller**
than the measured value (51). **[A]** A current community assessment states flatly that "the
baryon asymmetry requires new ingredients beyond the minimal SM" (61). **[A]**

The contested claim: Elor, Houtz, Ipek and Ulloa argue that SM CP violation *is* enough, via
"Mesogenesis with a Morphing Mediator," in which a mediator's temperature-dependent mass
enhances baryon production so that CP violation in neutral B-meson oscillations generates the
whole asymmetry, with a possible pulsar-timing-array gravitational wave signature (51). **[B]**
Note carefully what this does and does not establish: the mediator is new physics. The claim is
that no new *source of CP violation* is needed, not that the SM alone suffices. The ten-order
shortfall for SM-only electroweak baryogenesis stands.

### Dark matter and dark energy - INFERRED STRONGLY, IDENTIFIED NOT AT ALL

Dark matter: covered in Part 4. LZ's null result at 2.1 x 10^-48 cm^2 (54). **[A]**

Dark energy: DESI DR2 BAO plus CMB prefers w0 > -1 and wa < 0 over LCDM at **3.1 sigma**, rising
to **2.8-4.2 sigma** with supernovae depending on the sample (52). **[A]** All eleven dataset
combinations prefer the same direction (52). **[A]** The collaboration's own caveats are
explicit and should be carried with the number: the conclusion holds "unless there is an unknown
systematic error associated with one or more datasets"; the BAO-CMB tension in LCDM alone is
only 2.3 sigma, dropping to 2.0 sigma without CMB lensing; the preferred w0 and wa depend
strongly on which supernova sample is used; and the Lyman-alpha BAO carries an added 0.3%
theoretical systematic reflecting disagreement among theory studies (52). **[A]**

Audit verdict: the strongest *current* evidence for physics beyond the minimal framework is in
cosmology, not at colliders, and it is at 3-4 sigma with acknowledged sample dependence. That
ordering deserves more weight than it usually gets in collider-motivation documents.

---

## Part 6 - Fringe claims, assessed and rejected

These are handled explicitly because ignoring them leaves them standing. Each is named, its
strongest form stated, and the specific evidence that defeats it given. **None of these is a
live alternative to anything in Parts 1-5, and none should be cited in this archive except as a
rejected claim.**

### Plasma cosmology (Alfven, Lerner) - REJECTED on five independent quantitative grounds

Wright's point-by-point refutation supplies the arithmetic (55). **[A]**

1. **CMB spectrum.** Lerner's fit has two effectively free parameters; it was a passable fit to
   the 1994 FIRAS points but is **about 6 standard deviations from the improved Fixsen et al.
   (1996) data**, and refitting changes chi^2 by only 0.7 for two new degrees of freedom - worse
   than an average random model. Current spectral-distortion limits are about **100 times
   tighter** than when the model was written.
2. **Helium versus metals.** Observations show about 3.2 g of helium per 1 g of heavier elements.
   Producing the Sun's 28% helium by stellar nucleosynthesis would yield about **four times** the
   observed 2% heavy-element fraction; producing 23% helium alongside the ~0.01% metals of old
   halo stars is "completely out of the question."
3. **Deuterium and lithium.** Cosmic rays show about 80 deuterium nuclei per lithium nucleus; the
   Universe has about **6 million**. Spallation origin for lithium leaves about 99.99% of the
   observed deuterium unexplained.
4. **No absorbing curtain.** The model requires >99% radio absorption toward Cygnus A, which is
   not seen; Abell 2218 shows no CMB hole with a Sunyaev-Zeldovich deficit under 1 mK; 3CRR
   sources at 0.4 < z < 0.5 would appear as about -2 mK holes in Saskatoon data and none was
   seen; and a density peak at Virgo would make absorption strongly direction-dependent whereas
   radio sources are uniform to within a few percent.
5. **Number counts.** Observed counts scale as N proportional to F_min^-1.8; the model predicts
   exponents of -1.25, or -0.83 with a nearby density peak.

Also recorded: electromagnetic forces are about **10^17 times too small** to affect the Sun's
galactic orbit (55). **[A]**

### Electric universe - REJECTED by direct measurement of the Sun's energy source

The claim that the Sun is externally electrically powered rather than fusion-powered is refuted
by the solar neutrino flux, which is a direct observation of the fusion reactions themselves.
Borexino measured, with a single detector: pp neutrinos at (6.1 +/- 0.5 +0.3/-0.5) x 10^10
cm^-2 s^-1; 7-Be at (4.99 +/- 0.11 +0.06/-0.08) x 10^9; pep at (1.27 +/- 0.19 +0.08/-0.12) x 10^8;
8-B at (5.68 +0.39/-0.41) x 10^6; and **CNO-cycle neutrinos at (7.0 +3.0/-2.0) x 10^8** (56).
**[A]**

That last one is decisive. The CNO cycle is a specific catalytic nuclear reaction sequence; its
neutrinos were detected at the predicted flux. No electrical model predicts a CNO neutrino flux,
and a model in which the Sun's luminosity has a non-nuclear origin has to explain why the
nuclear reaction products are present at the rate the nuclear model specifies.

### "Quarks do not exist" - REJECTED, with the specific evidence a sceptic must address

The claim takes two forms: that quarks are mathematical bookkeeping with no referent, and that
confinement is an unfalsifiable excuse for their non-observation. The evidence against both (26)
**[A]**:

- **Point-like constituents.** SLAC deep inelastic scattering: counting rates at large momentum
  transfer far above elastic predictions, and F_2 depending only on x and not on Q^2 at fixed
  x = 0.25. Bjorken scaling means the constituents cannot be resolved as extended objects.
- **Spin one-half.** Neutrino scattering: a (1-y)^2 angular distribution for antineutrinos
  against a flat one for neutrinos; and sigma/sigma-bar about 2 rather than the naive 3, which
  requires a sea antiquark fraction of roughly 20%.
- **Fractional charge.** Dividing the electron data by **5/18** brings the neutrino and electron
  F_2 data into agreement - a quantitative prediction of the fractional-charge assignment with
  no free parameter.
- **Momentum not carried by quarks.** Average momentum fraction x-bar ~ 0.43 implies about half
  the nucleon momentum is carried by something else, which the model names as gluons and which
  was then found.
- **Three colours.** R = sigma(hadrons)/sigma(mu mu) above the b-bbar threshold would be 11/9
  without colour; the measured value is **11/3**, a factor of exactly three. Independently, W
  leptonic branching fractions of 11% each close to 100% only if each quark flavour comes in
  three colours.
- **Gluon spin.** TASSO determined J = 1 for the gluon from three-jet angular correlations.
- **Ab initio spectrum.** Nine hadron masses from three inputs to 1-3% (24).
- **One quark seen before hadronisation.** PDG notes the top quark decays while still effectively
  free because its lifetime is shorter than the hadronisation time (25).

On confinement: PDG states **"Experiments have produced no evidence for free propagating
quarks,"** and that QCD predicts exactly this (25). **[A]** The honest caveat, which should be
recorded rather than suppressed: **confinement has no rigorous proof. Yang-Mills existence and
the mass gap remains an unsolved Clay Millennium Problem, and the Clay statement is that
experiments and computer simulations suggest a mass gap exists but "no proof of this property
is known"** (62). **[A]** That is a genuine gap in the mathematical foundations. It is not
evidence that quarks are unreal, because the absence of a proof of a mechanism does not
weaken the nine quantitative results above - which is what any sceptic has to defeat, and what
none has attempted.

A representative example of the claim in circulation is Santilli's general-physics preprint
arguing that both quarks and neutrinos are untenable conjectures, with the neutrino rejected
"due to lack of energy" in beta decay and replaced by an "etherino" (58). **REJECTED.** Neutrinos
have been directly detected for seventy years, their flavour oscillations measured to 6-15%
(23), their solar fluxes measured species by species including the CNO cycle (56), and their
absolute mass bounded at 0.45 eV (49). An argument that the neutrino does not exist is not a
competing hypothesis; it is a claim contradicted by direct detection in multiple independent
experiments.

### Unzicker's claims, separated and individually assessed

The claims in *The Higgs Fake*, as his publisher states them, are (57): the Standard Model "has
grown unbelievably complicated"; the complexity of the data analysis means **no one can oversee
it**; consensus rests on blind faith in experts, group-think and parroting; particle physics
since 1930 is "a futile enterprise in its entirety"; and the Nobel Committee was fooled.

These are not of equal quality and lumping them together is how the one defensible observation
gets discarded along with the rest.

- **"No one can oversee the analysis": PARTLY SUPPORTED, and this is the one with substance.**
  The field says the same thing in its own documents. The LHC reinterpretation report states
  that some analyses, especially ML-based ones, cannot currently be reproduced outside the
  collaborations, and lists the information that would be needed (37). **[A]** Junk and Lyons
  note that external reproduction is hard because of analysis complexity, detector complexity,
  expert effort required, and the need for collaboration approval (36). **[A]** The correct
  conclusion is **auditability**, not falsity - and Unzicker does not draw it; he draws the
  falsity conclusion, which the next item refutes.
- **"Particle physics since 1930 is futile in its entirety": REJECTED.** A fifteen-digit
  measurement matched by theory to 10^-12 (1)(2); the Z mass to 2.2 x 10^-5 (13); nine hadron
  masses from three inputs (24); neutrino oscillation parameters to 6-15% (23). The claim is not
  arguable against these numbers.
- **"The Higgs is fake" / the Nobel Committee was fooled: REJECTED.** The state is seen at
  125.11 +/- 0.11 GeV (18), in five decay channels at 10% precision (19), in two detectors of
  independent design, with kappa_V = 1.002 +/- 0.027 (20) and p_SM = 77-78% (20).
- **"The SM is unbelievably complicated": NOT A PHYSICS CLAIM.** The SM's roughly nineteen free
  parameters are a real criticism of its explanatory economy, and the field makes the same
  criticism when it motivates unification. Parameter count is not an argument about empirical
  adequacy, and treating it as one is a category error.

### "Collider results are fabricated or circular artefacts" - REJECTED

The specific mechanisms that defeat this, with their honest limits.

*Against fabrication and circularity*: blind analysis, with procedures fixed before the signal
region is viewed and precision measurements using a hidden offset removed only at unblinding
(36) **[A]**; internal working-group review and staged approval (36) **[A]**; multiple detectors
of independent design, with high-profile results announced by competing collaborations (36)
**[A]**; calibration anchored on quantities established elsewhere - single-particle test-beam
response and in-data pT balance for the jet energy scale (27), and a 0.3% energy scale as the
result **[A]**; published likelihoods on HEPData, Rivet routines, and preservation efforts (36)
**[A]**; and a 5 sigma threshold with pre-registered criteria (36) **[A]**.

*The strongest single piece of counter-evidence* is the record itself. The 750 GeV excess was
published, built on by about 500 papers, and then killed by the same collaborations with more
data (31). The R(K) anomaly was published at 3.1 sigma and then removed by the same
collaboration reanalysing the same data with better electron identification and background
modelling, **with the reason published** (59). A fabricating system does not do either of these
things.

*The honest limits, which the field states*: reproduction only checks computation, and a flawed
analysis "contains the same flaws" when reproduced; replications using overlapping data are not
independent, and shared systematic errors make them less independent than they appear;
unrecognised systematics - "unknown unknowns" - are the most problematic; exclusion limits
carry a built-in false-exclusion rate (36). **[A]**

So the residue of the claim, after the fabrication part is discarded, is a genuine and bounded
one: **correlated systematics across experiments that share event generators, parton
distribution functions and detector-simulation frameworks are not obviously treated correctly,
and no external party is positioned to check.** That is a Tier C structural inference resting on
(36) and (37); it would be falsified by a published cross-experiment correlation treatment for
generator and PDF systematics. It is a far weaker claim than fabrication and a far stronger one,
because it might be true.

---

## Claims Examined and Not Supported

**1. "The precision of Standard Model confirmation is overstated." Not supported, and asserting
it would end the archive's credibility.** Fifteen significant figures on g/2 matched to 10^-12
(1); m_Z to 2.2 x 10^-5 (13); nine hadron masses from three inputs to 1-3% (24); global
electroweak fit p = 0.34 (17). No critique in this archive may rest on denying these.

**2. "The electron g-2 is a clean twelve-digit confirmation of QED." Overstated in the opposite
direction, and the correction matters.** The *measurement* is 0.13 ppt (1); the *test* is limited
by the imported value of alpha, whose uncertainty (0.229 x 10^-12) is twenty times the
tenth-order QED uncertainty (0.011) (2), and whose two best determinations differ from the g/2
value by 2.1 and 3.9 sigma (1). The tenth-order coefficient itself needed an independent
recomputation to resolve a 5 sigma discrepancy between two calculations (3). Both the
triumphalist and the dismissive readings are wrong.

**3. "Jets are simply assumed to be quarks." Not supported as stated.** The jet energy scale is
calibrated so that reconstructed jet energy equals the energy of the corresponding
**particle-level** jet (27), anchored on single-particle test-beam response and in-data pT
balance, to 0.3% at 300 GeV (27). The defensible claim is narrower: *parton-level unfolding is a
separate, model-dependent step, and the parton is never the object of a measurement.* Use that
form.

**4. "Missing transverse energy is invented to rescue the theory." Not supported.** It is a
measured momentum imbalance with quantified resolution, improved up to 30% at high pile-up by
working-point choice (28). What is model-licensed is the *interpretation* as an invisible
particle, and separately the soft-term uncertainty is defined by the spread across three
generators (28) - a real instance of theory input sizing an error bar, which is the claim worth
making.

**5. "The muon g-2 anomaly has been resolved." Not supported.** It has been relocated. WP20 and
WP25 are incompatible at about 3 sigma (8); the switch to lattice HVP happened because CMD-3
made data-driven combination "impossible... in a meaningful way" (6); KLOE and CMD-3 differ at
5 sigma (10); and the origin of that tension "remains unknown" (9).

**6. "The muon g-2 anomaly is still a 5 sigma signal of new physics." Also not supported.**
Against WP25 the difference is 0.6 sigma (6)(7), and independent lattice groups agree with each
other (11). Citing the 2020 comparison as current is a factual error.

**7. "The CDF-II W mass is evidence for new physics." Not supported.** PDG excludes it; inclusion
drops compatibility from 91% to 0.5% (14); CMS disagrees with it by 73 MeV while agreeing with
the SM (15); and in the global fit it forces m_t = 184.2 +/- 1.7 GeV against a measured
172.47 +/- 0.46 (17). The surviving critical point is governance - an unresolvable dispute over a
decommissioned detector's dataset with no independent reanalysis (16).

**8. "The B-meson anomalies have all evaporated." Not supported, and neither is the opposite.**
R(K) and R(K*) did dissolve, from 3.1 sigma to 0.2 sigma, with the cause published - electron
identification and misidentified-hadron background modelling (59). The b -> s mu mu angular and
branching-fraction anomalies persist, with the live dispute now being hadronic charm-loop
contributions versus new physics, and a non-zero S7 that "cannot be explained by heavy new
physics" (60).

**9. "Supersymmetry has been ruled out by the LHC." Not supported.** pMSSM-viable gluinos at
about 1 TeV and stops at about 400 GeV survive, simplified-model limits assume two or three new
particles with simple decays, and high-scale SUSY cannot be excluded by any feasible collider
(41). **The converse, "natural SUSY is alive and well," is also not supported**: a 125 GeV Higgs
in the MSSM needs a ~3 TeV stop scale or large mixing, in conflict with the naturalness
motivation for light stops (41). The testable residue is higgsinos at mu <~ 200-400 GeV (41).

**10. "Technicolor is a live alternative to the Higgs mechanism." Not supported.** S parameter
above the allowed value, ETC flavour bounds requiring 10^3-10^4 TeV, technipions too light
against LEP, and no generic prediction of a 125 GeV scalar: "the original models are largely
ruled out" (38). The surviving strong-dynamics programme has, on its own lattice evidence, no
confirmed realistic model (39).

**11. "MOND is a viable replacement for particle dark matter." Not supported, on its own
advocates' account.** Clusters are where "the apparent failure of MOND is most evident"; a
quasi-static AQUAL/QUMOND limit "is not sufficient" for the Bullet Cluster; Cassini disfavours
the simplest interpolating functions; and TeVeS "has thus been ruled out after GW170817" (45).
**The converse, "MOND has no successes," is also not supported**: the baryonic Tully-Fisher
relation has about 6% intrinsic scatter and the radial acceleration relation extends to weak
lensing (45).

**12. "Preon models and extra dimensions remain promising near-term targets." Not supported.**
Compositeness scales above 24-36 TeV and excited quarks excluded to 6.7 TeV (42); ADD M_D above
9.4 TeV with sub-37-micrometre radius limits (43); RS KK gravitons above 4.8 TeV (43). Each is
beyond the reach of any approved machine, which makes them untestable rather than promising.

**13. "Collider results are fabricated or are circular artefacts of the analysis chain." Not
supported.** Blind analysis with hidden offsets, independent detectors, test-beam and in-data
calibration to 0.3%, published likelihoods (27)(36). And the record refutes it directly: the
field published a 750 GeV bump and killed it (31), and published a 3.1 sigma R(K) anomaly and
removed it with a published reason (59). The surviving Tier C claim is about correlated
generator and PDF systematics across experiments with no external auditor (36)(37) - a different
and much stronger argument.

**14. "Quarks do not exist" / "confinement is an unfalsifiable excuse." Not supported.** Bjorken
scaling, the (1-y)^2 antineutrino distribution, the 5/18 rule, R = 11/3 against 11/9, gluon
J = 1 from TASSO, nine lattice hadron masses from three inputs, and the top quark decaying
before hadronisation (24)(25)(26). **Recorded against the field's own usual framing: confinement
has no rigorous proof, and Yang-Mills existence and the mass gap remains an open Clay Millennium
Problem, with "no proof of this property... known" (62).** That gap is real and should be stated
whenever confinement is called established; it does not transfer any support to the fringe claim.

**15. "Plasma cosmology and the electric universe are suppressed alternatives." Not supported.**
Plasma cosmology's CMB fit is 6 sigma from FIRAS, its helium-metal ratio off by a factor of four,
its deuterium-lithium ratio off by about five orders of magnitude, its required absorption holes
absent toward Cygnus A, Abell 2218 and 3CRR sources, and its number-count exponent -1.25 against
an observed -1.8 (55). The electric universe is refuted by the measured solar neutrino spectrum,
including CNO-cycle neutrinos at the predicted flux (56). These failed on evidence, not on
reception.

**16. "Santilli's dismissal of the neutrino and quark conjectures deserves a hearing on the
merits." Not supported.** It was examined (58) and it is contradicted by direct neutrino
detection, measured oscillation parameters (23), species-resolved solar fluxes (56), and the
0.45 eV mass bound (49).

**17. "The field does not acknowledge the model-dependence of its own results." Clearly false,
and the claim would discredit this stream if made.** Acknowledgement is institutional and in the
collaborations' own documents: a multi-collaboration report stating that reinterpretation is
impossible without information the experiments do not currently publish, and that ML-based
analyses cannot be reproduced externally (37); a Harvard Data Science Review paper by a Fermilab
and an Imperial physicist cataloguing the limits of reproduction and the primacy of unknown
systematics (36); ATLAS stating in print that pT^miss is "a proxy" and that its soft-term
uncertainty is assumed to be dominated by MC modelling (28); a published philosophical analysis,
built from LHCb's own procedures, concluding that real and simulated data cannot easily be
separated in the final data model (29); and a Fermilab theorist arguing in print that 5 sigma
"does not hold up to historical scrutiny" (30). The defensible critical claim is not that the
field is unaware. It is that **this acknowledgement is distributed across dozens of documents
with different audiences and has never been assembled into a single auditable accounting - and
that the two quantities which would make it auditable, a cross-experiment correlation treatment
for generator and PDF systematics and an acceptance measure over signature space, have no owner
and no publication.** **[C]** Falsified by: publication of either.

**18. "The strongest current evidence for physics beyond the Standard Model is at colliders."
Not supported.** The strongest live tensions are in cosmology - dynamical dark energy at 3.1
sigma from BAO plus CMB and 2.8-4.2 sigma with supernovae (52), and the neutrino mass
cosmology-oscillation tension at up to about 3 sigma (53) - plus the unexplained >5 sigma
gallium deficit (48). The collider sector's two headline anomalies have respectively dissolved
(59) and been reduced to a measurement dispute (14)(16). This ordering is worth carrying into
the governance stream.

---

## References

1. X. Fan, T. G. Myers, B. A. D. Sukra and G. Gabrielse, *Measurement of the Electron Magnetic Moment*, Phys. Rev. Lett. 130, 071801 (2023). https://physics.aps.org/featured-article-pdf/10.1103/PhysRevLett.130.071801
2. T. Aoyama, T. Kinoshita and M. Nio, *Theory of the Anomalous Magnetic Moment of the Electron*, Atoms 7 (2019) 28. https://www.mdpi.com/2218-2004/7/1/28
3. T. Aoyama, M. Hayakawa, A. Hirayama and M. Nio, *Verification of the tenth-order QED contribution to the anomalous magnetic moment of the electron from diagrams without fermion loops*. https://arxiv.org/abs/2412.06473
4. *Precision tests of QED* (compilation of fine-structure-constant determinations). https://en.wikipedia.org/wiki/Precision_tests_of_QED
5. Muon g-2 Collaboration, *Measurement of the Positive Muon Anomalous Magnetic Moment to 127 ppb*. https://arxiv.org/abs/2506.03069
6. Muon g-2 Theory Initiative, *The anomalous magnetic moment of the muon in the Standard Model: an update*, Phys. Rep. 1143 (2025) 1-158. https://arxiv.org/abs/2505.21476
7. Muon g-2 Theory Initiative, *White Paper (2025)* summary page. https://muon-gm2-theory.illinois.edu/white-paper-25/
8. CERN Courier, *Fermilab's final word on muon g-2*. https://cerncourier.com/fermilabs-final-word-on-muon-g-2/
9. A. Keshavarzi, Physics World, *Muon g-2 achieves record precision, but theoretical tensions remain*. https://physicsworld.com/a/muon-g-2-achieves-record-precision-but-theoretical-tensions-remain/
10. CERN Courier, *Shifting sands for muon g-2*. https://cerncourier.com/a/shifting-sands-for-muon-g-2/
11. BMW/DMZ Collaboration, *BMW/DMZ calculation of the hadronic vacuum polarisation for the muon magnetic moment*. https://arxiv.org/abs/2603.03835
12. G. Colangelo et al., *Tensions in e+e- -> pi+pi-(gamma) measurements: the new landscape of data-driven hadronic vacuum polarization predictions for the muon g-2*. https://arxiv.org/abs/2312.02053
13. Particle Data Group, *Z Boson* listings (2024). https://pdg.lbl.gov/2024/listings/rpp2024-list-z-boson.pdf
14. Particle Data Group, *Mass and Width of the W Boson*, review 54 (2025). https://pdg.lbl.gov/2025/reviews/rpp2025-rev-w-mass.pdf
15. CMS Collaboration, *High-precision measurement of the W boson mass with the CMS experiment*. https://arxiv.org/abs/2412.13872
16. *Status of the W boson mass and the future of the electroweak fit in the next decades*. https://arxiv.org/abs/2506.01887
17. J. Haller et al. (Gfitter), *Status of the global electroweak fit with Gfitter in the light of new precision measurements*. https://arxiv.org/abs/2211.07665
18. ATLAS Collaboration, *ATLAS sets record precision on Higgs boson's mass*. https://atlas.cern/Updates/Press-Statement/atlas-sets-record-precision-higgs-bosons-mass
19. Particle Data Group, *Status of Higgs Boson Physics*, review 11 (2026). https://pdg.lbl.gov/2026/reviews/rpp2026-rev-higgs-boson.pdf
20. ATLAS Collaboration, *Combination of Higgs boson measurements at sqrt(s) = 13 TeV and their interpretations by the ATLAS experiment*. https://arxiv.org/abs/2608.07332
21. CMS Collaboration, *Constraints on the Higgs boson self-coupling from the combination of single and double Higgs boson production in pp collisions at 13 TeV*. https://arxiv.org/abs/2407.13554
22. Particle Data Group, *Vud, Vus, the Cabibbo Angle, and CKM Unitarity*, review 67 (2025). https://pdg.lbl.gov/2025/reviews/rpp2025-rev-vud-vus.pdf
23. I. Esteban, M. C. Gonzalez-Garcia, M. Maltoni, I. Martinez-Soler, J. P. Pinheiro and T. Schwetz, *NuFit-6.0: updated global analysis of three-flavor neutrino oscillations*, JHEP 12 (2024) 216. https://arxiv.org/abs/2410.05380
24. S. Duerr et al. (Budapest-Marseille-Wuppertal), *Ab Initio Determination of Light Hadron Masses*, Science 322 (2008) 1224. https://arxiv.org/abs/0906.3599
25. Particle Data Group, *Free Quark Searches* review (2026). https://pdg.lbl.gov/2026/reviews/rpp2026-rev-free-quark-searches.pdf
26. *Key Historical Experiments in Hadron Physics*. https://arxiv.org/abs/2503.14689
27. ATLAS Collaboration, *A precise measurement of the jet energy scale derived from single-particle measurements and in situ techniques in pp collisions at 13 TeV with the ATLAS detector*. https://arxiv.org/abs/2407.15627
28. ATLAS Collaboration, *The performance of missing transverse momentum reconstruction and its significance with the ATLAS detector using 140 fb-1 of 13 TeV pp collisions*. https://arxiv.org/abs/2402.05858
29. A. Antoniou, *What is a data model?*, European Journal for Philosophy of Science 11 (2021) 101. https://link.springer.com/article/10.1007/s13194-021-00412-2
30. D. Hooper, *What Makes A Discovery* (182nd Nobel Symposium proceedings). https://arxiv.org/abs/2312.00672
31. *750 GeV diphoton excess* (summary of ATLAS/CMS significances and subsequent data). https://en.wikipedia.org/wiki/750_GeV_diphoton_excess
32. P. Maettig and M. Stoeltzner, *Model Choice and Crucial Tests. On the Empirical Epistemology of the Higgs Discovery*. https://arxiv.org/abs/1806.09201
33. Stanford Encyclopedia of Philosophy, *Experiment in Physics* (Franklin's strategies; Pickering, Hacking, Galison, Karaca). https://plato.stanford.edu/entries/physics-experiment/
34. Stanford Encyclopedia of Philosophy, *Theory and Observation in Science* (Hanson, Kuhn, Bogen and Woodward). https://plato.stanford.edu/entries/science-theory-observation/
35. M. Morrison, *Reconstructing Reality: Models, Mathematics, and Simulations* (OUP 2015), reviewed by C. Beisbart, Notre Dame Philosophical Reviews. https://ndpr.nd.edu/reviews/reconstructing-reality-models-mathematics-and-simulations/
36. T. R. Junk and L. Lyons, *Reproducibility and Replication of Experimental Particle Physics Results*, Harvard Data Science Review. https://arxiv.org/abs/2009.06864
37. W. Abdallah et al., *Reinterpretation of LHC Results for New Physics: Status and Recommendations after Run 2*. https://arxiv.org/abs/2003.07868
38. *Technicolor (physics)* - S parameter, ETC flavour bounds, technipion masses, effect of the 125 GeV discovery. https://en.wikipedia.org/wiki/Technicolor_(physics)
39. J.-W. Lee, *Strongly coupled gauge theories towards physics beyond the Standard Model* (Lattice 2023). https://arxiv.org/abs/2402.01087
40. *Experimental Particle Physics Priorities 2025: A String Phenomenology Perspective*. https://arxiv.org/abs/2505.12965
41. L. Constantin, S. Kraml and F. Mahmoudi, *The LHC has ruled out Supersymmetry - really?*, Nucl. Phys. B 1018 (2025) 117012. https://arxiv.org/abs/2505.11251
42. Particle Data Group, *Searches for Quark and Lepton Compositeness*, review 90 (2025). https://pdg.lbl.gov/2025/reviews/rpp2025-rev-searches-quark-lep-compositeness.pdf
43. Particle Data Group, *Extra Dimensions* listings (2025). https://pdg.lbl.gov/2025/listings/rpp2025-list-extra-dimensions.pdf
44. J. F. Donoghue, *A Critique of the Asymptotic Safety Program*. https://arxiv.org/abs/1911.02967
45. B. Famaey and A. Durakovic, *Modified Newtonian Dynamics (MOND)*. https://arxiv.org/abs/2501.17006
46. Particle Data Group, *Axions and Other Similar Particles*, review 89 (2025). https://pdg.lbl.gov/2025/reviews/rpp2025-rev-axions.pdf
47. O. Benevides Rodrigues, M. Hostert, K. J. Kelly, B. Littlejohn, P. A. N. Machado, I. Safa and T. Zhou, *Towards a Robust Exclusion of the Sterile-Neutrino Explanation of Short-Baseline Anomalies*. https://arxiv.org/abs/2503.13594
48. CERN Courier, *Two strikes for the light sterile neutrino*. https://cerncourier.com/two-strikes-for-the-light-sterile-neutrino/
49. KATRIN Collaboration, *KATRIN experiment sets most precise upper limit on neutrino mass: 0.45 eV*. https://www.eurekalert.org/news-releases/1079556
50. KamLAND-Zen Collaboration, *Search for Majorana Neutrinos with the Complete KamLAND-Zen Dataset*. https://arxiv.org/abs/2406.11438
51. G. Elor, R. Houtz, S. Ipek and M. Ulloa, *The Standard Model CP Violation is Enough*. https://arxiv.org/abs/2408.12647
52. DESI Collaboration, *DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints*. https://arxiv.org/abs/2503.14738
53. *Cosmological preference for a positive neutrino mass at 2.7 sigma: A joint analysis of DESI DR2, DESY5, and DESY1 data*. https://arxiv.org/abs/2507.16589
54. LZ Collaboration, *Dark Matter Search Results from 4.2 Tonne-Years of Exposure of the LUX-ZEPLIN (LZ) Experiment*. https://arxiv.org/abs/2410.17036
55. E. L. Wright, *Errors in "The Big Bang Never Happened"* (point-by-point refutation of Lerner's plasma cosmology). https://www.astro.ucla.edu/~wright/lerner_errors.html
56. Borexino Collaboration, *Borexino results on neutrinos from the Sun and Earth*. https://arxiv.org/abs/2105.13858
57. A. Unzicker, *The Higgs Fake: How Particle Physicists Fooled the Nobel Committee* (publisher's statement of the book's claims). https://politics-prose.com/book/9781492176244
58. R. M. Santilli, *Inconsistencies of Neutrino and Quark Conjectures and their Negative Environmental Implications*. https://arxiv.org/abs/physics/0603262
59. LHCb Collaboration, *Improved lepton universality measurements show agreement with the Standard Model*. https://lhcb-outreach.web.cern.ch/2022/12/20/improved-lepton-universality-measurements-show-agreement-with-the-standard-model/
60. *Large Hadronic Effects in B -> K* mu mu?*. https://arxiv.org/abs/2603.27753
61. *Fundamental Physics in 2025: Status, Decisive Targets, and Path Forward*. https://arxiv.org/abs/2512.21445
62. Clay Mathematics Institute, *Millennium Prize Problems* - Yang-Mills existence and the mass gap, listed unsolved. https://www.claymath.org/millennium-problems/

---

## Version Log

**v1 (2026-11-24)** - First full pass of stream 07. Establishes the Part 1 precision baseline from PDG reviews and primary measurement papers; locates the two steps at which the inferential chain becomes irreducibly model-dependent (object-to-entity mapping, acceptance factor) and distinguishes them from the instrumentally anchored earlier steps; rates ten competing frameworks with four of them downgraded to effectively dead or untestable; records R(K) as dissolved with its published cause and muon g-2 as displaced rather than resolved; rejects five fringe positions on specific quantitative grounds. Tier D section closed with eighteen entries, five of which reject claims that would otherwise have strengthened the archive's own thesis.
