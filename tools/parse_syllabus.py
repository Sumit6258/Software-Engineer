#!/usr/bin/env python3
"""Parse the authoritative syllabus (.docx) into curriculum/curriculum.json.

The source document encodes its hierarchy like this (discovered by inspecting
the OOXML, not guessed):

    outlineLvl 0                 -> PART heading
    outlineLvl 1 "N. Title"      -> numbered subject area
    outlineLvl 1 (unnumbered)    -> section heading inside a part (Part XV)
    outlineLvl 2                 -> sub-section heading inside a subject
    plain paragraph "- Title"    -> group (chapter) heading
    bullet paragraph (numPr)     -> leaf topic
    plain paragraph (other)      -> tag / description / label / card / note
    table                        -> structured leaf rows

The export that produced the .docx also left some noise (web-image captions,
citation chips). The parser removes it and records every removal so nothing is
dropped silently. See curriculum/extraction-report.md.

Usage:  python3 tools/parse_syllabus.py [--docx PATH] [--out PATH]
"""
import argparse
import hashlib
import json
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from collections import Counter
from urllib.parse import urlparse

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"


def q(tag):
    return "{%s}%s" % (W, tag)


def norm(s):
    return re.sub(r"\s+", " ", (s or "").replace("\u00a0", " ")).strip()


