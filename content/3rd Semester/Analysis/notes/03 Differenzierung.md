## Partielle Ableitung

**Partielle Ableitung**: Man wählt eine Zielvariable, betrachtet alle anderen Variablen als Konstanten und leitet ganz normal ab.

$$
f_i(x) = \frac{\partial f}{\partial x_i}(x) = \lim_{h \to 0} \frac{f(x_1, \dots, x_i + h, \dots, x_n) - f(x_1, \dots, x_i, \dots, x_n)}{h}
$$

*vor allem bei stückweiser Definition so arbeiten*

**Gradient-Vektor**  $\nabla f(p)$ 
- Gilt für skalare Funktionen (mehrere Variablen Input, _eine_ Zahl Output)
- **Bildung**: Für jede Variable wird die partielle Ableitung gebildet und untereinander in einen Spaltenvektor geschrieben
- Visuell: Pfeile die zur größten Steigung zeigen, Länge des Pfeils ist wie steil es ist.

---
## Jacobi Matrix

Gilt für Funktionen mit mehreren Variablen Input und _mehreren_ Werten Output (Vektorfunktionen)

**Bildung**: für jede Ausgabekomponente eine Zeile, für jede der Variablen ihre partielle Ableitungen in eine Spalte

Funktion ist total differenzierbar $\implies$ Jacobi Matrix $J_{f}$ ist genau die Matrix, die die lineare Abbildung beschreibt $f(x + h) \approx f(x) + J_f(x) \cdot h$

Rechenregeln: 
- $J_{f \circ g}(x) = J_f(g(x)) \cdot J_g(x)$
- $J_{f \cdot g}(x) = g(x) \cdot J_f(x) + f(x) \cdot J_g(x)$

## Totale Differenzierbarkeit 

Im Eindimensionalen approximiert die Tangente (Ableitung) den nächsten Wert. Im Mehrdimensionalen ist das zum Beispiel eine Tangentialebene.

Eine Funktion ist an einer Stelle $x$ total differenzierbar, falls es eine lineare Abbildung $L$ (die Jacobi-Matrix) gibt, die die Funktion bei $x$ nahezu perfekt approximiert. 
$$
\lim_{h \to 0} \frac{\vert{}\vert{}f(x + h) - f(x) - L(h)\vert{}\vert{}}{\vert{}\vert{}h\vert{}\vert{}} = 0
$$
- $f(x + h) - f(x)$ ist die tatsächliche Änderung der Funktion
- $L(h)$ ist die durch Matrix vorrausgesagte Änderung (Jacobi mal h) 

Alle partiellen Ableitungen $\partial_i f$ (Kombonenten der Jacobi-Matrix) sind stetig $\implies$ $f$ ist stetig differenzierbar

---
## Richtungsableitungen

Die Richtungsableitung einer Funktion $f$ an der Stelle $x_0$ in eine beliebige Richtung $v$ berechnet sich durch:

$$D_v f(x_0) = \lim_{h \to 0} \frac{f(x_0 + h v) - f(x_0)}{h}$$

Wenn eine Funktion total differenzierbar ist, **muss** diese Richtungsableitung eine lineare Abbildung bezüglich des Richtungsvektors $v$ sein. Es gilt dann zwingend:
$$D_v f(x_0) = J_f(x_0) \cdot v$$

Algorithmus zur Prüfung auf Differenzierbarkeit (z.B. in (0,0)):
1. Berechne den Limes für $D_v f(0,0)$ für einen allgemeinen Vektor $v = (v_1, v_2)$
2. Ergebnis **nicht** linear in $v_1$ und $v_2$ (z.B. Brüche $\frac{v_1^2}{v_2}$ oder Wurzeln wie $\sqrt{v_1^2+v_2^2}$ ), somit L nicht linear. Die Funktion ist **nicht** total differenzierbar.
3. **Ergebnis ist linear**: müssen händisch prüfen mit der Definition (Limes mit Jacobi Matrix und Norm)

---
## Beispiel: Widerlegung Differenzierbarkeit


"Prüfe ob bei (0,0) differenzierbar": Nehme allgemeinen $v = (v_1, v_2)$. Berechne Grenzwert für Richtungsableitung $L(v) = \lim_{t \to 0} \frac{f(0 + t v_1, 0 + t v_2) - f(0,0)}{t}$. Prüfe, ob linear gegenüber $v$. Nicht linear $\implies$ fertig, ist nicht total differenzierbar. Linear $\implies$ händischer Beweis notwendig (mit Jacobi Matrix, etc.)

**Globale Differenzierbarkeit**: gibt für jeden Punkt ein solches $L$.


$$
f(x,y) = \begin{cases} \frac{xy}{\sqrt{x^2+y^2}} & (x,y) \neq (0,0) \\ 0 & (x,y) = (0,0) \end{cases}
$$

1. Partielle Ableitungen an $(0,0)$ prüfen. $\lim_{h \to 0} \frac{f(0+h, 0) - f(0,0)}{h} = 0 \quad \text{und} \quad \lim_{h \to 0} \frac{f(0, 0+h) - f(0, 0)}{h} = 0$. Die partiellen Ableitungen existieren. Gäbe es eine totale Ableitung, müsste die Jacobi-Matrix $J_f = \begin{bmatrix}0 & 0\end{bmatrix}$ sein.
2. Totale Differenzierbarkeit händisch prüfen. Es muss gelten $\lim_{h \to 0} \frac{\Vert{}f(x + h) - f(x) - L(h)\Vert{}}{\Vert{}h\Vert{}} = 0$. Da $x=(0,0)$ und $L(h) = \begin{bmatrix}0 & 0\end{bmatrix} \cdot \begin{bmatrix}h_1 \\ h_2\end{bmatrix} = 0$, vereinfacht sich der Bruch zu $\lim_{h \to 0} \frac{\vert{}f(h_1, h_2)\vert{}}{\Vert{}h\Vert{}} = 0$. Damit dieser Grenzwert $0$ ist, muss er aus *jeder* beliebigen Richtung $0$ ergeben. 
3. Gegenbeispiel: Wähle $h = (t,t)$ und bilde den Limes $t \to 0$. $\lim_{t \to 0} \frac{\frac{\vert{}t\vert{}}{\sqrt{2}}}{\vert{}t\vert{}\sqrt{2}} = \frac{1}{2}$. 
4. Da der Grenzwert $\frac{1}{2}$ und nicht $0$ ist, ist bewiesen, die Funktion ist im Ursprung **nicht total differenzierbar**.

---

## Mehrfache Ableitungen

$C^0$: stetige Funktionen
$C^k$: kann die Funktion $k$-mal ableiten, Ergebnis ist immer noch stetig
$C^\infty$: glatt

**Satz von Schwarz**
$f \in C^k(U)$: Reihenfolge der bis zu $k$ partiellen Ableitungen ist irrelevant, Ergebnis ist gleich. Satz von Schwarz ist technically nur mit 2 Ableitungsschritten, gilt aber für beliebig viele.

**Erhaltung**: f und g sind $k$-fach stetig differenzierbar 
- $f + g$ auch
- $f \cdot g$ auch
- $f \circ h$ auch