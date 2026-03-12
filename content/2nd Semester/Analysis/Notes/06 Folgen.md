## Darstellung einer Folge

![[2nd Semester/Analysis/Slides/03 Slides.pdf#page=5|03 Slides]]

## Konvergenz und Divergenz

==konvergent==: Folge hat ein *einziges*, ausgezeichnetes Langzeitverhalten zu dem 
Wenn nicht konvergent, dann ==divergent==. z.B. $a_{n} = (-1)^n$ ist **divergent**.
### Grenzwert

==Grenzwert== L (z.B. $1, \infty, - \infty$)
  $$\forall \varepsilon > 0 \; \exists N \in \mathbb{N}_0 \; \forall n \geq N : |a_n - L| < \varepsilon$$
→ alternativ: die Menge der Elemente NICHT in Nähe des Grenzwertes ist endlich

z.B. $b(n)=n^{-p}$ konvergiert für $p>0$, divergiert für $p < 0$.

### Beweis, Grenzwert ist unique

![[2nd Semester/Analysis/Slides/03 Slides.pdf#page=9|03 Slides]]
![[2nd Semester/Analysis/Slides/03 Slides.pdf#page=10|03 Slides]]


---

## Teilfolgen

Können Konvergenz auf bestimmten Teilfolgen beobachten. z.B. nur jedes dritte Folgeglied. 

> Haben wir eine konvergente Folge mit Grenzwert L, dann ==konvergiert auch jede Teilfolge zum gleichen Grenzwert L==. 

Können zeigen, dass gesamte Folge nicht konvergiert (divergent ist), indem wir 2 Teilfolgen finden, die unterschiedliche Grenzwerte haben. 

## Häufungspunkt

Sei $(a_n)_{n \in \mathbb{N}_0}$ eine Folge in $\mathbb{R}$. Häufungspunkt A:

$$\forall \varepsilon > 0 \; \forall N \in \mathbb{N}_0 \; \exists n \geq N : |a_n - A| < \varepsilon$$

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

![[2nd Semester/Analysis/Slides/04 Slides.pdf#page=14]]

> [!example] Beweis für iii)
> 1. Stelle Formel $\forall \varepsilon > 0 \; \exists N \in \mathbb{N}_0 \; \forall n \geq N : |a_n - L| < \varepsilon$ für $a$ und $b$ auf
> 2. Stelle Gleichung auf $|(a_{n} + b_{n})-(K+L)| = |(a_{n} - K) + (b_{n} - L)|$
> 3. Mit Dreiecksungleichung $|(a_{n} - K) + (b_{n} - L)| \leq |a_{n} - K| + |b_{n} - b| < \frac{\epsilon}{2} + \frac{\epsilon}{2}$ 
> 4. Die Definition $\forall \varepsilon > 0 \; \exists N \in \mathbb{N}_0 \; \forall n \geq N : |a_n - L| < \varepsilon$ gilt auch für $\frac{\epsilon}{2}$.
> 5. $\forall n \geq N:|(a_{n} + b_{n})-(K+L)| < \epsilon$, wobei $N=max(K,L)$ 


## Grenzwerte

1. Kann ich den schnellsten Term ausklammern? 
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

### Wurzeltrick

Bei Addition/Subtraktion von Wurzeln, Formel mit konjugierter Form erweitern (Bruch, im Prinzip $\cdot 1$), vereinfachen 

Beispiel: 

$$ \begin{aligned}
\lim_{ n \to \infty } n(\sqrt{ n+1 } - \sqrt{ n })  & = \lim_{ n \to \infty } n \cdot \frac{n+1-n}{\sqrt{ n+1 } + \sqrt{ n }}  \\
 & = \lim_{ n \to \infty } \frac{n}{\sqrt{ n+1 } + \sqrt{ n }}  \\
 & = \lim_{ n \to \infty }  \frac{\cancel{\sqrt{ n }} \cdot \sqrt{ n }}{\cancel{\sqrt{ n }} \left( \sqrt{ 1+\frac{1}{n} } + 1 \right)}  \\
 & = \lim_{ n \to \infty } \frac{\sqrt{ n }}{2}  \\
 & = \infty
\end{aligned} $$

### Sandwich Theorem

*Upper and lower bound finden, z.B. indem man Teil-Terme dropped*

Beispiel: 

$\lim_{ n \to \infty } \sqrt[n]{ 2n^2 + 5n }$

1. Abschätzungen $$\sqrt[n]{ 2n^2 } \leq \lim_{ n \to \infty } \sqrt[n]{ 2n^2 + 5n } \leq \sqrt[n]{ 2n^2 + 5n^2 } = \sqrt[n]{ 7n^2 }$$

2. $\lim_{ n \to \infty } \sqrt[n]{ 2n^2 } = \lim_{ n \to \infty } \sqrt[n]{ n } \cdot \sqrt[n]{ n } \cdot \sqrt[n]{ n } = 1 \cdot 1 \cdot 1 = 1$ 
3. $\lim_{ n \to \infty } \sqrt[n]{ 7n^2 } = 1$ 


![[2nd Semester/Analysis/Slides/04 Slides.pdf#page=16]]


### Abschätzungen, Euler

> [!success] Allgemein
> $$\lim_{ n \to \infty }\left( 1+\frac{1}{n} \right)^n = e$$
> $$\lim_{ n \to \infty }\left( 1+\frac{k}{n} \right)^{m\cdot n} = e^{k\cdot m}$$

$$\begin{align}
\lim_{ n \to \infty } \left( 1+\frac{1}{2n} \right)^n  & = \lim_{ n \to \infty } \left( \left( 1+\frac{1}{2n} \right)^{2n} \right)^{\frac{1}{2}} \\
 & = \left( \lim_{ n \to \infty } \left( 1+\frac{1}{2n} \right)^{2n} \right)^{\frac{1}{n}} \\
 & = (e)^{\frac{1}{2}} \\
 & = \sqrt{ e }
\end{align}$$


---

## MONTAG UND CO

Montag

![[2nd Semester/Analysis/Slides/04 Slides.pdf#page=17]]

> [!Note] 
> Jede beschränkte und monotone Folge konvergiert.

→ add in handwritten notes by Kobel-Keller for limes calculation
Limes und Grenzwerte 

