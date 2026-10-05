## Partielle Ableitung

Wähle Zielvariable, betrachte die andere als Konstante und leite normal ab.

$$
\begin{align}
f_i(x) =\frac{\partial f}{\partial x_i}(x) &= \lim_{h \to 0} \frac{f(x + he_i) - f(x)}{h} \\
&= \lim_{h \to 0} \frac{f(x_1, \dots, x_i + h, \dots, x_n) - f(x_1, \dots, x_i, \dots, x_n)}{h}
\end{align}
$$

## Differential

Im Eindimensionalen haben wir durch die Ableitung (Tangente) den nächsten Wert approximieren können: $f(z+h) = f(z) + f'(z) \cdot h + \text{Rest}$. Im Mehrdimensionalen haben wir z.B. eine Ebene, nicht eine Gerade.

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

**Bildung**: für jede Ausgabekomponente eine Zeile, für jede der Variablen ihre partielle Ableitunge in eine Spalte

$$
f(x + h) \approx f(x) + J_f(x) \cdot h
$$

## Stetig differenzierbar

Eine Funktion $f$, die von einem offenen Definitionsbereich $U$ im $\mathbb{R}^n$ in den $\mathbb{R}^m$ abbildet, wird als stetig differenzierbar bezeichnet, falls alle ihre partiellen Ableitungen ($f_i$ für $1 \leq i \leq n$) existieren und auf dem Bereich $U$ stetig sind.

Solche Funktionen fasst man in einer Menge zusammen und schreibt dafür $f \in C^1(U, \mathbb{R}^m)$.

Falls für eine Funktion $f$ alle partiellen Ableitungen $\partial_i f$ auf einem offenen Bereich $U$ existieren und stetige Funktionen sind, dann ist $f$ auf dem gesamten Bereich $U$ differenzierbar.

## Mehrfache Ableitungen

**Satz von Schwarz**
$f \in C^k(U)$: Reihenfolge der bis zu $k$ partiellen Ableitungen ist irrelevant, Ergebnis ist gleich. Satz von Schwarz ist technically nur mit 2 Ableitungsschritten, gilt aber für beliebig viele.

$C^0$: alle stetigen Funktionen. Knicke erlaubt, keine Sprungstellen
$C^k$: kann die Funktion $k$-mal hintereinander ableiten, und das finale Ergebnis ist immer noch eine stetige Funktion ohne Sprünge
$C^\infty$: glatt

### Erhaltung

f und g sind $k$-fach stetig differenzierbar 

- $f + g$ auch
- $f \cdot g$ auch
- $f \circ h$ auch