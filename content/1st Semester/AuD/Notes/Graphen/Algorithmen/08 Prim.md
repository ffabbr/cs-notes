→ siehe [[06 MST Overview]]

**Anfang:** $v_{1}$ als besucht markieren/zum MST hinzufügen
Pro Iteration: 
- *Immer minimale ausgehende Kante aus der ganzen Zusammenhangskante, die nicht in zu einem anderen Knoten in der ZHK zeigt, hinzufügen.*, also: 
	- Alle anliegenden Kanten zu den "besucht" markierten Knoten anschauen, die zu einem Knoten führen, der nicht im MST ist. 
	- Minimum dieser Kanten auswählen und Knoten als besucht markieren/zum MST hinzufügen

Laufzeit $O((|V|+|E|)\cdot \log(|V|))$

→ vgl. [[04 Dijkstra]], statt nach Entfernung zu Startknoten zu arbeiten, wird mit Schnittprinzip ausgewählt
## Pseudocode

```java
Prim(G, s):                // s is the starting vertex, G = (V, E, c)
    P = PriorityQueue(V)   // all vertices initially have priority = ∞
    decreaseKey(P, s, 0)

    while not isEmpty(P):
        u = extractMin(P)
        mark u as visited

        for each (u, v) in E with v not visited:
            decreaseKey(P, v, min(currentKey(P, v), c(u, v)))

```

![[MST und Clustering.jpg]]![[Boruvka, Prim.png]]