- Vorstellung in $\mathbb{R}^2$: Determinante gibt Flächeninhalt der durch Spaltenvektoren aufgespannten Körpers an

- Für eine Matrix $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ gilt die Formel:
$$
\det(A) = a \cdot d - c \cdot b
$$
- → [[03 The General Case]]

## Rechenregeln

- A **nicht quadratisch: $\det(A)=0$.** Im Folgenden also nur quadratische Matrizen:

> [!abstract] Für quadratische Matrizen
> - $\det(A B) = \det(A) \cdot \det(B)$
> - $\det(A^T) = \det(A)$
> - $\det(A^{-1}) = \frac{1}{\det(A)}$ ($\det(A) \neq 0$)
> - $\det(\lambda \cdot A) = \lambda^n \cdot \det(A)$ (wobei $n$ die Ordnung der Matrix ist)
> - Matrix orthogonal, also $Q^\top Q=I$, dann gilt: $\det(A)=\pm 1$ 
> - Zwei Zeilen oder Spalten vertauscht, **Vorzeichen** der Determinante swappen
> - Determinante ändert sich nicht wenn man ein Vielfaches einer Zeile (Spalte) zu einer anderen addiert
> - **Invertierbar** genau dann wenn $\det(A) \neq 0$. (**lin.abh., dann det 0**, imagine zwei Vektoren auf einer Linie, also Flächeninhalt 0) 


**Determinanten sind linear:** 

Für jede $a_0, \dots, a_n \in \mathbb{R}^n$ und $\alpha_0, \alpha_1 \in \mathbb{R}$
$$
\det \left( \begin{bmatrix} - \alpha_0 a_0^T + \alpha_1 a_1^T - \\ - a_2^T - \\ \vdots \\ - a_n^T - \end{bmatrix} \right) = \alpha_0 \det \left( \begin{bmatrix} - a_0^T - \\ - a_2^T - \\ \vdots \\ - a_n^T - \end{bmatrix} \right) + \alpha_1 \det \left( \begin{bmatrix} - a_1^T - \\ - a_2^T - \\ \vdots \\ - a_n^T - \end{bmatrix} \right)
$$
und auch für Spalten
$$
\begin{align}
 &\det \left( \begin{bmatrix} | & | & & | \\ \alpha_0 a_0 + \alpha_1 a_1 & a_1 & \cdots & a_n \\ | & | & & | \end{bmatrix} \right)  \\
&= \alpha_0 \det \left( \begin{bmatrix} | & & | \\ a_0 & \cdots & a_n \\ | & & | \end{bmatrix} \right) + \alpha_1 \det \left( \begin{bmatrix} | & & | \\ a_1 & \cdots & a_n \\ | & & | \end{bmatrix} \right)
\end{align}
$$


---


## Determinanten spezieller Matrizen

**Quadratische Permutationsmatrix**
- ungerade (gerade) Anzahl an Permutationen, dann ist die Determinante -1 (1)
**Untere/Obere Dreiecksmatrix**: 
- Diagonale multiplizieren
**Nur nicht-null Einträge an der Diagonale**
- Diagonale multiplizieren

---

→ [[05 Kofaktoren]] (Laplace-Formel)
→ [[03 The General Case]] (Leibnitz-Formel)