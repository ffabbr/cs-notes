## Orthogonalität von Unterräumen

- Wir können Orthogonalität von Vektorräumen über ihre Basen überprüfen.
  $v_1,\dots,v_k$ ist Basis von $V$ und $w_1,\dots,w_\ell$ ist Basis von $W$
  $$
V \perp W \quad \Longleftrightarrow \quad v_i \perp w_j \text{ für alle } i,j.
$$
- Wenn $V$ und $W$ orthogonale Unterräume sind, dann ist
$$
\{v_1,\dots,v_k,w_1,\dots,w_\ell\}
$$
linear unabhängig.

- **Korollar 5.1.4**
	1. $V \cap W = \{0\}$  
	2. $V+W \text{ ist ein Unterraum}$  
	3. $\dim(V+W)=\dim(V)+\dim(W)\le n$

---

## Orthogonales Komplement 

$$
V^\perp = \{ w\in\mathbb{R}^n \mid w^T v = 0\ \forall v\in V\}.
$$
$$
N(A) = C(A^T)^\perp = R(A)^\perp.
$$
$$
V=(V^\perp)^\perp
$$
$$
\mathbb{R}^n = V + V^\perp = \{\, v + w \mid v \in V,\; w \in V^\perp \,\}
$$

## Orthogonale Vektorräume

Folgende Aussagen sind äquivalent: 

1. $W=V^\perp$  
2. $\dim(V)+\dim(W)=n$  
3. Jede Darstellung  $u = v + w,\quad v\in V,\ w\in W.$

Achtung – orthogonale Komplemente sind definiert für Unterräume und **nicht für einzelne Vektoren.** 

---

## Orthonormale Vektoren

- orthogonal
- jeweils Länge 1

$A^{T}A = I \Longleftrightarrow$ A hat orthonormale Spalten

## Orthogonale Matrizen

Eine Matrix ist orthogonal, wenn ihre Spalten und Zeilen orthonormal sind, **muss also quadratisch sein**.

**Äquivalente Aussagen**
1. $Q$ ist orthogonal
2. $Q^T = Q^{-1}$
3. $Q^{T}Q = QQ^{T} = I$

**Beispiel Rotationsmatrix** (siehe [[1st Semester/LinAlg/Exercises/10 Sheet.pdf|10 Sheet]]) 

Da $Q^\top Q=I$, gilt für Q: 
- $||Qx||=||x||$
- $(Qx)^\top(Qy)=x^\top y$ 

![[Zerlegungen und Gram Schmidt#Gram-Schmidt]]

![[Pasted image 20251202221126.png]]