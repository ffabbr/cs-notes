## Diskrete Mathematik

### Logik & Beweissysteme

| Begriff                         | Bedeutung                                                        |
| ------------------------------- | ---------------------------------------------------------------- |
| Beweissystem ($\Pi$)            | Tupel aus Aussagen, Beweisen, Wahrheitsfunktion und Verifikation |
| $\mathcal{S}$ (Statements)      | Menge der Aussagen                                               |
| $\mathcal{P}$ (Proofs)          | Menge der Beweise                                                |
| $\tau$ (Truth function)         | Funktion, die Wahrheitswert (0/1) einer Aussage definiert        |
| $\phi$ (Verification)           | Funktion, die prüft, ob ein Beweis gültig ist                    |
| Sound (korrekt)                 | Kein Beweis für falsche Aussagen möglich                         |
| Complete (vollständig)          | Für jede wahre Aussage existiert ein Beweis                      |
| Alphabet ($\Lambda$)            | Menge der erlaubten Symbole                                      |
| Interpretation                  | Zuweisung von Werten zu freien Elementen                         |
| Modell                          | Eine wahre Interpretation                                        |
| Logische Konsequenz ($\models$) | G folgt aus F                                                    |
| Logische Äquivalenz ($\equiv$)  | F und G haben in jeder Interpretation denselben Wahrheitswert    |
| Erfüllbar (satisfiable)         | Mindestens eine wahrmachende Interpretation existiert            |
| Tautologie                      | In jeder Interpretation wahr                                     |
| Unerfüllbar                     | In keiner Interpretation wahr                                    |

### Prädikatenlogik & Quantoren

| Begriff | Bedeutung |
|---------|-----------|
| Existenzquantor ($\exists$) | "Es existiert mindestens ein..." |
| Allquantor ($\forall$) | "Für alle..." |
| Scope (Geltungsbereich) | Bereich, in dem ein Quantor wirkt |

### Mengen

| Begriff | Bedeutung |
|---------|-----------|
| Element von ($\in$) | x ist in Menge A enthalten |
| Teilmenge ($\subseteq$) | Alle Elemente von A sind auch in B |
| Echte Teilmenge ($\subset$) | Teilmenge, aber nicht gleich |
| Tupel | Geordnete Menge (Reihenfolge wichtig) |
| Potenzmenge ($\mathcal{P}(A)$) | Menge aller Teilmengen von A |
| Kardinalität ($\|A\|$) | Anzahl der Elemente einer Menge |
| Kartesisches Produkt ($A \times B$) | Menge aller Paare (a,b) mit $a \in A$, $b \in B$ |
| Leere Menge ($\emptyset$) | Menge ohne Elemente |
| Russells Paradox | Widerspruch bei selbstreferenziellen Mengen |

### Relationen

| Begriff | Bedeutung |
|---------|-----------|
| Relation ($\rho$) | Teilmenge von $A \times B$ |
| Identitätsrelation ($id_A$) | Jedes Element steht nur zu sich selbst in Relation |
| Inverse Relation ($\hat{\rho}$) | Richtung der Paare vertauscht |
| Komposition ($\rho \circ \sigma$) | Verkettung von Relationen über Zwischenelement |
| Reflexiv | Jedes Element steht zu sich selbst in Relation |
| Irreflexiv | Kein Element steht zu sich selbst in Relation |
| Symmetrisch | Wenn $a \rho b$, dann $b \rho a$ |
| Antisymmetrisch | Beide Richtungen nur bei Gleichheit |
| Transitiv | Wenn $a \rho b$ und $b \rho c$, dann $a \rho c$ |
| Kongruenz modulo m ($\equiv_m$) | Gleicher Rest bei Division durch m |

### Spezielle Relationen

