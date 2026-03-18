
- Modern CPUs exploit parallelism internally (caching, vectorization, ILP, pipelining), even on a single core
- Code structure determines how effective these structures are

## History and Preamble

- Moore's Law: Transistor counts on a chip double approximately every two years
- Until the early 2000s: Shrinking transistors enabled both higher transistor densities and higher clock speeds, directly driving computational power growth

- computer executes one instruction per clock. An instructino describes an operation for a processor to perform (modify the conputer's state)

![[2nd Semester/PProg/Slides/06 Slides.pdf#page=9]]


### Single Core

Instruction level parallelism

![[2nd Semester/PProg/Slides/06 Slides.pdf#page=10]]

These optimizations make control unit more complex: Out of order scheduling, branch prediction, memory prefetching, cache, etc.

But limits: 
- Power consumption and heat 
- ILP wall 
- Memory wall 

So we got 

### Multi Core

Thread level parallelism

![[2nd Semester/PProg/Slides/06 Slides.pdf#page=15]]

We need to parallelize tasks, so **Programmers** must **design software to split work** into independent threads. 

---

## Caching

Von-Neumann-Architektur

![[2nd Semester/PProg/Slides/06 Slides.pdf#page=23]]

> Memory access results in latency → Invention of **Cache**

![[2nd Semester/PProg/Slides/06 Slides.pdf#page=26]]

> [!example] Example, summing an Array
> **Best performance** in **sequential access**, efficient due to cache locality, cache prefetching works 
> 
> **Jumping around** the Array is **Cache-unfiendly**, causing cache misses because prefetching is inefficient

→ a computer has multiple caches. Here each L stands for a cache, f.ex. L1 is 5x fasster than L2, etc.

![[2nd Semester/PProg/Slides/06 Slides.pdf#page=30]]

## Compute optimization

3 Approaches to apply parallelism:

- [[#Vectorization]]
- [[#ILP]]
- [[#Pipelining]] 

### Vectorization

Verschiedene, unabhängige Operationen vom gleichen Typen können parallelisiert werden, durch Optimierungen vom Compiler

> [!info] SIMD
> **SIMD**: Single Instruction, Multiple Data. 
> One instruction broadcasts to multiple ALUs (calculation units)


![[2nd Semester/PProg/Slides/06 Slides.pdf#page=33]]
![[2nd Semester/PProg/Slides/06 Slides.pdf#page=34]]

Compiler sieht Optimizationsmöglichkeiten 

![[2nd Semester/PProg/Slides/06 Slides.pdf#page=37]]


### ILP

Processor finds independent instructions and executes them in parallel ("Superscalar"). 
Independent: result of one instruction isn't input of the other. 
Hardware enables ILP

> **ILP:** Happens on a single thread, so no concurrency.  
> **Multi-threading:** multiple cores

**Combination:** Thread scheduled on a core, ILP to separate on the same thread

**Prefetching**: Preloading instructions into the CPU cache before needed. 

```java
x = a + b; // this and the one below are independent
y = c + d; // can execute these 2 instructions in parallel
z = x * y; // this one depends on results above, so has to wait
```

IPL ==can also **reorder** statements==, if independend from one another. 

> [!abstract] Independent Statements
> Two statemenets are **independent**, if
> - different register names
> - different memory addresses

**Slides**
- [[2nd Semester/PProg/Slides/06 Slides.pdf#page=43|Slide 1]]
- [[2nd Semester/PProg/Slides/06 Slides.pdf#page=46|Slide 2]]
- [[2nd Semester/PProg/Slides/06 Slides.pdf#page=47|Reordering]]

### Pipelining

→ split a "process" into different stages, each with clear function, f.ex. clothing washing process

> [!info] Balenced
> **Balanced pipeline**: all steps require same time

**1. Instruction Fetch**
- CPU reads the instruction from memory
- may prefetch multiple instructions

**2. Instruction Decode**
- decode the instructions, prepare instructions for execution
- instructions are then dispatched to the correct execution units

**3. Execution**
- CPU executes decoded instruction
- Superscalar execution: instructions dispatched to multiple execution units. 
- SIMD: apply one ==s==ingle ==i==nstruction to ==m==ultiple pieces of ==d==ata all at once

**4. Memory Access**
- If needed, exchange data between CPU and memory
- pre-fetching, caching, etc.

**5. Writeback**
- Save the final result of the execution
- outcome of the execution stage is written back into the CPU's registers
- Superscalar Execution: Multiple instructions can write their results back to different registers or memory locations at the same time

#### Throughput

**Throughput** = Menge an Arbeit die wir in bestimmter Zeit machen können ==larger is better==

→ EINHEITEN angeben #exam 

- For a specific number of instances n: $\text{Throughput = (n)/total time}$
- For infinite pipeline (per execution unit)
$$\text{Throughput bound} = \frac{1}{\text{Dauer vom längsten Schritt}}$$

Beispiele: 
-  $t_\text{put} = \frac{1}{3s}$ means 1 instruction per 3s
- 1 Produkt pro 15 min

#### Latency

**Latency** = time needed to perform a given computation. ==lower is better==

- Latency ist nicht konstant, kann sich verändern
- **Latency bound** = (no of stages) $\cdot$ Dauer vom längsten Schritt

- Konstant: nehme einfach erste Instanz `latency = Zeit für erste Instanz` 

- Nicht konstant: `latency = Zeit für erste Instanz + (Längste Stage - Time of first stage) * (n-1)` 

#### Example: unbalanced Pipeline creates waiting delays

Example: washing loads

![[2nd Semester/PProg/Slides/06 Slides.pdf#page=62|06 Slides]]

→ make pipeline balanced by increasing time for each stage to match longest stage

![[2nd Semester/PProg/Slides/06 Slides.pdf#page=64|06 Slides]]

→ add 2 dryers working in a row

![[2nd Semester/PProg/Slides/06 Slides.pdf#page=67|06 Slides]]


---


