#!/usr/bin/env python3
"""
Static site generator for the particle acceleration research archive.

Reads the research markdown, renders it to docs/, and adds the furniture a
long technical document needs: a sticky table of contents, heading anchors,
citation links that resolve to the reference list, a per-document evidence-tier
composition bar, a summary panel, and an interactive claims register.

Inline [A] / [B] / [C] / [D] markers become styled badges so the epistemic
status of a claim is inseparable from the claim.

Usage:  python3 site/build.py
"""

import html
import re
import shutil
import sys
from pathlib import Path

import markdown
import yaml

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
OUT = ROOT / "docs"
sys.path.insert(0, str(SITE / "data"))
import figures  # noqa: E402

SECTIONS = [
    ("00_method", "Method"),
    ("01_foundations", "Foundations"),
    ("02_theory_critique", "Theory"),
    ("03_hardware_systems", "Hardware"),
    ("04_software_algorithmic", "Software"),
    ("05_publication_governance", "Publication"),
    ("06_dissent_register", "Dissent"),
    ("07_epistemic_audit", "Known vs assumed"),
    ("08_evidential_audit", "Where proofs fail"),
    ("09_anchoring_gradient", "Anchoring"),
    ("10_financial_investigation", "Money"),
]
UI = {
    "en": dict(overview="Overview", toc="Contents", onpage="On this page",
               docs="Documents", thedocs="The documents", inprog="In progress",
               refs="references", claims="tier-labelled claims", archive="Research archive",
               tierhead="Evidence tiers used in this document", tiercount="labelled claims",
               clickdocs="Please click on the boxes to access the content.",
               found="What this stream found", struck="Examined and struck out",
               foot1="Every claim in this archive carries an evidence tier. Claims examined and "
                     "rejected are kept on the record rather than removed \u2014 including both "
                     "hypotheses the project began with.",
               foot2="Source, data and full revision history:"),
    "fr": dict(overview="Vue d\u2019ensemble", toc="Sommaire", onpage="Sur cette page",
               docs="Documents", thedocs="Les documents", inprog="En cours",
               refs="r\u00e9f\u00e9rences", claims="affirmations cot\u00e9es par niveau de preuve",
               archive="Archive de recherche",
               tierhead="Niveaux de preuve employ\u00e9s dans ce document", tiercount="affirmations cot\u00e9es",
               clickdocs="Veuillez cliquer sur les encadr\u00e9s pour acc\u00e9der au contenu.",
               found="Ce que ce volet a trouv\u00e9", struck="Examin\u00e9 et \u00e9cart\u00e9",
               foot1="Chaque affirmation de cette archive porte un niveau de preuve. Celles qui ont "
                     "\u00e9t\u00e9 examin\u00e9es puis rejet\u00e9es sont conserv\u00e9es au dossier plut\u00f4t "
                     "qu\u2019effac\u00e9es \u2014 y compris les deux hypoth\u00e8ses de d\u00e9part du projet.",
               foot2="Sources, donn\u00e9es et historique complet des r\u00e9visions :"),
}

SECTION_FR = {
    "00_method": "M\u00e9thode", "01_foundations": "Fondements", "02_theory_critique": "Th\u00e9orie",
    "03_hardware_systems": "Mat\u00e9riel", "04_software_algorithmic": "Logiciel",
    "05_publication_governance": "Publication", "06_dissent_register": "Dissidence",
    "07_epistemic_audit": "Connu vs suppos\u00e9", "08_evidential_audit": "O\u00f9 les preuves c\u00e8dent",
    "09_anchoring_gradient": "Ancrage", "10_financial_investigation": "Argent",
}

