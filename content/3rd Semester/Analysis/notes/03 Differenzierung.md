## Partielle Ableitung

Wähle Zielvariable, betrachte die andere als Konstante und leite normal ab.

$$
\begin{align}
f_i(x) =\frac{\partial f}{\partial x_i}(x) &= \lim_{h \to 0} \frac{f(x + he_i) - f(x)}{h} \\
&= \lim_{h \to 0} \frac{f(x_1, \dots, x_i + h, \dots, x_n) - f(x_1, \dots, x_i, \dots, x_n)}{h}
\end{align}
$$

## Differential

Im Eindimensionalen haben wir durch die Ableitung (Tangente) den nächsten Wert approximieren können: $f(z+h) = f(z) + f'(z) \cdot h + \text{Rest}$ (forme um auf $f'(z)$). Im Mehrdimensionalen haben wir z.B. eine Ebene, nicht eine Gerade.

Eine Funktion ist an einer Stelle $x$ **differenzierbar**, falls es eine **lineare Abbildung** $L$ (z.B. Matrix) gibt, die die Funktion bei $x$ nahezu perfekt approximiert. 
$$
\lim_{h \to 0} \frac{\vert{}\vert{}f(x + h) - f(x) - L(h)\vert{}\vert{}}{\vert{}\vert{}h\vert{}\vert{}} = 0
$$
- $f(x + h) - f(x)$ ist Änderung der Funktion
- $L(h)$ ist durch Matrix vorrausgesagte Änderung

**Globale Differenzierbarkeit**: gibt für jeden Punkt ein solches $L$.

### Gradient-Vektor

mehrere Variablen Input, eine Zahl Output

**Visuell**: Pfeile die zur größten Steigung zeigen, Länge des Pfeils ist wie steil es ist.
**Bildung**: für jede Variable eine Dimension im Vektor, bilde partielle Ableitungen und schreibe die Ergebnisse untereinander in einen Spaltenvektor
### Jacobi Matrix

mehrere Variablen Input, mehrere Werte Output (Vektorfunktionen)

**Bildung**: für jede Ausgabekomponente eine Zeile, für jede der Variablen ihre partielle Ableitungen in eine Spalte

$$
f(x + h) \approx f(x) + J_f(x) \cdot h
$$

differenzierbar $\implies$ Jacobi Matrix ist die Abbildung

---

Beispiel: 
$f(x,y) = \begin{cases} \frac{xy}{\sqrt{x^2+y^2}} & (x,y) \neq (0,0) \\ 0 & (x,y) = (0,0) \end{cases}$
Ist f bei (0,0) differenzierbar? Da $\lim_{h \to 0} \frac{f(0+h, 0) - f(0,0)}{h}=0$ und $\lim_{h \to 0} \frac{f(0, 0+h) - f(0, 0)}{h}=0$, somit ist unsere Jacobi Matrix $\begin{bmatrix}0 & 0\end{bmatrix} \in \mathbb{R}^{1 \times 2}$ . Dennoch jedoch nicht differenzierbar. Zeige mit $\lim_{h \to 0} \frac{\vert{}\vert{}f(x + h) - f(x) - L(h)\vert{}\vert{}}{\vert{}\vert{}h\vert{}\vert{}} = 0$. Nehme $h=(t,t)$ und betrachte $\lim_{ t \to 0 }$ mit $f(t,t)=\frac{|t|}{\sqrt{ 2 }}$ und $L(h)=(0, 0)\cdot \begin{bmatrix}t \\ t\end{bmatrix}$. Lim ist $\frac{1}{2}$, nicht 0 wie oben in der "zeige" Definition gefordert, somit nicht differenzierbar. 

---> nehme an L linear, also nehme an L hat eine jacobi matrix und schaue ob es in die definition der differenzierbarkeit passt

Beispiel für **Richtungsableitung**
Prüfe ob bei (0,0) differenzierbar. Ableitung in eine beliebige Richtung. Ableitung ist eine lineare Funktion, dann oder sonst muss man händisch prüfen, . ----> suche einen ausdruck für L und prüfe ob L linear ist. 

Wichtiges Lemma: alle partiellen Ableitungen stetig =>  f ist differenzierbar.

Also zb alle komponenten der jacobi matrix sind stetig , dann folgt direkt, dass f stetig differenzierbar ist.

Kettenregel: Jacobi matrix von f kreis g (x) ist jacobi von f ( g(x)) * jacobi_ g(x)
Produktregel: nehme an beide Funktionen scalare funktionen. j von f mal g = g(x)*jacobi von f(x) + f(X) * jacobi von g(x)

---

## Stetig differenzierbar

Eine Funktion $f$, die von einem offenen Definitionsbereich $U$ im $\mathbb{R}^n$ in den $\mathbb{R}^m$ abbildet, wird als stetig differenzierbar bezeichnet, falls alle ihre partiellen Ableitungen ($f_i$ für $1 \leq i \leq n$) existieren und auf dem Bereich $U$ stetig sind.

Solche Funktionen fasst man in einer Menge zusammen und schreibt dafür $f \in C^1(U, \mathbb{R}^m)$.

Falls für eine Funktion $f$ alle partiellen Ableitungen $\partial_i f$ auf einem offenen Bereich $U$ existieren und stetige Funktionen sind, dann ist $f$ auf dem gesamten Bereich $U$ differenzierbar.

## Mehrfache Ableitungen

**Satz von Schwarz**
$f \in C^k(U)$: Reihenfolge der bis zu $k$ partiellen Ableitungen ist irrelevant, Ergebnis ist gleich. Satz von Schwarz ist technically nur mit 2 Ableitungsschritten, gilt aber für beliebig viele.

$C^0$: stetige Funktionen
$C^k$: kann die Funktion $k$-mal ableiten, Ergebnis ist immer noch stetig
$C^\infty$: glatt
### Erhaltung

f und g sind $k$-fach stetig differenzierbar 

- $f + g$ auch
- $f \cdot g$ auch
- $f \circ h$ auch