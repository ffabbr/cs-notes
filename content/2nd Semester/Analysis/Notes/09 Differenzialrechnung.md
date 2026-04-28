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
$$
h(x) = f(x) \cdot g(x) \implies h'(x) = f'(x)g(x) + f(x)g'(x)
$$

**Kettenregel**
$$
(g \circ f)'(x) = g'(f(x))f'(x)
$$
(Voraussetzung f an $x_{0}$ und g an $f(x_{0})$ differenzierbar)

**Quotientenregel**
$$
\left(\frac{f}{g}\right)'(x) = \frac{f'(x)g(x) - f(x)g'(x)}{g(x)^2}
$$

**Ableitung der Umkehrfunktion**

*Voraussetzungen*: Funktion stetig, bijektiv. Umkehrfunktion auch stetig. $x_{0}$ Häufungspunkt von D, f an $x_{0}$ differenzierbar

$$
\left(f^{-1}\right)'(y_0) = \frac{1}{f'(x_0)}
$$

| **Funktion f(x)**          | **Ableitung f′(x)**                   |
| -------------------------- | ------------------------------------- |
| $a \cdot x^p$              | $a \cdot p \cdot x^{p-1}$             |
| $x^n$                      | $n \cdot x^{n-1}$                     |
| $e^{u(x)}$                 | $u'(x)\cdot e^{u(x)}$                 |
| $e^x$                      | $e^x$                                 |
| $a^x$                      | $\ln(a)\cdot a^x$                     |
| $mx + b$                   | $m$                                   |
| $\ln(x)$                   | $\frac{1}{x}$                         |
| $\log_a(x)$                | $\frac{1}{x\ln(a)}$                   |
| $\sin(x)$                  | $\cos(x)$                             |
| $\cos(x)$                  | $-\sin(x)$                            |
| $\tan(x)$                  | $\frac{1}{\cos^2(x)} = 1+\tan^2(x)$   |
| $\cot(x)$                  | $-\frac{1}{\sin^2(x)}$                |
| $\sinh(x)$                 | $\cosh(x)$                            |
| $\cosh(x)$                 | $\sinh(x)$                            |
| $\tanh(x)$                 | $\frac{1}{\cosh^2(x)} = 1-\tanh^2(x)$ |
| $\coth(x)$                 | $1+\coth^2(x)$                        |
| $\arcsin(x)$               | $\frac{1}{\sqrt{1-x^2}}$              |
| $\arccos(x)$               | $-\frac{1}{\sqrt{1-x^2}}$             |
| $\arctan(x)$               | $\frac{1}{1+x^2}$                     |
| $\text{arccot}(x)$         | $-\frac{1}{1+x^2}$                    |
| $\operatorname{arsinh}(x)$ | $\frac{1}{\sqrt{1+x^2}}$              |
| $\operatorname{arcosh}(x)$ | $\frac{1}{\sqrt{x^2-1}}$              |
| $\operatorname{artanh}(x)$ | $\frac{1}{1-x^2}$                     |
| $x^x$                      | $x^x(\ln(x)+1)$                       |
| $\sqrt{x}$                 | $\frac{1}{2\sqrt{x}}$                 |
| $r \cdot g(x)$             | $r \cdot g'(x)$                       |
| $\frac{1}{x}$              | $-\frac{1}{x^2}$                      |

### Mehrfache Ableitungen

Die Menge aller $n$-fach stetig differenzierbarer Funktionen auf $D$bezeichnen wir mit $C^n(D)$.

**==Glatte Funktionen==:** Eine glatte Funktion ist eine Funktion, die man unendlich oft ableiten kann. $C^\infty(D) := \bigcap_{n=0}^\infty C^n(D)$


### Extremstellen

### Lokale Extremstellen

Wenn es eine lokale Extremstelle $x_{0}$ gibt, so ist sie entweder

1. am Rand des Intervalls (Endpunkt)
2. an einem Knick ($f$ ist an $x_{0}$ nicht differenzierbar)
3. an waagrechten Stelle ($f'(x_{0})=0$)

### Mittelwertsatz

$f:[a,b] \to \mathbb{R}$ auf $[a,b]$ **stetig** und auf $(a,b)$ **differenzierbar**. 
Es gibt eine Stelle $x$, an der der Wert der Ableitung genau der Differenzenquotient (Durchschnitt) ist.

$$
f'(x) = \frac{f(b) - f(a)}{b - a}
$$

![[Bildschirmfoto 2026-04-27 um 16.58.23.png]]

### Satz von Rolle

Funktion im Intervall $[a,b]$ **stetig** und **differenzierbar**. Wenn $f(a) = f(b)$, dann gibt es eine Stelle $x \in (a,b)$ mit $f(x)=0$. 

Spezialfall vom Mittelwertsatz mit $f(a)=f(b)$, somit $f(a)-f(b)=0$ und $f'(x)=0$.

![[Bildschirmfoto 2026-04-27 um 17.02.00.png]]


---


![[Bildschirmfoto 2026-04-23 um 12.53.17.png]]![[Bildschirmfoto 2026-04-23 um 13.19.47.png]]
![[Bildschirmfoto 2026-04-26 um 16.08.08.png]]

---

## Bernoulli-l’Hospital

![[Bildschirmfoto 2026-04-23 um 14.08.58.png]]
Es kann z.B. $\frac{\infty}{-\infty}$ sein, es geht nur um den Betrag. 

Beispiel: 
$$
\lim_{ x \to \infty } x\cdot\ln(x)=\lim_{ x \to \infty } \frac{\ln(x)}{1/x}=\lim_{ x \to \infty } \frac{1/x}{1/x^2}=0
$$

## Krümmung

Die Verknüpfung 2 konvexer Funktionen, wobei die äussere monoton wachsend ist, ist wieder konvex.

![[Bildschirmfoto 2026-04-27 um 17.47.50.png]]