| Begriff | Bedeutung |
|---------|-----------|
| Äquivalenzrelation | Reflexiv, symmetrisch, transitiv |
| Äquivalenzklasse ($[a]_\Theta$) | Menge aller Elemente, die zu a äquivalent sind |
| Partition | Zerlegung einer Menge in disjunkte Teilmengen |
| Quotientenmenge ($A/\theta$) | Menge aller Äquivalenzklassen |
| Ordnungsrelation | Reflexiv, antisymmetrisch, transitiv |

### Posets & Hasse-Diagramme

| Begriff                       | Bedeutung                                                   |
| ----------------------------- | ----------------------------------------------------------- |
| Poset                         | Partially ordered set (Menge mit Ordnungsrelation)          |
| Lexikographische Ordnung      | Vergleich wie im Wörterbuch                                 |
| Deckung (covers)              | b deckt a, wenn nichts zwischen a und b liegt               |
| Vergleichbar                  | a ≼ b oder b ≼ a                                            |
| Totalgeordnet                 | Alle Elemente sind vergleichbar                             |
| Well-ordered                  | Totalgeordnet und jede Teilmenge hat kleinstes Element      |
| Kleinstes Element             | Element ist related zu allen anderen                        |
| Größtes Element               | Alle Elemente sind related zu diesem                        |
| Minimales Element             | Kein Element zeigt auf dieses                               |
| Maximales Element             | Zeigt auf kein anderes Element                              |
| Transitive Closure ($\rho^*$) | Alle erreichbaren Verbindungen über beliebig viele Schritte |
| Meet                          | Eindeutiger gemeinsamer lower bound zweier Elemente         |
| Join                          | Eindeutiger gemeinsamer upper bound zweier Elemente         |
| Lattice (Verband)             | Alle Paare haben Meet und Join                              |

### Zählbarkeit

| Begriff | Bedeutung |
|---------|-----------|
| Abzählbar (countable) | Gleichmächtig zu $\mathbb{N}$ |
| Überabzählbar (uncountable) | Nicht abzählbar (z.B. $\mathbb{R}$) |
| Equinumerous ($\sim$) | Gleichmächtig, es existiert eine Bijektion |
| Dominiert ($\preceq$) | Es existiert eine Injektion von A nach B |
| Bijektion | Injektiv und surjektiv |
| Injektion | Verschiedene Elemente haben verschiedene Bilder |
| Surjektion | Jedes Element im Zielbereich wird getroffen |

### Beweisstrategien

| Begriff | Bedeutung |
|---------|-----------|
| Direkter Beweis | Nimm S an, zeige T |
| Indirekter Beweis (Kontraposition) | Nimm ¬T an, zeige ¬S |
| Beweis durch Widerspruch | Nimm ¬S an, leite Widerspruch ab |
| Fallunterscheidung | Teile in Fälle auf, beweise jeden einzeln |
| Modus Ponens | Aus F und (F → G) folgt G |
| Existenzbeweis | Finde ein konkretes Beispiel |
| Pigeonhole Principle | n Objekte auf k Gruppen → mindestens eine Gruppe hat $\lceil n/k \rceil$ |

### Algebra – Grundlagen

| Begriff                              | Bedeutung                                             |
| ------------------------------------ | ----------------------------------------------------- |
| Algebra                              | Menge G mit Operation $*$, unter dieser abgeschlossen |
| Abgeschlossen / Closed               | Operation bleibt innerhalb der Menge                  |
| Assoziativ / Associative             | $(a*b)*c = a*(b*c)$                                   |
| Kommutativ / Commutative             | $a*b = b*a$                                           |
| Neutrales Element / Identity element | $a * e = e * a = a$                                   |
| Inverses Element / Inverse           | $a * \hat{a} = e$                                     |
| Monoid                               | Algebra + assoziativ + neutrales Element              |
| Gruppe / Group                       | Monoid + inverses Element für jedes $a$               |
| Abelsche Gruppe / Abelian group      | Gruppe + Kommutativität                               |

### Algebra – Ordnung

