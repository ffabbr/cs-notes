
> [!Note] Number of Addressing Modes
> **More Addressing Modes**
> - better mapping of high-level programming to hardware
> - results in smaller number of instructions and code size
> 
> **But**
> - more work for microarchitect
> - more options for the compiler what to use (compiler complexity)

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

> [!success] Complexity of Instructions
> - **Complex instructions** do a lot of work, f.ex. matrix multiply, insert into linked list, etc. 
> - **Simple instruction**, f.ex. Add, XOR, Multiply

> [!success] Number of Opcodes
> Use a **large or small set of opcodes**, f.ex. an operation for $(A\cdot B) + C$, but many operations mean complex hardware. So tradeoffs between 
> 
> - Hardware vs Software complexity
> - Latency

> [!example] Number of Registers
> **Many Registers**
> - better register allocation (more in fast register, fewer saves/restores)
> 
> **BUT**
> - larger instruction and register file size

> [!Note] Add Program Counter?
> **Yes**: sequential execution (easier to program)
> **No**: dataflow model (performance)