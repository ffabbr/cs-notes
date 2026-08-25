## Zusammenhang

Ein Graph ist zusammenhängend, wenn es für alle $u, v \in V$ einen Pfad von u nach v gibt

> [!faq]- Formal
> Sei
> - $G=(V,E)$ ein Graph
>  - $u,v \in V$
>  - $X \subseteq V\setminus\{u,v\}$ 
>   
>   X ist ein u,v Separator, wenn u und v in verschiedenen ZHK von $G[V\setminus X]$ liegen

## k-Zusammenhang

### (Knoten-)Connectivity

G ist k-(Knoten-)zusammenhängend $\iff$ egal welche k-1 Knoten man entfernt, der Graph bleibt zusammenhängend

Condition $\vert{}V\vert{} \ge k+1$

> [!faq]- Formal
> Man muss mindestens k Knoten löschen, um den Zusammenhang (entweder des Graphens oder nur zwischen u → v) zu zerstören. 
> - **Zwei verschiedene Knoten u und v sind k-zusammenhängend**, wenn man weniger als k beliebige andere Knoten löschen darf, und trotzdem gibt es immer noch einen Weg u → v.
>- **Ein Graph G ist k-zusammenhängend**, wenn beliebige u,v k-zusammenhängend sind.
>
>Conditions: 
>- $|V| \geq k+1$
>- Jede Knotenmenge, die u und v trennen kann, muss mindestens k Knoten enthalten. Für beliebige Knoten u,v gibt es einen Weg u → v nachdem man bis zu k-1 Knoten entfernt hat.
>- For every vertex v, $deg(v) \geq k$, otherwise the graph is not k-connected (könnten sonst alle anliegenden Kanten löschen).
>k-connected $\implies (k-1)$ connected, for all $k > 1$ 

### Edge-Connectivity

G ist k-Kanten-zusammenhängend $\iff$ egal welche k-1 Kanten man entfernt, der Graph bleibt zusammenhängend

> [!success] Es gilt immer
> (**Knoten**-)Zusammenhang $\leq$ **Kanten**-Zusammenhang $\leq$ min. **Grad**

→ [[Bildschirmfoto 2026-02-25 um 15.38.13.png|Beispiele]]

---

## Separatoren

Eine Menge X von Knoten/Kanten X ist ein u-v-Separator: 
Löscht man alle Knoten/Kanten aus X, sind u, v nicht mehr verbunden (in verschiedenen ZHKs)

---
## Brücken 

Eine Kante {x, y} ist eine Brücke, wenn 
- G zusammenhängend ist
- G \ {x, y} nicht zuammenhängend

Für x und y gilt jeweils: ==entweder deg 1, oder ist cut vertex==.

## Artikulationsknoten (cut vertex) 

Ein Knoten v ist ein Artikulationsknoten, wenn 
- G zusammenhängend ist
- G \ v nicht zuammenhängend

---

## Satz von Menger 

### Knoten Version

G ist k-Knoten-zusammenhängend $\iff$ für zwei verschiedene Knoten gibt es mindestens k intern knotendisjunkte u-v Pfade

Jeder u-v Separator X hat Grösse $|X| \geq k \iff$ gibt k intern-knotendisjnkte u-v-Pfade.

### Kanten Version

G ist k-zusammenhängend $\iff \forall u,v \in V, u \neq v$, gibt es k kantendisjunkte u-v-Pfade

---

## Blöcke

> Blocks are units that contain all ==**edges**== which are in a cycle with one another (or also just a single edge).

Äquivalenzklassen der Äquivalenzrelation auf ==Kanten== 

$$
e \sim f :\Longleftrightarrow 
\begin{cases} e = f, & \text{oder} \\ 
\exists \text{ Kreis durch } e \text{ und } f \end{cases}
$$

Wenn sich zwei Blöcke schneiden, dann schneiden sie sich an einem Artikulationsknoten. 

![[Bildschirmfoto 2026-02-17 um 15.38.48.png]] 

### Block-Graph

- Two blocks can only overlap in a cut-vertex.
- Block-Partitionings can be determined in $O(|E|)$
- If G (original graph) was **connected**:
	- I is a **tree**

![[Bildschirmfoto 2026-02-17 um 15.56.55.png]]

> [!info]
> Building the block partitioning in time $O(|E|)$ requires **finding Cut Vertices and -Edges** in $O(|E|)$ time: → [[02 Tarjan]]


