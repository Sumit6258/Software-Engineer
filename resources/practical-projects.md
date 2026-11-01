# Practical Projects

> **Generated file.** Produced by `tools/build.py` from `curriculum/curriculum.json` (parsed from the authoritative syllabus). Do not edit by hand; change the source data or the generator instead.

Suggested projects, at least two or three per subject, taken from `curriculum/subject-meta.json`. They are *ideas*, not yet full write-ups. When a project is written up it will state the problem, requirements, required concepts, architecture, implementation stages, diagrams, tests, performance and security considerations, and possible extensions (see [ROADMAP.md](../ROADMAP.md)).

## [Part I — Computer Science Foundations](../docs/01-computer-science-foundations/index.md)

| Subject | Suggested projects |
| --- | --- |
| [1. Computer Fundamentals](../docs/01-computer-science-foundations/01-computer-fundamentals/index.md) | A base-conversion and bit-inspection toolkit in Python<br>A hex-dump utility in C<br>A simulated 8-bit ALU built from logic gates |
| [2. Mathematics for Computer Science](../docs/01-computer-science-foundations/02-mathematics-for-computer-science/index.md) | Matrix operations and Gaussian elimination from scratch<br>Monte Carlo simulations of probability puzzles |
| [3. Digital Logic and Computer Organization](../docs/01-computer-science-foundations/03-digital-logic-and-computer-organization/index.md) | A software simulator for a small CPU<br>A cache simulator that reports hit rates for access traces |
| [4. Operating Systems](../docs/01-computer-science-foundations/04-operating-systems/index.md) | A small Unix shell in C<br>A page-replacement algorithm simulator |
| [5. Computer Networking](../docs/01-computer-science-foundations/05-computer-networking/index.md) | A TCP echo server and client<br>A minimal HTTP/1.1 server built on sockets |

## [Part II — Programming and Software Development](../docs/02-programming-and-software-development/index.md)

| Subject | Suggested projects |
| --- | --- |
| [6. Programming Fundamentals](../docs/02-programming-and-software-development/06-programming-fundamentals/index.md) | A command-line task manager<br>A text-adventure engine |
| [7. Programming Paradigms](../docs/02-programming-and-software-development/07-programming-paradigms/index.md) | The same program written in three paradigms<br>A small immutable-data library in a functional style |
| [8. Programming Languages and Ecosystem](../docs/02-programming-and-software-development/08-programming-languages-and-ecosystem/index.md) | One small service implemented in two languages and compared<br>A benchmark of the same algorithm across languages |
| [9. Data Structures and Algorithms (DSA)](../docs/02-programming-and-software-development/09-data-structures-and-algorithms/index.md) | Core data structures from scratch with a test suite<br>An autocomplete service built on a trie<br>A route planner using Dijkstra's algorithm |
| [10. Compilers and Programming Language Internals](../docs/02-programming-and-software-development/10-compilers-and-language-internals/index.md) | An expression parser and evaluator<br>A bytecode virtual machine for a tiny language |

## [Part III — Professional Software Engineering](../docs/03-professional-software-engineering/index.md)

| Subject | Suggested projects |
| --- | --- |
| [11. Software Development Lifecycle (SDLC)](../docs/03-professional-software-engineering/11-software-development-lifecycle/index.md) | A requirements document and backlog for a small product<br>A retrospective on an open-source project's release history |
| [12. Software Design Principles and Architecture](../docs/03-professional-software-engineering/12-software-design-principles-and-architecture/index.md) | Refactor a legacy module towards a clean architecture<br>A decision log (ADRs) for a small system |
| [13. Version Control and Developer Workflow](../docs/03-professional-software-engineering/13-version-control-and-developer-workflow/index.md) | Contribute a documentation fix to an open-source project<br>A branching strategy for a small team |
| [14. Development Environments and Tools](../docs/03-professional-software-engineering/14-development-environments-and-tools/index.md) | A dotfiles repository and setup script<br>A Makefile or CMake build for a multi-file project |

