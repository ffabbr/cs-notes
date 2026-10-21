
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