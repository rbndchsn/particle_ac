---
title: Theoretical Priors Encoded in the Software Stack
subtitle: Generators, tunes, detector simulation, unfolding and learned classifiers as carriers of the assumptions they are used to test — and the correlated-error problem between ATLAS and CMS
author: Robin
date: 2026-11-24
version: v1
status: active — Tier A/B evidence base complete; Tier C inferences narrowed against published sensitivity scans
source_files: 00_method/research_frame_v1.md; web research 2026-11-24 (42 primary sources, see references)
---

# What the Stack Is, and Why "Bias" Is the Wrong Word

A collider measurement is not a reading off an instrument. It is the output of a chain:
a matrix-element calculation, a parton shower, a hadronisation model, a multi-parton-interaction
model, a detector simulation, a reconstruction pass, a calibration, an acceptance and efficiency
correction, usually an unfolding step, and increasingly a neural network. Every link in that chain
except the raw detector readout is code, and most of the code embeds a physical model with
parameters that were fitted to earlier data.

The phenomenon under examination here is therefore not bias in the machine-learning-ethics sense.
It is narrower and sharper: **a model's assumptions are implemented in the simulation and analysis
software, and that software then supplies the corrections through which new data about the same
physics is interpreted.** The field's own literature states this plainly. The canonical review of
event generators warns against the practice of using a model to extrapolate a measurement, because
doing so "contaminates the result with the model that is used to perform the correction" (1).

The generators are explicit that they are models. PYTHIA's own manual divides its physics into parts
derived from theory and "other parts [that] are based on phenomenological models, with parameters
to be determined from data," and states that its predictions "depend upon O(100) parameters" whose
"values of these parameters are inferred from comparisons to data" (2). The review literature is
blunter: hadronisation models "are not derived directly from QCD and consequently have more free
parameters than the preceding components" (1). SHERPA's manual says its non-perturbative components
"involve a number of parameters, that are not determined by first principles. Rather, they need to
be adjusted through an iterative comparison of corresponding SHERPA predictions with experimental
data" (3). The Snowmass generator report attributes this to necessity: "Due to a lack of
first-principles calculations, event generators employ models inspired by preconfinement," and
"Currently, this process cannot be described in any other approach" (35).

This is Tier A throughout. The field does not claim that hadronisation is derived. The question
this file pursues is what follows structurally from that admission.

# Four Generators, Fewer Independent Models

## PYTHIA

PYTHIA hardcodes the **Lund string** model of hadronisation: colour-connected parton systems
fragment collectively along a relativistic string with a tension and a fragmentation function whose
parameters (the Lund $a$, $b$, and $\sigma_\perp$) are fitted, not calculated (1, 2) [A]. Its shower
is transverse-momentum ordered — the manual notes that "the ordering is normally done in a measure
of transverse momentum, from high to low," which is a scheme choice, and that the division into
components "is not entirely unambiguous and sometimes is open to corrections" (2) [A]. Dipoles are
"defined by colour connections that are assigned in the $N_c \to \infty$ limit, and are not unique
for $N_c = 3$"; the residual ambiguity is absorbed into a **colour reconnection** model (2) [A]. The
multi-parton-interaction model is the Sjöstrand–van Zijl impact-parameter model (3). The manual's
range-of-validity caveats are explicit: the string model "is most appropriate when the invariant
masses of the hadronizing systems are above 10 GeV or so," and "for lower-mass systems, the model is
less firmly reliable," closing with "As always, caveat emptor" (2) [A].

## HERWIG

HERWIG hardcodes **cluster** hadronisation, based on preconfinement: gluons are split, colour-singlet
clusters form and decay. Its tunable parameters are of a different kind from PYTHIA's — "the gluon
constituent mass and cluster momentum smearing in cluster hadronization models" against "the string
tension and fragmentation function parameters for string hadronization models" (1) [A]. Its default
shower is angular-ordered, which captures soft-gluon coherence by construction (1) [A].

## SHERPA

SHERPA's default shower is a Catani–Seymour dipole shower (3) [A]. Its hadronisation module AHADIC is
a cluster model, placed by the manual alongside HERWIG's: "cluster fragmentation models … such as
the ones implemented in HERWIG and SHERPA" (3) [A]. Critically for the correlated-error question,
**SHERPA's underlying-event model is not independent of PYTHIA's**: the manual states the MPI model
"was proposed by Sjöstrand and van der Zijl … and it is also the MPI model implemented in SHERPA"
(3) [A]. Its multijet merging (MEPS@NLO) introduces a free merging scale $Q_{cut}$ whose dependence
cancels only "to the logarithmic accuracy of the parton shower" (3) [A].

## MadGraph5_aMC@NLO

MG5_aMC is a matrix-element and matching engine, not a full event generator. It has **no hadronisation
or MPI model of its own**; the paper describes the merging approach as making "direct use of the
well-tuned showering and hadronization mechanisms of the parton shower Monte Carlos" (4) [A]. Tree-level
merging "is fully automated only when the shower phase is performed with either Pythia6 or Pythia8" (4) [A].

## The lineage map

Collapsing the above: there are **two** hadronisation paradigms in production use (string, cluster),
**one** widely used MPI paradigm (Sjöstrand–van Zijl, in both PYTHIA and SHERPA), and a set of
matrix-element engines (POWHEG, MG5_aMC) that **share the non-perturbative sector of whichever shower
they are matched to** [A, from 1, 2, 3, 4]. The Snowmass report, asking for "a detailed comparison
between its two main implementations in HERWIG and SHERPA," treats the two cluster implementations as
variants of one model rather than two models (35) [A].

## Parton shower accuracy is a documented, not assumed, limitation

Dasgupta, Dreyer, Hamilton, Monni and Salam examined whether the showers in production actually attain
next-to-leading-logarithmic accuracy and found they do not. For PYTHIA's pT-ordered shower and DIRE,
"the pattern of multiple emission that they generate has flaws in singular regions that are arguably
serious," traced to "the specific attribution of recoil"; effective double-emission matrix elements are
wrong by up to 100% in regions where two emissions have commensurate pT and separated rapidity, and the
colour factor is misassigned in soft-collinear regions (11) [A]. The consequence they quantify: NLL errors
"for a wide range of event-shape like observables," and for TeV-scale jet substructure, discrepancies "of
order 20%" (11) [A]. The canonical review is consistent: shower ordering variables are "all … formally
allowable choices," but "they differ in the amount of subleading terms they introduce" (1) [A].

This is the cleanest available statement of the structural point. The showers through which every LHC
measurement passes had a logarithmic accuracy that was not established at the time they were in universal
production use, and when it was established, it was found to be lower than assumed.

# Tuning: The Documented Procedure

## Monash 2013

The Monash tune is the reference point for the PYTHIA 8 parameters used across the LHC. Its procedure, in
the authors' own words, was **manual**: "We do this manually, rather than in an automated setup," and the
chi-square figures quoted are "intended merely to give an overall indication of the level of agreement or
disagreement," since "our tuning is not directly driven by a $\chi^2$ minimization" (6) [A]. Final-state
radiation and hadronisation were fitted first to LEP e+e- data, then hadron-collider ISR, MPI and
minimum-bias observables, then energy scaling (6) [A].

Three features of that paper matter structurally:

1. **Subjective judgement is acknowledged.** Where measurements conflicted the authors applied their own
   judgement, inflating systematic uncertainties on phi rates and overriding the PDG D± value with an ALEPH
   measurement nearly twice as large; the conclusions acknowledge "(subjective) decisions" taken to reach a
   self-consistent constraint set (6) [A].
2. **A tuned parameter is used to absorb missing perturbative physics.** The effective one-loop
   $\alpha_s(M_Z) = 0.1365$ for showers is chosen partly because it can "effectively mimic" missing
   higher-order K-factors, and the authors call the choice "somewhat arbitrary," made "purely for
   convenience" (6) [A]. This is the mechanism in its purest form: a non-perturbative parameter standing
   in for an uncalculated perturbative correction, then shipped to every user.
3. **Hadronisation is not cleanly separated from the shower.** The string $\sigma_\perp$ comes "essentially
   from the first two bins of the Thrust distribution," which also depends on the shower; the paper claims
   no formal separation (6) [A]. The authors disclaim finality: "By no means do we claim that this should be
   regarded as the final word in tuning" (6) [A].

