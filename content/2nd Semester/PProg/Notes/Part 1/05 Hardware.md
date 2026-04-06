
> [!warning] Not important
> This chapter can be skipped/speedrun, I recommend jumping to [[06 Pipelining]] instead.

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