| Begriff | Bedeutung |
|---------|-----------|
| Ordnung einer Gruppe / Order of a group | Anzahl Elemente in der Gruppe $\|G\|$ |
| Ordnung eines Elementes / Order of an element | Kleinstes $n$ mit $a^n = e$ |
| Satz von Lagrange | $\|H\|$ teilt $\|G\|$ für Untergruppe $H$ |

### Algebra – Untergruppen und Strukturen

| Begriff | Bedeutung |
|---------|-----------|
| Untergruppe / Subgroup | Teilmenge, abgeschlossen unter Operation, mit $e$ und Inversen |
| Zyklische Gruppe / Cyclic group | Alle Elemente entstehen aus einem Generator |
| Generator | Element das alle Gruppenelemente erzeugt |
| Direct Product | Neue Gruppe aus Tupeln mehrerer Gruppen |

### Algebra – Homomorphismen

| Begriff | Bedeutung |
|---------|-----------|
| Homomorphismus / Homomorphism | $\psi(a \circ b) = \psi(a) * \psi(b)$ |
| Isomorphismus / Isomorphism | Bijektiver Homomorphismus |
| Injektiv / Injective | $\psi(a) = \psi(b) \Rightarrow a = b$ |
| Surjektiv / Surjective | Jedes Element im Bild wird getroffen |
| Bijektion / Bijection | Injektiv und surjektiv |

### Algebra – Ringe und Körper

| Begriff | Bedeutung |
|---------|-----------|
| Ring | Menge mit Addition (Gruppe) und Multiplikation (Monoid) |
| Körper / Field | Ring, alle $\neq 0$ haben multiplikatives Inverses |
| Distributivgesetz | $a(b+c) = ab + ac$ |
| Nullteiler / Zero divisor | $a \neq 0$, $b \neq 0$, aber $ab = 0$ |
| Integritätsbereich / Integral domain | Ring ohne Nullteiler |
| Einheit / Unit | Element mit multiplikativem Inversen ($a \cdot b = 1$) |
| $R^*$ | Menge aller Einheiten (invertierbaren Elemente) |
| GF(p) / Galois Field | $\mathbb{Z}_p$ für Primzahl $p$ |

### Algebra – Polynome

| Begriff | Bedeutung |
|---------|-----------|
| Polynom / Polynomial | Ausdruck $a_n x^n + ... + a_0$ |
| $F[x]$ | Polynomring über Körper F |
| Grad / Degree | Höchste Potenz im Polynom |
| Monisch / Monic | Führender Koeffizient = 1 |
| Irreduzibel / Irreducible | Keine nicht-trivialen Faktoren |
| Reduzibel / Reducible | Hat Nullstelle, also faktorisierbar |
| Polynomdivision | $a(x) = b(x) \cdot q(x) + r(x)$ |
| Nullstelle / Root | Wert $\alpha$ mit $p(\alpha) = 0$ |
| $F[x]_{m(x)}$ | Polynome modulo $m(x)$, Körper wenn $m(x)$ irreduzibel |

### Zahlentheorie

| Begriff | Bedeutung |
|---------|-----------|
| Teilbarkeit / Divisibility | $d \mid a \Leftrightarrow \exists q: a = dq$ |
| gcd / ggT | Größter gemeinsamer Teiler |
| lcm / kgV | Kleinstes gemeinsames Vielfaches |
| Teilerfremd / Coprime | $\gcd(a,b) = 1$ |
| Ideal | Menge $\{ua + vb : u,v \in \mathbb{Z}\}$ |
| Primfaktorzerlegung | $a = \prod p_i^{e_i}$ |
| Äquivalenz modulo | $a \equiv_m b \Leftrightarrow m \mid (a-b)$ |
| Restklasse / Residue class | $[a]_m = \{b : a \equiv_m b\}$ |
| Multiplikatives Inverses | $a \cdot a^{-1} \equiv_m 1$ |

### Euler und Fermat

