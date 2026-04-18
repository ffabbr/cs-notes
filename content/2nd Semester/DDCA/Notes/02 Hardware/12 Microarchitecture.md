
> [!info] ISA vs Microarchitecture
> **ISA**
> - describes set of instructions that a processor can execute
> - what the processor can do (the instruction set)
> - Specifies: Instructions, Memory, Exception Handling, I/O, Power Management, etc.
> 
> **Microarchitecture**
> - how the processor executes the instructions defined by the ISA
> - defines the specific implementation of a processor based on that ISA
> - pipelining, memory management, parallelism, instruction order
> - anything done in hardware without control by the software


AS = Architectural state **before** processed, visible to programmer
AS' = Architectural state **after** processed, visible to programmer

ISA specifies what AS' should be, Microarchitecture implements state transition

---

Each takes a **single clock cycle** and uses **combinational logic**. But some instructions take longer, so **tune clock-cycle** per longest delay instruction.

**Single-cycle machine**: each instruction = 1 clock cycle, state updates at end of instruction, slowest instruction determines clock speed

**Multi-cycle machine**: multiple cycles/stages, state updates during instruction's execution, can load next instruction already, slowest "stage" determines speed

→ both single-cycle and multi-cycle can be built on top of von Neumann Microarchitecture

---
## Instruction Processing Engine

2 components:

- **Control logic**: hardware to determine control signals (set what datapath should do to data)
- **Datapath**: hardware to transform data signals 

When single-cycle, everything happens in one cycle serialized, in multi-cycle controls needed for next cycle can be generated already

> [!Note]- Performance Analysis
> ![[2nd Semester/DDCA/Slides/10 Slides.pdf#page=21]]


---

## Design Principles

- decrease maximum combinational logic array
- spend ressources on where it matters most
- balance through hardware
- keep it simple (kiss)
- keep it low cost

---

## Single-cycle 

- every instruction takes exactly **one clock cycle** to complete
- clock speed as slow as slowest instruction (f.ex. ld word)
- needs to replicate ressource if needed more than once
- CPI  = 1, but slow

> [!note]- Slides
> 
> ### Preparation
> 
> ![[2nd Semester/DDCA/Slides/10 Slides.pdf#page=24]]
> 
> Structure (plan):
> 
> ![[2nd Semester/DDCA/Slides/10 Slides.pdf#page=28]]
> 
> ### Datapath 
> 
> R-Type MIPS: 
> 
> ![[Bildschirmfoto 2026-04-16 um 19.46.15.png]]
> 
> ![[2nd Semester/DDCA/Slides/10 Slides.pdf#page=34]]
> 
> I-Type MIPS: 
> 
> ![[Bildschirmfoto 2026-04-16 um 19.46.43.png]]
> 
> R and I Type ALU Instructions
> 
> ![[2nd Semester/DDCA/Slides/10 Slides.pdf#page=37]]
> 
> ### Load Word
> 
> ![[2nd Semester/DDCA/Slides/10 Slides.pdf#page=41]]
> 
> ### Store Word
> 
> ![[2nd Semester/DDCA/Slides/10 Slides.pdf#page=45]]
> 
> ### Jump
> 
> ![[2nd Semester/DDCA/Slides/10 Slides.pdf#page=47]]
> 
> ![[2nd Semester/DDCA/Slides/10 Slides.pdf#page=48]]
> 
> ### Branch if Equal
> 
> ![[2nd Semester/DDCA/Slides/10 Slides.pdf#page=53]]


## Multi-cycle

- each instruction should take just as much time as needed
- isntructions can take mulitple cycles
- execution of an instruction is broken down into smaller, distinct stages (f.ex. Fetch, Decode, evaluate address, Execute, store result)
- add registers between processing elements to store intermediate results

> [!success]
> **Advantages**
> - clock cycle to complete the slowest single **stage**, not entire instruction
> - simpler instructions only few cycles
> - because instruction executes over multiple cycles, same hardware used more than once per instruction
> - only 1 alu and 1 memory (instead of 2)
>
> **Disadvantages**
> - hardware needed to store intermediate results
> - overhead bigger


