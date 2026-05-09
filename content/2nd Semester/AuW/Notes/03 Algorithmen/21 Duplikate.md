
## Duplikate finden mit direktem Sortieren

1. Sortieren 
2. Durchlaufen, gleiche Werte sind nebeneinander

$O(n \log n + |\text{Duplikate}|)$

Maximale Anzahl Duplikate bei n Elementen: $\sum_{i=1}^{n-1} i = \frac{n(n-1)}{2}$ 
## Duplikate finden mit Hashfunktion

- sortieren und vergleichen kann teuer sein bei grossen Elementen
- Lösung: nutze Hashfunktion um grosses Element klein darzustellen

- gleiche daten haben gleichen Hash
- selten kann passieren dass verschiedene Daten gleichen Hash haben (**Kollision**)

**Vorgehen** 

1. Berechne Hash
2. Sortiere anhand von Hash
3. finde Duplikate im Hash
4. überprüfe Original-Elemente bei gleichem Hash

$O(n \log n + |\text{Duplikate}| + |\text{Kollisionen}|)$

Damit schnell, dürfen nicht zu viele Kollisionen auftreten. Bei grosser Anzahl möglicher Hashwerte $m = n^2$, ist die **erwartete Anzahl an Kollisionen konstant**.

Notizen zum Beweis: 

- $K_{i,j}$ ist Indikatorvariable, 1 wenn $(i, j)$ eine Kollision ist. Das passiert mit Wahrscheinlichkeit $\frac{1}{m}$, da eine Hashfunktion zufällig auf m Plätze verteilt. Somit ist $\mathbb{E}[K_{i,j}]\leq \frac{1}{m}$ 
- Linearität des Erwartungswertes: $\mathbb{E}[\text{Anzahl Kollisionen}] = \sum_{1 \leq i < j \leq n} \mathbb{E}[K_{i,j}]$ 
- Umformungen
- $< \frac{1}{2}$

![[Bildschirmfoto 2026-05-04 um 14.03.12.png]]


## Duplikate finden mit Hase-Igel-Algorithmus (Floyd)

Gegeben: Array Grösse n mit Elementen zwischen 1 und n-1. Es gibt immer ein Duplikat per Pigeonhole Principle.

Gerichteter Graph: 

Vertices sind die indizes des Arrays, und directed Edge zu dem Vertex dessen Wert wir an der Stelle haben, also von `i` zu `a[i]`; der Index ist der aktuelle Knoten, der Wert an diesem Index ist der Folgeknoten.

![[Bildschirmfoto 2026-05-04 um 14.18.00.png|461]]

Der Graph besteht aus 
1. einem "Weg zum Kreis"
2. einem Kreis. Der Graphhat einen Kreis, da 
	1. keine Sachgassen, jede Node hat einen ausgehenden Pfeil
	2. mindestens ein Wert kommt doppelt vor (siehe oben, Pigeonhole), also zeigen 2 Edges auf den selben Node => Kreis

Igel und Hase laufen

**Treffen 1**: 

- Igel: macht 1 Schritt `igel = a[igel]`
- Hase: macht 2 Schritte `hase = a[a[hase]]`

- Hase und Igel laufen bei Knoten n los, Hase ist schneller, läuft aber dann im Kreis bis Treffen mit Igel. 
- Treffen nach spätestens n Schritten. Why? Graph hat insgesamt n Knoten, also ist Weg zum Kreis $\leq n$, und sobald im Kreis ist "Aufholjagd"
- Da der Graph einen Kreis enthält, läuft der schnelle Hase irgendwann von hinten auf den Igel auf. 

Beweis: 
- [[Bildschirmfoto 2026-05-04 um 15.04.00.png|Gesamt]]
- Igel macht x Schritte, Hase 2x. Da TP ist Differenz 2x - x = x Schritte Vielfaches der Kreislänge. 

**Treffen 2**: 
1. Igel bleibt stehen, wo 1. Treffen
2. Hase zurück zu Startknoten n
3. beide Laufen 1 Schritt speed
4. Knoten vom Treffpunkt ist Beginn des Kreises

Beweis: 
- [[Bildschirmfoto 2026-05-04 um 15.04.13.png|Gesamt]]
- Distanz Igel: $x=k+m$, k=Weg zum Kreis, m=im Kreis. 
- da x Vielfaches der Kreislänge: $k + m = c \cdot l$, c=Anzahl Runden
- Igel hat schon m im Kreis gemacht, jetzt noch k Schritte weiter, dann m+k. Da m+k vielfaches der Kreislänge, ist Igel am Start. 
- Hase macht k Schritte bis zum Kreis

![[Bildschirmfoto 2026-05-04 um 15.03.19.png|345]]

$O(n)$