| Begriff | Bedeutung |
|---------|-----------|
| Eulersche Phi-Funktion $\varphi(m)$ | Anzahl teilerfremder Zahlen zu $m$ |
| $\mathbb{Z}_m^*$ | Menge der zu $m$ teilerfremden Elemente |
| Satz von Euler | $a^{\varphi(m)} \equiv_m 1$ für $\gcd(a,m)=1$ |
| Satz von Fermat | $a^{p-1} \equiv_p 1$ für Primzahl $p$ |

### Kryptographie

| Begriff | Bedeutung |
|---------|-----------|
| Diffie-Hellman | Schlüsselaustausch mit $g^{x_A}$, $g^{x_B}$ mod $p$ |
| RSA | Public-Key-Verfahren mit $n = p \cdot q$ |
| Diskreter Logarithmus | Aus $g^x$ schwer $x$ zu berechnen |
| Public Key | Öffentlicher Schlüssel |
| Private Key | Geheimer Schlüssel |

---

## Algorithmen und Datenstrukturen

### Datenstrukturen – Grundlegend

| Begriff | Bedeutung |
|---------|-----------|
| Array | Feste Größe, O(1) Zugriff, O(n) Einfügen/Löschen |
| 1-verkettete Liste | Einfach verkettete Liste, O(1) Einfügen, O(n) Zugriff |
| 2-verkettete Liste | Doppelt verkettete Liste, O(1) Einfügen/Löschen |
| Stack | Last In First Out (push, pop) |
| Queue | First In First Out (enqueue, dequeue) |
| Priority Queue | Min/Max-Heap, O(log n) für Insert/ExtractMin |

### Datenstrukturen – Bäume

| Begriff | Bedeutung |
|---------|-----------|
| Heap | Binärbaum mit O(log n) Einfügen/Löschen, O(1) Max-Zugriff |
| Binärer Suchbaum | Sortierter Baum mit O(log n) Operationen |
| 2-3-Baum | Balancierter Baum mit garantiert O(log n) |
| Heapify | Array in Heap umwandeln, O(n) |
| ExtractMax | Maximum aus Heap entfernen und versickern |

### Sortieralgorithmen

| Begriff | Bedeutung |
|---------|-----------|
| Bubble Sort | Benachbarte Elemente tauschen, O(n²) |
| Selection Sort | Größtes Element ans Ende, O(n²) |
| Insertion Sort | Element an richtige Stelle im sortierten Teil, O(n²) |
| Merge Sort | Divide & Conquer, rekursiv teilen und mergen, O(n log n) |
| Quicksort | Pivotelement wählen, partitionieren, in-place, O(n log n) avg |
| Heapsort | Selection Sort mit Max-Heap, O(n log n) |
| Bucket Sort | Elemente in Buckets verteilen, O(n) |
| Pivotelement | Element zum Partitionieren bei Quicksort |

### Suchalgorithmen

| Begriff | Bedeutung |
|---------|-----------|
| Linear Search | Jedes Element durchgehen, O(n) |
| Binary Search | Liste halbieren bei sortiertem Array, O(log n) |
| Entscheidungsbaum | Binärbaum für Vergleiche, Blätter sind Ergebnisse |
| Star-Suche | Person finden, die alle kennen aber niemanden kennt |

### Graphentheorie – Grundbegriffe

| Begriff | Bedeutung |
|---------|-----------|
| Vertex (Knoten) | Punkt im Graphen |
| Edge (Kante) | Verbindung zwischen zwei Knoten |
| Grad | Anzahl anliegender Kanten eines Knotens |
| Weg (Walk) | Folge benachbarter Knoten |
| Pfad (Path) | Weg ohne wiederholte Knoten |
| Zyklus | Weg mit Start = Ende |
| Kreis (Cycle) | Zyklus ohne Knotenwiederholung, min. 3 Knoten |
| Eulerweg | Jede Kante genau einmal |
| Hamiltonpfad | Jeder Knoten genau einmal |
| adjazent | Benachbarte Knoten |
| inzident | Kante anliegend zu einem Knoten |
| Zusammenhangskomponente | Verbundener Teilgraph |
| Baum (Tree) | Zusammenhängend ohne Kreis |
| bipartit | Graph in zwei Partitionen teilbar |
| cut vertex | Knoten dessen Entfernung Graph trennt |
| cut edge | Kante deren Entfernung Graph trennt |

