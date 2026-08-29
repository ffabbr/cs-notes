
## Matchings auf bipartiten Graphen

kardinalitätsmaximales (maximum) Matching auf bipartiten Graphen durch Reduktion auf Maxflow in $O(nm)$

Transformiere Graphen in Netzwerk, indem 
- Kanten gerichtet, gleiche Richtung und Kapazität 1
- füge s und t hinzu

![[Bildschirmfoto 2026-05-21 um 15.07.22.png]]

Kap der Kanten von s zu den Knoten aus U ist 1, da Flusserhaltung und Flusswerte ganzzahlig kann nur eine Kante weiterfliessen.

---

## Kantendisjunkte Wege

Gegeben Graph, erstelle Natzwerk mit jeweils 2 Kanten in beide Richtungen

![[Bildschirmfoto 2026-05-21 um 15.16.40.png]]

Fluss 1 oder 0, die mit 1 sind ein Subgraphen. Es gilt, jeder Knoten hat gleich viele ausgehende wie eingehende Kanten (→ [[23 Flows|Flusserhaltung]]). Finde Pfade von u nach v (greedy) und markiere gebrauchte Kanten als gebraucht (nicht mehr nutzen). Das funktioniert da Flusserhaltung. Wiederhole $val(f)$ mal ($val(f)$ kantendisjunkte Pfade)

Aus dem Maxflow-Mincut Theorem folgt Satz von Menger

![[Bildschirmfoto 2026-05-21 um 15.22.00.png]]

---

## Bildmodellierung

![[Bildschirmfoto 2026-05-21 um 15.23.45.png]]