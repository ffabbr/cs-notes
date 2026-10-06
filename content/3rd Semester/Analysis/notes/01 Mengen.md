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

**Offene Mengen durch Bälle**
- $A \subseteq \mathbb{R}^n \text{ offen} \iff \text{jeder Punkt hat einen Ball in A}$ 
- Ball = Menge aller Punkte, die weniger als $r$ vom Mittelpunkt $x$ entfernt sind
- $B_r(x)=\{y\in \mathbb R^n \mid \|x-y\|<r\}$

**Offene Mengen durch Kombinationen** 
- Endlich viele Schnitte und beliebig viele Vereinigungen belassen diese Eigenschaft.

**Offene Mengen durch konvergente Folgen**
- jede Folge, die gegen einen Punkt in A konvergiert, ab einem bestimmten Schritt komplett innerhalb von A verläuft
- $A \text{ offen} \iff \text{jede konvergente Folge mit Grenzwert } x \in A \text{ gilt } \exists N \in \mathbb{N}, \forall n>N, x_{n} \in A$

**Offene Mengen durch Urbildkriterium**
- Ist $f: X\to Y$ eine stetige Funktion, $U \subseteq Y$ offen (abgeschlossen), dann ist auch das Urbild dieser Teilmenge offen (abgeschlossen) $f^{-1}(U)$
- finde eine Funktion $f$, die den Term in der Bedingung der Menge beschreibt. Zeige, dass $f$ stetig ist. Drücke die Menge als das Urbild $f^{-1}(I)$ eines Intervalls aus. Prüfe von $I$ offen oder abgeschlossen ist. Diese Eigenschaft überträgt sich dann direkt auf M. 
- Bsp.: $M = \{ (x,y) \in \mathbb{R}^2 \mid x^2 + y^2 < 1 \}$ 
	- definiere $f(x,y) = x^2 + y^2$
	- Funktionswerte also $(-\infty, 1)$ 
	- M als Urbild schreiben $M = f^{-1}((-\infty, 1))$ 
	- Da $(-\infty, 1)$ offen ist und $f$ stetig, ist $M$ offen
## Abgeschlossene Menge

**Abgeschlossene Mengen durch Komplement**
- $A \subseteq \mathbb{R}^n \text{ ist abgeschlossen} \iff \mathbb{R}^n \setminus A \text{ ist offen}$
- z.B. $[0, \infty)$ ist abgeschlossen, da das Komplement ist $(-\infty, 0)$. Das ist offen. Somit abgeschlossen.

**Abgeschlossene Mengen durch Kombinationen**
- Endlich viele Vereinigungen und beliebige Schnitte belassen diese Eigenschaft.

**Abgeschlossene Mengen durch konvergente Folgen**
- $A \text{ abgeschlossen} \iff \text{jede konvergente Folge in }A\text{ hat ihren Grenzwert wieder in }A.$
- Beispiel: zeige, dass D nicht abgeschlossen ist 
	*  $D = \left\{(x,y) \in \mathbb{R}^2 : y > x^2\right\}$
	* Definiere $x_n = \left(0, \frac{1}{n}\right) \in D$
	* $\lim_{n \to \infty} x_n = (0,0) \notin D$

**Abgeschlossene Menge durch Urbildkriterium**
- siehe oben
- Beispiel: $M = \{ (x,y,z) \in \mathbb{R}^3 \mid z - e^{x+y} \ge 0 \}$
	- definiere $f(x,y,z) = z - e^{x+y}$
	- Funktionswerte sind $[0, \infty)$, da $\geq 0$
	- $[0, \infty)$ ist abgeschlossen 
	- somit ist $M$ abgeschlossen
- Beispiel: $B=\{(x,y):x^2+y^2 \leq 4, y \geq x\}$ 
	- wir zerlegen in $B = B_1 \cap B_2$ 
	- $B_1 = \{(x,y) \in \mathbb{R}^2 \mid x^2 + y^2 \leq 4\}$. Definiere $f_1(x,y) = x^2 + y^2$ mit Intervall $U_{1} = [0, 4]$ oder $U_1 = (-\infty, 4]$. Intervall ist abgeschlossen. Somit ist $B_{1}$ abgeschlossen. 
	- $B_2 = \{(x,y) \in \mathbb{R}^2 \mid y \geq x\}$. Definiere $f_2(x,y) = y - x$. Intervall $[0, \infty)$. Intervall ist abgeschlossen. Somit ist $B_{2}$ abgeschlossen. 
	- Schnittmengen behalten Abgeschlossenheit. 

---

> [!NOTE] Beispiel
> $C = \{ (x,y) \in \mathbb{R}^2, x>0, y \ge 0 \}$
> - nicht offen
> - nicht abgeschlossen



