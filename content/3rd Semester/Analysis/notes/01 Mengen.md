$A^\circ$ **Inneres**: ohne Randpunkte, optimale offene Menge
$\overline A$ **Abschluss**: A plus Randpunkte
$\delta A$ **Rand**: $\overline A\setminus A^\circ$ 

Beispiel: $A=(0,1]$
- $A^\circ=(0,1)$
- $\overline A=[0,1]$
- Rand: $\{0,1\}$

---

*Offenheit und Abgeschlossenheit sind unabhängig.*
## Offene Menge

- $A \subseteq \mathbb{R}^n \text{ offen} \iff \text{jeder Punkt hat einen Ball in A}$ 
- Ball = Menge aller Punkte, die weniger als $r$ vom Mittelpunkt $x$ entfernt sind
- $B_r(x)=\{y\in \mathbb R^n \mid \|x-y\|<r\}$

Endlich viele Schnitte und beliebig viele Vereinigungen belassen diese Eigenschaft.

$$
A \text{ offen}
\iff
\text{jede konvergente Folge mit Grenzwert } x \in A \text{ gilt } \exists N \in \mathbb{N}, \forall n>N, x_{n} \in A
$$
*(jede Folge, die gegen einen Punkt in A konvergiert, ab einem bestimmten Schritt komplett innerhalb von A verläuft)*
## Abgeschlossene Menge

$$
A \subseteq \mathbb{R}^n \text{ ist abgeschlossen} \iff \mathbb{R}^n \setminus A \text{ ist offen}
$$

Endlich viele Vereinigungen und beliebige Schnitte belassen diese Eigenschaft.

$$
A \text{ abgeschlossen}
\iff
\text{jede konvergente Folge in }A\text{ hat ihren Grenzwert wieder in }A.
$$

Bsp. zeige, dass D nicht abgeschlossen ist 
*  $D = \left\{(x,y) \in \mathbb{R}^2 : y > x^2\right\}$
* Definiere $x_n = \left(0, \frac{1}{n}\right) \in D$
* $\lim_{n \to \infty} x_n = (0,0) \notin D$

---

> [!NOTE] Beispiel
> $C = \{ (x,y) \in \mathbb{R}^2, x>0, y \ge 0 \}$
> - nicht offen
> - nicht abgeschlossen

---

## Urbildkriterium

Ist $f: X\to Y$ eine stetige Funktion, $U \subseteq Y$ offen (abgeschlossen), dann ist auch das Urbild dieser Teilmenge offen (abgeschlossen) $f^{-1}(U)$. 

z.B. $C=\{(x, y):xy>1\}$. Definiere $f(x,y)=xy, U=(1, \infty)$. Das Urbild dieser Funktion auf U ist C. Nach dem Urbildkriterium ist also C auch offen.

z.B. $B=\{(x,y):x^2+y^2 \leq 4, y \geq x\}$. Ist eine Intersection von 2 Mengen, also $=\{(x,y):x^2+y^2 \leq 4\} \cap \{(x,y):y \geq x\}$. Nutze Urbildkriterium auf beiden Mengen separat. 1. $f_{1}(x,y)=x^2 + y^2, U=[0, 4] \text{ abgeschlossen}$. $f_{1}^{-1}(U)=\{(x,y):x^2+y^2 \leq 4\}$ 2. $f_{2}(x,y)=y-x, U=[0, \infty)$. 

