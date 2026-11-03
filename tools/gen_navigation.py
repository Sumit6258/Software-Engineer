#!/usr/bin/env python3
"""Generators for navigation pages, graphs and lesson headers/footers."""
import re
from pathlib import Path

from curlib import (ROOT, RANK, FM_RE, read_front_matter, link, rel_link, md_table, leaf_label)
from gen_inventory import GEN_NOTE, part_title, gh_slug, mention_subjects

CLASSDEFS = ["    classDef ns fill:#eceff1,stroke:#78909c,color:#263238;",
             "    classDef ip fill:#fff8e1,stroke:#f9a825,color:#263238;",
             "    classDef dr fill:#e8f5e9,stroke:#2e7d32,color:#1b2a1d;"]
CLASS_FOR = {"Not started": "ns", "In progress": "ip", "Drafted": "dr", "Reviewed": "dr", "Complete": "dr"}


def q(s):
    return s.replace('"', "'").replace("&", "and")


def fm_block(**kw):
    lines = ["---"]
    for k, v in kw.items():
        lines.append("%s: %s" % (k, ('"%s"' % v.replace('"', "'")) if isinstance(v, str) else v))
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def subj_label(r, n):
    return "%d. %s" % (n, r.subjects[n]["title"])


def sub_link(r, n, frm, text=None):
    return link(text or subj_label(r, n), frm, r.subj_index(n))


# --------------------------------------------------------------------------
def subject_pages(r):
    out = {}
    nums = sorted(r.subjects)
    for n in nums:
        s, m, path, pn = r.subjects[n], r.meta["subjects"][str(n)], r.subj_index(n), r.subj_part[n]
        ntop = sum(len(g["leaves"]) for g in s["groups"])
        ndone = sum(1 for g in s["groups"] for l in g["leaves"] if RANK[r.leaf_status(l["id"])] >= RANK["Drafted"])
        tags = [x for x in s["tags"] + ([s["level_range"]] if s["level_range"] else []) if x]
        L = [fm_block(title=s["title"], type="subject-index", part=pn, subject=n).rstrip("\n"), "",
             "# %d. %s" % (n, s["title"]), "",
             "> %s › %s › Subject %d" % (link("Home", path, ROOT / "README.md"),
                                          link("Part %s — %s" % (r.parts[pn]["roman"], part_title(r, pn)), path, r.part_index(pn)), n), "",
             "- **Status:** %s (%d of %d syllabus topics have a drafted lesson)" % (r.subject_status(n), ndone, ntop),
             "- **Source tags:** %s" % (" · ".join(tags) if tags else "—"),
             "- **Syllabus size:** %d chapters, %d topics" % (len(s["groups"]), ntop), "",
             "## Introduction", "", m["summary"], ""]
        for d in s["description"]:
            L += ["> " + d, ""]
        L += ["## Learning outcomes", "", "After working through this subject you should be able to:", ""]
        L += ["- " + o for o in m["outcomes"]] + [""]
        L += ["## Prerequisites", ""]
        L += (["- " + sub_link(r, p, path) for p in m["prereq"]] if m["prereq"]
              else ["None. This subject can be started without knowledge of another subject in this library."])
        L += ["", "## Beginner-to-advanced progression", "",
              "The chapters below follow the order of the source syllabus, which moves from foundational to advanced material. "
              "Colour shows documentation status (grey = not started, amber = in progress, green = drafted or better).", ""]
        if len(s["groups"]) >= 2:
            L += ["```mermaid", "flowchart %s" % ("LR" if len(s["groups"]) <= 5 else "TD")]
            chain = " --> ".join('C%d["%d. %s (%d)"]' % (g["number"], g["number"], q(g["title"]), len(g["leaves"])) for g in s["groups"])
            L += ["    " + chain]
            L += CLASSDEFS
            for g in s["groups"]:
                L.append("    class C%d %s;" % (g["number"], CLASS_FOR[r.group_status(n, g)]))
            L += ["```", ""]
        else:
            L += ["This subject has a single chapter.", ""]
        L += ["## Chapters and topics", ""]
        for g in s["groups"]:
            gs = r.group_status(n, g)
            L += ["### Chapter %d: %s" % (g["number"], g["title"]), "",
                  "%d topics · status: **%s**%s" % (len(g["leaves"]), gs, " · *heading synthesized (not in source)*" if g["synthesized"] else ""), ""]
            if r.chapter_exists(n, g):
                L += ["Chapter index: " + link("Chapter %d" % g["number"], path, r.chapter_index(n, g)), ""]
                for ls in r.lessons_in(n, g["number"]):
                    L.append("- %s — %s *(%s)*" % (link(ls["title"], path, ls["_path"]), ls["summary"], ls["status"]))
                L.append("")
            else:
                L += ["*Planned location:* `%s/`. No lessons yet." % r.chapter_dir(n, g).relative_to(ROOT).as_posix(), ""]
            L += ["<details><summary>Syllabus topics in this chapter (%d)</summary>" % len(g["leaves"]), ""]
            prev = object()
            for leaf in g["leaves"]:
                sub = leaf.get("subgroup")
                if sub != prev:
                    if sub:
                        L += ["", "**%s**" % sub, ""]
                    prev = sub
                cov = r.leaf_cover.get(leaf["id"], [])
                tail = (" — " + ", ".join(link(c["title"], path, c["_path"]) for c in cov)) if cov else " — *not started*"
                L.append("- `%s` %s%s" % (leaf["id"], leaf_label(leaf), tail))
            L += ["", "</details>", ""]
        L += ["## Recommended reading order", ""]
        L += ["%d. Chapter %d — %s" % (i, g["number"], (link(g["title"], path, r.chapter_index(n, g)) if r.chapter_exists(n, g) else g["title"]))
              for i, g in enumerate(s["groups"], 1)] + [""]
        L += ["Within a chapter, read lessons in numeric order. Pick the later chapters only when the earlier ones feel comfortable; the syllabus orders them from fundamental to advanced.", ""]
        L += ["## Related subjects", ""] + ["- " + sub_link(r, x, path) for x in m["related"]] + [""]
        L += ["## Suggested practical projects", ""] + ["- " + p for p in m["projects"]] + [""]
        L += ["*Full project write-ups (requirements, architecture, stages, tests, extensions) are planned; see [ROADMAP.md](%s).*" % rel_link(path, ROOT / "ROADMAP.md"), ""]
        nav = []
        if n > 1:
            nav.append("**Previous subject:** " + sub_link(r, n - 1, path))
        nav.append("**Up:** " + link("Part %s" % r.parts[pn]["roman"], path, r.part_index(pn)))
        if n < 64:
            nav.append("**Next subject:** " + sub_link(r, n + 1, path))
        L += ["---", "", " · ".join(nav), ""]
        out[path] = "\n".join(L)
    return out


