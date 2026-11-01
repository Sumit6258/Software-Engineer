# Complete Curriculum — Source Inventory

> **Generated file.** Produced by `tools/build.py` from `curriculum/curriculum.json` (parsed from the authoritative syllabus). Do not edit by hand; change the source data or the generator instead.

This file is the faithful, hierarchical record of the authoritative syllabus (`curriculum/source/Software_Engineering_Topics.docx`). Every part, numbered subject area, group and topic appears here exactly once, in source order, with a stable ID.

**How to read the IDs.** A subject topic has the ID `SS.GG.NN`: subject number, group (chapter) number within the subject, and topic number within the group. Topics in Parts XIII–XV use `PNN.GG.NN`. These IDs are the keys used by the [coverage matrix](curriculum/coverage-matrix.md).

**Headings marked “synthesized”** were not present in the source; the parser created them so that bullets without a group heading still have a home (see the [extraction report](curriculum/extraction-report.md)).

| Parts | Subject areas | Groups | Subject topics | Topics in Parts XIII–XV |
|---|---|---|---|---|
| 15 | 64 | 246 | 3032 | 229 |

## PART I — COMPUTER SCIENCE FOUNDATIONS

These are the foundations underneath almost everything a software engineer does.

### 1. Computer Fundamentals

*Source tags: Start here · Beginner → Advanced*

#### 1.1 Introduction to computers

- `01.01.01` What is a computer?
- `01.01.02` Hardware vs software
- `01.01.03` Input, processing, output and storage
- `01.01.04` Types of computers
- `01.01.05` Desktop, laptop, workstation, server, supercomputer
- `01.01.06` Embedded computers
- `01.01.07` Client vs server
- `01.01.08` Local vs remote computing

#### 1.2 Number systems

- `01.02.01` Decimal
- `01.02.02` Binary
- `01.02.03` Octal
- `01.02.04` Hexadecimal
- `01.02.05` Number-system conversions
- `01.02.06` Binary arithmetic
- `01.02.07` Signed and unsigned numbers
- `01.02.08` Two's complement
- `01.02.09` Floating-point representation
- `01.02.10` IEEE 754

#### 1.3 Data representation

- `01.03.01` Bits and bytes
- `01.03.02` Nibbles, words and memory addresses
- `01.03.03` Character encoding
- `01.03.04` ASCII
- `01.03.05` Unicode
- `01.03.06` UTF-8, UTF-16
- `01.03.07` Integer and floating-point representation
- `01.03.08` Endianness
- `01.03.09` Image, audio and video encoding
- `01.03.10` Data serialization

#### 1.4 Boolean logic

- `01.04.01` AND, OR, NOT
- `01.04.02` NAND, NOR, XOR, XNOR
- `01.04.03` Truth tables
- `01.04.04` Boolean algebra
- `01.04.05` De Morgan's laws
- `01.04.06` Logic simplification

#### 1.5 Computer components

- `01.05.01` CPU
- `01.05.02` GPU
- `01.05.03` RAM
- `01.05.04` ROM
- `01.05.05` Cache
- `01.05.06` SSD and HDD
- `01.05.07` Motherboard
- `01.05.08` Power supply
- `01.05.09` Network interface card
- `01.05.10` Peripheral devices

#### 1.6 How computers execute instructions

- `01.06.01` Fetch-decode-execute cycle
- `01.06.02` Machine instructions
- `01.06.03` Registers
- `01.06.04` Memory access
- `01.06.05` Interrupts
- `01.06.06` Instruction execution
- `01.06.07` System calls

### 2. Mathematics for Computer Science

*Source tags: Beginner → Research level*

Mathematics is particularly important for algorithms, graphics, AI, cryptography, scientific computing and quantum computing.

#### 2.1 Basic mathematics

- `02.01.01` Arithmetic
- `02.01.02` Fractions
- `02.01.03` Percentages
- `02.01.04` Ratios
- `02.01.05` Exponents
- `02.01.06` Logarithms
- `02.01.07` Algebra
- `02.01.08` Equations and inequalities
- `02.01.09` Functions

#### 2.2 Discrete mathematics

- `02.02.01` Sets
- `02.02.02` Relations
- `02.02.03` Functions
- `02.02.04` Sequences
- `02.02.05` Permutations
- `02.02.06` Combinations
- `02.02.07` Mathematical induction
- `02.02.08` Recurrence relations
- `02.02.09` Pigeonhole principle
- `02.02.10` Inclusion-exclusion principle

#### 2.3 Mathematical logic

- `02.03.01` Propositional logic
- `02.03.02` Predicate logic
- `02.03.03` First-order logic
- `02.03.04` Quantifiers
- `02.03.05` Logical equivalence
- `02.03.06` Proof techniques
- `02.03.07` Direct proof
- `02.03.08` Contradiction
- `02.03.09` Contrapositive
- `02.03.10` Formal reasoning

#### 2.4 Graph theory

- `02.04.01` Vertices and edges
- `02.04.02` Directed and undirected graphs
- `02.04.03` Weighted graphs
- `02.04.04` Trees
- `02.04.05` Cycles
- `02.04.06` Connected components
- `02.04.07` Bipartite graphs
- `02.04.08` Graph coloring
- `02.04.09` Planar graphs
- `02.04.10` Eulerian and Hamiltonian paths
- `02.04.11` Network flow

#### 2.5 Linear algebra

- `02.05.01` Scalars
- `02.05.02` Vectors
- `02.05.03` Matrices
- `02.05.04` Matrix multiplication
- `02.05.05` Matrix transformations
- `02.05.06` Determinants
- `02.05.07` Eigenvalues
- `02.05.08` Eigenvectors
- `02.05.09` Vector spaces
- `02.05.10` Linear independence
- `02.05.11` Singular value decomposition
- `02.05.12` Tensor algebra

#### 2.6 Probability

- `02.06.01` Random variables
- `02.06.02` Probability distributions
- `02.06.03` Conditional probability
- `02.06.04` Bayes' theorem
- `02.06.05` Independent events
- `02.06.06` Expected values
- `02.06.07` Variance
- `02.06.08` Standard deviation
- `02.06.09` Markov chains
- `02.06.10` Bayesian inference

#### 2.7 Statistics

- `02.07.01` Descriptive statistics
- `02.07.02` Inferential statistics
- `02.07.03` Sampling
- `02.07.04` Hypothesis testing
- `02.07.05` Confidence intervals
- `02.07.06` Correlation
- `02.07.07` Regression
- `02.07.08` ANOVA
- `02.07.09` Statistical significance
- `02.07.10` Experimental design
- `02.07.11` Bayesian statistics

#### 2.8 Calculus

- `02.08.01` Limits
- `02.08.02` Continuity
- `02.08.03` Differentiation
- `02.08.04` Integration
- `02.08.05` Partial derivatives
- `02.08.06` Multivariable calculus
- `02.08.07` Gradients
- `02.08.08` Gradient descent
- `02.08.09` Vector calculus

#### 2.9 Numerical mathematics

- `02.09.01` Numerical approximation
- `02.09.02` Numerical integration
- `02.09.03` Numerical differentiation
- `02.09.04` Error analysis
- `02.09.05` Floating-point errors
- `02.09.06` Numerical optimization
- `02.09.07` Iterative algorithms

#### 2.10 Advanced mathematics

- `02.10.01` Information theory
- `02.10.02` Entropy
- `02.10.03` Combinatorial optimization
- `02.10.04` Operations research
- `02.10.05` Game theory
- `02.10.06` Number theory
- `02.10.07` Abstract algebra
- `02.10.08` Group theory
- `02.10.09` Differential equations
- `02.10.10` Convex optimization
- `02.10.11` Stochastic processes
- `02.10.12` Computational geometry

### 3. Digital Logic and Computer Organization

#### 3.1 Digital electronics

- `03.01.01` Logic gates
- `03.01.02` Combinational circuits
- `03.01.03` Sequential circuits
- `03.01.04` Flip-flops
- `03.01.05` Registers
- `03.01.06` Multiplexers
- `03.01.07` Decoders
- `03.01.08` Encoders
- `03.01.09` Counters
- `03.01.10` State machines

#### 3.2 Computer organization

- `03.02.01` CPU architecture
- `03.02.02` ALU
- `03.02.03` Control unit
- `03.02.04` Registers
- `03.02.05` Instruction sets
- `03.02.06` Memory hierarchy
- `03.02.07` Cache architecture
- `03.02.08` Bus architecture
- `03.02.09` Interrupt handling

#### 3.3 Computer architecture

- `03.03.01` Von Neumann architecture
- `03.03.02` Harvard architecture
- `03.03.03` RISC
- `03.03.04` CISC
- `03.03.05` ARM
- `03.03.06` x86
- `03.03.07` RISC-V
- `03.03.08` Instruction set architecture
- `03.03.09` Pipelining
- `03.03.10` Superscalar processors
- `03.03.11` Out-of-order execution
- `03.03.12` Branch prediction
- `03.03.13` Speculative execution
- `03.03.14` Multicore processors
- `03.03.15` NUMA architecture

#### 3.4 Advanced hardware architecture

- `03.04.01` GPU architecture
- `03.04.02` TPU and AI accelerators
- `03.04.03` FPGA
- `03.04.04` ASIC
- `03.04.05` System-on-Chip
- `03.04.06` Heterogeneous computing
- `03.04.07` Neuromorphic computing
- `03.04.08` Chiplet architecture
- `03.04.09` Memory-centric computing

### 4. Operating Systems

#### 4.1 Operating system fundamentals

- `04.01.01` What is an operating system?
- `04.01.02` Kernel and user space
- `04.01.03` System calls
- `04.01.04` Boot process
- `04.01.05` OS architecture
- `04.01.06` Monolithic kernels
- `04.01.07` Microkernels
- `04.01.08` Hybrid kernels

#### 4.2 Process management

- `04.02.01` Processes
- `04.02.02` Threads
- `04.02.03` Process states
- `04.02.04` Context switching
- `04.02.05` CPU scheduling
- `04.02.06` Process synchronization
- `04.02.07` Inter-process communication
- `04.02.08` Signals

#### 4.3 Memory management

- `04.03.01` RAM management
- `04.03.02` Virtual memory
- `04.03.03` Paging
- `04.03.04` Segmentation
- `04.03.05` Page tables
- `04.03.06` Memory allocation
- `04.03.07` Heap and stack
- `04.03.08` Memory protection
- `04.03.09` Memory leaks
- `04.03.10` Garbage collection

#### 4.4 Concurrency

- `04.04.01` Multithreading
- `04.04.02` Locks
- `04.04.03` Mutexes
- `04.04.04` Semaphores
- `04.04.05` Monitors
- `04.04.06` Condition variables
- `04.04.07` Race conditions
- `04.04.08` Deadlocks
- `04.04.09` Starvation
- `04.04.10` Lock-free algorithms
- `04.04.11` Atomic operations

#### 4.5 File systems

- `04.05.01` Files and directories
- `04.05.02` File permissions
- `04.05.03` Inodes
- `04.05.04` Journaling
- `04.05.05` File system caching
- `04.05.06` File system allocation
- `04.05.07` Virtual file systems
- `04.05.08` Distributed file systems

#### 4.6 Storage and device management

- `04.06.01` Device drivers
- `04.06.02` I/O management
- `04.06.03` Interrupts
- `04.06.04` DMA
- `04.06.05` Block devices
- `04.06.06` Character devices
- `04.06.07` Disk scheduling

#### 4.7 Advanced OS concepts

- `04.07.01` Kernel programming
- `04.07.02` Kernel modules
- `04.07.03` Virtualization
- `04.07.04` Hypervisors
- `04.07.05` Containers
- `04.07.06` Real-time operating systems
- `04.07.07` Embedded operating systems
- `04.07.08` eBPF
- `04.07.09` Linux internals
- `04.07.10` Android internals
- `04.07.11` Distributed operating systems

#### 4.8 Operating system families

- `04.08.01` Linux
- `04.08.02` Windows
- `04.08.03` macOS
- `04.08.04` Android
- `04.08.05` iOS
- `04.08.06` FreeBSD
- `04.08.07` OpenBSD
- `04.08.08` Unix
- `04.08.09` QNX
- `04.08.10` FreeRTOS
- `04.08.11` Zephyr

### 5. Computer Networking

#### 5.1 Networking fundamentals

- `05.01.01` What is a computer network?
- `05.01.02` LAN, WAN, MAN and PAN
- `05.01.03` Network topologies
- `05.01.04` Network devices
- `05.01.05` Client-server communication
- `05.01.06` Peer-to-peer networking
- `05.01.07` Bandwidth
- `05.01.08` Latency
- `05.01.09` Throughput
- `05.01.10` Packet switching
- `05.01.11` Circuit switching

#### 5.2 Networking models

- `05.02.01` OSI model
- `05.02.02` TCP/IP model
- `05.02.03` Encapsulation
- `05.02.04` Decapsulation
- `05.02.05` Network layers
- `05.02.06` Protocol stacks

#### 5.3 IP networking

- `05.03.01` IPv4
- `05.03.02` IPv6
- `05.03.03` IP addressing
- `05.03.04` Subnetting
- `05.03.05` CIDR
- `05.03.06` Public and private IP
- `05.03.07` NAT
- `05.03.08` Routing
- `05.03.09` Static routing
- `05.03.10` Dynamic routing
- `05.03.11` BGP
- `05.03.12` OSPF
- `05.03.13` ICMP
- `05.03.14` ARP

#### 5.4 Transport protocols

- `05.04.01` TCP
- `05.04.02` UDP
- `05.04.03` QUIC
- `05.04.04` Three-way handshake
- `05.04.05` Flow control
- `05.04.06` Congestion control
- `05.04.07` Retransmission
- `05.04.08` Connection management

#### 5.5 Application protocols

- `05.05.01` HTTP
- `05.05.02` HTTPS
- `05.05.03` HTTP/1.1
- `05.05.04` HTTP/2
- `05.05.05` HTTP/3
- `05.05.06` DNS
- `05.05.07` DHCP
- `05.05.08` FTP
- `05.05.09` SFTP
- `05.05.10` SMTP
- `05.05.11` IMAP
- `05.05.12` POP3
- `05.05.13` SSH
- `05.05.14` WebSocket
- `05.05.15` MQTT
- `05.05.16` AMQP
- `05.05.17` SNMP

#### 5.6 Network infrastructure

- `05.06.01` Routers
- `05.06.02` Switches
- `05.06.03` Firewalls
- `05.06.04` Proxies
- `05.06.05` Reverse proxies
- `05.06.06` Load balancers
- `05.06.07` Gateways
- `05.06.08` CDNs
- `05.06.09` VPNs
- `05.06.10` Network address translation

#### 5.7 Wireless networking

- `05.07.01` Wi-Fi
- `05.07.02` Bluetooth
- `05.07.03` NFC
- `05.07.04` Zigbee
- `05.07.05` Cellular networking
- `05.07.06` 4G
- `05.07.07` 5G
- `05.07.08` 6G research
- `05.07.09` Satellite networking
- `05.07.10` Software-defined networking

#### 5.8 Advanced networking

- `05.08.01` Network virtualization
- `05.08.02` Network function virtualization
- `05.08.03` Software-defined networking
- `05.08.04` Content delivery
- `05.08.05` Anycast
- `05.08.06` Multicast
- `05.08.07` Zero-trust networking
- `05.08.08` Network observability
- `05.08.09` Network automation
- `05.08.10` High-performance networking

## PART II — PROGRAMMING AND SOFTWARE DEVELOPMENT

### 6. Programming Fundamentals

*Source tags: Essential for every software developer*

#### 6.1 First programming concepts

- `06.01.01` What is programming?
- `06.01.02` Source code
- `06.01.03` Machine code
- `06.01.04` Compilers and interpreters
- `06.01.05` Variables
- `06.01.06` Constants
- `06.01.07` Data types
- `06.01.08` Operators
- `06.01.09` Expressions
- `06.01.10` Input and output

#### 6.2 Control flow

- `06.02.01` If-else
- `06.02.02` Switch
- `06.02.03` Loops
- `06.02.04` For
- `06.02.05` While
- `06.02.06` Do-while
- `06.02.07` Break and continue
- `06.02.08` Nested loops
- `06.02.09` Pattern programming

#### 6.3 Functions

- `06.03.01` Function declaration
- `06.03.02` Function calling
- `06.03.03` Parameters
- `06.03.04` Return values
- `06.03.05` Scope
- `06.03.06` Local and global variables
- `06.03.07` Pass by value
- `06.03.08` Pass by reference
- `06.03.09` Recursion
- `06.03.10` Function overloading
- `06.03.11` Higher-order functions
- `06.03.12` Closures

#### 6.4 Data structures in programming

- `06.04.01` Arrays
- `06.04.02` Strings
- `06.04.03` Structures
- `06.04.04` Unions
- `06.04.05` Enumerations
- `06.04.06` Pointers
- `06.04.07` References
- `06.04.08` Dynamic memory
- `06.04.09` Collections

#### 6.5 Error handling

- `06.05.01` Syntax errors
- `06.05.02` Runtime errors
- `06.05.03` Logical errors
- `06.05.04` Exceptions
- `06.05.05` Exception propagation
- `06.05.06` Custom exceptions
- `06.05.07` Assertions
- `06.05.08` Error codes
- `06.05.09` Defensive programming

