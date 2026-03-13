
> Keine adjazenten Knoten haben die gleiche Farbe.

> [!info]- Formale Definition
> Eine (Knoten-)Färbung eines Graphen $G = (V, E)$ mit **k Farben** ist eine Abbildung $c : V \to [k]$, so dass gilt $$c(u) \neq c(v) \text{ für alle Kanten } \{u, v\} \in E.$$

## Introduction

- Die **chromatische Zahl** $\chi(G)$ ist die **minimale Anzahl Farben**, die für eine Knotenfärbung von G benötigt wird.
- k-partit: können in k verschiedene Farben einfärben
- $\chi(G) \leq k \iff \text{G ist k-partit}$ 

**Runtime**
- G bipartit? $O(|E|)$
- G k-partit für $k\geq 3$: 
	- Exponentiell
	- ist ==NP-vollständig==
	- gibt ==keine Approximation==

- **2-färbbarer Graph**: Färbung mit BFS, ungerade/gerade Distanz
- **3-färbbarer Graph**: Zeit $O(|V| + |E|)$ mit $O(\sqrt{|V|})$ Farben färben
- **NP-vollständig**: gibt es eine Färbung mit $\leq k$  Farben mit $k \geq 3$

- Anzahl Färbungen: $O(2^{|V|} \cdot |V|)$

$\forall k \in \mathbb{N}, \forall r \in \mathbb{N} :$ Es gibt Graphen ohne einen Kreis mit Länge $\le k$, aber mit chromatischer Zahl $\ge r$.

> [!Note] 
> - maximal degree: $\Delta(G)$
> - minimal degree $\delta(G)$


## Greedy Algorithm

Der Greedy-Algorithmus färbt Knoten nacheinander und nimmt immer die erste verfügbare Farbe. 

Knoten in perfekter Reihenfolge: optimale Lösung

Laufzeit mit Adjecency list: 
- zusammenhängend: $O(|E|)$
- nicht zusammenhängend: $O(|E| + |V|)$ 

```java
GREEDY-FÄRBUNG (G)
1: wähle eine beliebige Reihenfolge der Knoten: V = {v1, ..., vn}
2: c[v1] ← 1
3: for i = 2 to i = n do
4:     c[vi] ← min{k ∈ ℕ | k ≠ c(u) für alle u ∈ N(vi) ∩ {v1, ..., vi-1}}
```

Number of colors $C(G)$ needed: 
$$\chi(G) \leq C(G) \leq \Delta(G) + 1.$$

- Gibt Reihenfolge $V = \{v_1, \dots, v_n\}$ der Knoten, Greedy-Algorithmus braucht nur $\chi(\mathbf{G})$ viele Farben
- Es gibt bipartite Graphen und eine Reihenfolge der Knoten, für die der GreedyAlgorithmus $|V|/2$ viele Farben benötigt. Kann auch passieren, dass bei bipartitem Graphen mehrere Farben benötigt. 

- Gilt für die (gewählte) Reihenfolge $|N(v_i) \cap \{v_1, \dots, v_{i-1}\}| \le k \quad \forall 2 \le i \le n$,  benötigt  Greedy-Algorithmus max. $\mathbf{k+1}$ Farben.
  
  Wenn du Knoten $v_i$ färbst, er hat max. $k$ Nachbarn , die in der Rhf vor ihm, so können diese Nachbarn max. $k$  Farben blockieren. Nehmen nächste freie Farbe nehmen, worst case Farbe $k+1$

- In jedem möglichen Restgraphen existiert ein Knoten, der maximal $k$ Nachbarn hat $\implies$ max. $k+1$ Farben (z.B. 2 Farben für Bäume)

- Wenn ein **zusammenhängender Graph** einen Knoten besitzt, dessen Grad **kleiner als das Maximum** ($\Delta(G)$) ist, liefert eine schlaue Sortierung eine Färbung mit höchstens $\Delta(G)$ Farben.

### Heuristik

