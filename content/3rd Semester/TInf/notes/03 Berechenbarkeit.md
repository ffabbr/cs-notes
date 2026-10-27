
> [!summary] Zusammenfassung Mengenlehre
> - $\vert{}A\vert{} \le \vert{}B\vert{}$, falls es eine injektive Funktion von $A$ nach $B$ gibt
> - $\vert{}A\vert{} = \vert{}B\vert{}$, falls $\vert{}A\vert{} \le \vert{}B\vert{}$ und $\vert{}B\vert{} \le \vert{}A\vert{}$ (also Bijektion)
> - $\vert{}A\vert{} < \vert{}B\vert{}$, falls $\vert{}A\vert{} \le \vert{}B\vert{}$ und es gibt keine Injektion von $B$ nach $A$
>
> #### Abzählbarkeit
>
> - abzählbar, falls $A$ endlich oder $|A| = |\mathbb{N}|$
> - Die Menge KodTM der Turingmaschinenkodierungen ist abzählbar.
> - das kartesische Produkt einer endlichen Anzahl abzählbarer Mengen ist abzählbar
> - die Potenzmenge einer abzählbar unendlichen Menge ist überabzählbar
>
> - $(\mathbb{N} - \{0\}) \times (\mathbb{N} - \{0\})$ ist abzählbar
>    ![[Bildschirmfoto 2026-10-27 um 16.36.28.png|184]]
>
> - $\mathbb{Q}^{+}$ ist abzählbar. Definiere Abbildung $h(\frac{p}{q}) = (p, q)$ von $\mathbb{Q}^{+}$ nach $(\mathbb{N} - \{0\}) \times (\mathbb{N} - \{0\})$. $h$ injektiv. Weil $(\mathbb{N} - \{0\}) \times (\mathbb{N} - \{0\})$ abzählbar, ist auch $\mathbb{Q}^{+}$ abzählbar.
> - $[0, 1]$ ist nicht abzählbar
> - $P((\Sigma_{\text{bool}})^*)$ ist nicht abzählbar
>
> ![[Bildschirmfoto 2026-10-26 um 13.07.57.png]]

## Einführung

Es gibt Probleme, die nicht algorithmisch lösbar sind. Also Probleme, für die keine TM existiert. Also gibt es mehr Sprachen als Turing Machinen. Also gibt es mehr Sprachen als Kodierungen für Turing Machinen. 

==Die Menge aller endlichen Sprachen über einem endlichen Alphabet ist abzählbar==
Sei $\Sigma$ ein endliches Alphabet. Dann ist $\Sigma^*$ abzählbar. Beweis: definiere lineare Ordnung der Elemente des Alphabets. Das ist unsere Injektion $\Sigma^* \to \mathbb{N}$. 

==Die Menge aller unendlichen Sprachen über einem endlichen Alphabet ist überabzählbar==
Die Menge aller Sprachen über $\Sigma_{\text{bool}}$ (die Potenzmenge $\mathcal{P}(\Sigma_{\text{bool}}^*)$) ist überabzählbar. Da die Menge der _endlichen_ Sprachen abzählbar ist, muss die Menge der verbleibenden _unendlichen_ Sprachen zwingend überabzählbar sein, da die Vereinigung zweier abzählbarer Mengen wieder abzählbar wäre.

==Es gibt mehr Sprachen als Kodierungen für Turing Machinen.==
Die Menge KodTM der Turingmaschinenkodierungen ist abzählbar. 
Die Potenzmenge einer abzählbar unendlichen Menge ist **überabzählbar**. 

$|\text{KodTM}| < |\mathcal{P}((\Sigma_{\text{bool}})^*)|$ 

- $\text{KodTM} \subseteq (\Sigma_{\text{bool}})^*$ ist abzählbar
- Menge aller Sprachen $\mathcal{P}((\Sigma_{\text{bool}})^*)$ ist **überabzählbar** 
- somit $|\text{KodTM}| < |\mathcal{P}((\Sigma_{\text{bool}})^*)|$  

**Beweis**: Nichtabzählbarkeit der Menge aller Sprachen über $\{0,1\}$, also $P((\Sigma_{\text{bool}})^*)$:  Injektion von $[0,1]_{R}$ in $\mathcal{P}((\Sigma_{\text{bool}})^*)$. Schreibe als unendliche Binärfolge. Unterteile Bitfolge in Stücke strikt aufsteigender Länge (1. $w_1 = b_1$, 2. $w_2 = b_2 b_3$, 3. $w_3 = b_4 b_5 b_6$, etc.). Alle gemeinsam $f(a) = \{w_1, w_2, w_3, \dots\}$ ist eine Teilmenge von $(\Sigma_{bool})^*$. Injektiv, da nach Länge sortiert die Binärfolge wieder entsteht. 

---

## Diagonalsprache

$$
L_{diag} = \{ x \in (\Sigma_{bool})^* \mid x = w_i \text{ für ein } i \in \mathbb{N}-\{0\} \text{ und } M_i \text{ akzeptiert das Wort } w_i \text{ nicht} \}
$$

*Die Diagonalsprache $L_{diag}$ ist so konstruiert, dass ein Wort $w_k$ genau dann zu ihr gehört, wenn die $k$-te Maschine $M_k$ dieses Wort ==NICHT AKZEPTIERT==.*

