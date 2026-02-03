- Wiederhole rekursiv:
	- Wähle ein **Pivotelement p** (z.B. das letzte Element des Arrays).
	- Alle Elemente kleiner als p nach links, alle größer als p nach rechts (links und rechts ist nicht sortiert) 
		- Ein Zeiger sucht von links ausgehend die erstelle Stelle die größer als das Pivot ist, ein anderer Zeiger sucht von rechts ausgehend ein Element kleiner als das Pivot, die beiden werden getauscht. Und so weiter... 
		- Wenn sich die beiden Zeiger kreuzen, dann finito und die Stelle wird mit dem Pivot getauscht

- Läuft **in-place** 

- **Invariante:** Nach jeder Aufteilung gilt: Alle Elemente links vom Pivot sind kleiner oder gleich, alle rechts größer.

- Problem entsteht, wenn das Pivotelement z.B. den größten oder kleinsten Wert der Liste hat (z.B. Array schon sortiert) → worst case

- **Laufzeit:**
	- Best Case: $O(n \log n)$ 
	- Worst Case: $O(n^2)$ 