
- [[01 Algorithmen|01 Algorithmen]]
	- [[02 BFS|02 BFS]]
	- [[03 DFS|03 DFS]]
	- [[04 Dijkstra|04 Dijkstra]]
	- [[05 Bellman-Ford|05 Bellman-Ford]]
	- [[06 MST Overview|06 MST Overview]]
	- [[07 Boruvka|07 Boruvka]]
	- [[08 Prim|08 Prim]]
	- [[09 Kruskal|09 Kruskal]]
	- [[UnionFind.java|UnionFind]]
- [[Gerichtete Graphen und Darstellung|Gerichtete Graphen und Darstellung]]
- [[Topologische Reihenfolge|Topologische Reihenfolge]]

## Einführung

| **Begriff**        | **Bedeutung**                       |
| ------------------ | ----------------------------------- |
| Vertex             | Knoten                              |
| Grad eines Knotens | Anzahl anliegender Kanten           |
| Graph G=(V,E)      | mit Knotenmenge V und Kantenmenge E |

## Spezielle Typen 

| Begriff              | Bedeutung                                                                                                                          |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Weg (walk)**       | **Folge benachbarter Knoten**                                                                                                      |
| Eulerweg             | jede Kante genau einmal                                                                                                            |
| **Pfad (path)**      | **Weg ohne wiederholte Knoten**                                                                                                    |
| Hamiltonpfad         | jeder Knoten genau einmal                                                                                                          |
| Zyklus (closed walk) | **Weg mit Start = Ende**, mindestens 2 Knoten (hin-zurück-hin), Endknoten inzident zu (verbunden mit) geraden Anzahl Kanten im Weg |
| Eulerzyklus          | Eulerweg (jede Kante genau einmal) mit Anfang = Ende. Kann z.B. isolierte Knoten ohne Kante geben.                                 |
| Kreis (cycle)        | Anfang = Ende, aber kein Knoten wird 2 mal besucht, also mindestens 3 Knoten                                                       |
| Hamiltonkreis        | Kreis über alle Knoten                                                                                                             |

- Ist ein Pfad $\implies$ ist ein Weg
- Wenn Eulerweg existiert, dann sind $\leq 2$ Knotengrade ungerade
- ==Laufzeit== Eulerweg $O(n+m)$, 
- ==Laufzeit== Hamiltonpfad ist *polynomiell unmöglich*
- $\sum_{v∈V}\text{deg}(v)=2|E|$ (**Handschlagslemma**) 
- Weg ist Zyklus $\Longleftrightarrow$ der Endknoten vom Eulerweg ist inzident zu einer geraden Anzahl von Kanten
- ein Graph hat maximal $\frac{|V|\cdot(|V|-1)}{2}$ Kanten 
- Eulerzyklus existiert $\Longleftrightarrow$ alle Knotengrade gerade, Graph connectedk
- Walk-Algorithmus: 
  
  ```java
  walk(u):
	  if ∃ v mit uv ∈ E, nicht markiert
		  markiere uv
		  walk(v)
	  ```

- Euler-Walk Algorithmus nutzt eine ```for``` Schleife statt einer if

## Rede

| Begriff                 | Bedeutung                                                                                                                                                                                         |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| adjazent                | **benachbarte** Knoten                                                                                                                                                                            |
| inzident                | Kante **anliegend** zu einem Knoten                                                                                                                                                               |
| u erreicht v            | gibt einen Weg zwischen u und v (Äquivalenzrelation)                                                                                                                                              |
| Zusammenhangskomponente | Teil ist ineinander connected (Äquivalenzklasse der ÄR)                                                                                                                                           |
| eularian                | Graph enthält Eulerzyklus                                                                                                                                                                         |
| bipartit                | Graph lässt sich in zwei (Knoten-)Partitionen zerteilen, jede Kante verläuft durch beide. <br><br>Bipartit $\Leftrightarrow$ kein Zyklus ungerader Länge<br><br>Wenn abwechselnde Färbung möglich |

## Zusammenhang 

| Begriff                           | Bedeutung                                                                                                      |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Graph zusammenhängend (connected) | gibt nur eine Zusammenhangskomponente, Graph ist nicht getrennt, (man kommt von jedem Knoten zu jedem anderen) |
| Baum (tree)                       | Graph ist zusammenhängend und hat keinen Kreis                                                                 |
| cut vertex (Knoten)               | entfernt man den Knoten und alle anliegenden Kanten ist der Graph disconnected                                 |
| cut edge (Kante)                  | entfernt man die Kante (aber keine Knoten), ist der Graph disconnected                                         |


