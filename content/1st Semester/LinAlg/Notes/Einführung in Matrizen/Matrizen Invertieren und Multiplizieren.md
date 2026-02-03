## Quick Facts

- Invertierbar, wenn **quadratisch** und **voller Spaltenrang** 

- Bei der Identitätsmatrix I gilt $(A+I)^2 = A^2 + 2AI + I^2$. Sonst aber nicht.

> [!abstract] Rechenregeln
> - $(AB)^{\mathrm{T}} = B^{\mathrm{T}} A^{\mathrm{T}}$  
> - $(AB)^{-1} = B^{-1} A^{-1}$  
> - $(A^{\mathrm{T}})^{-1} = (A^{-1})^{\mathrm{T}}$  
> - $(A^{-1})^{-1} = A$
> - $A^{-1} \cdot A=I$ 

- Der Nullspace von A ist nie $\emptyset$, da $A \cdot 0=0$ immer gilt. 
- Wenn A invertierbar ist, so gilt $Ax=0$ nur für $x=0$
- $(A^2)^{-1} = (A^{-1})^2$

- "invertierbar" heißt eigentlich bijektiv, siehe [[Transformations-Eigenschaften]]

### Invertieren

Case $1 \times 1.$
$$

A = [a] \quad \Rightarrow \quad A^{-1} = \left[ \frac{1}{a} \right]

\quad (\text{if } a \neq 0).

$$

  
Case $2 \times 2.$

$$
A = \begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
\quad \Rightarrow \quad
A^{-1} =
\frac{1}{ad - bc}
\begin{bmatrix}
d & -b \\
-c & a
\end{bmatrix}
\quad (\text{if } ad - bc \neq 0).
$$

Sonst? Durch Logik oder Row Operations eine Matrix mit $B \cdot B^{-1} = I$ finden. Siehe [[Inverse Matrix.mp4]]