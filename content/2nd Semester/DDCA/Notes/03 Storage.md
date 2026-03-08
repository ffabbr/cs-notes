
Two inverters connected in a loop. There are two different options for this, so we can store one bit. It is stable.
$$Q = 0, \; \overline{Q} = 1 \qquad \text{or} \qquad Q = 1, \; \overline{Q} = 0$$

![[2nd Semester/DDCA/Slides/03 Slides.pdf#page=93]]

Problem is this runs forever, so we need a control mechanism. We get our desired value to `bitline`. Raising the wordline to 1 allows for data to flow in our out. At wordline = 0 the SRAM loop holds state indefinitely. 

![[2nd Semester/DDCA/Slides/03 Slides.pdf#page=94]]

## Storage Types

![[2nd Semester/DDCA/Slides/03 Slides.pdf#page=95]]

## The Reset-Set Latch

Problem: The forbidden state S = R = 1 is ambiguous and must be avoided.

![[2nd Semester/DDCA/Slides/03 Slides.pdf#page=97]]

## Gated D Latch

To avoid setting R and S to 0 at the same time (forbidden). Only has ==one input==. 

Left side takes `D`and `write enable` and creates S and R: 
$$S = \overline{D \cdot WE} \qquad R = \overline{\overline{D} \cdot WE}$$
S and R can never be 0 at the same time because $\overline{D}$ and $D$ can't be 0 at the same time. 

- `write enable = 0`, dann haben die beiden linken NAND's ouput 1, unabhängig von D. damit haben wir $S=1, R=1$, und das System ist idle, holding $Q_{\text{prev}}$.
- `write enable = 1`, dann 
	- Wenn `D=0`, dann $S=1, R=0$, somit `Q=0`
	- Wenn `D=1`, dann $S=0, R=1$, somit `Q=1`
	- in beiden Fällen hat Q den Wert von D


![[2nd Semester/DDCA/Slides/03 Slides.pdf#page=101]]
![[2nd Semester/DDCA/Slides/03 Slides.pdf#page=102]]


##  D Flip-Flop 

> [!success]
> Changes only happen on rising edge.

![[2nd Semester/DDCA/Slides/06 Slides.pdf#page=55]]

![[2nd Semester/DDCA/Slides/03 Slides.pdf#page=148]]
![[2nd Semester/DDCA/Slides/03 Slides.pdf#page=151]]

**Multiple D Flip-Flops:** 

![[2nd Semester/DDCA/Slides/03 Slides.pdf#page=152]]

![[Harris Harris.pdf#page=139]] 

## Register

- a combination of flip-flops that share a common CLK input
- all bits of the register are updated at the same time

![[2nd Semester/DDCA/Slides/03 Slides.pdf#page=104]]
![[2nd Semester/DDCA/Slides/03 Slides.pdf#page=105]]

