"""Hand-built SVG figures for the research findings, in English and French.

No dependencies, no runtime JS. Colours come from the page's CSS custom
properties so the figures theme with the site and invert correctly in print.
Every figure states its own source in the caption.
"""

SVG_STYLE = """
<style>
  .f-lbl   { font: 600 12px var(--sans, sans-serif); fill: var(--ink, #eee); }
  .f-sub   { font: 400 11px var(--sans, sans-serif); fill: var(--ink-faint, #777); }
  .f-num   { font: 700 15px var(--sans, sans-serif); fill: var(--ink-bright, #fff);
             font-variant-numeric: tabular-nums; }
  .f-big   { font: 700 26px var(--sans, sans-serif); fill: var(--accent, #e0a33c);
             font-variant-numeric: tabular-nums; letter-spacing: -0.02em; }
  .f-axis  { stroke: var(--rule, #2a2a2e); stroke-width: 1; }
  .f-bar   { fill: var(--accent, #e0a33c); }
  .f-bar-d { fill: var(--tier-d, #c0564e); }
  .f-bar-a { fill: var(--tier-a, #4e9e73); }
  .f-bar-c { fill: var(--tier-c, #5b8dc9); }
  .f-bar-b { fill: var(--tier-b, #d99a2b); }
  .f-mute  { fill: var(--bg-inset, #1b1b1e); }
  .f-rule  { stroke: var(--rule-soft, #1e1e21); stroke-width: 1; }
</style>
"""


def _wrap(view, body):
    return (f'<svg viewBox="0 0 {view}" xmlns="http://www.w3.org/2000/svg" '
            f'role="img">{SVG_STYLE}{body}</svg>')


def _n(v, lang):
    """Thin-space thousands separator in French, comma in English."""
    return f"{v:,}".replace(",", " ") if lang == "fr" else f"{v:,}"


# --------------------------------------------------------------- figure 1

TRIG = {
    "en": dict(s1="Bunch crossings", s2="After Level-1 (hardware, &lt;2.5 µs)",
               s3="After high-level trigger", rej="rejected",
               lost="not recoverable", full="Data rate if everything were read out",
               writ="Data rate actually written", tot="total rejection factor"),
    "fr": dict(s1="Croisements de paquets", s2="Après le niveau 1 (matériel, &lt;2,5 µs)",
               s3="Après le déclencheur de haut niveau", rej="rejetés",
               lost="non récupérables", full="Débit si tout était lu",
               writ="Débit réellement enregistré", tot="facteur de rejet total"),
}


def trigger_cascade(lang="en"):
    """What the LHC keeps, stage by stage. Log-scaled bars with stated ratios."""
    import math
    t = TRIG[lang]
    stages = [(t["s1"], 40_000_000, "40 MHz", "f-bar"),
              (t["s2"], 100_000, "100 kHz", "f-bar-b"),
              (t["s3"], 3_000, "3 kHz", "f-bar-d")]
    x0, w, top, bh, gap = 240, 470, 42, 34, 46
    lo, hi = math.log10(1_000), math.log10(40_000_000)
    rows = []
    for i, (label, val, disp, cls) in enumerate(stages):
        y = top + i * gap
        bw = max(4, (math.log10(val) - lo) / (hi - lo) * w)
        rows.append(
            f'<text class="f-lbl" x="{x0-14}" y="{y+bh*0.62}" text-anchor="end">{label}</text>'
            f'<rect class="{cls}" x="{x0}" y="{y}" width="{bw:.1f}" height="{bh}" rx="2"/>'
            f'<text class="f-num" x="{x0+bw+12}" y="{y+bh*0.68}">{disp}</text>')
        if i:
            rows.append(
                f'<text class="f-sub" x="{x0+4}" y="{y-7}">↓ {t["rej"]} '
                f'{_n(stages[i-1][1]//val, lang)}× — {t["lost"]}</text>')
    rows.append(f'<line class="f-axis" x1="{x0}" y1="{top-22}" x2="{x0}" y2="{top+3*gap-4}"/>')
    rows.append(
        '<g transform="translate(240,196)">'
        f'<text class="f-sub" x="0" y="0">{t["full"]}</text>'
        '<text class="f-num" x="0" y="22">40 TB/s</text>'
        f'<text class="f-sub" x="190" y="0">{t["writ"]}</text>'
        '<text class="f-num" x="190" y="22">~1 GB/s</text>'
        f'<text class="f-big" x="360" y="20">{_n(13000, lang)}×</text>'
        f'<text class="f-sub" x="360" y="38">{t["tot"]}</text></g>')
    return _wrap("800 250", "".join(rows))


