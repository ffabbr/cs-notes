
- Ein Matching ist eine Kantenmenge, bei der kein Knoten zu mehr als einer Kante inzident ist
- jeder Graph hat ein Matching (z.B. leeres Matching)

1. [[#Arten von Matchings]]
2. [[#Greedy-Algorithmus]]
3. [[#Augmentierende Pfade]]
4. [[#Satz von Berge]]
5. [[#Satz von Hall]]
6. [[#Satz von Frobenius]]
7. [[#Hopcroft und Karp]]

## Arten von Matchings

==Perfektes== Matching
- alle Knoten werden überdeckt
- $|M|=\frac{|V|}{2}$
- in **vollständigem Graphen** mit **gerader Knotenanzahl** existiert immer ein perfektes Matching

==kardinalitätsmaximales== (*maximum*) Matching
- es gibt kein Matching mit mehr Kanten 

==inklusionsmaximales== (*maximal*) Matching
- können keine Kante zu dem Matching hinzufügen damit es ein Matching bleibt

![[Bildschirmfoto 2026-03-08 um 00.52.13.png]]

![[Bildschirmfoto 2026-03-05 um 16.48.11.png]]

---

## Greedy-Algorithmus

Mit dem Greedy-Algorithmus kann man in Zeit $O(|E|)$ ein ==inklusionsmaximales== Matching $M_{\text{Greedy}}$ bestimmen mit

$$|M_{\text{Greedy}}| \geq \frac{|M_{\text{max}}|}{2},$$
Allgemein: 
$$\frac{1}{2}|M_{\text{kard.max}}| \leq |M_{\text{inkl.max}}| \leq |M_{\text{kard.max}}|$$

→ $M_{\text{max}}$ ist ein kardinalitätsmaximales Matching 

![[2nd Semester/AuW/Slides/05 Slides.pdf#page=14|05 Slides]]

![[Bildschirmfoto 2026-03-08 um 00.54.43.png]]

```java
GREEDY-MATCHING (G)
1: M ← ∅
2: while E ≠ ∅ do
3:     wähle eine beliebige Kante e ∈ E
4:     M ← M ∪ {e}
5:     lösche e und alle inzidenten Kanten in G
```

![[Bildschirmfoto 2026-03-14 um 17.46.26.png]]

## Perfect matching in $2^k$ regular graph

Let $G = (A \cup B, E)$ be a $2^k$ -regular graph. We can find a perfect matching in $O(|E|)$ time. 

1. Repeat until Graph is $2^0=1$ -regular:
	1. note that this graph's connected components are eulerian
	2. find and traverse that eulerian cycle in $O(|E|)$ 
	3. remove every second edge
	4. we have $|E|/2$ edges left, the graph is $2^{k-1}$ -regular 
2. Each vertex now is degree 1, the graph itself is a perfect matching
$$|E| + \frac{1}{2}|E| + \frac{1}{4}|E| + \frac{1}{8}|E| + \dots = 2|E| \text{ (Geometrische Summe)}$$

> [!info]
> Let $G=(A \uplus B,E)$ be a $k$\-regular bipartite graph. Then there exist matchings $M_1,\dots,M_k$ such that they are pairwise disjoint and construct the entire set of edges together $E=M_1 \uplus \dots \uplus M_k$ and all $M_i$ are perfect matchings.


---

## Augmentierende Pfade

> [!Note] 
> Ein M-augmentierender Pfad P ist ein Pfad, der 
> - abwechselnd Kanten aus M und nicht aus M hat 
> - in von M ==nicht überdeckten Knoten beginnt und endet==
> - daher ungerade Länge hat

Können Matching M vergrössern mit **XOR zu M-augmentierendem Pfad**: 
- $M' = M \oplus P$
- gewinnen Länge +1. 

- Anzahl kantendisjunkte augmentierende Pfade bzgl. Matching M: 
  $|M^*| - |M|$, wobei $M^*$ ein kardinalitätsmaximales Matching ist


**Augmentierenden Pfad in ==bipartitem Graph== in linearer Zeit finden:** 

- BFS mit abwechselnd Kanten aus dem Matching und nicht dem Matching. 
- Ende, wenn es nicht überdeckten Knoten in aktuellem Layer gibt 

![[2nd Semester/AuW/Slides/06 Slides.pdf#page=6|06 Slides]]

---
## Satz von Berge

> Jedes nicht kardinalitätsmaximale Matching hat einen augmentierenden Pfad. 

Corollary: Let $M_1$ and $M_2$ be matchings. If $|M_2| = |M_1| + k$, then there exist $k$ $M_1$-augmenting-paths.

![[Bildschirmfoto 2026-03-08 um 01.07.14.png]]
![[Bildschirmfoto 2026-03-08 um 01.07.31.png]]

![[04 Slides.pdf#page=31]]

![[04 Slides.pdf#page=32]]


## Satz von Hall

Ein ==bipartiter== Graph $G=(A \uplus B,E)$ hat ein Matching $M$ der Grösse $|M|=|A| \iff |X| \le |N(X)|$ ==für alle Teilmengen== $X \subseteq A$. 

$N(X)$ sind die Nachbarknoten von X. 

> Jede Gruppe von Knoten aus $A$ muss insgesamt mindestens genauso viele Nachbarknoten in der Menge $B$ haben, wie die Gruppe selbst groß ist. 
> 
> Nur wenn diese Bedingung für jede Teilmenge gilt, ist garantiert, dass jeder Knoten aus $A$ einen eigenen, exklusiven Partner in $B$ finden kann (ein vollständiges Matching für $A$).

![[Bildschirmfoto 2026-03-08 um 14.00.41.png]]

**Beweis von Hall's Theorem**

![[Bildschirmfoto 2026-03-14 um 17.39.31.png]]

→ [[2nd Semester/AuW/Skript.pdf#page=76|Skript]] 

Slides
- [[04 Slides.pdf#page=35|=> Richtung]]
- [[04 Slides.pdf#page=36|<= Richtung]]
- [[04 Slides.pdf#page=37|<= Richtung]]

---

## Satz von Frobenius

Ein ==k-regulärer== Graph ist ein Graph, bei dem ==jeder Knoten Grad k== hat. Hier ist der Satz von Hall immer wahr, also gilt: 

>Jeder k-reguläre bipartite graph enthält ein perfektes Matching.

Perfektes Matching finden
- bipartit: $O(|V| \cdot |E|)$
- k-regulär, bipartit: $O(|E|)$

## Hopcroft und Karp

→ nur auf ==bipartiten== Graphen 
**→ [[2nd Semester/AuW/Skript.pdf#page=70|Skript]]** 

[[#Augmentierende Pfade]] finden mit besserer Laufzeit.

> **Idee**: Wenn wir effizient augmentierende Pfade finden können, können wir die Grösse des Matchings vergrössern bis wir ein kardinalitätsmaximales Matching haben. Upper bound für Vergrösserungen ist $O(|V|)$, da max. $\frac{|V|}{2}$ edges in Matchings. 

- it is able to find a maximal set of shortest pairwise disjoint M-augmenting-paths

1. Füge random Kante zu M
2. While $\exists$ augmentierende Pfade
	1. finde kürzesten augmentierenden Pfad
	2. finde inklusionsmaximale S dieser augmentierenden Pfade (disjunkt)
	3. augmentiere mit allen Pfaden aus S
3. kardinalitätsmax. Matching gefunden

**Runtime**

- While loop at most $O(\sqrt{|V|})$ times
- calculates maximum matching in $O(\sqrt{|V|} \cdot (|V| + |E|))$

![](https://youtu.be/lM5eIpF0xjA?si=g65DFdBSOwNwnWAd&t=251)

> [!warning]
>1. If $M$ is a matching and $P$ is a shortest $M$\-augmenting-path and $P'$ an $M \oplus P$\-augmenting-path (i.e. we apply $P$ first, then $P'$), then $$|P'| \geq |P| + 2|P \cap P'|$$ So if we augment $M$ successively with shortest $M$\-augmenting-paths, then the length of augmenting-paths cannot become smaller.
>2. with every iteration of the while-loop, the length of a shortest augmenting-path increases by at least 2.
>3. Let $M$ be a matching, where the length of the shortest augmenting-paths is $k$. Let $M'$ be an arbitrary another matching. Then $$|M'| \leq |M| + \frac{|V|}{k+1}$$


---

## Wahre Aussagen

> Sei $M$ ein Matching in $G$. $P$ und $P'$ seien zwei **knoten-disjunkte augmentierende Pfade** bzgl. $M$. Dann ist $(M \oplus P) \oplus P'$ ein Matching der Größe $|M| + 2$.

Ist wahr, weil knoten-disjunkt. 

> Falls bezüglich eines Matchings $M$ kein augmentierender Pfad der Länge eins existiert, ist $M$ bereits inklusionsmaximal.

Damit ein Pfad der Länge 1 (besteht nur aus einer Kante) bzgl. $M$ augmentierend ist, müssen beide Endknoten $u$ und $v$ **ungematcht** sein. Ein Matching ist inklusionsmaximal, wenn man keine weitere Kante aus dem Graphen hinzufügen kann, wenn es eine Kante gäbe, die man einfach zu $M$ hinzufügen könnte, müssten beide Endpunkte dieser Kante bisher ungematcht sein

> Sei G ein Graph mit $|V| = 12$ und einem perfekten Matching. Der kürzeste augmentierende Pfad bzgl. M hat 5 Kanten. Welche Werte kann $|M|$ annehmen?

