## Logik

- **kürzesten Weg** von einem Startknoten zu allen anderen Knoten finden
- funktioniert auch mit negativem Gewicht

## Vorgehen 
 
1. Den Startknoten auf Distanz **0** setzen, alle anderen Knoten auf **unendlich** ($\infty$) 
2. Man geht **jede einzelne Kante** (Verbindung) im gesamten Graphen einmal durch (die Reihenfolge ist egal) und prüft für jede Kante (von $A$ nach $B$):
    - Kenne ich schon einen Weg zu $A$ (Distanz nicht unendlich)
	    - Ja? Ist der Weg über $A$ nach $B$ kürzer als der Weg, den ich bisher für $B$ kannte?
		    - Ja? Aktualisiere die Distanz zu $B$ mit dem neuen, besseren Wert.
3. Diese komplette "Runde" (alle Kanten prüfen) genau **$|V| - 1$ Mal** durchführen
4. **==Negativen Zyklus erkennen==:** Genau eine weitere Runde durchführen, wenn ein Weg verkürzt werden kann, gibt es einen negativen Zyklus


> [!success] Invariante
> Nach i Iterationen ist $dist_s(v)$ minimal für alle v ∈ V die einen kürzesten s-v Pfad haben mit maximal i Kanten. 

## Pseudocode

Laufzeit: $O(|V|\cdot|E|)=O(n\cdot m)$

```java 
BellmanFord(E, c, s)
    d[1...n] = {inf, ..., inf}
    d[s] = 0

    for i = 1, ..., n-1:
        for (u, v) in E:
            d[v] = min(d[v], d[u] + c(u, v))

    // Letzte Iteration überprüft auf negative Zyklen
    for (u, v) in E:
        if d[u] + c(u, v) < d[v]:
            return "negative Cycle"

    return d
```

