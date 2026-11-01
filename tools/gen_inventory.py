#!/usr/bin/env python3
"""Generators for the curriculum-derived inventory pages."""
import re
from collections import defaultdict, Counter

from curlib import (ROOT, STATUSES, RANK, Repo, link, md_table, leaf_label, rel_link)

GEN_NOTE = ("> **Generated file.** Produced by `tools/build.py` from `curriculum/curriculum.json` "
            "(parsed from the authoritative syllabus). Do not edit by hand; change the source "
            "data or the generator instead.")


def gh_slug(text):
    s = text.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s, flags=re.U)
    return s.replace(" ", "-")


def part_heading(p):
    return "PART %s — %s" % (p["roman"], p["title"])


def part_title(r, n):
    return r.meta["parts"][str(n)]["title"]


# --------------------------------------------------------------------------
def complete_curriculum(r):
    path = ROOT / "COMPLETE-CURRICULUM.md"
    L = ["# Complete Curriculum — Source Inventory", "", GEN_NOTE, "",
         "This file is the faithful, hierarchical record of the authoritative syllabus "
         "(`curriculum/source/Software_Engineering_Topics.docx`). Every part, numbered subject "
         "area, group and topic appears here exactly once, in source order, with a stable ID.", "",
         "**How to read the IDs.** A subject topic has the ID `SS.GG.NN`: subject number, group "
         "(chapter) number within the subject, and topic number within the group. Topics in "
         "Parts XIII–XV use `PNN.GG.NN`. These IDs are the keys used by the "
         "[coverage matrix](curriculum/coverage-matrix.md).", "",
         "**Headings marked “synthesized”** were not present in the source; the parser created "
         "them so that bullets without a group heading still have a home (see the "
         "[extraction report](curriculum/extraction-report.md)).", ""]
    st = r.cur["stats"]
    L += ["| Parts | Subject areas | Groups | Subject topics | Topics in Parts XIII–XV |", "|---|---|---|---|---|",
          "| %d | %d | %d | %d | %d |" % (st["parts"], st["subjects"], st["groups"], st["leaves"], st["part_leaves"]), ""]
    for p in r.cur["parts"]:
        L += ["## " + part_heading(p), ""]
        for t in p["tags"]:
            L += ["*%s*" % t, ""]
        for dsc in p["description"]:
            L += [dsc, ""]
        for s in p["subjects"]:
            L += ["### %d. %s" % (s["number"], s["title"]), ""]
            meta = [x for x in s["tags"] + ([s["level_range"]] if s["level_range"] else []) if x]
            if meta:
                L += ["*Source tags: %s*" % " · ".join(meta), ""]
            for dsc in s["description"]:
                L += [dsc, ""]
            L += render_groups(s["groups"], 4, s["number"])
            for c in s["closing_notes"]:
                L += ["> %s" % c, ""]
        if p["number"] >= 13:
            L += render_groups(p["groups"], 3, None)
            for c in p["closing_notes"]:
                L += ["> %s" % c, ""]
    return {path: "\n".join(L).rstrip() + "\n"}


def render_groups(groups, level, subj):
    L = []
    for g in groups:
        num = ("%d.%d " % (subj, g["number"])) if subj else ""
        mark = " *(synthesized heading)*" if g["synthesized"] else ""
        L += ["#" * level + " " + num + g["title"] + mark, ""]
        prev = object()
        for leaf in g["leaves"]:
            sub = leaf.get("subgroup")
            if sub != prev:
                if sub:
                    L += ["", "**%s**" % sub, ""]
                prev = sub
            L.append("- `%s` %s" % (leaf["id"], leaf_label(leaf)))
        L.append("")
    return L


