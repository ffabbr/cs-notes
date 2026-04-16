## Differenzenquotient

![[Bildschirmfoto 2026-04-15 um 13.49.21.png]]


## Ableitung (Differentialquotient)

- momentane Anderungsrate
- Steigung der Tangente

- Funktion an Stelle $x$ differenzierbar $\implies$ an Stelle $x$ stetig

**Keine Ableitung möglich an**
- Definitionslücken
- Sprungstellen/nicht stetig
- Knickstellen

### Einseitige Ableitungen

![[Bildschirmfoto 2026-04-13 um 00.16.35.png]]

| **Funktion f(x)** | **Ableitung f′(x)**         | **Erklärung**                                    |
| ----------------- | --------------------------- | ------------------------------------------------ |
| $e^x$             | $e^x$                       | Die Ableitung von $x$ ist 1, also $e^x \cdot 1$. |
| $e^{5x}$          | $5e^{5x}$                   | Die Ableitung von $5x$ ist 5.                    |
| $e^{x^2}$         | $2x \cdot e^{x^2}$          | Die Ableitung von $x^2$ ist $2x$.                |
| $e^{\sin(x)}$     | $\cos(x) \cdot e^{\sin(x)}$ | Die Ableitung von $\sin(x)$ ist $\cos(x)$.       |


### Mehrfache Ableitungen

Die Menge aller $n$-fach stetig differenzierbarer Funktionen auf $D$bezeichnen wir mit $C^n(D)$.

**==Glatte Funktionen==:** Eine glatte Funktion ist eine Funktion, die man unendlich oft ableiten kann. $C^\infty(D) := \bigcap_{n=0}^\infty C^n(D)$

### Ableitungsregeln

![[Bildschirmfoto 2026-04-15 um 13.55.07.png]]

Ausserdem: 



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

### Lokale Extremstellen

Wenn es eine lokale Extremstelle $x_{0}$ gibt, so ist sie entweder

1. am Rand des Intervalls (Endpunkt)
2. an einem Knick ($f$ ist an $x_{0}$ nicht differenzierbar)
3. an waagrechten Stelle ($f'(x_{0})=0$)

### Satz von Rolle

Funktion im Intervall $[a,b]$ **stetig** und **differenzierbar**. Wenn $f(a) = f(b)$, dann gibt es eine Stelle $x \in (a,b)$ mit $f(x)=0$. 

### Mittelwertsatz

Funktion im Intervall $[a,b]$ **stetig** und **differenzierbar**. Es gibt eine Stelle $x$, an der der Wert der Ableitung genau der Differenzenquotient (Durchschnitt) ist.

$$
f'(x) = \frac{f(b) - f(a)}{b - a}
$$


