
The Von Neumann model has a **fixed sequence**. 

The [[21 Dataflow|Dataflow]] model goes by data availability (in data flow order), meaning f.ex. when Operands are loaded, in dependence of the program, etc. multiple Instructions can run at the same time, thus in **parallel**.


Fetch and execute order: 
**Control flow order**: program counter (instruction pointer) specifies

**==Dataflow model==**: 

- no program counter, 
- **act when ready depending on data flow dependence (when all operands are received)** 
- Instructions can execute at the same time
- Execute computation when all inputs available

- Data Flow at [[10 Instruction Set Architectures|ISA]] level not successful as programmers would need to adapt
- **Data Flow at [[12 Microarchitecture|microarchitecture]] very successful**: The order of processing doesn't matter as long as the semantics of ISA are met. But that's not visible to the programmer, the programmer only sees the ISA (f.ex. as in [[09 Von Neumann|von Neumann]]).

**Dataflow graph**

- write down all instructions with their registers with correct order, meaning f.ex. extract/reverse-engineer them from the [[17 Out of order execution#Tomasulo's Algorithm|Tomasulo]] charts (RAT, Register Alias Table; RS, Reservation station) with the tags
- **==when a value in the RS doesn't appear in the original RAT, it has been written in the meantime. look at what that instruction could have been==**
- look at dependencies, then draw graph 

![[Bildschirmfoto 2026-04-16 um 18.51.51.png|Dataflow Graph for factorial]]

![[Bildschirmfoto 2026-05-02 um 22.25.23.png]]


> [!error] ISA BASED
> **Advantages**: 
> - use irregular parallelism
> - more parallelism
> 
> **Disadvantages**
> - no precise state semantics
> - large hardware