## [Part IV — Building Software Products](../docs/04-building-software-products/index.md)

| Subject | Suggested projects |
| --- | --- |
| [15. Database Management Systems (DBMS)](../docs/04-building-software-products/15-database-management-systems/index.md) | A normalised schema with migrations for a small application<br>A key-value store with a write-ahead log |
| [16. Backend Development](../docs/04-building-software-products/16-backend-development/index.md) | A REST API with authentication and tests<br>A URL shortener with rate limiting |
| [17. Frontend Development](../docs/04-building-software-products/17-frontend-development/index.md) | A responsive, accessible portfolio page<br>A single-page application consuming a public API |
| [18. UI/UX and Human-Computer Interaction](../docs/04-building-software-products/18-ui-ux-and-human-computer-interaction/index.md) | A clickable prototype with a usability report<br>An accessibility audit of an existing website |
| [19. Mobile Application Development](../docs/04-building-software-products/19-mobile-application-development/index.md) | A notes app with offline sync<br>A small app published to a test track |
| [20. Desktop Application Development](../docs/04-building-software-products/20-desktop-application-development/index.md) | A cross-platform text utility<br>An auto-updating desktop tool |
| [21. API Integration and Messaging Systems](../docs/04-building-software-products/21-api-integration-and-messaging-systems/index.md) | A producer/consumer pipeline over a message broker<br>A webhook receiver with signature verification |

## [Part V — Distributed Systems and System Design](../docs/05-distributed-systems-and-system-design/index.md)

| Subject | Suggested projects |
| --- | --- |
| [22. Distributed Systems](../docs/05-distributed-systems-and-system-design/22-distributed-systems/index.md) | A replicated key-value store using Raft<br>A fault-injection test harness for a toy service |
| [23. System Design](../docs/05-distributed-systems-and-system-design/23-system-design/index.md) | A design document for a chat system<br>A distributed cache design with an implementation sketch |

## [Part VI — Cloud, DevOps and Infrastructure](../docs/06-cloud-devops-and-infrastructure/index.md)

| Subject | Suggested projects |
| --- | --- |
| [24. Cloud Computing](../docs/06-cloud-devops-and-infrastructure/24-cloud-computing/index.md) | A three-tier application deployed to one provider<br>A cost and architecture comparison across providers |
| [25. Containers and Container Orchestration](../docs/06-cloud-devops-and-infrastructure/25-containers-and-orchestration/index.md) | A multi-container application with Compose<br>A Kubernetes deployment with health checks and autoscaling |
| [26. DevOps Engineering](../docs/06-cloud-devops-and-infrastructure/26-devops-engineering/index.md) | A pipeline that builds, tests and deploys a container<br>Infrastructure as code for a small environment |
| [27. Site Reliability Engineering (SRE)](../docs/06-cloud-devops-and-infrastructure/27-site-reliability-engineering/index.md) | An SLO dashboard and alert policy for a demo service<br>A game-day exercise with a written post-mortem |
| [28. Observability and Monitoring](../docs/06-cloud-devops-and-infrastructure/28-observability-and-monitoring/index.md) | An OpenTelemetry-instrumented service<br>A dashboard and alert set for a demo application |
| [29. Performance Engineering](../docs/06-cloud-devops-and-infrastructure/29-performance-engineering/index.md) | A profiling report for a slow program with before-and-after measurements<br>A load test of a small API |

## [Part VII — Software Quality and Cybersecurity](../docs/07-software-quality-and-cybersecurity/index.md)

| Subject | Suggested projects |
| --- | --- |
| [30. Software Testing and Quality Assurance](../docs/07-software-quality-and-cybersecurity/30-software-testing-and-quality-assurance/index.md) | A test suite with measured coverage for an existing library<br>A property-based test for a data structure |
| [31. Cybersecurity and Software Security](../docs/07-software-quality-and-cybersecurity/31-cybersecurity-and-software-security/index.md) | A threat model for a small web application<br>A secure authentication flow with documented attack analysis |

