---
title: Who Actually Builds the Hardware
subtitle: The industrial supply chain of high-energy particle physics — firms, countries, ownership, concentration and geopolitical exposure
author: Robin
date: 2026-11-24
version: v1
status: draft for review — evidence-tiered, with an explicit not-substantiated section
source_files:
  - USGS Mineral Commodity Summaries 2026 (niobium, helium)
  - DOE Office of Science / ARDAP, "Business Models to Assure Availability of Advanced Superconductors" (2023)
  - CERN Procurement, "Doing Business with CERN" (FCC Week May 2025; UK Meet the Buyer Apr 2025)
  - BSBF 2024 Procurement Handbook (CERN, ESO, ESS, ESRF, European XFEL, F4E, ILL, SKAO, CTAO, FAIR)
  - L. Rossi, "The LHC Superconducting Magnets", PAC2003
  - SRF2013/SRF2015/NAPAC2025 proceedings on cavity and niobium procurement
  - Streicher & Gabelberger (2026), EPJ Research Infrastructures 10:10
  - Experiment technical papers: Auger, TAx4, JUNO, CMS, PANDA, EIC
---

# Scope, method and how to read the evidence tiers

This file answers one question: when a collider or a cosmic-ray observatory is built, which companies physically make the parts, in which countries, under what ownership, and where is the supply base thin enough that a single firm or a single state can stop the work.

Every substantive claim carries a tier label:

- **[A] Documented** — procurement records, official organisation documents, company statements, government mineral statistics, published technical design or production reports.
- **[B] Contested** — a live disagreement with named parties on both sides.
- **[C] Structural inference** — follows from Tier A facts, but is not a finding the field has assembled or endorsed. Each Tier C statement names what it rests on and what would falsify it. None of it should be read as an established result.
- **[D]** — the closing section, listing what was investigated and could not be substantiated.

A standing caution that applies to the whole file: **concentration in this sector is, on the documented evidence, overwhelmingly explained by ordinary industrial specialisation.** Order books are tiny (tons per year, not kilotons), qualification costs are high, lead times run 12–18 months, and the products stay in service for twenty years against an industrial norm of a few. Those facts produce near-monopolies without anyone conspiring to create them. Where this file flags a dependency, it flags a dependency — not a finding of capture or corruption. Where information is absent, the file says it is absent, and does not read capture into the silence.

A note on search coverage: this pass exhausted its web-search allocation. Several specific documents named in the closing section could not be retrieved, mostly because CERN's document server (`cds.cern.ch`) was blocked both by bot protection and by the session's network policy.

# 1. Superconducting magnets: the LHC main ring

## 1.1 The three dipole consortia

The 1,232 main dipoles were not built by CERN. They were built by three industrial consortia, each of which received an identical pre-series order and an identical series order (2, 3) [A].

| Consortium | Country | Pre-series | Series | Notes |
|---|---|---|---|---|
| Alstom MSA – Jeumont Industries | France | 30 | 386 | French consortium of two firms (2) |
| Ansaldo Superconduttori | Italy | 30 | 386 | (2) |
| Babcock Noell Nuclear ("Noell") | Germany | 30 | 386 | (2, 3) |

Pre-series cold masses were assigned in autumn 1999 and the series contracts in spring 2002; the three contracts together exceeded 300 million (currency symbol garbled in the primary source, read as MCHF) (2) [A]. Per-firm contract values are not published (see Tier D). Coil manufacture accounted for 60% of the magnet production work, and from spring 2004 each firm had to deliver three cold masses a week to hold the schedule (3) [A].

## 1.2 Quadrupoles and insertion magnets

| Magnet | Quantity | Manufacturer | Country |
|---|---|---|---|
| Main quadrupole (MQ) | 392–400 | Accel | Germany (1, 2) |
| MQM insertion quadrupole | 86 | Tesla Engineering | United Kingdom (2) |
| MQY insertion quadrupole | 26 | Accel | Germany (2) |
| Low-beta quadrupoles | 32 | KEK and US national laboratories (in-kind, not commercial) | Japan / USA (2) |
| Beam separation dipoles | — | KEK (in-kind) | Japan (2) |
| Corrector magnets | >6,000 | not named in source | — (2) |

Accel won the main quadrupole tender in 1999 after prototyping at CEA–CERN (1, 2) [A]. So two German firms (Accel, Babcock Noell) and one UK firm held the entire non-dipole superconducting magnet build, and the dipole build was split France/Italy/Germany [A].

# 2. Superconducting strand and cable: who actually makes the wire

This is the least publicly documented layer of the whole chain, and the most concentrated.

## 2.1 Quantities

| Quantity | Figure | Source |
|---|---|---|
| LHC superconducting cable, total | ~1,200 t, ~7,600 km | (4) |
| of which Nb-Ti metal | ~470 t (rest copper) | (6) |
| Cable architecture | 36-strand Rutherford; 6,426 filaments per strand | (4) |
| LHC Nb-Ti, as stated by CERN magnet group | ~1,200 t | (9) |
| Furukawa Electric's own stated LHC contribution | 180 t strand, 360 t Rutherford cable | (5) |
| Tevatron, for comparison | ~1,000 magnets, 50 t cable containing 17 t Nb-Ti | (6) |

CERN's own outreach material names **Furukawa Electric (Japan)** as "one of two main suppliers" of the cable and does not name the second (4) [A]. Furukawa's product catalogue states it made 180 t of strand and 360 t of cable for the LHC dipoles and received a CERN "Golden Hadron Award" (5) [A, company statement]. The authoritative CERN magnet paper names no cable or strand supplier at all, and describes cable as a main component supplied by CERN to the magnet firms as free-issue material (2) [A]. The commonly repeated figure of six qualified LHC strand suppliers could not be confirmed from a primary source in this pass (Tier D).

## 2.2 What LHC construction did to the market

- Tevatron conductor came from **two** manufacturers, Intermagnetics General and Magnetic Corporation of America, in an 80/20 split, and Tevatron alone consumed 80–90% of all Nb-Ti then ever made (1) [A].
- LHC construction **doubled world Nb-Ti output for five to six years** (1) [A].
- When LHC construction ended the market reverted to the MRI base load. Nb-Ti is now "a low-margin commodity" with, in CERN Courier's words, more suppliers than the market can support; the industry consolidated and attention shifted to Nb3Sn (1) [A].
- Market scale as of 2013: MRI ~€3.5 bn/yr, large laboratory facilities just under €1 bn, HTS ~€0.3 bn (1) [A]. By 2021 the MRI market was estimated at $4.8 bn (7) [A].

## 2.3 The Nb3Sn supplier map

The most complete public list of Nb3Sn high-volume producers, by process route (BR = bronze, IT = internal tin, PIT = powder-in-tube) (8) [A]:

| Manufacturer | Route | Country | Note |
|---|---|---|---|
| Bruker EAS (ex-Vacuumschmelze) | PIT, BR | Germany | "the world's only contemporary manufacturer with high-volume [PIT] capabilities" (8) |
| Bruker OST (ex-Oxford Superconducting Technology) | IT (RRP, HER) | USA — Carteret, NJ (7) | supplied **all** HL-LHC Nb3Sn wire (7) |
| Western Superconducting Technologies (WST) | BR, IT | China | (8) |
| Kiswire Advanced Technology (KAT) | IT | Korea | spun off from Kiswire (8) |
| Japan Superconductor Technology (JASTEC) | BR | Japan | Kobe Steel + Japan Magnet Technology merger (8) |
| Furukawa Electric | BR | Japan | (5, 8) |
| Luvata Special Products | BR, IT | now part of Mitsubishi Materials; Waterbury, CT operation (7, 8) |
| SH Copper (ex-Hitachi Cable) | BR | Japan | (8) |
| Chepetsky Mechanical Plant (CMP) | BR | Russia | (8) |
| Supercon Inc. | BR, PIT | USA | (8) |
| Outokumpu / Europa Metalli / ICG-IGCAS (former Luvata divisions) | BR | — | (8) |

Developers without high-volume status: Hyper Tech Research (rod-in-tube), Supramagnetics, Supergenics, Kobe Steel (7, 8) [A].

## 2.4 Annual volumes and the accelerator-grade bottleneck

| Conductor | Annual world production | Relative cost | Source |
|---|---|---|---|
| Nb-Ti | hundreds of tons | 1.0 (baseline) | (7) |
| Nb3Sn RRP | 5–10 t | ~5× | (7) |
| Nb3Sn PIT | <1 t | ~8× | (7) |

DOE's 2023 assessment is explicit: "Accelerator magnets require premium grades of Nb3Sn conductor that have a limited supplier base," and **HL-LHC's performance and piece-length requirements were met by only one supplier**, against eight manufacturers used for ITER (7) [A]. It warns that if Bruker OST consolidated manufacturing overseas, as early as 2024, conductor development roadmaps could be interrupted, and that "a technology gap of ~5 years opens before alternative manufacturing can emerge"; conductor lead times are 12–18 months (7) [A].

**[C] The accelerator-grade Nb3Sn market is a single-corporate dependency, not a two-supplier market.** This rests on three Tier A facts: Bruker OST supplied all HL-LHC Nb3Sn wire (7); Bruker EAS is the world's only high-volume PIT producer (8); and the two likely HEP conductor candidates are a Bruker EAS PIT wire and a Bruker OST RRP wire (8). Both brands sit under Bruker Corporation. So the apparent choice between two wire types is a choice between two product lines of one owner. Falsified by: a non-Bruker firm (WST, KAT, JASTEC, Luvata) qualifying at HL-LHC Jc and piece-length specification, or by divestiture of OST or EAS to a separate owner. This is not an allegation of misconduct — the DOE report frames the same facts as a market-size problem, which is the likelier explanation.

