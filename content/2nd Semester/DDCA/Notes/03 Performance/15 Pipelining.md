
- Think PProg [[06 Pipelining]]. 
- Divide into stages (Fetch, Decode, Execute, Writeback), each stage different hardware

**Dependency types: 
- **==Read after write==**
- Write after read
- write after write

**Dependencies can be dealt with through the Hardware or Software.** 

*Hardware interlocking*: Given a timeline, a raw dependency can be seen by having the execute of R2 stalled to start only after the writeback of R1 through "-" at given "wait" cycles

*Software interlocking*: nop (no operation) buffer tasks with the full f.ex. F,D,E,M,W are put in the timeline, to push the fetch of the 2nd op back to then have E after W of 1st. 

**Data forwarding**: 
The 2nd instruction gets the value of Execute of the 1st instruction without having to wait for the writeback of 1st instruction. So f.ex. Execute/Memory of 1st passes to Execute of 2nd. We call a "forwarding path" a connection from the pipeline stage (f.ex. M, W, E, E1, E2, etc.) where to a stage (f.ex. E1) in a directly subsequent cycle. We can't pass 2 cycles to the future. 

**Loop counting**
When doing loop counting beware that data dependencies might completely change  the stalls if the part before the loop is only executed at the beginning and not every iteration 

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

---

![[Bildschirmfoto 2026-04-18 um 10.21.25.png]]
![[Bildschirmfoto 2026-04-18 um 10.31.30.png]]

## Problem handling

Problem in the image: We always need ==percice exceptions== (know the exact state of exception). Suppose first operation (DIV) has exception, but ADD did already do the writeback.

![[Bildschirmfoto 2026-04-18 um 11.09.12.png]]

Solution: 

## Reorder buffer 

reorder back before making results visible to architectural state

- RF has (1) value valid (2) value (3) pointer to ROB
- ROB has values (1) value valid (2) dest reg id (3) dest reg value (4) dest reg written. And pointer to oldest and newest instruction.

1. Start: all valid in RF. 
2. Suppose multiply R1, R2, store to R3. Add row to ROB, set valid. Set row in RF to invalid, and point to ROB. Because of pointer, not every row of ROB needs to be searched

<iframe width="560" height="315" src="https://www.youtube.com/embed/TH386wzOXvA?si=v3eDbakgwpQ2hn_I&amp;start=5544" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

## Pipelining Tasks

![[Bildschirmfoto 2026-04-18 um 12.39.41.png]]
![[Bildschirmfoto 2026-04-18 um 12.39.59.png]]
![[Bildschirmfoto 2026-04-18 um 12.45.19.png]]