# --------------------------------------------------------------------------
def curriculum_index(r):
    path = ROOT / "curriculum/curriculum-index.md"
    st = r.cur["stats"]
    kinds = r.cur["leaf_kinds"]
    L = ["# Curriculum Index", "", GEN_NOTE, "",
         "A numeric summary of the source syllabus and where each subject lives in this repository.", "",
         "## Source totals", "",
         md_table(["Measure", "Count"], [
             ["Parts", st["parts"]], ["Numbered subject areas", st["subjects"]],
             ["Groups (chapters) inside subjects", st["groups"]],
             ["Topics inside subjects", st["leaves"]],
             ["Groups inside Parts XIII–XV", st["part_groups"]],
             ["Topics inside Parts XIII–XV", st["part_leaves"]]]), "",
         "Topic kinds inside subjects: " + ", ".join("%s = %d" % (k, v) for k, v in kinds.items() if not k.startswith("part:")) + ".", "",
         "## Topics per part", "", "```mermaid", "pie showData", "    title Syllabus topics per part (subjects only)"]
    for p in r.cur["parts"]:
        if p["subjects"]:
            n = sum(len(g["leaves"]) for s in p["subjects"] for g in s["groups"])
            L.append('    "Part %s" : %d' % (p["roman"], n))
    L += ["```", "", "## Parts", ""]
    rows = []
    for p in r.cur["parts"]:
        ng = sum(len(s["groups"]) for s in p["subjects"]) if p["subjects"] else len(p.get("groups", []))
        nt = (sum(len(g["leaves"]) for s in p["subjects"] for g in s["groups"]) if p["subjects"]
              else sum(len(g["leaves"]) for g in p.get("groups", [])))
        rows.append([link("Part %s — %s" % (p["roman"], part_title(r, p["number"])), path, r.part_index(p["number"])),
                     len(p["subjects"]) or "—", ng, nt])
    L += [md_table(["Part", "Subjects", "Groups", "Topics"], rows), "", "## Subject areas", ""]
    rows = []
    for n, s in r.subjects.items():
        rows.append([n, link(s["title"], path, r.subj_index(n)), "Part " + r.parts[r.subj_part[n]]["roman"],
                     len(s["groups"]), sum(len(g["leaves"]) for g in s["groups"]),
                     " · ".join(x for x in s["tags"] + ([s["level_range"]] if s["level_range"] else []) if x) or "—"])
    L += [md_table(["#", "Subject", "Part", "Groups", "Topics", "Source tags"], rows), ""]
    return {path: "\n".join(L)}


# --------------------------------------------------------------------------
def planned_location(r, leaf_id):
    p, s, g, l = r.leaf_index[leaf_id]
    if s is None:
        return r.part_index(p["number"])
    return r.chapter_dir(s["number"], g)


