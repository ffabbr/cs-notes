## Darstellung einer Folge

![[2nd Semester/Analysis/Slides/03 Slides.pdf#page=5|03 Slides]]

## Konvergenz und Divergenz

==konvergent==: Folge hat ein *einziges*, ausgezeichnetes Langzeitverhalten zu dem ==Grenzwert== L (z.B. $1, \infty, - \infty$)
  $$\forall \varepsilon > 0 \; \exists N \in \mathbb{N}_0 \; \forall n \geq N : |a_n - L| < \varepsilon$$

Wenn nicht konvergent, dann ==divergent==.

z.B. $b(n)=n^{-p}$ konvergiert für $p>0$, divergiert für $p < 0$.

![[2nd Semester/Analysis/Slides/03 Slides.pdf#page=9|03 Slides]]
![[2nd Semester/Analysis/Slides/03 Slides.pdf#page=10|03 Slides]]

## Teilfolgen

Können Konvergenz auf bestimmten Teilfolgen beobachten. z.B. nur jedes dritte Folgeglied. 

Haben wir eine konvergente Folge mit Grenzwert L, dann konvergiert auch jede Teilfolge zum gleichen Grenzwert L. 

## Häufungspunkt

Sei $(a_n)_{n \in \mathbb{N}_0}$ eine Folge in $\mathbb{R}$. Ein Punkt $A \in \mathbb{R}$ heisst **Häufungspunkt**, falls

$$\forall \varepsilon > 0 \; \forall N \in \mathbb{N}_0 \; \exists n \geq N : |a_n - A| < \varepsilon$$

Das bedeutet: In jedem Intervall $(A - \varepsilon, A + \varepsilon)$ liegen **unendlich viele** Folgenglieder. 

> [!success] Beispiel
> Die Folge $a_n = (-1)^n$ hat die Häufungspunkte $1$ und $-1$, aber **keinen** Grenzwert, weil sie immer zwischen beiden hin- und herspringt.

> [!example]
> Jede konvergente Folge in $\mathbb{R}$ hat ==genau einen Häufungspunkt== (den Grenzwert der Folge).

---

## Graphische Darstellung

1. auf einem Zahlenstrahl
2. als Punkte in der Ebene

---

![[2nd Semester/Analysis/Slides/04 Slides.pdf#page=14]]
![[2nd Semester/Analysis/Slides/04 Slides.pdf#page=15]]
![[2nd Semester/Analysis/Slides/04 Slides.pdf#page=16]]
![[2nd Semester/Analysis/Slides/04 Slides.pdf#page=17]]

> [!Note] 
> Jede beschränkte und monotone Folge konvergiert.

→ add in handwritten notes by Kobel-Keller for limes calculation