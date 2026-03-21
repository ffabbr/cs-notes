
> How does performance improve with additional cores? 
> More cores/hardware do not always result in a linear speedup. 

## Limiting factors

- parts of a program that cannot be executed parallelly
- data strcutres that require sequential access (f.ex. linked list)
- Verteilung auf Cores und Threads
- Overhead and time for synchronization/locking 
- Memory bandwidth, cache misses


---

## Speedup

==S: Speedup==, How performance improves with additional cores

==T==: Execution time

> [!success]
> $T_{1}$: sequential execution time
> $T_{p}$: Execution time on p CPUs. 
> 
> $T_{p} = \frac{T_{1}}{p}$: linear speedup
> 
> $T_{p} > \frac{T_{1}}{p}$: normal speedup

Parallel speedup on **p** CPUs 
$$
S_{p} = \frac{T_{1}}{T_{p}}
$$
- $S_{p} = p$ : linear
- $S_{p} < p$ (sub-linear, performance loss)

Efficiency 
$$
E=\frac{S_{p}}{p}
$$

---

### Beispiel

80% parallelisierbar, 20% sequenziell. 

- $T_{1} = 10$
- $T_{seq} = 10 \cdot 0.2$
- $T_{p} = 10 \cdot 0.8$
- $p=8$ CPUs

$T_{8} = ?$
$$
\begin{align}
T_{8} &= T_{seq} + T_{par} \\
 & = 10\cdot 0.2 + \frac{10\cdot 0.8}{8} \\
 & = 2+1 \\
 & = 3
\end{align}
$$

$S_{8} = ?$ 
$$
S_{8} = \frac{T_{1}}{T_{8}}=\frac{10}{3}=3.33
$$

$E=?$
$$
E=\frac{3.33}{8} \approx 0.4 \implies 40\%
$$


---

## Amdahl's Law

*"Will ein Problem lösen, geht nimmer schneller"*

> The speedup from parallelization is limited by the part that must run sequentially.

$W_{ser}$ ... time spend on non-parallelizable work
$W_{par}$ ... time spend on parallelizable work

$$
T_{1} = W_{ser} + W_{par}
$$

$$
T_{p} \geq W_{ser} + \frac{W_{par}}{p}
$$

So in the definition of speedup: 

$$
S_{p} = \frac{T_{1}}{T_{p}} \leq \frac{W_{ser} + W_{par}}{W_{ser} + \frac{W_{par}}{p}}
$$
> [!info] Formula with percentage
> $f$ is the percentage of how much is sequential
> $$
> S_{p} = \frac{1}{f+ \frac{1-f}{P}}
> $$

![[2nd Semester/PProg/Slides/07 Slides.pdf#page=34]]

---

## Gustafson's Law

*"Geht nimmer schneller, aber egal, ich kann mehr (anderes) in der selben Zeit machen"*

Parallel part of a program scales with the problem size. 

Wie viel Arbeit können wir in einem fixen Zeitfenster ausführen, wenn wir mehr Hardware hinzufügen? 

**Formulas**

- $f$: Percentage of sequential part
- **$1-f$**: parallelizable part
- **$P$**: number of cores
- $T_{wall}$: total time allowed for execution
- $W$: amount of work
- $S_{p}$: speedup achieved by $p$ processors

$$
W=P\cdot (1-f)\cdot T_{wall} + f \cdot  T_{wall}
$$

> [!success]
> $$
\begin{align}
S_{p} &= f+P\cdot (1-f) \\
 & = P-f\cdot (P-1)
\end{align}
$$


![[2nd Semester/PProg/Slides/07 Slides.pdf#page=39]]

![[Bildschirmfoto 2026-03-18 um 17.47.02.png]]

![[Bildschirmfoto 2026-03-18 um 17.49.46.png]]

![[Bildschirmfoto 2026-03-18 um 17.51.28.png]]


Siehe #exam , Kosten-Nutzen Analyse, lohnt es sich, mehr Hardware hinzuzufügen?


![[Bildschirmfoto 2026-03-19 um 14.12.29.png]]![[Bildschirmfoto 2026-03-19 um 14.12.40.png]]![[Bildschirmfoto 2026-03-19 um 14.12.49.png]]