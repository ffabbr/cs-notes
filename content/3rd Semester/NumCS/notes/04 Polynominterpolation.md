
Wir approximieren eine Funktion durch ein Polynom. 

Je glatter $f$ ist, desto besser funktioniert das. Es gibt ein Polynom $p$ welches die Funktion $f$ beliebig gut approximiert. Polynom von Grad k ist durch $k+1$ Punkte eindeutig bestimmt. Wir notieren das Polynom als eine Linearkombination von Basen. 
## Basen

linear unabhängig und erzeugend. 
z.B. Monombasis: $p_n(x) = \alpha_0 + \alpha_1 x + \alpha_2 x^2 + \dots + \alpha_n x^n$
## Interpolationsgleichung

Die Bedingungen $f(t_i)=y_i$ ergeben ein lineares Gleichungssystem:

$$\underbrace{\begin{bmatrix} b_0(t_0) & \dots & b_m(t_0)\\ \vdots & \ddots & \vdots \\ b_0(t_n) & \dots & b_m(t_n)\end{bmatrix}}_{B\in\mathbb{R}^{(n+1)\times(m+1)}} \begin{bmatrix}\alpha_0\\ \vdots \\ \alpha_m\end{bmatrix} = \begin{bmatrix}y_0\\ \vdots \\ y_n\end{bmatrix} \iff B\boldsymbol{\alpha} = \mathbf{y}$$

Bei **Polynom**: 
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

Schnelles **Auswerten** eines Polynoms: 
Wir klammern $x$ wiederholt aus, und berechnen dann.

z.B. $n=3$ 
$$
p(x) = x(x(a x + b) + c) + d
$$ 

```python
def horner(p, x): 
	y = p[0] # innerste klammer
	for i in range(1,len(p)): 
		# bisheriges y mal x plus aktueller Koeffizient p[i]
		y = x * y + p[i]
	return y
```

---

## Newton Basis

Das gleiche Polynom kann man mit anderen Basen schreiben, um die Berechnung der Koeffizienten zu vereinfachen. Statt Vandermonde Matrix verwenden wir eine Basis, sodass wir eine untere Dreiecksmatrix haben. So können wir die Koeffizienten effizienter bestimmen. 

**a: Forward Substitution**

Basiselemente basierend auf den Stellen: 

- $N_0(t) = 1$
- $N_1(t) = (t - t_0)$
- $N_2(t) = (t - t_0)(t - t_1)$
- $N_i(t) = (t - t_0)(t - t_1)\dots(t - t_{i-1}) = \prod_{j=0}^{i-1} (t - t_j)$ 

Also ist z.B. $N_{1}(t_{0})=0$, da es den Faktor $(t_{0}-t_{0})$ enthält. 
Wir haben somit eine untere Dreiecksmatrix

$$
\begin{bmatrix}
1 & 0 & \cdots & 0 \\
1 & (t_1 - t_0) & \ddots & \vdots \\
\vdots & \vdots & \ddots & 0 \\
1 & (t_n - t_0) & \cdots & \prod_{i=0}^{n-1}(t_n - t_i)
\end{bmatrix}
\begin{bmatrix}
\alpha_0 \\
\alpha_1 \\
\vdots \\
\alpha_n
\end{bmatrix}
=
\begin{bmatrix}
y_0 \\
y_1 \\
\vdots \\
y_n
\end{bmatrix}
$$

Lösen des Gleichungssystems: 
1. erste Zeile: $1 \cdot \alpha_0 = y_0 \implies \alpha_0 = y_0$
2. zweite Zeile: $\alpha_0 + (t_1 - t_0)\alpha_1 = y_1$, mit $\alpha_0 = y_0$ also $\alpha_1 = \frac{y_1 - y_0}{t_1 - t_0}$ 
3. etc. 

**b: dividierte Differenzen**

Base Case $k=0$:    $f[t_i] = y_i$

$$
f[t_i, \dots, t_{i+k}] = \frac{f[t_{i+1}, \dots, t_{i+k}] - f[t_i, \dots, t_{i+k-1}]}{t_{i+k} - t_i}
$$

z.B. 
- $f[t_0, t_1] = \frac{f[t_1] - f[t_0]}{t_1 - t_0}$
- $f[t_0, t_1, t_2] = \frac{f[t_1, t_2] - f[t_0, t_1]}{t_2 - t_0}$

![[Bildschirmfoto 2026-10-04 um 16.56.04.png]]

```python
for i in range (1, n): 
  for j in range (n-1, i-1, -1):
	y[j] = (y[j]-y[j-1])/(x[j] - x[j-i])

return(y)
```

oder

```python
for i in range (1, n):
	y[i:] = (y[i:] - y[i-1:-1]) / (x[i:] - x[:-i])

return y
```


**Dann: Interpolant aufstellen**
berechnete Koeffizienten der Diagonalen mit den Basiselementen multiplizieren und Summieren

$$
f(t) = \sum_{i=0}^n f[t_0, \dots, t_i] N_i(t)
$$

-> auch hier Horner Schema zum Auswerten verwenden

```python
# Input: x  ... Stuetzstellen
#   dd ... dividierte Differenzen
#   xx ... auswertungspunkte
# Output: yy ... Newton-Polynom ausgewertet an xx

n = len(dd)
r = 0*xx

for i in range(n-1, -1, -1):
	r = dd[i] + (xx - x[i]) * r

return r
```

