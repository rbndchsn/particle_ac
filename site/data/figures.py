"""Hand-built SVG figures for the research findings.

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


def trigger_cascade():
    """What the LHC keeps, stage by stage. Log-scaled bars with stated ratios."""
    import math
    stages = [
        ("Bunch crossings", 40_000_000, "40 MHz", "f-bar"),
        ("After Level-1 (hardware, &lt;2.5 µs)", 100_000, "100 kHz", "f-bar-b"),
        ("After high-level trigger", 3_000, "3 kHz", "f-bar-d"),
    ]
    x0, w, top, bh, gap = 240, 470, 42, 34, 46
    lo, hi = math.log10(1_000), math.log10(40_000_000)
    rows = []
    for i, (label, val, disp, cls) in enumerate(stages):
        y = top + i * gap
        bw = max(4, (math.log10(val) - lo) / (hi - lo) * w)
        rows.append(
            f'<text class="f-lbl" x="{x0-14}" y="{y+bh*0.62}" text-anchor="end">{label}</text>'
            f'<rect class="{cls}" x="{x0}" y="{y}" width="{bw:.1f}" height="{bh}" rx="2"/>'
            f'<text class="f-num" x="{x0+bw+12}" y="{y+bh*0.68}">{disp}</text>'
        )
        if i:
            rows.append(
                f'<text class="f-sub" x="{x0+4}" y="{y-7}">↓ rejected '
                f'{stages[i-1][1]//val:,}× — not recoverable</text>')
    rows.append(f'<line class="f-axis" x1="{x0}" y1="{top-22}" x2="{x0}" y2="{top+3*gap-4}"/>')
    rows.append(
        '<g transform="translate(240,196)">'
        '<text class="f-sub" x="0" y="0">Data rate if everything were read out</text>'
        '<text class="f-num" x="0" y="22">40 TB/s</text>'
        '<text class="f-sub" x="190" y="0">Data rate actually written</text>'
        '<text class="f-num" x="190" y="22">~1 GB/s</text>'
        '<text class="f-big" x="360" y="20">13,000×</text>'
        '<text class="f-sub" x="360" y="38">total rejection factor</text>'
        '</g>')
    return _wrap("800 250", "".join(rows))


def dissent_ratio():
    """60 confrontations by category; the validity segment is the finding."""
    cats = [
        ("Priority &amp; cost", 21, "f-bar"),
        ("Epistemic &amp; sociological", 15, "f-bar-c"),
        ("Safety", 12, "f-bar-b"),
        ("Specific result", 9, "f-bar-a"),
        ("Validity of the physics", 3, "f-bar-d"),
    ]
    total = sum(c[1] for c in cats)
    x0, w, y, h = 40, 720, 60, 46
    x, segs = x0, []
    for label, n, cls in cats:
        sw = n / total * w
        segs.append(f'<rect class="{cls}" x="{x:.1f}" y="{y}" width="{sw-2:.1f}" height="{h}" rx="2"/>')
        if n > 5:
            segs.append(f'<text class="f-num" x="{x+sw/2:.1f}" y="{y+h*0.64}" text-anchor="middle">{n}</text>')
        x += sw
    keys, kx = [], x0
    for label, n, cls in cats:
        keys.append(
            f'<g transform="translate({kx},{y+h+34})">'
            f'<rect class="{cls}" x="0" y="-9" width="10" height="10" rx="2"/>'
            f'<text class="f-sub" x="16" y="0">{label} · {n}</text></g>')
        kx += 152
    ann = (
        f'<text class="f-sub" x="{x0}" y="36">60 documented confrontations, 1961–2026 '
        f'— stated as a floor, not a census</text>'
        f'<g transform="translate({x0+w-96},{y+h+72})">'
        f'<text class="f-big" x="96" y="0" text-anchor="end">3 of 60</text>'
        f'<text class="f-sub" x="96" y="18" text-anchor="end">dispute the physics itself</text>'
        f'<text class="f-sub" x="96" y="34" text-anchor="end">none of the three is a</text>'
        f'<text class="f-sub" x="96" y="48" text-anchor="end">practising particle physicist</text></g>'
        f'<g transform="translate({x0},{y+h+72})">'
        f'<text class="f-lbl" x="0" y="0">All 36 scientists in the priority and epistemic categories —</text>'
        f'<text class="f-lbl" x="0" y="18">including five Nobel laureates — concede in writing that</text>'
        f'<text class="f-lbl" x="0" y="36">the machines work and the Standard Model is confirmed.</text></g>')
    line = (f'<line class="f-rule" x1="{x0+w-6:.1f}" y1="{y+h+4}" '
            f'x2="{x0+w-6:.1f}" y2="{y+h+60}" stroke-dasharray="2 3"/>')
    return _wrap("800 250", ann + "".join(segs) + line + "".join(keys))


def fcc_drift():
    """Four parameters of the proposed next machine, 2019 design vs 2025."""
    rows = [
        ("Projected cost", "~€9 bn", "CHF 15.3 bn", "worse"),
        ("Tunnel circumference", "100 km", "90.7 km", "worse"),
        ("Second-stage energy", "100 TeV", "85 TeV", "worse"),
        ("Operations begin", "late 2050s", "early 2070s", "worse"),
    ]
    out = ['<text class="f-sub" x="40" y="30">2019 conceptual design → 2025 feasibility study</text>']
    for i, (label, a, b, _) in enumerate(rows):
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
    out.append('<text class="f-lbl" x="40" y="268">Cost up. Specification down. Schedule out by roughly fifteen years.</text>')
    out.append('<text class="f-sub" x="40" y="288">Panel cost figures are taken from the proponents; the subcommittee was barred from producing its own.</text>')
    return _wrap("800 300", "".join(out))


def naturalness_goalposts():
    """Tolerated fine-tuning vs the exclusion limits it was meant to predict."""
    import math
    thresh = [(1988, 10), (1998, 20), (2013, 100), (2013.5, 1000)]
    limits = [(2008, 310), (2012, 1000), (2019, 2300)]
    x0, x1, yT, hT, yL, hL = 70, 760, 56, 78, 190, 70
    def px(yr): return x0 + (yr - 1986) / (2021 - 1986) * (x1 - x0)
    def pyT(v): return yT + hT - (math.log10(v) - 1) / 2 * hT
    def pyL(v): return yL + hL - (v / 2500) * hL
    out = ['<text class="f-sub" x="70" y="28">Tolerated fine-tuning parameter Δ (log scale) — moved by stipulation</text>']
    pts, prev = [], None
    for yr, v in thresh:
        X, Y = px(yr), pyT(v)
        if prev: pts.append(f'L{X:.0f} {prev:.0f} L{X:.0f} {Y:.0f}')
        else: pts.append(f'M{X:.0f} {Y:.0f}')
        prev = Y
        out.append(f'<circle cx="{X:.0f}" cy="{Y:.0f}" r="3.5" class="f-bar-b"/>'
                   f'<text class="f-num" x="{X+8:.0f}" y="{Y+4:.0f}" style="font-size:12px">{v}</text>')
    pts.append(f'L{px(2020):.0f} {prev:.0f}')
    out.insert(1, f'<path d="{"".join(pts)}" fill="none" stroke="var(--tier-b,#d99a2b)" stroke-width="2"/>')
    out.append(f'<line class="f-axis" x1="{x0}" y1="{yT+hT}" x2="{x1}" y2="{yT+hT}"/>')
    out.append('<text class="f-sub" x="70" y="178">Gluino mass exclusion limit, GeV — what the criterion was meant to predict</text>')
    lp = " ".join(f'{px(y):.0f},{pyL(v):.0f}' for y, v in limits)
    out.append(f'<polyline points="{lp}" fill="none" stroke="var(--tier-d,#c0564e)" stroke-width="2"/>')
    for yr, v in limits:
        out.append(f'<circle cx="{px(yr):.0f}" cy="{pyL(v):.0f}" r="3.5" class="f-bar-d"/>'
                   f'<text class="f-num" x="{px(yr)+8:.0f}" y="{pyL(v)+4:.0f}" style="font-size:12px">{v:,}</text>')
    out.append(f'<line class="f-axis" x1="{x0}" y1="{yL+hL}" x2="{x1}" y2="{yL+hL}"/>')
    for yr in (1990, 2000, 2010, 2020):
        out.append(f'<text class="f-sub" x="{px(yr):.0f}" y="{yL+hL+18}" text-anchor="middle">{yr}</text>')
    out.append(f'<line x1="{px(2008):.0f}" y1="{yT}" x2="{px(2008):.0f}" y2="{yL+hL}" '
               f'class="f-rule" stroke-dasharray="3 4"/>'
               f'<text class="f-sub" x="{px(2008)+6:.0f}" y="{yT-6}">2008: sub-TeV bound published '
               f'with a stated failure condition</text>')
    return _wrap("800 290", "".join(out))


def supply_concentration():
    """Single points of failure in the accelerator supply chain."""
    def dots(n, filled, cls, x, y, r=6, gap=19):
        out = []
        for i in range(n):
            c = cls if i < filled else "f-mute"
            out.append(f'<circle cx="{x + i*gap}" cy="{y}" r="{r}" class="{c}"/>')
        return "".join(out)
    out = ['<text class="f-sub" x="40" y="28">Qualified suppliers, by component</text>']
    out.append('<text class="f-lbl" x="40" y="70">Nb₃Sn superconductor at ITER specification</text>')
    out.append(dots(8, 8, "f-bar-a", 440, 65))
    out.append('<text class="f-num" x="620" y="70">8 suppliers</text>')
    out.append('<text class="f-lbl" x="40" y="112">Nb₃Sn at HL-LHC specification</text>')
    out.append(dots(8, 1, "f-bar-d", 440, 107))
    out.append('<text class="f-num" x="620" y="112" style="fill:var(--tier-d,#c0564e)">1 supplier</text>')
    out.append('<text class="f-lbl" x="40" y="154">Helium turbo-expanders of required size</text>')
    out.append(dots(8, 2, "f-bar-d", 440, 149))
    out.append('<text class="f-num" x="620" y="154" style="fill:var(--tier-d,#c0564e)">2 companies</text>')
    out.append('<line class="f-rule" x1="40" y1="178" x2="760" y2="178"/>')
    bx, bw = 40, 400
    out.append('<text class="f-lbl" x="40" y="212">World niobium mine production</text>')
    out.append(f'<rect class="f-mute" x="{bx}" y="228" width="{bw}" height="22" rx="2"/>')
    out.append(f'<rect class="f-bar-d" x="{bx}" y="228" width="{bw*0.93:.0f}" height="22" rx="2"/>')
    out.append(f'<text class="f-num" x="{bx+bw+14}" y="245">93% Brazil</text>')
    out.append('<text class="f-sub" x="40" y="272">One firm holds 77–90% of that. The United States produces none.</text>')
    out.append('<text class="f-sub" x="440" y="272">FCC demand: 8,000–10,000 t. World output: 5–10 t/yr.</text>')
    return _wrap("800 290", "".join(out))


FIGURES = {
    "trigger-cascade": (
        trigger_cascade,
        "<b>What the LHC keeps.</b> Rates are log-scaled; rejection factors are stated between "
        "stages. Discarded crossings are dropped in hardware within microseconds and cannot be "
        "recovered. Source: ATLAS and CMS trigger performance papers, Run 2–3."),
    "dissent-ratio": (
        dissent_ratio,
        "<b>Who has challenged particle accelerators, and on what grounds.</b> The distribution is "
        "the result: challenges to the validity of the physics are a rounding error against "
        "challenges to priorities, cost, safety and epistemics. Source: dissent register, 58 "
        "references."),
    "fcc-drift": (
        fcc_drift,
        "<b>The proposed next machine, 2019 design against 2025 feasibility study.</b> All four "
        "parameters moved adversely over six years. Source: FCC conceptual design report and 2025 "
        "feasibility study."),
    "naturalness-goalposts": (
        naturalness_goalposts,
        "<b>The criterion and the evidence, 1988–2019.</b> The tolerated fine-tuning parameter "
        "was raised by stipulation at each step, while the exclusion limits it was meant to predict "
        "rose by nearly an order of magnitude. Source: theory critique, 44 references."),
    "supply-concentration": (
        supply_concentration,
        "<b>Single points of failure.</b> Filled circles are qualified suppliers. The HL-LHC "
        "niobium-tin specification was met by one firm where ITER's was met by eight. Source: "
        "hardware supply chain, 56 references."),
}


def render(name):
    fn, caption = FIGURES[name]
    return (f'<figure class="fig" id="fig-{name}">{fn()}'
            f'<figcaption>{caption}</figcaption></figure>')