## 2.5 HL-LHC and future-collider demand

| Project | Conductor requirement | Source |
|---|---|---|
| HL-LHC | ~20 t state-of-the-art high-Jc Nb3Sn (9); ~30 t (8); DOE cites both 10 t and 30 t inconsistently (7) | (7, 8, 9) |
| ITER | ~500 t Nb3Sn; 8 suppliers; Bruker EAS alone >37 t of TF wire | (7, 8, 9) |
| FCC-hh | ~8,000 t Nb3Sn (9); ~10,000 t, a potential ~$20 bn market at ~$2 M/t (7) | (7, 9) |

DOE's blunt summary: "No superconductor is presently manufactured at the huge scale required for a high energy or muon collider," and the industry "lacks adequate economic margins from Nb-Ti MRI wire manufacture" to fund innovation (7) [A].

## 2.6 HL-LHC magnet and link builders

HL-LHC's high-field magnets are built by national laboratories, not by industry: BNL, Fermilab and LBNL under the US Accelerator Upgrade Project (successor to the 15-year LARP programme) plus CERN itself. The US labs deliver ten 9 m helium vessels each holding two 4.2 m MQXF magnets (eight for installation, two spare); CERN delivers ten 9 m vessels each holding one 7.5 m magnet; 24 magnets total, six each side of ATLAS and CMS (10) [A].

**ASG Superconductors (Italy)** supplied magnets for the LHC and won a contract for 10 ITER superconducting coils; its Columbus MgB2 Unit in Genoa makes MgB2 wire, the conductor class used for HL-LHC superconducting links. ASG has been owned since 2001 by Hofima spa and Luleo SA, both Malacalza family holdings; Davide Malacalza is President (11) [A, company statement]. Roughly 1,000 km of MgB2 is needed for electrical-transmission-class applications, of which ~280 km had been procured as of 2017 (9) [A].

# 3. Niobium: the raw material

## 3.1 Mine production — one country, three mines

USGS, niobium content in metric tons (12) [A]:

| Country | 2024 | 2025e | Reserves |
|---|---|---|---|
| Brazil | 104,000 | 104,000 | 14,000,000 |
| Canada | 6,900e | 6,000 | 640,000 |
| Congo (Kinshasa) | 930e | 970 | NA |
| Russia | 300 | 300 | 3,000 |
| Rwanda | 210e | 200 | NA |
| China | 44e | 40 | 6,500,000 |
| United States | — (zero) | — (zero) | 210,000 |
| **World** | **112,000** | **112,000** | **>21,000,000** |

Brazil is 92.9% of 2025e world mine production (104,000/112,000; my arithmetic on USGS figures) [A for inputs].

## 3.2 Producers and ownership

| Producer | Mine | Country | Output / share | Ownership |
|---|---|---|---|---|
| CBMM | Araxá, Minas Gerais | Brazil | ~85,000 t, ~77% (14); "close to 90%" (15); ">80% of world supply" (13) | Moreira Salles family 70%; a Japanese/Korean consortium 15%; a Chinese consortium 15% — both acquired 2011 (13) |
| CMOC Brasil / NML | Catalão, Goiás | Brazil | 10,024–10,348 t, ~9% (14, 15) | China Molybdenum (CMOC); bought Boa Vista from Anglo American in 2016 (15) |
| Magris Performance Materials | Niobec, Saint-Honoré, Québec | Canada | ~6,900 t, ~6% (14); company claims ~10% of market (15) | Magris, CEF/Temasek-backed (14, 15) |
| Société Minière de Bisunzu | North Kivu | DR Congo | part of DRC's ~970 t, <1% (15) | — |

CBMM extracts from a pyrochlore deposit said to meet market demand for at least 200 years at current consumption; as of 2016 it produced 90,000 t/yr ferroniobium equivalent with a planned rise to 150,000 t/yr, and sells alloys, oxides and pure metal but not raw ore (13) [A].

## 3.3 Downstream and US exposure

- US import reliance: **100%** of apparent consumption, every year 2021–2025e (12) [A]. Total imports by source: Brazil 67%, Canada 28%, other 5%; ferroniobium and niobium metal: Brazil 65%, Canada 31%; niobium oxide: Brazil 89% (12) [A].
- Ferroniobium average unit value: $21/kg (2021) rising to $26/kg (2025e) (12) [A].
- China is the largest importer, consuming ~36% of global ferroniobium and sourcing ~95% of its niobium mostly from Brazil (14) [A].
- Brazil has been reluctant to use export controls given allied demand, but could use niobium as a bargaining chip; niobium was exempted from the 50% Brazil tariff in July 2025, and a Section 232 review with reporting due around July 2026 could reshape flows. NioCorp's Elk Creek project in Nebraska is the only identified US pathway to domestic production, with full output unlikely before 2029 (14) [A].

## 3.4 High-purity (high-RRR) niobium — a different, narrower market

High-RRR niobium for SRF cavities (RRR ≈ 300) costs ~$530/kg against ~$130/kg for reactor-grade (RRR ≈ 30) (16) [A]. Seven firms are named as electron-beam refiners of high-purity niobium: ATI Wah Chang, Cabot, H.C. Starck (DE/US), W.C. Heraeus (DE), Tokyo Denkai (JP), Ningxia OTIC (CN) and CBMM (BR) (16) [A]. Ningxia OTIC specifically markets "superconducting-grade sheet" (15) [A].

# 4. SRF cavities: from niobium sheet to cryomodule

## 4.1 Niobium sheet — the US exit and the Asian takeover

The NAPAC 2025 assessment of the US SRF industry is the single most candid document found in this pass (17) [A]:

- **ATI Specialty Alloys & Components** (formerly ATI Wah Chang, earlier Teledyne Wah Chang) is the remaining domestic US high-purity Nb sheet source; its output fell to about **3 tons per year** between 2010 and 2020.
- Fansteel Metal and Cabot were domestic suppliers in the 1980s; Teledyne Wah Chang was the main one from the 1990s.
- The **main current suppliers are Ningxia OTIC (China) and Tokyo Denkai (Japan)**.
- China has "the worldwide leading industrial supplier of high-purity Nb sheets" and is described as self-sufficient across the whole SRF technology stack.
- Causes named: price competition from China, and competing demand from the superconducting magnet industry.

## 4.2 Cavity fabrication — a two-firm European duopoly for flagship linacs

| Project | Cavities | Vendors | Split | Source |
|---|---|---|---|---|
| CEBAF (late 1980s) | ~350 | Interatom (Germany) — whole procurement | 100% | (17) |
| European XFEL | 800 | Research Instruments (Germany), Ettore Zanon S.p.A. (Italy) | 560 base contracted Sept 2010 build-to-print; 240 option split 120/120 | (18) |
| ILC R&D (2007–2012) | ~100 | Niowave (Lansing MI), C.F. Roark Welding (Brownsburg IN), Advanced Energy Systems (Medford NY) | — | (17) |
| LCLS-II | 266 | Research Instruments, Ettore Zanon — dual award May 2015 | 133 each (8 first-article + 125 production) | (20) |

Other named worldwide vendors: Research Instruments (Germany) and Zanon Research & Innovation (Italy) are the major European industrial vendors, plus three unnamed Chinese suppliers (17) [A]. Advanced Energy Systems is the only US company named as able to supply complete cryomodules (for NSLS-II), and it **lost the LCLS-II bid of about 340 cavities to European vendors** (17) [A].

Niobium for both E-XFEL and LCLS-II was free-issued by the laboratory, not bought by the vendor: DESY supplied the Nb and NbTi, ran its quality control and the vertical RF tests (18); FNAL procured the Nb for LCLS-II with SLAC and JLab support (20) [A]. For E-XFEL, **PLANSEE (Austria)** and **Ningxia OTIC (China)** passed all three qualification steps, and in production four firms supplied ~25,000 semi-finished parts: Heraeus (DE), PLANSEE (AT), Tokyo Denkai (JP), Ningxia OTIC (CN) (18) [A]. Pressure-equipment compliance was overseen by the notified body TÜV NORD (18) [A]. For FRIB, $13.2 M of niobium sheet, tube and flange was awarded to three suppliers across four task orders: Wah Chang (NbTi alloy), Tokyo Denkai (sheet) and Ningxia (sheet, tube, rod) (19) [A].

LCLS-II's selection was run by JLab as a DOE-approved "Best Value" source selection scored on experience, past performance, resources, understanding of requirements and quality assurance — i.e. explicitly not lowest price (20) [A]. Phase I required each vendor to process two consecutive qualification cavities under a transferred nitrogen-doping recipe (20) [A].

**[C] Flagship SRF linac production worldwide has consolidated into two firms.** Rests on: RI and Zanon jointly holding E-XFEL (800 cavities) and LCLS-II (266 cavities), the two largest SRF procurements of the era, and the documented loss of US capacity (17, 18, 20). Falsified by a third vendor winning a build-to-print contract above ~100 cavities. The NAPAC authors' own framing — loss of domestic competitiveness, not vendor misconduct — is the parsimonious reading.

## 4.3 Advocacy for intervention

