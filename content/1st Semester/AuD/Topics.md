### 1. Laufzeitanalyse & Mathematische Grundlagen

- **Asymptotische Notation**
    - Definitionen von $O$ (Obere Schranke), $\Omega$ (Untere Schranke) und $\Theta$ (Exakte Schranke).
    - Verständnis, dass Konstanten bei $O$-Notation wegfallen.
    - **Wachstum von Logarithmen:**
        - Basiswechsel verändert die Komplexitätklasse nicht (konstanter Faktor).
        - Achtung bei Exponenten im Logarithmus (z.B. $\log(n^{\sqrt{n}})$ ist $\Theta(\sqrt{n} \log n)$).
    - **Stirling-Formel:** Näherung für $n! \approx \sqrt{2\pi n}(\frac{n}{e})^n$.
- **Rekursion & Master Theorem**
    - Auflösen von Rekursionen der Form $T(n) = aT(n/b) + Cn^d$.
    - Die 3 Fälle des Master Theorems (abhängig vom Verhältnis $d$ zu $\log_b a$).
    - Herleitung der Laufzeit durch rekursives Einsetzen (warum $n/2$ zu $\log n$ führt).
- **Beweistechniken**
    - **Invariante:** Aussage, die vor und nach jeder Iteration einer Schleife wahr bleibt (z.B. bei Sortieralgorithmen).
    - **Untere Schranke für vergleichsbasiertes Suchen/Sortieren:**
        - Entscheidungsbaum-Modell (Höhe des Baumes = Anzahl Vergleiche).
        - Beweis, dass Suchen $\Omega(\log n)$ und Sortieren $\Omega(n \log n)$ benötigt.

### 2. Suchen & Sortieren

- **Suchalgorithmen**
    - **Linear Search:** $\Theta(n)$.
    - **Binary Search:** Auf sortierten Arrays, $\Theta(\log n)$.
        - Anwendung: Index Search in fast sortiertem Array.
    - **Star-Suche (Problem):** Finden eines "Stars" (kennt niemanden, alle kennen ihn).
        - Ansätze: Naiv ($O(n^2)$), Rekursiv, Optimiert ($3n-4$ Fragen).
    - **Maximum Subarray Sum:** Finden der größten Summe eines Teilarrays.
        - Varianten: Brute Force ($O(n^3)$ oder $O(n^2)$), Divide & Conquer ($O(n \log n)$), Dynamisch/Kadane ($O(n)$).
- **Sortieralgorithmen**
    - **Einfache Verfahren ($O(n^2)$):**
        - Bubble Sort, Selection Sort, Insertion Sort.
        - Laufzeiten für Vergleiche vs. Vertauschungen/Bewegungen unterscheiden.
    - **Effiziente Verfahren ($O(n \log n)$):**
        - **Merge Sort:** Divide & Conquer, stabil, benötigt $O(n)$ Zusatzspeicher.
        - **Quicksort:** Pivot-Wahl, Partitionierung, In-place, Best Case $O(n \log n)$, Worst Case $O(n^2)$.
        - **Heapsort:** Basiert auf Max-Heap, In-place, nicht stabil.
        - **Bucket Sort:** Wenn Wertebereich bekannt, $O(n)$ möglich.

### 3. Datenstrukturen

- **Vergleichstabelle:** Laufzeiten für Insert, Get, Delete bei Array, Listen (1-fach/2-fach), Heaps, Suchbäumen.
- **Heap (Vorzugsweiseschlange/Priority Queue)**
    - Struktur (Binärbaum im Array), Max-Heap vs. Min-Heap Eigenschaft.
    - Operationen: `Insert`, `ExtractMax/Min`, `Heapify` (Array zu Heap in $O(n)$), `DecreaseKey`.
    - Index-Berechnung: Kinder von $k$ sind bei $2k$ und $2k+1$.
- **Union-Find (Disjoint Set)**
    - Verwaltung von disjunkten Mengen (z.B. für Kruskal MST).
    - Operationen: `make`, `find` (same), `union`.
    - Laufzeit: Amortisiert fast konstant $O(\log n)$ bzw. mit Pfadkompression noch schneller.
- **Graphendarstellung**
    - **Adjazenzmatrix:** Gut für dichte Graphen, Kanten-Test $O(1)$, Speicher $O(n^2)$.
    - **Adjazenzliste:** Gut für dünne Graphen, Speicher $O(n+m)$, Nachfolger iterieren effizient.

### 4. Graphentheorie Grundlagen

