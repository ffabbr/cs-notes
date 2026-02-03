### Subtask a

We are to find an orthogonal $2 \times 2$ matrix that is not a rotation matrix. 

As implied through example 6.3.4 of the lecture notes, the determinant of a rotation matrix is 1. We can show this using the rotation matrix given in the task. 

$$A = \begin{bmatrix}
\cos\phi & -\sin\phi \\
\sin\phi & \cos\phi
\end{bmatrix}$$

Following definition 7.2.3 for calculating the determinant of $2 \times 2$ marices, we get 

$$\det A = \cos\phi\cdot\cos\phi + \sin\phi\cdot \sin \phi=1$$

As we are looking for an orthogonal $2 \times 2$ matrix, per proposition 7.2.4 the determinant must be either 1 or -1. As shown above, we can exclude 1 as that would make it a rotation matrix. Thus, we are **looking for a square matrix whose determinant is -1**. Furthermore, per definition of an orthogonal matrix $A^\top A=I$ must hold. 

Using the above informations we can set up a system of linear equations as follows: 

$$A^\top A=I$$
$$\begin{bmatrix}
a & c \\
b & d
\end{bmatrix}\cdot \begin{bmatrix}
a & b \\
c & d
\end{bmatrix}=\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}$$

$$
\begin{align}
ad-bc&=-1 \\
a^2+c^2&=1 \\
ba+dc&=0 \\
b^2+d^2&=1
\end{align}
$$
Solving this system we get $b = c$ and $d = -a$ as our solutions. An example for such a matrix would be 

$$A=\begin{bmatrix}
1 & 0 \\
0 & -1
\end{bmatrix}$$

---

### Subtask b

We are to prove that if A is orthogonal, $|\det(A)|=1$ holds.

Once again, as A is an orthogonal matrix, $A^\top A=I$ holds. We know that the determinant of I is 1, so by Lemma 7.1.2 we can write $$\det(A^\top A)=\det(A^\top) \det(A)=1$$Per theorem 7.2.5 we know that $\det(A^\top)=\det(A)$, meaning that we can substitute $A^\top$ with A in the above equation. We get

$$\begin{align}
1&=\det(A)\det(A) \\
&=\det(A)^2 \\
\end{align}$$
Substituting $\det(A)$ with $x$ we get $1=x^2$, and solving that equations leaves us with $x=\det(A)=\pm 1$. This proofs $|\det(A)|=1$.

---

### Subtask c

We are looking for a matrix A that is not orthogonal but still $|\det(A)|=1$ holds. A matrix not being orthogonal means by definition $A^\top A \neq I$. Intuitively, a skew matrix should be a valid example to proof that this converse doesn't hold. In the following we will check that statement. 

Graphically, we can interpret a determinant of 1 in $2\times 2$ to be the area of the parallellogram spanned by the vectors of that matrix. Starting with a matrix with the standard unit vectors, we get a square spanned by $(0,1)^\top$ and $(1,0)^\top$. We want to skew this matrix by t while preserving $\det=\pm1$. 

We get: 
$$\begin{vmatrix}
0 & 1 \\
1 & t
\end{vmatrix} = \pm 1$$
And indeed $0t-1=-1$, and $|-1|=1$. So for arbitrary t, the area remains 1. 

For example, we will use $t=2$.  $$A=\begin{bmatrix}
0 & 1 \\
1 & 2
\end{bmatrix}$$
It remains to show that this matrix is not orthogonal, meaning $A^\top A \neq I$. 

$$\begin{bmatrix}
0 & 1 \\
1 & 2
\end{bmatrix}\cdot \begin{bmatrix}
0 & 1 \\
1 & 2
\end{bmatrix}=\begin{bmatrix}
1 & 2 \\
2 & 5
\end{bmatrix} \neq \begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}$$

Thus we have found such a matrix. 