def coverage_matrix(r):
    out = {}
    dash = ROOT / "curriculum/coverage-matrix.md"
    counts = r.counts()
    total = counts["total"]
    L = ["# Coverage Matrix", "", GEN_NOTE, "",
         "The purpose of this matrix is that **no syllabus topic can be forgotten**: every topic in the "
         "source appears as one row in a per-part detail file, with the document that covers it (or the "
         "planned location if it is not written yet) and an honest status.", "",
         "## Status definitions", "",
         md_table(["Status", "Meaning"], [
             ["Not started", "No document covers this topic yet. The planned chapter directory is shown."],
             ["In progress", "A document is being written but is incomplete."],
             ["Drafted", "A full lesson exists and has passed the automated checks (links, front matter, runnable code, Mermaid). It has **not** had an independent technical review."],
             ["Reviewed", "A person other than the author has checked technical accuracy against the cited sources."],
             ["Complete", "Reviewed, and meets the completion standard below."]]), "",
         "### Completion standard", "",
         "A topic is **not** complete because its file exists. It is complete when a beginner can "
         "understand it, an intermediate learner can implement it, and an advanced engineer can "
         "understand its internal workings and trade-offs. The lesson template in "
         "[CONTRIBUTING.md](../CONTRIBUTING.md) lists the sections that make this checkable.", "",
         "## Overall (topics inside the 64 numbered subjects)", "",
         md_table(["Status", "Topics", "Share"],
                  [[s, counts[s], "%.1f%%" % (100.0 * counts[s] / total)] for s in STATUSES] +
                  [["**Total**", total, "100%"]]), "",
         "Topics in Parts XIII–XV (%d) are covered by the generated pages under `docs/13-…`, "
         "`docs/14-…` and `docs/15-…` and are tracked in their own detail files." % r.cur["stats"]["part_leaves"], "",
         "## By part", ""]
    rows = []
    for p in r.cur["parts"]:
        pn = p["number"]
        detail = ROOT / "curriculum/coverage" / ("part-%02d-%s.md" % (pn, r.meta["parts"][str(pn)]["dir"][3:]))
        if p["subjects"]:
            ids = [l["id"] for s in p["subjects"] for g in s["groups"] for l in g["leaves"]]
        else:
            ids = [l["id"] for g in p["groups"] for l in g["leaves"]]
        done = sum(1 for i in ids if RANK[r.leaf_status(i)] >= RANK["Drafted"])
        rows.append([link("Part %s — %s" % (p["roman"], part_title(r, pn)), dash, detail), len(ids), done,
                     r.part_status(pn)])
    L += [md_table(["Part", "Topics", "Drafted or better", "Part status"], rows), "", "## By subject", ""]
    rows = []
    for n, s in r.subjects.items():
        pn = r.subj_part[n]
        detail = ROOT / "curriculum/coverage" / ("part-%02d-%s.md" % (pn, r.meta["parts"][str(pn)]["dir"][3:]))
        ids = [l["id"] for g in s["groups"] for l in g["leaves"]]
        done = sum(1 for i in ids if RANK[r.leaf_status(i)] >= RANK["Drafted"])
        anchor = gh_slug("%d. %s" % (n, s["title"]))
        rows.append([n, link(s["title"], dash, detail, anchor), len(s["groups"]), len(ids), done, r.subject_status(n)])
    L += [md_table(["#", "Subject", "Groups", "Topics", "Drafted or better", "Status"], rows), ""]
    L += ["## Additions beyond the source syllabus", "",
          "Topics introduced by this repository that are **not** in the original syllabus are listed here "
          "and nowhere else. Each one is declared by the lesson that introduces it (`adds:` in its front "
          "matter). Proposed-but-unwritten additions are tracked in "
          "[proposed-additions.md](proposed-additions.md).", ""]
    if r.additions:
        rows = [[ls["subject"], "Chapter %s" % ls["chapter"], a, link(ls["title"], dash, ls["_path"]), ls["status"]]
                for ls, a in r.additions]
        L += [md_table(["Subject", "Chapter", "Added topic", "Introduced in", "Status"], rows), ""]
    else:
        L += ["_None yet._", ""]
    L += ["## Verification", "",
          "Run `python3 tools/validate.py` to re-count the source `.docx` independently of the parser and "
          "to confirm that every topic ID below appears in exactly one detail file.", ""]
    out[dash] = "\n".join(L)

    for p in r.cur["parts"]:
        pn = p["number"]
        detail = ROOT / "curriculum/coverage" / ("part-%02d-%s.md" % (pn, r.meta["parts"][str(pn)]["dir"][3:]))
        M = ["# Coverage Matrix — Part %s: %s" % (p["roman"], part_title(r, pn)), "", GEN_NOTE, "",
             "[← Back to the coverage dashboard](../coverage-matrix.md)", ""]
        if p["subjects"]:
            for s in p["subjects"]:
                n = s["number"]
                M += ["## %d. %s" % (n, s["title"]), "",
                      "Subject status: **%s** · [Subject index](%s)" % (r.subject_status(n), rel_link(detail, r.subj_index(n))), ""]
                M += matrix_groups(r, detail, s["groups"], n)
        else:
            M += ["These topics are covered by the generated page "
                  "[%s](%s)." % (r.meta["parts"][str(pn)]["dir"], rel_link(detail, r.part_index(pn))), ""]
            M += matrix_groups(r, detail, p["groups"], None)
        out[detail] = "\n".join(M)
    return out


