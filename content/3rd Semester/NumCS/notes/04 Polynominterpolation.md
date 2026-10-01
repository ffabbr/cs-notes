
Wir approximieren eine Funktion durch ein Polynom. Je glatter $f$ ist, desto besser funktioniert das. Es gibt ein Polynom $p$ welches die Funktion $f$ beliebig gut approximiert. 

Polynom von Grad k ist durch $k+1$ Punkte eindeutig bestimmt.

Wir notieren das Polynom als eine Linearkombination von Basen. 

## Basen

Eine **Basis** $b_0,\dots,b_m$ ist linear unabhängig und erzeugend. Jedes $f\in\mathcal{P}_m$ lässt sich eindeutig schreiben als

$$f(t) = \sum_{j=0}^m \alpha_j b_j(t) = \boldsymbol{\alpha}^\top \mathbf{b}(t).$$

z.B. Monombasis: $p_n(x) = \alpha_0 + \alpha_1 x + \alpha_2 x^2 + \dots + \alpha_n x^n$
Dimension der Basis: Anzahl der Elemente in der Basisdefinition

## Interpolationsgleichung

Die Bedingungen $f(t_i)=y_i$ ergeben ein lineares Gleichungssystem:

$$\underbrace{\begin{bmatrix} b_0(t_0) & \dots & b_m(t_0)\\ \vdots & \ddots & \vdots \\ b_0(t_n) & \dots & b_m(t_n)\end{bmatrix}}_{B\in\mathbb{R}^{(n+1)\times(m+1)}} \begin{bmatrix}\alpha_0\\ \vdots \\ \alpha_m\end{bmatrix} = \begin{bmatrix}y_0\\ \vdots \\ y_n\end{bmatrix} \iff B\boldsymbol{\alpha} = \mathbf{y}$$

Und suchen die Koeffizienten mit Bedingung $p_n(x_i) = y_i$.

Matrix-Form: 
$$
\underbrace{ \begin{bmatrix} 1 & x_0 & \cdots & x_0^n \\ 1 & x_1 & \cdots & x_1^n \\ \vdots & \vdots & \ddots & \vdots \\ 1 & x_n & \cdots & x_n^n \end{bmatrix} }_{\text{Vandermonde-Matrix}} \begin{bmatrix} \alpha_0 \\ \alpha_1 \\ \vdots \\ \alpha_n \end{bmatrix} = \begin{bmatrix} y_0 \\ y_1 \\ \vdots \\ y_n \end{bmatrix}
$$

## Vandermonde Matrix erstellen

Langsam: 

```python
for j in range(1, Z.shape[1]): # alle spalten
	# gesamte erste dimension (alle Zeilen), und nur Spalte j
	Z[:, j] = t ** j 
	return Z
```

Schnell:

```python
def dirZ(Z):
	# künstliche neue achse 
	Z[:, 1:] = t[:, np.newaxis]
	# kumulatives produkt in-place also [1, x, x^2, x^3, x^4]
	np.cumprod(Z, axis=1, out=Z)
	return Z
```

Kumulatives Produkt: 

- Spalte 0: Algorithmus startet. Wert ist 1
- Spalte 1: bisheriges Ergebnis (1) multipliziert mit aktuellen Wert der Spalte ($x$), also: $1 \cdot x$
- Spalte 2: bisheriges Ergebnis ($x$) multipliziert mit dem aktuellen Wert der Spalte ($x$), also: $x \cdot x$. 
- etc.

## Horner Schema

Wir klammern $x$ wiederholt aus und bekommen 
$$
p(x) = (x \dots x (x (\alpha_n x + \alpha_{n-1}) + \dots + \alpha_1) + \alpha_0)
$$
z.B. $n=3$
$p(x) = x(x(\alpha_3 x + \alpha_2) + \alpha_1) + \alpha_0$

```python
def horner(p, x): 
	y = p[0] # innerste klammer
	for i in range(1,len(p)): 
		# bisheriges y mal x plus aktueller Koeffizient p[i]
		y = x * y + p[i]
	return y
```

## Lagrange


$$l_i(x) = \prod_{\substack{j=0 \\ j \neq i}}^{n} \frac{x - x_j}{x_i - x_j}.$$



## Barizentrische Formel

## Newtons

divide and differences - koeffizienten

Seite 45