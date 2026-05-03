
## Glossary

| **Abbreviation** | **Full Term**                | **Description**                                    |
| ---------------- | ---------------------------- | -------------------------------------------------- |
| **MAR**          | Memory Address Register      | Holds target memory address for R/W                |
| **MDR**          | Memory Data Register         | Holds data being moved to/from memory              |
| **ALU**          | Arithmetic Logic Unit        | Executes math and logic operations                 |
| **I/O**          | Input / Output               | Hardware for external interaction (e.g., keyboard) |
| **IR**           | Instruction Register         | Stores instruction currently being executed        |
| **PC**           | Program Counter              | Stores address of next instruction                 |
| **[[10 Instruction Set Architectures\|ISA]]** | Instruction Set Architecture | Processor instruction "vocabulary"                 |
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

## Components

![[2nd Semester/DDCA/Slides/07 Slides.pdf#page=30|07 Slides]]

### 01 Memory

- Stores **Programs** and **Data** through **bits**. 
	- bits is the smallest unit
	- a byte is typically 8 bits
	- a word consists of multiple bytes
- Each storage location is identified by its address. The set of all addresses is called address space. 
- Addressability: number of bits at an address location. Could be f.ex. 
	- **word-addressable**, meaning each word has a unique address
	- byte-addressable, meaning each byte has a unique address (common). A 32-bit word at address `X` would occupy bytes `X`, `X+1`, `X+2`, `X+3`.

Example, suppose a word is 4 Bytes (4 columns in one row). That's why the adresses on the left make 4er Schritte (C is 12). A box is 1 Byte, the content in hex format. 

#### Accessing Memory

- **MAR**: Memory Address Register
  Holds the address of where the data is stored or where to save something. 
- **MDR**: Memory Data Register
  Holds the actual data

![[2nd Semester/DDCA/Slides/07 Slides.pdf#page=36|07 Slides]]


Conventions to order the four bytes in a row: 

- **Big Endian**: Most significant byte gets **lower** byte address
- **Little Endian**: Most significant byte gets **higher** byte address


### 02 Processing Unit

![[2nd Semester/DDCA/Slides/07 Slides.pdf#page=42|07 Slides]]

- ALU performs arithmetic and bitwise operations. 
- Registers hold temporary data. 
#### Registers

- [[#Memory]] is large but slow, ==Registers are for fast access==
- Computer has small memory close to ALU for fast temporary access (f.ex. for intermediate results in a calculation)
- The collection of those single registers is called the Register File. 
- F.ex. `LC-3` has 8 general purpose registers, `MIPS` has 32
- [[03 Storage#Register|Implementation (03 Storage)]]

More Registers: better register allocation, fewer saves, re-stores, BUT larger instruction size and register file size

### 03  I/O, Input and Output

Well, the obvious. 
Here, we mainly consider keyboard and monitor. 

### 04 Control Unit

Conducts step by step process of executing a program. Sends signals to ALU to select an operation, to registers to read or write data,  to memory to initiate read or write cycles. 

- **Instruction Register**: keeps track of instructions that are being processed
- **==Program Counter== / Instruction Pointer**: contains address of next instruction to process




---


![[2nd Semester/DDCA/Slides/07 Slides.pdf#page=66|07 Slides]]
![[2nd Semester/DDCA/Slides/07 Slides.pdf#page=67|07 Slides]]


