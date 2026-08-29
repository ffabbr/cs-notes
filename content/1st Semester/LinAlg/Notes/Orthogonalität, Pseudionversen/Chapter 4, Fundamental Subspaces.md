
This is a very broad summary meant to give a natural language understanding of the topics. Definitely re-read the [script](https://ti.inf.ethz.ch/ew/courses/LA25/notes_part_I.pdf) from page 126 onwards. 

- Nullspace $N(A) \subseteq \mathbb{R}^n$
- Rowspace $C(A^T) \subseteq \mathbb{R}^n$
- Column Space $C(A) \subseteq \mathbb{R}^m$ 
  
- $C(A)$ Dimension r, 
- $N(A)$ Dimension $n-r$, 
- $R(A)$ Dimension r. 
- $N(A^T)$ Dimension $m-r$
- $rank(A) = rank(A^\top)$

Rank-Nullity: $\text{rank}(A)+\text{dim}(N(A)))=\text{Anzahl Spalten}$ #helpsheet 

  ![[Nullspace und Summary, n-r.png]]

- Auch der Lösungsraum ist ein Unterraum. Bei $\text{Sol}(A,b):={x ∈ R^n:Ax=b}⊆R^n$, kein Unterraum bei b ungleich 0, da sonst 0 nicht Teil des Unterraums wäre.
- The number of independent columns equals the number of independent rows. $\text{rank}(A) = \dim(\text{Row}(A)) = \dim(\text{Col}(A))$. Somit gilt auch $\text{rank}(A)=\text{rank}(A^\top)$ 

### Polynome 

- The polynomial $0$ has the degree $-1$
- Der Vektorraum der Polynomfunktionen ist ein Vektorraum, weil man zwei Polynome addieren und einen Polynom mit einem Skalar multiplizieren kann.
- The vector space of polynomials is to be treated with particular care. It is a prime example of why we only allow a finite amount of linear combinations, because the sum
$$
\sum_{j=0}^{\infty} x^j
$$
is not a polynomial, as those only have finitely many different powers of x (per definition 4.3).

#### Endlich Generiert

- A vector space V is called finitely generated if there exists a finite subset $G ⊆ V$ with $\text{Span}(G)=V$. Es reicht, endlich viele Vektoren zu haben, um alle Vektoren des Raums daraus „zusammenzubauen“. 
- Also z.B. $R^3$ kann man mit den drei Basiseinheitsvektoren (drei, also endlich) "zusammenbauen". 
- Der Vektorraum aller Polynomfunktionen ist nicht endlich erzeugt, da wir unendlich viele Potenzen brauchen würden, um alle Polynome darzustellen, was aber per obiger Notiz nicht geht.

### Steinitz

- **Steinitz exchange lemma:** Imagine the vector space V, $F \subseteq V$ a set of linearly independent Vectors and $G\subseteq V$ a set of vectors that span V. $|F|\leq|G|$ holds (there aren't more independent vectors in the space than those that form the basis, meaning span the space). 
- Also, you can replace vectors (elements) of the basis with other linearly independent vectors (elements) and the basis remains being the basis. Also haben in einem fixen Vektorraum alle Basen gleich viele Vektoren (Elemente).
- ==Anzahl der Elemente in der Basis ist die **Dimension des Raumes**.==

### Abbildungen und Funktionen

- Die **Linearitätsbedingung** auch hier ist $T(\lambda_1 x_1 + \lambda_2 x_2) = \lambda_1 T(x_1) + \lambda_2 T(x_2)$
- Invertierbare Matrizen haben umkehrbare Transformationen und ändern die Dimension somit nicht. 
- Ein **Isomorphismus** ist eine bijektive (umkehrbare) lineare Abbildung T zwischen zwei Vektorräumen V und W. V und W sind also im Prinzip „derselbe Raum“, nur mit einer anderen Darstellung der Elemente. V und W haben die gleiche Dimension, wenn es einen Isomorphismus zwischen ihnen gibt. Außerdem gilt $|T(B)|=|B|$ (die Anzahl der Vektoren die wir "reingeben" ist gleich mit der Anzahl der Vektoren die wir "rausbekommen", da bijektiv. Eine Basis bleibt nach der Transformation weiterhin eine Basis, aber für einen anderen Raum. Somit sind die Dimensionen der beiden Vektorräumen auch gleich. Siehe Theorem 4.29. z.B. Matrix flattening (siehe unten).
$$
V = \mathbb{R}^{2 \times 2}, 
\quad 
W = \mathbb{R}^4, 
\quad 
T : 
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
\mapsto
\begin{pmatrix}
a \\ b \\ c \\ d
\end{pmatrix}
$$
- Wenn $Ax = b$ eine Lösung hat, dann besteht die Lösungsmenge aus allen Vektoren, die man erhält, wenn man eine bestimmte Lösung $s$ nimmt und **alle Vektoren aus dem Nullraum** $N(A)$ dazuaddiert. 
- Das heißt: Jede Lösung sieht aus wie $s + x$, wobei $x \in N(A)$. Wenn $b = 0$, ist das einfach der Nullraum selbst; wenn $b \neq 0$, ist es derselbe Raum, nur verschoben, also ein sog. shifted nullspace.

![[Spalten, Zeilen, Nullraum#Beispiele zum Notieren von den fundamentalen Unterräumen]]

![[Theorem 4.38.png]]![[07 Sheet in-class.pdf]]