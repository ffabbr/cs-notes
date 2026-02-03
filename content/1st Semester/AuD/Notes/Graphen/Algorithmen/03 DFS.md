## Logik

- bei *einem* Knoten starten
- zu einem benachbarten Knoten traversieren (wenn mehrere, dann lexografisch kleineren wählen), so weit wie möglich "vorlaufen"
- wenn "Sackgasse", also keine weitere Kanten zu unbesuchten Knoten, also einen Knoten über den Weg, "von dem wir gekommen sind" zurück, gibt es hier Kanten zu unbesuchten Knoten?
## Pseudocode

- **Stack:** Last in First out (push, pop)

### Ohne Pre- und Post-Order

```java
DFS(Adj):
    n = Adj.length
    visited[1...n] = {false, ..., false} 

    for v = 1...n:
        if visited[v] == false:
            Path(v, Adj, visited)


Path(v, Adj, visited):
	// Knoten v als besucht markiert
    visited[v] = true
    for u in Adj[v]:
        if visited[u] == false:
	        // alle unbesuchten Nachbarn besuchen
            Path(u, Adj, visited)
```

**Laufzeit** 
$O(|\text{Anzahl Knoten}|+|\text{Anzahl Kanten}|)$, 
$O(|\text{Anzahl Kanten}|)$, wenn verbunden, da $|V| \leq |E| +1$

*jeder Knoten wird genau einmal besucht (da visited Array), markieren ist Konstant*


> [!success] Order
> - **Pre-order**: 
>   Reihenfolge des ersten Betretens
>   
> - **Post-order**: 
>   Reihenfolge des letzten Verlassens, alle Nachfolger wurden bereits besucht, Teilbaum unter den Knoten ist abgearbeitet, dann wird zurücknummeriert
>   
> - Werden Pre- und Postorder zu jedem Knoten notiert, dann zählt man einfach bei Pre und Post-zahl weiter (gemeinsame Nummerierung, siehe Bild unten)

### Mit Pre- und Post-Order

→ [[#Pseudocode DFS mit Pre- und Post order]]

Liefert zusätzlich topologische Sortierung über Postorder und Informationen über den [[#Suchbaum]], siehe unten. 

[Vorlesungs-Snippet](https://video.ethz.ch/lectures/d-infk/2025/autumn/252-0026-00L/v/D6npeP4IDx7?t=01m27s)

## Suchbaum

Zeitlichen Ablauf als Suchbaum darstellen, siehe Bild, Mitte
### Spezielle Kanten im Suchbaum (siehe Bild rechts)

- **Tree edges**: Kanten im Tiefensuchbaum
- **Forward edges**
	- Kante zu indirektem Nachfolger, also von oben nach unten 
	- Pre-/Post Zahlen sind innerhalb der von der Quelle (ganz oben im [[#Suchbaum]])
- **Back edge**: 
	- Kante zu indirektem Vorgänger
	- Back-edge: gibt einen *directed cycle* 
- **Cross edge**: 
	- Kante, die zwei Knoten aus unterschiedlichen DFS-Teilbäumen verbindet, "man muss hoch und dann wieder runter laufen"

![[Pre- und Postorder.png]]

![[Tiefensuche.png]]
#### Beobachtungen

- $\exists$ back edge $\implies$ $\exists$ gerichteter Zyklus
- $\forall$ nicht back edges $(u,v) \in E$:  $post[u]\geq post[v]$ 

- Gibt es keinen gerichteten Zyklus, so
	- gibt es keine back edge 
	- umgekehrte post-order ist topologische Sortierung

![[Pasted image 20251116233306.png]]

## Pseudocode DFS mit Pre- und Post order

```java
static t = 1        // global time counter for pre/post timestamps

DFS(Adj):
    n = Adj.length
    visited[1..n] = {false, ..., false}

    pre[1..n]  = {-1, ..., -1}
    post[1..n] = {-1, ..., -1}

    // explore all components
    for v = 1..n:
        if visited[v] == false:
            Path(v, Adj, visited, pre, post)


Path(v, Adj, visited, pre, post):
    visited[v] = true
    pre[v] = t
    t = t + 1

    // visit all unvisited neighbors
    for u in Adj[v]:
        if visited[u] == false:
            Path(u, Adj, visited, pre, post)

    post[v] = t
    t = t + 1
``` 