def matrix_groups(r, detail, groups, n):
    M = []
    for g in groups:
        ids = [l["id"] for l in g["leaves"]]
        done = sum(1 for i in ids if RANK[r.leaf_status(i)] >= RANK["Drafted"])
        head = ("### %d.%d %s" % (n, g["number"], g["title"])) if n else ("### %s" % g["title"])
        M += [head, "", "%d topics · %d drafted or better" % (len(ids), done), ""]
        rows = []
        for leaf in g["leaves"]:
            cov = r.leaf_cover.get(leaf["id"], [])
            if leaf["id"].startswith("P"):
                where = link("generated page", detail, planned_location(r, leaf["id"]))
            elif cov:
                where = "<br>".join(link(c["title"], detail, c["_path"]) for c in cov)
            else:
                where = "`%s/`" % planned_location(r, leaf["id"]).relative_to(ROOT).as_posix()
            sub = leaf.get("subgroup")
            lab = leaf_label(leaf) + ((" — *%s*" % sub) if sub else "")
            rows.append(["`%s`" % leaf["id"], lab, where, r.leaf_status(leaf["id"])])
        M += [md_table(["ID", "Topic", "Documented in / planned location", "Status"], rows), ""]
    return M


# --------------------------------------------------------------------------
def extraction_report(r):
    path = ROOT / "curriculum/extraction-report.md"
    cur = r.cur
    noise = cur["noise_removed"]
    L = ["# Extraction Report", "", GEN_NOTE, "",
         "How the source syllabus was read, what was interpreted, and what was removed. "
         "Nothing is dropped silently.", "",
         "## Source file", "",
         md_table(["Property", "Value"], [["File", "`curriculum/source/%s`" % cur["source"]["file"]],
                                        ["Size", "%d bytes" % cur["source"]["bytes"]],
                                        ["SHA-256", "`%s`" % cur["source"]["sha256"]]]), "",
         "## How the hierarchy was recovered", "",
         "The `.docx` has no heading styles and every bullet has list level 0, so nesting is not stored "
         "as indentation. The hierarchy was recovered from the document's own markers:", "",
         md_table(["Source marker", "Meaning in this repository"], [
             ["Outline level 0 (`PART …`)", "Part"],
             ["Outline level 1 beginning `N.`", "Numbered subject area"],
             ["Outline level 1 without a number", "Section heading inside a part (Part XV)"],
             ["Outline level 2", "Sub-section inside a subject (treated as a group)"],
             ["Plain paragraph beginning `- `", "Group, which becomes a chapter"],
             ["Bullet paragraph", "Topic"],
             ["Plain paragraph followed by bullets", "Sub-group label (or, if it ends with `:`, a group)"],
             ["Table", "One topic per row (languages, frameworks, technology categories, stages, roles)"],
             ["Image caption followed by a name and description", "Technology card; one topic per card"]]), "",
         "## Parser decisions that add structure", "",
         "These decisions affect structure only. No topic text was changed.", ""]
    synth = [d for d in cur["parser_decisions"] if "Core topics" in d]
    other = [d for d in cur["parser_decisions"] if "Core topics" not in d]
    L += ["- **%d subjects** have bullets that appear directly under the subject heading with no group "
          "heading. They were collected into a synthesized group named “Core topics”: %s." %
          (len(synth), ", ".join(re.match(r"S(\d+)", d).group(0) for d in synth))]
    L += ["- " + d for d in other]
    L += ["", "## Source noise that was removed", "",
          "The document was exported from a chat interface and still contains web-image captions "
          "and citation chips. They are not curriculum topics.", "",
          md_table(["Kind", "Count"], sorted(Counter(n["kind"] for n in noise).items())), "",
          "<details><summary>Every removed item</summary>", "",
          md_table(["Kind", "Text", "Body element"], [[n["kind"], n["text"], n["src"]] for n in noise]), "",
          "</details>", "",
          "The removed caption links pointed at an image host and were discarded. The three official-site "
          "links (AWS, Azure, Google Cloud) were kept as the `url` of those provider cards after "
          "removing tracking parameters.", "",
          "## Claims in the source that this repository has not verified", "",
          "Three closing notes in the source refer to external organisations: NIST's AI Risk "
          "Management Framework and Generative AI Profile (subject 46), and IBM's published quantum "
          "roadmap and the post-quantum cryptography distinction (subject 54). In the source these "
          "carried citation chips whose sources were not preserved. They are retained verbatim in "
          "[COMPLETE-CURRICULUM.md](../COMPLETE-CURRICULUM.md) but must be verified against the "
          "primary documents before being repeated in a lesson.", ""]
    return {path: "\n".join(L)}


