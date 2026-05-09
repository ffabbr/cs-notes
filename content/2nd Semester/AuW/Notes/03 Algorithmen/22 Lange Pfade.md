
Achtung: ein Pfad Länge `n` hat `n+1` Knoten

Gibt es einen Pfad der Länge B (B Kanten, B+1 verschiedene Knoten) in dem Graphen? 

## NP-Vollständigkeit

Das Problem ist NP-Vollständig: G hat Hamiltonkreis $\iff$ G' hat Pfad Länge n.
**Hamiltonkreis**: jeder Knoten des Graphen genau einmal, Anfang = Ende

![[Bildschirmfoto 2026-05-07 um 20.29.05.png]]![[Bildschirmfoto 2026-05-07 um 20.29.23.png]]

## Long Path Algorithmus
### Schritt 1: Color Coding

- ==**färbe zufällig**==
- finde bunte Pfade (alle Knoten unterschiedliche Farbe)
- Farbfunktion: $\gamma(v)$

### Schritt 2: Wahrscheinlichkeiten bunt

$\exists$ Pfad mit Länge $k-1 \implies \Pr(\exists \text{ bunten Pfad mit Länge } k-1)\geq e^{-k}$

Beweis: 

![[Bildschirmfoto 2026-05-07 um 20.30.40.png]]

### Schritt 3: DP Algorithmus Bunter Pfad (Monte Carlo)

$P_{i}(v)$ ist die Menge der (der Menge der Farben der) bunten Pfade von Länge i, die bei Knoten v enden.

**Base Case:** 
- $P_{0}(v)={{\gamma(v)}}$ für alle Knoten v
  (Länge 0, also nur die Farbe des Endknotens)

**Rekursion**
- wir verlängern jeden Pfad den wir noch haben, indem wir einen vorherrigen (um 1 kürzeren Pfad) nehmen und schauen, ob der Pfad immer noch bunt bleibt, wenn wir ihn verlängern

![[Bildschirmfoto 2026-05-07 um 20.31.21.png]]

Der Algorithmus ist erfolgreich fertig, wenn am Ende beim Prüfen der Länge $k-1$ bei _irgendeinem_ Knoten $v$, $P_{k-1}(v)$ nicht leer ist. Das bedeutet, dass ein bunter Pfad der gewünschten Länge existiert.

→ [[Bildschirmfoto 2026-05-07 um 20.31.33.png|LAUFZEIT]]

### Schritt 4: Fehlerreduktion

Bisher haben wir einen Monte-Carlo Algorithmus mit einsieitgem Fehler. Remember, wir haben in [[#Schritt 1 Color Coding]] die Färbung zufällig gemacht.

- Immer korrekt für NEIN-Instanzen (wenn es keinen Pfad Länge $k-1$ gibt, finden wir auch keinen)
- Wahrscheinlichkeit $\geq e^{-k}$ korrekt für JA (oft wird der Pfad nicht gefunden, da unglückliche Färbung)

![[Bildschirmfoto 2026-05-07 um 20.31.44.png]]

---

Achtung #exam Modifikationen, z.B. finde Dreiecke, Vierecke mit Color-Coding, etc.