Differenzenquotient: mittlere Änderungsrate (Sekante)
**Differentialquotient**: Ableitung (Tangente):

Funktion an Stelle $x$ differenzierbar $\implies$ an Stelle $x$ stetig

**Keine Ableitung möglich an**
- Definitionslücken
- Sprungstellen/nicht stetig
- Knickstellen

Hilfreich: 
- $\ln(a^b) = b \cdot \ln(a)$
- darf log anwenden

### Ableitungsregeln

**Summenregel**
$$
(f + g)^{(n)}(x) = f^{(n)}(x) + g^{(n)}(x)
$$
**Produktregel**
$$
(f \cdot g)^{(n)}(x) = \sum_{k=0}^n \binom{n}{k} f^{(k)}(x) g^{(n-k)}(x)
$$

Spezialfall, $n=1$
$h(x) = f(x) \cdot g(x) \implies h'(x) = f'(x)g(x) + f(x)g'(x)$

**Kettenregel**
$$
(g \circ f)'(x) = g'(f(x))f'(x)
$$
(Voraussetzung f an $x_{0}$ und g an $f(x_{0})$ differenzierbar)

**Quotientenregel**
$$
\left(\frac{f}{g}\right)'(x) = \frac{f'(x)g(x) - f(x)g'(x)}{g(x)^2}
$$
($g(x_{0}) \neq 0$)

**Ableitung der Umkehrfunktion**

*Voraussetzungen*: Funktion stetig, bijektiv. Umkehrfunktion auch stetig. $x_{0}$ Häufungspunkt von D, f an $x_{0}$ differenzierbar

$$
\left(f^{-1}\right)'(y_0) = \frac{1}{f'(x_0)}
$$

**Quadratwurzel**

$$(\sqrt{x})'=\frac{1}{2\sqrt{x}}$$

| **Funktionstyp**         | **Funktion f(x)** | **Ableitung f′(x)**                   |
| ------------------------ | ----------------- | ------------------------------------- |
| Potenzfunktion           | $a \cdot x^p$     | $a \cdot p \cdot x^{p-1}$             |
| Natürliche Exponentialf. | $e^{u(x)}$        | $u'(x) \cdot e^{u(x)}$                |
| Allgemeine Exponentialf. | $a^x$             | $\ln(a) \cdot a^x$                    |
| Logarithmusfunktion      | $\ln(x)$          | $\frac{1}{x}$                         |
| Sinus                    | $\sin(x)$         | $\cos(x)$                             |
| Kosinus                  | $\cos(x)$         | $-\sin(x)$                            |
| Tangens                  | $\tan(x)$         | $\frac{1}{\cos^2(x)} = 1 + \tan^2(x)$ |
| x hoch x                 | $x^x$             | $x^x(\ln(x) + 1)$                     |


### Mehrfache Ableitungen

Die Menge aller $n$-fach stetig differenzierbarer Funktionen auf $D$bezeichnen wir mit $C^n(D)$.

**==Glatte Funktionen==:** Eine glatte Funktion ist eine Funktion, die man unendlich oft ableiten kann. $C^\infty(D) := \bigcap_{n=0}^\infty C^n(D)$


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


