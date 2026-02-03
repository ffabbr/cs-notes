→ siehe [[06 Komplexe Zahlen]]

> [!success] Quick
> **Eigenwerte** berechnen: 
> - Nullstellen von $\det(A-\lambda I)$
> - Der Eigenwert von $A$ und $A^{\top}$ sind gleich. 
> - Diagonalmatrix oder Dreiecksmatrix: Einträge auf Diagonale sind Eigenwerte 
> - ähnliche Matizen ($B = S^{-1} \cdot A \cdot S$) haben die selben Eigenwerte
> 
> **Eigenvektoren** bestimmen:
> - für jeden Eigenwert $\lambda$, berechne Basis für $N(A-\lambda I)$
> - also berechne $A-\lambda I$ und dann $(A-\lambda I)\cdot x=0$ mit z.B. Gauss
> - Bei Diagonalmatrizen sind die Standardbasisvektoren die Eigenvektoren

## Vorstellung

- Vorstellung Determinante: Flächeninhalt
- Hier: Wie ändern Matrizen einen Vektor? 

- der **Eigenvektor** einer Matrix ist der Vektor, der seine Richung nach der Transformation nicht ändert und 
- der **Eigenwert** gibt an, wie sehr der Eigenvektor skaliert wird unter der Transformation

**Daher:**

In $Av=\lambda v$: 
- A ist die Matrix der Transformation
- v ist der Eigenvektor
- $\lambda$ ist der Eigenvalue

**Diagonalmatrix**: Eigenwerte sind auf der Diagonalen

> [!info] Also
> $Av=\lambda v$ sagt, dass A angewendet auf v das gleiche ergibt, als v by $\lambda$ zu skalieren.

![](https://youtu.be/PFDu9oVAE-g?si=hBefBKb8tNcOBy9F) 


## Berechnen

$Av=\lambda v$ 
$\Longleftrightarrow Av-\lambda v=0$
$\Longleftrightarrow (A-\lambda I)v=0$
$\Longleftrightarrow (A-\lambda I)v=0$           hat eine nicht triviale Lösung
$\Longleftrightarrow (A-\lambda I)$                  ist nicht invertierbar
$\Longleftrightarrow \det(A-\lambda I)=0$


---

## Beispiele, Eigenwerte

#### Beispiel 1
$$A = \begin{bmatrix} 2 & 3 \\ 1 & 0 \end{bmatrix}$$
$$\det(A - \lambda I) = \det \left( \begin{bmatrix} 2-\lambda & 3 \\ 1 & -\lambda \end{bmatrix} \right) = \lambda^2 - 2\lambda - 3 = 0$$
$$\lambda^2 - 2\lambda - 3 = (\lambda - 3)(\lambda + 1) = 0$$

**Eigenwerte:** 
- $\lambda_1 = 3$
- $\lambda_2 = -1$

#### Beispiel 2

→ siehe [[06 Komplexe Zahlen]]
$$A = \begin{bmatrix} 1 & -1 \\ 1 & 1 \end{bmatrix}$$
$$\det(A - \lambda I) = \det \left( \begin{bmatrix} 1-\lambda & -1 \\ 1 & 1-\lambda \end{bmatrix} \right) = \lambda^2 - 2\lambda + 2 = 0$$
$$\lambda_{1,2} = \frac{2 \pm \sqrt{-4}}{2}= \frac{2 \pm 2i}{2}= 1 \pm i$$
**Eigenwerte**
- $\lambda_1 = 1 + i$
- $\lambda_2 = 1 - i$

