
## Introduction

- a program using fork/join can be seen as a DAG
- Vertixes: units of work
- Edges: dependencies (source must finish before destination starts)

**fork**
- current node ends, 2 outgoing edges and vertices created. If possible, then in parallel
	1. The newly forked task
	2. The continuation of original task 

**join**
- one node with 2 incoming edges
- 1 edge from the forked task that finished
- 1 edge from continuation of original task that was waiting for the forked task
- program cannot proceed until both incoming branches  complete

![[2nd Semester/PProg/Slides/09 Slides.pdf#page=10]]


## Example, Fibonacci

![[2nd Semester/PProg/Slides/09 Slides.pdf#page=12]]


## Performance Model

### Introduction

$T_{p}$: execution time on P worker threads. This does not necessarily mean physical hardware cores.

To determine how much a program can potentially speed up by running in parallel, the model relies on two critical metrics derived from the DAG. 

Speedup: 
$$
S_{p} = \frac{T_{1}}{T_{p}}
$$

Maximum Parallelism
$$
S_{\infty}= \frac{T_{1}}{T_{\infty}}
$$

**Work:** $T_1$
- execution time if sequentially run 
- on DAG, ==total number of nodes in the entire graph==.

**Span, Critical Path:** $T_{\infty}$
- ==longest chain of dependent operations in the DAG== (tasks that cannot be run simultaneously)

**Width of the Graph**: number of processors to archive $T_{\infty}$, so the maximum speed

![[Bildschirmfoto 2026-03-19 um 14.37.21.png]]

![[2nd Semester/PProg/Slides/09 Slides.pdf#page=20]]

### DAG Bounds

**wide graph**: higher potential parallelism (shorter $T_{\infty}$)
**deep graph**: more dependencies, less speedup

#### Lower bound

**Work law:**
linear speedup
$$
T_p \ge \frac{T_1}{p}
$$

**Span law**
the longest sequential chain determines the time, no matter how many worker threads we have
$$
T_p \ge T_\infty
$$
**Combining Work and Span law:**
$$
T_p \ge \max\left(\frac{T_1}{p}, T_\infty\right)
$$

#### Upper bound

The total time should not exceed the time it takes to do the perfectly divided work ($T_1 / p$) plus the time spent waiting on the critical path's dependencies ($\mathcal{O}(T_\infty)$).

$$
T_p \le \frac{T_1}{p} + \mathcal{O}(T_\infty)
$$

## Execution times with ForkJoin

![[2nd Semester/PProg/Slides/09 Slides.pdf#page=25]]
![[2nd Semester/PProg/Slides/09 Slides.pdf#page=26]]


---

## Asymptotic Bound

Summing an Array: 
- Sequential: $O(n) = T_{1}$
- Parallel: $O(\log n) = T_{\infty} = span$
- Parallelism: $O\left( \frac{n}{\log n} \right)$

## Patterns

Reduction always achieve $O(\log n)$
Map achieves $O(\log n)$ with Divide & Conquer
### Reduction

The dimension (size) of the output is smaller than of the input. We get the output by applying an **associative operator** on all Input entries. 

### Maps

A map applies a function to each element. f.ex. squaring each element of an array

|output| = |input|

**Zip map**: multiple inputs, f.ex. element-wise addition of 2 arrays
**Stencil**: multiple inputs of the same array to calculate the output. f.ex. `O[i] = f(Input[i-1], Input[i])`. 

### Prefix-sum

![[Bildschirmfoto 2026-03-24 um 09.24.12.png]]

![[2nd Semester/PProg/Slides/09 Slides.pdf#page=64]]

`fromLeft = sum_of_left + fromLeft of top`

$O(n)$ work, $O(\log n)$ span

### Pack

Given an array input, produce an array output containing only elements such that f(elt) is true.

Output array hat Elemente aus dem Input mit bestimmen Eigenschaften. Erkennen: [[#Maps]]. In neues Array screiben: [[#Prefix-sum]]. 

![[2nd Semester/PProg/Slides/09 Slides.pdf#page=72]]


## Data structures

For parallelism: **balanced trees / arrays** are better than lists, as we can bet all data in $O(\log n)$ instead of $O(n)$.

![[Bildschirmfoto 2026-03-24 um 09.23.47.png]]


## Example, Quicksort
![[2nd Semester/PProg/Slides/09 Slides.pdf#page=76]]![[2nd Semester/PProg/Slides/09 Slides.pdf#page=77]]h