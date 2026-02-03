## Logik

- andere Reihenfolge als [[03 DFS]] 
- Statt einen Weg "möglichst weit zu laufen", coveren wir erst alle Kanten von A. Also A nach B, zurück, A nach C, ..., B nach D, B nach F, bis Ebene 2 fertig, dann zurück zu A, Ebene 2, also C nach F, aber F schon besucht, also ned, etc.
## Breitensuchbaum

- erfasst **minimale Distanzen zu jedem Knoten**, jede Ebene nach unten ist eine Distanz mehr
- Bipartition erkennen: jede Ebene bekommt andere Farbe (abwechselnd)

## Pseudocode 

- **Queue:** First in First Out (enqueue, dequeue)
- **Laufzeit:** Wie [[03 DFS]], $O(|V|+|E|)$, wenn verbunden $O(|E|)$ 

```java
BFS(Adj):
    n = Adj.length
    visited[1...n] = {false, ..., false}
    
    for v = 1...n
        if visited[v] == false:
            Path(v, Adj, visited)

Path(v, Adj, visited)
    Q = [v]
    while Q not empty:
        u = dequeue(Q)
        visited[u] = true
        for w in Adj[u]
            if not visited[w]
                enqueue(Q, w)
```

![[BFS Notes.png]]

![[1st Semester/Media/Übung 10.pdf]]