The NAPAC 2025 action plan calls for supply-chain security, sustained US capabilities and a **National SRF Council** (17) [A]. The DOE conductor report proposes annual conductor acquisitions of ~1 t/yr of Nb3Sn purely to keep manufacturing lines active, a limited national conductor stockpile, workforce pipelines, an innovation institute, and low-cost industry access to test facilities (7) [A]. The same report concedes that the public-private model it builds on — the Conductor Development Program and its successor CPRD — is "unlikely" to fully offset MRI-market cost pressures (7) [A]. No named opponent of these proposals was found in this pass, so this is advocacy on record, not a Tier B dispute.

# 5. RF power: klystrons and solid-state amplifiers

## 5.1 Klystrons

| Project | Tube | Manufacturer | Units | Source |
|---|---|---|---|---|
| European XFEL | TH1802 | Thales (France) | 20 of 26 installed | (21) |
| European XFEL | E3736H | Toshiba (Japan) | 6 of 26 installed | (21) |
| European XFEL series production | both | Thales + Toshiba | 23 produced by Sept 2014 of 27 planned | (22) |

Three vendors developed multibeam klystrons meeting the XFEL requirements; **two were selected** (21) [A]. Series performance: 9.9–10.5 MW output against a 10 MW design, 63–68% efficiency, 1.5 ms pulses at 10 Hz, 155 kW average RF. Of 23 tubes produced, one was lost in overseas transport and four were returned to the factories (filament connection, solenoid, two for RF instability) (22) [A]. The XFEL pulse step modulators are a commercial product from **Ampegon**, 24 stacked HV modules producing 10 kV-level pulses at 1.6 kA (21) [A].

The clearest public statement of klystron obsolescence risk comes from ESRF: **only one of the three original makers of the klystron ESRF used still produced that tube**, and ESRF names this as a problem for medium-sized laboratories (23) [A].

On the US side, **CPI International** — spun out of Varian Associates in 1995, IPO 2006, acquired by Veritas Capital for ~$525 M in 2011, then by Odyssey Investment Partners in 2017, FY2018 revenue ~$495 M — holds Eimac (new vacuum tubes) and Econco (tube rebuilding), and is described as the largest manufacturer and rebuilder of electron devices in the United States, though that specific claim is unsourced in the reference consulted (24) [A for ownership chronology; weak for the market claim]. **Note the structure: the principal US high-power vacuum-tube house has been under successive private-equity ownership since 2011** (24) [A].

## 5.2 Solid-state power amplifiers (the substitution path)

| Firm | Country | Product | Deployment |
|---|---|---|---|
| ELTA (subsidiary of AREVA), Blagnac | France | 352.2 MHz, 150 kW SSAs | 7 units at ESRF (4 replacing a booster klystron, 3 on storage-ring cavities), via technology transfer from SOLEIL (23) |
| Bruker → Sigmaphi Electronics, Haguenau | France | 10 kW, 1.3 GHz SSAs | 4 pairs at ELBE, replacing 4 klystrons (23) |
| Cryolectra GmbH, Wuppertal | Germany | SSAs at various frequency/power | 72 MHz, 150 kW for a medical cyclotron (23) |

SOLEIL built the reference designs: a 40 kW MOSFET SSA for its booster, then 2 × 180 kW for the storage ring (2000–2007), with its 500 MHz designs reused at LNLS and SESAME (23) [A].

The transistors are the real dependency: **NXP (Eindhoven, Netherlands)** BLF578 LDMOS devices are used in the ELTA/SOLEIL SSAs, and **Freescale Semiconductor (Austin, Texas)** is named as an LDMOS maker (23) [A]. ESRF's own assessment is that operating SSAs "commits the user to carefully follow the transistor market," because transistors have short product lifetimes and new RF modules must be developed to fit existing SSAs when a device goes end-of-life (23) [A].

**[C] The SSA transition trades a vacuum-tube duopoly for exposure to the commercial RF transistor market.** Rests on: the ESRF statement above, the single named LDMOS device in the leading SSA design, and the klystron obsolescence problem that motivated the switch (23). The substitution reduces single-vendor risk at the subsystem level and increases churn risk at the component level. Falsified by evidence that accelerator SSA designs routinely qualify two or more interchangeable transistor sources at the outset.

# 6. Cryogenics and the helium chokepoint

## 6.1 Who built the LHC cryoplants

| Plant class | Units | Supplier | Country | Contract / acceptance |
|---|---|---|---|---|
| 18 kW @ 4.5 K refrigerator | 2 (Points 1.8 and 4) | Air Liquide | France | contracts 1998; accepted Mar 2002 and Dec 2002 (25) |
| 18 kW @ 4.5 K refrigerator | 2 (Points 8 and 6) | Linde | Switzerland | contracts 1998; accepted Aug 2003 and Dec 2003 (25) |
| 18 kW @ 4.5 K refrigerator | 4 | recovered from LEP and upgraded | — | (25) |
| 2.4 kW @ 1.8 K unit | 4 | IHI / Linde | Japan / Switzerland | (26) |
| 2.4 kW @ 1.8 K unit | remainder of 8 | Air Liquide | France | unit count not stated in source (26) |

CERN Courier states plainly: **"Only two companies in the world provide turbo-expanders with sufficient cooling power"** (25) [A]. The eight plants deliver ~140 kW at 4.5 K, roughly 40,000 litres of liquid helium per hour, at ~4 MW electrical input each, 32 MW in total; each cold box weighs ~60 t and carries a 600 kW liquid-nitrogen pre-cooler (25) [A].

## 6.2 Helium production — a three-country market

USGS, million cubic metres (27) [A]:

| Country | 2024 | 2025e | Reserves |
|---|---|---|---|
| United States | 380 | 381 | 8,500 |
| Qatar | 64e | 63 | Large |
| Russia | 17e | 18 | 1,700e |
| Algeria | 11e | 11 | 1,800e |
| Canada | 6 | 6 | NA |
| China | 3 | 3 | NA |
| Poland | 3 | 3 | 24 |
| South Africa | — | <0.5 | 400 |
| **World total (rounded)** | **183e** | **190** | **NA** |

**Caution on this table:** as published, the US row cannot be on the same basis as the world total — 381 alone exceeds the stated world total of 190. USGS separately reports US Grade-A and gaseous helium **sales** of ~81 million m³ in 2025, valued at ~$970 M, which is plausibly the comparable number (27) [A, with the inconsistency flagged]. Do not compute shares from the 381 figure.

Identified resources, billion m³: Qatar 10.1, Algeria 8.2, Russia 6.8, Canada 2.0, China 1.1; US mean recoverable 8.49 excluding storage (27) [A].

US helium import sources 2021–24: **Canada 47%, Qatar 28%, Algeria 10%, China 5%** (27) [A]. Grade-A base price ~$12/m³ ($330 per thousand cubic feet) in 2025, before producer surcharges (27) [A]. EU and US sanctions imposing an import ban on Russian helium continued into 2025, and rare-gas supply from Russia and Ukraine remained limited (27) [A].

## 6.3 Who controls it

- Fewer than 15 companies worldwide supply helium; the US and Qatar together produce more than 75% of world consumption (29) [A].
- **Exxon Mobil's Shute Creek plant alone is ~20% of global supply**; the Cliffside-fed pipeline has long supplied about half of US helium (28) [A].
- **Gardner Cryogenics** produces the bulk of the global supply of the superinsulated cylinders helium ships in — a chokepoint in logistics, not production (28) [A].
- Russia's **Amur** plant has not operated since an October 2021 fire and explosion, one month after commissioning; it could add 21–42 million m³/yr (28) [A].
- The **US Federal Helium System was sold to Messer** (German industrial gas group), top bidder in the January 2024 GSA auction; BLM closed the sale in June 2024 (30, 31) [A]. The auctioned package included the 425-mile pipeline and about 51 billion litres of helium (28, 32) [A]. The sale price was not disclosed in the primary sources read (Tier D).
- Research is only **10% of worldwide helium consumption** (28) [A].

Laboratory price data, as reported: PNNL $39/L (double two years earlier), Northwestern ~$30/L (vs $7/L a decade earlier), Marian University $45/L, Western Australia and New Zealand up to Aus$100/L (~$68/L), University of Crete €44/L (from €24/L), Texas A&M $19/L; a Canadian Helium Users Group survey found unscheduled increases of 25% to 400%, and one supplier cut a lab's deliveries from 2,400 L to 962 L per month (28) [A]. USGS price: $7.57/m³ (2020) to a record $14 (2023) (29) [A].

**[B] Is the helium squeeze structural or cyclical?** Consultant Phil Kornbluth expects Qatar's fourth plant plus Russia's new facility to raise global supply ~50% within a few years, making Russia the world's third-largest producer and displacing Algeria (29); he separately estimates that emptying the former federal reserve will take ten years or more (28). Against that, laboratory users and the American Physical Society — which lobbied unsuccessfully for reserve buyers to be required to prioritise scientific users — treat the constraint as persistent, and labs have responded with 75–95%-efficiency recovery systems rather than waiting for supply (28). Both positions are on the record; the disagreement is about timing, not about the concentration.

**[C] Cryogenic physics has no pricing power in the helium market.** Rests on: research being 10% of consumption (28); the sanctions-driven removal of Russian supply (27); a sub-15-firm supplier set (29); and a single US plant representing ~20% of global supply (28). Falsified by evidence that major laboratories hold long-term fixed-price supply contracts that insulate them — a document class I did not find.

# 7. Detector components

## 7.1 Silicon tracking sensors

For the CMS HL-LHC Outer Tracker sensor campaign, **all test structures and sensors were implemented by a single industrial supplier, Hamamatsu Photonics (Japan)**, across float-zone, deep-diffused float-zone and magnetic-Czochralski material at 120–300 µm active thickness (35) [A]. The paper does not state the production award. The ATLAS ITk strip sensor vendor and production totals could not be confirmed (Tier D).

