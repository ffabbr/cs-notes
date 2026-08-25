**Gruppe:**  
- Menge mit **einer** Verknüpfung, jedes Element hat Inverse

**[[#Ring]]:**  $〈R,+, -, 0, \cdot, 1〉$ 
- Menge mit **zwei** Verknüpfungen (Addition und Multiplikation)
	- Unter Addition: **Gruppe**
- Nicht jedes Element hat multiplikatives Inverse

**[[#Körper]]:**  $〈R,+,-,0,\cdot, -1,1〉$
- Ring, **alle Elemente außer 0** haben Inverses in der Multiplikation ([[#Einheit]])

---

## Kurze Wiederholung

- $|Z_7| = 7$
- $|Z_7^*| = \varphi(7) = 6 \quad \text{(Anzahl teilerfremder Elemente)}$
	- $Z_7^* = \{1,2,3,4,5,6\}$
	- $Z_{12}^* = \{1,5,7,11\}$
- $Z_7^* = \langle 3 \rangle$
- $\text{GF}(7) = \mathbb{Z}_7$
- $|\text{GF}(p)^*| = p - 1$ wenn p prim (Anzahl invertierbarer Elemente)

---
## Ring

Ring $R = \langle R, +, \cdot, 0, 1 \rangle$

- $\langle R, +, 0 \rangle$ abelsche Gruppe  
- $\langle R, \cdot, 1 \rangle$ Monoid (nicht immer kommutativ)

In einem Ring gilt das *Distributivgesetz*.
### Nullteiler

Ein nicht-null Element, dass multipliziert mit einem nicht-null Element 0 ergibt.

$ab \equiv_m 0 \Rightarrow a \equiv_m 0 \ \text{oder}\ b \equiv_m 0$

z. B. 2 in $\mathbb Z_{2m}$

### Integritätsbereich

Ring ohne Nullteiler. 
R ist Integritätsbereich, wenn R keinen Nullteiler hat

z.B.
$\mathbb Z_5 = \{0,1,2,3,4\}$
gibt keine $a,b \ne 0$ mit $ab = 0$

z.B.
$\mathbb Z,\ \mathbb Q,\ \mathbb R,\ \mathbb C,\ \mathbb Z_m$ für m prim  

### Einheit

$a\cdot b = 1$ für ein $b \in R$
Alle Elemente die teilerfremd zur Gruppenordnung sind.

Notation: 
$\boxed{\text{R}^*}$ bedeutet alle Einheiten, also alle invertierbaren Elemente. 

### Irreduzibilität

Element, das keine (interessanten) Zerlegungen hat (z. B. Primzahlen). 
Einheiten zählen nicht als irreduzibel

![[06 Polynome#Irreduzierbarkeit von Polynomen]]

### Lemma 5.17

![[Lemma 5.17.png]]

### Polynomringe

→ siehe [[06 Polynome]]

## Körper

- Ring, aber jedes Element außer 0 hat ein Inverses. 
- Wenn Körper, dann auch Integritätsbereich.
- Alle Körper mit gleich vielen Elementen sind isomorph.
- Man kann rechnen wie mit normalen Zahlen. Die Division ist "mal das Inverse".
- Es gibt einen Körper mit x Elementen wenn x prim oder $x=p^k$ für p prim

**z.B.**
- $\mathbb{R}, \mathbb{Q}, \mathbb{C}$
- $〈\mathbb{Z}_m,+_{m},\cdot_{m}〉$ für ==m prim==
- $F[x]_{m(x)}$ für irreduzibles m(x)

---

### $F$ Körper $\Rightarrow F$ Integritätsbereich (kein Nullteiler)

*Beweis:* 

Sei $u \in F \setminus \{0\}$
$\underline{u \cdot v = 0} \Rightarrow v = 0$:
$$
\begin{aligned}
v &= 1 \cdot v \\
v &= u^{-1} \cdot \underbrace{u \cdot v}_{0 \text{ per Annahme}} \\
v &= u^{-1} \cdot 0 = 0
\end{aligned}
$$

**Def. „GF“**

$GF(p) = \mathbb{Z}_p$ für $p$ prim

---

![[DM Lecture Ringe und Körper.pdf]]