def slugify(s, limit=70):
    s = s.lower().replace("&", " and ")
    s = re.sub(r"[’'`]", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    if len(s) > limit:
        s = s[:limit].rsplit("-", 1)[0]
    return s


SMALL_WORDS = {"and", "of", "the", "in", "to", "for", "a", "on", "vs", "or"}


def smart_title(s):
    out = []
    for i, w in enumerate(s.lower().split()):
        out.append(w if (i and w in SMALL_WORDS) else w.capitalize())
    return " ".join(out)


ROMAN = {"I": 1, "V": 5, "X": 10, "L": 50}


def roman_to_int(r):
    total = 0
    for i, ch in enumerate(r):
        v = ROMAN[ch]
        total += -v if i + 1 < len(r) and ROMAN[r[i + 1]] > v else v
    return total


# --------------------------------------------------------------------------
# Reading the OOXML
# --------------------------------------------------------------------------
def load_rels(z):
    rels = {}
    root = ET.fromstring(z.read("word/_rels/document.xml.rels"))
    for rel in root.findall("{%s}Relationship" % REL_NS):
        rels[rel.get("Id")] = rel.get("Target")
    return rels


def collect_runs(node, in_link, url, rels, out):
    for ch in node:
        if ch.tag == q("hyperlink"):
            collect_runs(ch, True, rels.get(ch.get("{%s}id" % R)), rels, out)
        elif ch.tag == q("r"):
            txt = ""
            for x in ch:
                if x.tag == q("t"):
                    txt += x.text or ""
                elif x.tag == q("tab"):
                    txt += " "
            out.append((txt, in_link, url))
        elif ch.tag in (q("pPr"), q("rPr"), q("bookmarkStart"), q("bookmarkEnd")):
            continue
        else:
            collect_runs(ch, in_link, url, rels, out)


def read_paragraph(p, rels):
    runs = []
    collect_runs(p, False, None, rels, runs)
    plain = norm("".join(t for t, linked, _ in runs if not linked))
    link_text = norm("".join(t for t, linked, _ in runs if linked))
    urls = [u for _, linked, u in runs if linked and u]
    ppr = p.find(q("pPr"))
    outline = None
    numid = None
    if ppr is not None:
        o = ppr.find(q("outlineLvl"))
        if o is not None:
            outline = int(o.get(q("val")))
        n = ppr.find(q("numPr"))
        if n is not None and n.find(q("numId")) is not None:
            numid = n.find(q("numId")).get(q("val"))
    return {
        "plain": plain,
        "link_text": link_text,
        "url": urls[0] if urls else None,
        "outline": outline,
        "numid": numid,
    }


def read_table(tbl):
    rows = []
    for tr in tbl.findall(q("tr")):
        row = []
        for tc in tr.findall(q("tc")):
            parts = []
            for p in tc.iter(q("p")):
                t = norm("".join((x.text or "") for x in p.iter(q("t"))))
                if t:
                    parts.append(t)
            row.append(" / ".join(parts))
        rows.append(row)
    return rows


def clean_url(u):
    """Drop tracking query strings left by the export (e.g. utm_source)."""
    pu = urlparse(u)
    return "%s://%s%s" % (pu.scheme, pu.netloc, pu.path or "/")


CHIP_RE = re.compile(r"^[A-Za-z][A-Za-z0-9 .'’&-]{0,48}\+\d+$")


def build_events(docx_path):
    z = zipfile.ZipFile(docx_path)
    rels = load_rels(z)
    body = ET.fromstring(z.read("word/document.xml")).find(q("body"))
    events, noise = [], []
    for idx, el in enumerate(body):
        if el.tag == q("tbl"):
            events.append({"type": "table", "rows": read_table(el), "src": idx})
            continue
        if el.tag != q("p"):
            continue
        p = read_paragraph(el, rels)
        plain = p["plain"]
        host = urlparse(p["url"]).netloc if p["url"] else ""
        # --- noise: hyperlinked web-image captions ---------------------
        if not plain and p["link_text"] and host.endswith("images.openai.com"):
            noise.append({"kind": "image-caption-link", "text": p["link_text"], "src": idx})
            events.append({"type": "caption", "src": idx})
            continue
        # --- noise: trailing official-site link text -------------------
        url = None
        if plain and p["link_text"] and p["url"]:
            url = clean_url(p["url"])
            noise.append({"kind": "trailing-link-text", "text": p["link_text"],
                          "kept_url": url, "src": idx})
        if p["outline"] == 0:
            m = re.match(r"^PART ([IVXL]+) — (.+)$", plain)
            if not m:
                sys.exit("Unparseable part heading at body index %d: %r" % (idx, plain))
            events.append({"type": "part", "roman": m.group(1), "title": m.group(2),
                           "src": idx})
        elif p["outline"] == 1:
            m = re.match(r"^(\d+)\.\s+(.+)$", plain)
            if m:
                events.append({"type": "subject", "number": int(m.group(1)),
                               "title": m.group(2), "src": idx})
            else:
                events.append({"type": "section", "title": plain, "src": idx})
        elif p["outline"] is not None and p["outline"] >= 2:
            events.append({"type": "h2", "title": plain, "src": idx})
        elif p["numid"] is not None:
            events.append({"type": "item", "text": plain, "numid": p["numid"], "src": idx})
        elif plain.startswith("- "):
            events.append({"type": "group", "title": plain[2:].strip(), "src": idx})
        elif not plain:
            continue
        elif CHIP_RE.match(plain):
            noise.append({"kind": "citation-chip", "text": plain, "src": idx})
        else:
            events.append({"type": "note", "text": plain, "url": url, "src": idx})
    return events, noise


# --------------------------------------------------------------------------
# Building the tree
# --------------------------------------------------------------------------
def new_group(title, kind, synthesized=False, src=None):
    return {"title": title, "kind": kind, "synthesized": synthesized,
            "src": src, "leaves": []}


def add_leaf(group, text, kind="item", sub=None, detail=None, url=None, src=None, **extra):
    leaf = {"text": text, "kind": kind}
    if sub:
        leaf["subgroup"] = sub
    if detail:
        leaf["detail"] = detail
    if url:
        leaf["url"] = url
    for k, v in extra.items():
        if v is not None:
            leaf[k] = v
    if src is not None:
        leaf["src"] = src
    group["leaves"].append(leaf)
    return leaf


def split_list(s):
    return [norm(x) for x in re.split(r",", s) if norm(x)]


def parse(docx_path):
    events, noise = build_events(docx_path)
    decisions = []
    parts, part, subj, group, sub = [], None, None, None, None
    card_state, card_name = None, None
    section = None  # unnumbered section inside a part (Part XV)

    def nxt(i):
        return events[i + 1] if i + 1 < len(events) else None

    for i, ev in enumerate(events):
        t = ev["type"]
        if t == "part":
            part = {"roman": ev["roman"], "number": roman_to_int(ev["roman"]),
                    "title": ev["title"], "tags": [], "description": [],
                    "subjects": [], "blocks": [], "closing_notes": [], "src": ev["src"]}
            parts.append(part)
            subj = group = sub = section = None
        elif t == "subject":
            subj = {"number": ev["number"], "title": ev["title"], "tags": [],
                    "level_range": None, "description": [], "groups": [],
                    "closing_notes": [], "src": ev["src"]}
            part["subjects"].append(subj)
            group = sub = section = None
            card_state = None
        elif t == "section":
            section = {"title": ev["title"]}
            part["blocks"].append({"type": "heading", "title": ev["title"]})
            subj = group = sub = None
        elif t == "h2":
            group = new_group(ev["title"], "h2", src=ev["src"])
            subj["groups"].append(group)
            sub = None
            card_state = None
        elif t == "group":
            group = new_group(ev["title"], "group", src=ev["src"])
            subj["groups"].append(group)
            sub = None
            card_state = None
        elif t == "item":
            if subj is None:
                sys.exit("Bullet outside a subject at body index %d" % ev["src"])
            if group is None:
                group = new_group("Core topics", "implicit", synthesized=True)
                subj["groups"].append(group)
                decisions.append("S%02d: bullets with no group heading were collected into a "
                                 "synthesized group 'Core topics'." % subj["number"])
            add_leaf(group, ev["text"], "item", sub=sub, src=ev["src"])
        elif t == "caption":
            card_state = "name"
        elif t == "table":
            hdr = ev["rows"][0]
            data = ev["rows"][1:]
            if subj is None:
                part["blocks"].append({"type": "table", "header": hdr, "rows": data})
            elif hdr == ["Language", "Major areas of use"]:
                group = new_group("Major programming languages", "table", synthesized=True,
                                  src=ev["src"])
                subj["groups"].append(group)
                decisions.append("S%02d: language table converted to synthesized group "
                                 "'Major programming languages' (one topic per row)." % subj["number"])
                for r in data:
                    add_leaf(group, r[0], "row", detail=r[1], src=ev["src"])
            elif hdr == ["Language", "Frameworks"]:
                for r in data:
                    for fw in split_list(r[1]):
                        add_leaf(group, fw, "framework", language=r[0], src=ev["src"])
            else:
                sys.exit("Unhandled table %r at body index %d" % (hdr, ev["src"]))
        elif t == "note":
            text = ev["text"]
            if card_state == "name":
                card_name, card_state = text, "desc"
                continue
            if card_state == "desc":
                container = group
                leaf = add_leaf(container, card_name, "card", sub=sub, detail=text,
                                url=ev.get("url"), src=ev["src"])
                if ev.get("url"):
                    for svc in split_list(text):
                        add_leaf(container, svc, "service", sub=sub, parent=card_name,
                                 src=ev["src"])
                card_state = None
                continue
            also = re.match(r"^Also:\s*(.+?)\.?$", text)
            if also and group is not None:
                for name in split_list(also.group(1)):
                    add_leaf(group, name, "also", sub=sub, src=ev["src"])
                continue
            nx = nxt(i)
            if subj is None:
                # part-level lines
                if part["subjects"] or part["blocks"]:
                    part["blocks"].append({"type": "note", "text": text})
                else:
                    part["blocks"].append({"type": "note", "text": text})
                continue
            if group is None and not any(g["leaves"] for g in subj["groups"]):
                # subject intro lines
                if "→" in text:
                    subj["level_range"] = text
                elif text.endswith(".") or len(text) > 70:
                    subj["description"].append(text)
                else:
                    subj["tags"].append(text)
                continue
            if nx and nx["type"] == "item":
                if text.endswith(":"):
                    title = text[:-1].strip()
                    if title == "Advanced":
                        decisions.append("S%02d: label 'Advanced:' became group 'Advanced topics'."
                                         % subj["number"])
                        title = "Advanced topics"
                    group = new_group(title, "label", src=ev["src"])
                    subj["groups"].append(group)
                    sub = None
                else:
                    sub = text
                continue
            if nx and nx["type"] == "caption":
                sub = text
                continue
            subj["closing_notes"].append(text)
    return parts, noise, decisions


# --------------------------------------------------------------------------
# Post-processing: Parts XIII-XV become groups and leaves too
# --------------------------------------------------------------------------
def build_part_groups(part):
    """Turn the table / layer blocks of Parts XIII-XV into groups of leaves."""
    groups, notes = [], []
    heading = None
    layers_pending = None
    for b in part["blocks"]:
        if b["type"] == "heading":
            heading = b["title"]
        elif b["type"] == "table":
            hdr = b["header"]
            if hdr == ["Technology category", "Examples"]:
                for row in b["rows"]:
                    g = new_group(row[0], "category")
                    for ex in split_list(row[1]):
                        add_leaf(g, ex, "technology")
                    groups.append(g)
            elif hdr == ["Stage", "What to master", "Target"]:
                g = new_group("Learning stages", "table", synthesized=True)
                for row in b["rows"]:
                    add_leaf(g, row[1], "stage", detail=row[2], stage=int(row[0]))
                groups.append(g)
            elif hdr == ["Engineering role", "Main knowledge areas"]:
                g = new_group("Engineering roles", "table", synthesized=True)
                for row in b["rows"]:
                    add_leaf(g, row[0], "role", detail=row[1])
                groups.append(g)
            else:
                sys.exit("Unhandled part table %r" % hdr)
        elif b["type"] == "note":
            txt = b["text"]
            if "·" in txt and layers_pending:
                g = new_group(smart_title(layers_pending), "layer")
                for area in [norm(x) for x in txt.split("·") if norm(x)]:
                    add_leaf(g, area, "area")
                groups.append(g)
                layers_pending = None
            elif txt.isupper() and len(txt) < 60:
                layers_pending = txt
            else:
                notes.append(txt)
    return groups, notes


def finalize(parts):
    stats = Counter()
    for part in parts:
        if part["number"] >= 13:
            part["groups"], part["notes"] = build_part_groups(part)
            part["description"] = part["notes"][:1]
            part["closing_notes"] = part["notes"][1:]
        else:
            notes = [b["text"] for b in part["blocks"] if b["type"] == "note"]
            for n in notes:
                (part["tags"] if (len(n) < 60 and not n.endswith(".")) else part["description"]).append(n)
        for s in part["subjects"]:
            for gi, g in enumerate(s["groups"], 1):
                g["number"] = gi
                g["slug"] = slugify(g["title"])
                for li, leaf in enumerate(g["leaves"], 1):
                    leaf["id"] = "%02d.%02d.%02d" % (s["number"], gi, li)
        if part["number"] >= 13:
            for gi, g in enumerate(part["groups"], 1):
                g["number"] = gi
                g["slug"] = slugify(g["title"])
                for li, leaf in enumerate(g["leaves"], 1):
                    leaf["id"] = "P%02d.%02d.%02d" % (part["number"], gi, li)
        part.pop("blocks", None)
    return parts


def compute_stats(parts):
    c = Counter()
    kinds = Counter()
    for p in parts:
        c["parts"] += 1
        for s in p["subjects"]:
            c["subjects"] += 1
            for g in s["groups"]:
                c["groups"] += 1
                for l in g["leaves"]:
                    c["leaves"] += 1
                    kinds[l["kind"]] += 1
        for g in p.get("groups", []):
            c["part_groups"] += 1
            for l in g["leaves"]:
                c["part_leaves"] += 1
                kinds["part:" + l["kind"]] += 1
    return dict(c), dict(kinds)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--docx", default="curriculum/source/Software_Engineering_Topics.docx")
    ap.add_argument("--out", default="curriculum/curriculum.json")
    a = ap.parse_args()
    parts, noise, decisions = parse(a.docx)
    parts = finalize(parts)
    stats, kinds = compute_stats(parts)
    raw = open(a.docx, "rb").read()
    doc = {
        "schema": 1,
        "source": {"file": a.docx.split("/")[-1], "bytes": len(raw),
                   "sha256": hashlib.sha256(raw).hexdigest()},
        "stats": stats,
        "leaf_kinds": kinds,
        "noise_removed": noise,
        "parser_decisions": sorted(set(decisions)),
        "parts": parts,
    }
    with open(a.out, "w", encoding="utf8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    print("parts=%(parts)d subjects=%(subjects)d groups=%(groups)d leaves=%(leaves)d "
          "part_groups=%(part_groups)d part_leaves=%(part_leaves)d" % stats)
    print("leaf kinds:", kinds)
    print("noise removed:", Counter(n["kind"] for n in noise))


if __name__ == "__main__":
    main()
