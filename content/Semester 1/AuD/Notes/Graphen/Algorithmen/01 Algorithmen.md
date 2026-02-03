
> [!success] Tipp
> Nicht den Algorithmus verändern, sondern den Graphen. 

- **sichere Kanten:** enthalten in jedem MST
- **Schnittprinzip**: Für jedes Subset ist die minimale ausgehende Kante sicher. 
## Algorithmen

- [[02 BFS]] (Breitensuche, kürzeste Wege finden)
- [[03 DFS]] (Tiefensuche, Pfade erkunden)
- [[04 Dijkstra]] (kürzesten Weg **ohne** negative Kante)
- [[05 Bellman-Ford]] (kürzesten Weg mit negativen Kanten)
- [[07 Boruvka]] (MST durch Kantenverbindung)
- [[08 Prim]] (MST durch Knotenerweiterung)
- [[09 Kruskal]] (MST durch Kantensortierung)


### Overview

> [!success] Overview  
> **==Kürzeste Wege==**
> **Dijkstra**:				Schranken verbessern, jedes mal vom minimalen Knoten, **keine** neg. Kanten
> **Bellman-Ford**:			V-1 mal Schranken verbessern, Reihenfolge egal, auch wenn neg.
> 
> **==MST==**
> **Boruvka**: 			minimale Kante an jeder ZHK anfügen bis es nur mehr eine ZHK gibt
> **Prim**: 				minimale ausgehende Kante aus der gesamten ZHK anfügen
> **Kruskal**: 			edges von billig → teuer hinzufügen


## What to use?

#### BFS vs DFS

| **Frage / Aufgabe**                                          | **[[03 DFS\|DFS]]** | **[[02 BFS\|BFS]]** |
| ------------------------------------------------------------ | :-----------------: | :-----------------: |
| $G$ verbunden?                                               |          ☑          |          ☑          |
| Hat $G$ gerichteten Zyklus?                                  |          ☑          |          ☑          |
| topologische Sortierung ausgeben                             |          ☑          |          ☐          |
| $G$ Bipartit?                                                |          ☑          |          ☑          |
| Kürzester Weg von $v \in V$ zu jedem anderen Knoten Ausgeben |          ☐          |          ☑          |
| Längsten Pfad (meiste Kanten) in $G$ finden.                 |          ☐          |          ☐          |


![[Graphenalgos, Übersicht.png]]