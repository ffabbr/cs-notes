- Algebraische Vielfachheit: wie oft ist eine Nullstelle eine Nullstelle?
- Geometrische Vielfachheit: $\dim(N(A-\lambda I))$ 

- Wenn gleich, dann **complete set of real eigenvectors**
- Wenn eine $n \times n$ Matrix $n$ verschiedene reelle Eigenwerte hat, dann **complete set of real eigenvectors**, also diagonalisierbar

## Beispiel

$$A=\begin{bmatrix}4 & 1\\ 0 & 2\end{bmatrix}$$
Eigenwerte $\lambda_1=4,\quad \lambda_2=2$. 

**1. Lambda = 4**
$$A-4I=\begin{bmatrix}0 & 1\\ 0 & -2\end{bmatrix}$$
Löse $(A-4I)x=0$

$$\begin{cases}
x_2=0\\
-2x_2=0
\end{cases}
\Rightarrow x_2=0,\; x_1 \text{ frei}$$
$\text{Nullspace von A - 4 I}=\left\{ \begin{pmatrix}x_1\\0\end{pmatrix} : x_1\in\mathbb{R}\right\}$

$\boxed{\text{geom. Vielfachheit von }4 = 1}$

**Repeat mit Lambda = 2**