NAV_PRIMARY = {"00_method": "research_frame", "03_hardware_systems": "trigger_data_destruction"}
TIER_NAMES = {"A": "Documented", "B": "Contested", "C": "Inference", "D": "Rejected"}
TIER_FR = {"A": "Document\u00e9", "B": "Contest\u00e9", "C": "Inf\u00e9rence", "D": "Rejet\u00e9"}
# Longest token first, so "SUPPORTED-AS-INFERENCE" is not eaten by "SUPPORTED".
STATUS_CLASS = [
    ("SUPPORTED-AS-INFERENCE", "st-inference"), ("REJECTED", "st-rejected"),
    ("SUPPORTED", "st-supported"), ("UNTESTED", "st-untested"), ("WEAKENED", "st-weakened"),
    ("\u00c9TAY\u00c9E COMME INF\u00c9RENCE", "st-inference"), ("REJET\u00c9E", "st-rejected"),
    ("\u00c9TAY\u00c9E", "st-supported"), ("NON \u00c9PROUV\u00c9E", "st-untested"),
    ("AFFAIBLIE", "st-weakened"),
]

FILTERS = {
    "en": [("all", "All claims"), ("SUPPORTED", "Supported"),
           ("SUPPORTED-AS-INFERENCE", "Inference"), ("REJECTED", "Rejected"),
           ("UNTESTED", "Untested")],
    "fr": [("all", "Toutes"), ("\u00c9TAY\u00c9E", "\u00c9tay\u00e9es"),
           ("\u00c9TAY\u00c9E COMME INF\u00c9RENCE", "Inf\u00e9rences"),
           ("REJET\u00c9E", "Rejet\u00e9es"), ("NON \u00c9PROUV\u00c9E", "Non \u00e9prouv\u00e9es")],
}


# ----------------------------------------------------------------- utilities

def split_frontmatter(text):
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    try:
        meta = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        meta = {}
    return meta, parts[2].lstrip("\n")


def outside_code(text, fn):
    """Apply fn only to the parts of the markdown outside fenced code."""
    chunks = text.split("```")
    for i in range(0, len(chunks), 2):
        chunks[i] = fn(chunks[i])
    return "```".join(chunks)


def normalise_headings(md_text):
    """Shift ATX headings so the shallowest level in the document becomes h2.

    The archive's convention puts the title in YAML frontmatter and starts the
    body at the first section, but files vary between starting at '#' and '##'.
    Normalising here keeps one h1 per page and a consistent TOC.
    """
    levels = [len(m.group(1)) for m in re.finditer(r"^(#{1,6})\s", md_text, re.M)]
    if not levels:
        return md_text
    shift = 2 - min(levels)
    if shift == 0:
        return md_text

    def bump(m):
        n = min(6, max(1, len(m.group(1)) + shift))
        return "#" * n + " "
    return outside_code(md_text, lambda t: re.sub(r"^(#{1,6})\s", bump, t, flags=re.M))


def strikethrough(md_text):
    return outside_code(md_text, lambda t: re.sub(r"~~(.+?)~~", r"<del>\1</del>", t))


def badge_tiers(md_text):
    def repl(m):
        t = m.group(1)
        return (f'<span class="tier tier-{t.lower()}" '
                f'title="Tier {t} — {TIER_NAMES[t]}">{t}</span>')
    return outside_code(md_text, lambda s: re.sub(r"\[([ABCD])\](?!\()", repl, s))


def count_tiers(md_text):
    counts = {k: 0 for k in TIER_NAMES}
    for t in re.findall(r"\[([ABCD])\](?!\()", md_text):
        counts[t] += 1
    return counts


def embed_figures(md_text, lang="en"):
    md_text = re.sub(r"\{\{art:([a-z0-9-]+)\}\}",
                     lambda m: figures.render_art(m.group(1), lang), md_text)
    return re.sub(r"\{\{fig:([a-z0-9-]+)\}\}",
                  lambda m: figures.render(m.group(1), lang), md_text)


def render_md(md_text, lang="en"):
    return markdown.markdown(
        strikethrough(badge_tiers(embed_figures(normalise_headings(md_text), lang))),
        extensions=["tables", "fenced_code", "attr_list", "sane_lists", "md_in_html"],
    )


