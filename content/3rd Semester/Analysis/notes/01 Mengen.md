
---

$A^\circ$ **Inneres**: ohne Randpunkte
$\overline A$ **Abschluss**: A plus Randpunkte
**Rand**: $\overline A\setminus A^\circ$ 

Beispiel: $A=(0,1]$
- $A^\circ=(0,1)$
- $\overline A=[0,1]$
- Rand: $\{0,1\}$

---

*Offenheit und Abgeschlossenheit sind unabhängig.*
## Offene Menge

- $A \subseteq \mathbb{R}^n \text{ offen} \iff \text{jeder Punkt hat einen Ball in A}.$
- Ball = Menge aller Punkte, die weniger als $r$ vom Mittelpunkt $x$ entfernt sind
- $B_r(x)=\{y\in \mathbb R^n \mid \|x-y\|<r\}$


Endlich viele Schnitte und beliebig viele Vereinigungen belassen diese Eigenschaft.

$$
A \text{ offen}
\iff
\text{jede konvergente Folge mit Grenzwert } x \in A \text{ gilt } \exists N \in \mathbb{N}, \forall n>N, x_{n} \in A
$$
## Abgeschlossene Menge

$$
A \subseteq \mathbb{R}^n \text{ ist abgeschlossen} \iff \mathbb{R}^n \setminus A \text{ ist offen}
$$


> [!NOTE] Beispiel
> $C = \{ (x,y) \in \mathbb{R}^2, x>0, y \ge 0 \}$
> - nicht offen
> - nicht abgeschlossen


Endliche Vereinigungen und beliebige Schnitte belassen diese Eigenschaft.

$$
A \text{ abgeschlossen}
\iff
\text{jede konvergente Folge in }A\text{ hat ihren Grenzwert wieder in }A.
$$

---

zeige, dass D nicht abgeschlossen ist 

*   $D = \left\{(x,y) \in \mathbb{R}^2 : y > x^2\right\}$
* Definiere $x_n = \left(0, \frac{1}{n}\right) \in D$
* $\lim_{n \to \infty} x_n = (0,0) \notin D$