## ATLAS A14

A14 is built on the Monash tune with PYTHIA 8.186 and performs a "simultaneous variation of 10 parameters"
covering ISR and FSR $\alpha_s$ and cutoffs together with MPI, fitted with Rivet and Professor to ATLAS
7 TeV underlying-event, jet-shape, dijet-decorrelation, jet-gap-fraction and Z $\phi^*$ data (8) [A].
Colour reconnection and hadronisation are not among the tuned ten (8) [A]. The eigentune variations — the
object experiments actually propagate as "parton shower uncertainty" — were not derived from any
model-adequacy criterion: the full 10 x 2 = 20 variations were judged "too unwieldy" and reduced to 10 in
five pairs, a reduction the ATLAS presentation states "is physics dependent" (8) [A].

That same ATLAS presentation states the two facts this file is about, in the collaboration's own words:
"Non-perturbative parameters can not be derived from first principles, so require tuning," and
"**Over-tuning of non-perturbative parameters may hide New Physics**" (8) [A]. It also flags a residual
"Tension in LEP vs LHC jet observables?" after the fit (8) [A].

## CMS CP1–CP5

CMS used Rivet 2.5.2 and Professor 1.4.0, generated around 150 parameter points, fitted a third-order
polynomial response surface, and minimised a chi-square in which "No correlation across bins is included
in the minimized $\chi^2$ function" (7) [A]. Five parameters were varied: pT0Ref, ecmPow, coreFraction,
coreRadius and ColorReconnection:range (7) [A].

The decisive sentence for the correlated-error question is this one: "The parameters related to the
simulation of the hadronization and beam remnants are not varied in the fits and are kept fixed to the
values of the **Monash** tune" (7) [A].

The eigentune uncertainty is normalised to the input data errors, not to any measure of model adequacy:
CMS sets $\Delta\chi^2_{min} = \chi^2$, a choice that "produces a tune whose uncertainty bands are roughly
the same as the uncertainties in the fitted data points" (7) [A]. CMS also documents that the fitted
pT0Ref moves from about 2.3–2.4 GeV at LO to about 1.4–1.5 GeV at NLO/NNLO purely from the PDF order
(7) [A] — i.e. the MPI parameter absorbs the perturbative order of the PDF, exactly as the review
literature predicts: "much of the effect of PDF changes can be absorbed into typical MPI model parameter
choices" (1) [A].

CMS's own caveats are extensive and should be recorded as the field's good practice: discrepancies up to
20% below 3 GeV, inability to reproduce 300 and 900 GeV UE data, up to 40% differences in CASTOR for the
LO tunes, and the explicit instruction that "Analyses particularly sensitive to hadronization should
carefully evaluate the corresponding systematic uncertainties" because hadronisation was left untuned (7) [A].

## What the tuning literature says about degeneracy

The canonical review states the problem directly. Generators "most have of order 15 or more tuning
parameters"; the space is "far too high for comprehensive exploration," so tuning proceeds in stages, with
ISR tuned before MPI specifically to avoid "the danger of absorbing effects which should be perturbatively
describable" into the MPI model (1) [A]. It warns that "a tuned value located far into the perturbative
regime would be an abuse of the model and suggest deficiencies elsewhere," and sets the norm: "Generator
tuning should primarily optimize phenomenological simulation aspects, and not make up for shortcomings in
modelling" (1) [A]. The Snowmass report records where this has not held: on flavour composition, "the
flavour-composition picture currently contains too many epicycles" (35) [A].

# The Circularity, Stated Precisely

The loose form of the charge — "generators are tuned on data then used to interpret data" — is too crude to
survive contact with the practice, and the honest version is narrower.

What is **not** happening: generators are not tuned on the signal distributions they are later used to
measure. Tunes are fitted to LEP event shapes and identified-particle rates, and to minimum-bias and
underlying-event observables at the Tevatron and LHC (6, 7, 8) [A]. Acceptance and efficiency factors are
then computed from those tuned samples for analyses in different phase spaces and different final states.

What **is** happening, and is documented:

1. **A single non-perturbative parameter set propagates to both experiments.** CMS fixes hadronisation to
   Monash values (7); ATLAS builds A14 on the Monash tune and does not re-tune hadronisation (8). Monash
   itself was a manual fit with acknowledged subjective decisions, in which the shower coupling was chosen
   partly to mimic missing higher orders (6) [A].
2. **Tuned parameters absorb missing perturbative physics**, by the authors' own description (1, 6) [A].
   An acceptance correction computed from such a sample carries that substitution.
3. **The correction model and the measurement are not independent of each other when the measurement is of
   a quantity defined by the model.** The sharpest case is the top quark mass. Hoang's review states that
   direct measurements "determine the top mass parameter of the MMC" — the Monte Carlo generator's mass
   parameter — and that "finding a rigorous relation between $m_t^{MC}$ and top mass renormalization schemes
   defined in field theory is unresolved" (13) [A]. The MC mass depends on the shower cutoff, "and in
   principle also the type of the PS"; "the physical meaning of the top mass parameters in different PSs
   should not be assumed to be universal" (13) [A]. On tuning specifically: "This relation is diluted or even
   lost to the extent that the tuning compensates for conceptual deficiencies of the PS" (13) [A]. The size:
   "we are talking about differences and effects at the level of 0.5 to 1 GeV," and "the error in identifying
   $m_t^{MC}$ with the pole mass is at least of the same size" as the quoted experimental uncertainty
   (13) [A]. And on whether the experiments cover it: "none of the three $\Delta$ terms … is accessible via
   the error estimates carried out by the experimental collaborations" (13) [A].