# --------------------------------------------------------------- figure 2

DISS = {
    "en": dict(cats=["Priority &amp; cost", "Epistemic &amp; sociological", "Safety",
                     "Specific result", "Validity of the physics"],
               head="60 documented confrontations, 1961–2026 — a floor, not a census",
               big="3 of 60", l1="dispute the physics itself",
               l2="none of the three is a", l3="practising particle physicist",
               r1="All 36 scientists in the priority and epistemic categories —",
               r2="including five Nobel laureates — concede in writing that",
               r3="the machines work and the Standard Model is confirmed."),
    "fr": dict(cats=["Priorités et coûts", "Épistémique et sociologique",
                     "Sûreté", "Résultat précis", "Validité de la physique"],
               head="60 confrontations documentées, 1961–2026 — un plancher, non un recensement",
               big="3 sur 60", l1="contestent la physique elle-même",
               l2="aucune des trois n’est", l3="physicien des particules en exercice",
               r1="Les 36 scientifiques des catégories priorités et",
               r2="épistémique — dont cinq lauréats Nobel — concèdent",
               r3="que les machines fonctionnent et le Modèle standard tient."),
}


def dissent_ratio(lang="en"):
    """60 confrontations by category; the validity segment is the finding."""
    d = DISS[lang]
    counts, classes = [21, 15, 12, 9, 3], ["f-bar", "f-bar-c", "f-bar-b", "f-bar-a", "f-bar-d"]
    total = sum(counts)
    x0, w, y, h = 40, 720, 60, 46
    x, segs = x0, []
    for label, n, cls in zip(d["cats"], counts, classes):
        sw = n / total * w
        segs.append(f'<rect class="{cls}" x="{x:.1f}" y="{y}" width="{sw-2:.1f}" height="{h}" rx="2"/>')
        if n > 5:
            segs.append(f'<text class="f-num" x="{x+sw/2:.1f}" y="{y+h*0.64}" text-anchor="middle">{n}</text>')
        x += sw
    keys, kx = [], x0
    for label, n in zip(d["cats"], counts):
        cls = classes[d["cats"].index(label)]
        keys.append(f'<g transform="translate({kx},{y+h+34})">'
                    f'<rect class="{cls}" x="0" y="-9" width="10" height="10" rx="2"/>'
                    f'<text class="f-sub" x="16" y="0">{label} · {n}</text></g>')
        kx += 152
    ann = (f'<text class="f-sub" x="{x0}" y="36">{d["head"]}</text>'
           f'<g transform="translate({x0+w-96},{y+h+72})">'
           f'<text class="f-big" x="96" y="0" text-anchor="end">{d["big"]}</text>'
           f'<text class="f-sub" x="96" y="18" text-anchor="end">{d["l1"]}</text>'
           f'<text class="f-sub" x="96" y="34" text-anchor="end">{d["l2"]}</text>'
           f'<text class="f-sub" x="96" y="48" text-anchor="end">{d["l3"]}</text></g>'
           f'<g transform="translate({x0},{y+h+72})">'
           f'<text class="f-lbl" x="0" y="0">{d["r1"]}</text>'
           f'<text class="f-lbl" x="0" y="18">{d["r2"]}</text>'
           f'<text class="f-lbl" x="0" y="36">{d["r3"]}</text></g>')
    line = (f'<line class="f-rule" x1="{x0+w-6:.1f}" y1="{y+h+4}" '
            f'x2="{x0+w-6:.1f}" y2="{y+h+60}" stroke-dasharray="2 3"/>')
    return _wrap("800 250", ann + "".join(segs) + line + "".join(keys))


# --------------------------------------------------------------- figure 3

