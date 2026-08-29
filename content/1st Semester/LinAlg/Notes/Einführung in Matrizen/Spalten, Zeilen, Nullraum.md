> $N(A) = N(A^T A)$ 
> $C(A^T) = C(A^T A)$ 
> $R(A^T) = R(A^T A)$  

## Notation

#### Spaltenraum (Column Space)
$$
\text{Col}(A) = \text{span} \left\{ \begin{pmatrix} a_{1} \\ a_{2} \\ \vdots \\ a_{m} \end{pmatrix}, \begin{pmatrix} b_{1} \\ b_{2} \\ \vdots \\ b_{m} \end{pmatrix} \right\}
$$
$$
\operatorname{Col}(A) = \left\{ A x \mid x \in \mathbb{R}^n \right\}.
$$
*Pivot-Spalten vom [[Gauss and Gauss-Jordan|RREF]] aus der Originalmatrix nehmen.* 

#### Zeilenraum (Rowspace)

*Die Zeilen in der RREF die nicht 0 sind.*
$$
\text{Row}(A) = \text{span} \big\{ (1, 0, 2), (0, 1, 5) \big\}
$$
> $x, y \in R(A)$, dann $Ax = Ay \iff x = y$

#### Nullraum (Nullspace)
$$
\text{Nul}(A) = \left\{ x \in \mathbb{R}^n \mid Ax = 0 \right\}
$$
$$
\operatorname{Null}(A) = \operatorname{Row}(A)^\perp
$$

---

## Beispiel

Gesucht: $A x = 0$
$$
\begin{cases}
x_1 + 2x_2 + 3x_3 = 0 \\
4x_1 + 5x_2 + 6x_3 = 0
\end{cases}
$$

Reduktion:
$$
-3x_2 - 6x_3 = 0 \Rightarrow x_2 = -2x_3
$$
$$
x_1 - x_3 = 0 \Rightarrow x_1 = x_3
$$

Allgemeine Lösung:
$$
x = t
\begin{bmatrix}
1 \\ -2 \\ 1
\end{bmatrix}, \quad t \in \mathbb{R}
$$

→ Der Nullraum ist eine **Gerade** in $\mathbb{R}^3$ entlang von $(1, -2, 1)$.

---

$$
\text{Rang}(A) + \text{Nullität}(A) = 2 + 1 = 3 = \text{Anzahl der Spalten}
$$

---

### Unabhängigen Vektor finden 

Um einen unabhängigen Vektor von zwei gegebenen zu bilden, entweder (wenn möglich) das Kreuzprodukt nehmen (siehe Foto unten), oder eine random Linearkombination der beiden bilden und einen Wert ändern (z.B. auf 0 setzen).

![[Kreuzprodukt.png]]

