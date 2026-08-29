## Polynome als Ringe

$F[x]$ ... Polynom über einen Körper mit Koeffizienten aus F. $F[x]$ ist ein Ring.

z.B. 
$\mathbb R[x]$,  
$\mathbb Z_5[x]$

Da nur Konstanten (Grad 0) invertierbar sind, gilt $R[x]^* = R^*$

Wenn R ein Ring ist, dann ist $R[x]$ auch ein Ring

**==Anzahl Elemente in Polynomring==**: $\text{modulo Wert}^\text{höchster Grad des Polynoms}$

### Begriffe

#### Monisch

max. Potenz hat Koeffizient $1$

#### Grad

$\deg(x^5) = 5$ 
$\deg(x)=1$
$\deg(2) = 0$ 
$\deg(0) = -\infty$

#### Kardinalität

$|R[x]|=\infty$, auch wenn R endlich, z.B. $|R|=5$, da unendlich viele mögliche Grade
$|\mathbb{Z}_{2}[x]_{x^2 + 1}=2^2$ 

### Polynomdivision

z.B. über $\text{GF}(7) = \mathbb{Z}_7 \\[1em]$, also Koeffizienten immer mod 7
**Theorem 5.25**
Grad vom Rest r(x) ist kleiner als der von b(x)
$$
\begin{array}{l}
% Beschriftungen
\color{orange}{a(x)} \hspace{3.3cm} = \quad \color{orange}{b(x)} \qquad \ \ \cdot \quad \color{orange}{q(x)} \quad + \quad \color{orange}{r(x)} \\[5pt]

% Die Hauptgleichung
x^3 + 2x^2 + 5x + 4 \quad = \quad (2x^2 + x + 1)(4x + 6) + (2x + 5) \\

% Die schriftliche Division darunter
-(x^3 + 4x^2 + 4x) \\
\hline
% Erstes Ergebnis
\phantom{-(x^3+\,\,\,} 5x^2 + \phantom{1}x + 4 \\
% Zweite Subtraktion
\phantom{-(x^3+\,\,\,} -(5x^2 + 6x + 6) \\
\hline
% Rest
\phantom{-(x^3+\,\,\,-(5x^2+6x+\,} 2x + 5
\end{array}
$$
![[Zerlegungen mit Euklid.png]]

### Irreduzierbarkeit von Polynomen

#helpsheet Liste an irreduziblen Polynomen

1. $deg(a)\geq 1$
2. alle $p(x)$ mit $p(x)\ |\ a(x)$ $deg(p)=0$ oder p ist Vielfaches von a

Also *nicht-triviale Teiler haben Grad zwischen 0 und a*

- Ein Polynom ist reduzierbar, wenn es eine Nullstelle im betrachteten Körper hat. 
- **Bei Grad 1,2,3 gilt**: ein Polynom ist irreduzierbar, wenn es keine Nullstelle im betrachteten Körper hat. Ab Grad 4 gilt das nicht mehr, da wir Faktorisierungen als quadratisch $\times$ quadratisch haben könnten, ohne dass Nullstellen existieren. Grad 3: linear $\times$ quadratisch, also Nullstelle bei linear.

z.B. $(x^2+1)$ in $\mathbb R$ irreduzibel, in $\mathbb C$ nicht, da: $x^2+1 = (x+i)(x-i)$ 

---
### Auswertung
$$
\begin{align}
\alpha \text{ ist Nullstelle} &\Longleftrightarrow p(\alpha)=0 \\
&\Longleftrightarrow (x-\alpha) \ | \ p(x)
\end{align}
$$
Also ist $p(x)$ reduzibel, wenn es eine Nullstelle gibt. Die Umkehrung gilt nur bei Grad $\leq$ 3, siehe oben

---

## Polynome als Körper

- $\mathbb{Z}_{5}[x]$ ist kein Körper, da z.B. $x^2$ keine Inverse hat. Daher modulus, z.B: $\mathbb{Z}_{5}[x]_{x^2}$
- $F[x]_{m(x)}$ ist ein Körper für irreduzibles $m(x)$

> Es existiert ein Körper mit k Elementen $\Longleftrightarrow k=p^n \text{ mit p prin, n}\in \mathbb{N}$ 

**Rechenbeispiele**
- $3x^3 + 2 \equiv_{x^2} 2$

z.B. $\mathbb{Z}_{3}[x]_{x^3 + 2x + 1}$ ist ein Körper, da (quick-check) $\mathbb{Z}_{3}$ ein Körper ist und da $x^3+2x+1$ keine Nullstelle hat (ist also irreduzibel)

---
## Notizen 

![[DM Lecture 19-11-2025.pdf]]