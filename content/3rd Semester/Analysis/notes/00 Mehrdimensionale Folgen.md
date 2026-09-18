
## Einführung 

Da wir in $\mathbb R^n$ sind ist jedes Element der Folge selbst ein Vektor, keine Zahl. Somit ist der Abstand nicht mehr einfach der Betrag, sondern die **Norm**.

$(x_s)_{s\in\mathbb N}$ ist eine Folge, 
$x_s$ ist das s-te Element der Folge

$$
x_s=
\begin{pmatrix}
x_{1,s}\\
x_{2,s}\\
\vdots\\
x_{n,s}
\end{pmatrix}
$$

## Konvergenz

Die Folge konvergiert gegen einen Vektor $y\in\mathbb R^n$, wenn die Vektoren $x_{n}$ für grosse $n$ beliebig nahe an $y$ kommen.

Formal: 
$$
\forall \varepsilon>0\ \exists N>0\ \text{sodass für alle } n>N:
\|x_n-y\|<\varepsilon
$$

> Der Grenzwert einer konvergenten Folge ist eindeutig. 

> Folge konvergiert $\iff$ jede einzelne Koordinate konvergiert

## Ball

**offener Ball** = Menge aller Punkte, die weniger als $r$ von einem Mittelpunkt $x$ entfernt sind.

$$
B_r(x)=\{y\in \mathbb R^n \mid \|x-y\|<r\}
$$
Achtung, Rand gehört nicht dazu, es steht ja $<$.

## Mengen

**offene Menge**: für jeden Punkt in der Menge gibt es einen Ball (kein Punkt von A liegt "direkt am Rand" der Menge). Endliche Schnitte und beliebige Vereinigungen belassen diese Eigenschaft.

$$
A \text{ offen}
\iff
x_n\to x\in A \Rightarrow x_n\in A \text{ ab einem gewissen }N.
$$
$$
\text{Grenzwert liegt in }A \Rightarrow \text{ Folge liegt irgendwann in }A
$$

**abgeschlossene Menge**: sonst. Endliche Vereinigungen und beliebige Schnitte belassen diese Eigenschaft.

$$
A \text{ abgeschlossen}
\iff
\text{jede Folge in }A\text{ hat ihren Grenzwert wieder in }A.
$$
$$
\text{Folge liegt in }A \Rightarrow \text{ Grenzwert liegt in }A
$$

---

$A^\circ$ **Inneres**: ohne Randpunkte
$\overline A$ **Abschluss**: A plus Randpunkte
**Rand**: $\overline A\setminus A^\circ$ 

Beispiel: $A=(0,1]$
- $A^\circ=(0,1)$
- $\overline A=[0,1]$
- Rand: $\{0,1\}$

---