

## Kritische Stellen

**Kritische Stellen im Eindimensionalen**: 
$f'(x) = 0$, dann prüfen mit $f''(x) = 0$

**Kritische Stellen im Mehrdimensionalen**:
Gradient:
$$
x_{0} \text{ ist kritischer Punkt} \iff\nabla f(x_0) = 0
$$
Was passiert im Unendlichen entlang der Koordinatenachsen? Punkte an denen der Gradient nicht definiert ist, aber die im Definitionsbereich sind, müssen separat auf kritische Punkte geprüft werden. 

## Extremstelle

**Sattelpunkt graphisch**: nach einer Achse werden die Funktionswerte größer (Minimalstelle), in die andere werden sie kleiner (Maximalstelle). Also 2 Richtungen mit unterschieldichem Verhalten. 

Prüfe die 2. Ableitungen an allen kritischen Punkten, indem wir die Hesse Matrix aufstellen.

## Hesse Matrix  

$H_{ij}f(x) = \partial_i \partial_j f(x)$
Alle Kombinationen, die Ableitungen zu machen, in einer Matrix. 

Beispiel mit 2 Variablen: 
$$
H_f(x,y) = \begin{pmatrix} f_{xx}(x,y) & f_{xy}(x,y) \\ f_{yx}(x,y) & f_{yy}(x,y) \end{pmatrix}
$$

Um die Krümmung auszulesen, nutzen wir die Eigenwerte. Sei $U$ offen und die Stelle $x_0 \in U$ ein kritischer Punkt. Es gilt:

- **Positiv definit:** alle Eigenwerte positiv, "Landschaft in alle Richtungen nach oben gekrümmt", lokales Minimum
- **Negativ definit:** alle Eigenwerte negativ "Landschaft überall nach unten", lokales Maximum
- **Indefinit:** gibt positive und negative EW, "in eine Richtung rauf, in die andere runter", Sattelpunkt
- **Degeneriert:** mind. ein Eigenwert ist null, keine Aussage
- **Indefinit** und **Degeneriert** (Eigenwere positiv, negativ, und 0): Sattelpunkt

Berechnen der Eigenwerte: $\det(M - \lambda I) = 0$ 

Zeit sparen durch die Spur $\Delta f(x)$: 
- Spur ist Summe der Diagonalwerte
- Spur ist immer gleich der Summe der Eigenwerte
- z.B. ist die Spur negativ, kann nicht positiv definit sein

![[Bildschirmfoto 2026-10-26 um 16.20.07.png]]

### Kriterium von Sylvester

Definitheit einer **symmetrischen Matrix** bestimmen. 

Beispiel: 2 dimensional
$$
H = \begin{pmatrix} a & b \\ b & c \end{pmatrix}
$$
![[Bildschirmfoto 2026-10-25 um 21.49.15.png]]


---


## Globale Maxima/Minima

![[Bildschirmfoto 2026-10-26 um 16.19.48.png]]![[Bildschirmfoto 2026-10-26 um 16.20.00.png]]