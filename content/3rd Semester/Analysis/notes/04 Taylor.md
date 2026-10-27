*Mehrdimensionale Taylorapproximation*

Im Eindimensionalen notieren wir z.B. fünfmal ableiten als $f^{(5)}(x)$. Im Mehrdimensionalen ist pro Ableitung relevant, nach welcher Variablen wir ableiten. 

- $\alpha = (\alpha_1, \alpha_2, \dots, \alpha_n)$ heisst **Multiindex**. 
- $|\alpha| := \alpha_1 + \dots + \alpha_n$ ist, wie oft abgeleitet wird. 
 - Jede Stelle steht für eine Variable. Wenn $\alpha = (3, 2)$ ist, leitest du insgesamt $5$-mal ab. 
- $\alpha! := \alpha_1! \cdots \alpha_n!$ 
- Ableitung $\partial^\alpha f$: "Leite $f$ $\alpha_1$-mal nach $x_1$ ab, dann $\alpha_2$-mal nach $x_2$ ab, etc."

**Theorem (Satz von Taylor)**
Einfachere Approximation der Umgebung von $x_{0}$ an $x_0 + h$. 

$$
f(x_0 + h) = \sum_{\alpha \in \mathbb{N}_0^n, \vert{}\alpha\vert{} \leq k} \frac{\partial^\alpha f(x_0)}{\alpha!} h^\alpha + R_{k+1}f(x_0, h)
$$
- Summe: alle Kombinationen von Ableitungen bis zur maximalen Tiefe $k$
- Bruch: wir berechnen Ableitung an $x_{0}$ und teilen durch die Multiindex-Fakultät
- $h^{\alpha}$ ist Entfernung zum Zielpunkt für jede Variable, potenziert mit den Zählern

Restterm:
$R_{k+1}f(x_0, h) := \int_0^1 (k+1)(1-t)^k \sum_{\alpha \in \mathbb{N}_0^n, |\alpha|=k+1} \frac{\partial^\alpha f(x_0 + th)}{\alpha!} h^\alpha dt$

## Quadratische Approximation (2. Grades)

$$
T_2(x,y) = \underbrace{f(0,0)}_{\text{Startwert}} + \underbrace{f_x(0,0) \cdot x + f_y(0,0) \cdot y}_{\text{1. Ableitungen (Steigung)}} + \underbrace{\frac{f_{xx}(0,0)}{2} \cdot x^2 + f_{xy}(0,0) \cdot xy + \frac{f_{yy}(0,0)}{2} \cdot y^2}_{\text{2. Ableitungen (Krümmung)}}
$$
$$
\begin{align*} f(p+h) &= f(p) + \nabla f(p)^T h + \frac{1}{2} h^T H_f(p) h + O(\Vert{}h\Vert{}^2) \quad \text{f. } h \to 0 \end{align*}
$$

![[Bildschirmfoto 2026-10-25 um 21.31.49.png]]

### Example

![[Bildschirmfoto 2026-10-17 um 16.56.26.png]]



## Substitution

![[Bildschirmfoto 2026-10-26 um 16.20.23.png]]