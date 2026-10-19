
Approximation von Integralen

Algebraische Konvergenz: $E(n) \in O\left( \frac{1}{n^p} \right) \text{ für } p> 0$
Exponentielle Konvergenz: $E(n) \in O(q^n) \text{ für } 0 \leq q \leq 1$ 


| **Formel**      | **Lokaler Fehler** | **Globaler Fehler** | **Ordnung $p$** |
| --------------- | -------------- | --------------- | ----------- |
| **Mittelpunkt** | $O(h^3)$       | $O(h^2)$        | 2           |
| **Trapez**      | $O(h^3)$       | $O(h^2)$        | 2           |
| **Simpson**     | $O(h^5)$       | $O(h^4)$        | 4           |

Dabei ist $h$ die Länge des Intervalls $[a, b]$, also $h = \frac{b-a}{n}$.

Der lokale Fehler bezieht sich auf den Fehler auf einem Teil-Intervall $[x_i, x_{i+1}]$ und ist gegeben durch $E_{local} = O(h^{p+1})$.

Der globale Fehler bezieht sich auf den Fehler auf dem gesamten Intervall $[a, b]$ und ist die Summer aller lokalen Fehler, $E_{global} = nO(E_{local}) = O(h^p)$.

Romberg Schema