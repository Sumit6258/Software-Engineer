# Roadmap

The project is built in the phases below, in order. Status is stated honestly; "done" means the deliverable exists **and** passes `tools/validate.py`. The detailed state of every topic is in the [coverage matrix](curriculum/coverage-matrix.md) and the running log is in [PROGRESS.md](PROGRESS.md).

| Phase | Goal | Status |
|---|---|---|
| 1. Curriculum extraction and planning | Parse the whole syllabus; create the inventory, coverage matrix, prerequisite map, roadmap and progress log | **Done** |
| 2. Repository foundation | Landing page, start guide, contribution and policy files, glossary, FAQ, learning-paths overview, knowledge graph, references, all part and subject indexes | **Done**, except that the glossary and references grow with every lesson |
| 3. Foundational curriculum | Document the curriculum in learning order, starting with Part I | **In progress**: see PROGRESS.md for the exact point reached |
| 4. Subject-by-subject expansion | For each subject: chapters, lessons, diagrams, code, exercises, references, cross-links, validation, matrix update | **In progress** (Subject 1 only) |
| 5. Advanced and research material | Advanced algorithms, consensus, database internals, compilers, cryptography, deep learning, transformers, RAG, agents, HPC, quantum, formal methods | Not started |
| 6. Repository-wide audit | Re-verify the coverage matrix against the source; recheck links, diagrams, examples and references; independent technical review | Not started |

## Planned files not yet written

- **Role learning paths** in `learning-paths/`: `computer-science-beginner`, `general-software-engineer`, `software-development-engineer`, `backend-engineer`, `frontend-engineer`, `full-stack-engineer`, `android-engineer`, `ios-engineer`, `systems-engineer`, `compiler-engineer`, `cloud-engineer`, `devops-engineer`, `site-reliability-engineer`, `security-engineer`, `database-engineer`, `data-engineer`, `data-scientist`, `machine-learning-engineer`, `ai-engineer`, `game-engineer`, `graphics-engineer`, `embedded-engineer`, `iot-engineer`, `robotics-engineer`, `hpc-engineer`, `quantum-software-engineer`. The roles and their core and advanced subjects are already tabulated in [LEARNING-PATHS.md](LEARNING-PATHS.md).
- **Full project write-ups** (requirements, architecture, stages, tests, performance and security notes, extensions) for the suggested projects in [resources/practical-projects.md](resources/practical-projects.md).
- **Companion solution documents** where exercise solutions outgrow a fold inside a lesson.
- **Independent technical review** of every drafted lesson.

## Near-term order of work

1. Finish Subject 1 (Computer Fundamentals): the remaining chapters in syllabus order.
2. Subject 2 (Mathematics for Computer Science), then Subject 3 (Digital Logic and Computer Organization), Subject 4 (Operating Systems) and Subject 5 (Computer Networking), completing Part I.
3. Part II, beginning with Subject 6 (Programming Fundamentals).

The exact next file is always recorded in [PROGRESS.md](PROGRESS.md).
