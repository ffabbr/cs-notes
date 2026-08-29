→ siehe [[04 Cramers Rule]]

**Laplace-Methode**

- Submatrix einer Matrix A mit genau einer Zeile und Spalte weniger als A
- $\det(A)$ ist die Summe der Elemente **einer Zeile (oder Spalte)** mal den zugehörigen Kofaktoren

$$
\det(A) = \sum_{j=1}^{n} a_{ij} \cdot c_{ij}
$$
Fixiere eine Zeile i oder Spalte j und berechne:
$$
c_{ij} = (-1)^{i+j} \cdot \det(\mathscr{A}_{ij})
$$
wobei hier $\mathscr{A}$ für A mit der entfernten Zeile i und Spalte j ist. 

**Also z.B in $3 \times 3$:**
$$
\begin{vmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{vmatrix} = a_{11} \underbrace{\begin{vmatrix} a_{22} & a_{23} \\ a_{32} & a_{33} \end{vmatrix}}_{C_{11}} + a_{12} \underbrace{\left( - \begin{vmatrix} a_{21} & a_{23} \\ a_{31} & a_{33} \end{vmatrix} \right)}_{C_{12}} + a_{13} \underbrace{\begin{vmatrix} a_{21} & a_{22} \\ a_{31} & a_{32} \end{vmatrix}}_{C_{13}}
$$

![[Cofactor Rows.png]]

## Lemmas
$$
\det(A) = \sum_{j=1}^{n} a_{ij}C_{ij}
$$
$A \in \mathbb{R}^{n \times n}$ mit $\det(A) \neq 0$. Sei $C$ die $n \times n$ Matrix mit den Kofaktoren von $A$ als Einträge:
$$
A^{-1} = \frac{1}{\det(A)} C^T
$$

![[Skript Part 2.pdf#page=34]]