FCC = {
    "en": dict(head="2019 conceptual design → 2025 feasibility study",
               rows=[("Projected cost", "~€9 bn", "CHF 15.3 bn"),
                     ("Tunnel circumference", "100 km", "90.7 km"),
                     ("Second-stage energy", "100 TeV", "85 TeV"),
                     ("Operations begin", "late 2050s", "early 2070s")],
               f1="Cost up. Specification down. Schedule out by roughly fifteen years.",
               f2="Panel cost figures are taken from the proponents; the subcommittee was barred from producing its own."),
    "fr": dict(head="Conception de 2019 → étude de faisabilité de 2025",
               rows=[("Coût projeté", "~9 G€", "15,3 G CHF"),
                     ("Circonférence du tunnel", "100 km", "90,7 km"),
                     ("Énergie de 2ᵉ étape", "100 TeV", "85 TeV"),
                     ("Début de l’exploitation", "fin 2050", "début 2070")],
               f1="Coût en hausse. Spécifications en baisse. Calendrier repoussé d’environ quinze ans.",
               f2="Les chiffres de coûts viennent des promoteurs ; le sous-comité n’a pas eu le droit de produire les siens."),
}


def fcc_drift(lang="en"):
    """Four parameters of the proposed next machine, 2019 design vs 2025."""
    d = FCC[lang]
    out = [f'<text class="f-sub" x="40" y="30">{d["head"]}</text>']
    for i, (label, a, b) in enumerate(d["rows"]):
        y = 70 + i * 46
        out.append(
            f'<text class="f-lbl" x="40" y="{y}">{label}</text>'
            f'<text class="f-num" x="330" y="{y}" text-anchor="end" '
            f'style="fill:var(--ink-faint,#777)">{a}</text>'
            f'<path d="M346 {y-5} L402 {y-5}" stroke="var(--tier-d,#c0564e)" stroke-width="1.5"/>'
            f'<path d="M396 {y-9} L402 {y-5} L396 {y-1}" fill="none" '
            f'stroke="var(--tier-d,#c0564e)" stroke-width="1.5"/>'
            f'<text class="f-num" x="416" y="{y}" style="fill:var(--tier-d,#c0564e)">{b}</text>'
            f'<line class="f-rule" x1="40" y1="{y+14}" x2="760" y2="{y+14}"/>')
    out.append(f'<text class="f-lbl" x="40" y="268">{d["f1"]}</text>')
    out.append(f'<text class="f-sub" x="40" y="288">{d["f2"]}</text>')
    return _wrap("800 300", "".join(out))


# --------------------------------------------------------------- figure 4

NAT = {
    "en": dict(t1="Tolerated fine-tuning parameter Δ (log scale) — moved by stipulation",
               t2="Gluino mass exclusion limit, GeV — what the criterion was meant to predict",
               note="2008: sub-TeV bound published with a stated failure condition"),
    "fr": dict(t1="Paramètre d’ajustement fin toléré Δ (échelle log) — relevé par stipulation",
               t2="Limite d’exclusion de masse du gluino, GeV — ce que le critère devait prédire",
               note="2008 : borne sous le TeV publiée avec une condition d’échec énoncée"),
}