## 7.2 Photomultiplier tubes — the clearest near-monopoly in the chain

Hamamatsu Photonics states that its high-sensitivity photomultiplier tubes let it "capture 90% of the global market," on consolidated sales of ¥212.0 bn and 6,601 employees as of September 2025, across 22 locations in five countries with major factories near Hamamatsu City (33) [A, company claim — no methodology published]. The 90% figure is labelled "PMT market share" in one place and "Top-selling products share" in another on the same page, so treat it as a company claim rather than audited market data (33) [B on the number's precision].

| Instrument | PMTs | Vendor | Source |
|---|---|---|---|
| IceCube | 5,160 DOMs, each a 10-inch Hamamatsu PMT | Hamamatsu (Japan) | (34) |
| IceCube Upgrade | selected | Hamamatsu | (34) |
| IceCube-Gen2 | under consideration | Hamamatsu | (34) |
| Auger fluorescence detector | XP3062 | Photonis | (52) |
| Auger surface detector | 3 × 9-inch per station | not named in source | (51) |
| TAx4 surface detector | R8619 | Hamamatsu (Japan) | (53) |
| JUNO | 15,000 MCP-PMT + 5,000 dynode | NNVT (China) + Hamamatsu (Japan) | (54) |

**JUNO is the one documented case of a deliberate second source at scale.** NNVT (North Night Vision Technology, China) supplies 15,000 20-inch MCP-PMTs and Hamamatsu 5,000 20-inch dynode PMTs, 20,000 total; measured photon detection efficiency averaged 27.5% for NNVT against 28.3% for Hamamatsu, with newer NNVT batches reaching ~30.1% (54) [A]. The source does not state why two suppliers were used (Tier D).

## 7.3 Scintillating crystals — and what actually happened to Russian supply

The documented history (36) [A]:

| Producer | Country | Method | Supplied |
|---|---|---|---|
| BTCP (Bogoroditsk Technical Chemical Plant) | Russia | Czochralski | essentially all high-quality CMS PWO crystals; **"now out of business"** |
| SICCAS (Shanghai Institute of Ceramics, CAS) | China | Bridgman | ~1,825 for CMS; 1,200 for JLab Hybrid EmCal; a few hundred for PANDA (2011–15); ~670 for NPS (2014–19) |
| CRYTUR | Czech Republic | Czochralski, from BTCP pre-production material | ~8,000 expected for the PANDA barrel; ~700 for NPS, ~350 delivered 2018–19 |

SICCAS and CRYTUR are described as **the only two vendors worldwide with PWO mass-production capability**, and the loss of BTCP is said to have significantly changed global availability of high-quality PbWO4 (36) [A].

**Important correction to a common framing: the documented Russian PWO exit is a business failure, not a 2022 sanctions event.** The JLab assessment reporting "BTCP is now out of business" predates February 2022 (36), and PANDA's 2020 document describes BTCP as no longer a current supplier, with Russian involvement reduced to *funding* that PANDA needed by end-2022 (37) [A]. PANDA states there is "currently no alternative plan" for obtaining the required crystals, and names Crytur as the "currently only vendor continuously producing crystals" of satisfactory quality; if Russian funding were severely delayed, PANDA would aim to complete at least 50% of the barrel (37) [A]. I found no document attributing a post-2022 PWO crystal disruption to sanctions (Tier D).

**[B] Is SICCAS-grown PWO acceptable for precision calorimetry?** PANDA says no: it judged SICCAS's Bridgman growth unable to control doping precisely enough and expected an unacceptably high rejection rate, noting SICCAS had shown little interest since 2012 (37). Against that, the JLab/NPS and Hybrid EmCal groups bought and used SICCAS crystals in four-figure quantities (36), and the 2025 DRD calorimetry collaboration still lists SICCAS as a PWO source while reporting that its 2025 BSO samples had worse transmittance and a higher cutoff wavelength than its 2024 ones (39). Named parties on both sides; the disagreement is about tolerance, and it determines whether the world has one PWO supplier or two.

The EIC's electron endcap calorimeter illustrates the live consequence: the first long-lead procurement went to **the US arm of Crytur (Czechia)**, delivering 1,069 accepted PbWO4 crystals of ~3,000 needed, in a three-phase purchase enabled by DOE Critical Decision-3A in April 2024, at ~100–120 crystals per month after a pilot batch; no alternative supplier is mentioned, and a project scientist describes crystal-based technology as "basically the only practical technology" for this calorimeter (38) [A].

Broader crystal and scintillator supplier set as of 2025 (39) [A]: CRYTUR (Czech Republic — GAGG, PWO), ISMA / NAS of Ukraine (YAG via an iridium-free carbon crucible, plastics, BSO/BGSO), SICCAS (China — BSO, PWO), SiPAT (China — large Czochralski ingots), Kuraray, Luxium, Eljen and Nuvia (plastics and fibres), Schott (scintillating glass), Formlabs (bio-resins). Russia does not appear in the 2025 European R&D supplier landscape at all (39) [A].

## 7.4 Silicon photomultipliers

The SiPM market was valued at $152.4 M in 2025, forecast to $208.12 M by 2030 at 6.43% CAGR, with North America 39.0% of 2024 revenue; medical imaging is 45.6% of application revenue and healthcare 47.6% of end-user revenue (40) [A, commercial market report]. **Hamamatsu, onsemi, Broadcom and Teledyne together held roughly 55% of 2024 revenue**; Broadcom acquired KETEK's assets; FBK runs specialty wafer runs for scientific arrays (40) [A]. Barriers to entry cited are patents on quench resistors, deep-trench isolation and digital multiplexing (40) [A].

**[B] How concentrated is the SiPM market?** The same report calls the landscape "moderately concentrated" in its takeaways and rates concentration "High" in its overview table (40). The source contradicts itself; no independent per-vendor SiPM revenue figure was obtainable. The CMS HGCAL/MTD SiPM vendor selection could not be retrieved (Tier D).

Note also that the dominant PMT supplier is also a top-four SiPM supplier and the named CMS tracker sensor supplier — Hamamatsu appears in three separate detector subsystems (33, 35, 40) [A].

# 8. Electronics: FPGAs and the rad-hard ASIC foundries

## 8.1 Custom ASICs

HL-LHC front-end ASICs use standard bulk CMOS at **130 nm and 65 nm**, qualified to 100 and 500 Mrad total ionising dose, with R&D at **28 nm** targeting above 1 Grad (41) [A]. Academic access runs through Europractice and MOSIS, which have served research institutions for over 30 years (41) [A].

CERN's own ASIC support slides are the most specific public document found (42) [A]:

- **TSMC is named as the 28 nm foundry**, with access negotiated through a HEP-specific **three-way NDA between CERN, IMEC and the foundry**.
- The 130 nm and 65 nm foundries are referred to only as "Foundry 1" and "Foundry-2" and are **not named** — see Tier D; this is a case where the information is simply not public.
- Europractice provides mini@sic multi-project wafer runs (1 mm² minimum, charged per 0.1 mm² increment); IMEC QUERIO distributes the PDKs; Cadence VCAD Services holds a separate contract for design-kit maintenance and training.
- Obtaining access to the 28 nm standard-cell back-end views took **more than two years of negotiation**, and 28 nm access depended on the foundry returning a signed NDA.
- 130 nm and 65 nm are now labelled "Legacy Common Design Platforms," and 28 nm HPC support was dropped as runs moved to HPC+.

## 8.2 FPGAs

ATLAS trigger FPGA history, which doubles as a record of vendor dependence (43) [A]:

| Era | Devices | Vendors |
|---|---|---|
| mid-1990s prototype | XC4008, 0.35 µm, 8,000 gates | Xilinx |
| Runs 1–2 (9U VME) | Virtex-E, Virtex-II, Virtex-II Pro, 0.13 µm | Xilinx |
| Run 3 (ATCA L1Calo) | Arria 10; Virtex-7, UltraScale+; 22–14 nm FinFET, up to 2.5 M logic cells, up to 120 transceivers | Altera, Xilinx |
| Run 4 options | Agilex; Versal Prime, Versal AI Core | Intel, Xilinx |

A Run 3 trigger board cost about $40,000 (~£100,000), and ATLAS electronics typically run ~20 years against a much shorter industrial norm; part of the original 9U VME L1Calo system runs to the end of Run 3 (43) [A].

Market structure: Yole forecasts FPGA revenue reaching $15.4 bn by 2029 at a 10% CAGR from 2023; **AMD (which acquired Xilinx in 2022) holds more than 50% of the market at roughly $1 bn revenue per quarter**, Intel (which acquired Altera in 2015) is second, and Microchip, Lattice and Achronix make up the remainder (44) [A].

**[C] HEP trigger systems are locked to a duopoly that consolidated underneath them.** Rests on: every ATLAS trigger generation for 30 years using Xilinx or Altera parts (43); both vendors having since been absorbed into AMD and Intel (44); AMD alone exceeding 50% share (44); and 20-year HEP equipment lifetimes against short commercial support windows (43). The exposure is not price but support horizon: a device family's end-of-life is set by data-centre and telecom demand, not by a 20-year physics programme. Falsified by evidence that HEP buys extended-lifecycle or industrial-grade parts with contractual support windows matching detector lifetimes.

# 9. Computing: the WLCG, its vendors, and cloud encroachment

## 9.1 Structure and scale

| Metric | Value | Source |
|---|---|---|
| Sites / countries | 164 sites, 42 countries | (45) |
| Tier structure | CERN as Tier-0; national Tier-1s; university Tier-2s | (45) |
| 2024 CPU pledge | ~550 kcores | (45) |
| 2024 storage pledge | ~2 EB tape, ~1 EB disk | (45) |
| Transfers | ~260 PB/month | (45) |
| Benchmark | HEPScore 2023 (HS23) for pledges and accounting | (45) |
| Example Tier-1 (Canada, TRIUMF/SFU) | ~9,300 cores, 17 PB disk, 46 PB tape | (45) |

The funding model is the "flat budget model," assuming roughly +15%/yr in CPU, disk and tape at constant funding; recent five-year averages are ~+14% CPU and ~+15% disk, and the WLCG itself calls the flat budget model **"problematic" for Run 4** (45) [A].

## 9.2 Hardware procurement at CERN

CERN's IT hardware procurement runs market survey, invitation to tender, then award on a **"Lowest Compliant"** basis with sample evaluation, and the stated specification philosophy is to be detailed enough to exclude non-compliant bids but not so narrow as to lock in one vendor — e.g. specifying CPUs by HS06 per core and RAM per core rather than by part number (46) [A].

| Tender | Date | CPU | Scale |
|---|---|---|---|
| IT4529 | end 2019 | 2 × Intel Cascade Lake per server | ~1.5 M HS06, 165 PB |
| IT4614/IT4615 | end 2020 | 2 × AMD Rome per server | ~3.6 M HS06, 300 PB, 220k cores, 21.5k drives |
| 2022 (ongoing) | 2022 | not named | ~1.6 M HS06, 200 PB |

CERN's own note is that **AMD's return to competitiveness helps competition in tenders** — i.e. the single-vendor period was a procurement problem, not just a performance one (46) [A]. As of that talk, **no major bulk GPU purchases had been made and GPU procurement had been "very difficult," with long waits** (46) [A]. Commercial cloud is not mentioned in CERN's procurement talk (46), and GPU use in the WLCG appears as HPC-hosted capacity and R&D — GPU-accelerated event generators (up to ~10× for Sherpa) and GPU-based tracking — rather than as owned fleet (45) [A]. The extent of commercial cloud use in LHC computing could not be established in this pass (Tier D).

# 10. CERN's procurement rules and the industrial-return policy

## 10.1 The mechanism, as published

| Element | Rule | Source |
|---|---|---|
| Return coefficient | % of CERN supply-contract expenditure in a Member State ÷ % of that State's contribution to the CERN budget | (47, 48) |
| Measurement window | 4 years; status then applies for 12 months from 1 March | (47, 48) |
| Classification | coefficient <1 = "poorly balanced"; ≥1 = "well balanced" | (47) |
| Price enquiry | CHF 10,000–400,000; 4–6 week deadline; >50k notified to Industrial Liaison Officers; 200k–400k announced on the website | (47) |
| Market survey + invitation to tender | above CHF 400,000; ITT issued only to qualified, selected firms | (47) |
| Award basis | lowest compliant bid (mainly supplies); best value for money (mainly industrial services) | (47) |
| **Price alignment** | above CHF 100,000, on lowest-compliant awards, a bidder whose goods originate ≥60% in poorly balanced Member States may **match** the lowest bid and win (services: ≥40%, by place of establishment). If the threshold is met, the whole bid is treated as originating in a poorly balanced State | (47, 48) |
| **Limited tendering** | targets the **12 most poorly balanced** Member States for supply contracts, where competition is sufficient; a bid is considered only if ≥60% of its value originates there | (47) |
| Country of origin | for supplies, where goods including components and subassemblies are manufactured or undergo their last major transformation | (47) |

Financial scale: CERN's yearly budget ~1,300 MCHF; total procurement expenditure 613 MCHF; supplies in 2024 (CERN budget only) 279 MCHF; largest 2025 contributions Germany 20.10% (254.7 MCHF) and the United Kingdom 14.63% (185.4 MCHF) (47, 48) [A].

Classification for 1 March 2025 – 28 February 2026, as published (48) [A, with a caveat]: **well balanced** — Bulgaria, Croatia*, Czech Republic, Estonia, France, Italy, Pakistan*, Switzerland, Türkiye*, Ukraine*; **poorly balanced** — Austria, Belgium, Brazil*, Cyprus*, Denmark, Finland, Germany, Greece, Hungary, India, Israel, Latvia*, Lithuania*, Netherlands, Norway, Poland, Portugal, Romania, Serbia*, Slovak Republic, Slovenia*, Spain, Sweden, United Kingdom (* = Associate Member State). **Caveat:** the slide layout did not unambiguously label which column was which; the assignment above follows the order of the labels and should be verified against the original before being relied on.

The pattern is worth stating plainly: the two host states (France, Switzerland) and Italy are well balanced; Germany and the UK, CERN's two largest contributors, are poorly balanced (47, 48) [A].

## 10.2 What the policy actually redistributes

The most recent independent analysis is Streicher & Gabelberger (2026), *The Global Value Chains of CERN Procurement: A Time Series Analysis for 1999–2024*, EPJ Research Infrastructures 10:10 (49) [A]:

| Finding | Figure |
|---|---|
| Member states' share of direct contract volume | ~94% |
| Member states' share of total value added (direct + indirect + induced) | ~77% |
| France share of direct procurement | 31% |
| Switzerland share of direct procurement | 27% |
| France + Switzerland share of total estimated economic benefits | ~40% |
| Manufacturing | 52% of direct spending, 32% of value added |
| Services | 21% of direct spending, 46% of value added |
| Non-member states | ~2% of direct awards, 11% of indirect value added (13% including capital replacement) |
| China | 0.2% of direct contracts; indirect/induced value added 0.5% (1999) → ~5.0% (2024) |
| US + Japan (observers) | ~4% of direct contract volume combined |
| Correlation, budget contribution vs direct contract allocation | 56%; **92% excluding the host states** |

The authors note their own limits: the model captures "operational supply-chain mechanics" but excludes "wider long-term technological spillovers, human capital enhancement, or endogenous growth effects"; Israel and Serbia could not be analysed individually for lack of database coverage; and commodity classification used GPT-4.5 with human review of every mapping (49) [A]. The paper does **not** critically evaluate industrial return as a policy (49).

CERN's own supplier engagement: its Procurement and Industrial Services group consulted 1,569 suppliers with orders above CHF 50,000 in 2022–2023; 502 responded, a 32% rate (56) [A].

## 10.3 How return interacts with technical merit — and the comparison that settles it

The key textual point is that price alignment operates **only on lowest-compliant-bid awards**, i.e. only among bids that have already passed the technical specification (47). The policy therefore does not relax technical requirements; it reallocates the award among technically compliant bidders at the same price, since the aligning bidder must match the lowest price (47) [A].

The informative comparison is that peer organisations split on whether to do this at all (50) [A]:

| Organisation | Geographical return | In-kind | Award basis / thresholds |
|---|---|---|---|
| CERN | yes — balance classification + alignment ≥60% | none mentioned | lowest compliant / best value; 400k CHF ITT threshold |
| SKAO | yes — restricted to member countries, defined industrial "fair work return"; European procurement rules do not apply | yes, members procure in-kind under their own rules | — |
| F4E / ITER | open as a rule to EU27, worldwide in justified cases; strategies favour Member-State-registered firms | yes, in-kind to ITER; €2,225 M budget 2024–27 | open/restricted/negotiated/competitive dialogue |
| ESO | favours Member States and host state Chile, "as fair a distribution per country as possible" | yes, instruments for observing nights | lowest compliant or best value, fixed before release; two-envelope |
| ESRF | no fixed rule, but industrial return monitored quarterly with ILO help | — | best value; double envelope above €300k |
| CTAO | not stated | yes — in-kind contributors manage nearly all procurement under national rules | TED above EU thresholds |
| **ESS** | **none** — EU principles of transparency, non-discrimination, competition; tenderers from any country | yes — 40.5% of the €1.843 bn construction cost (€747.5 M) | best value, typically 60–70% technical / 30–40% price |
| **European XFEL** | **explicitly none** — shareholders decided to follow public procurement law so competition is on merit and any business worldwide may bid | construction only | national tenders €25k–€221k; TED above €221k |
| **FAIR** | **"there is no policy of geo-return"** | yes — over half of accelerator components procured in kind from shareholders | calls above €30,000 published |
| ILL | none stated; all suppliers eligible on EU principles | — | — |

**[B] Does industrial return cost technical merit?** Named parties on both sides, from the handbook itself: CERN, ESO and SKAO operate return or national-restriction mechanisms; **European XFEL's shareholders explicitly decided against a fair-return policy so that competition would be on merit**, and ESS and FAIR state they have no geo-return (50). This is a real institutional disagreement among organisations that buy the same classes of hardware from the same vendors — not a commentator's objection. What I did **not** find is a published study comparing outcomes (price, schedule, quality) between return and non-return regimes for comparable procurements; see Tier D.

**[C] Industrial return redistributes which country books the revenue far more than which firm does the work.** Rests on: European XFEL (no return) and LCLS-II (US Best Value) both awarding to Research Instruments and Ettore Zanon (18, 20); the same narrow vendor sets recurring across return and non-return organisations — Air Liquide and Linde for cryoplants (25), Thales and Toshiba for klystrons (21), Bruker for Nb3Sn (7, 8), Hamamatsu for photodetectors (33, 35); and alignment applying only among already-compliant bids (47). On those facts the binding constraint on vendor identity is technical qualification, and return policy operates on the residual. Falsified by showing that return-policy organisations systematically use materially different vendors from non-return organisations for the same component class. Note the counter-consideration this inference does **not** resolve: a well-balanced-state firm that knows its low bid can be matched away has a weaker incentive to bid aggressively, so the policy may still have a price effect through bidding behaviour rather than through award price. No data on that was found.

**[C] In-kind contribution, not industrial return, is the main vehicle by which national politics shapes who builds large physics facilities.** Rests on: ESS at 40.5% in-kind (€747.5 M), FAIR at over half of accelerator components in-kind, CTAO with nearly all procurement managed by in-kind contributors under national rules, SKAO with members procuring in-kind under their own rules, and HL-LHC's highest-technology magnets built by BNL/FNAL/LBNL/CERN rather than tendered at all (10, 50). Where work is in-kind, it never enters a competitive tender and no return coefficient applies to it. Falsified by evidence that in-kind work packages are themselves competitively tendered internationally. This matters for any assessment of the sector: a procurement-rules analysis that looks only at tenders misses the majority of the construction effort at several of these facilities.

# 11. Astroparticle instruments

## 11.1 Pierre Auger Observatory

| Component | Supplier | Country | Source |
|---|---|---|---|
| Surface detector PMTs | 3 × 9-inch per station; manufacturer not named in source | — | (51) |
| Fluorescence detector PMTs | Photonis XP3062, 8-stage hexagonal, bialkali | France | (52) |
| UV filter glass | Schott MUG-6 | Germany | (52) |
| Corrector ring glass | Schott BK7 | Germany | (52) |
| Corrector ring segments | Schwantz Ltd | — | (52) |
| PMT head electronics | Intratec-Elbau, Berlin | Germany | (52) |
| Water tanks | rotationally moulded HDPE; **four companies** produced tanks | — | (51) |
| Liner reflective layer | DuPont Tyvek 1025-BL | USA | (51) |
| Batteries | Acumuladores Moura S.A., model 12MC105 | Brazil | (51) |
| Charge controller | Morningstar SunSaver SS-10-24V | USA | (51) |
| GPS | Motorola Oncore UT+ | USA | (52) |
| Solar panels | 2 × 55 Wp; manufacturer not named | — | (51) |

Auger qualified the *production process* rather than selecting a sole vendor: 32 prototypes in an Engineering Array, then a pre-production run of 100 detectors to qualify the process (51) [A]. No sole-source procurement is described (51).

## 11.2 Telescope Array / TAx4

| Component | Supplier | Country | Source |
|---|---|---|---|
| PMTs | Hamamatsu R8619 | Japan | (53) |
| Wavelength-shifting fibre | Kuraray Y-11 | Japan | (53) |
| Wireless LAN module | WiVi-Com WVCWB-R-022(05) — replaced the TA module, which went out of production | — | (53) |
| Tower access point | Cisco Aironet AP1572E-Q-K9 | USA | (53) |
| Tower DAQ computer | Raspberry Pi 2 Model B | UK | (53) |
| GPS receiver | i-Lotus M12M | — | (53) |
| Scintillator | not named | — | (53) |

257 surface detectors were deployed in February–March 2019 of ~500 planned; scintillator boxes were assembled mostly in Japan with 30 in Korea in 2018, PMTs attached before shipping, final assembly in Utah (53) [A]. Note the obsolescence signature: the original wireless module went out of production and had to be replaced mid-project (53) [A].

## 11.3 IceCube and CTA

IceCube: 5,160 spherical DOMs each with a 10-inch Hamamatsu PMT; Hamamatsu PMTs were also selected for the IceCube Upgrade and are under consideration for IceCube-Gen2 (34) [A]. Hamamatsu makes no sole-supplier claim (34).

CTAO procurement is structurally different: in-kind contributors manage nearly all project procurement under their own national rules, with tenders above EU thresholds published on TED (50) [A]. The CTA small-sized-telescope SiPM vendor selection could not be retrieved (Tier D).

# 12. Light sources and XFELs as the commercial tail

The same firms and the same technology base serve a market far larger than particle physics (55) [A]:

| Metric | Figure |
|---|---|
| Accelerators built in 60 years | >30,000; more than half for industrial purposes |
| Industrial accelerator shipments | ~1,000 systems/yr, sales >$2 bn |
| Industrial electron-beam irradiation market | ~$90 bn/yr worldwide |
| Semiconductor components made with ion implantation | >$250 bn/yr |
| Commercial value of products touched by a charged-particle beam | >$500 bn/yr |
| Cyclotrons worldwide | ~650, of which ~350 for PET radionuclides |

Industry installs new systems almost twice as fast as research and medical therapy combined, and most industrial applications evolved from science programmes using research accelerators — but industry's demands for reliability and cost drove advances back the other way, including negative-ion cyclotron acceleration and RFQ structures for ion linacs (55) [A].

The direct, traceable tail of the HEP supply chain shows up most clearly in SRF and RF power: the two cavity vendors serving European XFEL and LCLS-II are the same two (18, 20); the SSA designs developed for SOLEIL and ESRF were transferred to ELTA and reused at LNLS and SESAME (23); and the klystron makers serving XFEL are the same houses that serve radar and broadcast (21, 24) [A].

**[C] Light sources and XFELs are what keeps the HEP vendor base alive between colliders.** Rests on: the documented post-LHC collapse of superconductor demand back to the MRI base load (1); the DOE finding that accelerator conductor manufacturing is sustained only by non-HEP revenue and may need deliberate ~1 t/yr purchases to stay alive (7); and the same two SRF vendors carrying both the European and US flagship linacs across a decade (18, 20). Falsified by evidence that HEP-specific product lines are profitable on HEP orders alone. The practical implication is that a collider programme's hardware feasibility depends on the light-source and medical-device order book, over which the physics community has no control.

# 13. Single-vendor and near-monopoly map

| Layer | Component | Dependency | Tier |
|---|---|---|---|
| Raw material | Niobium ore | **Brazil ~93% of world mine production; CBMM ~77–90%**; US 100% import-reliant with zero production | [A] (12, 13, 14, 15) |
| Raw material | Helium | US + Qatar >75% of consumption; <15 supplier firms; one US plant ~20% of global supply; Russian supply sanctioned out | [A] (27, 28, 29) |
| Raw material | High-RRR Nb sheet | Ningxia OTIC (China) + Tokyo Denkai (Japan) are the main suppliers; the last US source fell to ~3 t/yr | [A] (17) |
| Conductor | Accelerator-grade Nb3Sn | HL-LHC specification met by **one** supplier (Bruker OST); Bruker EAS the only high-volume PIT maker | [A] (7, 8) |
| Conductor | Nb3Sn PIT | **Bruker EAS, world's only high-volume manufacturer** | [A] (8) |
| Magnets | Main-ring dipoles (LHC) | three consortia (France, Italy, Germany) — a deliberate three-way split | [A] (2, 3) |
| Cryogenics | Large helium turbo-expanders | **"Only two companies in the world"** — Air Liquide, Linde | [A] (25) |
| RF | Multibeam klystrons | three vendors qualified, **two selected** (Thales, Toshiba) | [A] (21) |
| RF | ESRF-class klystron tube | **one of three original makers still produced it** | [A] (23) |
| RF | SSA LDMOS transistors | commercial market; one named device (NXP BLF578) dominant in the leading design | [A] (23) |
| SRF | Flagship cavity fabrication | **two firms** — Research Instruments (DE), Ettore Zanon (IT) — hold E-XFEL and LCLS-II | [A] (18, 20) |
| SRF | Complete US cryomodules | **one** named capable US company (Advanced Energy Systems) | [A] (17) |
| Detectors | Photomultiplier tubes | **Hamamatsu claims 90% of the global market** | [A, company claim] (33) |
| Detectors | Silicon strip sensors (CMS OT campaign) | **single supplier** used for all test structures and sensors (Hamamatsu) | [A] (35) |
| Detectors | PWO scintillating crystals | **two mass-production vendors worldwide** (SICCAS, CRYTUR); PANDA calls Crytur the only continuous producer of satisfactory quality; EIC bought from Crytur alone | [A] (36, 37, 38) |
| Detectors | SiPMs | top four ~55% of revenue; patent barriers on quench resistors, deep-trench isolation, digital multiplexing | [A] (40) |
| Electronics | 28 nm rad-hard ASIC foundry | **TSMC**, under a three-way CERN–IMEC–foundry NDA | [A] (42) |
| Electronics | FPGAs | **AMD >50% share; AMD + Intel absorbed both historic HEP vendors** | [A] (43, 44) |
| Computing | Server CPUs | effectively Intel/AMD; CERN notes AMD's return restored tender competition | [A] (46) |
| Computing | Bulk GPUs | procurement "very difficult," no major bulk purchase at CERN as of the source | [A] (46) |
| Logistics | Helium shipping cylinders | **Gardner Cryogenics produces the bulk of global supply** | [A] (28) |

# 14. Geopolitical exposure

Stated as facts, with the inference flagged separately.

**[A] Documented exposures.** Brazil holds ~93% of niobium mine production and CBMM, which supplies most of it, is 30% owned by a Chinese consortium and a Japanese/Korean consortium in equal 15% shares (12, 13, 14). The US has no niobium production and 100% import reliance, with 67% of imports from Brazil (12). China holds the world's leading industrial position in high-purity niobium sheet and is described as self-sufficient across SRF technology, while the last US sheet source shrank to ~3 t/yr (17). The world's largest helium resources sit in Qatar, Algeria and Russia (27); Russian helium is under EU and US import bans continuing into 2025 (27); Russia's Amur plant has been down since an October 2021 explosion (28); and the US Federal Helium System now belongs to Messer, a German group (30, 31, 32). Accelerator-grade Nb3Sn comes from one qualified supplier (7). The 28 nm rad-hard ASIC node is TSMC's (42). Russia's Bogoroditsk plant, which made essentially all of CMS's PWO crystals, is out of business, leaving two PWO vendors worldwide, one Chinese and one Czech (36, 37).

**[C] The European-led and US-led programmes have diverged in their dependence on China, and neither has publicly measured it.** Rests on: Chinese firms supplying high-purity Nb sheet to E-XFEL as a qualified vendor (18) and being the main current sheet supplier (17); SICCAS and SiPAT as PWO/BSO sources in the 2025 European R&D landscape with Russia absent (39); NNVT supplying 15,000 of JUNO's 20,000 large PMTs (54); and China receiving only 0.2% of CERN's *direct* contracts while its share of indirect and induced value added rose from 0.5% to ~5.0% between 1999 and 2024 (49). The last figure is the important one: CERN's industrial-return accounting measures direct contracts, where China is negligible, and does not measure the supply chain behind them, where China's share grew tenfold. Falsified by a published tier-2/tier-3 origin audit of CERN or DESY procurement showing low non-member content. **This is an observation about what is and is not measured, not a claim that anyone concealed anything** — Streicher & Gabelberger built their estimate precisely because the direct-contract data does not capture it, and published it.

**[C] The single most likely hardware-driven failure mode for a next-generation collider is conductor, not magnets.** Rests on: FCC-scale demand of 8,000–10,000 t of Nb3Sn (7, 9) against current world RRP output of 5–10 t/yr and PIT output under 1 t/yr (7); DOE's statement that no superconductor is made at the scale a high-energy or muon collider needs (7); a 12–18 month lead time and a ~5 year gap before alternative manufacturing could emerge (7); and the absence of margins in the Nb-Ti MRI business to fund the expansion (7). Falsified by a credible industrial capacity-expansion commitment from any Nb3Sn producer, or by a shift to HTS at qualified accelerator specification. The field states the input facts openly; what is missing is a published, costed industrialisation plan. A three-orders-of-magnitude scale-up in a product with no commercial demand outside the project is the kind of problem that is identified late because it belongs to no single technical work package.

# Claims Examined and Not Supported

Tier D. Everything below was investigated in this pass and could **not** be substantiated. Several items are cases where the information is simply not public; those are marked as such, and absence of data is not treated as evidence of anything.

**Could not be retrieved (access or budget limits, not absence of the information):**

1. **ATLAS ITk strip sensor vendor, production totals and yield.** The relevant CERN Document Server PDFs returned an Anubis bot-protection challenge through WebFetch, and `cds.cern.ch` was refused outright by this session's network policy. The Hamamatsu-sole-vendor claim for ITk is widely assumed but is **not substantiated here**.
2. **CMS HGCAL and MIP Timing Detector SiPM vendor selection, quantities and area.** arXiv:2606.13956 was rate-limited on five consecutive attempts.
3. **The CTA small-sized-telescope SiPM vendor selection.** The ScienceDirect article returned a client error.
4. **LHC Project Report 660 and Report 797** (full magnet and 1.8 K refrigeration procurement detail). Both blocked at CDS.
5. **CERN 2024 Financial Statements** detail on procurement. The indico attachment returned a client error.
6. **Air Liquide's unit count for the eight 2.4 kW @ 1.8 K units.** IHI/Linde's four are documented (26); the remaining four are a reasonable inference from the eight-unit total but the source does not state it, so it is not asserted here.
7. **Toshiba's electron-tube business transfer to Canon** (relevant because the XFEL klystron vendor's corporate identity changed). Could not verify; the web-search budget was exhausted and no primary source was reachable.
8. **Commercial cloud use in LHC computing.** The ATLAS commercial-clouds paper was unreachable on ResearchGate; CERN's own procurement talk does not mention cloud. The scale of commercial cloud encroachment is therefore **unestablished**, in either direction.