# -------------------------------------------------- post-processing of HTML

def number_references(html_text):
    """Give the reference list items ids and link inline (N) citations to them."""
    m = re.search(r'(<h2[^>]*>\s*(?:\d+\.\s*)?References?.*?</h2>)(.*)', html_text,
                  re.I | re.S)
    if not m:
        return html_text, 0
    head, tail = m.group(1), m.group(2)
    n = [0]

    def add_id(li):
        n[0] += 1
        return f'<li id="ref-{n[0]}">'

    tail_new = re.sub(r"<li>", add_id, tail)
    if not n[0]:
        return html_text, 0
    tail_new = tail_new.replace("<ol>", '<ol class="refs">', 1)
    tail_new = tail_new.replace("<ul>", '<ul class="refs">', 1)
    body = html_text[:m.start()] + head + tail_new
    total = n[0]

    def link(mm):
        nums = [x.strip() for x in mm.group(1).split(",")]
        if not all(x.isdigit() and 1 <= int(x) <= total for x in nums):
            return mm.group(0)
        out = ", ".join(f'<a class="cite" href="#ref-{x}">{x}</a>' for x in nums)
        return f"({out})"

    # Only cite-link the document body, never the reference list itself.
    split = body.index(head)
    head_part = re.sub(r"\((\d+(?:\s*,\s*\d+)*)\)", link, body[:split])
    return head_part + body[split:], total


def add_anchors_and_toc(html_text):
    """Add id anchors to h2/h3 and return (html, toc_items)."""
    toc, used = [], set()

    def slug(text):
        s = re.sub(r"<[^>]+>", "", text)
        s = re.sub(r"[^\w\s-]", "", html.unescape(s)).strip().lower()
        s = re.sub(r"[\s_]+", "-", s)[:60] or "section"
        base, i = s, 2
        while s in used:
            s, i = f"{base}-{i}", i + 1
        used.add(s)
        return s

    def repl(m):
        lvl, attrs, text = m.group(1), m.group(2), m.group(3)
        if "id=" in attrs:
            return m.group(0)
        s = slug(text)
        toc.append((int(lvl), s, re.sub(r"<[^>]+>", "", text)))
        return (f'<h{lvl}{attrs} id="{s}">{text}'
                f'<a class="anchor" href="#{s}" aria-label="Link to section">#</a></h{lvl}>')

    out = re.sub(r"<h([23])([^>]*)>(.*?)</h\1>", repl, html_text, flags=re.S)
    return out, toc


def wrap_tables(html_text):
    return html_text.replace("<table>", '<div class="tablewrap"><table>').replace(
        "</table>", "</table></div>")


def mark_claim_rows(html_text):
    """Tag claims-register rows with their status so they can be filtered."""
    def row(m):
        body = m.group(0)
        for token, cls in STATUS_CLASS:
            if token in body:
                tagged = body.replace(
                    token, f'<span class="status {cls}">{token}</span>', 1)
                return tagged.replace("<tr>", f'<tr data-status="{token}">', 1)
        return body
    return re.sub(r"<tr>.*?</tr>", row, html_text, flags=re.S)


# ------------------------------------------------------------------ chrome

def tier_bar(counts, lang="en"):
    total = sum(counts.values())
    if total < 5:
        return ""
    segs, keys = [], []
    for t in "ABCD":
        c = counts[t]
        if c:
            segs.append(f'<span class="tier-{t.lower()}" style="width:{c/total*100:.2f}%"></span>')
        nm = TIER_FR[t] if lang == "fr" else TIER_NAMES[t]
        keys.append(f'<span><span class="tier tier-{t.lower()}">{t}</span> '
                    f'{nm} <b>{c}</b></span>')
    return (f'<div class="tierbar">'
            f'<p class="tierbar-head">{UI[lang]["tierhead"]} '
            f'<span>({total} {UI[lang]["tiercount"]})</span></p>'
            f'<div class="track">{"".join(segs)}</div>'
            f'<div class="keys">{"".join(keys)}</div></div>')


