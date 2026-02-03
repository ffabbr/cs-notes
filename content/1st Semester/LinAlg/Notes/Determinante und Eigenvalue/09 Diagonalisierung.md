
**Prerequesits**
- das charakteristische Polynom $\det(A-\lambda I)=0$ zerfällt in Linearfaktoren
- die geometrische und algebraische Vielfachheit der Eigenwerte muss gleich sein
	- algebraische Vielfachheit: wie oft ist eine Nullstelle eine Nullstelle
	- [[09b Geometrische Vielfachheit|geometrische Vielfachheit]]: $\dim(N(A-\lambda I))$ für jedes $\lambda$
	- gleich? *complete set of real eigenvectors*

Suche eine Diagonal Matrix D (nur Einträge auf der Diagonalen), die zur Matrix A ähnlich ist. A und B sind ähnlich, wenn es S gibt mit $B = S^{-1} \cdot A \cdot S$. Wir schreiben die Eigenwerte in die Diagonale.

$$D = \begin{pmatrix} \lambda_1 & 0 & \cdots & 0 \\ 0 & \lambda_2 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & \lambda_n \end{pmatrix}$$

- $V$ hat ==Eigenvektoren als Spalten==
- **$\Lambda$** ist ==Diagonalmatrix mit Eigenwerten== 

- $A = V \Lambda V^{-1}$
- $\Lambda = V^{-1} A V$


> [!success] Definition ähnliche Matrizen
> - A und B sind ähnlich, wenn S existiert sodass $B=S^{-1} AS$
> - ähnliche Matrizen haben die selben Eigenwerte


![[Bildschirmfoto 2025-12-20 um 19.57.54.png]]

---

## Matrix-Potenzen berechnen

z.B. man möchte $A^{100}$ berechnen. 

$$A^2 = (V \Lambda V^{-1}) \cdot (V \Lambda V^{-1})$$
$$A^2 = V \cdot \Lambda \cdot \Lambda \cdot V^{-1} = V \Lambda^2 V^{-1}$$
$$A^k = V \Lambda^k V^{-1}$$
$$\Lambda^k = \begin{pmatrix} \lambda_1^k & 0 \\ 0 & \lambda_n^k \end{pmatrix}$$