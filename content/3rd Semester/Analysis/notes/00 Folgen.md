
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

---

**Aufgabe**
- $A = \{(x,y) \in \mathbb{R}^2 : x^2 + y^2 \le 1\}.$
- Sei $(x_k)$ eine Folge in $A$ mit $x_k \to x \in \mathbb{R}^2.$
- Zeigen Sie, dass $x \in A$ gilt.

Die Folge $(x_k)$ besteht aus Vektoren im $\mathbb{R}^2$. Wir schreiben die einzelnen Folgenglieder in Koordinatenform als $x_k = (a_k, b_k)$. Den Grenzwert $x$, gegen den die Folge konvergiert, definieren wir analog als $x = (a, b)$. Da $x_{k}$ konvergiert konvergieren auch die einzelnen Koordinaten $a_{k}$ und $b_{k}$. 

Jedes Folgenglied $x_k$ liegt laut Angabe in der Menge $A$. Daher erfüllen alle Koordinaten $a_k^2 + b_k^2 \le 1$. 

Wir wenden den Limes an: $\lim_{k \to \infty} (a_k^2 + b_k^2) = (\lim_{k \to \infty} a_k)^2 + (\lim_{k \to \infty} b_k)^2 = a^2 + b^2$. Somit $a^2 + b^2 \le 1$. Die Koordinaten $(a, b)$ des Grenzwerts $x$ erfüllen die Ungleichung $a^2 + b^2 \le 1$. Somit liegt $x \in A$.