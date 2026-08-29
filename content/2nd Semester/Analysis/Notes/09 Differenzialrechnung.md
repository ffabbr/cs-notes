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
### Tabelle

→ [[13 Tabelle]]

### Mehrfache Ableitungen

Die Menge aller $n$-fach stetig differenzierbarer Funktionen auf $D$ bezeichnen wir mit $C^n(D)$. 

**==Glatte Funktionen==:** Eine glatte Funktion ist eine Funktion, die man unendlich oft ableiten kann. $C^\infty(D) := \bigcap_{n=0}^\infty C^n(D)$


## Extremstellen

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

Konvex: lokales minimum ist auch globales minimum. 

**Wendepunkt**: Krümmung ändert sich
- Vorzeichenwechsel von $f''$ bei $x_0$ $\Rightarrow$ Wendepunkt
- und $f'''(x_0)\neq 0$ $\Rightarrow$ Wendepunkt

**Sattelpunkt**: $f'(x)=0$, $f''(x)=0$ und **$f'''(x)\neq 0$

![[Bildschirmfoto 2026-04-27 um 17.47.50.png]]

