
## Matchings auf bipartiten Graphen

kardinalitätsmaximales (maximum) Matching auf bipartiten Graphen durch reduktion auf Maxflow in $O(nm)$

Transformiere Graphen in Netzwerk, indem 
- Kanten gerichtet, gleiche Richtung und Kapazität 1
- füge s und t hinzu

![[Bildschirmfoto 2026-05-21 um 15.07.22.png]]

Knoten bekommt 1 Fluss, also kann nicht zu 2 Knoten nach unten verbunden werden, das wäre Fluss out 2 und dadurch nicht Flusserhaltung

---

## Kantendisjunkte Wege

Gegeben Graph, erstelle Natzwerk mit jeweils 2 Kanten in beide Richtungen

![[Bildschirmfoto 2026-05-21 um 15.16.40.png]]

Fluss 1 oder 0, die mit 1 sind ein Subgraphen. Es gilt, jeder Knoten hat gleich viele ausgehende wie eingehende Kanten (→ Flusserhaltung). Finde Pfade von u nach v (greedy) und markiere gebrauchte Kanten aus gebraucht (nicht mehr nutzen). Das funktioniert da Flusserhaltung. Wiederhole $val(f)$ mal ($val(f)$ kantendisjunkte Pfade)

Aus dem Maxflow-Mincut Theorem folgt Satz von Menger

![[Bildschirmfoto 2026-05-21 um 15.22.00.png]]

---

## Bildmodellierung

![[Bildschirmfoto 2026-05-21 um 15.23.45.png]]