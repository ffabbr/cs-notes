
## Allgemein

Eine $m \times n$ Matrix hat $m$ Zeilen und $n$ Spalten. 

### Lemma 1.28  

Wenn $m$ Vektoren $v_1, \ldots, v_m \in \mathbb{R}^m$ linear unabhängig sind, dann spannen sie den ganzen Raum auf:
$$
\text{Span}(v_1,\ldots,v_m) = \mathbb{R}^m
$$

***

## Spezielle Matrizen

| Name                  | Bedingung                   | Beispiel                                                            |
| --------------------- | --------------------------- | ------------------------------------------------------------------- |
| Identität $I$         | $a_{ij} = \delta_{ij}$      | $\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$ |
| Diagonalmatrix        | nur Hauptdiagonale $\neq 0$ | $\begin{bmatrix} 2 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 5 \end{bmatrix}$ |
| Obere Dreiecksmatrix  | $a_{ij} = 0$ für $i > j$    | $\begin{bmatrix} 2 & 1 & 0 \\ 0 & 4 & 7 \\ 0 & 0 & 5 \end{bmatrix}$ |
| Untere Dreiecksmatrix | $a_{ij} = 0$ für $i < j$    | $\begin{bmatrix} 2 & 0 & 0 \\ 1 & 4 & 0 \\ 0 & 7 & 5 \end{bmatrix}$ |
| Symmetrisch           | $A = A^T$                   | $\begin{bmatrix} 2 & 1 & 0 \\ 1 & 4 & 7 \\ 0 & 7 & 5 \end{bmatrix}$ |

---

1. Ein Vektor $b \in \mathbb{R}^m$ ist genau dann eine Linearkombination der Spalten von $A$, wenn es ein $x$ mit $Ax = b$ gibt.  
   → Alle $b$, die man durch $Ax$ erreichen kann, sind im Spaltenraum von $A$.

2. Die Spalten von $A$ sind linear unabhängig, genau dann, wenn die einzige Lösung von $Ax = 0$ der Nullvektor ist.

***

## Span und Spaltenraum

Wenn du eine Matrix $A = [v_1\ v_2\ \cdots\ v_n]$ hast, dann sind ihre Spalten $v_j \in \mathbb{R}^m$.  
Der Spaltenraum (column space) ist also genau der Span dieser Spalten:

$$
C(A) = \text{Span}(v_1, v_2, \ldots, v_n)
$$

oder:

$$
C(A) = \{Ax : x \in \mathbb{R}^n\}
$$

> Der Spaltenraum ist die Menge aller Ergebnisse, die du erhältst, wenn du $A$ auf alle möglichen Vektoren $x$ anwendest.  

Da $Ax = x_1 v_1 + x_2 v_2 + \cdots + x_n v_n$, ist das genau der gleiche Ausdruck wie der Span oben – nur in anderer Notation.

***

## Linearität und Transformationen

Eine Matrix-Transformation ist immer linear. Ein **Lineares Funktional** bildet von einem Vektorraum in die reellen Zahlen ab. 

![[Transformations-Eigenschaften#Lineare Transformationen]]

***

#### Schreibweise $T_A(x) = Ax$

- $T_A$ ist Name der Abbildung (die zur Matrix $A$ gehört)
- $x$ ist Input
- $Ax$ ist Output

***

#### Kombinieren von Transformationen

$$
x \xrightarrow{T_B} Bx \xrightarrow{T_A} A(Bx)
$$
Zusammen:
$$
T_C(x) = T_A(T_B(x)) = A(Bx)
$$**Komposition**:
$$
T_C = T_A \circ T_B
$$
(„erst B, dann A“).
