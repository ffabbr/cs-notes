
## Introduction

- an instruction is the most basic unit of computer processing 
- the [[10 Instruction Set Architectures|ISA]] (instruction set architecture) is like the "vocabulary" of the computer language
- can be written as machine language (0's and 1's) or Assembly (human readable)
- `LC-3` vs `MIPS` instructions


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

> [!success]- Example for an LC-3 Instruction
> In binary code, `0001` is the **opcode for ADD**. Next, we have the desgination register. The R's stand for the Registers. `110` is the binary number for 6, so R6. R2 is the source register 1, so the first number to be added. A `0` in bit 5 means we want to add a value of another register, and not a raw number. Bits 4 and 5 are ignored, and R6 is our Source Register 2. 
> 
> ==Generally, we do not need to know such syntax.== 
> 
> ![[Bildschirmfoto 2026-03-16 um 15.18.25.png]]
> 
> ![[2nd Semester/DDCA/Slides/07 Slides.pdf#page=74|07 Slides]]

> [!Success]- Example for a MIPS Instruction
> ![[2nd Semester/DDCA/Slides/07 Slides.pdf#page=76|07 Slides]]


> [!info] ISA vs Microarchitecture
> **ISA**
> - describes set of instructions that a processor can execute
> - what the processor can do (the instruction set)
> 
> **Microarchitecture**
> - how the processor executes the instructions defined by the ISA
> - defines the specific implementation of a processor based on that ISA
> - pipeline design, branch prediction policies, memory management

### Instruction Processing Cycle

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

![[2nd Semester/DDCA/Slides/08 Slides.pdf#page=14|08 Slides]]

### Glossary

| **Kürzel** | **Term**                     | **Description**                                                    |
| ---------- | ---------------------------- | ------------------------------------------------------------------ |
| **OP**     | Opcode                       | Specifies operation type (e.g., $0001$)                            |
| **SR**     | Source Register              | Register containing input data                                     |
| **DR**     | Destination Register         | Register where result is stored                                    |
| **IMM**    | Immediate                    | Literal constant encoded in instruction                            |
| **RS**     | Source Register              | Register containing input data in MIPS                             |
| **RT**     | Target Register              | Destination or second source register in MIPS                      |
| **PC**     | Program Counter              | Stores address of next instruction                                 |
| **ISA**    | Instruction Set Architecture | Processor instruction "vocabulary"                                 |
| **LD**     | Load                         | Moves data from $PC + offset$ to register                          |
| **LEA**    | Load Effective Address       | load address to register without touching memory                   |
| **ST**     | Store                        | Moves data from register to $PC + offset$                          |
| **LDR**    | Load Register                | Moves data from $BaseR + offset$ to register                       |
| **STR**    | Store Register               | Moves data from register to $BaseR + offset$                       |
| **LDI**    | Load Indirect                | Moves data from address pointed to by $PC + offset$                |
| **STI**    | Store Indirect               | Stores data to address pointed to by $PC + offset$                 |
| **LUI**    | Load Upper Immediate         | Loads 16 bits into upper half of register and zeros lower half     |
| **ORI**    | OR Immediate                 | Performs bitwise OR with literal to fill lower bits or modify data |
| **GPR**    | General Purpose Register     |                                                                    |
| **JMP**    | Jump                         |                                                                    |
| **beq**    | branch if equal              |                                                                    |
| **BRz**    | Branch if zero               |                                                                    |
| **PC**     | Program Counter              | Stores address of next instruction                                 |


## ISA Introduction

The ISA is the connection of software and hardware. It specifies the memoriy organization, the register set and the instruction set (Opcodes, Data types, Addressing modes). 

1. **Opcode**: what operation
2. **Operands**: who does it
## Opcodes

Use a large or small set of opcodes, f.ex. an operation for $(A\cdot B) + C$, but many operations mean complex hardware. So tradeoffs between 

- Hardware vs Software complexity
- Latency

**3 Types of Instructions**

1. operate instructions (in the ALU)
2. move data 
3. control / change sequence of execution
### LC-3 Opcodes

Example Opcode for ADD: 0001. There are 15 in total. 

![[2nd Semester/DDCA/Slides/08 Slides.pdf#page=23|08 Slides]]

### MIPS Opcodes

#### MIPS Instruction Types

- **R-type (Register):** operations where all data values is located in CPU registers (f.ex. add, and, nor, xor, ...). Opcode is 0, function is what defines operation
- **I-type (Immediate):** versions of R-type that involve f.ex. memory access, immediate operand, etc.
- **J-type (Jump):** f.ex. floating point operations, jumps to different part of program, large address space needed, etc.

![[2nd Semester/DDCA/Slides/08 Slides.pdf#page=25|08 Slides]]


## Data Types

- one or several data types supported
- LC-3 only supports 2's complement integers

**"Semantic gap"**: ==How close are data types to high level language?== With **complex** instructions/data types we have a **small** semantic gap. 

> [!Note] Number of Datatypes
> **More Datatypes**
> - better mapping of high-level programming to hardware
> - hardware directly operates on data types of programming languages
> - results in smaller number of instructions and code size
> 
> **But**
> - more work for microarchitect

> [!example] Complexity of Datatypes
> 
> **Complex Instructions/Datatypes**
> - smaller code size, better memory uzilication, more efficient
> - simpler compiler
> 
> **But**
> - more work for the compiler at once 
> - more complex hardware

### LC-3 Data Types

- **2's Complement:** standard binary system, represent whole numbers (both positive and negative)
- **Finding the negative version of a binary number**: 
  `Negative of ... X = NOT(X) + 1`. To make a positive number negative (or vice versa), you **invert every bit**, then add 1. So to display `-2`, so `00010`, we make `11101`, then add `0001`, and get `11110`. 

### MIPS Data Types

- **2's complement**
- **Unsigned integers**: numbers that will never be negative
- **Floating point**: numbers with decimals

---


## Addressing Modes

→ specify where an **operand** is located

The **Semantic Gap** also applies here.

> [!Note] Number of Addressing Modes
> **More Addressing Modes**
> - better mapping of high-level programming to hardware
> - results in smaller number of instructions and code size
> 
> **But**
> - more work for microarchitect
> - more options for the compiler what to use (compiler complexity)

### LC-3 Addressing Modes

- Immediate (the data is in the instruction itself)
- Register (instruction includes which register to check)
- Memory Addressing Modes
	- **PC-relative** ("*the data is x staps away from current location*")
	- **Indirect** (the provided memory address holds another memory address where the real data is stored)
	- **Base+offset** (*The memory address is `A+i`. A is base address and i is the offset.*). See → [[2nd Semester/DDCA/Slides/08 Slides.pdf#page=60|Slides for Base+Offset Addressing Mode]]

### MIPS Addressing Modes

Compared to LC-3, MIPS has pseudo-direct addressing (j, jal), but NO indirect addressing

## Operate Instructions

### LC-3 Operate Instructions

- NOT
- ADD
- AND

Bit no. 5 ("steering bit") is an extension of the Opcode. It determines what Bits 4 to 0 are. `0` means we have `00`, followed by a source register (3 bit address). `1` means the upcoming 5 bits are the values directly ("an immediate").

![[2nd Semester/DDCA/Slides/08 Slides.pdf#page=48|08 Slides]]


### MIPS Operate Instructions

- there is NO `NOT` 

![[#MIPS Instruction Types]]

F.ex. an **I-type** instruction: 

![[2nd Semester/DDCA/Slides/08 Slides.pdf#page=50|08 Slides]]

---

### Example: Subtraction

`a = b + c - d`

**LC-3** does not have a subtract instruction. Calculate `R2 <- b + c`, negate `c`, add `R2+c` 

**MIPS**: Calculate `b + c` and use the subtract instruction for the subtraction. In MIPS assembly: `addi $s1, $s0, -3`. 

![[2nd Semester/DDCA/Slides/08 Slides.pdf#page=52|08 Slides]]


---


## Data Movement Instructions

In MIPS there are only → [[2nd Semester/DDCA/Slides/08 Slides.pdf#page=60|Base+Offset]] and Immediate modes for load and store. 

In **LC-3**:
- 7 data movement instructions (LD, LDR, LDI, LEA, ST, STR, STI)

1. Opcode
2. DR or SR
3. Address generation bits

Remember [[#LC-3 Addressing Modes]], we are using PC relative addressing. 

**LD**: Load from memory 
**ST**: Store into memory

![[2nd Semester/DDCA/Slides/07 Slides.pdf#page=79|07 Slides]]

![[2nd Semester/DDCA/Slides/08 Slides.pdf#page=57|08 Slides]]

→ [[2nd Semester/DDCA/Slides/08 Slides.pdf#page=58|Indirect Accessing Mode]]

### LC-3 Data Movement

**LEA**: Load Effective Address
Loading an immediate value into the register without going to memory. The "effective address" stored is the result of `PC + offset`. So the calculated address itself is stored in the register. 

For comparison, at LD/ST, we need to first calculate the address and THEN go to that spot in the memory. 

So LEA: `DR <- PC + sign-extended(PCoffset9)`


### MIPS Data Movement

Instructions are exactly 32 bits long, so you cannot fit a full 32-bit constant inside a single instruction. In an I-type instruction (like `addi`), the **immediate** field is only 16 bits. If you want to load the value `0x6d5e4f3c`, you can't do it in one go because that value is 32 bits wide.

**Solution**

We "build" the number in two 16-bit halves:

**lui** (**load upper** immediate) place first 16 bits at the top of the register and fill bottom with 0. Example after `lui`: `0x6d5e0000`

**ori** (fill lower immediate) Use OR between register and remaining 16 bit constant. Lower 16 bits of the register are 0, OR puts in new value without changing upper bits. Example after `ori`: `0x6d5e4f3c` (start)

---

## Control Flow Instructions

![[2nd Semester/DDCA/Slides/08 Slides.pdf#page=73|08 Slides]]

### Conditions

### LC-3 Conditions

**Branch if Zero**

Condition codes are separate single bit hardware registers. When a value is written into a general purpose register, 3 condition codes are updated. The branch instruction itself does **no comparison**.

3 condition codes, EXACTLY 1 is set to 1, others 0
- N set, Z and P cleared: value **negative**
- Z set, N and P cleared: **value is 0**
- P set, N and Z cleared: value **positive**

### MIPS Conditions

The comparison happens in the branch instruction itself. So instead of reading of stored bits as in LC-3, we perform the comparison when requested. For example, beq (branch if rs and rt are equal)

```pseudocode
beq	$s0, $s1, offset

-------------------------
| 4 | rs | rt | offset   |
-------------------------
```