# --------------------------------------------------------------------------
def part_pages(r):
    out = {}
    for pn in range(1, 13):
        p, path = r.parts[pn], r.part_index(pn)
        pm = r.meta["parts"][str(pn)]
        L = [fm_block(title="Part %s — %s" % (p["roman"], pm["title"]), type="part-index", part=pn).rstrip("\n"), "",
             "# Part %s — %s" % (p["roman"], pm["title"]), "",
             "> %s › Part %s" % (link("Home", path, ROOT / "README.md"), p["roman"]), "",
             "**Status:** %s" % r.part_status(pn), "", pm["scope"], ""]
        for d in p["description"]:
            L += ["> " + d, ""]
        for t in p["tags"]:
            L += ["*Source tag: %s*" % t, ""]
        rows = []
        for s in p["subjects"]:
            n = s["number"]
            rows.append([n, sub_link(r, n, path, s["title"]), r.meta["subjects"][str(n)]["summary"],
                         sum(len(g["leaves"]) for g in s["groups"]), r.subject_status(n)])
        L += ["## Subjects in this part", "", md_table(["#", "Subject", "What it covers", "Topics", "Status"], rows), ""]
        ids = {s["number"] for s in p["subjects"]}
        L += ["## How the subjects depend on each other", "",
              "Solid arrows point from a prerequisite to the subject that builds on it. Only dependencies inside this part are drawn.", "",
              "```mermaid", "flowchart LR"]
        for n in sorted(ids):
            L.append('    S%d["%d. %s"]' % (n, n, q(r.subjects[n]["title"])))
        edges = [(a, n) for n in sorted(ids) for a in r.meta["subjects"][str(n)]["prereq"] if a in ids]
        for a, b in edges:
            L.append("    S%d --> S%d" % (a, b))
        L += CLASSDEFS
        for n in sorted(ids):
            L.append("    class S%d %s;" % (n, CLASS_FOR[r.subject_status(n)]))
        L += ["```", ""]
        ext = [(n, a) for n in sorted(ids) for a in r.meta["subjects"][str(n)]["prereq"] if a not in ids]
        L += ["## What you need from other parts", ""]
        if ext:
            L += [md_table(["Subject in this part", "Prerequisite elsewhere"],
                           [[sub_link(r, n, path), sub_link(r, a, path)] for n, a in ext]), ""]
        else:
            L += ["Nothing outside this part is required.", ""]
        nav = []
        if pn > 1:
            nav.append("**Previous part:** " + link("Part %s" % r.parts[pn - 1]["roman"], path, r.part_index(pn - 1)))
        nav.append("**Up:** " + link("Master index", path, ROOT / "MASTER-INDEX.md"))
        nav.append("**Next part:** " + link("Part %s" % r.parts[pn + 1]["roman"], path, r.part_index(pn + 1)))
        L += ["---", "", " · ".join(nav), ""]
        out[path] = "\n".join(L)
    return out