def summary_panel(summ, lang="en"):
    if not summ:
        return ""
    found = "".join(f"<li>{x}</li>" for x in summ.get("key_findings", []))
    struck = "".join(f"<li>{x}</li>" for x in summ.get("rejected", []))
    note = summ.get("note")
    found_label = summ.get("found_label", UI[lang]["found"])
    struck_label = summ.get("struck_label", UI[lang]["struck"])
    parts = [f'<div class="found"><h3>{html.escape(found_label)}</h3><ul>{found}</ul></div>']
    if struck:
        parts.append(f'<div class="struck"><h3>{html.escape(struck_label)}</h3><ul>{struck}</ul></div>')
    if note:
        parts.append(f'<div class="note"><b>Note</b>{note}</div>')
    return f'<section class="summary">{"".join(parts)}</section>'


def toc_html(toc, lang="en"):
    if len(toc) < 3:
        return ""
    items = "".join(
        f'<li class="lvl-{lvl}"><a href="#{s}">{html.escape(t)}</a></li>' for lvl, s, t in toc)
    return (f'<nav class="toc" aria-label="{UI[lang]["toc"]}"><p class="toc-head">{UI[lang]["toc"]}</p>'
            f'<ol>{items}</ol></nav>')


def nav_html(active_slug, pages, lang="en"):
    home = "index.html" if lang == "en" else "index-fr.html"
    items = ['<a href="%s"%s>%s</a>'
             % (home, ' class="active"' if active_slug in ("index", "index-fr") else "",
                UI[lang]["overview"])]
    for folder, label in SECTIONS:
        group = [p for p in pages if p["folder"] == folder]
        if not group:
            continue
        pref = NAV_PRIMARY.get(folder)
        target = next((p for p in group if p["stem"] == pref), group[0])
        cls = ' class="active"' if any(p["slug"] == active_slug for p in group) else ""
        lbl = SECTION_FR.get(folder, label) if lang == "fr" else label
        items.append(f'<a href="{target["slug"]}.html"{cls}>{html.escape(lbl)}</a>')
    return "\n        ".join(items)


PAGE = """<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{ogtitle}">
<meta property="og:description" content="{desc}">
<link rel="stylesheet" href="assets/style.css?v={cssv}">
</head>
<body>
<header class="masthead">
  <div class="masthead-inner">
    <a class="wordmark" href="index.html">Particle Acceleration</a>
    <nav>
        {nav}
    </nav>
    <div class="langswitch">{langswitch}</div>
  </div>
</header>
{body}
<footer>
  <div class="shell">
    <p>{foot1}</p>
    <p>{foot2}<br>
    <a href="https://github.com/rbndchsn/particle_ac">github.com/rbndchsn/particle_ac</a><br>
    <span class="buildmark">build {cssv}</span></p>
  </div>
</footer>
<script src="assets/site.js?v={jsv}" defer></script>
</body>
</html>
"""


def filters_html(lang):
    btns = "".join(
        f'<button aria-pressed="{str(i == 0).lower()}" data-f="{html.escape(k)}">'
        f'{html.escape(lab)}</button>'
        for i, (k, lab) in enumerate(FILTERS[lang]))
    word = "claims" if lang == "en" else "affirmations"
    return (f'<div class="filters" data-filter-table data-word="{word}">'
            f'{btns}<span class="count"></span></div>')


def langswitch_html(lang):
    """EN / FR toggle. Research pages link to the landing page of the other language."""
    en_cls = ' class="on"' if lang == "en" else ""
    fr_cls = ' class="on"' if lang == "fr" else ""
    return (f'<a href="index.html"{en_cls} hreflang="en">EN</a>'
            f'<span aria-hidden="true">/</span>'
            f'<a href="index-fr.html"{fr_cls} hreflang="fr">FR</a>')


