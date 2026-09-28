- $(AA)x \rightarrow \mathcal{O}(n^3)$
- $A(Ax) \rightarrow \mathcal{O}(n^2)$

![[Bildschirmfoto 2026-09-27 um 22.03.50.png]]


## Diagonalmatrix

- Diagonalmatrix * A: Zeilen skaliert
- A * Diagonalmatrix: Spalten skaliert

z.B. D ist Diagonalmatrix, skaliert also die Spalten von A. Wir nutzen die Struktur von `D*A` aus: 

```python
D.diagonal()[:, np.newaxis]*A
```

`D.diagonal()` ist ein 1D Array der Diagonalwerte, `[:, np.newaxis]` macht daraus ein 2D Array (also macht aus der Zeile eine Spalte), und dann `*A` macht die Elementweise Multiplikation mit A.

## Multiplikation mit Relevanz oben rechts

Wir wollen $\mathbf{y} = \text{triu}(\mathbf{A}\mathbf{B}^T)\mathbf{x}$ berechnen. `triu` meint nur den Teil rechts oben. 

**Langsame Variante**: Wir berechnen $A\cdot B$, verwerfen alles außer den Teil rechts oben, und multiplizieren diese Matrix mit x. 

```python
M = A @ B.T
U = np.triu(M)
y = np.dot(U, x)
return(y)
```

**Schnelle Variante**: Wir berechnen $Bx$, dann machen wir $T\cdot (Bx)$, wobei T eine Matrix die `1` überhalb der Diagonalen hat, ist. 

$$
\begin{bmatrix} 1 & 1 & \dots & 1 \\ 0 & 1 & \dots & 1 \\ \vdots & \ddots & \ddots & \vdots \\ 0 & \dots & 0 & 1 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix} = \begin{bmatrix} v_1 + v_2 + \dots + v_n \\ v_2 + \dots + v_n \\ \vdots \\ v_n \end{bmatrix}
$$

Jetzt multiplizieren wir links A an.

```python
n, p = A.shape
Bx = B * x.reshape(-1, 1) # reshape macht Spaltenvektor
partial_sums = np.cumsum(Bx[::-1, :], axis=0)[::-1, :]
y = np.sum(A * partial_sums, axis=1)
```

## Kronecker Produkt

### Beispiel

$$A= \begin{pmatrix} 1 & 2\\ 3 & 4 \end{pmatrix} \qquad B= \begin{pmatrix} 5 & 6\\ 7 & 8 \end{pmatrix}$$
$$A\otimes B = \begin{pmatrix} 1B & 2B\\ 3B & 4B \end{pmatrix}$$
$$A\otimes B = \begin{pmatrix} 1\cdot5 & 1\cdot6 & 2\cdot5 & 2\cdot6\\ 1\cdot7 & 1\cdot8 & 2\cdot7 & 2\cdot8\\ 3\cdot5 & 3\cdot6 & 4\cdot5 & 4\cdot6\\ 3\cdot7 & 3\cdot8 & 4\cdot7 & 4\cdot8 \end{pmatrix}$$
### Kronecker mal Vektor

$(A \otimes B)x$

**Langsam**: Berechne $(A \otimes B)$ und dann mal x. 

```python
K = np.kron(A, B)
y = K @ x
```

**Schnell**: 

```python
n = A.shape[0]
X = x.reshape(n, n)
y = (A @ X) @ B.T     # ?!?!?!?!
return y.ravel()
```

- reshape nimmt den Vektor und zerteilt ihn in n Spalten
- ravel nimmt die Matrix und gibt alle Spalten untereinander in einen Vektor

## Vandermonde Matrix

→ [[04 Polynominterpolation]]