**Not public, as far as this pass could determine:**

9. **Per-firm contract values for the three LHC dipole consortia.** Only an aggregate of "exceeding 300 M" is published (2). Individual values appear to be withheld as commercially confidential — a normal practice, not an anomaly.
10. **The identity of CERN's 130 nm and 65 nm ASIC foundries.** CERN's own internal slides call them "Foundry 1" and "Foundry-2" and do not name them (42). The 28 nm foundry is named as TSMC because the access NDA is described (42). This is a genuine, documented non-disclosure, and it is almost certainly a foundry NDA requirement rather than anything else.
11. **The complete list of LHC Nb-Ti strand suppliers.** CERN's outreach page names Furukawa as one of two main cable suppliers without naming the second (4); the authoritative magnet paper names none (2). The frequently repeated figure of six qualified strand suppliers has no primary source in this pass.
12. **Messer's purchase price for the US Federal Helium System.** Neither the BLM release (30) nor the trade press report (31) discloses it. A figure of roughly $425 M circulates; it is **not confirmed by any primary source read here** and is not used in this file.
13. **Per-country CERN procurement spend tables.** The published presentations embed them as images; the figures are not in the extractable text (47, 48).
14. **Per-vendor SiPM and klystron revenue shares.** Only paywalled market-report titles were found. The only accessible concentration statements are Mordor's top-four ~55% (40) and ESRF's "one of three original makers" (23).
15. **Hamamatsu's 90% PMT share methodology.** It is a company claim on a company page, labelled inconsistently on that page ("PMT market share" in one place, "Top-selling products share" in another), with no published methodology (33). Treat it as a credible indicator, not a measured figure.
16. **Bruker's position on consolidating OST manufacturing overseas.** DOE named the risk and a 2024 timeframe (7); no Bruker statement, confirmation or denial was found.
17. **Any published outcome comparison between geographical-return and non-return procurement regimes.** The handbook documents that CERN, ESO and SKAO use return mechanisms while European XFEL, ESS, FAIR and ILL explicitly do not (50), and Streicher & Gabelberger quantify where CERN's value lands (49) — but no study compares price, schedule or quality outcomes across the two regimes for comparable hardware. The [B] disagreement in §10.3 is therefore unresolved on the evidence, and **this file does not conclude that industrial return harms technical merit.**
18. **Bid-level data on whether price alignment changes bidding behaviour.** The mechanism creates an incentive question (§10.3) that no public data answers.

