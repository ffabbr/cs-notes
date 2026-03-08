
Parallel output order changes between runs, because ==console access is random==. 

## Single-Core

![[2nd Semester/PProg/Slides/01 Slides.pdf#page=5]]

- während *waiting for I/O* ist CPU auf idle, was man vermeiden möchte
- CPU scheduler regelt das, verteilt CPU zwischen Prozessen (Prozesse umschalten)

![[2nd Semester/PProg/Slides/01 Slides.pdf#page=7]] 

- processes share CPU, but each process has own memory space

![[2nd Semester/PProg/Slides/01 Slides.pdf#page=10]]

### Every process needs context (PCB)

- hardware context
- memory context
- os-level context

- changing to another process requires a context switch, resulting in large overhead

![[2nd Semester/PProg/Slides/01 Slides.pdf#page=12]]

- swap memory (green) is a lot slower

### OS manages processes

- starts processes
- ends processes
- controls resource usage
- schedules cpu time
- allows inter-process communication

### Context switching

1. P1 is executing
2. capture PCB(1)
3. load PCB(2)
4. P2 is executing

## Prallelism and Concurrency

![[2nd Semester/PProg/Slides/01 Slides.pdf#page=16]]
![[2nd Semester/PProg/Slides/01 Slides.pdf#page=17]]

## Threads

### General

- independent sequences of execution on the same process
- Threads are not shielded from each other
- memory shared
- Context switching between threads is ***efficient*** 

They 
- share heap (memory space)
- have own execution stack 
- have own instruction screen 

![[2nd Semester/PProg/Slides/01 Slides.pdf#page=23]] 
![[2nd Semester/PProg/Slides/01 Slides.pdf#page=25]] 

#### Thread Attributes

![[2nd Semester/PProg/Slides/01 Slides.pdf#page=45]]

### Threads in Java

#### Option 1

![[2nd Semester/PProg/Slides/01 Slides.pdf#page=31]] 
![[2nd Semester/PProg/Slides/01 Slides.pdf#page=32]] 

#### Option 2

![[2nd Semester/PProg/Slides/01 Slides.pdf#page=33]] 
![[2nd Semester/PProg/Slides/01 Slides.pdf#page=34]] 

```java
t1.start();
t2.start();
```

- Threads can continue to run even if main() returns already
- threads need to be started 
- always at least one thread (first one calls `main()`) 

![[2nd Semester/PProg/Slides/01 Slides.pdf#page=36]] 

- the console is shared between all threads, internal mechanisms make sure only one thread read/writes at the same time. who gets ==access is random==

---

## Example
![[2nd Semester/PProg/Slides/01 Slides.pdf#page=41]] ![[Bildschirmfoto 2026-02-23 um 11.55.21.png]]
