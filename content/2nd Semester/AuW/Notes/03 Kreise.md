
## Recap 

| Begriff              | Bedeutung                                                                                                                          |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Weg (walk)**       | **Folge benachbarter Knoten**                                                                                                      |
| Eulerweg             | jede Kante genau einmal                                                                                                            |
| **Pfad (path)**      | **Weg ohne wiederholte Knoten**                                                                                                    |
| Hamiltonpfad         | jeder Knoten genau einmal                                                                                                          |
| Zyklus (closed walk) | **Weg mit Start = Ende**, mindestens 2 Knoten (hin-zurück-hin), Endknoten inzident zu (verbunden mit) geraden Anzahl Kanten im Weg |
| ==Eulertour==        | Closed Walk, jede Kante genau einmal                                                                                               |
| Kreis                | Anfang = Ende, aber kein Knoten wird 2 mal besucht, also mindestens 3 Knoten                                                       |
| ==Hamiltonkreis==    | Kreis über alle Knoten                                                                                                             |


> $\sum_{v∈V}\text{deg}(v)=2|E|$ (**Handschlagslemma**) 

> ein Graph hat maximal $\frac{|V|\cdot(|V|-1)}{2}$ Kanten 

## Eulertouren 

> Geschlossener Weg (Zyklus), jede Kante genau einmal

- Eulertour existiert $\Longleftrightarrow$ alle Knotengrade gerade, Graph connected
- Weg ist Zyklus $\Longleftrightarrow$ der Endknoten vom Eulerweg ist inzident zu einer geraden Anzahl von Kanten

**Eulertouren finden**

$O(|E|)$ 

1. Ein random Kreis finden 
2. Repeat: Einen Knoten, wo es noch nicht markierte Kanten hat, von dort aus neuen Kreis finden und in die bisherige Lösung einfügen

## Hamiltonkreise

> Kreis mit allen Knoten genau einmal

- Ist ein [[04 NP, TSP|P/NP Problem]] 
- Anzahl Hamiltonkreise: $\frac{1}{2} (n-1)!$ 
- Ein $n \times m$ Gitter hat einen Hamiltonkreis $\iff$ $n\cdot m$ gerade 
- Bipartiter Graph $A \cup B$, mit $|A| \neq |B|$, hat ==keinen== Hamiltonkreis

- Können Existenz in $O(|V| \cdot 2^{|V|})$ finden 


---

## Siebformel

Für endliche Mengen, Grösse trotz Überschneidung berechnen

Nür n=2: 
$|A_{1} \cup A_{2}| = |A_{1}| + |A_{2}| - |A_{1} \cap A_{2}|$


---

## Dirak (Dirac)

Jeder Graph mit 
- $|V| \geq 3$ und 
- $\delta(G)$ Minimalgrad $\geq \frac{|V|}{2}$

hat einen Hamiltonkreis. 

### Beweis von Dirak, Hamiltonkreis existiert

Sei der Minimalgrad $\frac{n}{2}$, $n=|V|$. 

#### Schritt 1: Der Graph ist zusammenhängend

Minimalgrad $\frac{n}{2}$, also hat jeder Knoten mindestens $\frac{n}{2}$ Nachbarn. Der Graph ist zusammenhängend. Nehme zwei beliebige Knoten u und v. 

- Wenn direkt verbunden, trivial. 
- Wenn u und v nicht direkt verbunden: 
  Jeder Knoten hat mindestens $\frac{n}{2}$ Nachbarn, plus dem Knoten selbst macht $1+\frac{n}{2}$ Knoten. Das gilt für beide Knoten u und v, also gesamt $2+n$ Knoten, aber es gibt nur n. Somit Überschnitt der Nachbarknoten. **Alternativ**: Siebformel nach $|N(u) \cap N(v)|$ umstellen

![[Bildschirmfoto 2026-02-25 um 17.13.02.png]]
![[Bildschirmfoto 2026-03-05 um 12.05.45.png]]

#### Schritt 2: Hamiltonkreis (Induktion)

$k < n$
##### aus k-Kreis folgt k+1 Pfad

Hat es einen k-Kreis, so nimm einen Knoten der irgendwo absteht und sehe $k+1$ Pfad als der Kreis und die Kante mit dem abstehenden Knoten. Es gibt Knoten die nicht im Kreis sind, da $k< n$, und zusammenhängend. 

##### aus k-Pfad folgt: k+1 Pfad ∨ k-Kreis

**Fall 1:** 
Gibt es einen k-Pfad und ein Endknoten von diesem Pfad hat eine andere anliegende Kante. Füge die zu dem Pfad hinzu. 

**Fall 2:** 
alle Nachbarn von den Endknoten liegen auf dem Pfad
Wir brauchen ein $v_{j}$ ist Nachbar von $v_{1}$ und $v_{j-1}$ ist Nachbar von $v_{k}$.

Wir zeigen, dass das existiert, durch Überschnitt von Mengen. Sei $v_{j} \in N(v_{1})$, und def. $N^{+}(v_{j})=\{v_{i+1} : v_{i} \in N(v_{j})\}$. Jeweils $\frac{n}{2}$

$|N(v_{1}) \cap N^+(v_{j})| \geq 1$ (überschneiden sich)

![[Bildschirmfoto 2026-02-25 um 17.29.35.png]]

---

Dirak Beweis alternativ, Josia

![[Bildschirmfoto 2026-03-05 um 00.27.00.png]]
![[Bildschirmfoto 2026-03-05 um 00.28.34.png]]
![[Bildschirmfoto 2026-03-05 um 00.28.47.png]]
![[Bildschirmfoto 2026-03-05 um 00.27.33.png]]