#### 6.6 Advanced programming concepts

- `06.06.01` Memory management
- `06.06.02` Stack and heap
- `06.06.03` Pointers and references
- `06.06.04` Generators
- `06.06.05` Iterators
- `06.06.06` Coroutines
- `06.06.07` Asynchronous programming
- `06.06.08` Event-driven programming
- `06.06.09` Reactive programming
- `06.06.10` Metaprogramming
- `06.06.11` Reflection
- `06.06.12` Dependency injection

### 7. Programming Paradigms

You should understand the different ways programs can be designed.

#### 7.1 Core topics *(synthesized heading)*

- `07.01.01` Imperative programming
- `07.01.02` Procedural programming
- `07.01.03` Structured programming
- `07.01.04` Object-oriented programming
- `07.01.05` Functional programming
- `07.01.06` Declarative programming
- `07.01.07` Logic programming
- `07.01.08` Event-driven programming
- `07.01.09` Reactive programming
- `07.01.10` Concurrent programming
- `07.01.11` Parallel programming
- `07.01.12` Aspect-oriented programming
- `07.01.13` Data-oriented programming
- `07.01.14` Component-based programming
- `07.01.15` Message-driven programming
- `07.01.16` Actor model
- `07.01.17` Flow-based programming
- `07.01.18` Constraint-based programming
- `07.01.19` Domain-specific languages

#### 7.2 Object-oriented programming

- `07.02.01` Classes and objects
- `07.02.02` Constructors
- `07.02.03` Destructors
- `07.02.04` Encapsulation
- `07.02.05` Abstraction
- `07.02.06` Inheritance
- `07.02.07` Polymorphism
- `07.02.08` Method overriding
- `07.02.09` Method overloading
- `07.02.10` Interfaces
- `07.02.11` Abstract classes
- `07.02.12` Composition
- `07.02.13` Aggregation
- `07.02.14` Association
- `07.02.15` SOLID principles
- `07.02.16` Dependency inversion
- `07.02.17` Object lifecycle
- `07.02.18` Advanced object modeling

#### 7.3 Functional programming

- `07.03.01` Pure functions
- `07.03.02` Immutability
- `07.03.03` First-class functions
- `07.03.04` Higher-order functions
- `07.03.05` Lambda expressions
- `07.03.06` Closures
- `07.03.07` Map, filter and reduce
- `07.03.08` Function composition
- `07.03.09` Currying
- `07.03.10` Partial application
- `07.03.11` Recursion
- `07.03.12` Pattern matching
- `07.03.13` Monads
- `07.03.14` Functors
- `07.03.15` Lazy evaluation
- `07.03.16` Referential transparency

### 8. Programming Languages and Ecosystem

A software engineer does not need to master every programming language. However, you should understand the major language families and know which types of problems they solve.

#### 8.1 Major programming languages *(synthesized heading)*

- `08.01.01` C — Systems programming, embedded
- `08.01.02` C++ — Systems, games, performance
- `08.01.03` Java — Enterprise, backend, Android
- `08.01.04` Python — Backend, AI, automation, data science
- `08.01.05` JavaScript — Web development, full-stack
- `08.01.06` TypeScript — Large-scale web development
- `08.01.07` C# — .NET, enterprise, game development
- `08.01.08` Go — Cloud, infrastructure, backend
- `08.01.09` Rust — Systems, security, performance
- `08.01.10` Kotlin — Android, backend
- `08.01.11` Swift — iOS, macOS
- `08.01.12` PHP — Web backend
- `08.01.13` Ruby — Web applications
- `08.01.14` Scala — Distributed data, functional systems
- `08.01.15` R — Statistics and data science
- `08.01.16` Julia — Scientific computing
- `08.01.17` Dart — Cross-platform mobile
- `08.01.18` Elixir — Concurrent distributed systems
- `08.01.19` Erlang — Fault-tolerant distributed systems
- `08.01.20` Haskell — Functional programming
- `08.01.21` OCaml — Functional systems and compilers
- `08.01.22` F# — Functional .NET development
- `08.01.23` Clojure — Functional JVM development
- `08.01.24` Lua — Scripting and game engines
- `08.01.25` SQL — Database programming
- `08.01.26` Bash — Unix automation
- `08.01.27` PowerShell — Windows and infrastructure automation
- `08.01.28` Assembly — Low-level programming
- `08.01.29` Solidity — Blockchain smart contracts
- `08.01.30` Verilog — Digital hardware design
- `08.01.31` VHDL — Digital hardware design
- `08.01.32` MATLAB — Engineering and numerical computing
- `08.01.33` Fortran — Scientific and high-performance computing
- `08.01.34` COBOL — Legacy enterprise systems

#### 8.2 Language-specific advanced topics

- `08.02.01` Runtime environments
- `08.02.02` Virtual machines
- `08.02.03` Garbage collection
- `08.02.04` Memory safety
- `08.02.05` Type inference
- `08.02.06` Static and dynamic typing
- `08.02.07` Strong and weak typing
- `08.02.08` Generic programming
- `08.02.09` Template metaprogramming
- `08.02.10` Language interoperability
- `08.02.11` ABI
- `08.02.12` FFI
- `08.02.13` Reflection
- `08.02.14` Language runtimes
- `08.02.15` Compiler optimization
- `08.02.16` Runtime performance

### 9. Data Structures and Algorithms (DSA)

*Source tags: Core interview and problem-solving subject*

This area should be studied from simple structures to advanced algorithmic techniques.

#### 9.1 Basic complexity analysis

- `09.01.01` Time complexity
- `09.01.02` Space complexity
- `09.01.03` Big O
- `09.01.04` Big Omega
- `09.01.05` Big Theta
- `09.01.06` Best, average and worst cases
- `09.01.07` Amortized analysis
- `09.01.08` Recurrence relations

#### 9.2 Basic data structures

- `09.02.01` Arrays
- `09.02.02` Strings
- `09.02.03` Linked lists
- `09.02.04` Singly linked lists
- `09.02.05` Doubly linked lists
- `09.02.06` Circular linked lists
- `09.02.07` Stacks
- `09.02.08` Queues
- `09.02.09` Deques
- `09.02.10` Hash tables
- `09.02.11` Hash maps
- `09.02.12` Sets

#### 9.3 Trees

- `09.03.01` Binary trees
- `09.03.02` Binary search trees
- `09.03.03` AVL trees
- `09.03.04` Red-black trees
- `09.03.05` B-trees
- `09.03.06` B+ trees
- `09.03.07` Segment trees
- `09.03.08` Fenwick trees
- `09.03.09` Tries
- `09.03.10` Suffix trees
- `09.03.11` Suffix arrays
- `09.03.12` Merkle trees

#### 9.4 Heaps and priority structures

- `09.04.01` Min heap
- `09.04.02` Max heap
- `09.04.03` Binary heap
- `09.04.04` Fibonacci heap
- `09.04.05` Priority queues

#### 9.5 Graph data structures

- `09.05.01` Adjacency matrix
- `09.05.02` Adjacency list
- `09.05.03` Directed graphs
- `09.05.04` Undirected graphs
- `09.05.05` Weighted graphs
- `09.05.06` Disjoint set union
- `09.05.07` Union-find

#### 9.6 Basic algorithms

- `09.06.01` Linear search
- `09.06.02` Binary search
- `09.06.03` Bubble sort
- `09.06.04` Selection sort
- `09.06.05` Insertion sort
- `09.06.06` Merge sort
- `09.06.07` Quick sort
- `09.06.08` Heap sort
- `09.06.09` Counting sort
- `09.06.10` Radix sort
- `09.06.11` Bucket sort

#### 9.7 Algorithmic techniques

- `09.07.01` Two pointers
- `09.07.02` Sliding window
- `09.07.03` Prefix sums
- `09.07.04` Difference arrays
- `09.07.05` Fast and slow pointers
- `09.07.06` Recursion
- `09.07.07` Backtracking
- `09.07.08` Divide and conquer
- `09.07.09` Greedy algorithms
- `09.07.10` Dynamic programming
- `09.07.11` Memoization
- `09.07.12` Tabulation
- `09.07.13` Bit manipulation
- `09.07.14` Meet-in-the-middle
- `09.07.15` Binary search on answer

#### 9.8 Graph algorithms

- `09.08.01` BFS
- `09.08.02` DFS
- `09.08.03` Topological sorting
- `09.08.04` Dijkstra's algorithm
- `09.08.05` Bellman-Ford
- `09.08.06` Floyd-Warshall
- `09.08.07` Prim's algorithm
- `09.08.08` Kruskal's algorithm
- `09.08.09` A*
- `09.08.10` Strongly connected components
- `09.08.11` Tarjan's algorithm
- `09.08.12` Kosaraju's algorithm
- `09.08.13` Minimum spanning trees
- `09.08.14` Maximum flow
- `09.08.15` Minimum cut

#### 9.9 Advanced algorithms

- `09.09.01` String matching
- `09.09.02` KMP
- `09.09.03` Rabin-Karp
- `09.09.04` Z algorithm
- `09.09.05` Manacher's algorithm
- `09.09.06` Computational geometry
- `09.09.07` Convex hull
- `09.09.08` Number-theoretic algorithms
- `09.09.09` Randomized algorithms
- `09.09.10` Approximation algorithms
- `09.09.11` Online algorithms
- `09.09.12` Streaming algorithms
- `09.09.13` External-memory algorithms
- `09.09.14` Cache-efficient algorithms
- `09.09.15` Parallel algorithms
- `09.09.16` Distributed algorithms

#### 9.10 Algorithm theory

- `09.10.01` P and NP
- `09.10.02` NP-completeness
- `09.10.03` NP-hardness
- `09.10.04` Complexity classes
- `09.10.05` Decidability
- `09.10.06` Computability theory
- `09.10.07` Reductions
- `09.10.08` Lower bounds
- `09.10.09` Quantum algorithms

### 10. Compilers and Programming Language Internals

#### 10.1 Basic concepts

- `10.01.01` Source code
- `10.01.02` Compilation
- `10.01.03` Interpretation
- `10.01.04` Machine code
- `10.01.05` Bytecode
- `10.01.06` Assembly

#### 10.2 Compiler architecture

- `10.02.01` Lexical analysis
- `10.02.02` Tokens
- `10.02.03` Parsing
- `10.02.04` Context-free grammars
- `10.02.05` Abstract syntax trees
- `10.02.06` Semantic analysis
- `10.02.07` Type checking
- `10.02.08` Intermediate representation
- `10.02.09` Code generation
- `10.02.10` Linking
- `10.02.11` Loading

#### 10.3 Advanced compiler concepts

- `10.03.01` Compiler optimization
- `10.03.02` Control-flow graphs
- `10.03.03` Data-flow analysis
- `10.03.04` Static single assignment
- `10.03.05` Register allocation
- `10.03.06` Instruction scheduling
- `10.03.07` Just-in-time compilation
- `10.03.08` Ahead-of-time compilation
- `10.03.09` LLVM
- `10.03.10` Garbage collector implementation
- `10.03.11` Virtual machine design
- `10.03.12` Interpreter design
- `10.03.13` Formal language theory
- `10.03.14` Program verification

## PART III — PROFESSIONAL SOFTWARE ENGINEERING

### 11. Software Development Lifecycle (SDLC)

A professional engineer needs to understand the entire life of a software product, not just writing code.

#### 11.1 Project initiation

- `11.01.01` Problem identification
- `11.01.02` Business objectives
- `11.01.03` Feasibility analysis
- `11.01.04` Stakeholder identification
- `11.01.05` Product vision
- `11.01.06` Scope definition

#### 11.2 Requirements engineering

- `11.02.01` Functional requirements
- `11.02.02` Non-functional requirements
- `11.02.03` User requirements
- `11.02.04` Business requirements
- `11.02.05` System requirements
- `11.02.06` Technical requirements
- `11.02.07` Constraints
- `11.02.08` User stories
- `11.02.09` Acceptance criteria
- `11.02.10` Use cases
- `11.02.11` Requirements elicitation
- `11.02.12` Requirements prioritization
- `11.02.13` Requirements validation
- `11.02.14` Requirements traceability

#### 11.3 Software development models

- `11.03.01` Waterfall
- `11.03.02` V-model
- `11.03.03` Iterative development
- `11.03.04` Incremental development
- `11.03.05` Spiral model
- `11.03.06` Prototype model
- `11.03.07` RAD
- `11.03.08` Agile
- `11.03.09` Scrum
- `11.03.10` Kanban
- `11.03.11` Extreme Programming
- `11.03.12` Lean software development
- `11.03.13` DevOps
- `11.03.14` Continuous delivery

#### 11.4 Software project management

- `11.04.01` Project planning
- `11.04.02` Task estimation
- `11.04.03` Work breakdown structure
- `11.04.04` Milestones
- `11.04.05` Sprint planning
- `11.04.06` Backlog management
- `11.04.07` Risk management
- `11.04.08` Resource management
- `11.04.09` Project scheduling
- `11.04.10` Dependencies
- `11.04.11` Delivery tracking
- `11.04.12` Project reporting

#### 11.5 Software maintenance

- `11.05.01` Corrective maintenance
- `11.05.02` Adaptive maintenance
- `11.05.03` Perfective maintenance
- `11.05.04` Preventive maintenance
- `11.05.05` Refactoring
- `11.05.06` Technical debt
- `11.05.07` Legacy modernization
- `11.05.08` Version upgrades
- `11.05.09` Deprecation
- `11.05.10` Software retirement

### 12. Software Design Principles and Architecture

*Source tags: Essential for senior engineers*

#### 12.1 Fundamental design principles

- `12.01.01` DRY
- `12.01.02` KISS
- `12.01.03` YAGNI
- `12.01.04` Separation of concerns
- `12.01.05` Modularity
- `12.01.06` Cohesion
- `12.01.07` Coupling
- `12.01.08` Encapsulation
- `12.01.09` Abstraction
- `12.01.10` Reusability
- `12.01.11` Extensibility
- `12.01.12` Maintainability

#### 12.2 SOLID principles

- `12.02.01` Single Responsibility
- `12.02.02` Open/Closed
- `12.02.03` Liskov Substitution
- `12.02.04` Interface Segregation
- `12.02.05` Dependency Inversion

#### 12.3 Object-oriented design

- `12.03.01` GRASP
- `12.03.02` Composition over inheritance
- `12.03.03` Dependency injection
- `12.03.04` Inversion of control
- `12.03.05` Interface-based design
- `12.03.06` Domain modeling

#### 12.4 Gang of Four design patterns


**Creational patterns**

- `12.04.01` Singleton
- `12.04.02` Factory Method
- `12.04.03` Abstract Factory
- `12.04.04` Builder
- `12.04.05` Prototype

**Structural patterns**

- `12.04.06` Adapter
- `12.04.07` Bridge
- `12.04.08` Composite
- `12.04.09` Decorator
- `12.04.10` Facade
- `12.04.11` Flyweight
- `12.04.12` Proxy

**Behavioral patterns**

- `12.04.13` Chain of Responsibility
- `12.04.14` Command
- `12.04.15` Interpreter
- `12.04.16` Iterator
- `12.04.17` Mediator
- `12.04.18` Memento
- `12.04.19` Observer
- `12.04.20` State
- `12.04.21` Strategy
- `12.04.22` Template Method
- `12.04.23` Visitor

#### 12.5 Architectural patterns

- `12.05.01` Layered architecture
- `12.05.02` Three-tier architecture
- `12.05.03` N-tier architecture
- `12.05.04` Client-server architecture
- `12.05.05` MVC
- `12.05.06` MVP
- `12.05.07` MVVM
- `12.05.08` Clean architecture
- `12.05.09` Hexagonal architecture
- `12.05.10` Onion architecture
- `12.05.11` Modular monolith
- `12.05.12` Microservices
- `12.05.13` Service-oriented architecture
- `12.05.14` Event-driven architecture
- `12.05.15` Serverless architecture
- `12.05.16` Plugin architecture
- `12.05.17` Pipe-and-filter architecture
- `12.05.18` Peer-to-peer architecture

#### 12.6 Advanced architectural concepts

- `12.06.01` Domain-driven design
- `12.06.02` Bounded contexts
- `12.06.03` Aggregates
- `12.06.04` Entities and value objects
- `12.06.05` CQRS
- `12.06.06` Event sourcing
- `12.06.07` Saga pattern
- `12.06.08` Transactional outbox
- `12.06.09` Strangler pattern
- `12.06.10` Backend for Frontend
- `12.06.11` API gateway pattern
- `12.06.12` Service discovery
- `12.06.13` Sidecar pattern
- `12.06.14` Ambassador pattern
- `12.06.15` Anti-corruption layer
- `12.06.16` Distributed system architecture
- `12.06.17` Multi-tenant architecture
- `12.06.18` Multi-region architecture

#### 12.7 System quality attributes

- `12.07.01` Scalability
- `12.07.02` Performance
- `12.07.03` Availability
- `12.07.04` Reliability
- `12.07.05` Resilience
- `12.07.06` Fault tolerance
- `12.07.07` Security
- `12.07.08` Maintainability
- `12.07.09` Portability
- `12.07.10` Interoperability
- `12.07.11` Usability
- `12.07.12` Accessibility
- `12.07.13` Observability
- `12.07.14` Testability
- `12.07.15` Recoverability

