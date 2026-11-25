---
title: Research Frame and Evidence Standards
subtitle: How this investigation is structured, what counts as evidence, and the methodological traps built into its own premise
author: Robin
date: 2026-11-24
version: v1
status: active — governs all other files in this archive
source_files: none (method document)
---

# The Research Question

Across the full stack of high-energy particle physics — theoretical motivation, machine
hardware, detector instrumentation, simulation and analysis software, publication, and
funding governance — where are the weaknesses, and are they acknowledged?

The investigation operates at five levels, each with its own folder:

1. **Theory** — whether the notions motivating the machines are falsifiable, and what
   happens to a motivating argument when its prediction fails.
2. **Hardware** — what the instruments physically cannot see, and who builds them.
3. **Software** — what theoretical assumptions are encoded in the code that converts
   detector signals into physics claims.
4. **Publication** — whether the literature is structurally capable of auditing itself.
5. **Governance** — who decides what gets built, and what their interest is.

# The Trap in This Project's Own Premise

The brief is to "expose weaknesses." That phrasing pre-commits to a conclusion, which is
the same methodological failure the investigation intends to document in others. A critique
built on motivated reasoning can be dismissed on exactly the grounds it advances.

Two consequences follow, and they are binding on every file here:

**Tier D is mandatory.** Every research file must close with claims that were examined and
could *not* be supported. A file with no Tier D section is incomplete, not strong. The
presence of rejected claims is what distinguishes forensic work from advocacy, and it is
the only thing that makes the surviving claims cost anything to dismiss.

**Mundane explanations get priority over motivated ones.** Budget constraint, institutional
inertia, path dependence, and technical conservatism explain most of what looks like
suppression. An explanation involving interest or capture must beat the mundane explanation
on evidence, not on narrative appeal.

# A Terminological Correction

"Bias in the algorithms" imports a meaning from machine-learning ethics — social bias in
training data — that does not describe what happens here and would mislead a technical
reader.

The actual phenomenon is **theoretical prior encoded in instrumentation and code**: the
assumptions of a model are built into the apparatus and software that are then used to
test that model. This is a sharper, more defensible, and more serious claim than "bias."
The archive uses the precise formulation throughout. Where a genuine selection or
representational bias exists, it is named as such and distinguished.

# Evidence Tiers

Every substantive claim in every file carries a tier label.

| Tier | Meaning | Standard of proof |
|---|---|---|
| **A** | Documented and acknowledged inside the field | Primary literature, collaboration technical design reports, official lab or agency documents, procurement records |
| **B** | Contested inside the field, named advocates on both sides | Both positions cited from their own authors, not from characterisations |
| **C** | Structural inference — follows from Tier A facts but has not been assembled or tested by the field | Must state the Tier A facts it rests on and what would falsify it. Never presented as a finding. |
| **D** | Examined and rejected | Recorded with the reason it failed, so it is not re-litigated |

Tier C is where this project's original contribution lives, and it is also the most
dangerous tier. A Tier C claim that is presented as established converts the whole archive
into polemic. Tier C claims must be written so that a hostile specialist reading them would
say "that inference is available from those facts," not "that is unsupported."

# Falsifiability Requirement

Each level of analysis must state what would show its critique to be wrong:

- **Theory critique** fails if the motivating arguments were in fact abandoned openly and
  on the record when their predictions failed, with the abandonment reflected in subsequent
  funding requests.
- **Hardware critique** fails if the instrumental blind spots are published, quantified,
  and factored into discovery claims.
- **Software critique** fails if generator-choice and simulation-dependence uncertainties
  are propagated with correlations between experiments correctly treated.
- **Publication critique** fails if there is a working mechanism by which an outside
  specialist can audit a multi-thousand-author result and force a correction.
- **Governance critique** fails if strategy bodies include members with no prospective
  stake, and if their recommendations have historically gone against the interest of their
  own membership.

These are genuine tests. Some may be passed. Recording that is the job.

# Scope Boundaries

In scope: terrestrial accelerators and their detectors; the software stack converting
signals to claims; the publication and funding systems around them; astrophysical
particle-acceleration instruments where the same issues recur.

Out of scope, and explicitly so: any claim that experimental results are fabricated, that
the Standard Model's confirmed predictions are invalid, or that detector physics is faked.
These are not weak versions of the argument; they are a different and unsupportable
argument, and including them would discredit the defensible material by association. The
Standard Model is the most precisely tested theory in the history of physics. The critique
here concerns what *surrounds* that core: motivation, instrumentation limits, encoded
assumptions, accountability, and interest.


## One standing exception to the Tier D rule

`10_financial_investigation/` is a **collection-phase document** and deliberately carries no
"Claims Examined and Not Supported" section. It was commissioned on the explicit instruction
that collection and assessment be separated, and that nothing encountered be dropped — including
claims from weak or anonymous sources, which are recorded with their provenance rather than
filtered out.

In place of Tier D it closes with an enumerated list of what could not be established, each
item naming the document that would answer it. Every entry carries a source class (audit,
court, official, press, advocacy, anonymous) and a status (verified, reported, alleged,
unverifiable), so the assessment pass has what it needs.

This is an exception to the frame, not a lapse from it. A later pass should not "fix" it by
adding a rejection section — the assessment belongs in a separate document, against the
collected material.
