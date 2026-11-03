# Contributing

Thank you for helping. The most valuable contributions are corrections, clearer explanations, better diagrams, additional exercises, verified references, and new lessons for topics in the [coverage matrix](curriculum/coverage-matrix.md) that are still *not started*. Please read the [Code of Conduct](CODE_OF_CONDUCT.md) first.

## What "complete" means

A topic is **not** complete because its Markdown file exists. It is complete when:

- a **beginner** can understand it without searching elsewhere for the core idea,
- an **intermediate** learner can implement it from the lesson,
- an **advanced** engineer can understand its internal workings and trade-offs, and
- someone other than the author has checked the technical claims against the cited sources.

| Status | Meaning |
|---|---|
| Not started | No document covers the topic. |
| In progress | A document exists but is incomplete. |
| Drafted | A full lesson that passes `tools/validate.py`. Not independently reviewed. |
| Reviewed | A second person checked accuracy against the sources. |
| Complete | Reviewed, and meets every point of the standard above. |

Authors set `status` to at most **Drafted**. Only a reviewer promotes a lesson.

## Where things go

Lessons live at `docs/<part>/<NN-subject>/<NN-chapter>/<NN-lesson>.md`. Chapters correspond to groups in the source syllabus ([COMPLETE-CURRICULUM.md](COMPLETE-CURRICULUM.md)); the planned directory for every chapter is shown in the subject index and in the coverage matrix. Do not invent new top-level structure. If a topic is missing from the syllabus, propose it in [curriculum/proposed-additions.md](curriculum/proposed-additions.md) and declare it with `adds:` in the lesson that introduces it.

## Lesson template

Every lesson starts with YAML front matter and an H1. The header and footer blocks are generated; do not write them by hand.

```yaml
---
title: "Positional Number Systems"        # must equal the H1
subject: 1                                  # numbered subject area
chapter: 2                                  # group number inside the subject
order: 1                                    # 1..N inside the chapter; file is NN-slug.md
difficulty: "Absolute beginner to intermediate"
time_minutes: 60
status: Drafted
reviewed: 2026-10-31                        # date the content was last checked
summary: "One sentence shown in indexes."
covers: ["01.02.01-01.02.04"]               # syllabus topic IDs (ranges allowed); may be [] only if 'adds' is set
adds: ["A topic not in the source syllabus"]  # optional
prerequisites: ["docs/.../earlier-lesson.md", "Plain text prerequisites also allowed"]
related: ["docs/.../related-lesson.md"]
---
```

After `# Title`, write these sections, in this order, and omit one only when it genuinely does not apply:

1. **What you will learn**: outcomes a reader can check.
2. **Introduction** and **intuitive understanding**: what, why, where used; analogies that are accurate.
3. **Technical foundations** and **step-by-step working**: definitions, mechanisms, worked traces, edge cases and failure modes.
4. **Diagrams**: Mermaid, only where they clarify (see below).
5. **Code**: examples that are runnable, labelled and explained.
6. **Real-world applications**, **advanced concepts**, **comparisons and trade-offs**.
7. **Common mistakes**.
8. **Exercises** at several difficulty levels, with solutions or hints in a `<details>` block.
9. **Interview and practical questions** with explanations.
10. **Further reading**, separating official specifications, textbooks, research and community resources.

## Code rules

Mark every code block with one of these HTML comments on the line before it; the validator enforces this:

| Marker | Use |
|---|---|
| `<!-- run:python -->` | A complete program. It is executed. |
| `<!-- run:c -->` | A complete C11 program, compiled with `-Wall -Wextra -pedantic`; warnings fail. |
| `<!-- expect -->` | Placed before the output block that follows a run block; compared exactly. |
| `<!-- illustrative -->` | A fragment, pseudocode or a conceptual sketch. It is **not** executed, and the text must say so. |

Never present pseudocode as runnable. Say which language and version a runnable block needs. Output that varies between runs (timing, addresses, random values) must not be placed in an `expect` block.

## Diagram rules

Use Mermaid fenced blocks with quoted labels (`A["text"]`). Prefer flowchart, sequence, state, class, entity-relationship, Gantt, timeline and mind-map diagrams. Keep each diagram small enough to read, and explain it in the text. Every diagram is parsed by the Mermaid CLI during validation.

## Mathematics

Use LaTeX (`$...$` and `$$...$$`). Define every symbol, explain the intuition first, and work a numeric example.

## Sources and accuracy

- Prefer official documentation, standards (IETF, ISO, IEEE, W3C, WHATWG, NIST), textbooks and peer-reviewed work.
- **Never invent a citation, URL, benchmark or API.** If you cannot verify it, leave it out or say it is unverified.
- Paraphrase; do not copy text from other sources.
- For fast-moving topics, state the version and the date you checked it.
- Distinguish settled theory, active research, experimental prototypes and speculation.

## Workflow

```bash
python3 tools/build.py            # regenerate headers, footers, indexes and the matrix
python3 tools/validate.py         # every check; use --only links,code to be quick
```

1. Write or edit the lesson and set `covers` accurately.
2. Run `tools/build.py`, then `tools/validate.py`. Fix everything it reports.
3. Commit the lesson **and** the regenerated files together.
4. Open a pull request describing what changed and which sources you used.

Tools need Python 3.10+, PyYAML, gcc, and (for diagrams) `@mermaid-js/mermaid-cli` with a Chromium; see [SECURITY.md](SECURITY.md) for why the validator should be run in a sandbox on untrusted contributions.

If `source` validation fails, the syllabus `.docx` changed: run `python3 tools/parse_syllabus.py`, then `tools/build.py`, and review the coverage diff.

## Licence

No licence has been chosen yet (see [LICENSE](LICENSE)). Do not contribute material you do not have the right to share.
