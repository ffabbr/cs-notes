(Suchen und Sortieren)
### Suchalgorithmen

- **Linear Search** (jedes Element einmal anschauen)  
  - Laufzeit: $\Theta(n)$

- **Binary Search** (wenn sortiert)  
	- Rekursiv, Liste halbieren, schauen, ob die Mitte das gesuchte Element ist. Wenn nein, dann schauen ob die Mitte größer oder kleiner als das gesuchte Element ist und dementsprechend alles von vorne mit nur der linken/rechten Seite.
	- $T(n) = T\left(\frac{n}{2}\right) + c$  
	- Laufzeit $\Theta(\log n)$


> Jedes vergleichsbasierte Suchen braucht im schlechtesten Fall $\Omega(\log(n))$ Vergleiche. [[Beweis, vergleichsbasiertes Suchen in log(n)]]
> 
> Für vergleichsbasiertes Sortieren ist es $n \log(n)$.

##### Warum folgt aus $T\left( \frac{n}{2} \right)$ eine Laufzeit von $\log(n)$?

$T(n)=T\left( \frac{n}{2} \right)+c$
	$=(T\left( \frac{n}{4} \right)+c)+c$           | Konstanten irrelevant
	$=T\left( \frac{n}{8} \right)$
	...
	$=(T\left( \frac{n}{2^k} \right)+c)+c$

$\frac{n}{2^k}=1 \implies 2^k=n \implies k=\log_{2}(n)$


##### Entscheidungsbaum (Binärbaum)

- Jeder Knoten ist ein Vergleich
- jeder Knoten hat höchstens zwei Kinder, ja oder nein
- Ganz oben "Wurzel"
- Unteste Ebene: "Blätter" sind Rückgabewerte
- Gesamtzahl der Blätter mindestens $n+1$ (jeder Outcome + nicht gefunden)
- Anzahl der Vergleiche im schlechtesten Fall ist die Höhe des Baumes
- Entscheidungsbaum mit Tiefe h, hat eine Anzahl von Blättern > n!, die maximale Anzahl an Blättern ist $2^h$. Also gilt $2^h \geq n! \implies n \geq \log_{2}(n!) \geq \Omega(n \log(n))$. Tiefe des Binärbaumes ist log die Anzahl der Knoten.

---

### Sortieralgorithmen, Einführung

- **Bubble Sort**  
	- Wenn das Element größer als das darauffolgende ist, werden die beiden getauscht. 
	- Nach einer Iteration ist also das größte Element ganz hinten. 
	- Laufzeit $\Theta(n^2)$ 

- **Selection Sort**  
	- größtes Element ans Ende, indem mit Element an richtiger Stelle getauscht (oder kleinstes Element an den Anfang)
	- Vertauschungen $\Theta(n)$, aber Vergleiche $\Theta(n^2)$
	- Also Laufzeit $\Theta(n^2)$

- **Insertion Sort**
	- jedes neue Element von rechts an die richtige Stelle im sortierten Array ganz links einfügen 
	- **Invariante**: $I(j)$: nach $j$ Iterationen ist das Teilarray $A[1...j]$ (also die ersten $j$ Elemente) sortiert. Das heißt nicht, dass sie an der richtigen Stelle sind (aber sie sind halt sortiert).
	- **Vergleiche**: Wir nehmen ein neues Element und suchen die richtige Stelle im sortierten Teilarray, um es einzusetzen. Da Binary Search in $O(\log(n))$ läuft, und wir hier alle Elemente außer das erste einmal einsortieren müssen, haben wir $\sum_{j=2}^{n} \log(n)=n\log(n)$. 
	- **Vertauschungen**: Sagen wir, das Array ist verkehrt sortiert, z.B. $\boxed{54321}$, dann wird im ersten Schritt 4 in das sortierte Teilarray hinzugefügt, und 5 muss 1 nach rechts verschoben werden. Dann kommt 3, und 4 und 5 müssen jew. 1 nach rechts verschoben werden, etc. Am Ende haben wir also $\frac{n(n-1)}{2}$ Vertauschungen. Also:
	- Vergleiche $\Theta(n \cdot log(n))$, aber immer noch $\Theta(n^2)$ Vertauschungen
	- Also Laufzeit $\Theta(n^2)$

- **Merge Sort**  
	- teile immer wieder in Hälften, sortiere rekursiv und kombiniere (divide and conquer)
	- Achtung, extra Space (Hilfsarray)
	- Rekursives Mergesort ist $T\left( \frac{n}{2} \right)$, das wird zwei mal ausgeführt (da links und rechts), also $2 \cdot T\left( \frac{n}{2} \right)$, und Merge ist in $O(n)$. Mit dem [[Master Theorem]] kommen wir zur Laufzeit.
	- $\Theta(n \log n)$

- **Quicksort**
	- siehe [[02 Quicksort]]

- **Heap Sort**
	- siehe [[03 Heapsort]]

- **Bucket Sort**
	- Bedingung: wir müssen die Anzahl der Buckets wissen 
	- schreibe die Buckets sortiert auf
	- notiere in jedem Bucket wie oft das Element im Array vorkommt
	- gehe von links nach rechts alle Buckets durch
	- $O(n)$ 


### Übersicht

| Algorithmus    | Vergleiche                                 | Bewegungen    | Extr. Platz | Lokalität |
| -------------- | ------------------------------------------ | ------------- | ----------- | --------- |
| Bubble-Sort    | $O(n^2)$                                   | $O(n^2)$      | $O(1)$      | gut       |
| Selection-Sort | $O(n^2)$                                   | $O(n)$        | $O(1)$      | gut       |
| Insertion-Sort | $O(n \log n)$                              | $O(n^2)$      | $O(1)$      | gut       |
| Mergesort      | $O(n \log n)$                              | $O(n \log n)$ | $O(n)$      | gut       |
| Quicksort      | $O(n \log n)$ (best/avg), $O(n^2)$ (worst) | $O(n \log n)$ | $O(1)$      | gut       |
| Heap-Sort      | $O(n \log n)$                              | $O(n \log n)$ | $O(1)$      | schlecht  |

==Achtung==, bspw. die Laufzeit von Mergesort ist ja auch in $O(n^2)$

## Was ist die [[Invariante]]?

→ [[Invariante]]


