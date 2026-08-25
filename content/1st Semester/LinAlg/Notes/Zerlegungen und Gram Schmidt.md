## CR-Zerlegung

Zerlegung einer Matrix in ihre linear unabhängigen Spalten ($C$) und ihre Zeilenbasis ($R$).

- **Formel:** $A = C \cdot R$

1. Bringe $A$ in die reduzierte Zeilenstufenform (rref).
2. **R:** Nimm die Zeilen aus der rref, die nicht Null sind.
3. **C:** Nimm die Spalten aus der _Originalmatrix_ $A$, wo in der rref die führenden Einsen (Pivots) stehen.

Beispiel:

$$A = \begin{bmatrix} 1 & 3 & 4 \\ 2 & 6 & 8 \end{bmatrix}$$

1. **rref(A):** $\begin{bmatrix} \mathbf{1} & 3 & 4 \\ 0 & 0 & 0 \end{bmatrix}$ (Pivot ist in Spalte 1).
2. **R:** $\begin{pmatrix} 1 & 3 & 4 \end{pmatrix}$ (die einzige Nicht-Null-Zeile).
3. **C:** $\begin{pmatrix} 1 \\ 2 \end{pmatrix}$ (die 1. Spalte aus $A$).
4. **Check:** $\begin{bmatrix} 1 \\ 2 \end{bmatrix} \cdot \begin{bmatrix} 1 & 3 & 4 \end{bmatrix} = \begin{bmatrix} 1 & 3 & 4 \\ 2 & 6 & 8 \end{bmatrix} = A$.

*oder mache Gauss-Jordan, nehme die Spalten die eine neue Zeile introducen für C und gleich die ersten Zeilen als R'*

![[CR-Decomposition Script.png]]

---

## Gram-Schmidt

**Ziel:** Basis (linear unabhängige Matrix) **orthogonal und Länge 1** machen

**Step-by-Step:**
Gegeben $n$ linear unabhängige Vektoren $a_1, \dots, a_n$, die den Unterraum $S$ erzeugen. 

1. $q_1 = \frac{a_1}{\|a_1\|}$
2. Für $k=2, \dots, n$ setze: $$q_k' = a_k - \sum_{i=1}^{k-1} (a_k^\top q_i) q_i \quad , \quad q_k = \frac{q_k'}{\|q_k'\|}$$
---

## QR-Zerlegung

$A = QR$

- **Q** ist $m \times n$ Matrix mit orthonormalen Spalten (output von [[Zerlegungen und Gram Schmidt#Gram-Schmidt|Gram Schmidt]]). 
	- $QQ^\top A=A$
- **R** ist obere Dreiecksmatrix durch $R=Q^\top A$
	- **R ist invertierbar**

