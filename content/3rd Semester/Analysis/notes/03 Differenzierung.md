## Partielle Ableitung

**Partielle Ableitung**: Man wählt eine Zielvariable, betrachtet alle anderen Variablen als Konstanten und leitet ganz normal ab.

$$
f_i(x) = \frac{\partial f}{\partial x_i}(x) = \lim_{h \to 0} \frac{f(x_1, \dots, x_i + h, \dots, x_n) - f(x_1, \dots, x_i, \dots, x_n)}{h}
$$

*vor allem bei stückweiser Definition so arbeiten*

### Gradient 

 $\nabla f(p)$ 
 
- Gilt für skalare Funktionen (mehrere Variablen Input, _eine_ Zahl Output)
- Vektor, zeigt in die **Richtung der größten Steigung**
- "Länge" ist die maximale Änderungsrate

- **Bildung**: Für jede Variable wird die partielle Ableitung gebildet und untereinander in einen Spaltenvektor geschrieben

- Richtung des größten Abstiegs finden: entgegengesetzte $\cdot (-1)$ Richtung der größten Steigung

---
### Jacobi Matrix

Gilt für Funktionen mit mehreren Variablen Input und _mehreren_ Werten Output (Vektorfunktionen)

**Bildung**: 
für jede Ausgabekomponente eine Zeile, für jede der Variablen ihre partielle Ableitungen in eine Spalte

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

## Tangentialebene aufstellen

$$
z = f(x_0, y_0) + \frac{\partial f}{\partial x}(x_0, y_0) \cdot (x - x_0) + \frac{\partial f}{\partial y}(x_0, y_0) \cdot (y - y_0)
$$
Bzw. 

$$
\frac{\partial F}{\partial x}(x_0, y_0, z_0) \cdot (x - x_0) + \frac{\partial F}{\partial y}(x_0, y_0, z_0) \cdot (y - y_0) + \frac{\partial F}{\partial z}(x_0, y_0, z_0) \cdot (z - z_0) = 0
$$

### Gleichung der Normalengeraden

Gleichung der Tangentialebene: 
$$
ax+by+cz=d
$$
Somit Normalvektor: 
$$
\vec n=\begin{pmatrix}a\\b\\c\end{pmatrix}
$$
Und Normalengerade: 
$$
\boxed{
g:\ \vec x=
\begin{pmatrix}x_0\\y_0\\z_0\end{pmatrix}
+t\begin{pmatrix}a\\b\\c\end{pmatrix}
}
$$


---

## Richtungsableitungen

Statt nach nur einer Variablen abzuleiten, wollen wir von einer spezifischeren Richtung kommen. 

Der Vektor $v$ gibt diese Richtung an.

$$D_v f(x_0) =  \lim_{h \to 0} \frac{f(x_0 + h v) - f(x_0)}{h}$$

Wenn eine Funktion total differenzierbar ist, **muss** diese Richtungsableitung eine lineare Abbildung bezüglich des Richtungsvektors $v$ sein. Es gilt dann zwingend:
$$D_v f(x_0) = J_f(x_0) \cdot v$$

Bzw.
$$
D_{v}f(x_{0}) = \nabla f(p) \cdot v
$$

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

---

## Kettenregel

"aussere Ableitung mal innere Ableitung", aber hier mit Jacobi-Matrizen, da mit mehreren Variablen gleichzeitig. 

$$D(g \circ f)(x) = Dg(f(x)) \cdot Df(x)$$


## Mittelwertsatz

Irgendwo zwischen $x+h$ und $x$ gibt es eine Stelle, an der die momentane Steigung gleich groß ist wie die durchschnittliche Steigung.

$$
f(x+h) - f(x) = Df_{\xi}(h) = \partial_h f(\xi)
$$


## Mehrdimensionale Taylorapproximation

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
$$
R_{k+1}f(x_0, h) := \int_0^1 (k+1)(1-t)^k \sum_{\alpha \in \mathbb{N}_0^n, |\alpha|=k+1} \frac{\partial^\alpha f(x_0 + th)}{\alpha!} h^\alpha dt
$$


## Lokale Extremwerte 

Kritische Punkte im Eindimensionalen: $f'(x) = 0$, dann prüfen mit $f''(x) = 0$

Kritische Punkte im Mehrdimensionalen: alle partiellen Ableitungen 0:  $\partial_i f(x_0) = 0 \quad \forall 1 \leq i \leq n$

Wir prüfen das mit dem Gradienten 
$$
x_{0} \text{ ist kritischer Punkt} \iff\nabla f(x_0) = 0
$$

Achtung, Implikationsrichtung 
Lokales Extremum $\implies \nabla f(x_0) = 0$

Jetzt prüfen, ob Maximal-/Minimalstelle und nicht Sattelstelle ist. Wir erstellen eine Matrix aus allen zweiten Ableitungen:

**Hesse Matrix**  
$$
H_{ij}f(x) = \partial_i \partial_j f(x)
$$

z.B. bei 2 Variablen: leite zuerst einmal nach x ab, einmal nach y. Dann ausgehend von der x-Ableitung nochmal alle Optionen, also xx und xy, gleich mit erst y. Alle Kombinationen in die Matrix. 

Um die Krümmung auszulesen, nutzen wir die Eigenwerte. Sei $U$ offen und die Stelle $x_0 \in U$ ein kritischer Punkt. Es gilt:

- **Positiv definit:** alle Eigenwerte positiv, "Landschaft in alle Richtungen nach oben gekrümmt", lokales Minimum
- **Negativ definit:** alle Eigenwerte negativ "Landschaft überall nach unten", lokales Maximum
- **Indefinit:** gibt positive und negative EW, "in eine Richtung rauf, in die andere runter", Sattelpunkt
- **Degeneriert:** mind. ein Eigenwert ist null, keine Aussage

$\Delta f(x)$: Spur der Hasse-Matrix (Summe der Werte der Diagonale). Die Spur einer Matrix ist immer exakt gleich der Summe ihrer Eigenwerte. Zeit sparen: z.B. Spur ist negativ, so können nicht alle EW positiv sein.

Berechnen der Eigenwerte: $\det(M - \lambda I) = 0$ 

---

## Kurve


Eine Kurve ist eine Funktion mit einem Eingabewert (Vorestllung: Zeit) und einem Vektor mit drei Komponenten als Ausgabe. 