def naturalness_goalposts(lang="en"):
    """Tolerated fine-tuning vs the exclusion limits it was meant to predict."""
    import math
    d = NAT[lang]
    thresh = [(1988, 10), (1998, 20), (2013, 100), (2013.5, 1000)]
    limits = [(2008, 310), (2012, 1000), (2019, 2300)]
    x0, x1, yT, hT, yL, hL = 70, 760, 56, 78, 190, 70
    def px(yr): return x0 + (yr - 1986) / (2021 - 1986) * (x1 - x0)
    def pyT(v): return yT + hT - (math.log10(v) - 1) / 2 * hT
    def pyL(v): return yL + hL - (v / 2500) * hL
    out = [f'<text class="f-sub" x="70" y="28">{d["t1"]}</text>']
    pts, prev = [], None
    for yr, v in thresh:
        X, Y = px(yr), pyT(v)
        pts.append(f'L{X:.0f} {prev:.0f} L{X:.0f} {Y:.0f}' if prev else f'M{X:.0f} {Y:.0f}')
        prev = Y
        out.append(f'<circle cx="{X:.0f}" cy="{Y:.0f}" r="3.5" class="f-bar-b"/>'
                   f'<text class="f-num" x="{X+8:.0f}" y="{Y+4:.0f}" style="font-size:12px">{_n(v, lang)}</text>')
    pts.append(f'L{px(2020):.0f} {prev:.0f}')
    out.insert(1, f'<path d="{"".join(pts)}" fill="none" stroke="var(--tier-b,#d99a2b)" stroke-width="2"/>')
    out.append(f'<line class="f-axis" x1="{x0}" y1="{yT+hT}" x2="{x1}" y2="{yT+hT}"/>')
    out.append(f'<text class="f-sub" x="70" y="178">{d["t2"]}</text>')
    lp = " ".join(f'{px(y):.0f},{pyL(v):.0f}' for y, v in limits)
    out.append(f'<polyline points="{lp}" fill="none" stroke="var(--tier-d,#c0564e)" stroke-width="2"/>')
    for yr, v in limits:
        out.append(f'<circle cx="{px(yr):.0f}" cy="{pyL(v):.0f}" r="3.5" class="f-bar-d"/>'
                   f'<text class="f-num" x="{px(yr)+8:.0f}" y="{pyL(v)+4:.0f}" style="font-size:12px">{_n(v, lang)}</text>')
    out.append(f'<line class="f-axis" x1="{x0}" y1="{yL+hL}" x2="{x1}" y2="{yL+hL}"/>')
    for yr in (1990, 2000, 2010, 2020):
        out.append(f'<text class="f-sub" x="{px(yr):.0f}" y="{yL+hL+18}" text-anchor="middle">{yr}</text>')
    out.append(f'<line x1="{px(2008):.0f}" y1="{yT}" x2="{px(2008):.0f}" y2="{yL+hL}" '
               f'class="f-rule" stroke-dasharray="3 4"/>'
               f'<text class="f-sub" x="{px(2008)+6:.0f}" y="{yT-6}">{d["note"]}</text>')
    return _wrap("800 290", "".join(out))


# --------------------------------------------------------------- figure 5

SUP = {
    "en": dict(head="Qualified suppliers, by component",
               r1="Nb₃Sn superconductor at ITER specification", v1="8 suppliers",
               r2="Nb₃Sn at HL-LHC specification", v2="1 supplier",
               r3="Helium turbo-expanders of required size", v3="2 companies",
               r4="World niobium mine production", v4="93% Brazil",
               n1="One firm holds 77–90% of that. The United States produces none.",
               n2="FCC demand: 8,000–10,000 t. World output: 5–10 t/yr."),
    "fr": dict(head="Fournisseurs qualifiés, par composant",
               r1="Supraconducteur Nb₃Sn aux spécifications d’ITER", v1="8 fournisseurs",
               r2="Nb₃Sn aux spécifications du HL-LHC", v2="1 fournisseur",
               r3="Turbo-détendeurs à hélium de la taille requise", v3="2 entreprises",
               r4="Production minière mondiale de niobium", v4="93 % Brésil",
               n1="Une seule firme en détient 77 à 90 %. Les États-Unis n’en produisent aucun.",
               n2="Demande du FCC : 8 000 à 10 000 t. Production mondiale : 5 à 10 t/an."),
}


def supply_concentration(lang="en"):
    """Single points of failure in the accelerator supply chain."""
    d = SUP[lang]
    def dots(n, filled, cls, x, y, r=6, gap=19):
        return "".join(f'<circle cx="{x + i*gap}" cy="{y}" r="{r}" '
                       f'class="{cls if i < filled else "f-mute"}"/>' for i in range(n))
    out = [f'<text class="f-sub" x="40" y="28">{d["head"]}</text>',
           f'<text class="f-lbl" x="40" y="70">{d["r1"]}</text>', dots(8, 8, "f-bar-a", 440, 65),
           f'<text class="f-num" x="620" y="70">{d["v1"]}</text>',
           f'<text class="f-lbl" x="40" y="112">{d["r2"]}</text>', dots(8, 1, "f-bar-d", 440, 107),
           f'<text class="f-num" x="620" y="112" style="fill:var(--tier-d,#c0564e)">{d["v2"]}</text>',
           f'<text class="f-lbl" x="40" y="154">{d["r3"]}</text>', dots(8, 2, "f-bar-d", 440, 149),
           f'<text class="f-num" x="620" y="154" style="fill:var(--tier-d,#c0564e)">{d["v3"]}</text>',
           '<line class="f-rule" x1="40" y1="178" x2="760" y2="178"/>',
           f'<text class="f-lbl" x="40" y="212">{d["r4"]}</text>',
           '<rect class="f-mute" x="40" y="228" width="400" height="22" rx="2"/>',
           '<rect class="f-bar-d" x="40" y="228" width="372" height="22" rx="2"/>',
           f'<text class="f-num" x="454" y="245">{d["v4"]}</text>',
           f'<text class="f-sub" x="40" y="272">{d["n1"]}</text>',
           f'<text class="f-sub" x="440" y="272">{d["n2"]}</text>']
    return _wrap("800 290", "".join(out))


