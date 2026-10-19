
> [!warning]
> - AUSGABEZUSTÄNDE markieren
> - Zustände BENENNEN

## Allgemein

> [!success] Allgemein
> - $\Sigma$ **Alphabet**: **endliche, nichtleere** Menge an Zeichen
> - $w$ **Wort**: endliche Folge von Symbolen aus $\Sigma$ 
> - $L$ **Sprache** Menge von Wörtern aus dem Alphabet
> 	- $L^C$ Komplement der Sprache (alle Wörter in $\Sigma$, außer L)

- $\Sigma^*$: Menge aller Wörter aus $\Sigma$
  $\Sigma^+ = \Sigma^* - \{\lambda\}$ 
  z.B. $\Sigma_{\text{bool}}^*=\{\lambda, 0, 1, 00, 01, \ldots\}$

- Konkatination
	- Mit Worten: $w \cdot \lambda = \lambda \cdot w = w$ 
	- Mit Sprachen: 
		- $L_1 \cdot L_2 = \{ w_1 w_2 \mid w_1 \in L_1 \text{ und } w_2 \in L_2 \}$ : zuerst ein Wort aus $L_{1}$, dann ein Wort aus $L_{2}$ 
		- $L \cdot L_{\emptyset} = L\cdot \emptyset= L$ 
		- $L \cdot L_{\lambda} = L\cdot  \lambda = \{\lambda\}$  
- Umkehrung $w^R$

- Potenzen:
	- Wörter
		- $x^0 = \lambda$, 
		- $x^i = xx^{i-1}$
	- Sprachen, z.B. $L=\{aa, b\}$
		- $L^0 = \{ \lambda \}$
		- $L^1 = \{aa, b\}$
		- $L^2=\{aab, baa, aaaa, bb\}$ 

- **Ordnung**: Zuerst nach Wortlänge sortieren, bei gleicher Länge lexikographisch

- $L_{1}L_{2} \cup L_{1}L_{3} = L_{1}(L_{2}\cup L_{3})$ 
- $L_{1}(L_{2}\cap L_{3}) \subseteq L_{1}L_{2}\cap L_{1}L_{3}$  

## Touringmachine

Ein oder mehrere Bänder mit Kästchen und einem Lesekopf. Kann Zeichen lesen, schreiben, Kopf links oder rechts bewegen.
## Automaten

> [!success]
> Band von links nach rechts
> - $M=(Q, \Sigma, \delta, q_{0}, F)$
> - Q Zustände
> - F akzeptierende Zustände
> - $\delta$ Übergangsfunktion, z.B. $\delta(q_{1}, 0)=q_{2}$.  $\delta$ heißt ich nehme 1 Zeichen, $\hat{\delta}$ heißt ich nehme ein ganzes Wort

**Konfiguration** 
- (aktuelle Position, remaining input) $\vdash_M$ (neue Position, aktualisierter remaining input)
- am ende ist es (Endposition, $\lambda$) 
- $\vdash_M^*$ null, einen oder beliebig viele Schritte

$L(M)$ ... von M akzeptiere Sprachen

> [!Note] Tipps zum Aufstellen von Automaten
> - wenn nur Binär möglich, dann ASCI Darstellung oder z.B. # als Separator verwenden und # kodieren
> - 

**Äquivalenzklassen**
$\text{Kl}[q]$ ... Menge aller Wörter die uns an diesem Zustand landen lassen

## Regularität

> [!success]
> - **regulär:** gibt regular expression, kann mit endlich viel Memory erkennen
> - **nichtregulär:** brauche unbeschränkt viel Memory, z.B. $a^n b^n$ 

- "teilbar durch k" ist regulär
- Achtung endlich viele Zustände, Angaben die das "merken" von unendlich vielen Stellen benötigen sind nicht regulär

- $\text{endlich} \implies \text{regulär}$ 

$$
\boxed{
\text{\textbf{Regularität:}}\\
L_1,L_2\text{ regulär}
\Longrightarrow
\begin{cases}
L_1\cup L_2 & \text{regulär}\\
L_1\cap L_2 & \text{regulär}\\
L_1\setminus L_2 & \text{regulär}\\
L_1L_2 & \text{regulär}\\
L_1^* & \text{regulär}\\
L_1^+ & \text{regulär}
\end{cases}}
$$