# --------------------------------------------------------------------------
def tech_pages(r):
    out = {}
    # Part XIII
    p, path = r.parts[13], r.part_index(13)
    L = [fm_block(title="Part XIII — Complete Technology Ecosystem", type="part-index", part=13).rstrip("\n"), "",
         "# Part XIII — Complete Technology Ecosystem", "",
         "> %s › Part XIII" % link("Home", path, ROOT / "README.md"), "",
         r.meta["parts"]["13"]["scope"], ""]
    L += ["> " + d for d in p["description"]] + [""]
    rows = []
    for g in p["groups"]:
        subs = set()
        for l in g["leaves"]:
            subs |= mention_subjects(r, l["text"])
        rows.append([g["title"], ", ".join(l["text"] for l in g["leaves"]),
                     ", ".join(link(str(n), path, r.subj_index(n)) for n in sorted(subs)) or "—"])
    L += [md_table(["Technology category", "Examples", "Subjects whose topics mention them"], rows), ""]
    L += ["> " + c for c in p["closing_notes"]] + [""]
    L += ["The alphabetical [technology index](%s) lists every technology named anywhere in the syllabus. "
          "Subject numbers are links to the subject indexes; matching is by exact name." % rel_link(path, ROOT / "curriculum/technology-index.md"), "",
          "---", "", "**Previous part:** " + link("Part XII", path, r.part_index(12)) + " · **Next part:** " + link("Part XIV", path, r.part_index(14)), ""]
    out[path] = "\n".join(L)
    # Part XIV
    p, path = r.parts[14], r.part_index(14)
    layers = p["groups"]
    L = [fm_block(title="Part XIV — How the Entire Field Fits Together", type="part-index", part=14).rstrip("\n"), "",
         "# Part XIV — How the Entire Field Fits Together", "",
         "> %s › Part XIV" % link("Home", path, ROOT / "README.md"), "",
         r.meta["parts"]["14"]["scope"], "", "> " + p["description"][0], "",
         "## The source map", "",
         "The syllabus draws the field as seven layers. The arrows below show the order in which the source lists them; "
         "it is a simplified picture, because real dependencies cross layers in many places.", "",
         "```mermaid", "flowchart TB"]
    for i, g in enumerate(layers, 1):
        L.append('    subgraph L%d["%s"]' % (i, q(g["title"])))
        L.append("        direction LR")
        for j, l in enumerate(g["leaves"], 1):
            L.append('        A%d_%d["%s"]' % (i, j, q(l["text"])))
        L.append("    end")
    L.append("    " + " --> ".join("L%d" % i for i in range(1, len(layers) + 1)))
    L.append('    X["Professional practices, security, quality, ethics and communication"]')
    for i in range(1, len(layers) + 1):
        L.append("    X -.-> L%d" % i)
    L += ["```", "", "> " + p["closing_notes"][0], "", "## Where each layer lives in this library", ""]
    rows = []
    for g in layers:
        subs = r.meta["layers"][g["title"]]
        rows.append([g["title"], " · ".join(l["text"] for l in g["leaves"]), ", ".join(sub_link(r, n, path, str(n)) for n in subs)])
    L += [md_table(["Layer", "Areas named in the source", "Subjects"], rows), ""]
    unmapped = sorted(set(r.subjects) - set(sum(r.meta["layers"].values(), [])) - set(r.meta["cross_cutting"]))
    L += ["Subjects the simplified source map does not name, but which belong to the library: " +
          ", ".join(sub_link(r, n, path, str(n)) for n in unmapped) + " (game development, embedded systems, IoT, edge computing, bioinformatics and other specialised domains).", "",
          "Cross-cutting subjects (practices that apply in every layer): " +
          ", ".join(sub_link(r, n, path, str(n)) for n in r.meta["cross_cutting"]) + ".", "",
          "## Reading the map", "",
          "Each layer depends on the ones before it, and that dependency is concrete. A database index (subject 15) is usually a "
          "B-tree, which is a data structure from subject 9, and its performance depends on how storage and the memory hierarchy "
          "behave (subjects 3 and 4). A transformer language model (subject 42) is built from linear algebra (subjects 2 and 35) and "
          "neural-network training (subject 37). A reliable web service (subject 27) depends on networking (subject 5), "
          "distributed-systems theory (subject 22) and observability (subject 28).", "",
          "The practical consequence is that gaps in a lower layer show up as confusion in a higher one. When a topic resists "
          "understanding, look at its prerequisites in the [prerequisite map](%s) before re-reading it." % rel_link(path, ROOT / "curriculum/prerequisite-map.md"), "",
          "---", "", "**Previous part:** " + link("Part XIII", path, r.part_index(13)) + " · **Next part:** " + link("Part XV", path, r.part_index(15)), ""]
    out[path] = "\n".join(L)
    # Part XV
    p, path = r.parts[15], r.part_index(15)
    stages = p["groups"][0]["leaves"]
    roles = p["groups"][1]["leaves"]
    L = [fm_block(title="Part XV — The Practical Learning Order", type="part-index", part=15).rstrip("\n"), "",
         "# Part XV — The Practical Learning Order", "",
         "> %s › Part XV" % link("Home", path, ROOT / "README.md"), "",
         r.meta["parts"]["15"]["scope"], "", "> " + p["description"][0], "",
         "## Twelve stages", "", "```mermaid", "flowchart LR"]
    L.append("    " + " --> ".join('T%d["Stage %d: %s"]' % (l["stage"], l["stage"], q(l["detail"])) for l in stages))
    L += ["```", ""]
    rows = []
    for l in stages:
        subs = r.meta["stages"][str(l["stage"])]
        rows.append([l["stage"], l["text"], l["detail"], ", ".join(sub_link(r, n, path, str(n)) for n in subs)])
    L += [md_table(["Stage", "What to master (source)", "Target", "Subjects"], rows), "",
          "Stages overlap in practice. The subject links are this library's mapping of each stage's wording onto the numbered subject areas.", "",
          "## The difference between a generalist and a specialist", "",
          "> A software engineer is not expected to master everything in this map.", "", "The source gives these examples:", ""]
    rows = []
    for l in roles:
        rm = r.meta["roles"][l["text"]]
        rows.append([l["text"], l["detail"], ", ".join(sub_link(r, n, path, str(n)) for n in rm["core"]),
                     ", ".join(sub_link(r, n, path, str(n)) for n in rm["advanced"])])
    L += [md_table(["Engineering role", "Main knowledge areas (source)", "Core subjects", "Advanced subjects"], rows), "",
          "The role pages in [LEARNING-PATHS.md](%s) add more roles and detail." % rel_link(path, ROOT / "LEARNING-PATHS.md"), "",
          "---", "", "**Previous part:** " + link("Part XIV", path, r.part_index(14)) + " · **Up:** " + link("Master index", path, ROOT / "MASTER-INDEX.md"), ""]
    out[path] = "\n".join(L)
    return out