- **Begriffe:** Vertex (Knoten), Edge (Kante), Grad (Degree), Pfad (keine Wdh. Knoten), Weg (Walk), Zyklus (Kreis), Zusammenhangskomponente.
- **Spezielle Graphen/Wege:**
    - **Eulerweg/Zyklus:** Jede Kante genau einmal. Existiert $\Leftrightarrow$ alle Knotengrade gerade (Zyklus) oder max. 2 ungerade (Weg). Laufzeit $O(n+m)$.
    - **Hamiltonpfad/Kreis:** Jeder Knoten genau einmal. NP-schwer (polynomiell unmöglich).
    - **Bipartite Graphen:** 2-färbbar, keine Zyklen ungerader Länge.
    - **Bäume:** Zusammenhängend & kreisfrei. $cut vertex$ / $cut edge$.
- **Gerichtete Graphen:**
    - Topologische Sortierung (nur bei DAG - Directed Acyclic Graph).
    - Quellen (in-degree 0) und Senken (out-degree 0).

### 5. Graphenalgorithmen (Traversierung & Pfade)

- **Breitensuche (BFS)**
    - Verwendung: Kürzeste Wege in **ungewichteten** Graphen, Bipartition-Test, Zusammenhang prüfen.
    - Datenstruktur: Queue (FIFO).
    - Laufzeit: $O(|V|+|E|)$.
- **Tiefensuche (DFS)**
    - Verwendung: Topologische Sortierung, Zykluserkennung, Zusammenhangskomponenten.
    - Datenstruktur: Stack (LIFO) oder Rekursion.
    - **Pre- & Post-Order:** Wichtig für Topologische Sortierung (umgekehrte Post-Order).
    - **Kantenklassifizierung:** Tree edges, Forward edges, Back edges (Indikator für Zyklus!), Cross edges.
- **Kürzeste Wege (Gewichtet)**
    - **Dijkstra:**
        - Voraussetzung: Keine negativen Kantengewichte.
        - Funktionsweise: Greedy mit Priority Queue (Relaxation der Kanten).
        - Laufzeit: $O((|V|+|E|) \log |V|)$.
    - **Bellman-Ford:**
        - Erlaubt negative Kanten, erkennt negative Zyklen.
        - Funktionsweise: $|V|-1$ Runden Relaxation aller Kanten..
        - Laufzeit: $O(|V| \cdot |E|)$.

### 6. Minimale Spannbäume (MST)

- **Konzepte:**
    - Schnittprinzip (Cut Property): Die leichteste Kante, die aus einem Schnitt (Subset) herausführt, ist sicher im MST.
    - Unterschied zu kürzesten Wegen (Dijkstra).
- **Algorithmen:**
    - **Kruskal:** Sortiert Kanten aufsteigend, fügt hinzu, wenn kein Zyklus entsteht (nutzt Union-Find). Laufzeit $O(E \log E)$.
    - **Prim:** Wächst von einem Startknoten aus (wie Dijkstra, aber Distanz ist nur Kantenlänge, nicht Pfadsumme). Laufzeit $O((V+E) \log V)$.
    - **Boruvka:** Verbindet Zusammenhangskomponenten, indem für jede ZHK die billigste ausgehende Kante gewählt wird. Halbiert Anzahl ZHKs pro Runde. Laufzeit $O((V+E) \log V)$.

### 7. Dynamische Programmierung (DP)

- **Das 5-Schritte-Schema:**
    1. Dimension/Parametrisierung definieren.
    2. Teilproblem definieren ($DP$-Tabelle Bedeutung).
    3. Rekursionsformel (Übergang) aufstellen.
    4. Berechnungsreihenfolge & Base Case festlegen.
    5. Lösung extrahieren und Laufzeit bestimmen.
- **Konzepte:** Memoization vs. Bottom-Up, Rückverfolgung für Lösungskonstruktion.
- **Wichtige Beispiel-Probleme (Muster kennen!):**
    - **Jump-Game:** Min. Sprünge zum Ziel ($1D$ Array).
    - **Längste gemeinsame Teilfolge (LCS):** $2D$ Tabelle, Vergleich von zwei Strings.
    - **Editierdistanz:** Min. Operationen um Strings umzuwandeln (Einfügen, Löschen, Ersetzen).
    - **Teilsummenproblem:** Kann Summe $S$ mit gegebenen Zahlen erreicht werden? (Boolesche Tabelle).
    - **Ticket Shop / Coffee & Tea:** Varianten von Optimierungsproblemen.        