$$
\boxed{ \begin{array}{l} \text{\textbf{Nicht-Regularität:}} \\ L \text{ nicht regulär} \iff \overline{L} \text{ nicht regulär} \\ \left. \begin{array}{r} L_1 \cap L_2 \text{ nicht regulär} \\ L_2 \text{ regulär} \end{array} \right\} \implies L_1 \text{ \textbf{nicht} regulär} \\ \left. \begin{array}{r} L_1 \cup L_2 \text{ nicht regulär} \\ L_2 \text{ regulär} \end{array} \right\} \implies L_1 \text{ \textbf{nicht} regulär} \\ \left. \begin{array}{r} L_1 \setminus L_2 \text{ nicht regulär} \\ L_2 \text{ regulär} \end{array} \right\} \implies L_1 \text{ \textbf{nicht} regulär} \end{array} }
$$

$$
\boxed{ \begin{array}{l} \text{\textbf{Operationen auf nicht-regulären Sprachen:}} \\ L_1, L_2 \text{ nicht regulär} \implies \left\{ \begin{array}{ll} \overline{L_1} & \text{\textbf{nie} regulär} \\ L_1 \setminus L_2 & \text{\textbf{manchmal} regulär} \\ L_1 \cup L_2 & \text{\textbf{manchmal} regulär} \\ L_1 L_2 & \text{\textbf{manchmal} regulär} \end{array} \right. \end{array} }
$$


> [!info]
> - $L = \{0^{n^2} \mid n \in \mathbb{N} \setminus \{0\}\}$ ist nicht regulär
> - $L = \{ww \mid w \in \{0,1\}^*\}$ ist nicht regulär 

## Nicht-Regularität zeigen

###  Lemma 3.3 (Automaten sind Gedächtnislos)

Wir lesen 2 unterschiedliche Wörter ein die zu dem gleichen Zustand führen. Wenn wir jetzt ein neues Wort einlesen, führt das zu dem gleichen Zustand, egal welches Wort wir davor gelesen haben. 

Also $x, y \in \Sigma^*$, $(q_0, x) \vdash_A^* (p, \lambda)$ und $(q_0, y) \vdash_A^* (p, \lambda)$, dann für jedes z $xz \in L(A) \iff yz \in L(A)$. 

**Widerspruch**
1. Regularität annehmen. Es gibt also einen EA
2. nehme an, es gibt n Zustände
3. betrachte $n+1$ Wörter. Da mehr Wörter als Zustände, gibt es 2, die im gleichen Zustand landen.
4. nach Lemma 3.3 müssen sie sich gleich verhalten für jedes Suffix
5. Das gilt aber nicht
	1. zeige, gibt für alle $i, j, i \neq j$, ein Suffix, sodass ein Wort gültig ist, aber das andere nicht

**Beispiel**
Sei $L_2 = \{a^n b^m \mid n, m \in \mathbb{N}, 2 \le m \le n-1, m \text{ ist Teiler von } n\}$
1. nehme an, $L_{2}$ sei regulär. gibt also einen EA mit $L(A) = L_2$ 
2. sei k die Anzahl der Zustände von A
3. Betrachte $k+1$ Wörter a², a⁴, a⁸, a¹⁶, a³², …
4. es gibt mehr Wörter als Zustände, also müssen 2 davon in dem gleichen Zustand landen 
5. Nach Lemma 3.3 müssen sie sich gleich verhalten für jedes Suffix
6. Das gilt aber nicht (unteres muss man allgemein zeigen, nicht nur das Beispiel)
	1. nehme 2 dieser Wörter, bspw. a⁴ und a⁸. 
	2. nehme b hoch (Hälfte des grösseren a-Wortes, hier b⁴)
	3. a⁸b⁴ ist in $L_{2}$
	4. a⁴b⁴ ist nicht in $L_{2}$ 

> [!proof]- Beweisskizze
> Sei $A = (Q, \Sigma, \delta, q_0, F)$ ein DEA.
> 
> 1. **Voraussetzung:** Für $x, y \in \Sigma^*$ gilt:
>    $$\delta^*(q_0, x) = \delta^*(q_0, y) = p$$
> 2. **Erweiterung um Suffix $z$:** Für ein beliebiges $z \in \Sigma^*$ gilt aufgrund des Determinismus:
>    - $\delta^*(q_0, xz) = \delta^*(\delta^*(q_0, x), z) = \delta^*(p, z)$
>    - $\delta^*(q_0, yz) = \delta^*(\delta^*(q_0, y), z) = \delta^*(p, z)$
> 3. **Zustandsgleichheit:** $\delta^*(q_0, xz) = \delta^*(q_0, yz)$. Beide Wörter enden im selben Zustand.
> 4. **Fazit:** Da der Endzustand identisch ist, liegt er entweder in $F$ oder nicht. Daraus folgt direkt:
>    $$xz \in L(A) \iff yz \in L(A) \quad \square$$

### Pumping Lemma für reguläre Sprachen

> [!info] Pumping Lemma
> endlicher Automat hat endlich viele Zustände, muss also bei einem langen Wort irgendwann im Kreis laufen (Schleife), somit ist das Wort nach beliebig vielen Schlaufen immer noch in der Sprache.

Gegeben ein $n_{0}$ finden wir ein Wort $w, |w|\geq n_{0}$, sodass gegeben ein $y,x,z$, gilt (i) und (ii), aber (iii) nicht gelten kann

Sei L regulär. Man kann alle Wörter Länge $\geq n_{0}$ in $w = yxz$ zerlegen mit
(i) $|yx| \leq n_{0}$
(ii) $|x|  \geq 1$
(iii) entweder $\{ yx^k z \mid k \in \mathbb{N} \} \subseteq L$ oder $\{ yx^k z \mid k \in \mathbb{N} \} \cap L = \emptyset$

In jedem Automaten ist $n_{0}$ nicht größer  als die Anzahl Zustände. 

**Widerspruch**
- Regularität annehmen. 
- dann gibt es ein $n_{0} \in \mathbb{N}$ mit der Eigenschaft, die das Pumping-Lemma beschreibt
- wähle Wort Länge $\geq n_{0}$
- es muss eine Zerlegung $w = yxz$ geben, die (i) und (ii) und (iii) erfüllt
- zeige: nach (i) gilt ..., nach (ii) gilt ...
- zeige, dass für jede Zerlegung mindestens ein $i$ existiert (z.B. i=0 oder i=2), sodass das aufgepumpte Wort $x y^i z$ nicht in $L$ liegt

> [!info]- Beweis: Pumping Lemma
> Sei $L$ regulär und $A = (Q, \Sigma, \varphi, q_0, F)$ ein deterministischer endlicher Automat mit $L(A) = L$.
> **1. Wahl von $n_0$:** Setze $n_0 = |Q|$.
> 
> **2. Zustandsfolge:** Sei $w \in L$ mit $|w| = m \ge n_0$. Das Einlesen von $w = a_1 \dots a_m$ induziert eine Zustandsfolge $p_0, \dots, p_m$, wobei $p_0 = q_0$ und $p_i = \varphi(p_{i-1}, a_i)$.
> 
> **3. Schubfachprinzip:** Da $|w| \ge n_0$, werden beim Lesen der ersten $n_0$ Zeichen genau $n_0 + 1$ Zustände besucht. Da der Automat nur $n_0$ Zustände hat, muss sich zwingend ein Zustand wiederholen: Es existieren Indizes $j < l \le n_0$ mit $p_j = p_l$.
> 
> **4. Zerlegung:** Wir definieren:
> * $y = a_1 \dots a_j$ (Weg von $q_0$ nach $p_j$)
> * $x = a_{j+1} \dots a_l$ (Schleife von $p_j$ zurück nach $p_j$)
> * $z = a_{l+1} \dots a_m$ (Restweg von $p_j$ in den Endzustand $p_m \in F$)
> 
> **5. Verifikation der Bedingungen:**
> * **(i) $|yx| \le n_0$:** Folgt direkt aus $l \le n_0$.
> * **(ii) $|x| \ge 1$:** Folgt aus $j < l$, die Schleife hat die Länge $l - j \ge 1$.
> * **(iii) $yx^k z \in L$ für alle $k \in \mathbb{N}$:** Der Automat verarbeitet $y$ und erreicht $p_j$. Das Wort $x^k$ durchläuft die Schleife $p_j \xrightarrow{x} p_j$ exakt $k$-mal und verbleibt in $p_j$. Das Wort $z$ überführt den Automaten anschließend von $p_j$ in den akzeptierenden Zustand $p_m \in F$. Somit ist $yx^k z \in L(A)$.

---


