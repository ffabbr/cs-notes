
- Ein Matching ist eine Kantenmenge, bei der kein Knoten zu mehr als einer Kante inzident ist
- jeder Graph hat ein Matching (z.B. leeres Matching)

## Arten von Matchings

==Perfektes== Matching
- alle Knoten werden überdeckt
- $|M|=\frac{|V|}{2}$

==kardinalitätsmaximales== Matching
- es gibt kein Matching mit mehr Kanten 

==inklusionsmaximales== Matching
- können keine Kante zu dem Matching hinzufügen damit es ein Matching bleibt

![[Bildschirmfoto 2026-03-08 um 00.52.13.png]]

![[Bildschirmfoto 2026-03-05 um 16.48.11.png]]

---

## Greedy-Algorithmus

Mit dem Greedy-Algorithmus kann man in Zeit $O(|E|)$ ein ==inklusionsmaximales== Matching $M_{\text{Greedy}}$ bestimmen mit

$$|M_{\text{Greedy}}| \geq \frac{|M_{\text{max}}|}{2},$$

→ $M_{\text{max}}$ ist ein kardinalitätsmaximales Matching 

![[Bildschirmfoto 2026-03-08 um 00.54.43.png]]

```java
GREEDY-MATCHING (G)
1: M ← ∅
2: while E ≠ ∅ do
3:     wähle eine beliebige Kante e ∈ E
4:     M ← M ∪ {e}
5:     lösche e und alle inzidenten Kanten in G
```

## Augmentierende Pfade

> [!Note] 
> Ein M-augmentierender Pfad P ist ein Pfad, der 
> - abwechselnd Kanten aus M und nicht aus M hat 
> - in von M ==nicht überdeckten Knoten beginnt und endet==
> - daher ungerade Länge hat

Können Matching M vergrössern mit XOR zu M-augmentierendem Pfad: $M' = M \oplus P$, gewinnen Länge +1. 

---
## Satz von Berge

Jedes nicht kardinalitätsmaximale Matching hat einen augmentierenden Pfad. 

![[Bildschirmfoto 2026-03-08 um 01.07.14.png]]
![[Bildschirmfoto 2026-03-08 um 01.07.31.png]]

![[04 Slides.pdf#page=31]]

![[04 Slides.pdf#page=32]]


## Satz von Hall

Ein ==bipartiter== Graph $G=(A \uplus B,E)$ hat ein Matching $M$ der Grösse $|M|=|A| \iff |X| \le |N(X)|$ für alle Teilmengen $X \subseteq A$. 

$N(X)$ sind die Nachbarknoten von X. 

> Jede Gruppe von Knoten aus $A$ muss insgesamt mindestens genauso viele Nachbarknoten in der Menge $B$ haben, wie die Gruppe selbst groß ist. 
> 
> Nur wenn diese Bedingung für jede Teilmenge gilt, ist garantiert, dass jeder Knoten aus $A$ einen eigenen, exklusiven Partner in $B$ finden kann (ein vollständiges Matching für $A$).


![[04 Slides.pdf#page=36]]
![[04 Slides.pdf#page=37]]

---

05 Lecture
