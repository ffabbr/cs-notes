
## Beispiele für NP-vollständige Probleme

- ==Hamiltonkreis==
- Rucksackproblem
- Gibt es in einem Graphen k paarweise benachbarte Knoten? 
- Hat ein Polynom mod n eine Nullstelle? 
- Hat eine logische Formel eine Lösung? 

## Traveling Salesman Problem

*NP-vollständig, kann nicht approximiert werden, vollständiger Graph*

Gegeben: 
- ==vollständiger Graphen== mit n Knoten
- Distanzen zwischen allen Knoten

Gesucht: 
- minimale Länge eines Hamiltonkreises (kürzeste Rundreise)

### NP Vollständigkeit zeigen

Hamiltonkreis-Problem zu TSP umformulieren. In den Graph fehlende Kanten mit Länge 1 hinzufügen, existierende Kanten Länge 0. Hamiltonkreis in $G \iff$ TSP Lösung von $G' = 0$. 

Wenn der Ursprungsgraph $G$ einen Hamiltonkreis besitzt, kann die kürzeste Rundreise (TSP) im Graphen $G'$ genau diese Kanten nutzen. Wenn man also das TSP für den Graphen $G'$ löst und eine Tour der Länge 0 findet, hat man gleichzeitig bewiesen, dass ein Hamiltonkreis in $G$ existiert.

![[Bildschirmfoto 2026-03-08 um 00.40.45.png]]

Es gibt auch keinen Approximationsalgorithmus. Wenn in unserem konstruierten Graphen $G'$ das Optimum $0$ ist (weil ein Hamiltonkreis existiert), dann ist $c \cdot 0 = 0$.

### Metrisches TSP

==vollständiger Graphen==, der die ==Dreiecksungleichung== erfüllt

- immer noch **NP-Vollständig**
- kann **approximiert** werden 

#### 2 Approximation für METRISCHES TSP

$O(n^2)$, Adjazenzmatrix. 
Approximation ist im worst case doppelt so lange wie OPT.

Wir bringen ***jeden Knoten auf geraden Grad, damit es eine Eulertour gibt***. Dann, die grünen Abkürzungen sind immer effizienter, da der Graphen die ==Dreiecksungleichung==.

1. ==MST== bestimmen (T), $l (T) \leq opt(K_{n}, l)$
2. Kanten von T verdoppeln, es gilt, $2 l (T) \leq 2 opt(K_{n}, l)$
3. Bestimme ==Eulertour== W (laufe aussen rum)
4. durchlaufe W, mit ==Abkürzungen==, so dass jeder Knoten nur einmal besucht wird $\implies$ Hamiltonkreis C. 

![[Bildschirmfoto 2026-03-05 um 11.47.16.png]]
![[Bildschirmfoto 2026-03-08 um 00.48.47.png]]

#### 1.5 Approximation für METRISCHES TSP

1. bestimme ==MST==
2. X := alle Knoten mit ungeradem Grad im MST. Gibt eine gerade Anzahl ungerader Knoten (Handschlaglemma, $2|E|$ ist gerade)
3. Bestimme ==minimales Matching== M für X. Es gilt $l(M) \leq \frac{1}{2} \text{opt}(K_{n}, l)$
4. Bestimme ==Eulertour==, es gilt $l(T) + l(M) \leq \frac{3}{2} \text{opt}(K_{n}, l)$
5. durchlaufe W, mit ==Abkürzungen==, sodass jeder Knoten nur einmal besucht wird $\implies$ Hamiltonkreis. $l(T)+l(M) \leq \frac{3}{2} \text{opt}(K_{n}, l)$

