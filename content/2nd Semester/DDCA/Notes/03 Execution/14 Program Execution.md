
How we compile and run an application: 

1.  Compiler converts to machine code
2. Assembler replaces variables with addresses
3. Linker creates executable (text segment)

![[Bildschirmfoto 2026-04-16 um 18.22.08.png]]

Memory has **Instructions** and **Data**.

## Instructions

1. Instruction Fetch (IF)
2. Decode and register operand fetch (ID/RF)
3. Execute/Evaluate memory address (EX/AG)
4. Memory operand fetch (MEM)
5. Store result (WB, writeback)

## Interrupts and Exceptions

Interrupts: external cause (f.ex. power failure, IO needed)
Exceptions: internal cause (f.ex. divide by 0)

---

## Optimizations

1. [[#Pipelining]]
2. [[#Fine Grained Multithreading]]
3. [[#Out of order execution]]
4. [[#Dataflow Model]]
5. [[#Superscalar Execution]]

`Execution time = #instructions x average CPI x #clock cycle time`

### Pipelining

- Think PProg [[06 Pipelining]]. 
- Divide into stages (Fetch, Decode, Execute, Writeback), each stage different hardware

**Dependency types: 
- **==Read after write==**
- Write after read
- write after write

Data forwarding: ==write== of prev. inst. can be simulatnious with ==execute== of next with read after write dependency

![[Bildschirmfoto 2026-04-18 um 12.39.41.png]]
![[Bildschirmfoto 2026-04-18 um 12.39.59.png]]
![[Bildschirmfoto 2026-04-18 um 12.45.19.png]]


**Non-pipelined:** 
$$
T_{\text{put}}=\frac{1}{T+S}
$$
S = register (sequential logic) delay

combinational cost G
R = register cost
`Total Cost = G+R`

**k-stage pipelined:**
$$
\begin{align}
T_{\text{put}_{\text{k-stage}}}&=\frac{1}{T/k + S} \\
T_{\text{put}_{\text{max}}}&=\frac{1}{\text{1 Gate delay}+S}
\end{align}
$$

`Cost(k-stage) = G+Rk`

![[Bildschirmfoto 2026-04-18 um 10.21.25.png]]
![[Bildschirmfoto 2026-04-18 um 10.31.30.png]]

#### Problem handling

Problem in the image: We always need ==percice exceptions== (know the exact state of exception). Suppose first operation (DIV) has exception, but ADD did already do the writeback.

![[Bildschirmfoto 2026-04-18 um 11.09.12.png]]

Solution: 

#### Reorder buffer 

reorder back before making results visible to architectural state

- RF has (1) value valid (2) value (3) pointer to ROB
- ROB has values (1) value valid (2) dest reg id (3) dest reg value (4) dest reg written. And pointer to oldest and newest instruction.

2. Start: all valid in RF. 
3. Suppose multiply R1, R2, store to R3. Add row to ROB, set valid. Set row in RF to invalid, and point to ROB. Because of pointer, not every row of ROB needs to be searched

<iframe width="560" height="315" src="https://www.youtube.com/embed/TH386wzOXvA?si=v3eDbakgwpQ2hn_I&amp;start=5544" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Fine Grained Multithreading

...

### Out of order execution

Move the non-ready instructions out of the way of independent ones

> [!info]
> **Advantages**
> - latency tolerance
> - dynamically find and use parallelism
> 
> **Disadvantages**
> - complexity (critical path delay)
> - hardware needed

![[Bildschirmfoto 2026-04-18 um 11.56.36.png]]

→ [[14 Slides.pdf]]
### Dataflow Model

Fetch and execute order: 

**Control flow order**: program counter (instruction pointer) specifies

**==Dataflow model==**: 

- no program counter, 
- **act when ready depending on data flow dependence (when all operands are received)** 
- Instructions can execute at the same time
- Execute computation when all inputs available

- Data Flow at ISA level not successful as programmers would need to adapt
- **Data Flow at microarchitecture very successful**: The order of processing doesn't matter as long as the semantics of ISA are met. But that's not visible to the programmer, the programmer only sees the ISA (f.ex. as in von Neumann).

[[Bildschirmfoto 2026-04-16 um 18.51.51.png|Dataflow Program for factorial]]

> [!error] ISA BASED
> **Advantages**: 
> - use irregular parallelism
> - more parallelism
> 
> **Disadvantages**
> - no precise state semantics
> - large hardware


### Superscalar Execution

Fetch, decode, execute, retrieve multiple instructions at the same time

Processor: `[in order, out of order] x [scalar, superscalar]`

> [!info]
> **Advantages**
> - higher throughput (higher IPC, Instructions per Cycle)
> **Disadvantages**
> - complexity
> - hardware needed

---


![[Bildschirmfoto 2026-04-17 um 15.38.34.png]]