# --------------------------------------------------------------------------
def master_index(r):
    path = ROOT / "MASTER-INDEX.md"
    c = r.counts()
    L = ["# Master Index", "", GEN_NOTE, "",
         "Navigation across the entire library: all 15 parts, all 64 numbered subject areas, and every chapter "
         "and lesson. Chapters shown without a link are planned but not written yet.", "",
         "**Quick links:** %s · %s · %s · %s · %s" % (
             link("Start here", path, ROOT / "START-HERE.md"), link("Learning paths", path, ROOT / "LEARNING-PATHS.md"),
             link("Knowledge graph", path, ROOT / "KNOWLEDGE-GRAPH.md"), link("Coverage matrix", path, ROOT / "curriculum/coverage-matrix.md"),
             link("Progress", path, ROOT / "PROGRESS.md")), "",
         "**State:** %d of %d subject topics have a drafted lesson." % (sum(c[s] for s in ("Drafted", "Reviewed", "Complete")), c["total"]), ""]
    for p in r.cur["parts"]:
        pn = p["number"]
        L += ["## " + link("Part %s — %s" % (p["roman"], part_title(r, pn)), path, r.part_index(pn)), ""]
        if not p["subjects"]:
            L += ["- " + link(part_title(r, pn), path, r.part_index(pn)) + " (generated reference page)", ""]
            continue
        for s in p["subjects"]:
            n = s["number"]
            L.append("- **%s** — %s" % (sub_link(r, n, path), r.subject_status(n)))
            for g in s["groups"]:
                if r.chapter_exists(n, g):
                    L.append("  - %s" % link("Chapter %d: %s" % (g["number"], g["title"]), path, r.chapter_index(n, g)))
                    for ls in r.lessons_in(n, g["number"]):
                        L.append("    - %s *(%s)*" % (link(ls["title"], path, ls["_path"]), ls["status"]))
                else:
                    L.append("  - Chapter %d: %s *(planned)*" % (g["number"], g["title"]))
        L.append("")
    L += ["## Reference pages", "",
          "- " + link("Complete curriculum (source inventory)", path, ROOT / "COMPLETE-CURRICULUM.md"),
          "- " + link("Curriculum index", path, ROOT / "curriculum/curriculum-index.md"),
          "- " + link("Coverage matrix", path, ROOT / "curriculum/coverage-matrix.md"),
          "- " + link("Prerequisite map", path, ROOT / "curriculum/prerequisite-map.md"),
          "- " + link("Technology index", path, ROOT / "curriculum/technology-index.md"),
          "- " + link("Extraction report", path, ROOT / "curriculum/extraction-report.md"),
          "- " + link("Glossary", path, ROOT / "GLOSSARY.md"), "- " + link("References", path, ROOT / "REFERENCES.md"), ""]
    return {path: "\n".join(L)}