# --------------------------------------------------------------- captions

CAPTIONS = {
    "trigger-cascade": {
        "en": "<b>What the LHC keeps.</b> Rates are log-scaled; rejection factors are stated between stages. Discarded crossings are dropped in hardware within microseconds and cannot be recovered. Source: ATLAS and CMS trigger performance papers, Run 2–3.",
        "fr": "<b>Ce que le LHC conserve.</b> Échelle logarithmique ; les facteurs de rejet figurent entre les étapes. Les croisements écartés sont abandonnés en matériel en quelques microsecondes et sont irrécupérables. Source : articles de performance des déclencheurs d’ATLAS et de CMS, Run 2–3."},
    "dissent-ratio": {
        "en": "<b>Who has challenged particle accelerators, and on what grounds.</b> The distribution is the result: challenges to the validity of the physics are a rounding error against challenges to priorities, cost, safety and epistemics. Source: dissent register, 58 references.",
        "fr": "<b>Qui a contesté les accélérateurs de particules, et sur quels motifs.</b> La distribution est le résultat : les contestations de la validité de la physique sont négligeables face à celles visant les priorités, les coûts, la sûreté et l’épistémologie. Source : registre de dissidence, 58 références."},
    "fcc-drift": {
        "en": "<b>The proposed next machine, 2019 design against 2025 feasibility study.</b> All four parameters moved adversely over six years. Source: FCC conceptual design report and 2025 feasibility study.",
        "fr": "<b>La prochaine machine proposée : conception de 2019 contre étude de faisabilité de 2025.</b> Les quatre paramètres ont évolué défavorablement en six ans. Source : rapport de conception du FCC et étude de faisabilité de 2025."},
    "naturalness-goalposts": {
        "en": "<b>The criterion and the evidence, 1988–2019.</b> The tolerated fine-tuning parameter was raised by stipulation at each step, while the exclusion limits it was meant to predict rose by nearly an order of magnitude. Source: theory critique, 44 references.",
        "fr": "<b>Le critère et les données, 1988–2019.</b> Le paramètre d’ajustement fin toléré a été relevé par stipulation à chaque étape, tandis que les limites d’exclusion qu’il devait prédire montaient de près d’un ordre de grandeur. Source : critique théorique, 44 références."},
    "supply-concentration": {
        "en": "<b>Single points of failure.</b> Filled circles are qualified suppliers. The HL-LHC niobium-tin specification was met by one firm where ITER's was met by eight. Source: hardware supply chain, 56 references.",
        "fr": "<b>Points de défaillance uniques.</b> Les cercles pleins sont des fournisseurs qualifiés. Une seule firme a satisfait au cahier des charges niobium-étain du HL-LHC, là où huit ont satisfait à celui d’ITER. Source : chaîne d’approvisionnement matérielle, 56 références."},
}

FIGURES = {
    "trigger-cascade": trigger_cascade,
    "dissent-ratio": dissent_ratio,
    "fcc-drift": fcc_drift,
    "naturalness-goalposts": naturalness_goalposts,
    "supply-concentration": supply_concentration,
}


def render(name, lang="en"):
    return (f'<figure class="fig" id="fig-{name}">{FIGURES[name](lang)}'
            f'<figcaption>{CAPTIONS[name][lang]}</figcaption></figure>')
