
Seien $A$ und $B$ Ereignisse mit$\Pr[B] > 0$.
Die bedingte Wahrscheinlichkeit $\Pr[A|B]$von $A$ gegeben $B$ ist definiert durch

$$\Pr[A|B] := \frac{Pr[A \cap B]}{Pr[B]}$$

> [!success] Allgemein
> - $\Pr[A|\Omega] = \Pr[A]$
> - $\Pr[A|A] = 1$
> - $\Pr[A|\bar{A}] = 0$
> - $\Pr[A \cap B] = \Pr[A|B] \cdot \Pr[B] = \Pr[B|A] \cdot \Pr[A]$
> - $\Pr[A \cap B] = Pr[A|B] \cdot Pr[B]$

> [!example]- 2-Kinder-Problem
> Familie hat 2 Kinder, mindestens ein Kind ist ein Mädchen. Was ist die Wahrscheinlichkeit, dass das andere Kind auch ein Mädchen ist. 
> 
> $\Omega = \{mm, mw, wm, ww\}$
>
> Ergeignis A: Beide Mädchen {ww}. $\Pr[A] = \frac{1}{4}$
> Ereignis B: Mindestens 1 Mädchen. $\Pr[B] = \frac{3}{4}$
>
> $\Pr[A|B] = \frac{1/4}{3/4} = \frac{1}{3}$


## Multiplikationssatz 

Wahrscheinlichkeit, dass mehrere Ereignisse zusammen (oder nacheinander) eintreten:

1. Wie wahrscheinlich ist das erste Ereignis?
2. Wie wahrscheinlich ist das zweite, **unter der Bedingung**, dass das erste schon passiert ist?
3. Wie wahrscheinlich ist das dritte, wenn die ersten beiden schon passiert sind? ... und so weiter.

![[Bildschirmfoto 2026-03-23 um 11.27.38.png]]

> [!example]- Geburtstagsproblem
> Jeder Ball wird zufällig in einen der 365 Körbe geworfen. *Was ist die Wahrscheinlichkeit, dass 2 Bälle im gleichen Korb landen?*, bzw. ==Komplementärereignis==: *Was ist die W'keit, dass alle Bälle in unterschiedlichen Körben landen?*
> - Bälle ($m$): Personen im Raum
> - Körbe ($n$): möglichen Geburtstage (365)
> 
> ![[Bildschirmfoto 2026-03-23 um 11.33.38.png]]
>
> **Vereinfachen**:
> $$
> \begin{aligned}
\left(1 - \frac{1}{n}\right) \left(1 - \frac{2}{n}\right) \dots \left(1 - \frac{m-1}{n}\right) &\approx e^{-\frac{1}{n}} \cdot e^{-\frac{2}{n}} \dots e^{-\frac{m-1}{n}} \\
&\approx e^{-\frac{1}{n} (1 + 2 + \dots + (m-1))} \\
&= e^{-\frac{(m-1) \cdot m}{2n}}
\end{aligned}
> $$


## Satz der totalen Wahrscheinlichkeit

Der Satz von der totalen Wahrscheinlichkeit berechnet die Gesamtwahrscheinlichkeit eines Ereignisses $B$, das über mehrere, sich gegenseitig ausschließende Wege ($A_1$ bis $A_n$) erreicht werden kann. Man multipliziert die Wahrscheinlichkeit jedes Weges mit der Wahrscheinlichkeit, dass $B$ auf genau diesem Weg eintritt, und summiert die Ergebnisse auf:
$$
\Pr[B] = \sum_{i=1}^{n} \Pr[B|A_i] \cdot \Pr[A_i]
$$

**Beweis:** 
 1. Zerlegen: Das Ereignis $B$ wird in nicht-überlappende Stücke aufgeteilt, basierend darauf, mit welchem $A_i$ es sich überschneidet: $B = (B \cap A_1) \cup \dots \cup (B \cap A_n)$.
2. Addieren: Da sich diese Stücke nicht überlappen, ist die Gesamtwahrscheinlichkeit von $B$ einfach die Summe der Wahrscheinlichkeiten dieser Stücke: $\Pr[B] = \sum \Pr[B \cap A_i]$.
3. Umformen: Die Definition der bedingten Wahrscheinlichkeit besagt, dass $\Pr[B \cap A_i] = \Pr[B|A_i] \cdot \Pr[A_i]$ ist. Setzt man dies in die Summe ein, erhält man die finale Formel.

![[Bildschirmfoto 2026-03-23 um 11.45.19.png]]

## Satz von Beyes

Seien $A_{1}, \dots, A_{n}$ paarweise disjunkte Ereignisse, und $B \subseteq A_{1} \cup \dots \cup A_{n}$ ein Ereignis mit $\Pr[B] > 0$. Für jedes $i \in \{1, \dots, n\}$ gilt

$$
\text{Pr}[A_i|B] = \frac{\text{Pr}[B|A_i] \cdot \text{Pr}[A_i]}{\sum_{j=1}^{n} \text{Pr}[B|A_j] \cdot \text{Pr}[A_j]}
$$

Beweis: siehe Bedingte Wahrscheinlichkeit und Satz der totalen Wahrscheinlichkeit

- $\Pr[B] = \sum_{i=1}^{n} \Pr[B|A_i] \cdot \Pr[A_i]$  
- $\Pr[A|B] := \frac{Pr[A \cap B]}{Pr[B]}$.

![[2nd Semester/AuW/Slides/08 Slides.pdf#page=5]]