## [Part VIII — Data Engineering, Data Science and Analytics](../docs/08-data-engineering-data-science-and-analytics/index.md)

| Subject | Suggested projects |
| --- | --- |
| [32. Data Engineering](../docs/08-data-engineering-data-science-and-analytics/32-data-engineering/index.md) | An ELT pipeline with tests and scheduling<br>A streaming aggregation over a message queue |
| [33. Data Science and Business Intelligence](../docs/08-data-engineering-data-science-and-analytics/33-data-science-and-business-intelligence/index.md) | An exploratory analysis notebook on a public dataset<br>A BI dashboard with defined metrics |

## [Part IX — Artificial Intelligence and Machine Learning](../docs/09-artificial-intelligence-and-machine-learning/index.md)

| Subject | Suggested projects |
| --- | --- |
| [34. Artificial Intelligence Fundamentals](../docs/09-artificial-intelligence-and-machine-learning/34-artificial-intelligence-fundamentals/index.md) | A search-based puzzle solver<br>A rule-based expert system |
| [35. Mathematics for Machine Learning](../docs/09-artificial-intelligence-and-machine-learning/35-mathematics-for-machine-learning/index.md) | Gradient descent from scratch for linear regression<br>PCA implemented with linear algebra primitives |
| [36. Machine Learning](../docs/09-artificial-intelligence-and-machine-learning/36-machine-learning/index.md) | Linear and logistic regression from scratch<br>An end-to-end tabular model with a proper evaluation protocol |
| [37. Deep Learning](../docs/09-artificial-intelligence-and-machine-learning/37-deep-learning/index.md) | A small neural network in NumPy<br>A convolutional classifier in a deep-learning framework |
| [38. Natural Language Processing (NLP)](../docs/09-artificial-intelligence-and-machine-learning/38-natural-language-processing/index.md) | A text classifier with an error analysis<br>A semantic search prototype using embeddings |
| [39. Computer Vision](../docs/09-artificial-intelligence-and-machine-learning/39-computer-vision/index.md) | An image classifier with data augmentation<br>An object-detection demo with an evaluation report |
| [40. Reinforcement Learning](../docs/09-artificial-intelligence-and-machine-learning/40-reinforcement-learning/index.md) | Q-learning on a grid world<br>A policy-gradient agent for a simple control task |
| [41. Generative AI](../docs/09-artificial-intelligence-and-machine-learning/41-generative-ai/index.md) | A small variational autoencoder<br>A fine-tuning experiment with a before-and-after evaluation |
| [42. Large Language Models (LLMs)](../docs/09-artificial-intelligence-and-machine-learning/42-large-language-models/index.md) | A tiny transformer language model trained on a small corpus<br>An evaluation harness comparing prompts and models |
| [43. Retrieval-Augmented Generation (RAG)](../docs/09-artificial-intelligence-and-machine-learning/43-retrieval-augmented-generation/index.md) | A RAG question-answering system over a document set with an evaluation set<br>A comparison of retrieval strategies |
| [44. AI Agents and Agentic Systems](../docs/09-artificial-intelligence-and-machine-learning/44-ai-agents-and-agentic-systems/index.md) | A tool-using agent with permissions and an audit log<br>A multi-step agent benchmark with failure analysis |
| [45. AI Engineering and MLOps](../docs/09-artificial-intelligence-and-machine-learning/45-ai-engineering-and-mlops/index.md) | A model-serving service with monitoring<br>A CI pipeline that evaluates a model before release |
| [46. Responsible AI, AI Safety and AI Governance](../docs/09-artificial-intelligence-and-machine-learning/46-responsible-ai-safety-and-governance/index.md) | A model card and risk assessment for a classifier<br>A red-teaming report for a chat application |

## [Part X — Specialized Software Engineering Domains](../docs/10-specialized-software-engineering-domains/index.md)