#### 12.8 Architecture documentation

- `12.08.01` UML
- `12.08.02` Class diagrams
- `12.08.03` Sequence diagrams
- `12.08.04` Activity diagrams
- `12.08.05` Component diagrams
- `12.08.06` Deployment diagrams
- `12.08.07` State diagrams
- `12.08.08` C4 model
- `12.08.09` Architecture decision records
- `12.08.10` Threat models
- `12.08.11` Data-flow diagrams

### 13. Version Control and Developer Workflow

#### 13.1 Core topics *(synthesized heading)*

- `13.01.01` Git fundamentals
- `13.01.02` GitHub
- `13.01.03` GitLab
- `13.01.04` Bitbucket
- `13.01.05` Repository management
- `13.01.06` Git init
- `13.01.07` Clone
- `13.01.08` Add
- `13.01.09` Commit
- `13.01.10` Push
- `13.01.11` Pull
- `13.01.12` Fetch
- `13.01.13` Merge
- `13.01.14` Rebase
- `13.01.15` Cherry-pick
- `13.01.16` Stashing
- `13.01.17` Reset and revert
- `13.01.18` Branch management
- `13.01.19` Pull requests
- `13.01.20` Merge requests
- `13.01.21` Code reviews
- `13.01.22` Code owners
- `13.01.23` Protected branches
- `13.01.24` Tags
- `13.01.25` Releases
- `13.01.26` Semantic versioning
- `13.01.27` Git workflows
- `13.01.28` Trunk-based development
- `13.01.29` GitFlow
- `13.01.30` Monorepos
- `13.01.31` Polyrepos
- `13.01.32` Submodules
- `13.01.33` Git hooks
- `13.01.34` Commit signing
- `13.01.35` Release management

### 14. Development Environments and Tools

#### 14.1 Command-line tools

- `14.01.01` Terminal
- `14.01.02` Shell
- `14.01.03` Bash
- `14.01.04` Zsh
- `14.01.05` PowerShell
- `14.01.06` Linux commands
- `14.01.07` Pipes and redirection
- `14.01.08` Environment variables
- `14.01.09` Shell scripting

#### 14.2 Code editors and IDEs

- `14.02.01` VS Code
- `14.02.02` IntelliJ IDEA
- `14.02.03` PyCharm
- `14.02.04` Eclipse
- `14.02.05` Visual Studio
- `14.02.06` Android Studio
- `14.02.07` Xcode
- `14.02.08` Vim
- `14.02.09` Neovim
- `14.02.10` Emacs

#### 14.3 Development utilities

- `14.03.01` Debuggers
- `14.03.02` Profilers
- `14.03.03` Linters
- `14.03.04` Formatters
- `14.03.05` Static analyzers
- `14.03.06` Package managers
- `14.03.07` Build tools
- `14.03.08` Dependency managers
- `14.03.09` API clients
- `14.03.10` Database clients
- `14.03.11` Local development containers

#### 14.4 Build systems

- `14.04.01` Make
- `14.04.02` CMake
- `14.04.03` Maven
- `14.04.04` Gradle
- `14.04.05` npm
- `14.04.06` pnpm
- `14.04.07` Yarn
- `14.04.08` Webpack
- `14.04.09` Vite
- `14.04.10` Bazel
- `14.04.11` Buck
- `14.04.12` Ninja
- `14.04.13` MSBuild

#### 14.5 Documentation

- `14.05.01` README
- `14.05.02` API documentation
- `14.05.03` Technical specifications
- `14.05.04` Architecture documentation
- `14.05.05` OpenAPI/Swagger
- `14.05.06` AsyncAPI
- `14.05.07` Markdown
- `14.05.08` Documentation generators
- `14.05.09` Runbooks
- `14.05.10` ADRs

## PART IV — BUILDING SOFTWARE PRODUCTS

### 15. Database Management Systems (DBMS)

*Source tags: Essential*

#### 15.1 Database fundamentals

- `15.01.01` What is a database?
- `15.01.02` DBMS
- `15.01.03` RDBMS
- `15.01.04` Tables
- `15.01.05` Rows
- `15.01.06` Columns
- `15.01.07` Schemas
- `15.01.08` Primary keys
- `15.01.09` Foreign keys
- `15.01.10` Constraints
- `15.01.11` Relationships
- `15.01.12` Data types

#### 15.2 SQL

- `15.02.01` SELECT
- `15.02.02` INSERT
- `15.02.03` UPDATE
- `15.02.04` DELETE
- `15.02.05` WHERE
- `15.02.06` ORDER BY
- `15.02.07` GROUP BY
- `15.02.08` HAVING
- `15.02.09` JOINs
- `15.02.10` Subqueries
- `15.02.11` Common table expressions
- `15.02.12` Window functions
- `15.02.13` Stored procedures
- `15.02.14` Functions
- `15.02.15` Triggers
- `15.02.16` Views
- `15.02.17` Materialized views

#### 15.3 Database design

- `15.03.01` Entity-relationship diagrams
- `15.03.02` Entity relationships
- `15.03.03` Data modeling
- `15.03.04` Normalization
- `15.03.05` 1NF
- `15.03.06` 2NF
- `15.03.07` 3NF
- `15.03.08` BCNF
- `15.03.09` Denormalization
- `15.03.10` Schema migrations
- `15.03.11` Referential integrity

#### 15.4 Database internals

- `15.04.01` Query parsing
- `15.04.02` Query optimization
- `15.04.03` Query execution plans
- `15.04.04` Indexing
- `15.04.05` B-tree indexes
- `15.04.06` Hash indexes
- `15.04.07` Composite indexes
- `15.04.08` Database statistics
- `15.04.09` Buffer pools
- `15.04.10` Write-ahead logs
- `15.04.11` MVCC
- `15.04.12` Storage engines

#### 15.5 Transactions

- `15.05.01` ACID
- `15.05.02` Isolation levels
- `15.05.03` Dirty reads
- `15.05.04` Non-repeatable reads
- `15.05.05` Phantom reads
- `15.05.06` Locks
- `15.05.07` Deadlocks
- `15.05.08` Optimistic locking
- `15.05.09` Pessimistic locking
- `15.05.10` Transaction management

#### 15.6 Database scaling

- `15.06.01` Replication
- `15.06.02` Primary-replica architecture
- `15.06.03` Read replicas
- `15.06.04` Sharding
- `15.06.05` Partitioning
- `15.06.06` Horizontal scaling
- `15.06.07` Vertical scaling
- `15.06.08` Distributed transactions
- `15.06.09` Strong consistency
- `15.06.10` Eventual consistency

#### 15.7 Database technologies


**Relational databases**

- `15.07.01` **PostgreSQL** — Advanced relational database
- `15.07.02` **MySQL** — Relational database
- `15.07.03` MariaDB
- `15.07.04` SQLite
- `15.07.05` Oracle Database
- `15.07.06` Microsoft SQL Server
- `15.07.07` CockroachDB
- `15.07.08` YugabyteDB

**NoSQL databases**

- `15.07.09` MongoDB – document database
- `15.07.10` Redis – in-memory key-value store
- `15.07.11` Cassandra – wide-column database
- `15.07.12` DynamoDB – managed key-value/document database
- `15.07.13` Couchbase – document and key-value database
- `15.07.14` Neo4j – graph database
- `15.07.15` ScyllaDB – wide-column database
- `15.07.16` HBase – distributed wide-column database

**Specialized databases**

- `15.07.17` Elasticsearch, OpenSearch – search engines
- `15.07.18` ClickHouse, Apache Druid – analytical databases
- `15.07.19` InfluxDB, TimescaleDB – time-series databases
- `15.07.20` Snowflake, BigQuery, Redshift – cloud data warehouses
- `15.07.21` Milvus, Weaviate, Qdrant, Pinecone – vector databases
- `15.07.22` DuckDB – analytical database engine
- `15.07.23` Neo4j – graph data

#### 15.8 Advanced database topics

- `15.08.01` Distributed SQL
- `15.08.02` NewSQL
- `15.08.03` Vector indexing
- `15.08.04` Full-text search
- `15.08.05` Geospatial databases
- `15.08.06` Time-series storage
- `15.08.07` Graph traversal
- `15.08.08` Database encryption
- `15.08.09` Backup and point-in-time recovery
- `15.08.10` Database high availability
- `15.08.11` Multi-region data systems

### 16. Backend Development

*Source tags: Major software engineering specialization*

#### 16.1 Backend fundamentals

- `16.01.01` Client-server architecture
- `16.01.02` Request-response lifecycle
- `16.01.03` Server-side programming
- `16.01.04` Business logic
- `16.01.05` Routing
- `16.01.06` Controllers
- `16.01.07` Services
- `16.01.08` Repositories
- `16.01.09` Middleware
- `16.01.10` Configuration management

#### 16.2 API development

- `16.02.01` REST
- `16.02.02` RESTful design
- `16.02.03` HTTP methods
- `16.02.04` Status codes
- `16.02.05` Headers
- `16.02.06` Request and response bodies
- `16.02.07` JSON
- `16.02.08` XML
- `16.02.09` API versioning
- `16.02.10` Pagination
- `16.02.11` Filtering
- `16.02.12` Sorting
- `16.02.13` Rate limiting
- `16.02.14` Idempotency

#### 16.3 API technologies

- `16.03.01` REST API
- `16.03.02` GraphQL
- `16.03.03` gRPC
- `16.03.04` SOAP
- `16.03.05` WebSocket
- `16.03.06` Server-sent events
- `16.03.07` Webhooks
- `16.03.08` JSON-RPC
- `16.03.09` Protocol Buffers
- `16.03.10` OpenAPI
- `16.03.11` AsyncAPI

#### 16.4 Authentication and authorization

- `16.04.01` Authentication
- `16.04.02` Authorization
- `16.04.03` Sessions
- `16.04.04` Cookies
- `16.04.05` Password hashing
- `16.04.06` JWT
- `16.04.07` OAuth 2.0
- `16.04.08` OpenID Connect
- `16.04.09` SAML
- `16.04.10` RBAC
- `16.04.11` ABAC
- `16.04.12` Multi-factor authentication
- `16.04.13` Single sign-on

#### 16.5 Advanced backend concepts

- `16.05.01` Background tasks
- `16.05.02` Job queues
- `16.05.03` Caching
- `16.05.04` Distributed locking
- `16.05.05` Message brokers
- `16.05.06` Event-driven processing
- `16.05.07` Async processing
- `16.05.08` Concurrency
- `16.05.09` Database transactions
- `16.05.10` Distributed transactions
- `16.05.11` Rate limiting
- `16.05.12` Circuit breakers
- `16.05.13` Retry policies
- `16.05.14` Bulkheads
- `16.05.15` Multi-tenancy
- `16.05.16` File processing
- `16.05.17` Payment integrations
- `16.05.18` Email services
- `16.05.19` Notification systems

#### 16.6 Backend frameworks

