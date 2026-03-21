
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
![[2nd Semester/PProg/Slides/09 Slides.pdf#page=14]]


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

**Goals and Motivation**

![[2nd Semester/PProg/Slides/09 Slides.pdf#page=27]]

### DAG Bounds

![[2nd Semester/PProg/Slides/09 Slides.pdf#page=21]]

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