### Graphentheorie – Gerichtete Graphen

| Begriff | Bedeutung |
|---------|-----------|
| Gerichteter Graph | Graph mit geordneten Knotenpaaren |
| Senke | Knoten ohne Nachfolger, deg_out = 0 |
| Quelle | Knoten ohne Vorgänger, deg_in = 0 |
| Eingangsgrad | Anzahl eingehender Kanten |
| Ausgangsgrad | Anzahl ausgehender Kanten |
| Adjazenzmatrix | Matrix zur Darstellung von Kanten |
| Adjazenzliste | Liste aller Nachfolger pro Knoten |
| Topologische Sortierung | Reihenfolge mit erfüllten Abhängigkeiten |

### Graph-Algorithmen – Traversierung

| Begriff | Bedeutung |
|---------|-----------|
| BFS (Breitensuche) | Ebenenweise traversieren mit Queue, O(V+E) |
| DFS (Tiefensuche) | So weit wie möglich vorlaufen mit Stack, O(V+E) |
| Breitensuchbaum | Erfasst minimale Distanzen zu Knoten |
| Pre-order | Reihenfolge des ersten Betretens |
| Post-order | Reihenfolge des letzten Verlassens |
| Tree edge | Kante im Tiefensuchbaum |
| Forward edge | Kante zu indirektem Nachfolger |
| Back edge | Kante zu indirektem Vorgänger (→ Zyklus) |
| Cross edge | Kante zwischen verschiedenen DFS-Teilbäumen |

### Graph-Algorithmen – Kürzeste Wege

| Begriff | Bedeutung |
|---------|-----------|
| Dijkstra | Kürzester Weg mit pos. Gewichten, O((V+E) log n) |
| Bellman-Ford | Kürzester Weg auch mit neg. Gewichten, O(V·E) |
| Negativer Zyklus | Zyklus mit negativer Gesamtgewichtssumme |

### Laufzeitanalyse

| Begriff | Bedeutung |
|---------|-----------|
| O-Notation (Big-O) | Obere Schranke für Wachstum |
| Ω-Notation (Omega) | Untere Schranke für Wachstum |
| Θ-Notation (Theta) | Exakte Wachstumsordnung |
| Master Theorem | Laufzeit für T(n) = aT(n/b) + Cn^d bestimmen |
| a (Master Theorem) | Anzahl der Teilprobleme |
| b (Master Theorem) | Verkleinerungsfaktor |
| d (Master Theorem) | Arbeit außerhalb der Rekursion |

### Dynamische Programmierung

| Begriff | Bedeutung |
|---------|-----------|
| Dynamische Programmierung | Optimierung durch Teilprobleme und Memoization |
| Memoization | Zwischenspeichern bereits berechneter Werte |
| Bottom-up | Iterativ von kleinen zu großen Teilproblemen |
| DP-Tabelle | Tabelle zur Speicherung der Teilproblem-Lösungen |
| Teilproblem | Kleinere Instanz des Gesamtproblems |
| Rekursionsformel | Berechnung aus vorherigen Einträgen |
| Editierdistanz | Min. Operationen um String A in B umzuwandeln |
| LGT (Längste gemeinsame Teilfolge) | Längste gemeinsame Subsequenz zweier Folgen |
| Teilsummenproblem | Gibt es Teilmenge mit bestimmter Summe? |
| Rucksackproblem | Maximaler Wert bei begrenzter Kapazität |
| Maximum Subarray Sum | Größte Summe eines zusammenhängenden Teilarrays |

### Algorithmen-Konzepte

