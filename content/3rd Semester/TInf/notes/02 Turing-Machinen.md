
## Definitionen

**Band**
- Anfang: ¢ Symbol
- geht unendlich nach rechts
- mit Leerzeichen initialisiert

**Berechnungsschritt** 
$\delta(q, x_i) = (q', 1, R)$
"wechsel von $q$ zu $q'$, und überschreibe $x_i$ mit $1$, Lesekopf geht nach rechts"

TM ist ein 7-Tupel aus 
- Zustände
- Eingabe-Alphabet
- Schreib-)Alphabet
- Transitionsfunktion
	- $\delta : Q - \{q_{acc}, q_{rej}\} \times \Gamma \rightarrow Q \times \Gamma \times \underbrace{\{L, R, N\}}_{\text{Bewegung des Kopfes}}$
	- wenn ganz links, können wir nicht weiter nach links gehen, also $\delta(q, \text{¢}) \in Q \times \{\text{¢}\} \times \{R, N\}$
- Anfangszustand
- 1 akzeptierender Zustand
- 1 verwerfender Zustand

**Beispiel**

![[Bildschirmfoto 2026-10-13 um 00.47.33.png|337]]

**Konfigurationen**
Alle Bandsymbole (inklusive ¢) links von dem aktuellen Zustand, dann der aktuelle Zustand $q$, dann das aktuelle Bandsymbol und alle rechts davon.

**Berechnungsschritt**
Die Berechnung muss nicht endlich sein. 
![[Bildschirmfoto 2026-10-17 um 18.23.12.png]]![[Bildschirmfoto 2026-10-17 um 18.23.27.png]]

## Menge der Sprachen, für die es eine Turing-Machine gibt

$\mathcal{L}_{RE}$ **Rekursiv aufzählbar**

Sprache $L \subseteq \Sigma^*$ ist rekursiv aufzählbar, falls es $M$ gibt, für die $L = L(M)$ gilt. Gehört das Wort **nicht** nur Sprache, kann es zu einer Endlosschleife kommen. 

$\mathcal{L}_R$ **Rekursiv**

Sprache $L \subseteq \Sigma^*$ ist rekursiv, falls es $M$ gibt, für die $L = L(M)$ gilt und die für jede Eingabe in endlicher Zeit *ja* oder *nein* ausgibt (keine Endlosschleife)

**Total berechenbare Funktionen**

Funktion $F : \Sigma^* \to \Gamma^*$ ist total berechenbar, wenn eine Turingmaschine existiert, die diese **Funktion** für beliebige Eingabe berechnet.

## k - Band-Turingmachinen

1 Eingabeband ist read-only
k Arbeitsbänd==er== zum lesen/schreiben 

![[Bildschirmfoto 2026-10-17 um 18.51.21.png]]


### Beweis Äquivalenz Einband und Mehrband Turingmachinen

TM und MTM sind äquivalent. Zwei Machinen sind äquivalent, falls genau gleich akzeptiert, verworften, unendlich gelaufen wird.

**Für jede TM existiert eine äquivalente MTM**
Zuerst kopieren wir die gesamte Eingabe von dem Eingabeband auf das Arbeitsband und schieben den Zeiger zurück an den Anfang, jetzt ist unser Arbeitsband gleich wie das der TM. 

![[Bildschirmfoto 2026-10-17 um 18.59.08.png]]

**Für jede MTM existiert eine äquivalente TM**
Wir unterteilen das eine Band der TM in virtuelle Bänder mit virtuellen Köpfen, indem wir das Alphabet erweitern. 

![[Bildschirmfoto 2026-10-17 um 19.15.56.png]]

> [!success]
> TM und Programmiersprachen sind äquivalent.

> [!info] Church Turing These
> TM als Definition für Algorithmus


## Nicht deterministische TM (NTM)

$M = (Q, \Sigma, \Gamma, \delta, q_0, q_{acc}, q_{rej})$
$\delta : (Q - \{q_{acc}, q_{rej}\}) \times \Gamma \to \text{Pot}(Q \times \Gamma \times \{L, R, N\})$

$\delta(q, \text{¢}) \subseteq \{(p, \text{¢}, x) \mid p \in Q, x \in \{R, N\}\}$
$L(M) = \{w \in \Sigma^* \mid q_0 \text{¢} w \vdash_M^* y q_{acc} z \text{ mit } y, z \in \Gamma^*\}$

Sei $M$ eine NTM. Dann existiert TM $A$, sodass
- $L(M) = L(A)$
- falls $M$ keine unendl. Berechnungen hat, hält $A$ immer

![[Bildschirmfoto 2026-10-26 um 13.12.42.png]]


![[Bildschirmfoto 2026-10-26 um 13.12.00.png]]


## Berechnungsbaum

$T_{M,x}$ für eine NTM

- Wurzel: Startpunkt
- Knoten sind Zustände
- Kinder der Knoten die Folgekonfigurationen

Somit sind Pfade Berechnungen. 

Um alle parallelen Pfade abzuarbeiten, muss die TM den Baum Ebene für Ebene (Breitensuche) absuchen.

![[Bildschirmfoto 2026-10-26 um 13.13.16.png]]

## Kodierung einer TM

Wir könnten Turingmaschinen als Wörter über bool darstellen. 

- regulärer Zustand $q_i$ wird kodiert als eine Eins, gefolgt von $i+1$ Nullen, und einer abschließenden Eins ($10^{i+1}1$). Die Endzustände $q_{acc}$ und $q_{rej}$ erhalten analoge, aber längere Codes
- Jedes Bandsymbol $A_j$ wird als $110^{j+1}11$ kodiert
- Kopfbewegungen $N$, $R$ (und implizit $L$) erhalten feste Codes, wie z.B. $1110111$ für $N$.
- Übergangsregel (Transition) $\delta(p, A_l) = (q, A_n, \alpha)$ wird gebildet, indem man die Codes der Einzelteile hintereinanderschreibt und mit einem Hash-Symbol ($\#$) abtrennt


---


![[Bildschirmfoto 2026-10-26 um 13.04.02.png]]