So the circularity is real but it is local, not global. It bites hardest where the measured quantity is a
generator parameter rather than an observable. The field acknowledges this case and has not resolved it:
"no consensus has been reached on how to estimate and even formulate the uncertainty" (13) [B — Hoang and the
SCET community on one side, the experimental top groups' pragmatic treatment on the other].

# Generator-Choice Uncertainty: The Two-Point Prescription

Standard practice is to take the difference between a nominal and an alternative generator configuration as
a one-standard-deviation modelling uncertainty. The canonical review already flagged the limit: comparing
generators "is useful for getting an idea of the limitations of and differences between the predictions," but
taking the difference between generators or tunes "is not always sufficient" (1) [A].

The decisive empirical test is Ghosh and Nachman. Using W-tagging and fragmentation modelling, they find the
PYTHIA–HERWIG spread is about 40%; decorrelation shrinks it to about 20%, while **the SHERPA–PYTHIA spread
stays roughly unchanged** — so "using only two generators would badly underestimate the true uncertainty"
(10) [A]. They also establish why the two-point number is not a standard deviation in any statistical sense:
theory uncertainties "typically do not have a statistical origin," arising from "calculational approximations
and phenomenological model freedom, not from sampling," yet "These variations are then interpreted as a one
standard deviation uncertainty" (10) [A]. Their conclusion: "Until we know the complete set of theory nuisance
parameters, it seems prudent to not decorrelate away these uncertainties" (10) [A].

The Aspen 2026 summary, authored by Canonero, Cowan, Forte, Huston, Jaskiewicz, Kraus, Preuss, Reichelt,
Skands, Szafron and Ulrich, extends the critique to scale variations: they are "false friends," they
"inevitably underestimate uncertainties in regions where logarithmic resummation is necessary," and
"we cannot say with certainty which precise factor-$k$ variation would be equivalent to a statistical 68%"
interval, with "no particular reason to assume the likelihood function for such variations to be Gaussian"
(12) [A]. It records "a growing consensus on the importance of accounting for correlations among
missing-higher-order uncertainties" (12) [A].

[B] The remedy is genuinely contested. Tackmann's theory-nuisance-parameter programme proposes replacing
envelope prescriptions with parametrised, correlatable nuisance parameters (42); the Aspen group aligns with
it while proposing 19-point multiscale variations and a Gamma Variance Model that treats the uncertainty
estimate as itself uncertain (12). The Aspen authors explicitly decline to adjudicate: "it is not the objective
of this framework to provide a recipe for determining which variation is 'best'" (12).

**Do the two generators in a two-point comparison share lineage?** For the dominant case at the LHC — nominal
POWHEG+PYTHIA8 versus alternative POWHEG+HERWIG7 — the matrix element is the same code and the variation is
shower-plus-hadronisation. Herwig's string-model implementation paper gives the field's own reason for wanting
to break this up: its stated motivation is that it would be beneficial "to independently combine different
components from different generators," so that one can study hadronisation uncertainty by "fixing all the other
components of the simulation in Herwig and switching the hadronization models," and separately "compare the
results of Herwig and Pythia using the same hadronization model" to "see how the other physics components
within the generators change the simulation results" (5) [A]. That design intent is a direct statement, from
the generator authors, that the conventional PYTHIA-versus-HERWIG comparison does not isolate hadronisation.
The paper's tuning assumption is that the parameter groups "decouple and can be tuned separately in smaller
groups … without introducing significant correlations" (5) [A] — an assumption, stated as one.

PYTHIA has also recently gained internal reweighting for fragmentation variations (Bierlich, Ilten, Menzo,
Mrenna, Szewc, Wilkinson, Youssef, Zupan), motivated by the cost of repeated simulation rather than by a
critique of the two-point method; they note that methods for hadronisation uncertainties "have, up to now,
remained elusive," and caution that reweighting fails when the baseline sample does not cover the alternative
parameters (34) [A].

## [C] Inference: the two-point modelling uncertainty is an estimate of unknown sign, and both experiments use the same pair

Rests on: (1) the published demonstration that a PYTHIA–HERWIG spread does not bound a SHERPA–PYTHIA spread
(10); (2) the generators' own statement that the comparison mixes shower and hadronisation (5); (3) the shared
Monash hadronisation parameters underlying both experiments' nominal PYTHIA 8 configurations (6, 7, 8); (4) the
fact that MG5_aMC and POWHEG inherit the non-perturbative sector of the shower they are matched to (4).

Inference: where both collaborations estimate modelling uncertainty from the same nominal/alternative pair
built on a shared non-perturbative parameter set, the two experiments' modelling uncertainties are not merely
similar in size — they are estimates of the same model span, computed the same way. The quoted modelling
uncertainty is then better read as a sensitivity to one model axis than as a bound on model error.

**Falsified by:** a three-or-more-generator study on an LHC precision observable showing the two-point spread
does in fact bound the wider spread; or publication of ATLAS and CMS nominal configurations whose
non-perturbative parameters are independently fitted. Note this inference is **not** falsified or confirmed by
the combination scans discussed below, which vary the assumed correlation but not the underlying model span.

# GEANT4: One Detector Simulation

Both ATLAS and CMS use GEANT4 for full detector simulation. CMS's default physics list was FTFP_BERT_EMM;
ATLAS compared FTFP_BERT and QGSP_BERT (14) [A]. Simulation is the dominant computing cost: CMS full simulation
took 85% of total CPU time over 2009–2016 with the GEANT4 module at about 40%, and ATLAS used 39% of available
time on full simulation in 2015–16 (16) [A]. The DOE workshop report states GEANT4 "consumes the majority of the
hundreds of thousands of microprocessor cores devoted to experimental particle physics" (18) [A].

## Known accuracy limits

The HSF simulation white paper quantifies the state: hadron-shower response agrees with data "at the level of a
few percent," but shower shapes and resolution "show agreement at a level of 10–20%"; and the known directional
failure is that "the lateral profiles of Geant4 hadronic showers are too narrow" (16) [A]. It records that
LHC-tuned physics lists "disagree with existing hadron-production data by up to 40% in some areas of phase space"
for neutrino beams, that further tuning on thin-target data does not necessarily improve thick-target agreement,
and that "the current models are reaching their limits" (16) [A]. It also records that "a well-defined procedure
to tune hadronic models needs to be defined and deployed" (16) [A].

CALICE's test-beam validation gives the numbers, for 8–100 GeV pions in a highly granular scintillator-steel
calorimeter (15) [A]:

| Observable | Best lists | Documented disagreement |
|---|---|---|
| Energy response | FTFP_BERT, CHIPS best overall | QGSP-based lists: within 4% at 8 GeV, rising to **7–10% at 100 GeV**; CHIPS up to 10% at 80 GeV; LHEP 8–10% at low E |
| Interaction length | QGSP_FTFP_BERT, Fritiof ~4% | QGSP_BERT up to ~9% at 8–10 GeV; LHEP up to 14% at 100 GeV |
| Longitudinal profile | 5–10% at 8 and 18 GeV | **up to 20%** at the shower maximum at 80 GeV; LHEP up to 50% at 8 GeV |
| Radial profile | CHIPS 2–4% above 10 GeV | "Monte Carlo models **underestimate the radial extent of showers**"; up to ~12% at high energy |

The physics-list choice is itself an unpropagated degree of freedom. A systematic study of GEANT4's
electromagnetic constructors found most differ measurably from the nominal option4 reference — option1 and option2
compatible in "equal or lower than 67%" of test cases — and states plainly "We did not study the accuracy of the
simulation with respect to specific experimental data, but the general systematic uncertainty," offering no
prescription for a physics-list uncertainty and calling extrapolation across use cases "precarious" (19) [A].

## [C] Inference: GEANT4 is the one place where both experiments' simulation error is the same error

Rests on: both experiments use GEANT4 full simulation (14, 16); the documented shower-shape and
lateral-profile disagreements are properties of the hadronic models, not of either detector (15, 16); the HSF
white paper identifies "the need for careful assessment of the systematic uncertainties associated to GEANT4
predictions" as a need, i.e. as not yet met, with tools "being developed" (16) [A]; the Higgs combination treats
detector-related experimental systematics as uncorrelated between experiments (30).

Inference: a mismodelling in a GEANT4 hadronic model produces a shift in the same direction in both detectors,
to the extent that both detectors' calorimeters respond to the same mismodelled physics. Where that shift survives
in-situ calibration, it is a common-mode error that the standard correlation scheme — which assigns detector
systematics to the uncorrelated category because the detectors differ — does not represent.

**Falsified by:** a published study varying the hadronic physics list coherently in both experiments and showing
either that the calibration removes the effect or that the residual is smaller than the assigned uncorrelated
uncertainties. The strongest available counter is that this largely *is* removed by in-situ calibration (see
counterargument section), which is why this inference is weaker than it first appears.

# ROOT: The Framework Monoculture

The HSF roadmap states the dependency without hedging: the community "has developed and gravitated around a
single analysis ecosystem based on ROOT," which is "a data analysis toolkit that also plays a critical role in
the implementation of experiments' data storage systems," with tiered data formats "typically based on the ROOT
file format" (20) [A]. The same report notes the analysis monoculture extended to machine learning: "The vast
majority of HEP analyses published in recent years have used the HEP-specific software package TMVA included in
ROOT" (20) [A].

Maintenance footprint: the ROOT team page lists **15 people** (13 named), of whom 6 are at CERN, one each at
Fermilab, Princeton and Nebraska-at-CERN, with the remainder unstated, each owning a work package — Cling and the
interpreter, I/O, RooFit, graphics, math, columnar storage (21) [A]. The roadmap's own assessment of sustainability:
"There is considerable anxiety in the experiments that much of this software is not sustainable," with original
authors often gone and code poorly documented, and "The maintenance and sustainability of the current analysis
ecosystem also present a major challenge … this effort is provided by just a few institutions" (20) [A].

GEANT4 by comparison lists 143 collaboration members across roughly 79 institutions plus 50 external contributors
(17) [A] — far broader, though the DOE report notes "no one member could be an expert in all of its components"
and that much of the work is part-time institute-assigned effort, not a "free gift" (18) [A].

[C] The honest reading: ROOT is a **concentration** risk, not a bus-factor-of-one risk. Work-package ownership by
single named individuals (21) plus the roadmap's documented maintenance anxiety (20) supports concentration. It
does not support the stronger claim; see Tier D.

# Unfolding: Where the Prior Is the Regulariser

Unfolding inverts detector smearing to recover a particle-level spectrum. Schmitt's review states the
ill-conditioning: for this class of integral equation "small changes of $g(y)$ may result in large changes of
$f(x)$," and oscillating solutions are "often observed when solving inverse problems" (23) [A]. Unregularised
matrix inversion "returns an unbiased result, because it is a simple linear transformation," but the result "does
not correspond to a smooth curve as expected by the physicist's prejudice on such a distribution," with
neighbouring-bin correlations near −1 (23) [A]. Cousins et al. put the cost in starker terms: the price of
unbiasedness is variance that "renders the unfolded histogram unintelligible to humans" (24) [A].

Regularisation buys smoothness with bias, and **the simulation is the thing it biases toward**. The two sentences
that establish the mechanism:

- Tikhonov/TUnfold: regularisation terms "damp the fluctuations and reduce bin-to-bin correlations, at the cost of
  introducing biases," and "for very large $\tau$ the result is strongly biased to $x_B$," the bias vector (23) [A].
- Iterative "Bayesian" (D'Agostini/EM): "**The dependence on the start values, typically taken to be the Monte
  Carlo truth, provides a regularisation of the result**" (23) [A]. Cousins et al. concur: truncating EM iterations
  "retain[s] some memory of the starting point of the solution (typically leading to a bias)" (24) [A], and note that
  the method is misnamed in HEP — it is frequentist, not Bayesian (24) [A].
- Bin-by-bin correction factors — still in use as acceptance and efficiency factors around an unfolding step — are
  "biased significantly by the underlying Monte Carlo distributions," and Schmitt advises against them (23) [A].

The regularisation strength is not uniquely determined. Schmitt notes the two standard criteria disagree: "the
$\rho_{avg}$ minimisation yields a stronger regularisation than the L-curve method," and reports a case where the
$\rho_{avg}$ minimum "did not give a satisfactory result" (23) [A]. ATLAS's own practice review (Biondi) confirms the
heterogeneity: SVD with Tikhonov for the 8 TeV top pT measurement, iterative Bayes for the 13 TeV top-pair and W±Z
measurements, IDS with data-driven regularisation for inclusive jets, with the number of iterations set by judgement
— "the best compromise has been found in the three iterations case" (25) [A]. ATLAS does estimate the prior
dependence: "the unfolding uncertainty due to the shape chosen as prior is estimated" via a stress test in which "the
MC distribution is reweighted, taking into account the difference between data and MC shapes" and then unfolded
(25) [A]. Schmitt's bottom line is the field's: "detailed closure tests are required to quantify the level of bias
introduced by the unfolding" (23) [A].

[B] The contested question is whether unfolded spectra should be used to test hypotheses at all. Cousins argues for a
"bottom-line test" and concludes that "a more fundamentally sound way to test hypotheses is to smear the theoretical
predictions," that "extreme caution should be exercised" in quantitative use of unfolded results, and that even
unregularised ML unfolding "already results in some failures of the bottom-line test of GOF" (24). Named positions:
Cousins and Lyons on the bottom-line test, Zech extending it to parameter estimation and finding failures in fits to
peak widths; D'Agostini for the iterative method; Hocker and Kartvelishvili (SVD) and Schmitt (TUnfold) for
Tikhonov-type regularisation; Cowan for the ML framework; Kuusela for the link to the statistics literature (24). The
practice has not changed: unfolded differential cross sections remain the standard publication product. Cousins et al.
also limit their own claim — their study covers only simple-vs-simple tests, so "no general conclusions can be drawn,"
and "the potentially more important issue of bias due to regularization affecting the bottom line test remains to be
explored" (24) [A].

ML-based unbinned unfolding (OmniFold, Andreassen, Komiske, Metodiev, Nachman, Thaler) is the field's live alternative
(26); it changes the parametrisation of the prior dependence rather than removing it, since the iterative reweighting
still starts from a simulated sample.

# Machine Learning: Classifiers Trained on Models, Applied to Data

The production case to examine is ATLAS flavour tagging, because it is fully documented. GN2 is a transformer:
per-track initialisation, a four-layer encoder with eight attention heads, attention pooling, about 2.3M trainable
parameters per fold, four folds, roughly 300 A100 GPU-hours (27) [A]. It is trained entirely on simulation —
approximately 45M b-jets, 45M c-jets, 90M light-jets and 6.25M tau-jets per fold from simulated ttbar, mixed 2:1 with
Z' (27) [A]. On the opposite side, CMS's ParticleNet is in production and was used for the first observation of
Z → cc̄ (28) [A]; the Particle Transformer that supersedes it was trained on JetClass, 100M simulated jets generated
with MG5_aMC + PYTHIA + DELPHES in a CMS configuration (28) [A].

The domain-shift problem is explicit in the ATLAS paper: "Due to imperfections in the physics modelling of the MC
generator and in the simulated detector response," input distributions differ between data and simulation (27) [A].
ATLAS's response is not to correct inputs but to measure outputs: "dedicated calibration analyses are employed to
measure the tagging efficiency" per operating point, with flavour-dependent, pT-binned simulation-to-data correction
factors — b-jets from a ~90% pure e-mu ttbar sample, c-jets from W → cs in ttbar, light-jets from Z+jets with a
secondary-vertex-mass fit (27) [A].

This is the strongest counterargument in the whole file, and it is quantified. ATLAS publishes the generator
dependence of the tagger: alternative generators agree "to within 1–2%" for b-jets, "within 10%" for c-jets, "within
4%" for light-jets, and the paper states the gains "do not come with a strong dependence on the choice and
configuration of the MC event generator" (27) [A]. The residual is named: the dominant calibration systematics are
ttbar modelling for b- and c-jets and extrapolation uncertainty for light-jets, which is "a leading source of
systematic uncertainty" (27) [A].

So: the simulation dependence of a production ML tagger is measured, bounded, and corrected in data. What is not
bounded is the part the calibration cannot reach — the extrapolation to phase space where no control sample exists.
ATLAS says so itself in naming extrapolation as the leading light-jet systematic (27) [A].

The field's own statement of the general problem is Viren, Huang, Huang, Lin, Ren, Terao, Torbunov and Yu: simulations
"are always wrong at some level"; "We are best to keep in mind that the two data domains (simulated and real) remain
distinct"; the gap "introduces a systematic error which is difficult to estimate"; and even a tool built to measure the
gap leaves "the resulting systematic uncertainty … itself uncertain." Their summary of the failure mode — the
"domain-equivalency mistake" — ends: "**Failing that, we do not know how wrong we truly are**" (29) [A]. On
interpretability they are equally direct: in a trained network, "Any given parameter in that set has no identifiable
meaning" (29) [A]. And on fitting simulation parameters to real data, they warn that unmodelled effects "will cause
systematic shifts to be attributed to the unrelated parameters" (29) [A].

Ghosh and Nachman supply the specific pathology for ML and theory uncertainty together: training a classifier to be
decorrelated from a theory nuisance parameter can shrink the *apparent* uncertainty while "the only handle to determine
the theory uncertainty is eliminated," producing "a reduced *estimate* of the true uncertainty" (10) [A].

# The Central Question: Are ATLAS and CMS Correlated Through Shared Software?

This is where the file's falsifiability condition sits: the software critique fails if generator-choice and
simulation-dependence uncertainties are propagated with correlations between experiments correctly treated. The
answer is more favourable to the field than the question implies, and the specifics matter.

## What the combination papers actually do

**ATLAS+CMS Higgs Run-1 combination (30).** Correlations are specified explicitly in Section 3.3, not ignored
[A]:

- Correlated between experiments: theory uncertainties on signal yield; PDF uncertainties on inclusive rates, per
  production process, with WH, ZH and VBF "assumed to be fully correlated"; **QCD scale and underlying-event /
  parton-shower (UEPS) uncertainties "assumed to be correlated between the two experiments"** for the same process;
  branching fractions to WW and ZZ fully correlated; ZZ and ttV background cross sections from simulation "treated as
  fully correlated"; luminosity "partially correlated."
- Uncorrelated between experiments: other signal **acceptance and efficiency** theory uncertainties, on the stated
  ground that "They are estimated and treated in very different manners by the two experiments"; all experimental
  systematics "treated independently"; background modelling, because "the ATLAS and CMS background modelling
  uncertainties cannot be easily correlated."
- Checks published: "It was verified that treating them [signal acceptance uncertainties] as correlated would have a
  negligible impact on the results"; the full PDF correlation matrix "yields differences no larger than 1%"; not
  correlating background modelling has its largest effect in ttbb for ttH(bb), "below 10% of the total uncertainty in
  the signal strength measurement in this specific channel" [A].

Wardle's practitioner account confirms the mechanism and names the shared theory input: inclusive cross sections and
branching ratios came from the LHC Higgs Working Group, so both experiments started from one Standard Model
definition; acceptances and distributions came from each experiment's own samples, "not necessarily the same," and
simulation was **reweighted to a common "best" prediction** so that uncertainties could be correlated properly (33) [A].
He records that agreeing the theory-uncertainty convention required over a year of discussion for the mass combination
alone, that object-acceptance effects were de-correlated because the procedures differ and are often data-driven, and
that for the mass measurement correlations between dominant sources "should be studied in greater detail" (33) [A].

**ATLAS+CMS top quark mass combination, 7 and 8 TeV (31).** This is the strongest counterexample to a claim of
neglect. Modelling correlations are explicitly assigned, category by category, and then scanned [A]:

| Category | Inter-experiment ρ | Stated basis |
|---|---|---|
| Hadronisation | 0.5 | different nominal configurations, but "some degree of correlation is expected" |
| CMS b-hadron B | 0 | "treated as uncorrelated with the ATLAS uncertainties" |
| Colour reconnection | 0.5 | different PYTHIA nominal settings |
| Underlying event | 0.5 | as colour reconnection |
| QCD radiation (ISR/FSR) | 0.5 | partially correlated, "similarly to the ME category" |
| ME generator | 0.5 | "different nominal MC models" |
| PDF | 0.85 | "strongly correlated between ATLAS and CMS" |
| Pile-up | 0.85 | modelling relies on simulation |
| b-JES, g-JES, MC background | 0.85 | — |
| JES2, JER, leptons, trigger, data-driven background | 0 | — |

Three facts about that table are decisive. First, **no category is assigned ρ = 1** — the paper states this reflects
differences between the experiments [A]. Second, the sensitivity to the assignments **is published**: a per-category
scan gives a largest central-value shift of 26 MeV (b-JES) and a largest uncertainty shift of 7 MeV, with modelling
categories shifting the result by a few MeV each (QCD radiation 7 MeV, ME generator under 1 MeV), all small against a
total uncertainty of 0.30 GeV on $m_t = 172.51 \pm 0.33$ GeV; flipping sign assumptions for mixed-sign categories moves
the central value at most 41 MeV (31) [A]. Third, the result is **linear** in the correlation changes (31) [A], which
means the published single-parameter scans bound the effect of moderate simultaneous changes reasonably well.

The errors-on-errors study of the same combination adds method detail and one uncomfortable fact. It uses the official
correlation matrices from the combination's Appendix B; b-JES is "only partially correlated between experiments, with a
correlation coefficient of 0.85"; and **some of the official correlation matrices had negative eigenvalues**, fixed by
adding the magnitude of the smallest negative eigenvalue to the diagonal, which the authors say "has a minimal impact on
the final combination" (32) [A]. It also notes that one "may not … assign arbitrary values" to correlation coefficients
because the covariance matrix must remain positive definite (32) [A]. Treating the systematic variances themselves as
uncertain (errors-on-errors) moves the central value by at most 0.1 GeV and widens the confidence interval by about 10%
when b-JES is given a ~50% relative error on its error (32) [A]. Notably, the paper **does not** scan the 0.85 value
itself; its errors-on-errors treatment applies only to the variances (32) [A].

## Verdict on the central question

Inter-experiment correlation of theory and modelling systematics is **modelled, not ignored, and the sensitivity to the
modelling is published** [A]. The investigation's stated falsifiability test for the software critique is therefore
substantially met for the two combinations examined. This should be recorded as a pass, not minimised.

## [C] The residual, stated at its actual strength

Two gaps survive, and neither is large.

**(a) The correlation coefficients are set by procedural difference, not by model lineage.** The top-mass combination
assigns ρ = 0.5 to hadronisation, colour reconnection, UE, QCD radiation and ME generator because the two experiments
use "different nominal MC models" (31) [A]. But those different configurations share a non-perturbative sector: CMS
fixes hadronisation and beam-remnant parameters to Monash values (7); ATLAS A14 is built on Monash and tunes ISR, FSR
and MPI, not hadronisation (8); MG5_aMC and POWHEG inherit the shower's non-perturbative models (4); SHERPA's MPI model
*is* PYTHIA's (3). The quantity ρ is thus calibrated on how differently the two collaborations *configure and process*
the models, not on how much of the underlying model is literally the same code and the same fitted parameters. On the
facts, the physical correlation of the hadronisation category is plausibly closer to 1 than to 0.5.

**Why this matters less than it sounds:** the published scans show that moving modelling correlations shifts the top mass
by a few MeV, and the response is linear (31). Setting hadronisation to 1.0 instead of 0.5 would not move the answer
meaningfully. The inference survives as a *methodological* criticism — the coefficient is justified on the wrong
grounds — while failing as a *numerical* one for this measurement.

**Falsified by:** publication of a correlation scheme whose coefficients are derived from the shared-code and
shared-tune content of the two experiments' samples rather than from procedural difference, showing values near those
currently used. **Supported further by:** a combination in which modelling is a larger share of the total than it is
for $m_t$, where the same reasoning would have a larger numerical effect.

**(b) The 0.5 assignments are the same category in which the underlying model span is itself the unbounded quantity.**
The correlation question and the two-point question compound: a correlation coefficient multiplies a modelling
uncertainty whose magnitude is a two-generator sensitivity, and the two-generator sensitivity has been shown not to bound
a three-generator one (10) [A]. Varying ρ while holding the modelling uncertainty fixed cannot detect this. The scans in
(31) and the errors-on-errors in (32) both hold the model span fixed; (32) explicitly inflates variances but does not
scan the correlation, and (31) scans the correlation but not the variances. No published study does both at once for an
inter-experiment combination.

**Falsified by:** a joint scan over correlation coefficients and modelling variances showing the combined result stable;
or by a three-generator study establishing that the two-point span is conservative.

# Reproducibility: Who Can Actually Re-Analyse an LHC Result

The 2025 LPCC reinterpretation and preservation report is the most direct source, and it is harsher than any outside
critic has been [A]:

- "**Reproducibility of several LHC Run-1 and even Run-2 searches for new physics have already been lost within ATLAS
  and CMS**" (36).
- "It is often impossible to reproduce the analysis with high fidelity even within the collaboration that produced the
  work" (36).
- "Missing information is very difficult to retrieve," often because the team disbanded or files were lost; "key
  ingredients to many physics searches are missing, even to the collaborations"; and "Restrictive collaboration
  policies on the release of information" limit external use (36).
- Preservation "relies on the goodwill of a relatively small number of dedicated individuals" (36).
- "Without access to the complete computational workflow," precise reproduction "is impossible," and full detector
  simulation is "computationally intensive and requires significant expertise," making "their direct use challenging
  for external researchers" (36).
- Coverage: "only a fraction of the hundreds of publications from LHC experiments provide reusable material on
  HEPData." Of 1,117 HEPData records tagged for Rivet, MadAnalysis or CheckMATE as of 27 March 2025, 479 are from the
  four main LHC experiments (245 ATLAS, 142 CMS, 48 LHCb, 44 ALICE), "just over 22%" (36). SimpleAnalysis covers 56
  search analyses, mostly SUSY (36). Open-data studies "require at least as much time as do analyses within the
  collaborations" (36).

DPHEP's 2026 global report adds the collaborations' own assessment: ATLAS reports that "**the uptake of true 'data
preservation' via Reana and Recast remains limited**," that "there is no active support for the processing of Run 1
data," and that "support for the Run 2 and Run 3 data will be dropped in the coming HL-LHC era of Run 4" (38) [A].
DPHEP 2023 identifies the cause as mundane: "The key issue is the person power, that functions for most of the examples
of preserved data sets in a voluntary mode" (37) [A].

## The ATLAS–CMS open data asymmetry

| | CMS | ATLAS |
|---|---|---|
| Policy | "half of the data to the public after a six-year embargo period, with the remaining released after ten years"; all Run 1 released; over 300 collision datasets and over 20k simulated datasets, over 4 PB (38) | First research release July 2024: 2015–16 pp data, 36 fb⁻¹, PHYSLITE (38, 40) |
| Format | AOD-level reconstructed data (38) | PHYSLITE, "a light-weight analysis format that is also used internally" (40) |
| Volume | over 4 PB (38) | 7.1 billion events / 45 TB collision data plus ~300 MC datasets / 2 billion events / 20 TB; ~65 TB total (40); over 12 billion generator events across 6,000+ datasets (38) |
| Known content gaps | — | "PHYSLITE does not contain all tracks, so users cannot perform track-counting analyses"; particle-flow objects absent so users cannot build their own jets; LLP searches only partly possible; format limits could lead to "incorrect physical conclusions" in some measurements (40) |

The CERN policy itself (December 2020) sets Level 3 as calibrated reconstructed data with software, example workflows
and virtual environments, with support "a limited level of support … on a best-effort basis," releases commencing
"within five years of the conclusion of the run period" after "an appropriate latency period," and with data that "may
be withheld by an experiment if there are active analyses ongoing." Raw data is not released: "It is not practically
possible to make the full raw data-set from the LHC experiments usable" (39) [A]. The policy's own caveat on
independent audit is the key sentence: "**External authors should be aware that they will not have access to the vast
amount of tacit knowledge**" built up within the collaborations (39) [A].

## What has improved

Full statistical models are now published for some analyses. ATLAS released "the first full HistFactory models" in
2019, "met with enthusiasm" by the phenomenology community; a HEPData search found 41 statistical-model records (16
SUSY, 21 top), and "14 of the 16" SUSY searches with HistFactory models are reused by reinterpretation tools. CMS "has
recently followed suit by publishing their Combine software" with the 2012 Higgs statistical model and "plans to
systematically release full statistical models." The report recommends this become standard practice (36) [A]. Full
models let an outsider test a new signal "correctly accounting for non-Gaussian effects and nuisance
parameter-induced correlations" (36) [A].

## [C] Inference on auditability

Rests on: reproducibility already lost for some Run-1 and Run-2 searches, internally (36); ~22% HEPData/Rivet coverage
(36); ATLAS's limited REANA/RECAST uptake and planned end of Run-1/2/3 support (38); PHYSLITE content gaps (40); the
tacit-knowledge caveat (39).

Inference: for the bulk of LHC results, independent re-analysis by an outsider is not available, and for some results
re-analysis is not available to the collaboration either. Where re-analysis is available it is via published likelihoods
and Rivet routines — which lets an outsider test a *new signal hypothesis* against a preserved statistical model, not
re-derive the model from data. The audit path that exists is reinterpretation, not verification.

**Falsified by:** a demonstrated case of an outside group re-deriving a published LHC measurement from open data and
reaching the published result with published uncertainties. **Mundane explanation that must be beaten and largely is
not:** the cause named in every primary source is person-power, format decisions, and the cost of full simulation
(36, 37, 38, 39) — not a decision to resist scrutiny.

# Who Funds and Staffs the Stack

The 2025 EPPSU software input states the resourcing position directly [A]: MC event generators "can reach 20% of the
total CPU budget" at HL-LHC; generator developers are "a relatively small, but critically important, ecosystem of
researchers" whose "intersectionality" creates "serious challenges in terms of career paths and funding
opportunities"; the paper cites "the lack of resources routinely plaguing the generator theory community"; and
cross-experiment "committed funding sources for HEP have been lacking" (22). On analysis software: many packages are
maintained by early-career staff on "fixed-term contracts of no more than a few years," and without support they can
become "insufficiently maintained to be useful to the community" (22). On simulation: the paper calls for "ensuring a
generational transition before current experts retire" (22). On incentives: the "current mindset favours visibility and
recognition of those working on data analysis projects or detector hardware" (22).

The roadmap's language is the same: "Attracting, and retaining, people with the required skills who can provide
leadership is another significant challenge," "Continuous support is needed to recruit, train, and retain people with a
unique set of skills," and some experiments "do not currently recognise contributions to external projects as
experiment service work" (20) [A]. The HSF simulation paper names digitisation code as "one of the most significant
risks in terms of code aging and loss of expertise" (16) [A].

Headcounts, for the record: ROOT, 15 listed (21); GEANT4, 143 members / ~79 institutions / 50 external contributors
(17); the four main generators are maintained by theory groups of a few people each, with the paper describing the
population only qualitatively as small (22). No primary source gives FTE counts per package (22) — a gap worth naming.

[C] The structural reading: the software layer that converts every LHC signal into a physics claim is maintained by a
population one to two orders of magnitude smaller than the collaborations that depend on it, on funding and career
structures the field itself describes as inadequate. This is a **path-dependence and institutional-incentive**
explanation, and it is sufficient. It requires no claim of interest or capture, and the primary sources support the
mundane reading, not a motivated one.

# The Counterargument, Given Full Weight

The field is more sophisticated about this than the structure of the critique implies, and several of the mechanisms it
uses specifically target simulation dependence.

**In-situ calibration removes the bulk of detector-simulation error.** Elvira's review documents the practice: energy
scales are corrected by data-to-MC scale factors derived from data-driven techniques; closure tests check whether
data-driven methods recover MC truth, and a method that does not close "indicates the need to go back to the drawing
board"; and where discrepancies remain they are traced to specific causes, such as photon-conversion discrepancies that
"can be directly related to deficiencies in the detector geometry modeling" (14) [A]. The CALICE-level shower-shape
disagreements of 7–20% (15) are in observables that enter a measurement only after calibration, not as raw inputs.

**Data-driven background estimation is used precisely to cut simulation dependence.** The Higgs combination treats
background modelling as uncorrelated between the experiments in part because the estimates are data-driven and
procedure-specific (30), and Wardle notes that object-acceptance effects were decorrelated because "these are often
data-driven" (33) [A].

**Nuisance parameters are constrained by the data.** Lista, De Iorio and Iorio state the mechanism: "Data samples can
constrain nuisance parameters and reduce the original uncertainties," within a profile-likelihood framework in which
"the preferred choice of test statistic is the profile likelihood" (41) [A]. The cost is complexity, which the same
authors flag as itself a risk: management of hundreds of parameters can "make the analysis infrastructure complex and
hard to manage, eventually resulting in simplifications in the treatment of systematics, and in limitations to the
result interpretation" (41) [A].

**Simulation dependence of learned taggers is measured and published.** ATLAS quantifies the generator dependence of
GN2 at 1–2% (b), 10% (c), 4% (light), and calibrates efficiencies in data against dedicated control samples (27) [A].

**Inter-experiment correlation is modelled and its sensitivity is published.** Section above: explicit correlation
schemes, published per-category scans, linear response, shifts of a few MeV against 330 MeV total for $m_t$ (30, 31, 32) [A].

**The field is diagnosing its own tools.** The showers' logarithmic accuracy was established and found wanting by the
field itself (11); the two-point prescription's failure was demonstrated by the field (10); unfolding's prior dependence
is textbook (23, 24, 25); the top-mass interpretation problem is a live theory programme (13); internal hadronisation
reweighting was built to replace cross-generator comparison (34); Herwig implemented Pythia's hadronisation model to
disentangle the two (5); alternatives to envelope prescriptions are under active development (12, 42).

**On the specific concern about shared software:** the correct conclusion is that it is **partially handled and the
handled part is tested**. Theory and PDF systematics are correlated between experiments at 0.85–1.0 where they are
common inputs; UEPS and QCD scale are correlated; the residual categories are assigned 0.5 and scanned; the scans show
the answer does not move. Where the concern survives, it survives as a criticism of the *justification* for the
coefficients rather than of the *numbers*, and in the compounding of the correlation question with the separately
documented two-point question — not as a demonstration that any published result is wrong.

# What Would Falsify the Software Critique

Restating the frame's test, now with specifics:

1. **Correlation treatment.** Met, for the two combinations examined. Correlations are specified, nonzero for
   modelling, and scanned (30, 31, 32). The critique fails on the strong version.
2. **Generator-choice uncertainty.** Not met. Published evidence shows the two-point span does not bound the
   three-generator span (10), both experiments use the same nominal/alternative pair over a shared non-perturbative
   parameter set (4, 6, 7, 8), and the field has no agreed replacement (12, 42). This is the live residual.
3. **Simulation dependence of ML.** Met for the documented ATLAS case (27); unestablished for architectures whose
   generator dependence is not published.
4. **Unfolding.** Partly met: prior dependence is documented, estimated by stress tests, and the contentiousness is
   on the record (23, 24, 25); but the bottom-line-test literature's own open question — bias from regularisation
   affecting the bottom line — "remains to be explored" (24).
5. **Auditability.** Not met. Reproducibility of some published searches is lost internally; ~22% HEPData reuse
   coverage; no demonstrated outside re-derivation of a published LHC measurement (36, 38, 39, 40).

# Claims Examined and Not Supported

**Tier D.** Each of these was pursued and failed. They are recorded so they are not re-litigated.

**D1. That LHC combination papers ignore correlated theory and modelling systematics between ATLAS and CMS.**
Not supported, and the opposite is documented. The Higgs combination correlates signal theory, PDF, QCD scale and UEPS
uncertainties between experiments and publishes checks on the categories it decorrelates (30). The top-mass combination
assigns explicit inter-experiment correlations to hadronisation, colour reconnection, UE, QCD radiation, ME generator,
PDF and pile-up, publishes a per-category sensitivity scan, and reports linear response (31). A separate study
re-examines the same combination with errors-on-errors (32). This was the single most likely-looking claim going in; it
is false as stated.

**D2. That the correlation treatment materially changes published central values or uncertainties.**
Not supported for the cases with published scans. Largest per-category central-value shift 26 MeV, largest uncertainty
shift 7 MeV, modelling categories a few MeV each, against 0.33 GeV total on $m_t$ (31); errors-on-errors moves the
central value at most 0.1 GeV and widens the interval about 10% in the worst case examined (32); correlating the Higgs
signal acceptance uncertainties has "a negligible impact" and the full PDF correlation matrix changes results by no
more than 1% (30). The methodological criticism in [C](a) above stands; the numerical one does not.

**D3. That the field is unaware of, or silent about, the limitations of two-point generator comparisons.**
Not supported. The limitation is stated in the canonical review ("not always sufficient," (1)), demonstrated
quantitatively by Ghosh and Nachman (10), targeted by the Herwig+Lund-string programme (5) and by PYTHIA's internal
fragmentation reweighting (34), and the subject of an ongoing workshop and theory-nuisance-parameter programme
(12, 42). The defensible claim is that the *practice* has not changed, not that the problem is unrecognised.

**D4. That generators are tuned on the very distributions they are then used to correct, making measurements
self-confirming.**
Not supported as stated. Tunes are fitted to LEP event shapes and identified-particle rates and to minimum-bias and
underlying-event observables (6, 7, 8), not to the signal distributions measured in the analyses that use them; and
backgrounds are frequently estimated from data rather than simulation (30, 33). The narrow version that survives is
specific and must be stated as such: tuned parameters demonstrably absorb missing perturbative physics (1, 6), and where
the measured quantity *is* a generator parameter — the top MC mass — the interpretation problem is unresolved and
acknowledged (13).

**D5. That regularisation in unfolding drives published central values toward the simulation, rendering unfolded
spectra simulation artefacts.**
Not supported as a general claim. Regularisation does bias toward the prior and the Monte Carlo truth is the usual
starting point and therefore the regulariser (23, 24) — that much is Tier A. But ATLAS estimates the prior-shape
uncertainty by reweighting-and-unfolding stress tests (25), closure tests are standard (23, 25), and the central
critique in the literature (Cousins) concerns whether unfolded histograms should be used for *hypothesis testing*, not
whether their central values are artefacts; its authors explicitly limit their conclusions ("no general conclusions can
be drawn") (24). A claim that specific published unfolded spectra are prior-driven would need a specific analysis, and
none was found.

**D6. That GEANT4's hadronic-shower disagreements with test-beam data invalidate LHC calorimeter measurements.**
Not supported. The disagreements are real and sizeable — 7–10% in response at 100 GeV, up to 20% longitudinally at
80 GeV, systematically too-narrow lateral profiles (15, 16). But calorimeter energy scale and resolution are calibrated
in situ with data-derived scale factors, with closure tests (14), so the uncalibrated simulation response is not what
enters a measurement. The surviving concern is the unpropagated physics-list degree of freedom (19) and the absence of
an agreed uncertainty prescription for GEANT4 predictions (16), which is a gap in uncertainty *quantification*, not a
demonstrated error in results.

**D7. That ROOT is a single-maintainer or bus-factor-one dependency.**
Not supported. The team page lists 15 people across CERN, Fermilab, Princeton and Nebraska, with distinct work packages
(21). The supportable claim is concentration — "a single analysis ecosystem based on ROOT," with maintenance "provided
by just a few institutions" and documented "considerable anxiety" about sustainability (20) — not key-person dependency
of one. Similarly, GEANT4's 143 members and ~79 institutions (17) do not support a key-person framing.

**D8. That production ML taggers carry an unquantified simulation dependence.**
Not supported for the best-documented case. ATLAS publishes GN2's generator dependence (1–2% b-jets, 10% c-jets, 4%
light-jets) and calibrates efficiencies against data control samples (27). The surviving concern is extrapolation beyond
the control samples, which ATLAS itself names as a leading systematic (27), and the general domain-shift argument, which
is stated in the literature as a difficulty rather than a demonstrated error (29).

**D9. That open-data and preservation limits reflect a decision to impede outside scrutiny.**
Not supported, and the mundane explanation wins on the evidence. Every primary source attributes the limits to
person-power ("functions for most of the examples … in a voluntary mode" (37)), goodwill of "a relatively small number
of dedicated individuals" (36), format and content decisions (40), the cost and expertise required for full simulation
(36), and the impracticality of releasing raw data (39). Note that the most damaging statements about reproducibility
come from the collaborations' own reports (36, 38), which is evidence against a suppression reading. The policy's own
caveat about outsiders lacking "tacit knowledge" (39) is a statement of fact about expertise, not a restriction.

**D10. That "algorithmic bias" describes this phenomenon.**
Rejected on terminological grounds, per the research frame. No social or representational bias in training data is at
issue. The phenomenon is theoretical assumption implemented in simulation and analysis code that is then used to supply
the corrections through which the same physics is measured — which the generator literature itself names as
contamination of a result by the model used to correct it (1). The ML-ethics term would mislead a technical reader and
would make the claim easier to dismiss than it deserves.

**D11. That the shared software stack casts doubt on the Standard Model's confirmed predictions.**
Out of scope by the frame, and unsupportable. Nothing in the material examined bears on the validity of the Standard
Model's tested predictions. The in-situ calibration, data-driven background estimation and control-region validation
documented above (14, 27, 30, 33, 41) are specifically designed to limit simulation dependence, and the published
sensitivity scans (30, 31, 32) show the correlated-systematics question does not move the results examined.

# What Is Worth Carrying Forward

Three findings are strong enough to survive hostile review:

1. **The Monash hadronisation parameter set is a single common ancestor of both experiments' nominal PYTHIA 8
   configurations** (6, 7, 8), fitted manually with acknowledged subjective decisions and with a shower coupling chosen
   partly to mimic missing higher orders (6). This is the most concrete instance of a theoretical prior shared across
   the two experiments presented as independent.
2. **The two-point generator prescription is a demonstrated non-bound**, with the demonstration published inside the
   field (10), and no replacement adopted (12, 42).
3. **Reproducibility of some published LHC searches is already lost, internally** (36), and ATLAS's own report states
   that true preservation uptake "remains limited" and that Run 1–3 support will be dropped (38).

One finding runs the other way and must be carried with equal weight: **the inter-experiment correlation of modelling
systematics is explicitly modelled, and the published sensitivity scans show it does not move the results examined**
(30, 31, 32). The strong form of the correlated-error charge is refuted by the field's own documents. What remains is a
criticism of how the coefficients are justified, and of the compounding of correlation uncertainty with an
unbounded model span — narrower, defensible, and not yet tested by anyone.

# References

1. A. Buckley et al., "General-purpose event generators for LHC physics," Physics Reports. https://arxiv.org/abs/1101.2599
2. C. Bierlich et al., "A comprehensive guide to the physics and usage of PYTHIA 8.3," SciPost Phys. Codebases. https://arxiv.org/abs/2203.11601
3. E. Bothmann et al., "Event generation with Sherpa 2.2," SciPost Phys. 7, 034. https://arxiv.org/abs/1905.09127
4. J. Alwall et al., "The automated computation of tree-level and next-to-leading order differential cross sections (MadGraph5_aMC@NLO)," JHEP. https://arxiv.org/abs/1405.0301
5. "Herwig 7 with the Lund string model: tuning and comparative hadronization studies," Eur. Phys. J. C. https://arxiv.org/abs/2509.02348 and https://link.springer.com/article/10.1140/epjc/s10052-025-15182-x
6. P. Skands, S. Carrazza, J. Rojo, "Tuning PYTHIA 8.1: the Monash 2013 tune," Eur. Phys. J. C 74, 3024. https://arxiv.org/abs/1404.5630
7. CMS Collaboration, "Extraction and validation of a new set of CMS PYTHIA8 tunes from underlying-event measurements," Eur. Phys. J. C. https://arxiv.org/abs/1903.12179
8. S. Jiggins, "MC Tuning @ ATLAS," on behalf of the ATLAS Collaboration. https://indico.ictp.it/event/a14280/session/266/contribution/1041/material/slides/0.pdf
9. A. Buckley et al., "Systematic event generator tuning for the LHC" (Professor), Eur. Phys. J. C. https://arxiv.org/abs/0907.2973
10. A. Ghosh, B. Nachman, "A cautionary tale of decorrelating theory uncertainties," Eur. Phys. J. C. https://arxiv.org/abs/2109.08159
11. M. Dasgupta, F. Dreyer, K. Hamilton, P. F. Monni, G. P. Salam, "Logarithmic accuracy of parton showers: a fixed-order study," JHEP. https://arxiv.org/abs/1805.09327
12. E. Canonero, G. Cowan, S. Forte, J. Huston, S. Jaskiewicz, M. Kraus, C. T. Preuss, D. Reichelt, P. Skands, R. Szafron, Y. Ulrich, "Summary of Aspen discussions on perturbative uncertainties beyond 7-point variations." https://arxiv.org/abs/2610.25091
13. A. H. Hoang, "What is the top quark mass?," Ann. Rev. Nucl. Part. Sci. https://arxiv.org/abs/2004.12915
14. V. D. Elvira, "Impact of detector simulation in particle physics collider experiments," Physics Reports. https://arxiv.org/abs/1706.04293
15. CALICE Collaboration, "Validation of GEANT4 Monte Carlo models with a highly granular scintillator-steel hadron calorimeter," JINST. https://arxiv.org/abs/1306.3037
16. HEP Software Foundation, "HEP Community White Paper on Detector Simulation" (HSF-CWP-2017-07). https://arxiv.org/abs/1803.04165
17. Geant4 Collaboration, "Geant4 members and contributors." https://www.geant4.org/collaboration/members
18. US DOE Office of Science, "Transforming Geant4 for the Future," workshop report, September 2012. https://science.osti.gov/-/media/ascr/pdf/research/scidac/GEANT4-final.pdf
19. "Impact of Geant4's electromagnetic physics constructors on accuracy and performance of simulations for rare event searches." https://arxiv.org/abs/2507.14788
20. HEP Software Foundation, "A roadmap for HEP software and computing R&D for the 2020s," Comput. Softw. Big Sci. https://arxiv.org/abs/1712.06982
21. ROOT project, "Team." https://root.cern/d/team.html
22. "The critical importance of software for HEP," input to the 2026 European Strategy for Particle Physics Update, Eur. Phys. J. C. https://arxiv.org/abs/2504.01050
23. S. Schmitt, "Data unfolding methods in high energy physics," EPJ Web Conf. https://arxiv.org/abs/1611.01927
24. R. D. Cousins et al., "Should unfolded histograms be used to test hypotheses?" https://arxiv.org/abs/1607.07038
25. S. Biondi (ATLAS Collaboration), "Experience with using unfolding procedures in ATLAS," EPJ Web Conf. 137, 11002. https://www.epj-conferences.org/articles/epjconf/pdf/2017/06/epjconf_conf2017_11002.pdf
26. A. Andreassen, P. Komiske, E. Metodiev, B. Nachman, J. Thaler, "OmniFold: a method to simultaneously unfold all observables," Phys. Rev. Lett. 124, 182001. https://arxiv.org/abs/1911.09107
27. ATLAS Collaboration, "Transforming jet flavour tagging at ATLAS," Nature Communications. https://www.nature.com/articles/s41467-025-65059-6
28. H. Qu, C. Li, S. Qian, "Particle Transformer for jet tagging," ICML. https://arxiv.org/abs/2202.03772
29. B. Viren, J. Huang, Y. Huang, M. Lin, Y. Ren, K. Terao, D. Torbunov, H. Yu, "Solving simulation systematics in and with AI/ML," Snowmass21 Computational Frontier whitepaper. https://arxiv.org/abs/2203.06112
30. ATLAS and CMS Collaborations, "Measurements of the Higgs boson production and decay rates and constraints on its couplings from a combined ATLAS and CMS analysis of the LHC pp collision data at 7 and 8 TeV," JHEP. https://arxiv.org/abs/1606.02266
31. ATLAS and CMS Collaborations, "Combination of measurements of the top quark mass from data collected by the ATLAS and CMS experiments at 7 and 8 TeV," Phys. Rev. Lett. 132, 261902. https://arxiv.org/abs/2402.08713
32. "Correlated systematic uncertainties and errors-on-errors in measurement combinations: methodology and application to the 7-8 TeV ATLAS-CMS top quark mass combination." https://arxiv.org/abs/2407.05322
33. N. Wardle, "ATLAS+CMS Higgs combination experience," September 2024. https://indico.global/event/3065/contributions/33034/attachments/17048/27584/ATLAS_CMS_HComb_nwardle.pdf
34. C. Bierlich, P. Ilten, T. Menzo, S. Mrenna, M. Szewc, M. K. Wilkinson, A. Youssef, J. Zupan, "Reweighting Monte Carlo predictions and automated fragmentation variations in Pythia 8," SciPost Phys. https://arxiv.org/abs/2308.13459
35. "Event generators for high-energy physics experiments," Snowmass 2021 report. https://arxiv.org/abs/2203.11110
36. "Reinterpretation and preservation of data and analyses in HEP," CERN-LPCC-2025-002. https://arxiv.org/abs/2504.00256
37. DPHEP Collaboration, "Data preservation in high energy physics," Eur. Phys. J. C. https://arxiv.org/abs/2302.03583
38. DPHEP Collaboration, "Data preservation in high energy physics: global report 2026," DPHEP-2026-01. https://arxiv.org/abs/2607.06775
39. CERN, "CERN open data policy for the LHC experiments," December 2020. https://opendata.cern.ch/docs/cern-open-data-policy-for-lhc-experiments
40. "The first release of ATLAS open data for research," EPJ Web Conf. (CHEP 2024). https://www.epj-conferences.org/articles/epjconf/pdf/2025/22/epjconf_chep2025_01345.pdf
41. L. Lista, A. De Iorio, A. O. M. Iorio, "Managing many simultaneous systematic uncertainties." https://arxiv.org/abs/1810.11206
42. F. J. Tackmann, "Beyond scale variations: perturbative theory uncertainties from nuisance parameters." https://arxiv.org/abs/2411.18606

**Source access note.** The ATLAS A14 tune note itself (ATL-PHYS-PUB-2014-021) could not be retrieved — the CERN
Document Server returned a bot-protection challenge on both the record and the PDF. A14 details here come from
reference 8, an ATLAS tuning presentation given on behalf of the collaboration. Anyone extending this file should
confirm the A14 parameter list and eigentune construction against the note directly.