# --------------------------------------------------------------------------
def prerequisite_map(r):
    path = ROOT / "curriculum/prerequisite-map.md"
    L = ["# Prerequisite Map", "", GEN_NOTE, "",
         "Dependencies between subject areas. Prerequisite edges are authored in `curriculum/subject-meta.json`; "
         "they say what should be understood *first*, not what is merely related. The graph is checked to be acyclic.", "",
         "## Between parts", "",
         "An arrow from Part A to Part B means at least one subject in B lists a subject in A as a prerequisite.", "",
         "```mermaid", "flowchart LR"]
    for pn in range(1, 13):
        L.append('    P%d["Part %s: %s"]' % (pn, r.parts[pn]["roman"], q(part_title(r, pn))))
    edges = set()
    for n, m in r.meta["subjects"].items():
        for a in m["prereq"]:
            pa, pb = r.subj_part[a], r.subj_part[int(n)]
            if pa != pb:
                edges.add((pa, pb))
    for a, b in sorted(edges):
        L.append("    P%d --> P%d" % (a, b))
    L += CLASSDEFS
    for pn in range(1, 13):
        L.append("    class P%d %s;" % (pn, CLASS_FOR[r.part_status(pn)]))
    L += ["```", "", "## Subject by subject", ""]
    rows = []
    for n in sorted(r.subjects):
        m = r.meta["subjects"][str(n)]
        rows.append([sub_link(r, n, path), ", ".join(sub_link(r, a, path, str(a)) for a in m["prereq"]) or "—",
                     ", ".join(sub_link(r, a, path, str(a)) for a in m["related"]) or "—"])
    L += [md_table(["Subject", "Prerequisites", "Related"], rows), ""]
    return {path: "\n".join(L)}


# --------------------------------------------------------------------------
def knowledge_graph(r):
    path = ROOT / "KNOWLEDGE-GRAPH.md"
    assigned = {}
    for i, (name, subs) in enumerate(r.meta["layers"].items(), 1):
        for n in subs:
            if n not in assigned:
                assigned[n] = i
    other = sorted(set(r.subjects) - set(assigned) - set(r.meta["cross_cutting"]))
    L = ["# Knowledge Graph", "", GEN_NOTE, "",
         "How the 64 subject areas group into the seven layers of the source's Part XIV map. Each subject is drawn once, "
         "in the first layer that names it. Colour is documentation status (grey, amber, green as in the subject indexes).", "",
         "```mermaid", "flowchart TB"]
    for i, name in enumerate(r.meta["layers"], 1):
        L.append('    subgraph L%d["%s"]' % (i, q(name)))
        L.append("        direction LR")
        for n in sorted(k for k, v in assigned.items() if v == i):
            L.append('        S%d["%d %s"]' % (n, n, q(r.subjects[n]["title"].split(" (")[0])))
        L.append("    end")
    L.append('    subgraph LO["Other specialised domains"]')
    L.append("        direction LR")
    for n in other:
        L.append('        S%d["%d %s"]' % (n, n, q(r.subjects[n]["title"].split(" (")[0])))
    L += ["    end", '    subgraph LX["Cross-cutting professional practice"]', "        direction LR"]
    for n in r.meta["cross_cutting"]:
        L.append('        S%d["%d %s"]' % (n, n, q(r.subjects[n]["title"].split(" (")[0])))
    L += ["    end", "    " + " --> ".join("L%d" % i for i in range(1, len(r.meta["layers"]) + 1)),
          "    L7 --> LO", "    LX -.-> L1"]
    L += CLASSDEFS
    for n in sorted(r.subjects):
        L.append("    class S%d %s;" % (n, CLASS_FOR[r.subject_status(n)]))
    L += ["```", "",
          "Arrows between layers show the simplified order used by the source; for the real subject-level dependencies "
          "see the [prerequisite map](%s). A subject listed in two layers of the source (for example architecture and databases "
          "appear in more than one) is drawn in its first layer only." % rel_link(path, ROOT / "curriculum/prerequisite-map.md"), "",
          "## Layer membership", ""]
    rows = []
    for name, subs in r.meta["layers"].items():
        rows.append([name, ", ".join(sub_link(r, n, path, str(n)) for n in subs)])
    rows.append(["Other specialised domains", ", ".join(sub_link(r, n, path, str(n)) for n in other)])
    rows.append(["Cross-cutting professional practice", ", ".join(sub_link(r, n, path, str(n)) for n in r.meta["cross_cutting"])])
    L += [md_table(["Layer", "Subjects"], rows), "",
          "See also: [Part XIV](%s), the narrative version of this map." % rel_link(path, r.part_index(14)), ""]
    return {path: "\n".join(L)}


