## Darstellung einer Folge

![[2nd Semester/Analysis/Slides/03 Slides.pdf#page=5|03 Slides]]

## Konvergenz und Divergenz

- ==konvergent==: Folge strebt gegen konkreten, endlichen reellen Wert
- Wenn nicht konvergent, dann ==divergent==. z.B. $a_{n} = (-1)^n$ ist **divergent**.
- Differenz konvergenter Folgen konvergiert
- Gegenbeispiel für: Setze $a_n = (-1)^n$ und $b_n = -(-1)^n$. Dann ist $c_n = 0$ für alle $n$, also $\lim_{n\to\infty} c_n = 0$. Aber weder $(a_n)$ noch $(b_n)$ konvergiert.
- Falls $(a_n)$ konvergiert, ist die Folge $b_n = a_{n+1} + a_n$ konvergent.
$$
\lim_{n \to \infty} b_n = \lim_{n \to \infty} (a_{n+1} + a_n) = \lim_{n \to \infty} a_{n+1} + \lim_{n \to \infty} a_n = L + L = 2L
$$
### Grenzwert

==Grenzwert== L
$$
\forall \varepsilon > 0 \; \exists N \in \mathbb{N}_0 \; \forall n \geq N : |a_n - L| < \varepsilon
$$
→ alternativ: die Menge der Elemente NICHT in Nähe des Grenzwertes ist endlich

z.B. $b(n)=n^{-p}$ konvergiert für $p>0$, divergiert für $p < 0$.

### Beweis, Grenzwert ist unique

![[2nd Semester/Analysis/Slides/03 Slides.pdf#page=9|03 Slides]]
![[2nd Semester/Analysis/Slides/03 Slides.pdf#page=10|03 Slides]]


---

## Teilfolgen

Können Konvergenz auf bestimmten Teilfolgen beobachten. z.B. nur jedes dritte Folgeglied. 

> Eine Folge $(a_n)$ konvergiert gegen $L \iff$ Jede Teilfolge $(a_{n_k})$ konvergiert gegen $L$.

Können zeigen, dass gesamte Folge nicht konvergiert (divergent ist), indem wir 2 Teilfolgen finden, die unterschiedliche Grenzwerte haben. 

## Häufungspunkt

Sei $(a_n)_{n \in \mathbb{N}_0}$ eine Folge in $\mathbb{R}$. Häufungspunkt A:

$$
\forall \varepsilon > 0 \; \forall N \in \mathbb{N}_0 \; \exists n \geq N : |a_n - A| < \varepsilon
$$

> Es gibt unendlich viele Punkte die beliebig Nahe an den Häufunspunkt kommen. 

> [!success] Beispiel
> Die Folge $a_n = (-1)^n$ hat die Häufungspunkte $1$ und $-1$, aber **keinen** Grenzwert, weil sie immer zwischen beiden hin- und herspringt.

> [!example]
> Jede konvergente Folge in $\mathbb{R}$ hat ==genau einen Häufungspunkt== (den Grenzwert der Folge).

---

## Graphische Darstellung

1. auf einem Zahlenstrahl
2. als Punkte in der Ebene

---

Es gelte 
- $\lim_{n\to\infty} a_n = A (\neq \pm \infty)$
- $\lim_{n\to\infty} b_n = B (\neq \pm \infty)$
- $C$ ist eine Zahl

So gilt:

1. $\lim_{n\to\infty} (a_n + b_n) = A + B$
2. $\lim_{n\to\infty} (a_n - b_n) = A - B$
3. $\lim_{n\to\infty} (a_n \cdot b_n) = A \cdot B$
4. $\lim_{n\to\infty} (C \cdot a_n) = C \cdot A$
5. $B \neq 0 \wedge b_n \neq 0 \implies \lim_{n\to\infty} (a_n/b_n) = A/B$
6. $A < B \implies \exists N \in \mathbb{N} : a_n < b_n \quad \forall n \geq N$
7. $(\exists N \in \mathbb{N} : a_n \leq b_n \quad \forall n \geq N) \implies A \leq B$


> [!example] Beweis für iii)
> 1. Stelle Formel $\forall \varepsilon > 0 \; \exists N \in \mathbb{N}_0 \; \forall n \geq N : |a_n - L| < \varepsilon$ für $a$ und $b$ auf
> 2. Stelle Gleichung auf $|(a_{n} + b_{n})-(K+L)| = |(a_{n} - K) + (b_{n} - L)|$
> 3. Mit Dreiecksungleichung $|(a_{n} - K) + (b_{n} - L)| \leq |a_{n} - K| + |b_{n} - b| < \frac{\epsilon}{2} + \frac{\epsilon}{2}$ 
> 4. Die Definition $\forall \varepsilon > 0 \; \exists N \in \mathbb{N}_0 \; \forall n \geq N : |a_n - L| < \varepsilon$ gilt auch für $\frac{\epsilon}{2}$.
> 5. $\forall n \geq N:|(a_{n} + b_{n})-(K+L)| < \epsilon$, wobei $N=max(K,L)$ 


## Grenzwerte

1. Kann ich den [[#Schnellsten Term ausklammern|schnellsten Term ausklammern]] oder dividieren?  
2. [[#Wurzeltrick]]: Bei Addition/Subtraktion von Wurzeln, Formel mit konjugierter Form erweitern (Bruch, im Prinzip $\cdot 1$), vereinfachen 
3. [[#Sandwich Theorem]]
4. [[#Abschätzungen, Euler]]: Ähnlichkeit zu Folge e oder bekannter Folge aus den Regeln

> [!info]- Grenzwerte Regeln
> - $\lim_{n \to \infty} \frac{\log n}{n} = 0 = \lim_{n \to \infty} \frac{\ln n}{n}$
> - $\lim_{n \to \infty} n^{\frac{1}{n}} = 1$
> - $\lim_{n \to \infty} x^{1/n} = 1, x > 0$
> - $\forall x \in \mathbb{R} : \lim_{n \to \infty} \left(1 + \frac{x}{n}\right)^n = e^x$
> - $\forall x \in \mathbb{R} : \lim_{n \to \infty} \frac{x^n}{n!} = 0$
> - $\lim_{x \to \infty} \frac{1}{x} = 0$
> - $\lim_{x \to \infty} 1 + \frac{1}{x} = 1$
> - $\lim_{x \to \infty} e^x = \infty$
> - $\lim_{x \to -\infty} e^x = 0$
> - $\lim_{x \to \infty} e^{-x} = 0$
> - $\lim_{x \to -\infty} e^{-x} = \infty$
> - $\lim_{x \to \infty} \frac{e^x}{x^m} = \infty$
> - $\lim_{x \to -\infty} x e^x = 0$
> - $\lim_{x \to \infty} \ln(x) = \infty$
> - $\lim_{x \to 0} \ln(x) = -\infty$
> - $\lim_{x \to \infty} (1+x)^{\frac{1}{x}} = 1$
> - $\lim_{x \to 0} (1+x)^{\frac{1}{x}} = e$
> - $\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^b = 1$
> - $\lim_{x \to \infty} x^a q^x = 0, \forall 0 \le q < 1$
> - $\lim_{x \to \pm\infty} \left(1 + \frac{1}{x}\right)^x = e$
> - $\lim_{x \to \infty} \left(1 - \frac{1}{x}\right)^x = \frac{1}{e}$
> - $\lim_{x \to \pm\infty} \left(1 + \frac{k}{x}\right)^{mx} = e^{km}$
> - $\lim_{x \to 0} \frac{\sin x}{x} = 1$
> - $\lim_{x \to 0} \frac{1}{\cos(x)} = 1$
> - $\lim_{x \to 0} \frac{\cos x - 1}{x} = 0$
> - $\lim_{x \to 0} \frac{\log(1-x)}{x} = -1$
> - $\lim_{x \to 0} x \log x = 0$
> - $\lim_{x \to 0} \frac{1-\cos x}{x^2} = \frac{1}{2}$
> - $\lim_{x \to 0} \frac{e^x-1}{x} = 1$
> - $\lim_{x \to 0} \frac{x}{\arctan x} = 1$
> - $\lim_{x \to \infty} \arctan x = \frac{\pi}{2}$
> - $\lim_{x \to \infty} \left(\frac{x}{x+k}\right)^x = e^{-k}$
> - $\lim_{x \to 0} \frac{a^x-1}{x} = \ln(a) \ \forall a > 0$
> - $\lim_{x \to 0} \frac{e^{ax}-1}{x} = a$
> - $\lim_{x \to 0} \frac{\ln(x+1)}{x} = 1$
> - $\lim_{x \to 1} \frac{\ln(x)}{x-1} = 1$
> - $\lim_{x \to \infty} \frac{\ln(x)}{x} = 0$
> - $\lim_{x \to \infty} \frac{\log(x)}{x^a} = 0$
> - $\lim_{x \to \infty} \sqrt[x]{x} = 1$
> - $\lim_{x \to \infty} \frac{x}{2^x} = 0$
> - $\lim_{x \to \frac{\pi}{2}^-} \tan x = +\infty$
> - $\lim_{x \to \frac{\pi}{2}^+} \tan x = -\infty$
> - $\lim_{x \to \infty} \frac{\sin x}{x} = 0$
> - $\lim_{x \to 0^+} x \ln x = 0$

> $\lim_{n \to \infty} \sqrt[n]{x} = 1$ für beliebige $x, y$, auch z.B. bei $\lim_{n \to \infty} \sqrt[n]{n} = 1$


### Schnellsten Term ausklammern

Beispiel: 

$$
e_n = \sqrt[n]{5^n + 11^n + 17^n}
$$

Wir klammern $17^n$ aus

$$
e_n = \sqrt[n]{17^n\left(\left(\frac{5}{17}\right)^n + \left(\frac{11}{17}\right)^n + 1\right)} = 17 \cdot \sqrt[n]{\left(\frac{5}{17}\right)^n + \left(\frac{11}{17}\right)^n + 1}
$$
$\frac{5}{17} < 1$ und $\frac{11}{17} < 1$, konvergieren also gegen 0. Also
$$
\sqrt[n]{1} \leq \sqrt[n]{\left(\frac{5}{17}\right)^n + \left(\frac{11}{17}\right)^n + 1} \leq \sqrt[n]{3}
$$
Da $\sqrt[n]{3} \to 1$, per [[#Sandwich Theorem]], $\lim_{n \to \infty} e_n = 17 \cdot 1 = \boxed{17}$.

### Wurzeltrick

Bei Addition/Subtraktion von Wurzeln, Formel mit konjugierter Form erweitern (Bruch, im Prinzip $\cdot 1$), vereinfachen 

Beispiel: 

$$
\begin{aligned}
\lim_{ n \to \infty } n(\sqrt{ n+1 } - \sqrt{ n }) &= \lim_{n \to \infty} n \cdot \frac{(\sqrt{n+1} - \sqrt{n})(\sqrt{n+1} + \sqrt{n})}{\sqrt{n+1} + \sqrt{n}} \\
& = \lim_{ n \to \infty } n \cdot \frac{n+1-n}{\sqrt{ n+1 } + \sqrt{ n }}  \\
 & = \lim_{ n \to \infty } \frac{n}{\sqrt{ n+1 } + \sqrt{ n }}  \\
 & = \lim_{ n \to \infty }  \frac{\cancel{\sqrt{ n }} \cdot \sqrt{ n }}{\cancel{\sqrt{ n }} \left( \sqrt{ 1+\frac{1}{n} } + 1 \right)}  \\
 & = \lim_{ n \to \infty } \frac{\sqrt{ n }}{2}  \\
 & = \infty
\end{aligned}
$$


### Sandwich Theorem

*Upper and lower bound finden, z.B. indem man Teil-Terme dropped*

Beispiel: 

$\lim_{ n \to \infty } \sqrt[n]{ 2n^2 + 5n }$

1. Abschätzungen
$$
\sqrt[n]{ 2n^2 } \leq \lim_{ n \to \infty } \sqrt[n]{ 2n^2 + 5n } \leq \sqrt[n]{ 2n^2 + 5n^2 } = \sqrt[n]{ 7n^2 }
$$

2. $\lim_{ n \to \infty } \sqrt[n]{ 2n^2 } = \lim_{ n \to \infty } \sqrt[n]{ n } \cdot \sqrt[n]{ n } \cdot \sqrt[n]{ n } = 1 \cdot 1 \cdot 1 = 1$ 
3. $\lim_{ n \to \infty } \sqrt[n]{ 7n^2 } = 1$ 


![[2nd Semester/Analysis/Slides/04 Slides.pdf#page=16]]

### Abschätzungen, Euler

> [!success] Allgemein
>
$$
\lim_{ n \to \infty }\left( 1+\frac{1}{n} \right)^n = e
$$
>
$$
\lim_{ n \to \infty }\left( 1+\frac{k}{n} \right)^{m\cdot n} = e^{k\cdot m}
$$

$$
\begin{align}
\lim_{ n \to \infty } \left( 1+\frac{1}{2n} \right)^n  & = \lim_{ n \to \infty } \left( \left( 1+\frac{1}{2n} \right)^{2n} \right)^{\frac{1}{2}} \\
 & = \left( \lim_{ n \to \infty } \left( 1+\frac{1}{2n} \right)^{2n} \right)^{\frac{1}{n}} \\
 & = (e)^{\frac{1}{2}} \\
 & = \sqrt{ e }
\end{align}
$$


---

## Beschränkungen

- Eine Folge die nach oben und unten beschränkt ist, ist beschränkt. z.B. $(-1)^n$
- **monoton** fallend/wachsend: **strikte** Abnahme/Zunahme
- **streng monoton** fallend/wachsend: Abnahme/Zunahme oder gleich

> Immer wenn es einen **Limes Superior (Inferior) gibt**, gibt es auch eine **obere (untere) Schranke**


> [!Note] Lemmas
> - konvergente Folge $\implies$ beschränkt. 
> - **==beschränkt und monoton $\implies$ konvergiert==**
> - monotone Folge konvergiert $\iff$ beschränkt
> - beschränkte Folge hat mindestens einen Häufungspunkt **und konvergente Teilfolge** (Bolzano-Weierstrass)
> - konvergierend, monoton, beschränkt: vgl. Grenzwert mit [[01 Logik, Mengen, Zahlen#Intervalle|sup/inf von Intervallen]] 

![[Pasted image 20260317201505.png]]
### Konvergenz zeigen durch beschränkt und monoton, bei rekursiv definierter Folge

![[Bildschirmfoto 2026-03-17 um 19.35.20.png|590]]

---

## Limes Superior, Inferior

- beschreiben das Verhalten der oberen/unteren Schranke
- Jede beschränkte Folge hat lim sup und inf, auch, wenn keinen normalen Limes

- Folge konvergiert $\iff \limsup = \liminf$
- $(\limsup = \liminf) \land \text{beschränkt} \implies \text{Folge konvergiert}$
- $\limsup \neq \liminf \implies$ Folge divergent

- Der Limes superior (inferior) ist der **grösste (kleinste) Häufungspunkt** 
- Superior: $\lim_{n \to \infty} \sup \{ a_k \mid k \ge n \}$
- Inferior: $\lim_{n \to \infty} \inf \{ a_k \mid k \ge n \}$ 

**Wie beweisen?**

- [[#Sandwich Theorem]], oder
- Der lim einer konvergenten Folge (falls existent) ist auch ein Häufungspunkt. **Folge in Teilfolgen unterteilen**, z.B. gerade/ungerage, die ==alle== Stellen abdecken, dann **limes dieser Teilfolgen vergleichen**. Es kann keinen anderen Häufungspunkt geben, da diese Teillfolgen alles abdecken. Der Grenzwert einer Teilfolge ist der Häufungspunkt. Gilt auch als Beweis

![[Bildschirmfoto 2026-03-17 um 17.04.09.png|635]]

![[Bildschirmfoto 2026-03-17 um 20.15.53.png]]


---

## Cauchy-Folge

- konvergiert $\iff$ ist Cauchy-Folge 
- Folge ist beschränkt
- lim sup = lim inf $\implies$ ist Cauchy Folge
- der Abstand von zwei beliebigen Punkten ist $< \epsilon$ . 

$$
\forall \varepsilon > 0, \exists N \in \mathbb{N}, \forall m, n \geq N \quad |a_n - a_m| < \varepsilon
$$
- Konvergenz zeigen, wenn Grenzwert unbekannt, indem wir zeigen, dass eine Folge eine Cauchy-Folge ist

- $\sum_{k=1}^{n} \frac{1}{k^2}, n\geq_{1}$ ist eine Cauchy Folge, konvergiert
- $\sum_{k=1}^{\infty} \frac{1}{k}$ ist keine Cauchy Folge, divergiert

### Konvergenz zeigen durch Cauchy-Folge

- Beispiel, Beweis: $\frac{1}{n}$ konvergiert

![[Bildschirmfoto 2026-03-14 um 15.54.01.png|751]]


---

