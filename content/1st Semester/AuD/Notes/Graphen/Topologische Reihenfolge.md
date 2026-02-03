
→ [[Gerichtete Graphen und Darstellung]]
→ [[03 DFS]]

## Definition

Reihenfolge, die alle Abhängigkeiten erfüllt. z.B. richtige Reihenfolge beim Anziehen. Ordnet man Knoten nach dieser Reihenfolge an, so zeigen alle Kanten von links nach rechts. 

Wenn eine Kante von Knoten u zu Knoten v zeigt, muss u vor v stehen.

Topologische Reihenfolge ist *nicht* immer möglich, Gegenbeispiel gerichteter Zyklus. Hier hat jeder Knoten einen Nachfolger, kann nicht enden.

$\exists \text{ topologische Reihenfolge} \Longleftrightarrow \nexists \text{ gerichteter Zyklus}$

## Topologisch Sortieren

- finde Senke v durch den [[#Path-Algorithmus]]
- setze v an letzte Stelle
- entferne v und löse Rest rekursiv (finde neue Senke nachdem v entfernt wurde, etc.)

### Path-Algorithmus, Version 1
[Vorlesung](https://video.ethz.ch/lectures/d-infk/2025/autumn/252-0026-00L/v/HXRD6Vq9eof?t=53m22s)

```java
  Path(u):
	  markiere Knoten u
	  if ∃ Nachfolger v, unmarkiert
		  Path(v)
```

- Path(u) markiert Pfad P mit Start u
- Endknoten v von P hat alle Nachfolger markiert, v ist Senke, wenn $\nexists$ gerichteter Zyklus
- Von unten nach oben ablesen (immer die gefundene Senken werden ja ganz hinten hingestellt)

==Ineffizient==, da "wiederholtes Laufen", besser: Pfad wiederverwenden so weit wie möglich. 

### Version 2, [[DFS]]