| Begriff | Bedeutung |
|---------|-----------|
| Invariante | Aussage die nach jeder Iteration gilt |
| Divide and Conquer | Teilen, rekursiv lösen, kombinieren |
| In-place | Kein zusätzlicher Speicher nötig |
| Vergleichsbasiertes Suchen | Min. Ω(log n) Vergleiche im Worst Case |
| Vergleichsbasiertes Sortieren | Min. Ω(n log n) Vergleiche im Worst Case |


---

## Einführung in die Programmierung

### Hoare-Logik

| Begriff | Bedeutung |
|---------|-----------|
| Hoare-Tripel ({P} X = E {Q}) | Vorbedingung, Anweisung, Nachbedingung |
| Weakest Precondition | Schwächste Vorbedingung, die Nachbedingung garantiert |
| Loop Invariante | Bedingung, die vor/nach jeder Schleifeniteration gilt |

### Klassen & Objekte

| Begriff | Bedeutung |
|---------|-----------|
| Klasse (class) | Bauplan für Objekte |
| Objekt (object) | Instanz einer Klasse, erstellt mit `new` |
| Attribut | Variable in Klasse, beschreibt Zustand |
| Methode | Funktion in Klasse, beschreibt Verhalten |
| Zustand (state) | Menge aller Attributwerte eines Objekts |
| Referenz | Zeiger auf ein Objekt im Speicher |
| Punktnotation (dot notation) | Zugriff auf Attribute/Methoden via `objekt.name` |
| Dereferenzierung | Zugriff auf Objekt über Referenz |
| this | Referenz auf das aktuelle Objekt |
| Shadowing | Lokale Variable verdeckt gleichnamiges Attribut |
| Konstruktor | Spezielle Methode zur Objektinitialisierung |
| toString() | Methode zur String-Darstellung eines Objekts |

### Vererbung & Polymorphismus

| Begriff | Bedeutung |
|---------|-----------|
| Vererbung (extends) | Unterklasse übernimmt Attribute/Methoden der Oberklasse |
| Oberklasse (Superclass) | Klasse, von der geerbt wird |
| Unterklasse (Subclass) | Klasse, die erbt |
| Override (@Override) | Methode der Oberklasse in Unterklasse überschreiben |
| super | Referenz auf direkte Oberklasse |
| instanceof | Prüft ob Objekt Instanz einer Klasse ist |
| statischer Typ | Deklarierter Typ, unveränderlich |
| dynamischer Typ | Tatsächlicher Typ zur Laufzeit, änderbar |
| Dynamic Binding | Methodenauswahl basierend auf dynamischem Typ |
| Cast | Typumwandlung "nach unten" im Vererbungsbaum |
| Object | Wurzelklasse aller Java-Klassen |
| final (Klasse) | Verbietet Vererbung (kein extends) |
| final (Methode) | Verbietet Override |
| final (Variable) | Wert/Referenz unveränderbar |
| Abstrakte Klasse | Klasse die nicht instanziiert werden kann |

### Interfaces

| Begriff | Bedeutung |
|---------|-----------|
| Interface | Vertrag, dass Klasse bestimmte Methoden implementiert |
| implements | Klasse implementiert ein Interface |
| extends (Interface) | Interface erweitert anderes Interface |

### Sichtbarkeit (Access Modifiers)

| Begriff | Bedeutung |
|---------|-----------|
| public | Überall sichtbar |
| protected | In Klasse, Unterklassen und Package sichtbar |
| default (package-private) | Nur im selben Package sichtbar |
| private | Nur in eigener Klasse sichtbar |

### Datentypen – Primitiv

| Begriff | Bedeutung |
|---------|-----------|
| Primitive Typen | Speichern direkt den Wert (int, double, boolean, char) |
| int | Ganzzahl (primitiv) |
| double | Kommazahl (primitiv) |
| boolean | Wahrheitswert true/false (primitiv) |
| char | Einzelnes Zeichen (primitiv) |
| Value Semantics | Zuweisung kopiert den Wert (primitive Typen) |

### Datentypen – Referenz

