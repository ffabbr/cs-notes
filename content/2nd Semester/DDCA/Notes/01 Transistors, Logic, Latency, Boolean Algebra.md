## Transistors

- From 2300 (1971) to 21 Mil (2000) to 67 Bil (2022, M2 Max) transistors. 
- MOS (Conductors, Insulators, Semiconductors)
- Voltage and Type: Source and Drain get connected or not (Gate). 
- Transistor as switches. 
	- n-type: the circuit is closed when the gate is supplied with 3V, transistor gets high voltage, the connection from source to drain is closed. 0V: circut open, light off
	- p-type: the circuit is closed when the gate is supplied with 0V. marked with a dot. 0V: closed circuit, light on. 

![[Bildschirmfoto 2026-02-23 um 22.03.56.png]]

## CMOS

- p-type pulls up, n-type pulls down the output (the voltage)
  ![[Bildschirmfoto 2026-02-23 um 22.22.04.png]]
- ![[Bildschirmfoto 2026-02-23 um 22.37.57.png]]

## Logic Gates

![[2nd Semester/DDCA/Slides/02 Slides.pdf#page=32]]

## Boolean Algebra

- NOT: $\overline{A}$
- AND: $A\cdot B$
- OR: $A+B$ 


- ==Minterm==: Product (AND) that includes all input variables of a row in the truth table exactly once (DNF). For $011 → \overline{A}BC$ 
- ==Maxterm==: Sum (OR) that includes all input variables of a row in the truth table exactly once. For $011 → A + \overline{B} + \overline{C}$ 
- ==Implicant==: Product (AND) of literals ($A$ or $\overline{A}$)

- ==SOP==, sum of products. $(A \cdot B) + (\overline{A} \cdot C)$
- ==POS==, product of sums. $(A + B) \cdot (\overline{A} + \overline{C})$ 

- Create the truth table → bring into SOP/POS form → boolean simplification rules

![[2nd Semester/DDCA/Slides/02 Slides.pdf#page=71]]
![[2nd Semester/DDCA/Slides/02 Slides.pdf#page=76]]
![[2nd Semester/DDCA/Slides/02 Slides.pdf#page=80]]


## Simplification

![[2nd Semester/DDCA/Slides/02 Slides.pdf#page=80]]
![[Bildschirmfoto 2026-02-23 um 22.59.39.png]]![[2nd Semester/DDCA/Slides/02 Slides.pdf#page=62]]
## Dual

- + to $\cdot$ and vice versa
- 0 to 1 and vice versa

## Decoder

For example 2-to-4 decoder is about choosing one ouput (Y) depending on the input $A_{1}$ and $A_{2}$. 

Exactly one output (Y) is 1 and the rest is 0.

![[Bildschirmfoto 2026-02-20 um 15.46.28.png]]

## Multiplexer (Selector)

Selects one signal from N available inputs. Needs $\log_{2}(N)$ select controls

![[2nd Semester/DDCA/Slides/02 Slides.pdf#page=94]]
![[2nd Semester/DDCA/Slides/02 Slides.pdf#page=97]] 

## Latency and Power Consumption

- series connections are slower than parallel connections (more resistance on the wire)
- dynamic power consumption: charge capacitance as signal change ($0$ to $1$ or $1$ to $0$)
- capacitance of the circuit $\cdot$ supply voltage $^2$ $\cdot$ charging frequency of the capacitor
- voltage vs performance
- static power consumption: $V \cdot I_{leakage}$. Power used when signals do not change. supply voltage $\cdot$ leakage current
- energy is integral of power. energy determines battery life

 ---

## Full adder

More reading: 
- [[Harris Harris.pdf#page=265|H&H Information on Adders]]
- [[2nd Semester/DDCA/Slides/03 Slides.pdf#page=36|Carry Lookahead Adder]]

![[2nd Semester/DDCA/Slides/03 Slides.pdf#page=32]]

### Adders for higher bit addition

![[2nd Semester/DDCA/Slides/03 Slides.pdf#page=34]]

depends on sequential adders, thus slow

## PLA

A Programmable Logic Array is a customizable hardware construct used to implement specific digital logic functions, basically a super basic version of an FPGA. It is built using two distinct sets of logic gates: a column of AND gates whose outputs feed into a column of OR gates. You program the PLA by defining exactly which AND gate outputs connect to which OR gate inputs in the central connection block.

This physical AND-to-OR layout is specifically designed to calculate "Sum of Products" (SOP) equations. By connecting the right "minterms," the PLA can implement any required N-input, M-output logic function.

![[2nd Semester/DDCA/Slides/03 Slides.pdf#page=40]]

Implementing a [[#Full adder]]

![[2nd Semester/DDCA/Slides/03 Slides.pdf#page=41]]

![[2nd Semester/DDCA/Slides/03 Slides.pdf#page=42]]


## Completeness

> [!success] 
> Logically complete, meaning any trutz table (logic function) can be build only with them
> - NAND
> - NOR
> - {AND, OR, NOT}

> [!example] Example: NAND is logically complete
> Definition of NAND: $A \uparrow B = \overline{A \cdot B}$
> - $\overline{A} = \overline{A \cdot A} = A \uparrow A$
> - $A \cdot B = \overline{\overline{A \cdot B}} = \overline{(A \uparrow B)} = (A \uparrow B) \uparrow (A \uparrow B)$
> - $A + B = \overline{\overline{A} \cdot \overline{B}} = \overline{A} \uparrow \overline{B} = (A \uparrow A) \uparrow (B \uparrow B)$


## Equality Checker

![[2nd Semester/DDCA/Slides/03 Slides.pdf#page=50]]

## ALU

One component that can act as a bunch of different components. 

![[2nd Semester/DDCA/Slides/03 Slides.pdf#page=52]]

## Tri-State Buffer

A and E input, Y output. 

- E=0: New ==Z-State== is no signal, as if wire cut
- E=1: Acts as normal wire (Y=E)

Imagine a wire connecting the CPU and memory. At any time only the CPU or the memory can place a value on the wire, both not both. You can have two tri-state buffers: one driven by CPU, the other memory; and ensure at most one is enabled at any time

![[2nd Semester/DDCA/Slides/03 Slides.pdf#page=57]]


