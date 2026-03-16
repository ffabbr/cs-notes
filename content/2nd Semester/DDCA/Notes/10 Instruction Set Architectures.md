
## Glossary

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


## ISA Introduction

The ISA is the connection of software and hardware. It specifies the memoriy organization, the register set and the instruction set (Opcodes, Data types, Addressing modes). 

## Opcodes

Recall:
1. **Opcode**: Opcodes ==specify what operation to do==.
2. Operands: who does it

Use a large or small set of opcodes, f.ex. an operation for $(A\cdot B) + C$, but many operations mean complex hardware. So tradeoffs between 

- Hardware vs Software complexity
- Latency

LC-3, MIPS have 3 types of opcodes

1. operate instructions (in the ALU)
2. move data 
3. control

### Opcodes in LC-3

Example Opcode for ADD: 0001. There are 15 in total. 

![[2nd Semester/DDCA/Slides/08 Slides.pdf#page=23|08 Slides]]

### Opcodes in MIPS

#### MIPS Instruction Types

- **R-type (Register):** operations where all data values is located in CPU registers (f.ex. add, and, nor, xor, ...). Opcode is 0, function is what defines operation
- **I-type (Immediate):** versions of R-type that involve f.ex. memory access, immediate operand, etc.
- **J-type (Jump):** f.ex. floating point operations, jumps to different part of program, large address space needed, etc.

#### MIPS Instruction Type Slides

![[2nd Semester/DDCA/Slides/08 Slides.pdf#page=25|08 Slides]]

(this is only a selection of MIPS Upcodes, ==there are more==).

![[2nd Semester/DDCA/Slides/08 Slides.pdf#page=26|08 Slides]]


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

### LC-3

- **2's Complement:** standard binary system, represent whole numbers (both positive and negative)
- **Finding the negative version of a binary number**: 
  `Negative of ... X = NOT(X) + 1`. To make a positive number negative (or vice versa), you **invert every bit**, then add 1. So to display `-2`, so `00010`, we make `11101`, then add `0001`, and get `11110`. 

### MIPS

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

### LC-3

- NOT
- ADD
- AND


Bit no. 5 ("steering bit") is an extension of the Opcode. It determines what Bits 4 to 0 are. `0` means we have `00`, followed by a source register (3 bit address). `1` means the upcoming 5 bits are the values directly ("an immediate").

![[2nd Semester/DDCA/Slides/08 Slides.pdf#page=48|08 Slides]]


### MIPS

- there is NO `NOT` 

![[#MIPS Instruction Types]]

F.ex. an **I-type** instruction: 

![[2nd Semester/DDCA/Slides/08 Slides.pdf#page=50|08 Slides]]

---

### Subtraction, MIPS vs LC-3

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

![[2nd Semester/DDCA/Slides/08 Slides.pdf#page=57|08 Slides]]


**Indirect Addressing Mode**

![[2nd Semester/DDCA/Slides/08 Slides.pdf#page=58|08 Slides]]

### Immediate Addressing Mode

### LC-3

**LEA**: Load Effective Address
Loading an immediate value into the register without going to memory. The "effective address" stored is the result of `PC + offset`. So the calculated address itself is stored in the register. 

For comparison, at LD/ST, we need to first calculate the address and THEN go to that spot in the memory. 

So LEA: `DR <- PC + sign-extended(PCoffset9)`


### MIPS

Instructions are exactly 32 bits long, so you cannot fit a full 32-bit constant inside a single instruction. In an I-type instruction (like `addi`), the **immediate** field is only 16 bits. If you want to load the value `0x6d5e4f3c`, you can't do it in one go because that value is 32 bits wide.

**Solution**

We "build" the number in two 16-bit halves:

**lui** (**load upper** immediate) place first 16 bits at the top of the register and fill bottom with 0. Example after `lui`: `0x6d5e0000`

**ori** (fill lower immediate) Use OR between register and remaining 16 bit constant. Lower 16 bits of the register are 0, OR puts in new value without changing upper bits. Example after `ori`: `0x6d5e4f3c` (start)

---

## Control Flow Instructions

![[2nd Semester/DDCA/Slides/08 Slides.pdf#page=73|08 Slides]]

### Conditions

Condition codes are separate single bit hardware registers. When a value is written into a general purpose register, 3 condition codes are updated. 

3 condition codes, EXACTLY 1 is set to 1, others 0
- N set, Z and P cleared: value **negative**
- Z set, N and P cleared: **value is 0**
- P set, N and Z cleared: value **positive**

![[2nd Semester/DDCA/Slides/08 Slides.pdf#page=76]]![[2nd Semester/DDCA/Slides/08 Slides.pdf#page=78]]