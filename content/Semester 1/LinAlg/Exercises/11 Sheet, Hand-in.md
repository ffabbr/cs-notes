### Subtask a

We will be using the proposed decomposition from the hint. Let M' $\begin{bmatrix}I & B \\ 0 & C\end{bmatrix}$ and M'' $\begin{bmatrix}A & 0 \\ 0 & I\end{bmatrix}$. 

As we know that $\det(A B) = \det(A) \cdot \det(B)$ holds and that the multiplication is commutative, we need to show that (i) $\det(M')=\det(C)$ and (ii) $\det(M'')=\det(A)$. 

Part (ii)

We need to show that for an arbitrary square matrix A it holds that $\det\begin{bmatrix}A & 0 \\ 0 & I_{r}\end{bmatrix}=\det(A)$, where r is the size of the $r \times r$ identity matrix. 

I didn't really manage to solve this using Definition 7.2.3, so I will do so using Induction and Laplace: 

Let's define $$M''_r = \begin{bmatrix} A & 0 \\ 0 & I_r \end{bmatrix}$$
meaning $M''_{r} \in \mathbb{R}^{(m+r) \times (m+r)}$.

**IH:** Suppose for a r $$\det(M''_r) = \det \begin{bmatrix} A & 0 \\ 0 & I_r \end{bmatrix} = \det(A)$$
holds.

**Base Case:** r=0. We have $M''_0 = A$, so subsequently $\det(M''_0) = \det(A)$.

**Induction Step**: r → r+1. 

To show: $$M''_{r+1} = \begin{bmatrix} A & 0 \\ 0 & I_{r+1} \end{bmatrix}$$
We can write $M''_{r+1}$ down as $$M''_{r+1}=\begin{bmatrix}
A & 0 & 0 \\
0 & I_{r} & 0 \\
0 & 0 & 1
\end{bmatrix}$$
Per Laplace when we calculate the determinant on the last column, we only need to observe the case where the entry is nonzero (as otherwise the product would become 0). 

Using the formula, we have $(-1)^{(m+r+1) + (m+r+1)}=(-1)^{2(m+r+1)}$, meaning the exponent is an even number, so our Vorzeichen (hmm) is 1. $\mathscr{A}_{(m+r+1),(m+r+1)}$ is $\begin{bmatrix}A & 0 \\ 0 & I_{r}\end{bmatrix}$, so we have shown that $$\det(M''_{r+1}) = 1 \cdot \det(M''_r)$$
and per IH also $\det(M''_{r+1}) = \det(A)$

As this holds for all r, we have shown $\det\begin{bmatrix}A & 0 \\ 0 & I_{r}\end{bmatrix}=\det(A)$, meaning $\det(M'')=\det(A)$.

It remains to show that $\det(M')=\det(C)$. 

Let $$M'_r = \begin{bmatrix} I_r & B_r \\ 0 & C \end{bmatrix}$$
**IH** $$\det(M'_r) = \det \begin{bmatrix} I_r & B_r \\ 0 & C \end{bmatrix} = \det(C)$$
**BC**, r=1
$$M'_1 = \begin{bmatrix} 1 & B_{11} \\ 0 & C \end{bmatrix}$$

$(-1)^{1+1} = 1$, $\det(K_1) = 1 \cdot \det(C) = \det(C)$

So the BC holds.

**IS** $(r → r+1)$

Notice that the first column always remains a basic/standard unit vector, as we have I and below that 0. Using Laplace: $$\det(M'_{r+1}) = (1) \cdot 1 \cdot \det(\mathscr{A}_{11})$$
Now notice that $\det(\mathscr{A}_{11})$ holds the same structure as $M'_{r}$. Per IV $$\det(M'_{r+1}) = \det(C)$$ 
### Subtask 2

We can rewrite the matrix using 9 swaps (so our Vorzeichen is -1) to 

$$M'' = \begin{bmatrix} 2 & 0 & 0 & 3 & 5 & 7 \\ 3 & 1 & 0 & 2 & 5 & 2 \\ 8 & 7 & 2 & 8 & 3 & 1 \\ \mathbf{0} & \mathbf{0} & \mathbf{0} & 2 & 4 & 7 \\ \mathbf{0} & \mathbf{0} & \mathbf{0} & 9 & 0 & 4 \\ \mathbf{0} & \mathbf{0} & \mathbf{0} & 1 & 0 & 0 \end{bmatrix} = \begin{bmatrix} C & B \\ \mathbf{0} & A \end{bmatrix}$$

Using the results from subtask 1 we get $$\det(M'') = -(4 \cdot 16) = -64$$
 