# --------------------------------------------------------------------------
def learning_paths(r):
    path = ROOT / "LEARNING-PATHS.md"
    common = [1, 2, 4, 5, 6, 9, 13]
    L = ["# Learning Paths", "", GEN_NOTE, "",
         "The library is comprehensive, but nobody needs all of it. This page separates the **common foundation** from "
         "**role-specific depth**, following the source's own warning against trying to learn all 64 areas at once.", "",
         "## 1. Common foundation", "",
         "Almost every path starts here: " + ", ".join(sub_link(r, n, path) for n in common) + ".", "",
         "## 2. The twelve-stage progression", "",
         "From Part XV of the source. See the [full table with targets](%s)." % rel_link(path, r.part_index(15)), "", "```mermaid", "flowchart LR"]
    stages = r.parts[15]["groups"][0]["leaves"]
    L.append("    " + " --> ".join('T%d["Stage %d"]' % (l["stage"], l["stage"]) for l in stages))
    L += ["```", ""]
    rows = [[l["stage"], l["text"], l["detail"], ", ".join(sub_link(r, n, path, str(n)) for n in r.meta["stages"][str(l["stage"])])] for l in stages]
    L += [md_table(["Stage", "What to master", "Target", "Subjects"], rows), "", "## 3. Role paths", "",
          "Core subjects are the ones to master for the role; advanced subjects are the depth that distinguishes a senior specialist. "
          "Roles marked *added* are not in the source's list and were added by this library.", ""]
    src_roles = {l["text"]: l["detail"] for l in r.parts[15]["groups"][1]["leaves"]}
    rows = []
    for name, rm in r.meta["roles"].items():
        rows.append([name, ("source: " + src_roles[name]) if name in src_roles else "*added*",
                     ", ".join(sub_link(r, n, path, str(n)) for n in rm["core"]), ", ".join(sub_link(r, n, path, str(n)) for n in rm["advanced"])])
    L += [md_table(["Role", "Main knowledge areas", "Core subjects", "Advanced subjects"], rows), "",
          "## 4. Detailed role pages (planned)", "",
          "Each role page will list: required foundations, essential intermediate subjects, role-specific technologies, advanced subjects, "
          "practical exercises, portfolio projects, production knowledge and optional research specialisations. They will link to the main "
          "documentation rather than duplicate it. None are written yet; the planned files are listed in [ROADMAP.md](%s)." % rel_link(path, ROOT / "ROADMAP.md"), ""]
    return {path: "\n".join(L)}


# --------------------------------------------------------------------------
def practical_projects(r):
    path = ROOT / "resources/practical-projects.md"
    L = ["# Practical Projects", "", GEN_NOTE, "",
         "Suggested projects, at least two or three per subject, taken from `curriculum/subject-meta.json`. They are *ideas*, not yet full write-ups. "
         "When a project is written up it will state the problem, requirements, required concepts, architecture, implementation stages, "
         "diagrams, tests, performance and security considerations, and possible extensions (see [ROADMAP.md](%s))." % rel_link(path, ROOT / "ROADMAP.md"), ""]
    for pn in range(1, 13):
        L += ["## " + link("Part %s — %s" % (r.parts[pn]["roman"], part_title(r, pn)), path, r.part_index(pn)), ""]
        rows = [[sub_link(r, s["number"], path), "<br>".join(r.meta["subjects"][str(s["number"])]["projects"])] for s in r.parts[pn]["subjects"]]
        L += [md_table(["Subject", "Suggested projects"], rows), ""]
    return {path: "\n".join(L)}