**Smallest Last Coloring** für eine gute Reihenfolge: setze Knoten mit wenigsten Verbinungen ans Ende und entferne, suche weiter im Graphen Knoten mit wenigsten Verbindungen

1.  Platzierung: einfachsten Knoten ans Ende
2.  Sortierung: Ordne den Rest so an, dass ==jeder Knoten eine Verbindung zu einem späteren Knoten in der Liste== hat (z. B. per Breitensuche rückwärts).
3.  Vorteil: Beim Färben hat jeder Knoten höchstens $\Delta(G)-1$ bereits gefärbte Nachbarn – die "normalen" Knoten, weil einer ihrer Nachbarn noch ungefärbt ist; der letzte Knoten, weil er ohnehin nicht mehr Nachbarn hat.

---

### Planare Graphen

**Definition:** kann überkreuzungsfrei in der Ebene gezeichnet werden

> [!success]
> Ist ein Graph planar, so gibt es immer einen Knoten vom Grad $\le 5$.

- Die Heuristik findet eine Färbung mit $\le 6$ Farben für planare Graphen: 
  Gibt immer einen Knoten mit max. 5 Nachbarn, $k=5$. Also $5+1=6$

- ginge auch mit 4 Farben

---

## Block-Graph

Kann jeden Block eines Graphen mit max. $k$ Farben färben $\implies$ gesamter Graph ist k-färbbar. Also: $$\chi(G) = \max \{ \chi(B) \mid B \text{ ist ein Block von } G \}$$
Warum gilt das? 

- Färbung der Blöcke ist unabhängig voneinander, **ausser** am Artikulationsknoten
- Imagine in 
	- Artikulationsknoten hat Farbe 1 in Block Links
	- Artikulationsknoten hat Farbe 2 in Block Rechts
- tauschen im rechten Block Farben, sodass Artikulationsknoten auch Farbe 1 

---
## Satz von Brooks

*Remember:* 
Jeder Graph kann in Zeit $O(|E|)$ mit $\Delta(G)+1$ Farben gefärbt werden

*Satz von Brooks:*
$G \neq K_n, \quad G \neq C_{2n+1}, \quad G \text{ zusammenhängend:}$
$\implies G$ kann in Zeit $O(|E|)$ mit $\Delta(G)$ Farben gefärbt werden

> [!info]
> Man benötigt **$\Delta(G)+1$ Farben** bei
> 
> a) Kreisen mit **ungerader** Anzahl Knoten  
> b) **kompletten** Graphen
>
> Sonst, **höchstens Δ(G)** verschiedene Farben (zusammenhängend).

Beweis nicht prüfungsrelevant. 

![[Bildschirmfoto 2026-03-10 um 22.47.25.png]]


---

## 3-Färbung in linearer Zeit mit sqrt(n) Farben

Einen ==3-färbbaren Graphen== kann man in Zeit $O(|V| + |E|)$ mit $O(\sqrt{|V|})$ Farben färben.

1. Während es Knoten v gibt mit $> \sqrt{ |V| }$ ungefärbten Nachbarn: Färbe v mit neuer Farbe und Nachbarn mit 2 weiteren **neuen** Farben (BFS). 
2. Lösche v und Nachbarn (alle gefärbten Knoten). Restgraph hat Maximalgrad $\Delta \leq \sqrt{ |V| }$
3. Färbe verbleibende Knoten mit [[#Greedy Algorithm]] mit $\Delta + 1$ neuen Farben

There are at most $n/\sqrt{n} = \sqrt{n}$ many vertices of degree $\ge \sqrt{n}$. Thus in the first step, we used at most $3 \cdot \sqrt{n}$ colors (3 colors per neighborhood). In the second step, we used another $O(\sqrt{n})$ many colors. Since we used BFS and the greedy-algorithm, the algorithm operates in $O(|E|)$ runtime in total, which proves the theorem.

---

![[Bildschirmfoto 2026-03-12 um 16.02.10.png]]