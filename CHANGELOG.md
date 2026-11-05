# Changelog

All notable changes are recorded here, following the spirit of [Keep a Changelog](https://keepachangelog.com/). The project has not made a numbered release.

## [Unreleased]

### Added

- **Curriculum extraction.** `tools/parse_syllabus.py` parses the authoritative syllabus (15 parts, 64 numbered subject areas) into `curriculum/curriculum.json`: 246 chapter groups, 3,032 topics inside subjects and 229 in Parts XIII to XV. Source noise (image captions and citation chips) was removed and logged in `curriculum/extraction-report.md`.
- **Inventory and navigation, generated from the data:** `COMPLETE-CURRICULUM.md`, `MASTER-INDEX.md`, `curriculum/curriculum-index.md`, `curriculum/coverage-matrix.md` plus 15 per-part detail files, `curriculum/prerequisite-map.md`, `curriculum/technology-index.md`, `KNOWLEDGE-GRAPH.md`, `LEARNING-PATHS.md`, 15 part indexes, 64 subject indexes and `resources/practical-projects.md`.
- **Tooling:** `tools/build.py` (regenerates every derived page, with `--check`) and `tools/validate.py` (independent re-count of the source `.docx`, coverage, front matter, markdown rules, link and anchor checks, Mermaid parsing with the Mermaid CLI, and execution of runnable code with output comparison).
- **Repository files:** `README.md`, `START-HERE.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `LICENSE` (a documented placeholder; no licence chosen), `CITATION.cff`, `GLOSSARY.md`, `FAQ.md`, `ROADMAP.md`, `REFERENCES.md`, `PROGRESS.md`, four reference pages under `resources/`, `tools/README.md` and `tools/requirements.txt`, and a GitHub Actions workflow (`.github/workflows/validate.yml`, **written but not run**).
- **Lessons for Subject 1, Computer Fundamentals** (status *Drafted*): chapter 1, *Introduction to computers* (3 lessons); chapter 2, *Number systems* (5 lessons); chapter 3, *Data representation* (7 lessons: bits, bytes and addresses; error detection and correction; character encoding and ASCII; Unicode, UTF-8 and UTF-16; integers, floats and endianness; image, audio and video encoding; data serialization); and chapter 4, *Boolean logic* (3 lessons: logic gates and truth tables; Boolean algebra and De Morgan's laws; logic simplification).
- **Additions beyond the syllabus**, declared by the lessons that introduce them: BCD and Gray code; bitwise operations and shifts; integer overflow, wraparound and saturation; fixed-point arithmetic; error detection and correction codes (parity, checksums, CRC, Hamming codes).
- **Tooling:** a lesson may have an empty `covers` list when it declares what it introduces with `adds` (an additions-only lesson); the validator enforces that one or the other is present.
- **Tooling fix:** `build.py` is now idempotent in a single pass (word counts in `PROGRESS.md` are taken from the lesson text after headers and footers are injected), which the `fresh` check had shown needed two runs after adding a lesson.
