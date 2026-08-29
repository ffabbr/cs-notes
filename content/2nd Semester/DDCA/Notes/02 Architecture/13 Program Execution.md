
How we compile and run an application: 

1.  Compiler converts to machine code
2. Assembler replaces variables with addresses
3. Linker creates executable (text segment)

![[Bildschirmfoto 2026-04-16 um 18.22.08.png]]

Memory has **Instructions** and **Data**.

## Instructions

1. Instruction Fetch (IF)
2. Decode and register operand fetch (ID/RF)
3. Execute/Evaluate memory address (EX/AG)
4. Memory operand fetch (MEM)
5. Store result (WB, writeback)

## Interrupts and Exceptions

Interrupts: external cause (f.ex. power failure, IO needed)
Exceptions: internal cause (f.ex. divide by 0)
