
## Definition 

- **Selection Sort**, aber mit effizienter Suche nach dem größten Element durch Nutzung eines **Max-Heaps** (Binärbaum, und alle Childs sind kleiner als das Parent)

- Heap: von oben nach unten und links nach rechts gelesen sind die Elemente wie im Array. Alle child Elemente sind kleiner als das Parent Element. Somit findet man die Child-Elemente von $k$ bei $2k$ und $2k+1$. 

- **Laufzeit:** $O(n \log n)$

## Ablauf:

1. Wandle das Array in einen **Heap** um (Heapify)
2. Wiederhole:
	- Entferne das Maximum (Wurzel) 
	- Platziere es am Ende des Arrays
	- Stelle die Heap-Bedingung wieder her (versickere)
		- Tausche parent mit größerem child solange, bis Heap Bedingung gilt.

## Funktionen

- ExtractMax(H)
	- Entferne Maximum
	- letztes Element an die Spitze (klein)
	- Spitze versickern (größeres Child immer mit Parent tauschen)

- Insert(H, p)
	- Element an die nächste freie Position stellen
	- RestoreHeapCondition
		- Wenn Parent kleiner als das Element selbst, tausche

## Sonstiges

Funktion Heapify zum erstellen eines Heaps,  läuft in $O(n)$. Siehe [[2_Suchen und Sortieren.pdf]] im Skript.