| Begriff | Bedeutung |
|---------|-----------|
| Referenztypen | Speichern Referenz auf Objekt (String, Arrays, Klassen) |
| String | Text (Referenztyp, immutable) |
| Integer | Wrapper-Klasse für int, kann null sein |
| Autoboxing | Automatische Umwandlung primitiv → Wrapper |
| Unboxing | Automatische Umwandlung Wrapper → primitiv |
| null | Keine Referenz, Standardwert für Referenztypen |
| Reference Semantics | Zuweisung kopiert die Referenz (Referenztypen) |
| immutable | Unveränderbar (z.B. String) |
| Aliasing | Mehrere Referenzen zeigen auf dasselbe Objekt |

### Casting & Konvertierung

| Begriff | Bedeutung |
|---------|-----------|
| Implizites Casting (Widening) | Automatische Typumwandlung zu größerem Typ |
| Explizites Casting (Narrowing) | Manuelle Typumwandlung zu kleinerem Typ |

### Methoden & Funktionen

| Begriff | Bedeutung |
|---------|-----------|
| void | Kein Rückgabewert |
| return | Gibt Wert aus Methode zurück |
| Parameter | Eingabewerte einer Methode |
| Überladung (Overloading) | Mehrere Methoden mit gleichem Namen, unterschiedlicher Signatur |
| Signatur | Name + Parametertypen einer Methode |
| static | Gehört zur Klasse, nicht zum Objekt |

### Exceptions

| Begriff | Bedeutung |
|---------|-----------|
| Exception | Laufzeitfehler/Ausnahme |
| throw | Exception werfen |
| NullPointerException | Fehler bei Zugriff auf null-Referenz |
| IllegalArgumentException | Fehler bei ungültigen Argumenten |

### Kontrollstrukturen

| Begriff | Bedeutung |
|---------|-----------|
| if-else | Bedingte Verzweigung |
| switch-case | Mehrfachverzweigung |
| for-Schleife | Zählschleife |
| while-Schleife | Kopfgesteuerte Schleife |
| do-while-Schleife | Fußgesteuerte Schleife |
| Enhanced for | Iteriert über Arrays/Collections |
| break | Schleife abbrechen |
| continue | Aktuellen Durchlauf überspringen |

### Logische Operatoren

| Begriff | Bedeutung |
|---------|-----------|
| && | Logisches UND (AND) |
| \|\| | Logisches ODER (OR) |
| ! | Logisches NICHT (NOT) |
| == | Gleichheit (nur für primitive Typen) |
| equals() | Gleichheit für Objekte |

### Arrays & Collections

| Begriff | Bedeutung |
|---------|-----------|
| Array | Feste Sammlung von Werten gleichen Typs |
| Scanner | Klasse zum Einlesen von Eingaben |
| Random | Klasse für Zufallszahlen |

### Rekursion

| Begriff | Bedeutung |
|---------|-----------|
| Rekursion | Methode ruft sich selbst auf |
| Basisfall | Abbruchbedingung der Rekursion |
| Rekursiver Fall | Selbstaufruf mit verkleinertem Problem |

### Sonstiges

| Begriff | Bedeutung |
|---------|-----------|
| EBNF | Erweiterte Backus-Naur-Form, Grammatiknotation |
| UpperCamelCase | Namenskonvention für Klassen |
| lowerCamelCase | Namenskonvention für Methoden/Variablen |

---

## Lineare Algebra

### Matrizen – Grundlagen

| Begriff | Bedeutung |
|---------|-----------|
| Matrix $m \times n$ | Hat $m$ Zeilen und $n$ Spalten |
| Identitätsmatrix $I$ | Diagonale = 1, sonst 0; $A \cdot I = A$ |
| Diagonalmatrix | Nur Hauptdiagonale ≠ 0 |
| Obere Dreiecksmatrix | Einträge unter Diagonale = 0 |
| Untere Dreiecksmatrix | Einträge über Diagonale = 0 |
| Symmetrische Matrix | $A = A^T$ |
| Transponierte $(A^T)$ | Zeilen und Spalten vertauscht |
| Inverse Matrix $(A^{-1})$ | $A \cdot A^{-1} = I$, nur bei quadratisch & vollem Rang |