-> Vorteil: können einfach neue Werte hinzufügen, ohne alles neu zu berechnen.

---
## Lagrange-Basis statt Monome

-> kommt ein neuer Wert hinzu, müssen wir mit Lagrange Basis alles neu berechnen

Statt Gleichungssystem mit Vandermonde oder untere Dreiecksmatrix Matrix, haben wir hier nur mehr eine Einheitsmatrix mit $L_{n}(x)$. 

$$
L_i(x) = \prod_{\substack{j=0 \\ j \neq i}}^{n} \frac{x - x_j}{x_i - x_j}
$$
somit
$$
L_i(x_k) = \begin{cases} 1 & k = i \\ 0 & k \neq i \end{cases}
$$

z.B. $x_0=1,\quad x_1=2,\quad x_2=4$, $\quad L_0(x)=\frac{(x-2)(x-4)}{(1-2)(1-4)}$,  entweder es kürzt sich alles zu 1 oder es kommt Faktor 0 im Zähler

Bei $B\alpha=y$ haben wir also die Einheitsmatrix und somit $\mathbf{I}\alpha=y \;\Rightarrow\; \alpha=y$, $f(t)=\sum_{i=0}^n y_i\,L_i(t)$. 

> [!example] Beispiel: Monombasis vs. Lagrange-Basis
> Gesucht: $f$ mit $f(0)=3$ und $f(1)=5$.
>
> **Monombasis:** $f(x)=\alpha_0+\alpha_1 x$. Gleichungssystem lösen: $\alpha_0=3$, $\alpha_0+\alpha_1=5 \Rightarrow \alpha_1=2$, also $f(x)=3+2x$. (Bei vielen Punkten aufwendig.)
>
> **Lagrange-Basis:** $L_0(x)=\frac{x-1}{0-1}=1-x$, $L_1(x)=\frac{x-0}{1-0}=x$. Die Koeffizienten kennst du sofort, $\alpha_i=f(x_i)$, also $f(x)=3(1-x)+5x=3+2x$. 

### Lagrange-Basis mit Barizentrischer Formel

Für jeden Auswertungspunkt mussten wir alle $L_{i}(x)$ neu berechnen. Das wollen wir vereinfachen. Wir spalten den von t unabhängigen Teil ab. 

Definiere $\frac{1}{\lambda_i}:=\prod_{j\neq i}(t_i-t_j)$. 

$L_i(t)=\frac{\prod_{j\neq i}(t-t_j)}{\prod_{j\neq i}(t_i-t_j)}$. Siehe, der Nenner enthält kein $t$. Den Zähler schreiben wir um als $\prod_{j\neq i}(t-t_j)=\frac{\prod_{j=0}^n(t-t_j)}{t-t_i}$. Somit haben wir $L_i(t)=\Big(\prod_{j=0}^n(t-t_j)\Big)\cdot\frac{\lambda_i}{t-t_i}$, können umschreiben zu $\prod_{j=0}^n(t-t_j)=\frac{1}{\sum_{i=0}^n\frac{\lambda_i}{t-t_i}}$. Wir schreiben um zu 

$$
f(t)=\frac{\sum_{i=0}^n\frac{\lambda_i}{t-t_i}\,y_i}{\sum_{i=0}^n\frac{\lambda_i}{t-t_i}}
$$
Wenn $t$ genau einem Knoten $t_i$ entspricht, steht im Nenner $t-t_i=0$, und es gibt eine Division durch null. In dem Fall gibt man direkt $f(t_i)=y_i$ zurück.

```java
def barycentric_weights(x):
    n = len(x)
    barweight = np.ones(n)
    for j in range(n):
      diff = x[j] - x
      diff[j] = 1.0 
      barweight[j] = 1.0 / np.prod(diff)
    return barweight
```

## Chebyshev Interpolation

Wir optimieren, indem wir andere, nicht-gleichverteilte Punkte als Referenz wählen. 

- **Chebyshev-Knoten:** Die $n+1$ Knotenpunkte für $k=0, \dots, n$ berechnen sich durch die Formel $x_k = a + \frac{1}{2}(b-a)\left(\cos\left(\frac{2k+1}{2(n+1)}\pi\right) + 1\right)$.
- **Chebyshev-Abszissen:** Diese berechnen sich durch $x_k = a + \frac{1}{2}(b-a)\left(\cos\left(\frac{k}{n}\pi\right) + 1\right)$. Wenn man die Endpunkte des Intervalls bei der Berechnung auslassen möchte, läuft der Index lediglich über $k=1, \dots, n-1$.

Chebyshev-Polynome $T_k(x)$ als Basis: 
$p(x) = c_0 + c_1 T_1(x) + \dots + c_n T_n(x)$

**Clenshaw-Algorithmus**
- Man setzt die Startwerte $d_{n+2} = d_{n+1} = 0$.
- Man berechnet rückwärts für jedes $k$: $d_k = c_k + (2x)d_{k+1} - d_{k+2}$.
- Der endgültige Funktionswert ergibt sich dann aus $p(x) = d_0 - x d_1 = \frac{1}{2}(d_0 - d_2)$.

```python
def clenshaw(a,x):
	d_k1 = 0.0 * x
	d_k2 = 0.0 * x

	for k in range(len(a) - 1, 0, -1):
		d_k = a[k] + 2.0 * x * d_k1 - d_k2
		d_k2 = d_k1
		d_k1 = d_k
	
	y = a[0] + x * d_k1 - d_k2
	return y
```