**Premises examined and found to be wrong or unsupported:**

19. **"Russian crystal supply was lost after 2022."** Not supported. The documented loss of Bogoroditsk Technical Chemical Plant is a business failure reported *before* February 2022 (36), and PANDA's 2020 document already treats BTCP as a former supplier whose remaining relevance was Russian *funding*, not crystals (37). No document was found attributing a post-2022 PWO supply disruption to sanctions or to the war. The 2025 European crystal R&D landscape simply does not list Russia (39). The real event was earlier and commercial. Anyone writing about this should not date it to 2022.
20. **"CERN's industrial return policy lets politically favoured firms win on non-technical grounds."** Not supported as stated. Price alignment operates only among bids that have already passed the technical specification, on lowest-compliant awards above CHF 100,000 (47). The policy reallocates awards among compliant bidders at a matched price; it does not document any mechanism for relaxing technical requirements. A sharper and supportable version of the concern is about *bidding incentives* and about *in-kind work that never enters a tender at all* (§10.3).
21. **"CERN's supply chain is captured by its largest contributors."** Not supported — the data points the other way. CERN's two largest contributors, Germany (20.10%) and the United Kingdom (14.63%), are classified **poorly balanced**, while the host states France and Switzerland take 31% and 27% of direct procurement (47, 48, 49). The documented skew is toward the host states, which is what proximity to a construction site in Geneva would predict, and the correlation between contribution and contract allocation rises from 56% to 92% once the host states are removed (49) — i.e. outside the host states the policy appears to work roughly as designed.
22. **A single global "detector electronics foundry monopoly."** Not supported. HEP uses at least three distinct nodes across at least two unnamed foundries plus TSMC at 28 nm, with MPW access through two separate brokers, Europractice and MOSIS (41, 42). The documented dependency is node-specific and NDA-mediated, not a single-foundry monopoly.

