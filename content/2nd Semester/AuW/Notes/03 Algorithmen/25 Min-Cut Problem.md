
- kann mehrere Kanten zwischen 2 Knoten geben, aber keine Schleifen
- Kantenschnitt: Graph nicht mehr zusammenhängend, wenn ich C (Kantenset) wegnehme
- Achtung, Min-Cut nicht mit ST Schnitt verwechseln
- $\mu(G)$ = Grösse des kleinstmöglichen Schnitts. 
- gibt immer $\mu(G) \leq$ min deg (v)

## Min-Cut mit Flüssen 

- Gegeben Graph, finde Min-Cut. Haben Kante in beide Richtungen für jede Kante. kapazität ist die anzahl der kanten zwischen a und b in G
- maxflow algorithmus für alle targets (knoten) durchführen, (minimaler anzahl kanten um t von s zu trennen 
- minimum dieser ausgeben


### Kontraktion einer Kante

- Knoten mergen zu einem Knoten
- Kanten dazwischen fallen weg, alle anderen fehen mit
- minimale Kantenschnitt wird grösser gleich
- G' <- G'/e

### Monte Carlo Algorithmus

Kontrahieren $O(n)$, 
Iterationen $O(n)$

- Handschlaglemma
- Gegenwahrscheinlichkeit

## Bootstrapping


Fehleranfälliger gegen Ende. Statt Monte-Carlo gesamt zu wiederholen, wiederholen, führen wir einmal bis t aus und ab t öfters, können auch öfters bootstrappen, etc.

Theorie lernen





