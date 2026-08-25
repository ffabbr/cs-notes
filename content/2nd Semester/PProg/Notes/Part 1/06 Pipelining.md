→ split a "process" into different stages, each with clear function, f.ex. clothing washing process

> [!info] Balenced
> **Balanced pipeline**: all steps require same time

**1. Instruction Fetch**
- CPU reads the instruction from memory
- may prefetch multiple instructions

**2. Instruction Decode**
- decode the instructions, prepare instructions for execution
- instructions are then dispatched to the correct execution units

**3. Execution**
- CPU executes decoded instruction
- Superscalar execution: instructions dispatched to multiple execution units. 
- SIMD: apply one ==s==ingle ==i==nstruction to ==m==ultiple pieces of ==d==ata all at once

**4. Memory Access**
- If needed, exchange data between CPU and memory
- pre-fetching, [[05 Hardware#Caching|caching]], etc.

**5. Writeback**
- Save the final result of the execution
- outcome of the execution stage is written back into the CPU's registers
- Superscalar Execution: Multiple instructions can write their results back to different registers or memory locations at the same time

## Throughput

**Throughput** = number of instructions that exit the pipeline per time unit. higher is better

→ EINHEITEN angeben 

- For a specific number of instances n: $\text{Throughput} = \frac{n}{\text{total time}}$ oder $\frac{\text{total time}}{n}$
- For infinite pipeline (per execution unit)
$$\text{Throughput bound} = \frac{1}{\text{Dauer vom längsten Schritt}}$$

Beispiele: 
-  $t_\text{put} = \frac{1}{3s}$ means 1 instruction per 3s
- 1 Produkt pro 15 min

## Latency

**Latency** = time needed to perform single computation. ==lower is better==

- Latency ist nicht konstant, kann sich verändern
- **Latency bound** = (no of stages) $\cdot$ Dauer vom längsten Schritt

- Konstant: nehme einfach erste Instanz `latency = Zeit für erste Instanz` 

- Nicht konstant, für die **==n-te Instanz==**: `latency = Zeit für erste Instanz + (Längste Stage - Time of first stage) * (n-1)` 

## Total time

Example, we want to know how much time is needed for 100 instances. 

Suppose in this example we are processing images. Every image has a sequence of operations. 

1. Calculate for first instance. $T_{first} = 40 + 50 + 30 + 40 = 160\text{ ms}$
2. Once the pipeline is full, it outputs one finished image at the rate of its bottleneck.
   $T_{remaining} = 99 \times 50\text{ ms} = 4950\text{ ms}$
3. $T_{total} = 160\text{ ms} + 4950\text{ ms} = 5110\text{ ms}$

## Example: unbalanced Pipeline creates waiting delays

Example: washing loads

![[2nd Semester/PProg/Slides/06 Slides.pdf#page=62|06 Slides]]

→ make pipeline balanced by increasing time for each stage to match longest stage

![[2nd Semester/PProg/Slides/06 Slides.pdf#page=64|06 Slides]]

→ add 2 dryers working in a row

![[2nd Semester/PProg/Slides/06 Slides.pdf#page=67|06 Slides]]