| Subject | Suggested projects |
| --- | --- |
| [47. Game Development](../docs/10-specialized-software-engineering-domains/47-game-development/index.md) | A 2D game with physics and collision<br>A software rasteriser |
| [48. AR, VR, MR and Spatial Computing](../docs/10-specialized-software-engineering-domains/48-ar-vr-mr-and-spatial-computing/index.md) | A WebXR scene with interaction<br>A marker-based AR demo |
| [49. Embedded Systems and Firmware Engineering](../docs/10-specialized-software-engineering-domains/49-embedded-systems-and-firmware-engineering/index.md) | A sensor-logging device on a microcontroller<br>A small RTOS-based multitasking application |
| [50. Internet of Things (IoT)](../docs/10-specialized-software-engineering-domains/50-internet-of-things/index.md) | A sensor-to-dashboard pipeline<br>A device with signed over-the-air updates |
| [51. Robotics and Autonomous Systems](../docs/10-specialized-software-engineering-domains/51-robotics-and-autonomous-systems/index.md) | A simulated differential-drive robot with obstacle avoidance<br>A PID controller tuned in simulation |
| [52. Blockchain and Web3](../docs/10-specialized-software-engineering-domains/52-blockchain-and-web3/index.md) | A small blockchain in Python<br>A tested smart contract with a written security review |
| [53. High-Performance Computing (HPC)](../docs/10-specialized-software-engineering-domains/53-high-performance-computing/index.md) | A parallel matrix multiplication with scaling measurements<br>A GPU kernel compared with a CPU baseline |
| [54. Quantum Computing](../docs/10-specialized-software-engineering-domains/54-quantum-computing/index.md) | A state-vector simulator in Python<br>Grover's algorithm on a small search space |
| [55. Edge Computing and Fog Computing](../docs/10-specialized-software-engineering-domains/55-edge-and-fog-computing/index.md) | An edge inference service with cloud fallback<br>A latency comparison of edge and cloud deployments |
| [56. Bioinformatics and Computational Biology](../docs/10-specialized-software-engineering-domains/56-bioinformatics-and-computational-biology/index.md) | Needleman-Wunsch and Smith-Waterman implementations<br>A reproducible variant-analysis workflow |
| [57. Other Specialized Domains](../docs/10-specialized-software-engineering-domains/57-other-specialized-domains/index.md) | A domain brief on the standards that govern one industry<br>A small simulated domain system with its compliance notes |

## [Part XI — AI-Assisted Software Engineering](../docs/11-ai-assisted-software-engineering/index.md)

| Subject | Suggested projects |
| --- | --- |
| [58. AI Tools Used by Modern Software Engineers](../docs/11-ai-assisted-software-engineering/58-ai-tools-for-software-engineers/index.md) | A documented AI-assisted workflow with review checkpoints<br>An evaluation of an assistant on your own codebase |

## [Part XII — Professional Engineering Practices](../docs/12-professional-engineering-practices/index.md)

| Subject | Suggested projects |
| --- | --- |
| [59. Engineering Standards and Software Quality](../docs/12-professional-engineering-practices/59-engineering-standards-and-software-quality/index.md) | A quality plan for a small project<br>A metrics dashboard with a critique of each metric |
| [60. Software Configuration and Release Management](../docs/12-professional-engineering-practices/60-software-configuration-and-release-management/index.md) | A release checklist and automated changelog<br>A feature-flagged rollout plan |
| [61. Engineering Economics](../docs/12-professional-engineering-practices/61-engineering-economics/index.md) | A cost model for a cloud architecture<br>A build-versus-buy analysis |
| [62. Software Ethics, Law and Governance](../docs/12-professional-engineering-practices/62-software-ethics-law-and-governance/index.md) | A licence-compliance audit of a project's dependencies<br>A privacy impact assessment for a small application |
| [63. Technical Communication and Leadership](../docs/12-professional-engineering-practices/63-technical-communication-and-leadership/index.md) | A design document reviewed by peers<br>A tech talk with recorded feedback |
| [64. Research and Advanced Computer Science](../docs/12-professional-engineering-practices/64-research-and-advanced-computer-science/index.md) | A reproduction of a published algorithm paper<br>A formal specification of a protocol in a model checker |
