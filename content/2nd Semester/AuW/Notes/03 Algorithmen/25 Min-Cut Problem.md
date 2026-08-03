
## Begriffe

- Multigraph: kann mehrere Kanten zwischen 2 Knoten geben, aber keine Schleifen
- Grad: Anzahl anliegender **Kanten**, nicht Knoten
- Schnitt: Teilmenge der Kanten, Graph nicht mehr zusammenhängend, wenn ich diese Kanten entferne

$\mu(G)$ = minimaler Kantenschnitt:
**wie viele Kanten muss ich entfernen, damit nicht zusammenhängend**

Immer (logisch):
$$
\mu(G) \leq \text{kleinster Grad aller Knoten}
$$

## Min-Cut mit Flüssen 

1. Gegeben Graph, konstruiere Netzwerk:
	1. Wähle fixen (random) Knoten für s
	2. immer nur eine Kante (Arc) in jede Richtung mit gleicher $c(u,v)$: Anzahl der Kanten zwischen u und v im "alten Graphen"
2. Iteriere über alle möglichen targets (alle Knoten außer s), berechne $\text{max flow} = \text{min cap(S,T)}$ mit Fulkerson 
3. Output: min cap die gefunden wurde

![[Bildschirmfoto 2026-05-28 um 20.07.52.png]]

## Kontraktion einer Kante

Knoten mergen zu einem Knoten, Kanten dazwischen fallen weg, alle anderen fahren mit

![[Bildschirmfoto 2026-05-28 um 20.09.03.png|445]]

**Der minimale Kantenschnitt wird größer gleich** (Beweis: sei C ein minimaler Schnitt nach der Kontraktion, dann gibt es einen Schnitt im originalen Graphen mit den selben Kanten)
$$
\mu(G/e) \geq \mu(G)
$$

Falls der minimale Kantenschnitt eine Kante nicht enthält, so **ändert das Kontrahieren dieser Kante nicht den minimalen Kantenschnitt**

## Min-Cut Monte-Carlo Algorithmus 

1. Kopiere Graph
2. While (∃ mehr als 2 Knoten) 
	1. wähle random Kante
	2. Kontrahiere diese Kante
3. return Grösse des eindeutigen Schnitts 

![[Bildschirmfoto 2026-05-28 um 20.20.00.png]]

A single iteration is $O(n^2)$, but only correct with probability of $\geq \frac{2}{n\cdot(n-1)}$. 

Total runtime without Bootstrapping is $O(n^2\cdot \lambda n^2)$ 

## Bootstrapping

Der Algorithmus wählt ja Kanten at random. Wenn er eine Kante kontrahiert, die aber eigentlich Teil des min cuts ist, haben wir ein Problem.

Umdo kleiner der Graph, desto wahrscheinlicher macht der Algorithmus einen Fehler. Statt Monte-Carlo gesamt zu wiederholen, wiederholen wir umso öfter, desto "weiter hinten" wir im Algorithmus sind. 


![[Bildschirmfoto 2026-05-28 um 20.36.15.png]]
Runtime with bootstrapping: 

$$
O(n^2\cdot \log n)
$$

![[Bildschirmfoto 2026-05-28 um 20.41.15.png]]