# --------------------------------------------------------------------------
STOP_SHORT = 2  # names with <= this many characters are not text-searched


def _texts(r):
    if not hasattr(r, "_texts"):
        r._texts = [(s["number"], lid, l["text"] + " " + (l.get("detail") or ""))
                    for lid, (p, s, g, l) in r.leaf_index.items() if s is not None]
        r._mention_cache = {}
    return r._texts


def mention_subjects(r, name):
    """Subject numbers whose topic text mentions `name` (exact, case-sensitive)."""
    texts = _texts(r)
    if len(name) <= STOP_SHORT:
        return set()
    if name not in r._mention_cache:
        rx = re.compile(r"(?<![\w.])" + re.escape(name) + r"(?![\w])")
        r._mention_cache[name] = {sn for sn, lid, t in texts if rx.search(t)}
    return set(r._mention_cache[name])


def technology_index(r):
    path = ROOT / "curriculum/technology-index.md"
    names = {}  # name -> {"category": set, "source": set(ids)}

    def add(name, cat=None, lid=None):
        name = name.strip()
        if not name:
            return
        e = names.setdefault(name, {"category": set(), "ids": set()})
        if cat:
            e["category"].add(cat)
        if lid:
            e["ids"].add(lid)

    for p in r.cur["parts"]:
        for g in p.get("groups", []):
            if p["number"] == 13:
                for l in g["leaves"]:
                    add(l["text"], g["title"], l["id"])
        for s in p["subjects"]:
            for g in s["groups"]:
                for l in g["leaves"]:
                    if l["kind"] in ("row", "framework", "card", "also", "service"):
                        add(l["text"], None, l["id"])
                    elif " – " in l["text"] and l["id"].startswith("15."):
                        for nm in l["text"].split(" – ")[0].split(","):
                            add(nm, None, l["id"])
    rows = []
    for name in sorted(names, key=str.lower):
        e = names[name]
        subs = mention_subjects(r, name)
        for lid in e["ids"]:
            p, s, g, l = r.leaf_index[lid]
            if s is not None:
                subs.add(s["number"])
        rows.append((name, ", ".join(sorted(e["category"])) or "—",
                     ", ".join(link(str(n), path, r.subj_index(n)) for n in sorted(subs)) or "—"))
    L = ["# Technology Index", "", GEN_NOTE, "",
         "An alphabetical index of every technology named in the source syllabus: the Part XIII ecosystem "
         "checklist, the language and framework tables, technology cards and “Also:” lists, and the "
         "database technologies in subject 15. “Subjects” lists the subject areas whose topic text "
         "mentions the name (exact-name matching, so treat it as a navigation aid, not an assertion "
         "of depth). Names of two characters or fewer are not text-searched.", "",
         "This is an index, not a list of technologies every engineer must master. See "
         "[Part XIII](../docs/13-complete-technology-ecosystem/index.md).", "",
         "%d technologies indexed." % len(rows), ""]
    cur_letter = None
    buf = []

    def flush():
        if buf:
            L.extend([md_table(["Technology", "Part XIII category", "Subjects"], buf), ""])
            buf.clear()

    for name, cat, subs in rows:
        letter = name[0].upper() if name[0].isalpha() else "#"
        if letter != cur_letter:
            flush()
            cur_letter = letter
            L += ["## " + letter, ""]
        buf.append([name, cat, subs])
    flush()
    return {path: "\n".join(L)}
