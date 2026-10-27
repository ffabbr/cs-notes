
numerische Approximation von Integralen

Wir berechnen das Integral durch eine gewichtete Summe von bestimmten Funktionswerten 

$$
\int_a^b f(x)dx \approx \sum_{i=1}^n \omega_i f(x_i)
$$

**Fehler**
$E(n) := \left\vert{} \int_a^b f(x)dx - \sum_{i=1}^n \omega_i f(x_i) \right\vert{}$
- Algebraische Konvergenz: $E(n) \in O\left( \frac{1}{n^p} \right) \text{ für } p> 0$
- Exponentielle Konvergenz: $E(n) \in O(q^n) \text{ für } 0 \leq q \leq 1$ 

**Ordnung**
Ordnung $n+1 \implies$ können Polynome Grad $n$ exakt integrieren

> [!info] Unterräume
> ![[Bildschirmfoto 2026-10-19 um 23.27.36.png]]


| **Formel**      | **Lokaler Fehler** | **Globaler Fehler** | **Ordnung $p$** |
| --------------- | -------------- | --------------- | ----------- |
| **Mittelpunkt** | $O(h^3)$       | $O(h^2)$        | 2           |
| **Trapez**      | $O(h^3)$       | $O(h^2)$        | 2           |
| **Simpson**     | $O(h^5)$       | $O(h^4)$        | 4           |

Dabei ist $h$ die Länge des Intervalls $[a, b]$, also $h = \frac{b-a}{n}$.

Der lokale Fehler bezieht sich auf den Fehler auf einem Teil-Intervall $[x_i, x_{i+1}]$ und ist gegeben durch $E_{local} = O(h^{p+1})$.

Der globale Fehler bezieht sich auf den Fehler auf dem gesamten Intervall $[a, b]$ und ist die Summer aller lokalen Fehler, $E_{global} = nO(E_{local}) = O(h^p)$.

Romberg Schema

---

![[slide-01.png]]

![[slide-02.png]]

![[slide-03.png]]

![[slide-04.png]]

![[slide-05.png]]

![[slide-06.png]]

![[slide-07.png]]

![[slide-08.png]]

![[slide-09.png]]

![[slide-10.png]]

![[slide-11.png]]

![[slide-12.png]]

![[slide-13.png]]

![[slide-14.png]]

![[slide-15.png]]

![[slide-16.png]]

![[slide-17.png]]

![[slide-18.png]]

![[slide-19.png]]

![[slide-20.png]]

![[slide-21.png]]

![[slide-22.png]]

![[slide-23.png]]

![[slide-24.png]]

![[slide-25.png]]

![[slide-26.png]]



## Gauss Quadratur

Die Trapezregel oder die Simpsonregel unterteilen das Intervall in feste, meist gleichmäßig verteilte Abschnitte. Die Gauß-Quadratur wählt sowohl **Stützstellen** (Knotenpunkte) als auch deren **Gewichte** optimal aus.

So bekommen wir bei gleichem Rechenaufwand bessere Genauigkeit. Eine Gauß-Quadratur mit $n$ Stützstellen berechnet das exakte Integral für jedes Polynom bis zum Grad $2n-1$.

Bei der Gauss-Legendre-Quadratur entsprechen die Stützstelle den Nullstellen der Legendre-Polynome auf dem Standardintervall $[-1, 1]$. Jedes reale Integrationsintervall $[a, b]$ wird vor der Berechnung auf $[-1, 1]$ transformiert.

| Methode         | Feste Punkte | Ordnung | Verwendetes Polynom                                     |
| --------------- | ------------ | ------- | ------------------------------------------------------ |
| Gauss–Legendre  | keine        | $2n$    | $P_n^{(0,0)}(x)$                                         |
| Gauss–Radau     | 1 Randpunkt  | $2n-1$  | $P_{n-1}^{(1,0)}(x)$ oder $P_{n-1}^{(0,1)}(x)$           |
| Gauss–Lobatto   | 2 Randpunkte | $2n-2$  | $P_{n-2}^{(1,1)}(x)$                                     |


![[slide-05 1.png]]

![[slide-06 1.png]]

![[slide-07 1.png]]

![[slide-09 1.png]]

![[slide-10 1.png]]

![[slide-11 1.png]]

![[slide-12 1.png]]

![[slide-13 1.png]]

### Gauss-Legrende Quadratur

![[slide-14 1.png]]

![[slide-15 1.png]]

![[slide-16 1.png]]

![[slide-17 1.png]]

![[slide-18 1.png]]

![[slide-19 1.png]]

![[slide-20 1.png]]

![[slide-21 1.png]]


### Gauss-Radau Quadratur

![[slide-22 1.png]]


### Gauss-Lobatto Quadratur

![[slide-24 1.png]]


**Symmetrie der Knoten**: Auf dem Intervall $[-1, 1]$ sind die inneren Knoten symmetrisch um 0:
$x_i = -x_{n+1-i}$

**Symmetrie der Gewichte**: Die dazugehörigen Gewichte sind auch symmetrisch:
$b_i = b_{n+1-i}$


### Adaptive Quadratur

![[slide-27.png]]

![[slide-28.png]]

![[slide-29.png]]

![[slide-30.png]]

![[slide-31.png]]

![[slide-32.png]]


## Quadratur in Rd 

![[slide-33.png]]

![[slide-34.png]]

![[slide-35.png]]

![[slide-36.png]]

![[slide-37.png]]

![[slide-38.png]]

![[slide-40.png]]