
## Definitionen

- **Liniensegment**: alle Punkte die auf der Strecke zwischen 2 Punkten liegen. $\overline{v_0 v_1} := \{(1-\lambda) \cdot v_0 + \lambda \cdot v_1 \mid 0 \le \lambda \le 1\}$ 
- **konvexe Menge**: für beliebige 2 Punkte in der Menge ist die Verbindungslinie auch in der Menge
  ![[Bildschirmfoto 2026-05-29 um 12.25.37.png]]


- **konvexe Hülle**: $\text{conv(P)}$: „kleinstmögliche“ konvexe Menge, die alle Punkte umfasst; Schnittmenge aller konvexen Mengen, die $P$ enthalten
- die konvexe Hülle kann durch ein Polygon mit h Ecken aus P beschrieben werden (Reihenfolge der Ecken gegen den Uhrzeigersinn listen)
- **Randkante**: alle anderen Punkte sind ==links== von der Geraden

> [!Note] Allgemeine Lage
> Wenn "allgemeine Lage", so machen wir die folgenden Annahmen: 
> - keine 3 Punkte auf einer Geraden
> - keine 2 Punkte haben dieselbe x-Koordinate (keine senkrechte Linien)


**Lemma:** 
Eckenfolge des Polygons $\text{conv(P)} \iff$ alle Paare der Punkte der Eckenfolge sind Randkanten

**Prüfen, ob ein Punkt links von einer Geraden  liegt**:
$O(1)$ 
$p$ liegt links von der Gerade $q,r \iff \det \begin{bmatrix} q_x - p_x & r_x - p_x \\ q_y - p_y & r_y - p_y \end{bmatrix} > 0$


## FindNext Subroutine

$O(n)$
gegeben q (Hülleneckpunkt), finde nächsten Hülleneckpunkt rechts davon 

1. setze $q_{\text{next}}$ auf einen beliebigen Punkt
2. iteriere über alle Punkte p: wenn Punkt rechts von Gerade $q, q_{\text{next}}$, dann setze $q_{\text{next}}$ auf p

Das "ist rechts von" wird mit der Determinante in $O(1)$ überprüft. 
Imaging Laserpointer der von links nach rechts immer weiter "beamt"

## JarvisWrap

$O(n\cdot h)$

1. Startpunkt $p_{\text{now}}$: Punkt mit kleinster x Koordinate
2. wiederhole bis $p_{\text{now}}=q_{0}$ 
	1. setze $q_{h}$ auf $p_{\text{now}}$ 
	2. rufe `FindNext(q_h)` auf, um den nächsten Punkt am Außenrand zu finden und setze $p_{\text{now}}$ auf diesen Punkt
	3. $h+1$
3. return folge von q

Es gilt: 
- $h \leq n$
- wenn punkte gleichverteilt: $\mathbb{E}[h] \le O(\log n)$  

## Local Repair

$O(n \log n)$

1. sortiere Punkte nach x-Achse ($\mathcal{O}(n \log n)$), erster und letzter Punkt sind garantiert Eckpunkte
2. Statt Kreis zu suchen, suchen wir 
	1. **unteren** Teilpolygonzug: x-monoton wachsend, keine Punkte darunter
	2. **oberen** Teilpolygonzug: x-monoton fallend und keine Punkte darüber
3. Verbessern (Backtracking): 
	1. analysiere immer die letzten 3 Knoten, wenn wir je eine Rechtskurve machen (aka wenn wir Knoten 1 und 3 verbinden ist Knoten 2 links von der Verbindung, also det > 0), haben wir einen indent 
	2. wenn indent, entferne Knoten vom Indent

**Laufzeit**
- $O(n)$ bei sortierter Eingabe