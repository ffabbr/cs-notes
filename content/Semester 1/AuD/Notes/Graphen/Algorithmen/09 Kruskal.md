## Vorgehen 

**Anfang:** jeder Knoten ist seine eigene Zusammenhangskomponente

1. Sortiere alle edges im Graphen von billig zu teuer
2. füge die kleinste Edge, die zwei ZHKs neu verbindet (keine cycles), hinzu

> [!success] CodeExpert
> In CodeExpert schauen, **ob Arrays importiert ist**, wenn ja, dann ```Arrays.sort()``` 


![[Kruskal Example.png]]

## Pseudocode

```java
Kruskal(edges):
    U = unionFind(n)
    sort(edges)              // nach Gewicht sortieren
    MST = leere Liste
    for e in edges:
        (u, v) = e
        if not U.same(u, v):
            MST.add(e)
            U.union(u, v)

    return MST
```

## Laufzeit 

Alle Kanten einzelnd durchzugehen und DFS laufen zu lassen (um ZHK zu überprüfen) wäre $O(n\cdot(n+m))$. 

Mit [[#Datenstruktur Union-Find]] $O(|V|\cdot \log(|V|)+|E|\cdot \log(|E|))$.  

**Amotisierte Laufzeit** (durchschnittlicher worst-case) von union
- wäre ja theoretisch $O(|V|)$, aber eine Situation wie ZHKs $\frac{V}{2}-1$ und $\frac{V}{2}$ ist unwahrscheinlich
- also im Schnitt $O(\log|V|)$

Asymptotisch gleich wie Boruvka und Prim da maximale Anzahl Kanten $\frac{|V|\cdot(|V|-1)}{2}$, $O((|V|+|E|)\cdot \log(|V|))$

## Datenstruktur Union-Find

→ siehe [[UnionFind.java]]

- make 
- same (sind u und v in der gleichen ZHK?)
- union (verbindet zwei ZHKs)
#### Pseudocode

```java
class UnionFind
    rep = Array[n]
    // für jeden Knoten: speichert den "Repräsentanten"
    // der verbundenen Komponente dieses Knotens

    members = Array of LinkedLists[n]
    // für jeden Repräsentanten: eine LinkedList,
    // die alle Knoten seiner Komponente enthält

    make(V):    // V ist die Menge aller Knoten des Graphen
        for each v in V:
            rep[v] = v
            // zu Beginn ist jeder Knoten seine eigene Komponente

    same(u, v):
        return rep[u] == rep[v]
        // haben sie denselben Repräsentanten,
        // liegen sie in derselben Komponente

    union(u, v):
        // ohne Einschränkung der Allgemeinheit nehmen wir an,
        // dass die Komponente von u kleiner ist als die von v

        for x in members[rep[u]]:
            rep[x] = rep[v]        // (1)
            members[rep[v]].add(x) // (2)

```


![[04122025-1.png]]
![[04122025-2.png]]![[Bildschirmfoto 2025-12-07 um 23.16.10.png]]