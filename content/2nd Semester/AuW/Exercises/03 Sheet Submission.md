
## Choosing Seminars

**13 Students per Seminar**

We model a Graph $G$:

- for every student, have a vertex
- for each seminar, we create 13 vertices (one vertex per slot)
- for each student, we add an edge between the student and every slot of every course he applied to (meaning $3\cdot 13$ vertices per student)

We are now looking for perfect matchings in our Graph $G$.

Let $X$ be an arbitrary subset of students and $N(X)$ the slot nodes connected with the students. Let $m$ be the number of seminars the students of $X$ aplied to. 

$$
\begin{align}
 & m=\frac{|N(X)|}{13} \\
\implies & |N(X)| = 13\cdot m
\end{align}
$$

For the prerequesite to hold we need to show that $|X| \leq |N(X)|$ for all subsets X (Halls Theorem).

The seminars can receive a maximum of $$\leq 40+40+(39\cdot (m-2))=39\cdot m+2$$ combined applications. The students sent out a combined total of $|X| \cdot 3$ applications. We can bound like

$$
\begin{align}
 & |X|\cdot 3 \leq 39\cdot m+2 \\
\implies  & |X| \leq \frac{39\cdot m + 2}{3} \\
\implies & |X|\leq 13\cdot m + \frac{2}{3} \\
\implies  & |X| \leq 13\cdot m
\end{align}
$$
The second-last step comes from the fact that there cannot be a $\frac{2}{3}$-person, so the largest statement we can support is $13m$.

We have shown $|N(X)|= 13\cdot m$ and $|X| \leq 13\cdot m$, so  $|X| \leq |N(X)|$, which per Halls theorem concludes the proof. 

**12 Students per Seminar**

Counterexample: 
- 39 Students ($|X|=39$), 3 Seminars ($m=3$) 
- applications received: $\leq 39\cdot 3 + 2 = 119$, 
- $3\cdot 39=117$ applications sent. As $117 \leq 119$, this is valid

- Available slots: $3\cdot 12 = 36$
- $36 < 39$, thus not possible