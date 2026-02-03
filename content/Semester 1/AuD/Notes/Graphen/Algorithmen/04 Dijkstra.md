## Einleitung

- kürzesten Weg finden 
- wie BFS, aber jede Kante hat ein Gewicht
- minimale Distanz ist die mit der geringsten Summer der Gewichte
- Hier: **keine Gewichte negativ**, siehe → [[05 Bellman-Ford]]

## Step by step

1. Obere Schranken für Distanzen zu Startknoten festlegen: Startknoten 0, Rest unendlich 
2. Starte bei dem Startknoten und verbessere die anliegenden Knoten 
3. Wenn obere Schranke vom vorherigen Knoten + Wert der Kante < Knotenwert (zu Beginn $\infty$), dann ersetze obere Schranke mit neuen oberen Schranke. 
4. **==Nach den anliegenden Knoten, mache weiter mit dem Knoten mit der tiefsten Schranke==**
5. Minimale Distanz zu einem Knoten gefunden wenn alle eingehenden Kanten abgedeckt 

Hmm...
- Wenn Weg einen Knoten deckt dann ist obere Schranke fixiert
- "jedes mal vom Minimum ausgehen"
- Kind-of Invariante: PQ.extractMin → v

## Pseudocode

- **PriorityQueue** hat Toupel, für jeden Knoten ist aktuelle Distanz gespeichert (s,0), Rest $\infty$ (Achtung in Java, ```Integer.MAX_VALUE+1``` gibt overflow error, also ```Integer.MAX_VALUE/2``` nutzen)
- PQ.poll() ist PQ.extractMin
- Laufzeit: $O((|V|+|E|)\cdot \log(n))$ 

## Datenstruktur

Priority Queue, wie Min-Heap (vgl. Max-Heap aber umgekehrt)

### Operationen

- Insert
- ExtractMin / Poll
- DecreaseKey
- **Laufzeit der Operationen**: $O(\log n)$ 



![[Semester 1/Media/Übung 10.pdf]]