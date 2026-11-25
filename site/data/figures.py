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


# ------------------------------------------------- hero illustration

def hero_illustration(lang="en"):
    """Cartoon: a working accelerator wired to a screen, and someone who
    cannot tell whether the screen is telling the truth. The question mark
    is the argument."""
    ink = "var(--ink, #ebe7e0)"
    acc = "var(--accent, #e0a33c)"
    dim = "var(--ink-faint, #6b6861)"
    scr = "var(--tier-c, #5b8dc9)"
    red = "var(--tier-d, #c0564e)"
    o = []

    # --- accelerator ring: beam pipe, bending magnets, circulating bunches
    cx, cy, r = 112, 132, 66
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{dim}" stroke-width="11"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="var(--bg-raised,#141416)" stroke-width="6"/>')
    import math
    for i in range(12):                       # bending magnets around the ring
        a = i * 30 - 90
        mx = cx + r * math.cos(math.radians(a))
        my = cy + r * math.sin(math.radians(a))
        o.append(f'<rect x="{mx-7:.1f}" y="{my-5:.1f}" width="14" height="10" rx="2" '
                 f'fill="{dim}" transform="rotate({a+90} {mx:.1f} {my:.1f})"/>')
    for i, a in enumerate((-60, -20, 25)):    # circulating bunches
        bx = cx + r * math.cos(math.radians(a))
        by = cy + r * math.sin(math.radians(a))
        o.append(f'<circle cx="{bx:.1f}" cy="{by:.1f}" r="3.5" fill="{acc}"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r-26}" fill="none" stroke="{acc}" '
             f'stroke-width="1.5" stroke-dasharray="3 7" opacity="0.5"/>')
    # injector line feeding the ring
    o.append(f'<path d="M30 {cy+52} L{cx-r+6} {cy+26}" stroke="{dim}" stroke-width="6" stroke-linecap="round"/>')
    o.append(f'<circle cx="34" cy="{cy+50}" r="5" fill="{acc}"/>')
    # detector: barrel straddling the ring at the right
    dxc, dyc = cx + r, cy
    o.append(f'<g transform="translate({dxc},{dyc})">'
             f'<rect x="-17" y="-26" width="34" height="52" rx="7" fill="var(--bg-inset,#1b1b1e)" '
             f'stroke="{ink}" stroke-width="2.5"/>'
             f'<line x1="-17" y1="-10" x2="17" y2="-10" stroke="{ink}" stroke-width="1.5"/>'
             f'<line x1="-17" y1="4" x2="17" y2="4" stroke="{ink}" stroke-width="1.5"/>'
             f'<line x1="-17" y1="17" x2="17" y2="17" stroke="{ink}" stroke-width="1.5"/>'
             f'<circle cx="0" cy="-19" r="3" fill="{acc}"/></g>')

    # --- cable from detector to the computer
    o.append(f'<path d="M{dxc+18} {dyc} C 215 132, 215 86, 252 86" fill="none" '
             f'stroke="{dim}" stroke-width="3.5" stroke-linecap="round"/>')

    # --- monitor showing "the result"
    o.append('<g transform="translate(252,42)">')
    o.append(f'<rect x="0" y="0" width="128" height="92" rx="7" fill="var(--bg-inset,#1b1b1e)" '
             f'stroke="{ink}" stroke-width="2.5"/>')
    o.append(f'<rect x="9" y="9" width="110" height="74" rx="3" fill="var(--bg-sunk,#070708)"/>')
    o.append(f'<path d="M18 74 L18 18" stroke="{dim}" stroke-width="1.5"/>')
    o.append(f'<path d="M18 74 L110 74" stroke="{dim}" stroke-width="1.5"/>')
    # a spectrum with a bump in it
    o.append(f'<path d="M20 70 L34 67 L46 64 L56 60 L62 40 L68 22 L74 40 L80 60 L92 56 L104 53" '
             f'fill="none" stroke="{scr}" stroke-width="2.5" stroke-linejoin="round"/>')
    o.append(f'<circle cx="68" cy="22" r="3.5" fill="{acc}"/>')
    o.append(f'<path d="M50 90 L78 90 L82 104 L46 104 Z" fill="{dim}"/>')
    o.append(f'<rect x="38" y="104" width="52" height="5" rx="2.5" fill="{ink}"/>')
    o.append('</g>')

    # --- stick figure, and the question
    o.append('<g transform="translate(416,96)" stroke-linecap="round">')
    o.append(f'<circle cx="0" cy="0" r="11" fill="none" stroke="{ink}" stroke-width="2.5"/>')
    o.append(f'<circle cx="-4" cy="-2" r="1.6" fill="{ink}"/><circle cx="4" cy="-2" r="1.6" fill="{ink}"/>')
    o.append(f'<path d="M-4 5 Q0 2 4 5" fill="none" stroke="{ink}" stroke-width="1.8"/>')
    o.append(f'<path d="M0 11 L0 46" stroke="{ink}" stroke-width="2.5"/>')
    o.append(f'<path d="M0 20 L-16 32" stroke="{ink}" stroke-width="2.5"/>')   # arm toward screen
    o.append(f'<path d="M0 20 L14 14" stroke="{ink}" stroke-width="2.5"/>')    # hand on chin
    o.append(f'<path d="M0 46 L-11 66 M0 46 L11 66" stroke="{ink}" stroke-width="2.5"/>')
    o.append('</g>')
    o.append(f'<text x="416" y="-16" text-anchor="middle" '
             f'style="font:700 46px var(--sans,sans-serif);fill:{red}" '
             f'transform="translate(0,56)">?</text>')
    o.append(f'<circle cx="398" cy="60" r="2.5" fill="{red}" opacity="0.75"/>')
    o.append(f'<circle cx="392" cy="70" r="1.8" fill="{red}" opacity="0.5"/>')

    return (f'<svg viewBox="0 0 470 240" xmlns="http://www.w3.org/2000/svg" '
            f'class="hero-art" role="img" aria-label="'
            f'{"A particle accelerator wired to a screen, and a figure wondering whether the screen is right" if lang == "en" else "Un accelerateur de particules relie a un ecran, et une silhouette se demandant si lecran dit vrai"}'
            f'">{"".join(o)}</svg>')


# ------------------------------------------------- section vignettes
# One recurring stick figure, reacting to each finding. Same proportions
# throughout so it reads as a single character moving through the argument.

_INK = "var(--ink, #ebe7e0)"
_ACC = "var(--accent, #e0a33c)"
_DIM = "var(--ink-faint, #6b6861)"
_RED = "var(--tier-d, #c0564e)"
_GRN = "var(--tier-a, #4e9e73)"
_BLU = "var(--tier-c, #5b8dc9)"


def _person(x, y, scale=1.0, mood="think", arms="side"):
    """The recurring figure. mood: think | look | shrug | stop."""
    a = {"side": "M0 18 L-13 30 M0 18 L13 30",
         "point": "M0 18 L-18 24 M0 18 L11 12",
         "up": "M0 18 L-14 4 M0 18 L14 4",
         "chin": "M0 18 L-14 28 M0 18 L10 7"}[arms]
    face = {"think": '<path d="M-4 5 Q0 2 4 5" fill="none" stroke="%s" stroke-width="1.6"/>' % _INK,
            "look": '<path d="M-4 4 Q0 7 4 4" fill="none" stroke="%s" stroke-width="1.6"/>' % _INK,
            "shrug": '<path d="M-4 5 L4 5" stroke="%s" stroke-width="1.6"/>' % _INK,
            "stop": '<path d="M-4 6 Q0 2 4 6" fill="none" stroke="%s" stroke-width="1.6"/>' % _INK}[mood]
    return (f'<g transform="translate({x},{y}) scale({scale})" stroke-linecap="round">'
            f'<circle cx="0" cy="0" r="10" fill="none" stroke="{_INK}" stroke-width="2.2"/>'
            f'<circle cx="-4" cy="-2" r="1.5" fill="{_INK}"/>'
            f'<circle cx="4" cy="-2" r="1.5" fill="{_INK}"/>{face}'
            f'<path d="M0 10 L0 42" stroke="{_INK}" stroke-width="2.2"/>'
            f'<path d="{a}" stroke="{_INK}" stroke-width="2.2"/>'
            f'<path d="M0 42 L-10 60 M0 42 L10 60" stroke="{_INK}" stroke-width="2.2"/></g>')


def _vignette(body, label, w=260, h=150):
    return (f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
            f'class="vignette" role="img" aria-label="{label}">{body}</svg>')


def art_six_questions(lang="en"):
    """A checklist where none of the boxes has been ticked."""
    o = [f'<rect x="14" y="16" width="104" height="122" rx="6" fill="var(--bg-inset,#1b1b1e)" '
         f'stroke="{_INK}" stroke-width="2.2"/>',
         f'<rect x="46" y="8" width="40" height="13" rx="4" fill="{_DIM}"/>']
    for i in range(6):
        y = 36 + i * 17
        o.append(f'<rect x="26" y="{y}" width="11" height="11" rx="2.5" fill="none" '
                 f'stroke="{_RED}" stroke-width="1.8"/>')
        o.append(f'<line x1="45" y1="{y+6}" x2="{104 - (i % 3) * 12}" y2="{y+6}" '
                 f'stroke="{_DIM}" stroke-width="2.5" stroke-linecap="round"/>')
    o.append(_person(186, 56, 1.0, "think", "chin"))
    o.append(f'<text x="186" y="18" text-anchor="middle" '
             f'style="font:700 30px var(--sans,sans-serif);fill:{_ACC}">?</text>')
    lbl = ("Six unticked checkboxes and a puzzled figure" if lang == "en"
           else "Six cases non cochees et une silhouette perplexe")
    return _vignette("".join(o), lbl)


def art_criterion(lang="en"):
    """The prediction on the left; the word being erased on the right."""
    o = [f'<g transform="translate(10,22)">'
         f'<rect x="0" y="0" width="76" height="98" rx="5" fill="var(--bg-inset,#1b1b1e)" '
         f'stroke="{_DIM}" stroke-width="2"/>'
         f'<text x="38" y="30" text-anchor="middle" '
         f'style="font:700 15px var(--sans,sans-serif);fill:{_ACC}">1 TeV</text>'
         f'<line x1="12" y1="46" x2="64" y2="46" stroke="{_DIM}" stroke-width="2.5"/>'
         f'<line x1="12" y1="58" x2="56" y2="58" stroke="{_DIM}" stroke-width="2.5"/>'
         f'<line x1="12" y1="70" x2="64" y2="70" stroke="{_DIM}" stroke-width="2.5"/>'
         f'<text x="38" y="90" text-anchor="middle" '
         f'style="font:600 9px var(--sans,sans-serif);fill:{_GRN}">2008</text></g>',
         f'<g transform="translate(104,22)">'
         f'<rect x="0" y="0" width="76" height="98" rx="5" fill="var(--bg-inset,#1b1b1e)" '
         f'stroke="{_DIM}" stroke-width="2"/>'
         f'<line x1="12" y1="26" x2="64" y2="26" stroke="{_DIM}" stroke-width="2.5"/>'
         f'<line x1="12" y1="38" x2="44" y2="38" stroke="{_DIM}" stroke-width="2.5"/>'
         f'<line x1="12" y1="58" x2="64" y2="58" stroke="{_DIM}" stroke-width="2.5"/>'
         f'<rect x="12" y="42" width="34" height="11" rx="2" fill="{_RED}" opacity="0.28"/>'
         f'<text x="38" y="90" text-anchor="middle" '
         f'style="font:600 9px var(--sans,sans-serif);fill:{_RED}">2023</text></g>',
         # the eraser, mid-stroke
         f'<g transform="translate(118,56) rotate(-18)">'
         f'<rect x="0" y="0" width="26" height="13" rx="3" fill="{_RED}"/>'
         f'<rect x="20" y="0" width="12" height="13" rx="2" fill="{_DIM}"/></g>',
         _person(216, 46, 0.85, "look", "point")]
    lbl = ("A prediction from 2008 beside a 2023 document with the word erased"
           if lang == "en" else
           "Une prediction de 2008 a cote d un document de 2023 dont le mot a ete efface")
    return _vignette("".join(o), lbl)


def art_instrument(lang="en"):
    """Almost everything into the bin; one survivor out the bottom."""
    import random
    o = [f'<path d="M20 18 L140 18 L96 72 L96 112 L64 112 L64 72 Z" fill="var(--bg-inset,#1b1b1e)" '
         f'stroke="{_INK}" stroke-width="2.2" stroke-linejoin="round"/>']
    rnd = random.Random(7)
    for i in range(16):                        # incoming flood
        x = 26 + rnd.random() * 108
        y = -2 + rnd.random() * 16
        o.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="2.6" fill="{_ACC}" opacity="0.85"/>')
    for i in range(11):                        # spilling out, discarded
        side = -1 if i % 2 else 1
        x = 80 + side * (26 + rnd.random() * 34)
        y = 58 + rnd.random() * 48
        o.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="2.4" fill="{_RED}" opacity="0.7"/>')
    o.append(f'<circle cx="80" cy="124" r="3.4" fill="{_ACC}"/>')
    o.append(f'<path d="M62 132 L98 132 L94 146 L66 146 Z" fill="none" stroke="{_DIM}" stroke-width="2"/>')
    o.append(_person(212, 50, 0.9, "look", "point"))
    lbl = ("A funnel discarding almost everything, one particle surviving"
           if lang == "en" else
           "Un entonnoir qui ecarte presque tout, une seule particule survit")
    return _vignette("".join(o), lbl)


def art_literature(lang="en"):
    """A locked cabinet; two sheets in the out-slot."""
    o = [f'<rect x="18" y="20" width="104" height="112" rx="6" fill="var(--bg-inset,#1b1b1e)" '
         f'stroke="{_INK}" stroke-width="2.2"/>']
    for i in range(3):
        y = 32 + i * 34
        o.append(f'<rect x="28" y="{y}" width="84" height="26" rx="3" fill="none" '
                 f'stroke="{_DIM}" stroke-width="1.8"/>')
        o.append(f'<line x1="60" y1="{y+13}" x2="80" y2="{y+13}" stroke="{_DIM}" stroke-width="3"/>')
    o.append(f'<g transform="translate(70,76)">'
             f'<rect x="-11" y="-2" width="22" height="18" rx="3" fill="{_RED}"/>'
             f'<path d="M-6 -2 L-6 -9 A6 6 0 0 1 6 -9 L6 -2" fill="none" stroke="{_RED}" stroke-width="2.6"/></g>')
    o.append(f'<rect x="126" y="60" width="22" height="28" rx="2" fill="var(--bg-sunk,#070708)" '
             f'stroke="{_DIM}" stroke-width="1.6" transform="rotate(8 137 74)"/>')
    o.append(f'<rect x="132" y="56" width="22" height="28" rx="2" fill="var(--bg-sunk,#070708)" '
             f'stroke="{_DIM}" stroke-width="1.6" transform="rotate(-6 143 70)"/>')
    o.append(f'<text x="140" y="104" text-anchor="middle" '
             f'style="font:700 13px var(--sans,sans-serif);fill:{_ACC}">2</text>')
    o.append(_person(212, 50, 0.9, "shrug", "up"))
    lbl = ("A padlocked cabinet with two sheets released" if lang == "en"
           else "Un classeur cadenasse dont deux feuilles seulement sortent")
    return _vignette("".join(o), lbl)


def art_money(lang="en"):
    """Scales: the money on one side, 1.7% of science on the other."""
    o = [f'<path d="M130 24 L130 112" stroke="{_INK}" stroke-width="2.4"/>',
         f'<path d="M104 128 L156 128" stroke="{_INK}" stroke-width="2.4"/>',
         f'<path d="M130 112 L112 128 M130 112 L148 128" stroke="{_INK}" stroke-width="2.2"/>',
         f'<path d="M58 34 L202 50" stroke="{_INK}" stroke-width="2.4"/>',
         f'<path d="M58 34 L58 54 M202 50 L202 70" stroke="{_DIM}" stroke-width="1.6"/>',
         # heavy side
         f'<path d="M36 54 L80 54 L72 90 L44 90 Z" fill="{_DIM}"/>',
         f'<text x="58" y="78" text-anchor="middle" '
         f'style="font:700 17px var(--sans,sans-serif);fill:{_ACC}">€</text>',
         # light side
         f'<path d="M194 70 L210 70 L214 86 L190 86 Z" fill="none" stroke="{_BLU}" stroke-width="2"/>',
         f'<text x="202" y="104" text-anchor="middle" '
         f'style="font:700 12px var(--sans,sans-serif);fill:{_BLU}">1,7 %</text>'
         if lang == "fr" else
         f'<text x="202" y="104" text-anchor="middle" '
         f'style="font:700 12px var(--sans,sans-serif);fill:{_BLU}">1.7%</text>',
         _person(30, 96, 0.72, "shrug", "up")]
    lbl = ("Scales tipped by money against a tiny flask of science" if lang == "en"
           else "Une balance que l argent fait pencher face a une fiole de science")
    return _vignette("".join(o), lbl)


def art_dissent(lang="en"):
    """A crowd arguing about cost; three arguing about the physics."""
    o = []
    for i in range(9):
        x = 22 + (i % 5) * 34
        y = 56 + (i // 5) * 54
        o.append(_person(x, y, 0.42, "shrug", "side"))
        o.append(f'<rect x="{x-13}" y="{y-26}" width="26" height="12" rx="3" '
                 f'fill="{_ACC}" opacity="0.8"/>')
    for i in range(3):
        x = 196 + i * 26
        o.append(_person(x, 56, 0.42, "look", "side"))
        o.append(f'<rect x="{x-11}" y="30" width="22" height="12" rx="3" fill="{_RED}"/>')
    o.append(f'<line x1="180" y1="22" x2="180" y2="124" stroke="{_DIM}" '
             f'stroke-width="1.4" stroke-dasharray="3 4"/>')
    o.append(f'<text x="222" y="118" text-anchor="middle" '
             f'style="font:700 15px var(--sans,sans-serif);fill:{_RED}">3</text>')
    o.append(f'<text x="92" y="140" text-anchor="middle" '
             f'style="font:700 15px var(--sans,sans-serif);fill:{_ACC}">57</text>')
    lbl = ("A crowd of 57 with one kind of placard and three with another"
           if lang == "en" else
           "Une foule de 57 avec une pancarte et trois avec une autre")
    return _vignette("".join(o), lbl)


def art_notclaim(lang="en"):
    """The figure striking out its own placard."""
    o = [f'<rect x="56" y="30" width="116" height="60" rx="6" fill="var(--bg-inset,#1b1b1e)" '
         f'stroke="{_INK}" stroke-width="2.2"/>',
         f'<line x1="70" y1="48" x2="158" y2="48" stroke="{_DIM}" stroke-width="3"/>',
         f'<line x1="70" y1="62" x2="140" y2="62" stroke="{_DIM}" stroke-width="3"/>',
         f'<line x1="70" y1="76" x2="152" y2="76" stroke="{_DIM}" stroke-width="3"/>',
         f'<path d="M62 86 L166 36" stroke="{_RED}" stroke-width="4" stroke-linecap="round"/>',
         f'<path d="M114 90 L114 104" stroke="{_INK}" stroke-width="2.4"/>',
         _person(212, 52, 0.88, "stop", "point")]
    lbl = ("A figure striking through its own sign" if lang == "en"
           else "Une silhouette qui raye sa propre pancarte")
    return _vignette("".join(o), lbl)


ART = {
    "six-questions": art_six_questions, "criterion": art_criterion,
    "instrument": art_instrument, "literature": art_literature,
    "money": art_money, "dissent": art_dissent, "notclaim": art_notclaim,
}


def render_art(name, lang="en"):
    return f'<div class="sectionart">{ART[name](lang)}</div>'
