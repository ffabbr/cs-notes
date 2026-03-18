
- eine Reihe ist die Summe der Glieder einer Folge
- darf NICHT umgeordnet werden

eine Reihe konvergiert, wenn die Folge der Teilsummen konvergiert: 
- **Teilsummen**: Summe der ersten $n$ Glieder der Reihe ($s_{1} = a_{1}, s_{2} = a_{1} + a_{2}, \dots$)
- $s_1, s_2, s_3, \dots$ bilden eine neue Folge

---

Reihe konvergiert $\implies$ Grenzwert der Summanden ist 0. 
Grenzwert der Summanden ist nicht 0 $\implies$ Reihe divergiert

==ACHTUNG== auf Implikationsrichtung. z.B. $\sum_{n=1}^{\infty} \frac{1}{n}$ divergiert, $\sum_{n=1}^{\infty} \frac{1}{n^2}$ konvergiert

---

- Folge monoton & beschränkt $\implies$ konvergiert
- Jede konvergente Folge ist beschränkt

---

> [!info]
> - Wenn $a_n \geq 0$ für alle n (nur nicht-negative Glieder): 
>   Die Folge der Teilsummen $s_1, s_2, s_3, \dots$, $s_{n} = \sum_{k=0}^{n} a_{k}$ ist monoton wachsend. 

## Rechenregeln

$$
\sum_{n=0}^{\infty} C \cdot a_n = C \cdot \sum_{n=0}^{\infty} a_n \quad (C \in \mathbb{R})
$$

$$
\sum_{n=0}^{\infty} (a_n + b_n) = \sum_{n=0}^{\infty} a_n + \sum_{n=0}^{\infty} b_n
$$

Das Konvergenzverhalten ändert sich nicht durch Weglassen endlicher Glieder. Somit gilt $\sum_{n=0}^{\infty} a_n \text{ konvergent} \iff \sum_{n=N}^{\infty} a_n \text{ konvergent}$, also:

$$
\underbrace{\sum_{n=0}^{\infty} a_n}_{\text{Gesamt}} = \underbrace{\sum_{n=0}^{N-1} a_n}_{\text{Endlicher Anfang}} + \underbrace{\sum_{n=N}^{\infty} a_n}_{\text{Unendlicher Rest}}
$$

## Beispiele

**Beispiel**

Konvergiert für $s > 1$ und divergiert für $s \leq 1$:

$$\sum_{k=1}^{\infty} \frac{1}{k^s} = \sum_{k=1}^{\infty} k^{-s}$$

**Beispiel**

- Reihe: $a \sum_{n=0}^{\infty} q^n$
- Partialsumme: $s_n = a + aq + aq^2 + \dots + aq^{n-1} = a \cdot \frac{1 - q^n}{1 - q}$
- Falls $|q| < 1$, konvergiert: $s = \lim_{n \to \infty} s_n = a \sum_{n=0}^{\infty} q^n = a \frac{1}{1 - q}$

---

## Vergleichskriterium

vgl. ähnlich wie [[06 Folgen#Sandwich Theorem|Sandwich-Theorem]] 

- Reihe $\sum_{n=0}^{\infty} b_n$, alle Glieder $\geq 0$
- 2 Vergleichsreihen mit $c_n \leq b_n \leq a_n$

**Majorantenkriterium**
"größere" Reihe $\sum_{n=0}^{\infty} a_n$ konvergiert (nimmt endlichen Wert an) $\implies$ "kleinere" Reihe $\sum_{n=0}^{\infty} b_n$ konvergiert

**Minorantenkriterium**
"kleinere" Reihe $\sum_{n=0}^{\infty} c_n$ divergiert (wächst gegen unendlich) $\implies$  "größere" Reihe $\sum_{n=0}^{\infty} b_n$ divergiert

![[Bildschirmfoto 2026-03-18 um 14.35.14.png]]

## Absolute und Bedingte Konvergenz

![[2nd Semester/Analysis/Slides/05 Slides.pdf#page=14]]

### Riemannscher Umordnungssatz 

![[2nd Semester/Analysis/Slides/05 Slides.pdf#page=15]]