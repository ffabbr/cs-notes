
## Introduction to State

- the state is a snapshop of the system at a given moment
- ==state transitions take place at fixed units of time==
- ==clock== is a mechanism that triggers transition frmo one state to another in a sequential circuit
- computation needs to complete before clock cycle ends
- state-elements with clock attached (inputs evaluate, use input when clock ticks)
- pipelining (**with every cycle we get more results which are the inputs to the next cycle**) 


A ==sequential== circuit has a finite set of states. A ==synchronous sequential== circuit has a clock input, whose rising edges indicate a sequence of times where state transitions occur. A circuit is synchronous sequential if

- every element is either register or combinational
- at least one register
- all elements receive the same sigmal
- every cyclic path contains min. one register

If conditions not met, then *asynchronous*. 

![[2nd Semester/DDCA/Slides/03 Slides.pdf#page=136|03 Slides]]

## The FSM

A Finite State Machine is a system that can only be in **one specific condition** (state) at any given time, and it changes states based on specific rules. 

> An FSM with $k$ registers has $2^k$ unique states. 

A computer board needs to process information in a predictable way. FSMs are used to map out exactly how hardware should react to every possible event.

Has
- a finite number of **states**
- a finite number of **inputs**
- a finite numbers of **outputs**
- clock
- optionally reset signal

- ==transitions== (how to get from one state to another)
- an ==output function== ([[#Moore vs Mealy|moore or mealy]]) 

**There are two types of circuits. Most system use a combination of both.**
*Sequential vs Combinational (Combinational vs Sequential)* 

- **==Sequential Circuits== (Memory):** This part uses ==State Registers== to remember the machine's **Current State**. It safely holds this information and only updates to the **Next State** when the ==system clock== (CLK) ticks, keeping everything synchronized.

- ==**Combinational Circuits== (Logic):** Output depends only on current input, as a roolbook. 
    - **Next state logic:** Looks at the current situation and decides what the machine's _next_ state needs to be.
    - **Output logic:** Triggers the actual physical actions or signals the machine needs to perform right now.


![[2nd Semester/DDCA/Slides/03 Slides.pdf#page=140|03 Slides]]

### State register (CLK)

> [!warning] 
> States only change at exactly the rising clock edge.

![[2nd Semester/DDCA/Slides/03 Slides.pdf#page=143]]

### Gated D-Latch (Problems!)

Always when CLK is up, the output reflects the input. ==NOT WANTED==

![[2nd Semester/DDCA/Slides/03 Slides.pdf#page=145]]

---

Solution: → [[03 Storage#D Flip-Flop|D Flip-Flop]] 

---

## Moore vs Mealy

- ==Moore FSM==: output depends only on current state
- ==Mealy FSM==: output depends on current state and inputs

FSM: 

![[Bildschirmfoto 2026-03-07 um 12.28.21.png]]

### Example: 1101 Snail

![[2nd Semester/DDCA/Slides/06 Slides.pdf#page=14]]


## Transition Diagram

![[2nd Semester/DDCA/Slides/03 Slides.pdf#page=162]]
![[2nd Semester/DDCA/Slides/03 Slides.pdf#page=172]]
![[2nd Semester/DDCA/Slides/03 Slides.pdf#page=179]]

![[2nd Semester/DDCA/Slides/03 Slides.pdf#page=183]]
![[2nd Semester/DDCA/Slides/03 Slides.pdf#page=184]]

![[2nd Semester/DDCA/Slides/03 Slides.pdf#page=205]]

---

## Reset State

You ==NEED== to have a reset state, this is where it starts from 

![[05 Verilog#Reset]]


