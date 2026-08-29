## Introduction

Nutzen zum Lösen von Gleichungssystemen, wenn 

- Quadratisch, also gleich viele Gleichungen wie Unbekannte
- $\det(A) \neq 0$ (gibt eine eindeutige Lösung)

### Zum Lösen von $Ax=b$ 

Pro Unbekannte $x_{i}$:
$$
x_i = \frac{\det(\mathscr{B}_i)}{\det(A)}
$$

$\mathscr{B}_{i}$: Hilfsmatrix, nachdem die i-te Spalte von A mit dem Vektor b (rechte Seite) ersetzt wurde

## Beispiele

### Walkthrough in $3 \times 3$ 

$Ax = b$:
$$
A = \begin{bmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{bmatrix} \quad \text{und} \quad b = \begin{bmatrix} b_1 \\ b_2 \\ b_3 \end{bmatrix}
$$
$$
x_1 = \frac{\det\begin{bmatrix} \mathbf{b_1} & a_{12} & a_{13} \\ \mathbf{b_2} & a_{22} & a_{23} \\ \mathbf{b_3} & a_{32} & a_{33} \end{bmatrix}}{\det(A)}, \quad x_2 = \frac{\det\begin{bmatrix} a_{11} & \mathbf{b_1} & a_{13} \\ a_{21} & \mathbf{b_2} & a_{23} \\ a_{31} & \mathbf{b_3} & a_{33} \end{bmatrix}}{\det(A)}, \quad x_3 = \frac{\det\begin{bmatrix} a_{11} & a_{12} & \mathbf{b_1} \\ a_{21} & a_{22} & \mathbf{b_2} \\ a_{31} & a_{32} & \mathbf{b_3} \end{bmatrix}}{\det(A)}
$$

### Rechenbeispiel in $2 \times 2$

$$
\begin{cases} 2x + 1y = 5 \\ 1x - 3y = -1 \end{cases}
$$
$$
A = \begin{bmatrix} 2 & 1 \\ 1 & -3 \end{bmatrix}, \quad b = \begin{bmatrix} 5 \\ -1 \end{bmatrix}
$$
Da $\det(A) = -7 \neq 0$ ist das System lösbar. Formel von oben ist $x_i = \frac{\det(\mathscr{B}_i)}{\det(A)}$, also 
$$
x_1 = \frac{\det\begin{bmatrix} \mathbf{5} & 1 \\ \mathbf{-1} & -3 \end{bmatrix}}{\det(A)} = \frac{-15 - (-1)}{-7} = \frac{-14}{-7} = 2
$$

$$
x_2 = \frac{\det\begin{bmatrix} 2 & \mathbf{5} \\ 1 & \mathbf{-1} \end{bmatrix}}{\det(A)} = \frac{-2 - 5}{-7} = \frac{-7}{-7} = 1
$$