#!/usr/bin/env python3
"""
Static site generator for the particle acceleration research archive.

Reads the markdown research files, renders them to a static site in docs/,
and auto-styles the inline evidence-tier markers ([A], [B], [C], [D]) so the
epistemic status of every claim is visible on the page.

Usage:  python3 site/build.py
"""

import html
import os
import re
import shutil
import sys
from pathlib import Path

import markdown
import yaml

ROOT = Path(__file__).resolve().parent.parent
RESEARCH = ROOT
CONTENT = ROOT / "site" / "content"
OUT = ROOT / "docs"

# Section folders in read order. Title and blurb are used for navigation.
SECTIONS = [
    ("00_method", "Method"),
    ("01_foundations", "Foundations"),
    ("02_theory_critique", "Theory"),
    ("03_hardware_systems", "Hardware"),
    ("04_software_algorithmic", "Software"),
    ("05_publication_governance", "Publication"),
    ("06_dissent_register", "Dissent"),
    ("07_epistemic_audit", "Known vs Assumed"),
]

TIER_NAMES = {
    "A": "Documented",
    "B": "Contested",
    "C": "Inference",
    "D": "Rejected",
}


def split_frontmatter(text):
    """Return (metadata dict, body) for a file with YAML frontmatter."""
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


def badge_tiers(md_text):
    """Wrap inline [A] / [B] / [C] / [D] markers in styled spans.

    Fenced code blocks are protected so code samples are left alone. A marker
    immediately followed by '(' is a markdown link and is skipped.
    """
    chunks = md_text.split("```")
    for i in range(0, len(chunks), 2):  # even chunks are outside code fences
        def repl(m):
            t = m.group(1)
            return (
                f'<span class="tier tier-{t.lower()}" '
                f'title="Tier {t} — {TIER_NAMES[t]}">{t}</span>'
            )
        chunks[i] = re.sub(r"\[([ABCD])\](?!\()", repl, chunks[i])
    return "```".join(chunks)


def render_md(md_text):
    return markdown.markdown(
        badge_tiers(md_text),
        extensions=["tables", "fenced_code", "toc", "attr_list", "sane_lists"],
        extension_configs={"toc": {"permalink": False}},
    )


# When a section holds several files, this one is the section's nav target.
NAV_PRIMARY = {"00_method": "research_frame"}


def nav_html(active_slug):
    items = ['<a href="index.html"%s>Thesis</a>'
             % (' class="active"' if active_slug == "index" else "")]
    for folder, label in SECTIONS:
        d = RESEARCH / folder
        if not d.exists():
            continue
        files = sorted(d.glob("*.md"))
        if not files:
            continue
        preferred = NAV_PRIMARY.get(folder)
        target = next(
            (f for f in files if re.sub(r"_v\d+$", "", f.stem) == preferred),
            files[0],
        )
        # Keep the section highlighted whichever of its files is open.
        section_slugs = {slugify(folder, f) for f in files}
        cls = ' class="active"' if active_slug in section_slugs else ""
        items.append(f'<a href="{slugify(folder, target)}.html"{cls}>{label}</a>')
    return "\n      ".join(items)


def slugify(folder, path):
    stem = re.sub(r"_v\d+$", "", path.stem)
    return f"{folder.split('_', 1)[0]}-{stem}".replace("_", "-")


PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="masthead">
  <a class="wordmark" href="index.html">The Instrument and Its Blind Spot</a>
  <nav>
      {nav}
  </nav>
</header>
<main class="{bodyclass}">
{meta_block}
<article>
{content}
</article>
</main>
<footer>
  <p>Research archive. Every claim carries an evidence tier; rejected claims are kept on the
  record rather than removed. Source and revision history:
  <a href="https://github.com/rbndchsn/particle_ac">github.com/rbndchsn/particle_ac</a>.</p>
</footer>
</body>
</html>
"""


def meta_block(meta, extra_files=None):
    if not meta:
        return ""
    rows = []
    for key in ("subtitle", "version", "status", "date", "author"):
        val = meta.get(key)
        if val:
            rows.append(
                f'<div class="m-row"><dt>{html.escape(key)}</dt>'
                f'<dd>{html.escape(str(val))}</dd></div>'
            )
    title = html.escape(str(meta.get("title", "")))
    extra = ""
    if extra_files:
        links = " · ".join(
            f'<a href="{s}.html">{html.escape(t)}</a>' for s, t in extra_files
        )
        extra = f'<div class="m-row"><dt>also in section</dt><dd>{links}</dd></div>'
    return (
        f'<div class="docmeta"><h1>{title}</h1>'
        f'<dl>{"".join(rows)}{extra}</dl></div>'
    )


def legend():
    return """
