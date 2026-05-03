
- some data dependencies can be solved with **register renaming** using a [[15 Pipelining#Reorder buffer|reorder buffer]]
- we can also re-order instructions such that f.ex. instructions with independent values execute before the dependent instruction using reservation stations (assign tags to registers and execute instruction once concrete values are assigned to these tags)

## Tomasulo's Algorithm

→ [[14 Slides.pdf]]

For a given instruction: 

![[Bildschirmfoto 2026-05-02 um 21.47.15.png]]


> [!info]
> **Advantages**
> - latency tolerance
> - dynamically find and use parallelism
> 
> **Disadvantages**
> - complexity (critical path delay)
> - hardware needed

![[Bildschirmfoto 2026-04-18 um 11.56.36.png]]


