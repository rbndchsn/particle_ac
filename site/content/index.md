---
title: The Instrument and Its Blind Spot
subtitle: What particle physics states in its own documents about the limits of what it can see, and what it leaves out of the documents that ask for the next machine
author: Robin
date: 2026-11-24
version: v1
status: active
source_files: all files in this archive
---

# Start with what this does not claim

<div class="concede">
<h3>Conceded, up front and without reservation</h3>

The machines work. The Standard Model is the most precisely confirmed theory in the
history of physics. The detectors measure what they claim to measure. No part of this
archive argues otherwise, and any version of this critique that did would be wrong.

- Experimental results are **not** fabricated. Claims to the contrary were examined here and rejected.
- The Standard Model's confirmed predictions are **not** invalid.
- Critics of this field overwhelmingly dispute its **priorities and its motivating theory**, not its results. Treating them as a bloc that doubts the physics misrepresents nearly all of them.
- Particle physics publishes negative results **better than most of science**, not worse.
- The funding panels **do** operate a conflict-of-interest regime, and **do** include members without a stake in the outcome.
- Critics of the field are **not** professionally punished. The case most often cited as proof of that was a disciplinary matter about something else entirely.
- Analysis combinations between experiments **do** model their shared systematic error. They do not ignore it.

More than forty claims of this kind were tested here and struck out. They are kept on
the record, with reasons, rather than quietly dropped.
</div>

This page leads with the concessions because the argument that follows only has force if
the easy version of it is off the table first.

# The claim

<div class="thesis">
<p>Particle physics published, in advance and in print, the condition under which its
central organising argument would fail. The condition was met. The argument was then
removed from the documents that ask for the next machine — without being retracted in
them.</p>
<p>Around that absence sits a system that cannot audit what it discards: an instrument
whose selection errors are measured in one direction only, a simulation stack whose shared
ancestry is not reflected in how its uncertainties are combined, and a literature in which
the unit that publishes a result is the only body able to check it.</p>
</div>

That is a narrower claim than "particle accelerators are not doing what they say." It is
also harder to dismiss, because almost every fact supporting it is drawn from the field's
own technical documents, strategy reports and court records. This archive is not an
argument from outside physics. It is an argument assembled out of physics' own paperwork.

# The four findings

## 1. A falsification condition was set, met, and unreported

In 2008 a senior theorist derived an explicit bound — new physics below roughly 1 TeV —
and wrote that if the LHC found no such phenomena, the naturalness criterion would fail.
The LHC found none. By 2017 the same author conceded the point in the theory literature.

The 2023 US strategy report that sets particle physics priorities contains, across its
entire length, **zero** instances of "naturalness," "hierarchy problem," "fine-tuning," or
"unnatural" — while still paraphrasing the argument those words name. The term reappears
in the 2025 European briefing book.

Meanwhile the quantitative threshold that defined "natural" moved by stipulation across
three decades, and the mass limits it was meant to predict moved by nearly an order of
magnitude. The retirement happened. It happened on the record, in the journals. It did not
happen in the documents that request funding.

## 2. The instrument's errors are counted in one direction

The LHC produces forty million collisions a second and keeps roughly one thousand. A full
readout would be forty terabytes per second against about one gigabyte stored. What is
discarded is discarded in hardware, in microseconds, and is unrecoverable.

What decides is the trigger menu, and the field says plainly what builds it: menus select
events believed in advance to be interesting, guided by theoretical models and simulation.
Rate is allocated by committee, annually, in roughly equal thirds between new-physics
searches, measurements, and flavour physics.

This has already cost specific measurements, by the collaborations' own account — not
delayed them, prevented them. And the error is structurally asymmetric: a trigger that
keeps too much costs measured, budgeted bandwidth, visible to everyone. A trigger that
throws away the wrong thing costs events that no longer exist, and that cost is never
integrated over the space of signatures it might have contained.

**The strong version of this claim is false, and was dropped.** Unbiased data streams do
exist, at an effective prescale near forty thousand. Physics outside the menu is badly
sampled, not unobservable. The surviving claim is the asymmetry, and it is falsifiable by a
single coverage calculation that nobody appears to have published.

## 3. The simulation stack has one ancestor, and the uncertainties are combined as if it had two

Both general-purpose LHC experiments' nominal hadronisation model descends from a single
manual fit whose own authors describe making subjective choices, and who set a key parameter
to mimic a calculation that was missing. One experiment holds those parameters fixed
entirely; the other tunes ten parameters on top of them.

Systematic uncertainty from "model choice" is then estimated by comparing two generators.
A published study shows that this spread does not bound the spread to a third generator —
in its authors' words, using only two would badly underestimate the true uncertainty.
In unfolding, the field states openly that the simulation's own prediction serves as the
regularising prior.

Combinations between the experiments do assign a correlation coefficient to these shared
modelling terms — around one half. The question this archive raises is what that number is
calibrated on: procedural difference between two collaborations, rather than shared model
ancestry. On lineage grounds the true figure for hadronisation is plausibly near one. For
the top-mass combination this is numerically immaterial. Whether it is immaterial in general
has not been tested, because no published study scans correlation and model variance together.

## 4. The publishing unit is the only body that can audit the result

The field's own reinterpretation inventory records that full statistical likelihoods were
released for two analyses; that efficiency maps appear in very few cases; that data needed
to refit results is often not provided; and that machine-learning analyses cannot be
reproduced at all outside the collaboration that produced them. A 2025 assessment states
that reproducibility of some earlier searches has already been lost *inside* those
collaborations.

Authorship on every paper is earned by a service threshold, and the committee that grants
it explicitly disclaims responsibility for content.

The inference this supports is not suppression — it is a single cause with two opposite
effects. Because the collaboration is the publishing unit, there is no file drawer, which is
why this field's null-result record is genuinely good. And for the same reason there is no
external check, because no one outside holds what an audit would require.

# The money, for completeness

The projected cost of the proposed next machine moved from roughly €9 billion in its 2019
conceptual design to CHF 15.3 billion in 2025. Over the same period the tunnel shortened,
the design energy of the second-stage machine fell, and the start of operations moved from
the late 2050s to the early 2070s. Cost up, specification down, schedule out.

The strategy panels take their cost figures from the proponents, and one subcommittee was
barred from producing estimates of its own.

For precedent: the Superconducting Super Collider was authorised at $4.4 billion in 1987,
reached estimates of $8–12 billion, consumed about $2 billion, and was cancelled by the
House 231 to 181 in 1993.

# How this archive is built

Five levels, each a folder of the repository, each with its own documents: the motivating
theory, the hardware, the software, the publication system, and the governance. Every
substantive claim carries an evidence tier. Rejected claims stay on the page.

The method file states the trap in this project's own premise, which is that a brief to
"expose weaknesses" pre-commits to its conclusion and is therefore the first thing a
specialist would attack. The defence against that is not rhetoric. It is the Tier D
sections, and the fact that both of the strongest hypotheses this project started with were
rejected by its own research.
