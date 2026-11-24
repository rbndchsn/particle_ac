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
]
NAV_PRIMARY = {"00_method": "research_frame", "03_hardware_systems": "trigger_data_destruction"}
TIER_NAMES = {"A": "Documented", "B": "Contested", "C": "Inference", "D": "Rejected"}
STATUS_CLASS = [
    ("SUPPORTED-AS-INFERENCE", "st-inference"), ("REJECTED", "st-rejected"),
    ("SUPPORTED", "st-supported"), ("UNTESTED", "st-untested"), ("WEAKENED", "st-weakened"),
]


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


def embed_figures(md_text):
    return re.sub(r"\{\{fig:([a-z0-9-]+)\}\}",
                  lambda m: figures.render(m.group(1)), md_text)


def render_md(md_text):
    return markdown.markdown(
        strikethrough(badge_tiers(embed_figures(normalise_headings(md_text)))),
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

def tier_bar(counts):
    total = sum(counts.values())
    if total < 5:
        return ""
    segs, keys = [], []
    for t in "ABCD":
        c = counts[t]
        if c:
            segs.append(f'<span class="tier-{t.lower()}" style="width:{c/total*100:.2f}%"></span>')
        keys.append(f'<span><span class="tier tier-{t.lower()}">{t}</span> '
                    f'{TIER_NAMES[t]} <b>{c}</b></span>')
    return (f'<div class="tierbar"><div class="track">{"".join(segs)}</div>'
            f'<div class="keys">{"".join(keys)}</div></div>')


def summary_panel(summ):
    if not summ:
        return ""
    found = "".join(f"<li>{x}</li>" for x in summ.get("key_findings", []))
    struck = "".join(f"<li>{x}</li>" for x in summ.get("rejected", []))
    note = summ.get("note")
    parts = [f'<div class="found"><h3>What this stream found</h3><ul>{found}</ul></div>']
    if struck:
        parts.append(f'<div class="struck"><h3>Examined and struck out</h3><ul>{struck}</ul></div>')
    if note:
        parts.append(f'<div class="note"><b>Note</b>{note}</div>')
    return f'<section class="summary">{"".join(parts)}</section>'


def toc_html(toc):
    if len(toc) < 3:
        return ""
    items = "".join(
        f'<li class="lvl-{lvl}"><a href="#{s}">{html.escape(t)}</a></li>' for lvl, s, t in toc)
    return (f'<nav class="toc" aria-label="Contents"><p class="toc-head">Contents</p>'
            f'<ol>{items}</ol></nav>')


def nav_html(active_slug, pages):
    items = ['<a href="index.html"%s>Overview</a>'
             % (' class="active"' if active_slug == "index" else "")]
    for folder, label in SECTIONS:
        group = [p for p in pages if p["folder"] == folder]
        if not group:
            continue
        pref = NAV_PRIMARY.get(folder)
        target = next((p for p in group if p["stem"] == pref), group[0])
        cls = ' class="active"' if any(p["slug"] == active_slug for p in group) else ""
        items.append(f'<a href="{target["slug"]}.html"{cls}>{html.escape(label)}</a>')
    return "\n        ".join(items)


PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{ogtitle}">
<meta property="og:description" content="{desc}">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="masthead">
  <div class="masthead-inner">
    <a class="wordmark" href="index.html">The Instrument &amp; Its Blind Spot</a>
    <nav>
        {nav}
    </nav>
  </div>
</header>
{body}
<footer>
  <div class="shell">
    <p>Every claim in this archive carries an evidence tier. Claims examined and rejected are
    kept on the record rather than removed — including both hypotheses the project began with.</p>
    <p>Source, data and full revision history:<br>
    <a href="https://github.com/rbndchsn/particle_ac">github.com/rbndchsn/particle_ac</a></p>
  </div>
</footer>
<script src="assets/site.js" defer></script>
</body>
</html>
"""


def slugify_path(folder, path):
    stem = re.sub(r"_v\d+$", "", path.stem)
    return f"{folder.split('_', 1)[0]}-{stem}".replace("_", "-")


def build():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "assets").mkdir(exist_ok=True)
    shutil.copy(SITE / "assets" / "style.css", OUT / "assets" / "style.css")
    shutil.copy(SITE / "assets" / "site.js", OUT / "assets" / "site.js")
    (OUT / ".nojekyll").write_text("")

    summaries = yaml.safe_load((SITE / "summaries.yaml").read_text()) or {}

    pages = []
    for folder, label in SECTIONS:
        d = ROOT / folder
        if not d.exists():
            continue
        for f in sorted(d.glob("*.md")):
            meta, body = split_frontmatter(f.read_text(encoding="utf-8"))
            pages.append({
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
        header = (
            f'<div class="docmeta">'
            f'<p class="kicker">{html.escape(p["label"])}</p>'
            f'<h1>{html.escape(str(m.get("title", p["slug"])))}</h1>'
            f'<p class="sub">{html.escape(str(m.get("subtitle","")))}</p>'
            f'<div class="facts">{"".join(facts)}</div>'
            f'{tier_bar(p["tiers"])}</div>')
        filters = ""
        if is_register:
            filters = ('<div class="filters" data-filter-table>'
                       '<button aria-pressed="true" data-f="all">All claims</button>'
                       '<button aria-pressed="false" data-f="SUPPORTED">Supported</button>'
                       '<button aria-pressed="false" data-f="SUPPORTED-AS-INFERENCE">Inference</button>'
                       '<button aria-pressed="false" data-f="REJECTED">Rejected</button>'
                       '<button aria-pressed="false" data-f="UNTESTED">Untested</button>'
                       '<span class="count"></span></div>')
        toc_markup = toc_html(toc)
        wrap = "with-rail" if toc_markup else "no-rail"
        body = (
            f'<main class="shell"><div class="{wrap}">{toc_markup}'
            f'<div>{header}{summary_panel(summaries.get(p["key"]))}{filters}'
            f'<article>{content}</article></div></div></main>')
        (OUT / f'{p["slug"]}.html').write_text(PAGE.format(
            title=f'{m.get("title", p["slug"])} — The Instrument and Its Blind Spot',
            ogtitle=html.escape(str(m.get("title", p["slug"]))),
            desc=html.escape(str(m.get("subtitle", ""))[:180]),
            nav=nav_html(p["slug"], pages), body=body), encoding="utf-8")

    # ---- landing page
    imeta, ibody = split_frontmatter((SITE / "content" / "index.md").read_text(encoding="utf-8"))
    cards = []
    for folder, label in SECTIONS:
        group = [p for p in pages if p["folder"] == folder]
        if not group:
            continue
        cards.append(f'<div class="card-group"><h3>{html.escape(label)}</h3><div class="cards">')
        for p in group:
            t = p["tiers"]
            chips = "".join(
                f'<span><span class="tier tier-{k.lower()}">{k}</span><b>{t[k]}</b></span>'
                for k in "ABC" if t[k])
            cards.append(
                f'<a class="card" href="{p["slug"]}.html">'
                f'<span class="c-title">{html.escape(str(p["meta"].get("title", p["slug"])))}</span>'
                f'<span class="c-tiers">{chips}</span>'
                f'<span class="c-sub">{html.escape(str(p["meta"].get("subtitle","")))}</span></a>')
        cards.append("</div></div>")
    missing = [l for f, l in SECTIONS if not any(p["folder"] == f for p in pages)]
    pending = (f'<div class="pending"><h3>In progress</h3><p>{", ".join(missing)}.</p></div>'
               if missing else "")
    content, htoc = add_anchors_and_toc(wrap_tables(render_md(ibody)))
    hero = (
        f'<div class="hero"><div class="shell">'
        f'<p class="eyebrow">Research archive · {len(pages)} documents</p>'
        f'<h1>{html.escape(str(imeta.get("title","")))}</h1>'
        f'<p class="standfirst">{html.escape(str(imeta.get("subtitle","")))}</p>'
        f'<div class="byline"><span>{html.escape(str(imeta.get("author","")))}</span>'
        f'<span>{html.escape(str(imeta.get("date","")))}</span>'
        f'<span>{sum(sum(p["tiers"].values()) for p in pages)} tier-labelled claims</span>'
        f'</div></div></div>')
    home_toc = "".join(
        f'<li><a href="#{s}">{html.escape(t)}</a></li>' for lvl, s, t in htoc if lvl == 2)
    rail_docs = "".join(
        f'<li><a href="{p["slug"]}.html">{html.escape(str(p["meta"].get("title", p["slug"])))}</a></li>'
        for p in pages)
    rail = (f'<aside class="home-rail">'
            f'<div class="rail-block"><p class="toc-head">On this page</p>'
            f'<ol class="rail-list">{home_toc}</ol></div>'
            f'<div class="rail-block"><p class="toc-head">Documents</p>'
            f'<ol class="rail-list">{rail_docs}</ol></div></aside>')
    body = (f'{hero}<main class="shell home">'
            f'<div class="home-grid"><article>{content}</article>{rail}</div>'
            f'<section class="doclist"><h2>The documents</h2>{"".join(cards)}{pending}</section>'
            f'</main>')
    (OUT / "index.html").write_text(PAGE.format(
        title="The Instrument and Its Blind Spot — particle accelerators and what the field cannot see",
        ogtitle="The Instrument and Its Blind Spot",
        desc=html.escape(str(imeta.get("subtitle", ""))[:180]),
        nav=nav_html("index", pages), body=body), encoding="utf-8")

    total = sum(sum(p["tiers"].values()) for p in pages)
    print(f"built {len(pages)+1} pages, {total} tier-labelled claims -> {OUT}")
    for p in pages:
        t = p["tiers"]
        print(f'  {p["slug"]+".html":44s} A{t["A"]:>4} B{t["B"]:>3} C{t["C"]:>3} D{t["D"]:>3}')


if __name__ == "__main__":
    build()