def slugify_path(folder, path):
    stem = re.sub(r"_v\d+$", "", path.stem)
    return f"{folder.split('_', 1)[0]}-{stem}".replace("_", "-")


SITE_NAME = [""]
ASSETV = {"css": "0", "js": "0"}


def build():
    SITE_NAME[0] = str((split_frontmatter(
        (SITE / "content" / "index.md").read_text(encoding="utf-8"))[0]).get("title", ""))
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "assets").mkdir(exist_ok=True)
    shutil.copy(SITE / "assets" / "style.css", OUT / "assets" / "style.css")
    shutil.copy(SITE / "assets" / "site.js", OUT / "assets" / "site.js")
    import hashlib
    ASSETV["css"] = hashlib.sha1((SITE / "assets" / "style.css").read_bytes()).hexdigest()[:10]
    ASSETV["js"] = hashlib.sha1((SITE / "assets" / "site.js").read_bytes()).hexdigest()[:10]
    (OUT / ".nojekyll").write_text("")

    summaries = yaml.safe_load((SITE / "summaries.yaml").read_text()) or {}
    fr_titles = {}
    ft = SITE / "doc_titles.fr.yaml"
    if ft.exists():
        fr_titles = yaml.safe_load(ft.read_text(encoding="utf-8")) or {}

    pages = []
    for folder, label in SECTIONS:
        d = ROOT / folder
        if not d.exists():
            continue
        for f in sorted(d.glob("*.md")):
            if f.name.endswith(".fr.md"):
                continue
            meta, body = split_frontmatter(f.read_text(encoding="utf-8"))
            frf = f.with_suffix("").with_suffix(".fr.md")
            if not frf.exists():
                frf = d / (f.stem + ".fr.md")
            pages.append({
                "fr": frf if frf.exists() else None,
                "slug": slugify_path(folder, f), "folder": folder, "label": label,
                "stem": re.sub(r"_v\d+$", "", f.stem), "meta": meta, "body": body,
                "key": f"{folder}/{f.name}", "tiers": count_tiers(body),
            })

    for p in pages:
        content, nrefs = number_references(render_md(p["body"]))
        content, toc = add_anchors_and_toc(content)
        content = wrap_tables(content)
        is_register = p["stem"] == "claims_register"
        if is_register:
            content = mark_claim_rows(content)
        m = p["meta"]
        facts = [f'<span><b>{html.escape(str(m.get("version","v1")))}</b></span>',
                 f'<span>{html.escape(str(m.get("date","")))}</span>']
        if nrefs:
            facts.append(f'<span><b>{nrefs}</b> references</span>')
        facts.append(f'<span>{html.escape(str(m.get("status","")))}</span>')
        art = figures.DOC_ART.get(p["stem"])
        artmark = (f'<div class="doc-art">{figures.ART[art]("en")}</div>'
                   if art else "")
        header = (
            f'<div class="docmeta">'
            f'<div class="docmeta-main">'
            f'<p class="kicker">{html.escape(p["label"])}</p>'
            f'<h1>{html.escape(str(m.get("title", p["slug"])))}</h1>'
            f'<p class="sub">{html.escape(str(m.get("subtitle","")))}</p>'
            f'<div class="facts">{"".join(facts)}</div></div>'
            f'{artmark}'
            f'{tier_bar(p["tiers"])}</div>')
        filters = ""
        if is_register:
            filters = filters_html("en")
        toc_markup = toc_html(toc, "en")
        wrap = "with-rail" if toc_markup else "no-rail"
        body = (
            f'<main class="shell"><div class="{wrap}">{toc_markup}'
            f'<div>{header}{summary_panel(summaries.get(p["key"]), "en")}{filters}'
            f'<article>{content}</article></div></div></main>')
        if p.get("fr"):
            fmeta, fbody = split_frontmatter(p["fr"].read_text(encoding="utf-8"))
            fcontent, fnrefs = number_references(render_md(fbody, "fr"))
            fcontent, ftoc = add_anchors_and_toc(fcontent)
            fcontent = wrap_tables(fcontent)
            if is_register:
                fcontent = mark_claim_rows(fcontent)
            ffacts = [f'<span><b>{html.escape(str(fmeta.get("version","v1")))}</b></span>',
                      f'<span>{html.escape(str(fmeta.get("date","")))}</span>']
            if fnrefs:
                ffacts.append(f'<span><b>{fnrefs}</b> {UI["fr"]["refs"]}</span>')
            ffacts.append(f'<span>{html.escape(str(fmeta.get("status","")))}</span>')
            fart = (f'<div class="doc-art">{figures.ART[art]("fr")}</div>' if art else "")
            fheader = (
                f'<div class="docmeta"><div class="docmeta-main">'
                f'<p class="kicker">{html.escape(SECTION_FR.get(p["folder"], p["label"]))}</p>'
                f'<h1>{html.escape(str(fmeta.get("title", p["slug"])))}</h1>'
                f'<p class="sub">{html.escape(str(fmeta.get("subtitle","")))}</p>'
                f'<div class="facts">{"".join(ffacts)}</div></div>'
                f'{fart}{tier_bar(p["tiers"], "fr")}</div>')
            fbodyhtml = (
                f'<main class="shell">'
                f'<div class="{"with-rail" if toc_html(ftoc, "fr") else "no-rail"}">'
                f'{toc_html(ftoc, "fr")}<div>{fheader}'
                f'{filters_html("fr") if is_register else ""}'
                f'<article>{fcontent}</article></div></div></main>')
            (OUT / f'{p["slug"]}-fr.html').write_text(PAGE.format(
                title=f'{fmeta.get("title", p["slug"])} \u2014 {SITE_NAME[0]}',
                ogtitle=html.escape(str(fmeta.get("title", p["slug"]))),
                desc=html.escape(str(fmeta.get("subtitle", ""))[:180]),
                nav=nav_html(p["slug"], pages, "fr"), lang="fr",
                langswitch=langswitch_html("fr"),
                foot1=UI["fr"]["foot1"], foot2=UI["fr"]["foot2"],
                cssv=ASSETV["css"], jsv=ASSETV["js"],
                body=fbodyhtml), encoding="utf-8")

        (OUT / f'{p["slug"]}.html').write_text(PAGE.format(
            title=f'{m.get("title", p["slug"])} — {SITE_NAME[0]}',
            ogtitle=html.escape(str(m.get("title", p["slug"]))),
            desc=html.escape(str(m.get("subtitle", ""))[:180]),
            nav=nav_html(p["slug"], pages, "en"), lang="en",
            langswitch=langswitch_html("en"),
            foot1=UI["en"]["foot1"], foot2=UI["en"]["foot2"],
            cssv=ASSETV["css"], jsv=ASSETV["js"],
            body=body), encoding="utf-8")

    # ---- landing pages, one per language
    for lang, src, outfile in (("en", "index.md", "index.html"),
                               ("fr", "index.fr.md", "index-fr.html")):
        srcpath = SITE / "content" / src
        if not srcpath.exists():
            continue
        imeta, ibody = split_frontmatter(srcpath.read_text(encoding="utf-8"))
        u = UI[lang]
        cards = []
        for folder, label in SECTIONS:
            group = [p for p in pages if p["folder"] == folder]
            if not group:
                continue
            lbl = SECTION_FR.get(folder, label) if lang == "fr" else label
            cards.append(f'<div class="card-group"><h3>{html.escape(lbl)}</h3><div class="cards">')
            for p in group:
                t = p["tiers"]
                chips = "".join(
                    f'<span><span class="tier tier-{k.lower()}">{k}</span><b>{t[k]}</b></span>'
                    for k in "ABC" if t[k])
                tr = fr_titles.get(p["stem"], {}) if lang == "fr" else {}
                suffix = "-fr" if (lang == "fr" and p.get("fr")) else ""
                ct = tr.get("title", p["meta"].get("title", p["slug"]))
                cs = tr.get("subtitle", p["meta"].get("subtitle", ""))
                cards.append(
                    f'<a class="card" href="{p["slug"]}{suffix}.html">'
                    f'<span class="c-title">{html.escape(str(ct))}</span>'
                    f'<span class="c-tiers">{chips}</span>'
                    f'<span class="c-sub">{html.escape(str(cs))}</span></a>')
            cards.append("</div></div>")
        content, htoc = add_anchors_and_toc(wrap_tables(render_md(ibody, lang)))
        home_toc = "".join(
            f'<li><a href="#{sl}">{html.escape(tt)}</a></li>' for lv, sl, tt in htoc if lv == 2)
        rail_docs = "".join(
            '<li><a href="{s}{x}.html">{t}</a></li>'.format(
                s=p["slug"], x=("-fr" if (lang == "fr" and p.get("fr")) else ""),
                t=html.escape(str((fr_titles.get(p["stem"], {}) if lang == "fr" else {})
                                  .get("title", p["meta"].get("title", p["slug"])))))
            for p in pages)
        rail = (f'<aside class="home-rail">'
                f'<div class="rail-block"><p class="toc-head">{u["onpage"]}</p>'
                f'<ol class="rail-list">{home_toc}</ol></div>'
                f'<div class="rail-block"><p class="toc-head">{u["docs"]}</p>'
                f'<ol class="rail-list">{rail_docs}</ol></div></aside>')
        hero = (f'<div class="hero"><div class="shell hero-grid"><div class="hero-text">'
                f'<p class="eyebrow">{u["archive"]} \u00b7 {len(pages)} documents</p>'
                f'<h1>{html.escape(str(imeta.get("title","")))}</h1>'
                f'<p class="standfirst">{html.escape(str(imeta.get("subtitle","")))}</p>'
                f'<div class="byline"><span>{html.escape(str(imeta.get("author","")))}</span>'
                f'<span>{html.escape(str(imeta.get("date","")))}</span>'
                f'<span>{sum(sum(p["tiers"].values()) for p in pages)} {u["claims"]}</span>'
                f'</div></div>'
                f'<div class="hero-fig">{figures.hero_illustration(lang)}</div>'
                f'</div></div>')
        body = (f'{hero}<main class="shell home">'
                f'<div class="home-grid"><article>{content}</article>{rail}</div>'
                f'<section class="doclist"><h2>{u["thedocs"]}</h2>'
                f'<p class="clickprompt">{u["clickdocs"]}</p>{"".join(cards)}</section>'
                f'</main>')
        slug = "index" if lang == "en" else "index-fr"
        (OUT / outfile).write_text(PAGE.format(
            title=str(imeta.get("title", "")),
            ogtitle=html.escape(str(imeta.get("title", ""))),
            desc=html.escape(str(imeta.get("subtitle", ""))[:180]),
            nav=nav_html(slug, pages, lang), lang=lang,
            langswitch=langswitch_html(lang),
            foot1=u["foot1"], foot2=u["foot2"],
            cssv=ASSETV["css"], jsv=ASSETV["js"],
            body=body), encoding="utf-8")

    total = sum(sum(p["tiers"].values()) for p in pages)
    print(f"built {len(pages)+1} pages, {total} tier-labelled claims -> {OUT}")
    for p in pages:
        t = p["tiers"]
        print(f'  {p["slug"]+".html":44s} A{t["A"]:>4} B{t["B"]:>3} C{t["C"]:>3} D{t["D"]:>3}')


if __name__ == "__main__":
    build()
