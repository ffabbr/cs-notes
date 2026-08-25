Re-read [[06 Lecture.pdf]] and [[07 Lecture.pdf]], but here's my natural language interpretation of a subspace and basis.

A subspace is a subset of a vector space and acts as a vector space itself. If W is a subset (subspace) of V, the following properties must hold: 

1. $0 ∈ W$
2. $u,v ∈ W$, then $u+v ∈ W$ (closed under addition)
3. $u ∈ W$, then $\lambda u ∈ W$ (closed under scalar multiplication)

Subspaces are defined by basis vectors, and the span (all linear combinations) of those form the subspace. So each element of the basis is linearly independent. 

F.ex. in $\mathbb{R}^3$, we could f.ex. have these types of subspaces: 

- the zero vector (a point)
- a line through the origin
- a plane through the origin (2d subspace)
- all of 3d space (needs three lin. indep. vectors as a basis)

$\mathbb{R}^m \text{ has dimension } m$

> The **dimension** of a vector space $V$, denoted $\dim(V)$,  
> is the size (number of vectors) of any basis of $V$.

### Examples 

| vector space $V$                                                      | basis $B$                                                                                                                                             |
| --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| $\mathbb{R}^m$                                                        | $\{e_1, e_2, \ldots, e_m \}$                                                                                                                          |
| $C(A)$ (subspace of $\mathbb{R}^m$)                                   | independent columns of $A$                                                                                                                            |
| $2 \times 2$ symmetric matrices (subspace of $\mathbb{R}^{2\times2}$) | $\left\{ \begin{bmatrix}1 & 0 \\ 0 & 0\end{bmatrix}, \begin{bmatrix}0 & 1 \\ 1 & 0\end{bmatrix}, \begin{bmatrix}0 & 0 \\ 0 & 1\end{bmatrix} \right\}$ |
| $\mathbb{R}[x]$ (polynomials)                                         | $\{ x^i : i = 0, 1, \ldots \}$ (infinite set)                                                                                                         |
| $\{0\}$ (smallest vector space)                                       | $\varnothing$ (empty set)                                                                                                                             |

Definitely read and learn [[07 Lecture.pdf]].

![[Steinitz exchange lemma.png]]

## Steinitz Exchange Lemma

*all bases of a vector space have the same size.*

Let $V$ be a finitely generated vector space,  
and suppose we have:

- $F \subseteq V$: a finite **linearly independent** set,
- $G \subseteq V$: a finite set of vectors that **span** $V$.

#### (i) $|F| \le |G|$
#### (ii) There exists a subset $E \subseteq G$ of size $|G| - |F|$ such that
$$
\text{Span}(F \cup E) = V  
$$
You can **enlarge** the independent set $F$ by adding some elements of $G$ (but not too many) so that together they still span $V$.  

---

### Exchanging Basis

Let $V$ be a finitely generated vector space,  
and $B, B' \subseteq V$ be two **bases** of $V$.

Then:
$$
|B| = |B'|  
$$
**Proof:**

- Both $B$ and $B'$ are linearly independent and both span $V$.
- By part (i) of the Steinitz lemma:  
    $|B| \le |B'|$
- Swapping the roles (using $B'$ as $F$ and $B$ as $G$):  
    $|B'| \le |B|$
- Combining both gives $|B| = |B'|$.


