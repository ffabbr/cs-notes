Das Eintreten von B ändert die Wahrscheinlichkeit von A nicht. 

$$
\Pr[A|B] = \Pr[A]
$$

Wenn wir die Formel für die bedingte Wahrscheinlichkeit nehmen, können wir $\Pr[A|B] := \frac{Pr[A \cap B]}{Pr[B]}$ umformen auf 

$$
\Pr[A \cap B] = \Pr[A] \cdot \Pr[B]
$$

> [!warning]
> Unabhängigkeit ist oft nicht offensichtlich
> 
> ![[2nd Semester/AuW/Slides/08 Slides.pdf#page=8]]

## Unabhängigkeit mehrerer Ereignisse

### Variante A

![[Bildschirmfoto 2026-03-25 um 10.32.33.png]]

$s = (s_1, \dots, s_n) \in \{0, 1\}^n$

- die Gleichung für **jede mögliche Kombination** von Nullen und Einsen (Ereignis, Komplementärereignis) stimmen.
- bei $n=3$ Ereignissen gibt es $2^3 = 8$ Kombinationen

$\text{Pr} \left[ \bigcap_{j=1}^n A_j^{s_j} \right]$

- *"Wie hoch ist die Wahrscheinlichkeit, dass genau diese spezifische Kombination von Ereignissen und Nicht-Ereignissen eintritt?"*
- die n Ereignisse sollen gleichzeitig auftreten (UND). 
- $s_{j}$ besagt ob das Ereignis eintreten soll oder nicht (komplementär)

$\prod_{j=1}^n \text{Pr} \left[ A_j^{s_j} \right]$

- Wahrscheinlichkeit für jedes einzelne Ereignis in dem Zustand, den wir gewählt haben

> [!info]- Beweis
> ![[2nd Semester/AuW/Slides/08 Slides.pdf#page=19]]
> ![[2nd Semester/AuW/Slides/08 Slides.pdf#page=20]]

---

### Variante B

![[2nd Semester/AuW/Slides/08 Slides.pdf#page=16]]
![[Bildschirmfoto 2026-03-25 um 10.16.14.png]]

---

## Unabhängigkeit bei Vereinigung und Schnitt

$A$, $B$ und $C$ unabhängig. 
$\implies$ $A \cap B$ und $C$ unabhängig
$\implies$ $A \cup B$ und $C$ unabhängig

> [!example]- Proof
> Beweis: 
> 
> (1) 
> $\Pr[(A \cap B) \cap C] = \underbrace{\Pr[A] \cdot \Pr[B]}_{\Pr[A \cap B]} \cdot \Pr[C] = \Pr[A \cap B] \cdot \Pr[C]$
> 
> (2)
> $$
   \begin{align*}
\Pr[(A \cup B) \cap C] &= \Pr[(A \cap C) \cup (B \cap C)] && \\
&= \Pr[A \cap C] + \Pr[B \cap C] - \Pr[A \cap B \cap C] && \text{(Siebformel)} \\
&= \Pr[C] \cdot (\Pr[A] + \Pr[B] - \Pr[A \cap B]) && \text{(Unabhängigkeit von } A, B, C\text{)} \\
&= \Pr[C] \cdot \Pr[A \cup B] && \text{(Siebformel)} \quad \blacksquare
\end{align*}
$$