# --------------------------------------------------------------------------
HEADER_RE = re.compile(r"<!-- BEGIN HEADER.*?<!-- END HEADER -->\n?", re.S)
FOOTER_RE = re.compile(r"<!-- BEGIN FOOTER.*?<!-- END FOOTER -->\n?", re.S)
LIST_RE = re.compile(r"(<!-- BEGIN LESSONS.*?-->\n).*?(<!-- END LESSONS -->)", re.S)


def title_of(r, rootpath):
    p = ROOT / rootpath
    if not p.exists():
        return None
    fm, body = read_front_matter(p)
    if fm and fm.get("title"):
        return fm["title"]
    m = re.search(r"^# (.+)$", body, re.M)
    return m.group(1) if m else None


def breadcrumb(r, file, n, chapter_no=None, chapter_is_self=False):
    pn = r.subj_part[n]
    g = r.subjects[n]["groups"][chapter_no - 1] if chapter_no else None
    crumbs = [link("Home", file, ROOT / "README.md"),
              link("Part %s — %s" % (r.parts[pn]["roman"], part_title(r, pn)), file, r.part_index(pn)),
              sub_link(r, n, file)]
    if g:
        txt = "Chapter %d: %s" % (g["number"], g["title"])
        crumbs.append(txt if chapter_is_self else link(txt, file, r.chapter_index(n, g)))
    return "> " + " › ".join(crumbs)


def lesson_header(r, ls):
    f, n = ls["_path"], ls["subject"]
    pre = []
    for pr in ls.get("prerequisites") or []:
        t = title_of(r, pr) if str(pr).endswith(".md") else None
        pre.append(link(t, f, ROOT / pr) if t else str(pr))
    cov = []
    for lid in ls["_covers"]:
        leaf = r.leaf_index[lid][3]
        cov.append("`%s` %s" % (lid, leaf_label(leaf)))
    status = ls["status"]
    note = {"Drafted": "passes the automated checks; awaiting independent technical review",
            "In progress": "incomplete", "Reviewed": "independently reviewed", "Complete": "reviewed and complete"}[status]
    return "\n".join([
        "<!-- BEGIN HEADER (generated by tools/build.py from the front matter; edit the front matter, not this block) -->",
        breadcrumb(r, f, n, ls["chapter"]), "",
        "- **Difficulty:** %s" % ls["difficulty"],
        "- **Estimated time:** about %d minutes" % ls["time_minutes"],
        "- **Prerequisites:** %s" % (" · ".join(pre) if pre else "none beyond the earlier lessons in this chapter"),
        "- **Syllabus topics covered:** %s" % (" · ".join(cov) if cov else
                                              "none from the source syllabus. This lesson introduces an addition: " + "; ".join(ls.get("adds") or [])),
        "- **Status:** %s (%s). Last reviewed %s." % (status, note, ls["reviewed"]),
        "<!-- END HEADER -->"])


def lesson_footer(r, ls, prev, nxt):
    f, n = ls["_path"], ls["subject"]
    g = r.subjects[n]["groups"][ls["chapter"] - 1]
    L = ["<!-- BEGIN FOOTER (generated by tools/build.py) -->", "---", ""]
    rel = []
    for x in ls.get("related") or []:
        t = title_of(r, x)
        if t:
            rel.append("- " + link(t, f, ROOT / x))
    if rel:
        L += ["## Related topics", ""] + rel + [""]
    nav = []
    nav.append("**Previous:** " + (link(prev["title"], f, prev["_path"]) if prev else link("subject index", f, r.subj_index(n))))
    nav.append("**Up:** " + link("Chapter %d: %s" % (g["number"], g["title"]), f, r.chapter_index(n, g)))
    nav.append("**Next:** " + (link(nxt["title"], f, nxt["_path"]) if nxt else link("subject index", f, r.subj_index(n))))
    L += ["## Navigation", "", " · ".join(nav), "<!-- END FOOTER -->"]
    return "\n".join(L)


