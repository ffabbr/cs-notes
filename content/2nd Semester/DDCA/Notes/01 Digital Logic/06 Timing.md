
> [!abstract] Circuit Design Attributes
> - Area
> - *Speed*
> - Energy Consumption
> - Design Time


**Timing**: 
- How fast is a circuit?
- How can we make a circuit faster?
- What happens if we run a circuit too fast?

**Delay is caused by (physics):** 
- capacitance and resistance
- finite speed of light

**Delay is affected by:** 
- rising vs falling
- different inputs 
- environment (humidity)
- aging
- voltage

## Types of Delay




## Longest, Shortest Delay Path

Remember though that even wires can affect the delay, increasing with length 

![[2nd Semester/DDCA/Slides/06 Slides.pdf#page=34]]


---

## Implementation Comparisons

![[2nd Semester/DDCA/Slides/06 Slides.pdf#page=38]]
![[2nd Semester/DDCA/Slides/06 Slides.pdf#page=39]]

## Ouput Glitches

Let's say I calculated a delay wrong and therefore latch some wrong result at clock edge. 

> [!info] Definition Glitch
> ==One input== transition causes ==multiple output== transitions

On the left we initially have 0, 1, 1 input. So the top AND gate initially outputs 0. The bottom AND gate outputs 1. The final OR gate outputs 1. 

Now, suppose the middle input 1 → 0:  
1. bottom AND gate becomes 0
2. top AND gate is ==slower==, still outputs 0
3. final OR output is 0
4. ==Slow  Path catches up (ouput turns back to 1)==

> Not too important, timing analysis is important, but we don't always care about glitches.


![[2nd Semester/DDCA/Slides/06 Slides.pdf#page=48]]

### How to avoid Glitches

→ see [[07 K-Maps]]

![[2nd Semester/DDCA/Slides/06 Slides.pdf#page=51]]

## Sequential Circuit Timing, [[03 Storage#D Flip-Flop|D Flip-Flop]]

![[2nd Semester/DDCA/Slides/06 Slides.pdf#page=56]]

Metastability: Things changed while the sampling

![[2nd Semester/DDCA/Slides/06 Slides.pdf#page=57]]

$t_{ccq}$: Shortest Delay
$t_{pcq}$: Worst case delay

![[2nd Semester/DDCA/Slides/06 Slides.pdf#page=58]]

## Sequential Timing

### Ensuring Correct Sequential Operation

![[2nd Semester/DDCA/Slides/06 Slides.pdf#page=60]]

### Delay types

![[2nd Semester/DDCA/Slides/06 Slides.pdf#page=33]]
![[2nd Semester/DDCA/Slides/06 Slides.pdf#page=73]]

> [!success]
> The ==clock cycle time== $T_{c}$ needs to be greater than the ==sum of== 
> 1. maximum delay of reading the data from R1 (==propagation delay== from clock to q, $t_{pcq}$). At that point Q1 is stable.
> 2. maximum ==delay of the combinational logic== CL ($t_{pd}$)
> 3. the maximum ==time D2 needs to stay stable== ($t_{\text{setup}}$) 


- $t_{pcq}$ is the ==upper bound== (propagation delay clock to q) 
- $t_{ccq}$ is the ==lower bound== (contamination delay) of the time from the rising edge of the clock until the output changes. 
- the setup and hold times indicate when the inputs must be stable relative to the rising edge of the clock

### Setup contraint 

![[2nd Semester/DDCA/Slides/06 Slides.pdf#page=66]]

An asynchronous design would not have this overhead, but barely possible to design. 

**==Critical path==**: path with the longest $t_{pd}$. 

- critical path too long: slow 
- critical path too short: each cycle will do very little useful work

### Hold Time Constraint

![[2nd Semester/DDCA/Slides/06 Slides.pdf#page=72]]

### Example: Timing Analysis

> This circuit won't work because we ==don't satisfy the hold time constraints.==

$t_{pd}$ is always calculated using the ==critical path==. 

![[2nd Semester/DDCA/Slides/06 Slides.pdf#page=78]]

To fix the hold time, ==add buffers==. The critical path is not affected as can be seen, and the added contamination delay fixes the hold time constraints. 

![[2nd Semester/DDCA/Slides/06 Slides.pdf#page=84]]

## Clock Skew

Clocks have delays too. Clock Skew is the time difference between two clock edges. So different registers can have shifted f.ex. rising edges of the clocks. 

This ==increases== Setup and Hold time. 

### Clock Skew: Setup Time 

![[2nd Semester/DDCA/Slides/06 Slides.pdf#page=88]]

### Clock Skew: Hold Time 

![[2nd Semester/DDCA/Slides/06 Slides.pdf#page=89]]

---

![[Bildschirmfoto 2026-03-07 um 12.21.12.png]]