<aside class="legend">
  <h2>How to read this</h2>
  <p>Every substantive claim in this archive carries an evidence tier. The tier is part of
  the claim, not a disclaimer attached to it.</p>
  <ul>
    <li><span class="tier tier-a">A</span><strong>Documented.</strong> Acknowledged inside
    the field — primary literature, collaboration technical documents, procurement or
    court records.</li>
    <li><span class="tier tier-b">B</span><strong>Contested.</strong> Disputed inside the
    field, with named advocates on both sides, each cited from their own words.</li>
    <li><span class="tier tier-c">C</span><strong>Inference.</strong> Follows from Tier A
    facts but has not been assembled or tested by the field. Not a finding. States what it
    rests on and what would falsify it.</li>
    <li><span class="tier tier-d">D</span><strong>Rejected.</strong> Examined and not
    supported. Kept on the record with the reason it failed.</li>
  </ul>
</aside>
"""


def build():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "assets").mkdir(exist_ok=True)
    shutil.copy(ROOT / "site" / "assets" / "style.css", OUT / "assets" / "style.css")
    (OUT / ".nojekyll").write_text("")

    pages = []
    for folder, label in SECTIONS:
        d = RESEARCH / folder
        if not d.exists():
            continue
        files = sorted(d.glob("*.md"))
        for f in files:
            meta, body = split_frontmatter(f.read_text(encoding="utf-8"))
            pages.append(
                {
                    "slug": slugify(folder, f),
                    "folder": folder,
                    "label": label,
                    "meta": meta,
                    "body": body,
                    "path": f.relative_to(ROOT),
                }
            )

    # Research document pages
    for p in pages:
        siblings = [
            (q["slug"], q["meta"].get("title", q["slug"]))
            for q in pages
            if q["folder"] == p["folder"] and q["slug"] != p["slug"]
        ]
        content = render_md(p["body"])
        if p["folder"] == "00_method":
            content = legend() + content
        (OUT / f'{p["slug"]}.html').write_text(
            PAGE.format(
                title=f'{p["meta"].get("title", p["slug"])} — Particle Accelerators',
                desc=html.escape(str(p["meta"].get("subtitle", ""))[:160]),
                nav=nav_html(p["slug"]),
                bodyclass="doc",
                meta_block=meta_block(p["meta"], siblings),
                content=content,
            ),
            encoding="utf-8",
        )

    # Landing page
    index_md = (CONTENT / "index.md").read_text(encoding="utf-8")
    imeta, ibody = split_frontmatter(index_md)
    cards = []
    seen = set()
    for folder, label in SECTIONS:
        group = [p for p in pages if p["folder"] == folder]
        if not group or folder in seen:
            continue
        seen.add(folder)
        cards.append('<div class="card-group"><h3>%s</h3>' % html.escape(label))
        for p in group:
            st = html.escape(str(p["meta"].get("status", "")))
            cards.append(
                '<a class="card" href="{slug}.html">'
                '<span class="c-title">{t}</span>'
                '<span class="c-sub">{s}</span>'
                '<span class="c-status">{st}</span></a>'.format(
                    slug=p["slug"],
                    t=html.escape(str(p["meta"].get("title", p["slug"]))),
                    s=html.escape(str(p["meta"].get("subtitle", ""))),
                    st=st,
                )
            )
        cards.append("</div>")
    pending = [
        (label, folder) for folder, label in SECTIONS
        if not (RESEARCH / folder).exists() or not list((RESEARCH / folder).glob("*.md"))
    ]
    pending_html = ""
    if pending:
        pending_html = (
            '<div class="pending"><h3>Research in progress</h3><p>'
            + ", ".join(html.escape(l) for l, _ in pending)
            + ". These sections are being researched and are not yet published.</p></div>"
        )
    body = render_md(ibody) + legend() + '<section class="docs"><h2>The documents</h2>' \
        + "\n".join(cards) + pending_html + "</section>"
    (OUT / "index.html").write_text(
        PAGE.format(
            title="The Instrument and Its Blind Spot — particle accelerators, and what the field cannot see",
            desc=html.escape(str(imeta.get("subtitle", ""))[:160]),
            nav=nav_html("index"),
            bodyclass="home",
            meta_block="",
            content=body,
        ),
        encoding="utf-8",
    )

    print(f"built {len(pages) + 1} pages -> {OUT}")
    for p in pages:
        print(f"  {p['slug']}.html  <-  {p['path']}")
    if pending:
        print("  pending:", ", ".join(l for l, _ in pending))


if __name__ == "__main__":
    build()