### Räume (Spaces)

| Begriff | Bedeutung |
|---------|-----------|
| Vektorraum | Menge von Vektoren, abgeschlossen unter Addition & Skalierung |
| Unterraum (Subspace) | Teilmenge eines Vektorraums, selbst ein Vektorraum |
| Spaltenraum $C(A)$ | Span der Spalten von $A$; alle erreichbaren $Ax$ |
| Zeilenraum $R(A)$ | Span der Zeilen von $A$ |
| Nullraum $N(A)$ | Lösungen von $Ax = 0$ |
| Span | Alle Linearkombinationen einer Vektormenge |
| Basis | Linear unabhängige Vektoren, die Raum aufspannen |
| Dimension | Anzahl der Basisvektoren |

### Lineare Unabhängigkeit & Rang

| Begriff | Bedeutung |
|---------|-----------|
| Linear unabhängig | Keine Linearkombination ergibt 0 (außer triviale) |
| Linear abhängig | Ein Vektor ist Kombination der anderen |
| Rang (Rank) | Anzahl linear unabhängiger Spalten/Zeilen |
| Rang-Nullitätssatz | $\text{Rang}(A) + \text{Nullität}(A) = n$ (Spaltenanzahl) |
| Steinitz-Austauschlemma | Unabh. Menge ≤ Spannende Menge; Basen gleich groß |

### Transformationen

| Begriff | Bedeutung |
|---------|-----------|
| Lineare Transformation $T_A$ | $T_A(x) = Ax$; respektiert Addition & Skalierung |
| Injektiv | Verschiedene Inputs → verschiedene Outputs |
| Surjektiv | Jeder Output hat einen Input |
| Bijektiv | Injektiv + Surjektiv; invertierbar |

### Operationen auf LGS

| Begriff | Bedeutung |
|---------|-----------|
| Zeilenvertauschung | Zwei Zeilen tauschen |
| Skalierung | Zeile mit Konstante ≠ 0 multiplizieren |
| Zeilenaddition | Vielfaches einer Zeile zu anderer addieren |
| Gauss-Elimination | Umformung in Zeilenstufenform |
| Zeilenstufenform | Obere Dreiecksform durch Elimination |

### Orthogonalität

| Begriff | Bedeutung |
|---------|-----------|
| Orthogonal ($\perp$) | Skalarprodukt = 0 |
| Orthogonales Komplement $V^\perp$ | Alle Vektoren senkrecht zu $V$ |
| $N(A) = C(A^T)^\perp$ | Nullraum ist orthogonal zum Zeilenraum |
| Skalarprodukt (Dot Product) | $a \cdot b = \sum a_i b_i$ |

### Projektionen

| Begriff | Bedeutung |
|---------|-----------|
| Projektion $\text{proj}_S(b)$ | Nächster Punkt in $S$ zu $b$ |
| Projektionsmatrix $P$ | $P = A(A^TA)^{-1}A^T$ |
| Residuum $r$ | $r = b - \text{proj}_S(b)$; Fehlervektor |

### Least Squares & Regression

| Begriff | Bedeutung |
|---------|-----------|
| Least Squares | Minimiert $\|Ax - b\|^2$ |
| Normal Equations | $A^TA\hat{x} = A^Tb$ |
| Pseudoinverse $A^\dagger$ | $(A^TA)^{-1}A^T$; löst Least Squares |
| Lineare Regression | Beste Gerade durch Datenpunkte finden |

### Sonstiges

| Begriff | Bedeutung |
|---------|-----------|
| Kreuzprodukt | Liefert Vektor senkrecht zu zwei gegebenen |
| Norm $\|v\|$ | Länge eines Vektors |
| Linearkombination | Summe von skalierten Vektoren |
