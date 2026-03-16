
## Glossary

| **Abbreviation** | **Full Term**                | **Description**                                    |
| ---------------- | ---------------------------- | -------------------------------------------------- |
| **MAR**          | Memory Address Register      | Holds target memory address for R/W                |
| **MDR**          | Memory Data Register         | Holds data being moved to/from memory              |
| **ALU**          | Arithmetic Logic Unit        | Executes math and logic operations                 |
| **I/O**          | Input / Output               | Hardware for external interaction (e.g., keyboard) |
| **IR**           | Instruction Register         | Stores instruction currently being executed        |
| **PC**           | Program Counter              | Stores address of next instruction                 |
| **ISA**          | Instruction Set Architecture | Processor instruction "vocabulary"                 |
| **LC-3**         | Little Computer 3            | Architecture with 8 general-purpose registers      |
| **MIPS**         | Microprocessor without...    | Architecture with 32 general-purpose registers     |
| **LDR**          | Load Register                | Moves data from memory into register               |
| **ADD**          | Add(-ition)                  | Sums values from register file                     |
| **OP**           | Opcode                       | Specifies operation type (e.g., $0001$)            |
| **SR**           | Source Register              | Register containing input data                     |
| **DR**           | Destination Register         | Register where result is stored                    |
| **IMM**          | Immediate                    | Literal constant encoded in instruction            |
| **RS**           | Source Register              | Register containing input data in MIPS             |
| **RT**           | Target Register              | Destination or second source register in MIPS      |

## Principles

- **Stored-Program**: Instructions stored in linear memory array, memory between insstructions and data is unified
- **Sequential Instruction Execution:** Instructions executed sequentially one at the time. *Program counter*  identifies current instruction.

## Component Overview

![[2nd Semester/DDCA/Slides/07 Slides.pdf#page=30|07 Slides]]

## Memory

- Stores **Programs** and **Data** through **bits**. 
	- bits is the smallest unit
	- a byte is typically 8 bits
	- a word consists of multiple bytes
- Each storage location is identified by its address. The set of all addresses is called address space. 
- Addressability: number of bits at an address location. Could be f.ex. 
	- **word-addressable**, meaning each word has a unique address
	- byte-addressable, meaning each byte has a unique address (common). A 32-bit word at address `X` would occupy bytes `X`, `X+1`, `X+2`, `X+3`.

Example, suppose a word is 4 Bytes (4 columns in one row). That's why the adresses on the left make 4er Schritte (C is 12). A box is 1 Byte, the content in hex format. 

### Accessing Memory



- **MAR**: Memory Address Register
  Holds the address of where the data is stored or where to save something. 
- **MDR**: Memory Data Register
  Holds the actual data

![[2nd Semester/DDCA/Slides/07 Slides.pdf#page=36|07 Slides]]


Conventions to order the four bytes in a row: 

- **Big Endian**: Most significant byte gets **lower** byte address
- **Little Endian**: Most significant byte gets **higher** byte address


## Processing Unit

![[2nd Semester/DDCA/Slides/07 Slides.pdf#page=42|07 Slides]]

- ALU performs arithmetic and bitwise operations. 
- Registers hold temporary data. 
### Registers

- [[#Memory]] is large but slow, ==Registers are for fast access==
- Computer has small memory close to ALU for fast temporary access (f.ex. for intermediate results in a calculation)
- The collection of those single registers is called the Register File. 
- F.ex. `LC-3` has 8 general purpose registers, `MIPS` has 32
- [[03 Storage#Register|Implementation (03 Storage)]]

## I/O, Input and Output

Well, the obvious. 
Here, we mainly consider keyboard and monitor. 

## Control Unit

Conducts step by step process of executing a program. Sends signals to ALU to select an operation, to registers to read or write data,  to memory to initiate read or write cycles. 

- **Instruction Register**: keeps track of instructions that are being processed
- **==Program Counter== / Instruction Pointer**: contains address of next instruction to process




---


![[2nd Semester/DDCA/Slides/07 Slides.pdf#page=66|07 Slides]]
![[2nd Semester/DDCA/Slides/07 Slides.pdf#page=67|07 Slides]]

## Instructions

- an instruction is the most basic unit of computer processing 
- the ISA (instruction set architecture) is like the "vocabulary" of the computer language
- can be written as machine language (0's and 1's) or Assembly (human readable)
- `LC-3` vs `MIPS` instructions

1. **Opcode**: what to do
2. **Operands**: who does it

**3 Types of Instructions**

1. operate instructions (in the ALU)
2. move data 
3. change sequence of execution

> [!info]- Assembly Instructions, Examples
> **Assembly**: 
> ```
> add a, b, c
> ```
> 
> **LC-3 registers**: 
> ```
> b = R1 
> c = R2
> a = RO
> ```
> 
> **MIPS-registers**
> ```
> b = $s1
> c = $s2
> a = $s0
> ```

> [!success] Example for an LC-3 Instruction
> In binary code, `0001` is the **opcode for ADD**. Next, we have the desgination register. The R's stand for the Registers. `110` is the binary number for 6, so R6. R2 is the source register 1, so the first number to be added. A `0` in bit 5 means we want to add a value of another register, and not a raw number. Bits 4 and 5 are ignored, and R6 is our Source Register 2. 
> 
> ==Generally, we do not need to know such syntax.== 
> 
> ![[Bildschirmfoto 2026-03-16 um 15.18.25.png]]
> 
> ![[2nd Semester/DDCA/Slides/07 Slides.pdf#page=74|07 Slides]]

> [!Note] Example for a MIPS Instruction
> ![[2nd Semester/DDCA/Slides/07 Slides.pdf#page=76|07 Slides]]


## Reading Operands from Memory

- load from memory to register
- store from register to memory

### Example, load word

High level code: 
`A = A[i];`

Assembly: 
`load a, A, i`

The memory address is `A+i`. A is base address and i is the offset. 

→ [[2nd Semester/DDCA/Slides/08 Slides.pdf#page=60|Base+Offset Addressing Mode]]

![[2nd Semester/DDCA/Slides/07 Slides.pdf#page=79|07 Slides]]
![[2nd Semester/DDCA/Slides/07 Slides.pdf#page=80|07 Slides]]
![[2nd Semester/DDCA/Slides/07 Slides.pdf#page=81|07 Slides]]

## Instruction Processing Cycle

*If a value from memory is interpreted as an instruction depends on when in the instruction cycle it is fetched. F.ex. in the FETCH  state, it is an instruction, in FETCH OPERANDS as see it as Data.* 

1. **Fetch**
   Retrieve the instruction from memory
	1. Load the MAR with contents of the PC, increment the PC
	2. Interrogate memory, pleace instruction in MDR
	3. Load the IR with contents of the MDR
2. **Decode:** Determine the instruction’s operation and operands
3. **Evaluate Address:** Calculate memory addresses for memory operands (if needed).
4. **FETCH OPERANDS**
   Get the operands from registers or memory.
	- **LDR** (Load Register): load MAR with address calculated in [[#03 Evaluate Address]], read memory, place source operand in MDR
	- **ADD**: Get source operands from register file. 
5. **EXECUTE:** Perform the operation in the ALU.
6. **STORE RESULT:** Write the result back to a register or memory.


---


![[2nd Semester/DDCA/Slides/08 Slides.pdf#page=12|08 Slides]]
![[2nd Semester/DDCA/Slides/08 Slides.pdf#page=13|08 Slides]]
![[2nd Semester/DDCA/Slides/08 Slides.pdf#page=14|08 Slides]]
