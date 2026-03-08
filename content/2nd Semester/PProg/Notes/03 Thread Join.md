
**Busy waiting**: Main thread überprüft laufend ob das Resultat der worker-Threads schon da sind. Braucht CPU Zeit.

Ziel: let Main sleep until worker-Thread is done ("join")

![[Bildschirmfoto 2026-02-25 um 18.39.04.png]]

## Java Join

![[2nd Semester/PProg/Slides/01 Slides.pdf#page=54|01 Slides]] 


## Exceptions

![[2nd Semester/PProg/Slides/01 Slides.pdf#page=57|01 Slides]]
![[2nd Semester/PProg/Slides/01 Slides.pdf#page=58|01 Slides]]


## Interrupt Threads

Threads können sich immer nur selbst interrupten. Aber möglich ist ein Interrupt flag, dass der andere Thread lesen und reagieren kann. `Thread.interrupt()`. 