**On reading absence of data:** for items 9–16 above, the most likely explanation is ordinary commercial confidentiality and the small size of these markets, not concealment. Supply chains with three customers and two suppliers do not publish prices, anywhere in industry. Nothing in this file should be read as inferring capture from the absence of disclosure.

# References

1. CERN Courier, "Superconductors and particle physics entwined." https://cerncourier.com/a/superconductors-and-particle-physics-entwined/
2. L. Rossi, "The LHC Superconducting Magnets," PAC 2003. https://proceedings.jacow.org/p03/PAPERS/TOAB001.PDF
3. CERN Courier, "Industry delivers LHC dipole coils." https://cerncourier.com/a/industry-delivers-lhc-dipole-coils/
4. CERN, "LHC superconducting cable," LHC Machine Outreach. http://lhc-machine-outreach.web.cern.ch/components/cable.htm
5. Furukawa Electric, "Low Temperature Superconductors: Contribution to Advanced Technology" (product catalogue). https://www.furukawaelectric.com/en/product/catalogue/pdf/superconductor_se001.pdf
6. Wikipedia, "Niobium–titanium." https://en.wikipedia.org/wiki/Niobium%E2%80%93titanium
7. US DOE Office of Science / ARDAP, "Business Models to Assure Availability of Advanced Superconductors for the Accelerator Sector and Promote Stewardship of Superconducting Magnet Technology for the US Economy" (2023). https://science.osti.gov/-/media/ardap/pdf/2023/SC_Business_Models_2023.pdf
8. Lawrence Berkeley National Laboratory, Nb3Sn conductor review (LBL Publications). https://escholarship.org/content/qt2mg2k6h7/qt2mg2k6h7.pdf
9. A. Ballarino, "Development of Superconductors for Future Large Scale Applications," MT25. https://indico.cern.ch/event/445667/contributions/2567038/attachments/1514959/2363874/Pl3-01_MT25_Ballarino.pdf
10. CERN Courier, "HL-LHC magnets enter production in the US." https://cerncourier.com/a/hl-lhc-magnets-enter-production-in-the-us/
11. ASG Superconductors, "Company." https://www.asgsuperconductors.com/company
12. US Geological Survey, Mineral Commodity Summaries 2026 — Niobium (Columbium). https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-niobium.pdf
13. Wikipedia, "Companhia Brasileira de Metalurgia e Mineração." https://en.wikipedia.org/wiki/Companhia_Brasileira_de_Metalurgia_e_Minera%C3%A7%C3%A3o
14. Geopolitical Monitor, "Critical Minerals: Global Niobium Supply & Demand." https://www.geopoliticalmonitor.com/critical-minerals-global-niobium-supply-demand/
15. Critical Minerals News, "Niobium Producers: Top 10 Companies in 2026." https://critical-minerals-news.com/top-10-niobium-producers/
16. G. Ciovati, "Cavity Fabrication," US Particle Accelerator School 2015. https://uspas.fnal.gov/materials/15Rutgers/Cavity_Fabrication.pdf
17. NAPAC 2025, "A plan to revitalize the domestic superconducting radiofrequency industry." https://proceedings.jacow.org/napac2025/pdf/WEYD01_talk.pdf
18. SRF 2013, "The Challenge and Realization of the Cavity Production and Treatment in Industry for the European XFEL." https://proceedings.jacow.org/SRF2013/papers/moioa03.pdf
19. SRF 2013, "Quality Assurance and Acceptance Testing of Niobium" (FRIB). https://proceedings.jacow.org/SRF2013/papers/mop033.pdf
20. SRF 2015, "Cavity Procurement and Qualification Plan for LCLS-II." https://epaper.kek.jp/SRF2015/papers/tupb003.pdf
21. "The High Power RF System for the European XFEL." https://inspirehep.net/files/3b93ce0f8d13ec76db299a33e4e90dc0
22. LINAC 2014, "Testing of the First Part of Series Production 10 MW MBKs for the XFEL Project." https://proceedings.jacow.org/LINAC2014/papers/tupp023.pdf
23. J. Jacob (ESRF), "Radio Frequency Solid State Amplifiers," arXiv:1607.01570. https://arxiv.org/pdf/1607.01570
24. Wikipedia, "CPI International." https://en.wikipedia.org/wiki/CPI_International
25. CERN Courier, "CERN's giant fridge." https://cerncourier.com/a/cerns-giant-fridge/
26. Ph. Lebrun and L. Tavian, "Cooling with Superfluid Helium," arXiv:1501.07156. https://arxiv.org/pdf/1501.07156
27. US Geological Survey, Mineral Commodity Summaries 2026 — Helium. https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-helium.pdf
28. Physics Today, "Helium prices surge to record levels as shortage continues" (2023). https://physicstoday.aip.org/news/helium-prices-surge-to-record-levels-as-shortage-continues
29. MIT Technology Review, "The era of cheap helium is over—and that's already causing problems" (25 Feb 2024). https://www.technologyreview.com/2024/02/25/1088930/global-helium-market-semiconductors/
30. US Bureau of Land Management, "BLM completes sale of Federal Helium System" (27 June 2024). https://www.blm.gov/press-release/blm-completes-sale-federal-helium-system
31. gasworld, "Messer finalises purchase of Federal Helium Reserve." https://www.gasworld.com/story/messer-finalises-purchase-of-federal-helium-reserve/2140712.article/
32. Wikipedia, "National Helium Reserve." https://en.wikipedia.org/wiki/National_Helium_Reserve
33. Hamamatsu Photonics, "Hamamatsu at a glance." https://www.hamamatsu.com/jp/en/our-company/at-a-glance.html
34. Hamamatsu Photonics, "How Hamamatsu Photonics' technology supports IceCube" (Nov 2026). https://www.hamamatsu.com/jp/en/news/featured-products_and_technologies/2026/20261104000000.html
35. CMS Tracker Group, "Experimental Study of Different Silicon Sensor Options for the Upgrade of the CMS Outer Tracker," arXiv:2001.02023. https://arxiv.org/pdf/2001.02023
36. "Scintillating crystals for the Neutral Particle Spectrometer in Hall C at JLab," arXiv:1911.11577. https://arxiv.org/pdf/1911.11577
37. PANDA Collaboration, "Answers to the Questions of the FAIR ECE regarding the Update to the EMC TDR," RE-TDR-2020-007. https://www-panda.gsi.de/system/files/user_uploads/heinsius%40ep1.rub.de/RE-TDR-2020-007_0.pdf
38. Jefferson Lab, "First Procurement Contract Complete for New EIC Detector." https://www.jlab.org/news/stories/first-procurement-contract-complete-new-eic-detector
39. DRD Calorimetry WP3 Task 3.4.1 SCINTCAL status (3 April 2025). https://indico.ijclab.in2p3.fr/event/11400/contributions/37605/attachments/25409/37365/DRDcalo_WP3_Scintcal03042025.pdf
40. Mordor Intelligence, "Silicon Photomultiplier Market Size, Share & 2025-30 Outlook." https://www.mordorintelligence.com/industry-reports/silicon-photomultiplier-market
41. J. Kaplon (CERN), "Radiation hard Electronics for High Energy Physics Experiments." https://indico.cern.ch/event/1389825/contributions/5885829/attachments/2840571/4965074/RadHardElectronicsESEME.pdf
42. CERN, "ASIC Support news and EP R&D WP5 developments" (5 October 2021). https://indico.cern.ch/event/1071292/contributions/4535498/attachments/2322387/3955641/2021.10.05_MUG_ASIC_Support_and_WP5_v1.3.pdf
43. W. Qian, "ATLAS experience with FPGA (TDAQ's perspective)." https://indico.ihep.ac.cn/event/9960/contributions/113747/attachments/61194/70564/CEPC_TDAQ_ATLAS-FPGAusage_v1.pdf
44. Yole Group, "FPGA market set for steady demand growth." https://www.yolegroup.com/strategy-insights/fpga-market-set-for-steady-demand-growth/
45. R. Tafirout, "Discovery, accelerated" — WLCG status, TRIUMF Science Week 2024. https://indico.triumf.ca/event/509/contributions/5141/attachments/3555/5548/WLCG_ScienceWeek2024.pdf
46. CERN IT, "Procurement," HEPiX 2022. https://indico.cern.ch/event/1200682/contributions/5087578/attachments/2539878/4372140/HEPiX_2022_Procurement_CERN.pdf
47. CERN Procurement, "Doing Business with CERN," FCC Week (21 May 2025). https://indico.cern.ch/event/1507998/contributions/6346528/attachments/3072337/5435601/FCC%20Week%20-%20Procurement%20Presentation%202025_05_21.pdf
48. CERN Procurement, "Doing Business with CERN," UK Meet the Buyer (2 April 2025). https://indico.global/event/14316/contributions/123839/attachments/57637/110712/Procurement%20Presentation%202025_04_02.pdf
49. G. Streicher and F. Gabelberger, "The Global Value Chains of CERN Procurement: A Time Series Analysis for 1999–2024," EPJ Research Infrastructures 10(1):10 (2026), DOI 10.1007/s41781-026-00165-8; reported at https://bioengineer.org/cern-procurement-stimulates-far-reaching-global-value-chains-beyond-member-nations/
50. Big Science Business Forum, "BSBF 2024 Procurement Handbook." https://visits.bsbf2024.org/dl/3e28309f-ef9f-430c-b828-3d74b354f0a1/Procurement_Handbook_2024.pdf
51. Pierre Auger Collaboration, "The Surface Detector System of the Pierre Auger Observatory," FERMILAB-PUB-07-664-E-TD. https://lss.fnal.gov/archive/2007/pub/fermilab-pub-07-664-e-td.pdf
52. Pierre Auger Collaboration, "The Fluorescence Detector of the Pierre Auger Observatory," arXiv:0907.4282. https://arxiv.org/pdf/0907.4282v1
53. Telescope Array Collaboration, "Surface detectors of the TAx4 experiment," arXiv:2103.01086. https://arxiv.org/pdf/2103.01086
54. Z. Qin (IHEP), "The 20-inch PMT system for the JUNO experiment," ICHEP 2018. https://indico.cern.ch/event/686555/contributions/2972208/attachments/1682285/2703107/The20inchPMTSystem-ICHEP2018-V2.pdf
55. Physics Today, "The beam business: Accelerators in industry." https://physicstoday.aip.org/features/the-beam-business-accelerators-in-industry
56. CERN Knowledge Transfer Report 2024, "Innovation Through Supply and Service Contracts." https://report2024-kt.web.cern.ch/innovation-through-supplies-and-services-contracts/
