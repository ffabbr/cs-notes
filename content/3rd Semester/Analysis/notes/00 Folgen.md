
## Einführung 

Da wir in $\mathbb R^n$ sind ist jedes Element der Folge selbst ein Vektor, keine Zahl. Somit ist der Abstand nicht mehr einfach der Betrag, sondern die **Norm**.

$(x_s)_{s\in\mathbb N}$ ist eine Folge, 
$x_s$ ist das s-te Element der Folge

$$
x_s=
\begin{pmatrix}
x_{1,s}\\
x_{2,s}\\
\vdots\\
x_{n,s}
\end{pmatrix}
$$

## Konvergenz

Die Folge konvergiert gegen einen Vektor $y\in\mathbb R^n$, wenn die Vektoren $x_{n}$ für grosse $n$ beliebig nahe an $y$ kommen.

Folge konvergiert $\iff$ jede Koordinate konvergiert

Formal: 
$$
\text{konvergiert} \iff \forall \varepsilon>0\ \exists N>0\ \text{sodass für alle } n>N:
\|x_n-y\|<\varepsilon
$$

Beispiel

$\lim_{n \to \infty} \left( \frac{1}{n}, \frac{1}{n^2}, 5 \right) = (0, 0, 5).$

Fixieren wir beliebiges $\varepsilon > 0$. Wir wollen zeigen, dass $N \in \mathbb{N}$ existiert, s.d. $\forall n > N$

$$
\begin{align*}
\|x_n - y\| &= \left\| \left( \frac{1}{n}, \frac{1}{n^2}, 5 \right) - (0, 0, 5) \right\| \\
&= \left\| \left( \frac{1}{n}, \frac{1}{n^2}, 0 \right) \right\| \\
&= \sqrt{\frac{1}{n^2} + \frac{1}{n^4} + 0^2} \\
&\overset{n \ge 1}{\le} \sqrt{\frac{1}{n^2} + \frac{1}{n^2}} \\
&= \frac{\sqrt{2}}{n} < \varepsilon \\
&\implies \frac{\sqrt{2}}{\varepsilon} < n \text{, wähle also } N = \left\lceil \frac{\sqrt{2}}{\varepsilon} \right\rceil
\end{align*}
$$
