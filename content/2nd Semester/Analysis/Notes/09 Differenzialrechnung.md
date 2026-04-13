
## Ableitung

Funktion an Stelle $x$ differenzierbar $\implies$ an Stelle $x$ stetig

### Einseitige Ableitungen

![[Bildschirmfoto 2026-04-13 um 00.16.35.png]]

### Mehrfache Ableitungen

Die Menge aller $n$-fach stetig differenzierbarer Funktionen auf $D$bezeichnen wir mit $C^n(D)$.

**Glatte Funktionen:** Eine glatte Funktion ist eine Funktion, die man unendlich oft ableiten kann. $C^\infty(D) := \bigcap_{n=0}^\infty C^n(D)$

### Rechenregeln

**Summenregel**
$$
(f + g)^{(n)}(x_0) = f^{(n)}(x_0) + g^{(n)}(x_0)
$$
**Produktregel**
$$
(f \cdot g)^{(n)}(x_0) = \sum_{k=0}^n \binom{n}{k} f^{(k)}(x_0) g^{(n-k)}(x_0)
$$
**Kettenregel**
$$
(g \circ f)'(x_0) = g'(f(x_0))f'(x_0)
$$
(Voraussetzung f an $x_{0}$ und g an $f(x_{0})$ differenzierbar)

**Quotientenregel**
$$
\left(\frac{f}{g}\right)'(x_0) = \frac{f'(x_0)g(x_0) - f(x_0)g'(x_0)}{g(x_0)^2}
$$
($g(x_{0}) \neq 0$)

**Ableitung der Umkehrfunktion**

*Voraussetzungen*: Funktion stetig, bijektiv. Umkehrfunktion auch stetig. $x_{0}$ Häufungspunkt von D, f an $x_{0}$ differenzierbar

$$
\left(f^{-1}\right)'(y_0) = \frac{1}{f'(x_0)}
$$

### Extremstellen

![[Bildschirmfoto 2026-04-13 um 00.27.31.png]]

![[Bildschirmfoto 2026-04-13 um 00.28.52.png]]

![[Bildschirmfoto 2026-04-13 um 00.29.03.png]]