def inject_lessons(r):
    out = {}
    by_subject = {}
    for ls in r.lessons:
        by_subject.setdefault(ls["subject"], []).append(ls)
    for n, group in by_subject.items():
        for i, ls in enumerate(group):
            prev = group[i - 1] if i > 0 else None
            nxt = group[i + 1] if i + 1 < len(group) else None
            text = ls["_path"].read_text("utf8")
            m = FM_RE.match(text)
            head, body = text[:m.end()], text[m.end():]
            body = FOOTER_RE.sub("", HEADER_RE.sub("", body))
            h1 = re.search(r"^# .+\n", body, re.M)
            if not h1:
                r.problems.append("%s: no H1 title" % ls["_path"].relative_to(ROOT))
                continue
            rest = body[h1.end():].lstrip("\n")
            body = body[:h1.end()] + "\n" + lesson_header(r, ls) + "\n\n" + rest.rstrip("\n") + "\n\n" + lesson_footer(r, ls, prev, nxt) + "\n"
            out[ls["_path"]] = head + body
    return out


def inject_chapter_indexes(r):
    out = {}
    for n, s in r.subjects.items():
        for g in s["groups"]:
            f = r.chapter_index(n, g)
            if not f.exists():
                continue
            text = f.read_text("utf8")
            m = FM_RE.match(text)
            head, body = text[:m.end()], text[m.end():]
            body = FOOTER_RE.sub("", HEADER_RE.sub("", body))
            h1 = re.search(r"^# .+\n", body, re.M)
            lessons = r.lessons_in(n, g["number"])
            rows = [[i, link(l["title"], f, l["_path"]), l["difficulty"], "%d min" % l["time_minutes"], l["status"], l["summary"]]
                    for i, l in enumerate(lessons, 1)]
            tops = []
            prev = object()
            for leaf in g["leaves"]:
                sub = leaf.get("subgroup")
                if sub != prev:
                    if sub:
                        tops += ["", "**%s**" % sub, ""]
                    prev = sub
                cov = r.leaf_cover.get(leaf["id"], [])
                tops.append("- `%s` %s — %s" % (leaf["id"], leaf_label(leaf),
                            ", ".join(link(c["title"], f, c["_path"]) for c in cov) if cov else "*not started*"))
            block = ["<!-- BEGIN LESSONS (generated by tools/build.py) -->",
                     "## Lessons in this chapter", "",
                     md_table(["#", "Lesson", "Level", "Time", "Status", "Summary"], rows) if rows else "_No lessons yet._", "",
                     "## Syllabus topics in this chapter", ""] + tops + ["", "<!-- END LESSONS -->"]
            if "<!-- BEGIN LESSONS" in body:
                body = LIST_RE.sub(lambda mm: "\n".join(block), body)
            else:
                body = body.rstrip("\n") + "\n\n" + "\n".join(block) + "\n"
            hdr = ["<!-- BEGIN HEADER (generated by tools/build.py) -->", breadcrumb(r, f, n, g["number"], True),
                   "", "- **Status:** %s · %d syllabus topics" % (r.group_status(n, g), len(g["leaves"])), "<!-- END HEADER -->"]
            h1 = re.search(r"^# .+\n", body, re.M)
            body = body[:h1.end()] + "\n" + "\n".join(hdr) + "\n\n" + body[h1.end():].lstrip("\n")
            chapters = [x for x in s["groups"] if r.chapter_exists(n, x)]
            idx = [x["number"] for x in chapters].index(g["number"])
            nav = []
            nav.append("**Previous chapter:** " + (link("Chapter %d: %s" % (chapters[idx - 1]["number"], chapters[idx - 1]["title"]), f, r.chapter_index(n, chapters[idx - 1])) if idx > 0 else link("subject index", f, r.subj_index(n))))
            nav.append("**Up:** " + link("subject index", f, r.subj_index(n)))
            nav.append("**Next chapter:** " + (link("Chapter %d: %s" % (chapters[idx + 1]["number"], chapters[idx + 1]["title"]), f, r.chapter_index(n, chapters[idx + 1])) if idx + 1 < len(chapters) else "not written yet"))
            body = body.rstrip("\n") + "\n\n<!-- BEGIN FOOTER (generated by tools/build.py) -->\n---\n\n" + " · ".join(nav) + "\n<!-- END FOOTER -->\n"
            out[f] = head + body
    return out


def update_block(path, name, content):
    text = path.read_text("utf8")
    rx = re.compile(r"(<!-- BEGIN %s[^>]*-->\n).*?(<!-- END %s -->)" % (name, name), re.S)
    if not rx.search(text):
        raise SystemExit("%s: missing <!-- BEGIN %s --> ... <!-- END %s --> markers" % (path, name, name))
    return rx.sub(lambda m: m.group(1) + content.rstrip("\n") + "\n" + m.group(2), text)
