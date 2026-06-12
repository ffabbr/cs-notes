
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

Statt Kreis zu suchen, suchen wir **unteren** Teilpolygonzug: x-monoton wachsend, keine Punkte darunter, und **oberen** Teilpolygonzug: x-monoton fallend und keine Punkte darüber

1. sortiere Punkte nach x-Achse ($\mathcal{O}(n \log n)$), erster und letzter Punkt sind garantiert Eckpunkte
2. Iteriere über alle Knoten, zuerst von links nach rechts (unten), dann von rechts nach links (oben) und verbessere mit Backtracking:
	1. Suppose Knoten 1,2,3,4,5 sind in der Reihenfolge bzgl. x-Achse. Unser Teilpolygonzug unten ist bisher 1,2,3,4. Wir wollen 5 hinzufügen. Ziehe Verbindungslinie von Knoten 3 zu 5. 
	2. Liegt 4 jetzt links von dieser Linie, hätten wir eine Rechtskurve (aka indent), wenn wir 3 im unteren Polygonzug haben. Wir wollen keinen indent, also skippe Knoten 4, und Backtracking:
		1. wenn wir Knoten 2 und 5 Verbinden, liegt Knoten 3 links oder rechts von der Verbindungslinie → repeat solange bis nicht mehr links

**Runtime**
- $O(n \log n)$
- $O(n)$ wenn sortiert, da wir $2(n-1)-h \leq O(n)$ lokale Verbesserungen machen (Anzahl Ecken am Anfang – Anzahl Ecken am Ende). Pro Punkt 2 erfolgreiche Tests (für oben und unten), daher auch $\leq O(n)$.

![[Bildschirmfoto 2026-05-30 um 12.02.28.png]]


## Sortieren mit Convex Hull

Ecken von $\text{conv(P)}=$ Sortierung des Arrays

Wir wollen ein Array sortieren: 

Pro Wert $a_{i}$, erstelle Punkt $(a_{i}, a_{i}^2)$. 
$\implies$ die Punkte liegen automatisch auf einer Parabel
$\implies$ Parabel ist konvex
$\implies$ jeder Punkt ist Teil der konvexen Hülle
$\implies$ der $\text{conv(P)}$ Algorithmus listet gegen den Uhrzeigersinn, also genau sortiert

Runtime: $O(n)$
- Punkte erstellen $O(n)$
- Convex Hull $O(n)$
- Ablesen $O(n)$