- nicht rekursiv aufzählbar
- nicht rekursiv
- Komplement ist rekursiv aufzählbar (siehe unten)
- Komplement ist nicht rekursiv

Nehme eine Tabelle: 
- Zeilen: alle Turingmachinen, kanonisch sortiert
- Spalten: alle Wörter, kanonisch sortiert
- Eintrag in der Tabelle: `1` wenn akzeptiert

Wort ist in der Diagonalsprache, wenn $M_{i}$ nicht $w_{i}$ akzeptiert.

**Beweis**: Wir beweisen $L_{\text{diag}} \notin L_{\text{RE}}$ indirekt. Sei $L_{\text{diag}} \in L_{\text{RE}}$. Dann ist $L_{\text{diag}} = L(M)$ für eine TM $M$. Weil $M$ eine der Turingmaschinen in der Nummerierung aller Turingmaschinen sein muss, existiert ein $i \in \mathbb{N} - \{0\}$, so dass $M = M_i$. Aber $L_{\text{diag}}$ kann nicht gleich $L(M_i)$ sein, weil folgende Äquivalenz gilt: $w_i \in L_{\text{diag}} \iff d_{ii} = 0 \iff w_i \notin L(M_i)$, d.h., $w_i$ ist in genau einer der Sprachen $L_{\text{diag}}$ oder $L(M_i)$.

---

==Ein Sonderfall der Diagonalsprache, bei der explizit verworfen wird, ist rekursiv aufzählbar.==
Betrachte $L_{\text{rej}} = \{w_i \mid M_i \text{ verwirft } w_i \}$. Die Sprache $L_{\text{rej}}$ ist einfacher zu erkennen. Wir simulieren die Maschine $M_i$ auf dem Wort $w_i$, bis sie explizit verwirft.


==Das Komplement der Diagonalsprache ist rekursiv aufzählbar.==
Beweis durch [[#Reduktion]]:
$$(L_{diag})^c = \{w \in \{0, 1\}^* \mid w = w_i, i \in \mathbb{N} \setminus \{0\} \text{ und } M_i \text{ akzeptiert } w_i\}$$
Betrachte TM $D$
- Auf Eingabe $x$ berechnet $D$ den Index von $x$ bzgl. kanonischer Ordnung
- Berechne $kod(M_i)$, die Kodierung der $i$-ten TM 
- simuliere $M_{i}$ auf x. Akzeptiere genau dann wenn $M_{i}$ akzeptiert

---
## Reduktion

- L1 ist auf L2 reduzierbar ($L_1 \le_R L_2$), falls $L_2 \in \mathcal{L}_R \implies L_1 \in \mathcal{L}_R$
- wenn $L_{2}$ algorithmisch lösbar ist, so ist es auch $L_{1}$

**Eingabe-zu-Eingabe-Reduktion** (Spezialfall)
- die erste TM muss die ==Eingabe verändern (transformieren), und dann einmalig an die andere TM weitergeben==
- L1 ist auf L2 EE-reduzierbar, wenn eine TM existiert, die eine Abbildung $f_{M}:\Sigma_1^* \to \Sigma_2^*$ erzeugt, mit $x \in L_1 \iff f_M(x) \in L_2$. Die eine TM übersetzt also die Eingabe einfach in ein Format für die andere TM, und reicht das Problem weiter. 

**Allgemeine Reduktion**
- ==die erste TM kann beliebiges machen, und stets die andere TM als Hilfe nutzen==

- Beispiel: Sei $\Sigma$ ein Alphabet. Für jede Sprache $L \subseteq \Sigma^*$ gilt: $L \le_R L^c$ und $L^c \le_R L$


---

## Akzeptanzproblem

Menge aller Programme, universelle Sprache

$L_u = \{ \text{Kod}(m)\#w \mid M \text{ akzeptiert } w \} \subseteq \{0,1,\#\}^*$

Theorem:
$L_u \in L_{RE}$ 

Beweis durch Konstruktion
1. TM liest Eingabe $z \in \{0,1,\#\}^*$
2. TM prüft, ob $\vert{}z\vert{}_\# = 1$ (falls nein, verwerfe)
3. überprüfe, ob der vordere Teil $\text{Kod}(M)$ für ein M entspricht
4. simuliere M mit input w

Theorem: 
$L_u \notin L_{R}$

Beweis: zeige $(L_\text{diag})^c \le_R Lu.$. Eingabe $x \in \{0,1\}^*$. Nehme an, es gibt eine TM A, die $L_u$ entscheidet.

1. TM berechnet $i$ sodass $w_i = x$.
2. TM berechnet $kod(M_i)$.
3. TM überprüft mit $A$ ob $kod(M_i)\#x \in L_u$.
4. akzeptiere genau dann wenn A akzeptiert

---

## Halteproblem

$$
L_H = \{ \text{Kod}(M) \# x \mid x \in \{0,1\}^* \land M \text{ hält auf } x \}
$$

$L_H \notin \mathcal{L}_R$
$L_H \in \mathcal{L}_{RE}$

Beweis durch Reduktion von der universellen Sprache auf das Halteproblem.