- `16.06.01` Spring Boot *(Java)*
- `16.06.02` Jakarta EE *(Java)*
- `16.06.03` Quarkus *(Java)*
- `16.06.04` Micronaut *(Java)*
- `16.06.05` Django *(Python)*
- `16.06.06` FastAPI *(Python)*
- `16.06.07` Flask *(Python)*
- `16.06.08` Litestar *(Python)*
- `16.06.09` Node.js *(JavaScript)*
- `16.06.10` Express *(JavaScript)*
- `16.06.11` NestJS *(JavaScript)*
- `16.06.12` Fastify *(JavaScript)*
- `16.06.13` Gin *(Go)*
- `16.06.14` Echo *(Go)*
- `16.06.15` Fiber *(Go)*
- `16.06.16` Chi *(Go)*
- `16.06.17` ASP.NET Core *(C#)*
- `16.06.18` Laravel *(PHP)*
- `16.06.19` Symfony *(PHP)*
- `16.06.20` Rails *(Ruby)*
- `16.06.21` Sinatra *(Ruby)*
- `16.06.22` Axum *(Rust)*
- `16.06.23` Actix Web *(Rust)*
- `16.06.24` Rocket *(Rust)*
- `16.06.25` Ktor *(Kotlin)*
- `16.06.26` Spring Boot *(Kotlin)*

### 17. Frontend Development

#### 17.1 Web fundamentals

- `17.01.01` Internet and web
- `17.01.02` Browser architecture
- `17.01.03` Client-server communication
- `17.01.04` DOM
- `17.01.05` BOM
- `17.01.06` Rendering
- `17.01.07` Browser storage
- `17.01.08` Cookies
- `17.01.09` Local storage
- `17.01.10` Session storage

#### 17.2 HTML

- `17.02.01` Elements
- `17.02.02` Attributes
- `17.02.03` Semantic HTML
- `17.02.04` Forms
- `17.02.05` Tables
- `17.02.06` Multimedia
- `17.02.07` Accessibility
- `17.02.08` SEO
- `17.02.09` Structured data
- `17.02.10` Web components

#### 17.3 CSS

- `17.03.01` Selectors
- `17.03.02` Specificity
- `17.03.03` Box model
- `17.03.04` Positioning
- `17.03.05` Display
- `17.03.06` Flexbox
- `17.03.07` Grid
- `17.03.08` Transitions
- `17.03.09` Animations
- `17.03.10` Responsive design
- `17.03.11` Media queries
- `17.03.12` CSS variables
- `17.03.13` Container queries
- `17.03.14` CSS architecture
- `17.03.15` Advanced rendering techniques

#### 17.4 JavaScript

- `17.04.01` Variables
- `17.04.02` Data types
- `17.04.03` Functions
- `17.04.04` Scope
- `17.04.05` Closures
- `17.04.06` Objects
- `17.04.07` Arrays
- `17.04.08` Prototypes
- `17.04.09` Classes
- `17.04.10` Promises
- `17.04.11` Async/await
- `17.04.12` Event loop
- `17.04.13` Event delegation
- `17.04.14` Modules
- `17.04.15` ES6+
- `17.04.16` Memory management
- `17.04.17` Browser APIs
- `17.04.18` Performance optimization

#### 17.5 TypeScript

- `17.05.01` Static types
- `17.05.02` Interfaces
- `17.05.03` Type aliases
- `17.05.04` Generics
- `17.05.05` Union types
- `17.05.06` Intersection types
- `17.05.07` Utility types
- `17.05.08` Type narrowing
- `17.05.09` Advanced type manipulation
- `17.05.10` Declaration files

#### 17.6 Frontend frameworks

- `17.06.01` **React** — Component-based UI
- `17.06.02` **Angular** — Full frontend framework
- `17.06.03` **Vue.js** — Progressive framework
- `17.06.04` **Svelte** — Compiler-based UI
- `17.06.05` SolidJS
- `17.06.06` Preact
- `17.06.07` Qwik
- `17.06.08` Astro
- `17.06.09` Lit
- `17.06.10` Ember
- `17.06.11` Backbone
- `17.06.12` Alpine.js

#### 17.7 Frontend ecosystem

- `17.07.01` Next.js
- `17.07.02` Nuxt
- `17.07.03` Remix
- `17.07.04` React Router
- `17.07.05` TanStack Router
- `17.07.06` Redux
- `17.07.07` Zustand
- `17.07.08` MobX
- `17.07.09` NgRx
- `17.07.10` Pinia
- `17.07.11` React Query
- `17.07.12` TanStack Query
- `17.07.13` Tailwind CSS
- `17.07.14` Bootstrap
- `17.07.15` Sass
- `17.07.16` Less
- `17.07.17` Material UI
- `17.07.18` Ant Design
- `17.07.19` shadcn/ui
- `17.07.20` Radix UI

#### 17.8 Advanced frontend engineering

- `17.08.01` SSR
- `17.08.02` SSG
- `17.08.03` ISR
- `17.08.04` Hydration
- `17.08.05` Server components
- `17.08.06` Streaming rendering
- `17.08.07` Micro-frontends
- `17.08.08` Code splitting
- `17.08.09` Lazy loading
- `17.08.10` Tree shaking
- `17.08.11` Web Workers
- `17.08.12` Service Workers
- `17.08.13` WebAssembly
- `17.08.14` WebGPU
- `17.08.15` Progressive Web Apps
- `17.08.16` Browser security
- `17.08.17` Rendering optimization
- `17.08.18` Core Web Vitals
- `17.08.19` Accessibility engineering
- `17.08.20` Internationalization

### 18. UI/UX and Human-Computer Interaction

#### 18.1 Core topics *(synthesized heading)*

- `18.01.01` UI fundamentals
- `18.01.02` UX fundamentals
- `18.01.03` User research
- `18.01.04` User interviews
- `18.01.05` Persona creation
- `18.01.06` User journeys
- `18.01.07` User flows
- `18.01.08` Information architecture
- `18.01.09` Wireframing
- `18.01.10` Prototyping
- `18.01.11` Interaction design
- `18.01.12` Visual hierarchy
- `18.01.13` Typography
- `18.01.14` Color theory
- `18.01.15` Layout systems
- `18.01.16` Responsive design
- `18.01.17` Design systems
- `18.01.18` Design tokens
- `18.01.19` Component libraries
- `18.01.20` Accessibility
- `18.01.21` WCAG
- `18.01.22` Usability testing
- `18.01.23` A/B testing
- `18.01.24` Behavioral analytics
- `18.01.25` Cognitive psychology
- `18.01.26` Human-computer interaction
- `18.01.27` Inclusive design
- `18.01.28` Voice interfaces
- `18.01.29` Conversational interfaces
- `18.01.30` Spatial interfaces
- `18.01.31` Accessibility for assistive technologies

### 19. Mobile Application Development

#### 19.1 Mobile fundamentals

- `19.01.01` Mobile operating systems
- `19.01.02` Mobile hardware
- `19.01.03` App lifecycle
- `19.01.04` Touch interfaces
- `19.01.05` Device sensors
- `19.01.06` Mobile networking
- `19.01.07` Mobile storage

#### 19.2 Android development

- `19.02.01` Java
- `19.02.02` Kotlin
- `19.02.03` Android SDK
- `19.02.04` Android Studio
- `19.02.05` Activities
- `19.02.06` Fragments
- `19.02.07` Services
- `19.02.08` Broadcast receivers
- `19.02.09` Jetpack Compose
- `19.02.10` Room
- `19.02.11` WorkManager
- `19.02.12` Navigation
- `19.02.13` Dependency injection
- `19.02.14` Android security

#### 19.3 iOS development

- `19.03.01` Swift
- `19.03.02` SwiftUI
- `19.03.03` UIKit
- `19.03.04` Xcode
- `19.03.05` View controllers
- `19.03.06` Core Data
- `19.03.07` Combine
- `19.03.08` Swift concurrency
- `19.03.09` Core Animation
- `19.03.10` iOS security
- `19.03.11` App Store distribution

#### 19.4 Cross-platform development

- `19.04.01` Flutter
- `19.04.02` React Native
- `19.04.03` .NET MAUI
- `19.04.04` Kotlin Multiplatform
- `19.04.05` Ionic
- `19.04.06` Capacitor
- `19.04.07` NativeScript

#### 19.5 Advanced mobile

- `19.05.01` Offline-first applications
- `19.05.02` Local synchronization
- `19.05.03` Push notifications
- `19.05.04` Background processing
- `19.05.05` App signing
- `19.05.06` Deep linking
- `19.05.07` In-app purchases
- `19.05.08` Mobile analytics
- `19.05.09` Mobile testing
- `19.05.10` Battery optimization
- `19.05.11` App store optimization
- `19.05.12` Mobile application security

### 20. Desktop Application Development

#### 20.1 Core topics *(synthesized heading)*

- `20.01.01` Native desktop applications
- `20.01.02` Windows application development
- `20.01.03` macOS application development
- `20.01.04` Linux GUI development
- `20.01.05` Electron
- `20.01.06` Tauri
- `20.01.07` Qt
- `20.01.08` GTK
- `20.01.09` .NET MAUI
- `20.01.10` WPF
- `20.01.11` WinUI
- `20.01.12` JavaFX
- `20.01.13` Swing
- `20.01.14` Avalonia
- `20.01.15` Flutter desktop
- `20.01.16` Application packaging
- `20.01.17` Auto-updates
- `20.01.18` Native system integration
- `20.01.19` Desktop security
- `20.01.20` Cross-platform compatibility

### 21. API Integration and Messaging Systems

This is important in modern enterprise applications.

#### 21.1 Core topics *(synthesized heading)*

- `21.01.01` API consumption
- `21.01.02` Third-party integrations
- `21.01.03` Webhooks
- `21.01.04` Event notifications
- `21.01.05` Message queues
- `21.01.06` Publish-subscribe patterns
- `21.01.07` Point-to-point messaging
- `21.01.08` Message serialization
- `21.01.09` Message ordering
- `21.01.10` Delivery guarantees
- `21.01.11` At-most-once delivery
- `21.01.12` At-least-once delivery
- `21.01.13` Exactly-once processing semantics
- `21.01.14` Dead-letter queues
- `21.01.15` Retry mechanisms
- `21.01.16` Consumer groups
- `21.01.17` Message partitioning
- `21.01.18` Event streaming

#### 21.2 Technologies

- `21.02.01` Apache Kafka
- `21.02.02` RabbitMQ
- `21.02.03` Apache Pulsar
- `21.02.04` NATS
- `21.02.05` Redis Streams
- `21.02.06` Amazon SQS
- `21.02.07` Amazon SNS
- `21.02.08` Azure Service Bus
- `21.02.09` Google Pub/Sub
- `21.02.10` ActiveMQ

## PART V — DISTRIBUTED SYSTEMS AND SYSTEM DESIGN

### 22. Distributed Systems

*Source tags: Advanced software engineering*

#### 22.1 Fundamentals

- `22.01.01` Distributed computing
- `22.01.02` Nodes
- `22.01.03` Network communication
- `22.01.04` Service-to-service communication
- `22.01.05` Distributed resources
- `22.01.06` Partial failures
- `22.01.07` Network partitions

#### 22.2 Distributed system challenges

- `22.02.01` Latency
- `22.02.02` Clock synchronization
- `22.02.03` Clock drift
- `22.02.04` Timeouts
- `22.02.05` Retries
- `22.02.06` Duplicate requests
- `22.02.07` Message ordering
- `22.02.08` Network failures
- `22.02.09` Partial availability
- `22.02.10` Split-brain conditions

#### 22.3 Consistency

- `22.03.01` Strong consistency
- `22.03.02` Eventual consistency
- `22.03.03` Causal consistency
- `22.03.04` Sequential consistency
- `22.03.05` Linearizability
- `22.03.06` Read-your-writes consistency

#### 22.4 Distributed databases

- `22.04.01` Replication
- `22.04.02` Sharding
- `22.04.03` Partitioning
- `22.04.04` Leader-follower
- `22.04.05` Leaderless systems
- `22.04.06` Quorum reads and writes
- `22.04.07` Conflict resolution
- `22.04.08` Distributed transactions

#### 22.5 Theoretical concepts

- `22.05.01` CAP theorem
- `22.05.02` PACELC
- `22.05.03` FLP impossibility
- `22.05.04` Consensus
- `22.05.05` Byzantine fault tolerance
- `22.05.06` Failure detectors
- `22.05.07` Logical clocks
- `22.05.08` Vector clocks

#### 22.6 Consensus algorithms

- `22.06.01` Paxos
- `22.06.02` Raft
- `22.06.03` Multi-Paxos
- `22.06.04` Byzantine consensus
- `22.06.05` Gossip protocols
- `22.06.06` Leader election

#### 22.7 Advanced distributed architecture

- `22.07.01` Service discovery
- `22.07.02` Distributed locking
- `22.07.03` Distributed caching
- `22.07.04` Global load balancing
- `22.07.05` Multi-region deployments
- `22.07.06` Geo-replication
- `22.07.07` Disaster recovery
- `22.07.08` Distributed tracing
- `22.07.09` Stream processing
- `22.07.10` Distributed schedulers
- `22.07.11` Federated systems

### 23. System Design

This is a separate skill from simply knowing frameworks.

#### 23.1 Low-Level Design (LLD)

- `23.01.01` Object-oriented design
- `23.01.02` Class relationships
- `23.01.03` Interface design
- `23.01.04` SOLID
- `23.01.05` Design patterns
- `23.01.06` Class diagrams
- `23.01.07` Entity modeling
- `23.01.08` API contracts
- `23.01.09` Component design
- `23.01.10` Extensibility
- `23.01.11` Reusability

#### 23.2 High-Level Design (HLD)

- `23.02.01` Requirements
- `23.02.02` Architecture selection
- `23.02.03` Component identification
- `23.02.04` Service boundaries
- `23.02.05` Database selection
- `23.02.06` Caching strategy
- `23.02.07` Load balancing
- `23.02.08` Message queues
- `23.02.09` Network architecture
- `23.02.10` Scaling strategy
- `23.02.11` Reliability design

#### 23.3 Capacity planning

- `23.03.01` Traffic estimation
- `23.03.02` Requests per second
- `23.03.03` Daily active users
- `23.03.04` Storage estimation
- `23.03.05` Bandwidth estimation
- `23.03.06` Read/write ratios
- `23.03.07` Peak load
- `23.03.08` Resource utilization

#### 23.4 System design patterns

- `23.04.01` URL shortener
- `23.04.02` Social media platform
- `23.04.03` Chat application
- `23.04.04` Video streaming
- `23.04.05` File storage
- `23.04.06` Notification platform
- `23.04.07` Payment platform
- `23.04.08` Ride booking
- `23.04.09` E-commerce system
- `23.04.10` Search engine
- `23.04.11` Recommendation system
- `23.04.12` News feed
- `23.04.13` Real-time collaboration
- `23.04.14` Distributed task scheduler
- `23.04.15` Logging platform
- `23.04.16` Rate limiter

#### 23.5 Advanced system design

- `23.05.01` Multi-region architecture
- `23.05.02` Active-active systems
- `23.05.03` Active-passive systems
- `23.05.04` Global consistency
- `23.05.05` Multi-tenant systems
- `23.05.06` Event-driven systems
- `23.05.07` Serverless architecture
- `23.05.08` Fault isolation
- `23.05.09` Resilience engineering
- `23.05.10` Cost-aware architecture
- `23.05.11` Data-intensive architecture

## PART VI — CLOUD, DEVOPS AND INFRASTRUCTURE

### 24. Cloud Computing

#### 24.1 Cloud fundamentals

- `24.01.01` What is cloud computing?
- `24.01.02` IaaS
- `24.01.03` PaaS
- `24.01.04` SaaS
- `24.01.05` FaaS
- `24.01.06` Public cloud
- `24.01.07` Private cloud
- `24.01.08` Hybrid cloud
- `24.01.09` Multi-cloud
- `24.01.10` Cloud regions
- `24.01.11` Availability zones
- `24.01.12` Edge computing

#### 24.2 Cloud infrastructure

- `24.02.01` Virtual machines
- `24.02.02` Storage
- `24.02.03` Networking
- `24.02.04` Load balancers
- `24.02.05` Firewalls
- `24.02.06` DNS
- `24.02.07` CDNs
- `24.02.08` IAM
- `24.02.09` Secrets
- `24.02.10` Autoscaling
- `24.02.11` Monitoring
- `24.02.12` Billing
- `24.02.13` Disaster recovery

#### 24.3 Major cloud providers

- `24.03.01` **Amazon Web Services** — EC2, S3, RDS, Lambda, EKS, DynamoDB, CloudFront, SQS
- `24.03.02` EC2 *(service of Amazon Web Services)*
- `24.03.03` S3 *(service of Amazon Web Services)*
- `24.03.04` RDS *(service of Amazon Web Services)*
- `24.03.05` Lambda *(service of Amazon Web Services)*
- `24.03.06` EKS *(service of Amazon Web Services)*
- `24.03.07` DynamoDB *(service of Amazon Web Services)*
- `24.03.08` CloudFront *(service of Amazon Web Services)*
- `24.03.09` SQS *(service of Amazon Web Services)*
- `24.03.10` **Microsoft Azure** — Virtual Machines, Blob Storage, Functions, AKS, Azure SQL
- `24.03.11` Virtual Machines *(service of Microsoft Azure)*
- `24.03.12` Blob Storage *(service of Microsoft Azure)*
- `24.03.13` Functions *(service of Microsoft Azure)*
- `24.03.14` AKS *(service of Microsoft Azure)*
- `24.03.15` Azure SQL *(service of Microsoft Azure)*
- `24.03.16` **Google Cloud** — Compute Engine, GKE, Cloud Run, BigQuery, Cloud Storage
- `24.03.17` Compute Engine *(service of Google Cloud)*
- `24.03.18` GKE *(service of Google Cloud)*
- `24.03.19` Cloud Run *(service of Google Cloud)*
- `24.03.20` BigQuery *(service of Google Cloud)*
- `24.03.21` Cloud Storage *(service of Google Cloud)*

#### 24.4 Other cloud ecosystems

- `24.04.01` Oracle Cloud
- `24.04.02` IBM Cloud
- `24.04.03` Alibaba Cloud
- `24.04.04` DigitalOcean
- `24.04.05` Cloudflare
- `24.04.06` Akamai
- `24.04.07` OVHcloud
- `24.04.08` Hetzner
- `24.04.09` Vercel
- `24.04.10` Netlify
- `24.04.11` Fly.io
- `24.04.12` Render

#### 24.5 Advanced cloud

- `24.05.01` Cloud-native architecture
- `24.05.02` Hybrid networking
- `24.05.03` Multi-cloud architecture
- `24.05.04` Cloud migration
- `24.05.05` Cloud security
- `24.05.06` Cloud governance
- `24.05.07` Cloud cost optimization
- `24.05.08` Cloud automation
- `24.05.09` Cloud-native databases
- `24.05.10` Cloud-native AI infrastructure

### 25. Containers and Container Orchestration

#### 25.1 Core topics *(synthesized heading)*

- `25.01.01` Virtualization
- `25.01.02` Hypervisors
- `25.01.03` Virtual machines
- `25.01.04` Container fundamentals
- `25.01.05` Docker
- `25.01.06` Docker images
- `25.01.07` Dockerfiles
- `25.01.08` Docker Compose
- `25.01.09` Container registries
- `25.01.10` Container networking
- `25.01.11` Container storage
- `25.01.12` Container security
- `25.01.13` Image scanning
- `25.01.14` Kubernetes
- `25.01.15` Pods
- `25.01.16` Deployments
- `25.01.17` ReplicaSets
- `25.01.18` Services
- `25.01.19` ConfigMaps
- `25.01.20` Secrets
- `25.01.21` Namespaces
- `25.01.22` Ingress
- `25.01.23` Persistent volumes
- `25.01.24` StatefulSets
- `25.01.25` DaemonSets
- `25.01.26` Jobs
- `25.01.27` CronJobs
- `25.01.28` Helm
- `25.01.29` Kustomize
- `25.01.30` Operators
- `25.01.31` Custom resources
- `25.01.32` Kubernetes networking
- `25.01.33` Kubernetes scheduling
- `25.01.34` Cluster autoscaling
- `25.01.35` Federation
- `25.01.36` Multi-cluster management

#### 25.2 Container and orchestration ecosystem

- `25.02.01` Docker
- `25.02.02` Podman
- `25.02.03` containerd
- `25.02.04` CRI-O
- `25.02.05` Kubernetes
- `25.02.06` OpenShift
- `25.02.07` Amazon EKS
- `25.02.08` Azure AKS
- `25.02.09` Google GKE
- `25.02.10` Nomad
- `25.02.11` Rancher
- `25.02.12` Helm
- `25.02.13` K3s

### 26. DevOps Engineering

#### 26.1 DevOps fundamentals

- `26.01.01` Development and operations collaboration
- `26.01.02` Infrastructure automation
- `26.01.03` Continuous integration
- `26.01.04` Continuous delivery
- `26.01.05` Continuous deployment
- `26.01.06` Continuous testing
- `26.01.07` Release engineering
- `26.01.08` Configuration management

#### 26.2 CI/CD tools

- `26.02.01` GitHub Actions
- `26.02.02` GitLab CI/CD
- `26.02.03` Jenkins
- `26.02.04` CircleCI
- `26.02.05` Travis CI
- `26.02.06` Azure Pipelines
- `26.02.07` Buildkite
- `26.02.08` TeamCity
- `26.02.09` Argo CD
- `26.02.10` Flux CD

#### 26.3 Infrastructure as Code

- `26.03.01` Terraform
- `26.03.02` OpenTofu
- `26.03.03` Pulumi
- `26.03.04` AWS CloudFormation
- `26.03.05` Azure Bicep
- `26.03.06` Ansible
- `26.03.07` Chef
- `26.03.08` Puppet
- `26.03.09` Salt

#### 26.4 Infrastructure management

- `26.04.01` Environment provisioning
- `26.04.02` Configuration management
- `26.04.03` Secrets management
- `26.04.04` Certificate management
- `26.04.05` Automated deployments
- `26.04.06` Blue-green deployment
- `26.04.07` Canary deployment
- `26.04.08` Rolling deployment
- `26.04.09` Rollbacks
- `26.04.10` GitOps
- `26.04.11` Immutable infrastructure

#### 26.5 Advanced DevOps

- `26.05.01` Platform engineering
- `26.05.02` Internal developer platforms
- `26.05.03` Developer portals
- `26.05.04` Golden paths
- `26.05.05` Infrastructure automation
- `26.05.06` Policy as Code
- `26.05.07` Software supply chain management
- `26.05.08` Artifact management
- `26.05.09` Deployment orchestration
- `26.05.10` Environment management
- `26.05.11` DevSecOps

### 27. Site Reliability Engineering (SRE)

#### 27.1 Core topics *(synthesized heading)*

- `27.01.01` Reliability fundamentals
- `27.01.02` Availability
- `27.01.03` Durability
- `27.01.04` Redundancy
- `27.01.05` Fault tolerance
- `27.01.06` SLI
- `27.01.07` SLO
- `27.01.08` SLA
- `27.01.09` Error budgets
- `27.01.10` Monitoring
- `27.01.11` Alerting
- `27.01.12` Incident management
- `27.01.13` On-call practices
- `27.01.14` Postmortems
- `27.01.15` Root cause analysis
- `27.01.16` Capacity planning
- `27.01.17` Load testing
- `27.01.18` Stress testing
- `27.01.19` Chaos engineering
- `27.01.20` Resilience testing
- `27.01.21` Disaster recovery
- `27.01.22` Business continuity
- `27.01.23` Backup and restoration
- `27.01.24` High availability
- `27.01.25` Auto-healing infrastructure
- `27.01.26` Toil reduction
- `27.01.27` Reliability automation

### 28. Observability and Monitoring

#### 28.1 Core topics *(synthesized heading)*

- `28.01.01` Application logging
- `28.01.02` Structured logging
- `28.01.03` Log aggregation
- `28.01.04` Metrics
- `28.01.05` Distributed tracing
- `28.01.06` Profiling
- `28.01.07` Error tracking
- `28.01.08` Alerting
- `28.01.09` Dashboards
- `28.01.10` Health checks
- `28.01.11` Synthetic monitoring
- `28.01.12` Real-user monitoring
- `28.01.13` OpenTelemetry
- `28.01.14` Prometheus
- `28.01.15` Grafana
- `28.01.16` Loki
- `28.01.17` Jaeger
- `28.01.18` Tempo
- `28.01.19` ELK Stack
- `28.01.20` OpenSearch
- `28.01.21` Datadog
- `28.01.22` New Relic
- `28.01.23` Splunk
- `28.01.24` Sentry
- `28.01.25` PagerDuty

#### 28.2 Advanced topics

- `28.02.01` Cardinality management
- `28.02.02` Trace sampling
- `28.02.03` Service maps
- `28.02.04` Correlation IDs
- `28.02.05` Telemetry pipelines
- `28.02.06` Anomaly detection
- `28.02.07` AIOps
- `28.02.08` Automated remediation

### 29. Performance Engineering

#### 29.1 Core topics *(synthesized heading)*

- `29.01.01` Benchmarking
- `29.01.02` Profiling
- `29.01.03` CPU optimization
- `29.01.04` Memory optimization
- `29.01.05` Query optimization
- `29.01.06` Network optimization
- `29.01.07` Latency analysis
- `29.01.08` Throughput
- `29.01.09` Concurrency
- `29.01.10` Parallelism
- `29.01.11` Caching
- `29.01.12` Connection pooling
- `29.01.13` Load testing
- `29.01.14` Stress testing
- `29.01.15` Soak testing
- `29.01.16` Scalability testing
- `29.01.17` Performance regression
- `29.01.18` Tail latency
- `29.01.19` Performance modeling
- `29.01.20` Hardware-aware optimization
- `29.01.21` GPU performance tuning

## PART VII — SOFTWARE QUALITY AND CYBERSECURITY

### 30. Software Testing and Quality Assurance

*Source tags: Essential*

#### 30.1 Testing fundamentals

- `30.01.01` Verification vs validation
- `30.01.02` Test cases
- `30.01.03` Test scenarios
- `30.01.04` Test data
- `30.01.05` Test coverage
- `30.01.06` Assertions
- `30.01.07` Defects
- `30.01.08` Bugs
- `30.01.09` Test plans
- `30.01.10` Test strategies

#### 30.2 Testing levels

- `30.02.01` Unit testing
- `30.02.02` Integration testing
- `30.02.03` Component testing
- `30.02.04` System testing
- `30.02.05` Acceptance testing
- `30.02.06` End-to-end testing

#### 30.3 Testing types

- `30.03.01` Functional testing
- `30.03.02` Non-functional testing
- `30.03.03` Regression testing
- `30.03.04` Smoke testing
- `30.03.05` Sanity testing
- `30.03.06` Exploratory testing
- `30.03.07` Compatibility testing
- `30.03.08` Cross-browser testing
- `30.03.09` Accessibility testing
- `30.03.10` Localization testing

#### 30.4 Advanced testing

- `30.04.01` Load testing
- `30.04.02` Stress testing
- `30.04.03` Spike testing
- `30.04.04` Soak testing
- `30.04.05` Chaos testing
- `30.04.06` Security testing
- `30.04.07` Fuzz testing
- `30.04.08` Mutation testing
- `30.04.09` Property-based testing
- `30.04.10` Snapshot testing
- `30.04.11` Contract testing
- `30.04.12` Visual regression testing
- `30.04.13` Differential testing
- `30.04.14` Metamorphic testing
- `30.04.15` Formal verification

#### 30.5 Testing frameworks

- `30.05.01` JUnit
- `30.05.02` TestNG
- `30.05.03` PyTest
- `30.05.04` Unittest
- `30.05.05` Jest
- `30.05.06` Vitest
- `30.05.07` Mocha
- `30.05.08` Cypress
- `30.05.09` Playwright
- `30.05.10` Selenium
- `30.05.11` Appium
- `30.05.12` Robot Framework
- `30.05.13` Postman
- `30.05.14` REST Assured
- `30.05.15` k6
- `30.05.16` JMeter
- `30.05.17` Gatling
- `30.05.18` Locust

#### 30.6 Advanced quality engineering

- `30.06.01` Test automation
- `30.06.02` Continuous testing
- `30.06.03` Test pyramid
- `30.06.04` Test coverage analysis
- `30.06.05` Flaky test management
- `30.06.06` Test data management
- `30.06.07` Quality gates
- `30.06.08` Shift-left testing
- `30.06.09` Risk-based testing
- `30.06.10` Defect prediction

### 31. Cybersecurity and Software Security

*Source tags: Important for every professional engineer*

#### 31.1 Security fundamentals

- `31.01.01` Confidentiality
- `31.01.02` Integrity
- `31.01.03` Availability
- `31.01.04` CIA triad
- `31.01.05` Authentication
- `31.01.06` Authorization
- `31.01.07` Accountability
- `31.01.08` Non-repudiation
- `31.01.09` Threats
- `31.01.10` Vulnerabilities
- `31.01.11` Risks
- `31.01.12` Attack surfaces
- `31.01.13` Threat modeling

#### 31.2 Cryptography

- `31.02.01` Plaintext and ciphertext
- `31.02.02` Encryption and decryption
- `31.02.03` Symmetric encryption
- `31.02.04` AES
- `31.02.05` Asymmetric encryption
- `31.02.06` RSA
- `31.02.07` Elliptic curve cryptography
- `31.02.08` Digital signatures
- `31.02.09` Hashing
- `31.02.10` SHA-256
- `31.02.11` Password hashing
- `31.02.12` Salting
- `31.02.13` HMAC
- `31.02.14` PKI
- `31.02.15` Digital certificates
- `31.02.16` TLS
- `31.02.17` Key management

#### 31.3 Application security

- `31.03.01` OWASP Top 10
- `31.03.02` SQL injection
- `31.03.03` Cross-site scripting
- `31.03.04` CSRF
- `31.03.05` SSRF
- `31.03.06` Command injection
- `31.03.07` Path traversal
- `31.03.08` Broken access control
- `31.03.09` Insecure deserialization
- `31.03.10` Authentication vulnerabilities
- `31.03.11` Session hijacking
- `31.03.12` Clickjacking
- `31.03.13` Security headers
- `31.03.14` Input validation
- `31.03.15` Output encoding

#### 31.4 Secure software development

- `31.04.01` Secure coding
- `31.04.02` Secure architecture
- `31.04.03` Security requirements
- `31.04.04` Security testing
- `31.04.05` Security reviews
- `31.04.06` Dependency security
- `31.04.07` Secrets management
- `31.04.08` Software supply chain security
- `31.04.09` SBOM
- `31.04.10` Code signing
- `31.04.11` Artifact verification

#### 31.5 Infrastructure security

- `31.05.01` Network security
- `31.05.02` Firewall management
- `31.05.03` Cloud security
- `31.05.04` Container security
- `31.05.05` Kubernetes security
- `31.05.06` IAM
- `31.05.07` Privilege management
- `31.05.08` Zero trust
- `31.05.09` Endpoint security
- `31.05.10` Infrastructure hardening
- `31.05.11` Vulnerability management

#### 31.6 Security operations

- `31.06.01` Security monitoring
- `31.06.02` SIEM
- `31.06.03` SOAR
- `31.06.04` Incident response
- `31.06.05` Digital forensics
- `31.06.06` Threat intelligence
- `31.06.07` Malware analysis
- `31.06.08` Security auditing
- `31.06.09` Intrusion detection
- `31.06.10` Intrusion prevention
- `31.06.11` Penetration testing
- `31.06.12` Risk management

#### 31.7 Advanced security

- `31.07.01` Formal security verification
- `31.07.02` Hardware security
- `31.07.03` Trusted execution environments
- `31.07.04` Secure enclaves
- `31.07.05` Side-channel resistance
- `31.07.06` Homomorphic encryption
- `31.07.07` Secure multiparty computation
- `31.07.08` Zero-knowledge proofs
- `31.07.09` Privacy-preserving computation
- `31.07.10` Post-quantum cryptography
- `31.07.11` Cryptographic agility

#### 31.8 Standards and frameworks

- `31.08.01` OWASP
- `31.08.02` NIST Cybersecurity Framework
- `31.08.03` NIST SP 800 series
- `31.08.04` ISO 27001
- `31.08.05` ISO 27002
- `31.08.06` SOC 2
- `31.08.07` PCI DSS
- `31.08.08` GDPR
- `31.08.09` HIPAA
- `31.08.10` CIS Benchmarks
- `31.08.11` MITRE ATT&CK
- `31.08.12` CWE
- `31.08.13` CVE
- `31.08.14` CVSS

## PART VIII — DATA ENGINEERING, DATA SCIENCE AND ANALYTICS

### 32. Data Engineering

#### 32.1 Data fundamentals

- `32.01.01` Structured data
- `32.01.02` Semi-structured data
- `32.01.03` Unstructured data
- `32.01.04` Data sources
- `32.01.05` Data formats
- `32.01.06` CSV
- `32.01.07` JSON
- `32.01.08` XML
- `32.01.09` Parquet
- `32.01.10` Avro
- `32.01.11` ORC
- `32.01.12` Data ingestion

#### 32.2 Data processing

- `32.02.01` Batch processing
- `32.02.02` Stream processing
- `32.02.03` Real-time processing
- `32.02.04` ETL
- `32.02.05` ELT
- `32.02.06` Data transformation
- `32.02.07` Data cleansing
- `32.02.08` Data validation
- `32.02.09` Data deduplication
- `32.02.10` Schema evolution

#### 32.3 Data pipeline architecture

- `32.03.01` Data pipelines
- `32.03.02` Workflow orchestration
- `32.03.03` Scheduling
- `32.03.04` Dependency management
- `32.03.05` Data lineage
- `32.03.06` Data quality
- `32.03.07` Metadata management
- `32.03.08` Data observability
- `32.03.09` CDC
- `32.03.10` Data contracts

#### 32.4 Big data

- `32.04.01` Distributed storage
- `32.04.02` Distributed processing
- `32.04.03` Hadoop
- `32.04.04` HDFS
- `32.04.05` MapReduce
- `32.04.06` Apache Spark
- `32.04.07` Apache Flink
- `32.04.08` Apache Beam
- `32.04.09` Hive
- `32.04.10` Presto
- `32.04.11` Trino

#### 32.5 Data streaming

- `32.05.01` Apache Kafka
- `32.05.02` Kafka Streams
- `32.05.03` Apache Pulsar
- `32.05.04` Apache Flink
- `32.05.05` Spark Streaming
- `32.05.06` Debezium
- `32.05.07` Stream joins
- `32.05.08` Event-time processing
- `32.05.09` Windowing
- `32.05.10` Watermarks

#### 32.6 Modern data architecture

- `32.06.01` Data warehouses
- `32.06.02` Data lakes
- `32.06.03` Lakehouses
- `32.06.04` Data marts
- `32.06.05` Data mesh
- `32.06.06` Data fabric
- `32.06.07` Medallion architecture
- `32.06.08` Data virtualization
- `32.06.09` Reverse ETL
- `32.06.10` Data products

#### 32.7 Workflow orchestration

- `32.07.01` Apache Airflow
- `32.07.02` Dagster
- `32.07.03` Prefect
- `32.07.04` Luigi
- `32.07.05` Argo Workflows
- `32.07.06` Mage

#### 32.8 Advanced data engineering

- `32.08.01` Distributed query processing
- `32.08.02` Petabyte-scale processing
- `32.08.03` Data governance
- `32.08.04` Data cataloging
- `32.08.05` Privacy engineering
- `32.08.06` Data reliability
- `32.08.07` Streaming architectures
- `32.08.08` Real-time analytics

### 33. Data Science and Business Intelligence

#### 33.1 Data science foundations

- `33.01.01` Data collection
- `33.01.02` Data cleaning
- `33.01.03` Exploratory data analysis
- `33.01.04` Feature engineering
- `33.01.05` Statistical analysis
- `33.01.06` Data visualization
- `33.01.07` Hypothesis testing
- `33.01.08` Statistical modeling

#### 33.2 Data analysis

- `33.02.01` Descriptive analytics
- `33.02.02` Diagnostic analytics
- `33.02.03` Predictive analytics
- `33.02.04` Prescriptive analytics
- `33.02.05` Cohort analysis
- `33.02.06` Funnel analysis
- `33.02.07` Retention analysis
- `33.02.08` Customer segmentation
- `33.02.09` Time-series analysis

#### 33.3 Business intelligence

- `33.03.01` Business metrics
- `33.03.02` KPIs
- `33.03.03` Dashboards
- `33.03.04` Reporting
- `33.03.05` OLAP
- `33.03.06` Data cubes
- `33.03.07` Drill-down analysis
- `33.03.08` Self-service BI

#### 33.4 Tools

- `33.04.01` Excel
- `33.04.02` Python
- `33.04.03` R
- `33.04.04` SQL
- `33.04.05` Tableau
- `33.04.06` Power BI
- `33.04.07` Looker
- `33.04.08` Metabase
- `33.04.09` Apache Superset
- `33.04.10` Jupyter
- `33.04.11` Google Colab

#### 33.5 Advanced analytics

- `33.05.01` A/B testing
- `33.05.02` Causal inference
- `33.05.03` Predictive modeling
- `33.05.04` Regression analysis
- `33.05.05` Time-series forecasting
- `33.05.06` Bayesian analytics
- `33.05.07` Experimentation platforms
- `33.05.08` Decision science

## PART IX — ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING

*Major modern engineering discipline*

### 34. Artificial Intelligence Fundamentals

Start with understanding what AI actually is before jumping into LLMs.

#### 34.1 Core topics *(synthesized heading)*

- `34.01.01` Introduction to AI
- `34.01.02` History of AI
- `34.01.03` Narrow AI
- `34.01.04` General AI concepts
- `34.01.05` Symbolic AI
- `34.01.06` Statistical AI
- `34.01.07` Knowledge representation
- `34.01.08` Search and planning
- `34.01.09` Reasoning
- `34.01.10` Decision-making
- `34.01.11` Intelligent agents
- `34.01.12` Expert systems
- `34.01.13` Knowledge graphs
- `34.01.14` Rule-based systems
- `34.01.15` Fuzzy logic
- `34.01.16` Probabilistic reasoning
- `34.01.17` Multi-agent systems

### 35. Mathematics for Machine Learning

#### 35.1 Core topics *(synthesized heading)*

- `35.01.01` Linear algebra
- `35.01.02` Probability
- `35.01.03` Statistics
- `35.01.04` Calculus
- `35.01.05` Matrix operations
- `35.01.06` Vectors and tensors
- `35.01.07` Derivatives
- `35.01.08` Partial derivatives
- `35.01.09` Gradients
- `35.01.10` Gradient descent
- `35.01.11` Optimization
- `35.01.12` Convex optimization
- `35.01.13` Information theory
- `35.01.14` Entropy
- `35.01.15` Cross-entropy
- `35.01.16` KL divergence
- `35.01.17` Bayesian methods

### 36. Machine Learning

*Source tags: Beginner → Advanced*

#### 36.1 ML fundamentals

- `36.01.01` What is machine learning?
- `36.01.02` Training data
- `36.01.03` Testing data
- `36.01.04` Validation data
- `36.01.05` Features
- `36.01.06` Labels
- `36.01.07` Models
- `36.01.08` Training
- `36.01.09` Inference
- `36.01.10` Overfitting
- `36.01.11` Underfitting
- `36.01.12` Bias-variance tradeoff
- `36.01.13` Generalization

#### 36.2 Supervised learning

- `36.02.01` Linear regression
- `36.02.02` Logistic regression
- `36.02.03` Decision trees
- `36.02.04` Random forests
- `36.02.05` Support vector machines
- `36.02.06` K-nearest neighbors
- `36.02.07` Naive Bayes
- `36.02.08` Gradient boosting
- `36.02.09` XGBoost
- `36.02.10` LightGBM
- `36.02.11` CatBoost

#### 36.3 Unsupervised learning

- `36.03.01` K-means
- `36.03.02` Hierarchical clustering
- `36.03.03` DBSCAN
- `36.03.04` Gaussian mixture models
- `36.03.05` Principal component analysis
- `36.03.06` Independent component analysis
- `36.03.07` Dimensionality reduction
- `36.03.08` Anomaly detection

#### 36.4 Semi-supervised learning

- `36.04.01` Pseudo-labeling
- `36.04.02` Self-training
- `36.04.03` Consistency regularization
- `36.04.04` Label propagation

#### 36.5 Self-supervised learning

- `36.05.01` Contrastive learning
- `36.05.02` Masked prediction
- `36.05.03` Representation learning
- `36.05.04` Predictive learning

#### 36.6 Model evaluation

- `36.06.01` Accuracy
- `36.06.02` Precision
- `36.06.03` Recall
- `36.06.04` F1-score
- `36.06.05` ROC
- `36.06.06` AUC
- `36.06.07` Confusion matrix
- `36.06.08` Mean squared error
- `36.06.09` Mean absolute error
- `36.06.10` Cross-validation
- `36.06.11` Model calibration

#### 36.7 Advanced ML

- `36.07.01` Ensemble learning
- `36.07.02` Stacking
- `36.07.03` Boosting
- `36.07.04` Bagging
- `36.07.05` AutoML
- `36.07.06` Active learning
- `36.07.07` Transfer learning
- `36.07.08` Few-shot learning
- `36.07.09` Online learning
- `36.07.10` Continual learning
- `36.07.11` Federated learning
- `36.07.12` Explainable AI
- `36.07.13` Causal machine learning
- `36.07.14` Graph machine learning

### 37. Deep Learning

#### 37.1 Neural network fundamentals

- `37.01.01` Artificial neurons
- `37.01.02` Weights
- `37.01.03` Biases
- `37.01.04` Activation functions
- `37.01.05` Layers
- `37.01.06` Forward propagation
- `37.01.07` Backpropagation
- `37.01.08` Loss functions
- `37.01.09` Optimizers
- `37.01.10` Gradient descent
- `37.01.11` Learning rate
- `37.01.12` Batch size
- `37.01.13` Epochs

#### 37.2 Neural network architectures

- `37.02.01` Feedforward neural networks
- `37.02.02` Multilayer perceptrons
- `37.02.03` Convolutional neural networks
- `37.02.04` Recurrent neural networks
- `37.02.05` LSTM
- `37.02.06` GRU
- `37.02.07` Autoencoders
- `37.02.08` Variational autoencoders
- `37.02.09` Generative adversarial networks
- `37.02.10` Graph neural networks
- `37.02.11` Siamese networks

#### 37.3 Advanced deep learning

- `37.03.01` Attention mechanisms
- `37.03.02` Self-attention
- `37.03.03` Transformers
- `37.03.04` Encoder-decoder architectures
- `37.03.05` Positional embeddings
- `37.03.06` Residual connections
- `37.03.07` Normalization
- `37.03.08` Mixture of Experts
- `37.03.09` Sparse neural networks
- `37.03.10` Neural scaling laws
- `37.03.11` Multimodal neural networks

#### 37.4 Deep learning frameworks

- `37.04.01` PyTorch
- `37.04.02` TensorFlow
- `37.04.03` Keras
- `37.04.04` JAX
- `37.04.05` MXNet
- `37.04.06` ONNX
- `37.04.07` Hugging Face
- `37.04.08` TensorRT

### 38. Natural Language Processing (NLP)

#### 38.1 Core topics *(synthesized heading)*

- `38.01.01` Text preprocessing
- `38.01.02` Tokenization
- `38.01.03` Stemming
- `38.01.04` Lemmatization
- `38.01.05` Stop-word removal
- `38.01.06` Bag of Words
- `38.01.07` TF-IDF
- `38.01.08` Word embeddings
- `38.01.09` Word2Vec
- `38.01.10` GloVe
- `38.01.11` FastText
- `38.01.12` Named entity recognition
- `38.01.13` Part-of-speech tagging
- `38.01.14` Dependency parsing
- `38.01.15` Text classification
- `38.01.16` Sentiment analysis
- `38.01.17` Text summarization
- `38.01.18` Machine translation
- `38.01.19` Question answering
- `38.01.20` Information extraction
- `38.01.21` Language modeling
- `38.01.22` Conversational AI
- `38.01.23` Speech-to-text
- `38.01.24` Text-to-speech

#### 38.2 Advanced topics

- `38.02.01` Contextual embeddings
- `38.02.02` Transformer-based NLP
- `38.02.03` BERT
- `38.02.04` Encoder-decoder models
- `38.02.05` Retrieval-based NLP
- `38.02.06` Neural information retrieval
- `38.02.07` Semantic search
- `38.02.08` Long-context language modeling

### 39. Computer Vision

#### 39.1 Core topics *(synthesized heading)*

- `39.01.01` Image processing
- `39.01.02` Image representation
- `39.01.03` Image filtering
- `39.01.04` Edge detection
- `39.01.05` Image segmentation
- `39.01.06` Image classification
- `39.01.07` Object detection
- `39.01.08` Feature extraction
- `39.01.09` Image recognition
- `39.01.10` Face detection
- `39.01.11` Pose estimation
- `39.01.12` Optical flow
- `39.01.13` OCR
- `39.01.14` Video analysis
- `39.01.15` Motion detection
- `39.01.16` Visual tracking

#### 39.2 Advanced topics

- `39.02.01` CNN architectures
- `39.02.02` YOLO
- `39.02.03` Vision Transformers
- `39.02.04` Mask R-CNN
- `39.02.05` U-Net
- `39.02.06` Diffusion-based vision
- `39.02.07` Multimodal vision-language models
- `39.02.08` 3D reconstruction
- `39.02.09` Neural radiance fields
- `39.02.10` Gaussian splatting
- `39.02.11` Vision-language-action models

### 40. Reinforcement Learning

#### 40.1 Core topics *(synthesized heading)*

- `40.01.01` Agent
- `40.01.02` Environment
- `40.01.03` State
- `40.01.04` Action
- `40.01.05` Reward
- `40.01.06` Policy
- `40.01.07` Value function
- `40.01.08` Q-function
- `40.01.09` Markov decision processes
- `40.01.10` Bellman equations
- `40.01.11` Exploration vs exploitation
- `40.01.12` Q-learning
- `40.01.13` SARSA
- `40.01.14` Deep Q-networks
- `40.01.15` Policy gradients
- `40.01.16` Actor-critic
- `40.01.17` PPO
- `40.01.18` A3C
- `40.01.19` Model-based reinforcement learning
- `40.01.20` Model-free reinforcement learning
- `40.01.21` Offline reinforcement learning
- `40.01.22` Multi-agent reinforcement learning
- `40.01.23` Inverse reinforcement learning
- `40.01.24` Hierarchical reinforcement learning

### 41. Generative AI

*Source tags: Modern AI engineering*

#### 41.1 Generative AI basics

- `41.01.01` Discriminative vs generative models
- `41.01.02` Generative modeling
- `41.01.03` Probability distributions
- `41.01.04` Latent spaces
- `41.01.05` Sampling
- `41.01.06` Conditional generation
- `41.01.07` Unconditional generation

#### 41.2 Generative architectures

- `41.02.01` Autoregressive models
- `41.02.02` Transformer models
- `41.02.03` Variational autoencoders
- `41.02.04` Generative adversarial networks
- `41.02.05` Diffusion models
- `41.02.06` Flow-based models
- `41.02.07` Energy-based models

#### 41.3 Generative AI applications

- `41.03.01` Text generation
- `41.03.02` Image generation
- `41.03.03` Audio generation
- `41.03.04` Music generation
- `41.03.05` Video generation
- `41.03.06` 3D generation
- `41.03.07` Code generation
- `41.03.08` Synthetic data generation
- `41.03.09` Conversational assistants

#### 41.4 Model adaptation

- `41.04.01` Pretraining
- `41.04.02` Fine-tuning
- `41.04.03` Instruction tuning
- `41.04.04` Supervised fine-tuning
- `41.04.05` LoRA
- `41.04.06` QLoRA
- `41.04.07` Parameter-efficient fine-tuning
- `41.04.08` Knowledge distillation
- `41.04.09` Quantization
- `41.04.10` Pruning

### 42. Large Language Models (LLMs)

*Source tags: Advanced AI engineering*

#### 42.1 LLM fundamentals

- `42.01.01` Language modeling
- `42.01.02` Tokenization
- `42.01.03` Tokens
- `42.01.04` Vocabulary
- `42.01.05` Embeddings
- `42.01.06` Context windows
- `42.01.07` Attention
- `42.01.08` Transformers
- `42.01.09` Autoregressive generation
- `42.01.10` Logits
- `42.01.11` Sampling
- `42.01.12` Temperature
- `42.01.13` Top-k sampling
- `42.01.14` Top-p sampling

#### 42.2 LLM architecture

- `42.02.01` Decoder-only models
- `42.02.02` Encoder-only models
- `42.02.03` Encoder-decoder models
- `42.02.04` Multi-head attention
- `42.02.05` Rotary positional embeddings
- `42.02.06` KV caching
- `42.02.07` Grouped-query attention
- `42.02.08` Mixture of Experts
- `42.02.09` Long-context architectures

#### 42.3 LLM model families

- `42.03.01` GPT-style models
- `42.03.02` BERT-style models
- `42.03.03` Llama
- `42.03.04` Qwen
- `42.03.05` Gemma
- `42.03.06` Mistral
- `42.03.07` DeepSeek
- `42.03.08` Phi
- `42.03.09` T5
- `42.03.10` FLAN-T5
- `42.03.11` Claude-family models
- `42.03.12` Gemini-family models

#### 42.4 LLM development

- `42.04.01` Model selection
- `42.04.02` Prompt design
- `42.04.03` System prompts
- `42.04.04` Few-shot prompting
- `42.04.05` Chain-of-thought concepts
- `42.04.06` Structured outputs
- `42.04.07` Function calling
- `42.04.08` Tool calling
- `42.04.09` Context engineering
- `42.04.10` Model routing
- `42.04.11` Model evaluation
- `42.04.12` Hallucination mitigation
- `42.04.13` Safety evaluation

#### 42.5 Advanced LLM topics

- `42.05.01` Retrieval-augmented generation
- `42.05.02` Fine-tuning
- `42.05.03` Preference optimization
- `42.05.04` RLHF
- `42.05.05` DPO
- `42.05.06` Model alignment
- `42.05.07` Synthetic data
- `42.05.08` Long-context retrieval
- `42.05.09` LLM inference optimization
- `42.05.10` Speculative decoding
- `42.05.11` Paged attention
- `42.05.12` Continuous batching
- `42.05.13` Model parallelism
- `42.05.14` Tensor parallelism
- `42.05.15` Pipeline parallelism
- `42.05.16` Distributed inference

### 43. Retrieval-Augmented Generation (RAG)

#### 43.1 Core topics *(synthesized heading)*

- `43.01.01` RAG fundamentals
- `43.01.02` Document ingestion
- `43.01.03` Document parsing
- `43.01.04` Data cleaning
- `43.01.05` Chunking
- `43.01.06` Overlapping chunks
- `43.01.07` Embedding generation
- `43.01.08` Vector similarity
- `43.01.09` Cosine similarity
- `43.01.10` Nearest-neighbor search
- `43.01.11` Vector indexing
- `43.01.12` Metadata filtering
- `43.01.13` Retrieval
- `43.01.14` Prompt augmentation
- `43.01.15` Answer generation
- `43.01.16` Citation generation

#### 43.2 Advanced RAG

- `43.02.01` Hybrid search
- `43.02.02` Dense retrieval
- `43.02.03` Sparse retrieval
- `43.02.04` BM25
- `43.02.05` Reranking
- `43.02.06` Query expansion
- `43.02.07` Query decomposition
- `43.02.08` Multi-query retrieval
- `43.02.09` HyDE
- `43.02.10` Context compression
- `43.02.11` Graph RAG
- `43.02.12` Agentic RAG
- `43.02.13` Corrective RAG
- `43.02.14` Adaptive retrieval
- `43.02.15` Multimodal RAG
- `43.02.16` Retrieval evaluation
- `43.02.17` Groundedness evaluation

#### 43.3 Vector database ecosystem

- `43.03.01` FAISS
- `43.03.02` Milvus
- `43.03.03` Qdrant
- `43.03.04` Weaviate
- `43.03.05` Pinecone
- `43.03.06` Chroma
- `43.03.07` pgvector
- `43.03.08` Elasticsearch
- `43.03.09` OpenSearch
- `43.03.10` Vespa

### 44. AI Agents and Agentic Systems

*Source tags: Advanced and rapidly evolving area*

#### 44.1 Agent fundamentals

- `44.01.01` What is an AI agent?
- `44.01.02` Agent vs chatbot
- `44.01.03` Autonomous agents
- `44.01.04` Goals
- `44.01.05` State
- `44.01.06` Memory
- `44.01.07` Planning
- `44.01.08` Reasoning
- `44.01.09` Action selection
- `44.01.10` Tool usage
- `44.01.11` Environment interaction

#### 44.2 Agent architectures

- `44.02.01` ReAct
- `44.02.02` Plan-and-execute
- `44.02.03` Reflection
- `44.02.04` Hierarchical agents
- `44.02.05` Supervisor-worker
- `44.02.06` Multi-agent systems
- `44.02.07` Agent swarms
- `44.02.08` Workflow-based agents
- `44.02.09` Event-driven agents

#### 44.3 Agent capabilities

- `44.03.01` Tool calling
- `44.03.02` Function calling
- `44.03.03` Browser interaction
- `44.03.04` Code execution
- `44.03.05` Database queries
- `44.03.06` API invocation
- `44.03.07` File handling
- `44.03.08` Memory retrieval
- `44.03.09` Task decomposition
- `44.03.10` Planning and scheduling
- `44.03.11` Human approval
- `44.03.12` Long-running tasks

#### 44.4 Agent engineering

- `44.04.01` Agent orchestration
- `44.04.02` Agent state management
- `44.04.03` Context management
- `44.04.04` Memory systems
- `44.04.05` Checkpointing
- `44.04.06` Agent evaluation
- `44.04.07` Tool reliability
- `44.04.08` Permission boundaries
- `44.04.09` Sandboxing
- `44.04.10` Human-in-the-loop
- `44.04.11` Prompt injection defense
- `44.04.12` Observability
- `44.04.13` Cost management

#### 44.5 Agent frameworks and ecosystems

- `44.05.01` LangChain
- `44.05.02` LangGraph
- `44.05.03` LlamaIndex
- `44.05.04` Semantic Kernel
- `44.05.05` AutoGen
- `44.05.06` CrewAI
- `44.05.07` Haystack
- `44.05.08` DSPy
- `44.05.09` OpenAI Agents SDK

#### 44.6 Agent interoperability

- `44.06.01` Model Context Protocol (MCP)
- `44.06.02` Agent-to-agent communication
- `44.06.03` Tool discovery
- `44.06.04` Structured tool interfaces
- `44.06.05` Agent identity
- `44.06.06` Delegation and authorization
- `44.06.07` Interoperability standards

### 45. AI Engineering and MLOps

#### 45.1 Core topics *(synthesized heading)*

- `45.01.01` Model training pipelines
- `45.01.02` Dataset management
- `45.01.03` Experiment tracking
- `45.01.04` Model versioning
- `45.01.05` Model registries
- `45.01.06` Model deployment
- `45.01.07` Model serving
- `45.01.08` Batch inference
- `45.01.09` Online inference
- `45.01.10` GPU scheduling
- `45.01.11` Feature stores
- `45.01.12` Data drift
- `45.01.13` Concept drift
- `45.01.14` Model monitoring
- `45.01.15` Model evaluation
- `45.01.16` Model retraining
- `45.01.17` Pipeline orchestration

#### 45.2 Advanced topics

- `45.02.01` Distributed training
- `45.02.02` GPU clusters
- `45.02.03` Parameter servers
- `45.02.04` Training optimization
- `45.02.05` Model compression
- `45.02.06` Quantization
- `45.02.07` Distillation
- `45.02.08` Serving optimization
- `45.02.09` Model caching
- `45.02.10` Inference routing
- `45.02.11` LLM gateways
- `45.02.12` Guardrails
- `45.02.13` Red teaming
- `45.02.14` AI security
- `45.02.15` AI observability
- `45.02.16` LLMOps
- `45.02.17` Evaluation-driven development

#### 45.3 AI tooling

- `45.03.01` MLflow
- `45.03.02` Kubeflow
- `45.03.03` Ray
- `45.03.04` Weights & Biases
- `45.03.05` DVC
- `45.03.06` Hugging Face
- `45.03.07` BentoML
- `45.03.08` KServe
- `45.03.09` Seldon
- `45.03.10` NVIDIA Triton
- `45.03.11` vLLM
- `45.03.12` Ollama
- `45.03.13` LiteLLM
- `45.03.14` Langfuse
- `45.03.15` Arize
- `45.03.16` Evidently

### 46. Responsible AI, AI Safety and AI Governance

#### 46.1 Core topics *(synthesized heading)*

- `46.01.01` Fairness
- `46.01.02` Bias detection
- `46.01.03` Transparency
- `46.01.04` Explainability
- `46.01.05` Interpretability
- `46.01.06` Privacy
- `46.01.07` Data protection
- `46.01.08` Model accountability
- `46.01.09` Robustness
- `46.01.10` Reliability
- `46.01.11` Adversarial testing
- `46.01.12` Model security
- `46.01.13` Hallucination assessment
- `46.01.14` Content safety
- `46.01.15` Copyright and data provenance
- `46.01.16` Human oversight
- `46.01.17` AI auditability
- `46.01.18` Model documentation
- `46.01.19` Dataset documentation
- `46.01.20` Risk assessment
- `46.01.21` AI governance
- `46.01.22` AI compliance
- `46.01.23` AI lifecycle management

> NIST's AI Risk Management Framework and its Generative AI Profile are useful reference points for the trustworthy development, deployment and evaluation of AI systems.

## PART X — SPECIALIZED SOFTWARE ENGINEERING DOMAINS

### 47. Game Development

#### 47.1 Core topics *(synthesized heading)*

- `47.01.01` Game programming fundamentals
- `47.01.02` Game loops
- `47.01.03` Input handling
- `47.01.04` Game physics
- `47.01.05` Collision detection
- `47.01.06` Animation
- `47.01.07` Character controllers
- `47.01.08` Scene management
- `47.01.09` Game AI
- `47.01.10` Pathfinding
- `47.01.11` Multiplayer networking
- `47.01.12` Game state management
- `47.01.13` Game asset pipelines
- `47.01.14` Rendering
- `47.01.15` Game optimization
- `47.01.16` Game testing
- `47.01.17` Game distribution

#### 47.2 Graphics and rendering

- `47.02.01` 2D graphics
- `47.02.02` 3D graphics
- `47.02.03` Coordinate systems
- `47.02.04` Vectors and matrices
- `47.02.05` Transformations
- `47.02.06` Camera systems
- `47.02.07` Rasterization
- `47.02.08` Shaders
- `47.02.09` Lighting
- `47.02.10` Materials
- `47.02.11` Textures
- `47.02.12` Ray tracing
- `47.02.13` Global illumination
- `47.02.14` Physically based rendering
- `47.02.15` Real-time rendering
- `47.02.16` GPU programming

#### 47.3 Game engines

- `47.03.01` **Unity** — 2D, 3D and mobile games
- `47.03.02` **Unreal Engine** — Advanced real-time 3D
- `47.03.03` Godot
- `47.03.04` GameMaker
- `47.03.05` Defold
- `47.03.06` CryEngine
- `47.03.07` O3DE
- `47.03.08` Bevy

### 48. AR, VR, MR and Spatial Computing

#### 48.1 Core topics *(synthesized heading)*

- `48.01.01` Augmented reality
- `48.01.02` Virtual reality
- `48.01.03` Mixed reality
- `48.01.04` Extended reality
- `48.01.05` Spatial computing
- `48.01.06` 3D object tracking
- `48.01.07` Motion tracking
- `48.01.08` Hand tracking
- `48.01.09` Eye tracking
- `48.01.10` Spatial mapping
- `48.01.11` Pose estimation
- `48.01.12` SLAM
- `48.01.13` 3D interaction
- `48.01.14` Haptic interfaces
- `48.01.15` Spatial audio
- `48.01.16` Immersive user interfaces
- `48.01.17` Digital twins
- `48.01.18` Metaverse technologies
- `48.01.19` WebXR
- `48.01.20` OpenXR

### 49. Embedded Systems and Firmware Engineering

#### 49.1 Core topics *(synthesized heading)*

- `49.01.01` Digital electronics
- `49.01.02` Microprocessors
- `49.01.03` Microcontrollers
- `49.01.04` Firmware
- `49.01.05` C programming
- `49.01.06` C++ programming
- `49.01.07` Assembly
- `49.01.08` Memory-mapped I/O
- `49.01.09` GPIO
- `49.01.10` Interrupts
- `49.01.11` Timers
- `49.01.12` ADC
- `49.01.13` DAC
- `49.01.14` UART
- `49.01.15` SPI
- `49.01.16` I2C
- `49.01.17` CAN
- `49.01.18` USB
- `49.01.19` PWM
- `49.01.20` DMA
- `49.01.21` Bootloaders
- `49.01.22` Device drivers
- `49.01.23` RTOS
- `49.01.24` Embedded Linux
- `49.01.25` Firmware updates
- `49.01.26` Secure boot
- `49.01.27` Hardware debugging
- `49.01.28` Power management
- `49.01.29` Real-time constraints

#### 49.2 Hardware platforms

- `49.02.01` Arduino
- `49.02.02` ESP32
- `49.02.03` Raspberry Pi
- `49.02.04` STM32
- `49.02.05` ARM Cortex-M
- `49.02.06` RISC-V microcontrollers
- `49.02.07` BeagleBone
- `49.02.08` NVIDIA Jetson
- `49.02.09` FPGA development boards

### 50. Internet of Things (IoT)

#### 50.1 Core topics *(synthesized heading)*

- `50.01.01` Connected devices
- `50.01.02` Sensors
- `50.01.03` Actuators
- `50.01.04` Edge devices
- `50.01.05` Device communication
- `50.01.06` MQTT
- `50.01.07` CoAP
- `50.01.08` HTTP
- `50.01.09` BLE
- `50.01.10` Zigbee
- `50.01.11` Z-Wave
- `50.01.12` LoRaWAN
- `50.01.13` NB-IoT
- `50.01.14` Device provisioning
- `50.01.15` Device identity
- `50.01.16` Device management
- `50.01.17` IoT gateways
- `50.01.18` Edge computing
- `50.01.19` Telemetry
- `50.01.20` IoT analytics
- `50.01.21` Remote updates
- `50.01.22` IoT security
- `50.01.23` Industrial IoT

### 51. Robotics and Autonomous Systems

#### 51.1 Core topics *(synthesized heading)*

- `51.01.01` Robotics fundamentals
- `51.01.02` Robot architecture
- `51.01.03` Mechanical systems
- `51.01.04` Sensors
- `51.01.05` Actuators
- `51.01.06` Kinematics
- `51.01.07` Forward kinematics
- `51.01.08` Inverse kinematics
- `51.01.09` Dynamics
- `51.01.10` Motion planning
- `51.01.11` Path planning
- `51.01.12` Control systems
- `51.01.13` PID controllers
- `51.01.14` SLAM
- `51.01.15` Computer vision
- `51.01.16` Localization
- `51.01.17` Mapping
- `51.01.18` Sensor fusion
- `51.01.19` Robot operating systems
- `51.01.20` Autonomous navigation
- `51.01.21` Manipulation
- `51.01.22` Human-robot interaction

#### 51.2 Advanced topics

- `51.02.01` Autonomous vehicles
- `51.02.02` Swarm robotics
- `51.02.03` Multi-robot coordination
- `51.02.04` Reinforcement learning for robotics
- `51.02.05` Robot foundation models
- `51.02.06` Vision-language-action models
- `51.02.07` Embodied AI
- `51.02.08` Humanoid robotics

### 52. Blockchain and Web3

#### 52.1 Core topics *(synthesized heading)*

- `52.01.01` Distributed ledgers
- `52.01.02` Blockchain fundamentals
- `52.01.03` Hashing
- `52.01.04` Digital signatures
- `52.01.05` Public and private keys
- `52.01.06` Wallets
- `52.01.07` Cryptocurrency
- `52.01.08` Consensus algorithms
- `52.01.09` Proof of Work
- `52.01.10` Proof of Stake
- `52.01.11` Smart contracts
- `52.01.12` Ethereum
- `52.01.13` Solidity
- `52.01.14` EVM
- `52.01.15` Web3 development
- `52.01.16` Decentralized applications
- `52.01.17` Token standards
- `52.01.18` NFTs
- `52.01.19` Decentralized finance
- `52.01.20` Oracles
- `52.01.21` Layer 1 blockchains
- `52.01.22` Layer 2 scaling
- `52.01.23` Sidechains
- `52.01.24` Cross-chain protocols
- `52.01.25` Decentralized identity
- `52.01.26` Zero-knowledge proofs
- `52.01.27` Blockchain privacy
- `52.01.28` Smart contract auditing
- `52.01.29` Decentralized storage
- `52.01.30` Distributed governance

### 53. High-Performance Computing (HPC)

#### 53.1 Core topics *(synthesized heading)*

- `53.01.01` Scientific computing
- `53.01.02` Numerical simulation
- `53.01.03` Parallel processing
- `53.01.04` Multithreading
- `53.01.05` SIMD
- `53.01.06` Vectorization
- `53.01.07` GPU computing
- `53.01.08` CUDA
- `53.01.09` OpenCL
- `53.01.10` OpenMP
- `53.01.11` MPI
- `53.01.12` Distributed computing
- `53.01.13` Cluster computing
- `53.01.14` Supercomputing
- `53.01.15` High-speed interconnects
- `53.01.16` Memory optimization
- `53.01.17` Parallel algorithms
- `53.01.18` Scientific visualization
- `53.01.19` Performance modeling
- `53.01.20` Distributed training
- `53.01.21` Large-scale simulation

### 54. Quantum Computing

*Source tags: Frontier computing*

This is a substantial specialization of its own. It is not just another programming framework.

#### 54.1 Prerequisite foundations

- `54.01.01` Linear algebra
- `54.01.02` Complex numbers
- `54.01.03` Probability
- `54.01.04` Matrix operations
- `54.01.05` Tensor products
- `54.01.06` Basic quantum mechanics
- `54.01.07` Vector spaces
- `54.01.08` Hilbert spaces

#### 54.2 Quantum fundamentals

- `54.02.01` Classical bits vs qubits
- `54.02.02` Superposition
- `54.02.03` Entanglement
- `54.02.04` Quantum measurement
- `54.02.05` Quantum states
- `54.02.06` Bloch sphere
- `54.02.07` Quantum gates
- `54.02.08` Quantum circuits
- `54.02.09` Quantum interference
- `54.02.10` No-cloning theorem

#### 54.3 Quantum gates

- `54.03.01` Pauli-X
- `54.03.02` Pauli-Y
- `54.03.03` Pauli-Z
- `54.03.04` Hadamard
- `54.03.05` Phase gates
- `54.03.06` T gate
- `54.03.07` CNOT
- `54.03.08` Controlled gates
- `54.03.09` Toffoli
- `54.03.10` SWAP

#### 54.4 Quantum algorithms

- `54.04.01` Deutsch-Jozsa
- `54.04.02` Bernstein-Vazirani
- `54.04.03` Simon's algorithm
- `54.04.04` Grover's algorithm
- `54.04.05` Shor's algorithm
- `54.04.06` Quantum Fourier transform
- `54.04.07` Quantum phase estimation
- `54.04.08` Quantum walks
- `54.04.09` Variational quantum algorithms

#### 54.5 Quantum programming

- `54.05.01` Circuit creation
- `54.05.02` Quantum simulation
- `54.05.03` Circuit optimization
- `54.05.04` Quantum measurement
- `54.05.05` Hybrid quantum-classical programming
- `54.05.06` Quantum algorithm implementation
- `54.05.07` Quantum resource estimation

#### 54.6 Quantum software ecosystems

- `54.06.01` Qiskit
- `54.06.02` Cirq
- `54.06.03` PennyLane
- `54.06.04` Amazon Braket
- `54.06.05` CUDA-Q
- `54.06.06` Q#

#### 54.7 Quantum hardware

- `54.07.01` Superconducting qubits
- `54.07.02` Trapped-ion systems
- `54.07.03` Neutral atoms
- `54.07.04` Photonic quantum computing
- `54.07.05` Spin qubits
- `54.07.06` Quantum annealing
- `54.07.07` Quantum processors
- `54.07.08` Quantum control systems
- `54.07.09` Quantum networking

#### 54.8 Advanced quantum engineering

- `54.08.01` Quantum error correction
- `54.08.02` Logical qubits
- `54.08.03` Surface codes
- `54.08.04` Fault-tolerant quantum computing
- `54.08.05` Error mitigation
- `54.08.06` Quantum circuit compilation
- `54.08.07` Quantum-classical integration
- `54.08.08` Quantum resource optimization
- `54.08.09` Distributed quantum computing
- `54.08.10` Quantum machine learning
- `54.08.11` Quantum simulation

#### 54.9 Closely related but distinct: post-quantum cryptography

- `54.09.01` Quantum-resistant cryptography
- `54.09.02` Lattice-based cryptography
- `54.09.03` Hash-based signatures
- `54.09.04` Code-based cryptography
- `54.09.05` Post-quantum key exchange
- `54.09.06` Cryptographic migration
- `54.09.07` Crypto agility

> One important distinction: quantum computing uses quantum hardware to process certain classes of problems; post-quantum cryptography uses conventional computers to implement cryptographic methods designed to resist quantum attacks.

> IBM's published roadmap, for example, discusses quantum error-correction development, hybrid quantum-classical workflows and fault-tolerant systems as milestones in the 2026–2030 period. These are company targets, not guaranteed delivery dates.

### 55. Edge Computing and Fog Computing

#### 55.1 Core topics *(synthesized heading)*

- `55.01.01` Edge architecture
- `55.01.02` Fog computing
- `55.01.03` Edge devices
- `55.01.04` Edge gateways
- `55.01.05` Distributed processing
- `55.01.06` Edge AI
- `55.01.07` Edge inference
- `55.01.08` Edge storage
- `55.01.09` Edge networking
- `55.01.10` Latency-sensitive applications
- `55.01.11` Offline-first systems
- `55.01.12` Edge orchestration
- `55.01.13` Edge security
- `55.01.14` Edge-cloud integration

### 56. Bioinformatics and Computational Biology

#### 56.1 Core topics *(synthesized heading)*

- `56.01.01` Biological data formats
- `56.01.02` DNA and RNA sequence analysis
- `56.01.03` Genomics
- `56.01.04` Proteomics
- `56.01.05` Sequence alignment
- `56.01.06` Genome assembly
- `56.01.07` Gene expression analysis
- `56.01.08` Protein structure prediction
- `56.01.09` Computational drug discovery
- `56.01.10` Molecular simulation
- `56.01.11` Biological databases
- `56.01.12` Machine learning for biology
- `56.01.13` Biomedical data engineering

### 57. Other Specialized Domains

Software engineers can also work in fields where software intersects with another industry.

#### 57.1 FinTech

- `57.01.01` Digital payments
- `57.01.02` Banking systems
- `57.01.03` Trading platforms
- `57.01.04` Risk engines
- `57.01.05` Fraud detection
- `57.01.06` Financial data processing
- `57.01.07` Regulatory reporting

#### 57.2 HealthTech

- `57.02.01` Electronic health records
- `57.02.02` Medical imaging
- `57.02.03` Clinical software
- `57.02.04` Hospital information systems
- `57.02.05` Health data interoperability
- `57.02.06` Medical AI

#### 57.3 Automotive software

- `57.03.01` Vehicle operating systems
- `57.03.02` ECU programming
- `57.03.03` CAN bus
- `57.03.04` ADAS
- `57.03.05` Autonomous driving
- `57.03.06` Automotive cybersecurity
- `57.03.07` Functional safety

#### 57.4 Aerospace software

- `57.04.01` Flight software
- `57.04.02` Real-time control systems
- `57.04.03` Navigation systems
- `57.04.04` Satellite software
- `57.04.05` Space communications
- `57.04.06` Mission-critical systems

#### 57.5 Telecommunications

- `57.05.01` Mobile core networks
- `57.05.02` Radio access networks
- `57.05.03` Network orchestration
- `57.05.04` 5G and 6G
- `57.05.05` Network slicing
- `57.05.06` Software-defined networking

#### 57.6 Geospatial computing

- `57.06.01` Geographic information systems
- `57.06.02` GIS
- `57.06.03` Spatial databases
- `57.06.04` Remote sensing
- `57.06.05` Satellite imagery
- `57.06.06` Geospatial analytics
- `57.06.07` GPS and positioning systems

#### 57.7 Industrial software

- `57.07.01` PLC programming
- `57.07.02` SCADA
- `57.07.03` Industrial automation
- `57.07.04` Robotics
- `57.07.05` Digital twins
- `57.07.06` Industrial IoT
- `57.07.07` Manufacturing execution systems

#### 57.8 Other areas

- `57.08.01` Education technology
- `57.08.02` Legal technology
- `57.08.03` Retail technology
- `57.08.04` Logistics
- `57.08.05` Supply-chain software
- `57.08.06` Agriculture technology
- `57.08.07` Energy software
- `57.08.08` Climate technology
- `57.08.09` Scientific computing
- `57.08.10` Computational finance
- `57.08.11` Digital identity

## PART XI — AI-ASSISTED SOFTWARE ENGINEERING

### 58. AI Tools Used by Modern Software Engineers

This deserves its own category because AI is changing how engineers write, review, test and maintain software.

#### 58.1 AI-powered coding assistance

- `58.01.01` Code completion
- `58.01.02` Code explanation
- `58.01.03` Code generation
- `58.01.04` Refactoring assistance
- `58.01.05` Documentation generation
- `58.01.06` Test generation
- `58.01.07` Debugging assistance
- `58.01.08` Code review assistance

#### 58.2 AI coding tools

- `58.02.01` GitHub Copilot
- `58.02.02` Cursor
- `58.02.03` Windsurf
- `58.02.04` Claude Code
- `58.02.05` OpenAI Codex
- `58.02.06` Gemini Code Assist
- `58.02.07` Amazon Q Developer
- `58.02.08` JetBrains AI Assistant
- `58.02.09` Continue
- `58.02.10` Aider

#### 58.3 AI-assisted engineering workflows

- `58.03.01` Natural-language specifications
- `58.03.02` Codebase understanding
- `58.03.03` Repository-level reasoning
- `58.03.04` Automated bug fixing
- `58.03.05` Automated test creation
- `58.03.06` Documentation maintenance
- `58.03.07` PR review
- `58.03.08` Refactoring
- `58.03.09` Dependency updates
- `58.03.10` CI failure analysis

#### 58.4 Advanced agentic development

- `58.04.01` Autonomous coding agents
- `58.04.02` Multi-file changes
- `58.04.03` Repository exploration
- `58.04.04` Tool-using agents
- `58.04.05` Parallel agent execution
- `58.04.06` Agent orchestration
- `58.04.07` Code verification
- `58.04.08` Test-driven AI development
- `58.04.09` Sandboxed execution
- `58.04.10` Human approval
- `58.04.11` Change validation
- `58.04.12` Agent evaluation

#### 58.5 The engineer's responsibilities in AI-assisted development

- `58.05.01` Verify generated code
- `58.05.02` Check correctness
- `58.05.03` Validate dependencies
- `58.05.04` Review security
- `58.05.05` Evaluate performance
- `58.05.06` Check licensing
- `58.05.07` Test edge cases
- `58.05.08` Understand system architecture
- `58.05.09` Maintain accountability for shipped software

> AI tools can accelerate engineering work, but understanding the system and validating the output remain essential.

## PART XII — PROFESSIONAL ENGINEERING PRACTICES

### 59. Engineering Standards and Software Quality

#### 59.1 Core topics *(synthesized heading)*

- `59.01.01` Coding standards
- `59.01.02` Naming conventions
- `59.01.03` Style guides
- `59.01.04` Code readability
- `59.01.05` Code maintainability
- `59.01.06` Code review standards
- `59.01.07` API design standards
- `59.01.08` Documentation standards
- `59.01.09` Versioning standards
- `59.01.10` Architecture standards
- `59.01.11` Accessibility standards
- `59.01.12` Security standards
- `59.01.13` Performance standards
- `59.01.14` Reliability standards
- `59.01.15` Software quality models
- `59.01.16` Quality assurance processes
- `59.01.17` Quality metrics

### 60. Software Configuration and Release Management

#### 60.1 Core topics *(synthesized heading)*

- `60.01.01` Configuration management
- `60.01.02` Environment management
- `60.01.03` Version management
- `60.01.04` Dependency management
- `60.01.05` Build reproducibility
- `60.01.06` Artifact storage
- `60.01.07` Release planning
- `60.01.08` Release automation
- `60.01.09` Semantic versioning
- `60.01.10` Feature flags
- `60.01.11` Feature toggles
- `60.01.12` Database migrations
- `60.01.13` Backward compatibility
- `60.01.14` Deprecation management
- `60.01.15` Rollback management
- `60.01.16` Change management
- `60.01.17` Software distribution

### 61. Engineering Economics

#### 61.1 Core topics *(synthesized heading)*

- `61.01.01` Project cost estimation
- `61.01.02` Development cost
- `61.01.03` Infrastructure cost
- `61.01.04` Total cost of ownership
- `61.01.05` Technical debt economics
- `61.01.06` Build vs buy decisions
- `61.01.07` Cost-benefit analysis
- `61.01.08` Return on investment
- `61.01.09` Cloud cost optimization
- `61.01.10` FinOps
- `61.01.11` Licensing
- `61.01.12` Open-source economics
- `61.01.13` Vendor management
- `61.01.14` Capacity planning
- `61.01.15` Resource allocation

### 62. Software Ethics, Law and Governance

#### 62.1 Core topics *(synthesized heading)*

- `62.01.01` Professional ethics
- `62.01.02` Data privacy
- `62.01.03` Intellectual property
- `62.01.04` Software licensing
- `62.01.05` Open-source licenses
- `62.01.06` Copyright
- `62.01.07` Patents
- `62.01.08` Trademarks
- `62.01.09` Data ownership
- `62.01.10` Consent
- `62.01.11` Digital accessibility
- `62.01.12` Algorithmic fairness
- `62.01.13` AI ethics
- `62.01.14` Data governance
- `62.01.15` Regulatory compliance
- `62.01.16` Security governance
- `62.01.17` Responsible software development
- `62.01.18` Environmental sustainability
- `62.01.19` Green software engineering

### 63. Technical Communication and Leadership

#### 63.1 Core topics *(synthesized heading)*

- `63.01.01` Technical writing
- `63.01.02` Documentation
- `63.01.03` Requirement discussions
- `63.01.04` Design reviews
- `63.01.05` Code reviews
- `63.01.06` Technical presentations
- `63.01.07` Problem-solving
- `63.01.08` Team collaboration
- `63.01.09` Cross-functional communication
- `63.01.10` Stakeholder management
- `63.01.11` Conflict resolution
- `63.01.12` Mentoring
- `63.01.13` Knowledge sharing
- `63.01.14` Technical leadership
- `63.01.15` Engineering management
- `63.01.16` Architecture leadership
- `63.01.17` Technical decision-making

### 64. Research and Advanced Computer Science

These subjects are particularly relevant for research engineers, systems researchers, compiler engineers, AI researchers and academics.

#### 64.1 Core topics *(synthesized heading)*

- `64.01.01` Computability theory
- `64.01.02` Automata theory
- `64.01.03` Formal languages
- `64.01.04` Complexity theory
- `64.01.05` Formal methods
- `64.01.06` Model checking
- `64.01.07` Theorem proving
- `64.01.08` Program verification
- `64.01.09` Type theory
- `64.01.10` Category theory
- `64.01.11` Programming language semantics
- `64.01.12` Compiler research
- `64.01.13` Algorithm research
- `64.01.14` Distributed algorithms
- `64.01.15` Cryptographic research
- `64.01.16` Information theory
- `64.01.17` Machine learning theory
- `64.01.18` Statistical learning theory
- `64.01.19` Neural network theory
- `64.01.20` Quantum information theory
- `64.01.21` Quantum algorithms
- `64.01.22` Computational complexity
- `64.01.23` Neuromorphic computing
- `64.01.24` Photonic computing
- `64.01.25` Novel hardware architectures

## PART XIII — COMPLETE TECHNOLOGY ECOSYSTEM CHECKLIST

This section brings together the tools, platforms and technology families that a software engineer may encounter in practice.

### Programming

- `P13.01.01` Python
- `P13.01.02` Java
- `P13.01.03` C++
- `P13.01.04` Go
- `P13.01.05` Rust
- `P13.01.06` JavaScript

### Frontend

- `P13.02.01` React
- `P13.02.02` Angular
- `P13.02.03` Vue
- `P13.02.04` Svelte

### Backend

- `P13.03.01` Spring Boot
- `P13.03.02` Django
- `P13.03.03` FastAPI
- `P13.03.04` Express
- `P13.03.05` NestJS

### Mobile

- `P13.04.01` Android
- `P13.04.02` iOS
- `P13.04.03` Flutter
- `P13.04.04` React Native

### Desktop

- `P13.05.01` Electron
- `P13.05.02` Tauri
- `P13.05.03` Qt
- `P13.05.04` .NET

### Databases

- `P13.06.01` PostgreSQL
- `P13.06.02` MySQL
- `P13.06.03` MongoDB
- `P13.06.04` Redis

### Search

- `P13.07.01` Elasticsearch
- `P13.07.02` OpenSearch
- `P13.07.03` Solr

### Vector databases

- `P13.08.01` Milvus
- `P13.08.02` Qdrant
- `P13.08.03` Weaviate
- `P13.08.04` Pinecone

### Messaging

- `P13.09.01` Kafka
- `P13.09.02` RabbitMQ
- `P13.09.03` Pulsar
- `P13.09.04` NATS

### Data engineering

- `P13.10.01` Spark
- `P13.10.02` Flink
- `P13.10.03` Airflow
- `P13.10.04` dbt

### Analytics

- `P13.11.01` Power BI
- `P13.11.02` Tableau
- `P13.11.03` Superset

### AI/ML

- `P13.12.01` PyTorch
- `P13.12.02` TensorFlow
- `P13.12.03` JAX
- `P13.12.04` scikit-learn

### LLM development

- `P13.13.01` Hugging Face
- `P13.13.02` LangChain
- `P13.13.03` LangGraph
- `P13.13.04` LlamaIndex

### AI inference

- `P13.14.01` vLLM
- `P13.14.02` TensorRT
- `P13.14.03` Ollama

### Game development

- `P13.15.01` Unity
- `P13.15.02` Unreal
- `P13.15.03` Godot

### Graphics

- `P13.16.01` OpenGL
- `P13.16.02` Vulkan
- `P13.16.03` DirectX
- `P13.16.04` WebGPU

### Embedded

- `P13.17.01` Arduino
- `P13.17.02` ESP32
- `P13.17.03` STM32
- `P13.17.04` FreeRTOS

### Robotics

- `P13.18.01` ROS 2
- `P13.18.02` Gazebo
- `P13.18.03` MoveIt

### Blockchain

- `P13.19.01` Ethereum
- `P13.19.02` Solidity
- `P13.19.03` Hyperledger

### Quantum

- `P13.20.01` Qiskit
- `P13.20.02` Cirq
- `P13.20.03` PennyLane
- `P13.20.04` Q#

### Cloud

- `P13.21.01` AWS
- `P13.21.02` Azure
- `P13.21.03` Google Cloud

### Containers

- `P13.22.01` Docker
- `P13.22.02` Podman
- `P13.22.03` containerd

### Orchestration

- `P13.23.01` Kubernetes
- `P13.23.02` OpenShift
- `P13.23.03` Nomad

### Infrastructure as Code

- `P13.24.01` Terraform
- `P13.24.02` OpenTofu
- `P13.24.03` Pulumi

### Configuration management

- `P13.25.01` Ansible
- `P13.25.02` Chef
- `P13.25.03` Puppet

### CI/CD

- `P13.26.01` Jenkins
- `P13.26.02` GitHub Actions
- `P13.26.03` GitLab CI

### GitOps

- `P13.27.01` Argo CD
- `P13.27.02` Flux CD

### Monitoring

- `P13.28.01` Prometheus
- `P13.28.02` Grafana
- `P13.28.03` Datadog

### Logging

- `P13.29.01` Loki
- `P13.29.02` ELK
- `P13.29.03` OpenSearch

### Tracing

- `P13.30.01` OpenTelemetry
- `P13.30.02` Jaeger
- `P13.30.03` Tempo

### Testing

- `P13.31.01` PyTest
- `P13.31.02` JUnit
- `P13.31.03` Jest
- `P13.31.04` Playwright

### Security

- `P13.32.01` OWASP
- `P13.32.02` Snyk
- `P13.32.03` Semgrep
- `P13.32.04` Trivy

### API development

- `P13.33.01` Postman
- `P13.33.02` Swagger
- `P13.33.03` Insomnia

### Operating systems

- `P13.34.01` Linux
- `P13.34.02` Windows
- `P13.34.03` macOS
- `P13.34.04` Unix

### Developer environments

- `P13.35.01` VS Code
- `P13.35.02` IntelliJ
- `P13.35.03` Vim
- `P13.35.04` Neovim

### Collaboration

- `P13.36.01` Jira
- `P13.36.02` Linear
- `P13.36.03` Confluence
- `P13.36.04` Slack

### Documentation

- `P13.37.01` Markdown
- `P13.37.02` Docusaurus
- `P13.37.03` MkDocs

### Build systems

- `P13.38.01` Maven
- `P13.38.02` Gradle
- `P13.38.03` CMake
- `P13.38.04` Bazel

### Package management

- `P13.39.01` npm
- `P13.39.02` pnpm
- `P13.39.03` pip
- `P13.39.04` Poetry
- `P13.39.05` Cargo

### AI coding

- `P13.40.01` Copilot
- `P13.40.02` Cursor
- `P13.40.03` Codex
- `P13.40.04` Claude Code

### Enterprise systems

- `P13.41.01` SAP
- `P13.41.02` Salesforce
- `P13.41.03` ServiceNow

### Identity

- `P13.42.01` Keycloak
- `P13.42.02` Auth0
- `P13.42.03` Okta

### CDN and edge

- `P13.43.01` Cloudflare
- `P13.43.02` Fastly
- `P13.43.03` Akamai

### Web hosting

- `P13.44.01` Vercel
- `P13.44.02` Netlify
- `P13.44.03` Render
- `P13.44.04` Fly.io

> This is an ecosystem index, not a list of technologies that every engineer must install or master.

## PART XIV — HOW THE ENTIRE FIELD FITS TOGETHER

The following is a simplified map of the relationships between major areas.

### Computer Science Foundations

- `P14.01.01` Mathematics
- `P14.01.02` Logic
- `P14.01.03` Architecture
- `P14.01.04` Algorithms
- `P14.01.05` Operating Systems
- `P14.01.06` Networks

### Programming and Software Engineering

- `P14.02.01` Programming languages
- `P14.02.02` DSA
- `P14.02.03` OOP
- `P14.02.04` Design
- `P14.02.05` Testing
- `P14.02.06` Git
- `P14.02.07` SDLC

### Application Engineering

- `P14.03.01` Frontend
- `P14.03.02` Backend
- `P14.03.03` Mobile
- `P14.03.04` Desktop
- `P14.03.05` APIs

### Systems Engineering

- `P14.04.01` Architecture
- `P14.04.02` Distributed systems
- `P14.04.03` Databases
- `P14.04.04` Networking

### Infrastructure

- `P14.05.01` Cloud
- `P14.05.02` DevOps
- `P14.05.03` Containers
- `P14.05.04` SRE
- `P14.05.05` Security

### Data and Intelligence

- `P14.06.01` Data engineering
- `P14.06.02` Analytics
- `P14.06.03` ML
- `P14.06.04` AI
- `P14.06.05` LLMs

### Advanced and Frontier Computing

- `P14.07.01` AI agents
- `P14.07.02` Robotics
- `P14.07.03` HPC
- `P14.07.04` Quantum
- `P14.07.05` Blockchain
- `P14.07.06` Spatial computing
- `P14.07.07` Emerging hardware

> Professional practices, security, quality, ethics and communication apply across every layer.

## PART XV — THE PRACTICAL LEARNING ORDER

One mistake would be attempting to learn all 64 areas simultaneously. The map is comprehensive, but the depth required in each area depends on your specialization.

### Learning stages *(synthesized heading)*

- `P15.01.01` Stage 1: Computer fundamentals, Linux, mathematics *(target: Beginner)*
- `P15.01.02` Stage 2: One programming language, problem solving *(target: Beginner → Intermediate)*
- `P15.01.03` Stage 3: DSA, OOP, databases, SQL *(target: Intermediate)*
- `P15.01.04` Stage 4: Git, testing, debugging, software engineering *(target: Intermediate)*
- `P15.01.05` Stage 5: Backend, frontend, networking, APIs *(target: Intermediate)*
- `P15.01.06` Stage 6: Architecture, design patterns, system design *(target: Intermediate → Advanced)*
- `P15.01.07` Stage 7: Cloud, Docker, Kubernetes, CI/CD *(target: Advanced)*
- `P15.01.08` Stage 8: Distributed systems, security, SRE *(target: Advanced)*
- `P15.01.09` Stage 9: Data engineering, ML, AI fundamentals *(target: Specialist)*
- `P15.01.10` Stage 10: Deep learning, LLMs, RAG, AI agents *(target: Advanced specialist)*
- `P15.01.11` Stage 11: Robotics, embedded, HPC, blockchain, graphics *(target: Specialist)*
- `P15.01.12` Stage 12: Quantum computing and advanced research *(target: Research/specialist)*

### Engineering roles *(synthesized heading)*

- `P15.02.01` Software Development Engineer — Programming, DSA, databases, architecture, testing
- `P15.02.02` Backend Engineer — Backend, APIs, databases, networking, distributed systems
- `P15.02.03` Frontend Engineer — JavaScript, TypeScript, UI, UX, browser internals
- `P15.02.04` Full-Stack Engineer — Frontend, backend, databases, deployment
- `P15.02.05` Android Engineer — Kotlin, Java, Android SDK, mobile architecture
- `P15.02.06` iOS Engineer — Swift, SwiftUI, UIKit, iOS internals
- `P15.02.07` Systems Engineer — C, C++, Rust, OS, networking, computer architecture
- `P15.02.08` Cloud Engineer — Cloud, networking, Linux, containers, security
- `P15.02.09` DevOps Engineer — CI/CD, cloud, automation, containers, observability
- `P15.02.10` SRE — Distributed systems, reliability, monitoring, automation
- `P15.02.11` Data Engineer — SQL, Python, pipelines, Kafka, Spark, warehouses
- `P15.02.12` Data Scientist — Mathematics, statistics, Python, ML
- `P15.02.13` ML Engineer — ML, deep learning, deployment, MLOps
- `P15.02.14` AI Engineer — LLMs, RAG, agents, evaluation, AI infrastructure
- `P15.02.15` Security Engineer — Cryptography, secure coding, infrastructure and application security
- `P15.02.16` Game Engineer — C++, graphics, physics, game engines
- `P15.02.17` Embedded Engineer — C/C++, electronics, firmware, RTOS
- `P15.02.18` Robotics Engineer — Robotics, control systems, C++, Python, AI
- `P15.02.19` Quantum Software Engineer — Quantum algorithms, linear algebra, quantum SDKs
- `P15.02.20` Compiler Engineer — Compilers, operating systems, language theory, C++ or Rust

> A sensible progression is:

> A software engineer is not expected to master everything in this map.

> Consider these examples:
