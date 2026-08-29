## Syntax
→ siehe [[1st Semester/DM/Skript.pdf#page=168|Skript]] 

- **Variabel:** $x_i$ 
- **Funktion:** $f_i^{(k)}$ 
	- gibt Wert aus dem Universum aus
    - $k$ ist Anzahl der Argumente    
- **Prädikat:** $P_i^{(k)}$ (mit $i, k \in \mathbb{N}$)
    - gibt true/false (1/0) aus

## Freie und gebundene Variablen

Wenn ein $x$ an ein $\exists$ oder $\forall$ gebunden ist, dann ist es gebunden. Sonst frei. 
	
![[01 Einleitung Logik Revamped#Free]] 


**Quantoren-Überschreibung**
→ der zweite Quantor überschreibt den ersten, z.B. $\forall x \exists x F \equiv \exists xF$

## Interpretationen

### Definition

$$
\mathcal{A} = (U, \phi, \psi, \xi)
$$

Eine Interpretation weisst allen freien Elementen etwas zu. 

**Passende Interpretation:** 		jedem freien Element wird ein Wert zugewiesen
**Modell:** 								wahre Interpretaion

| **Symbol** | **Name der Komponente** | **Beschreibung**                           | **Mathematische Zuweisung (k)** |
| ---------- | ----------------------- | ------------------------------------------ | ------------------------------- |
| $U$        | Universum, nicht-leer   |                                            | Menge                           |
| $\phi$     | Funktionen              | Weisst Funktionssymbolen eine Funktion zu. | $\phi(f): U^k \to U$            |
| $\psi$     | Prädikate               | Bestimmt Bedeutung der Prädikatensymbole   | $\psi(P): U^k \to \{0, 1\}$     |
| $\xi$      | Variablen               | Bestimmt Werte der Variablen               | $\xi(x_i) \in U$                |

→ [[Interpretation.png|Skript]]

### Beispiele

![[Schreibweise PL.png]]
![[Bildschirmfoto 2025-12-09 um 13.54.39.png]]
![[Bildschirmfoto 2025-12-09 um 13.55.55.png]]


## Semantik

$$
\mathcal{A}(\forall x~G) = \begin{cases} 1 & \text{falls } \mathcal{A}_{[x \to u]}(G) = 1 \text{ für alle } u \text{ in } U \\ 0 & \text{sonst} \end{cases}
$$
$$
\mathcal{A}(\exists x~G) = \begin{cases} 1 & \text{falls } \mathcal{A}_{[x \to u]}(G) = 1 \text{ für einige } u \text{ in } U \\ 0 & \text{sonst.} \end{cases}
$$

![[Semantik.png]]
![[Lemma 6-7.png]]![[Formeln.png]]

## Ersetzungen

![[Substitution.png]]

## PNF (Pränex-Normalform)

→ alle Quantoren vorne

1. Formel in bereinigte Form bringen (G Formel in der y nicht frei, dann dürfen wir **==eine gebundene Variable==** zu y umbenennen, [[1st Semester/DM/Skript.pdf#page=164|Lemma 6.11]]. Freie Variablen können nicht umbenannt werden, da sie von der Interpretation festgelegt wird) 
2. Negationen hinter die Quantoren
3. mit [[Lemma 6-7.png|Lemma 6.7]] 7-10 die Quantoren nach vorne bringen


![[PNF.png]]


## Universum als Mengen, Russels Paradox

![[Bildschirmfoto 2025-12-10 um 23.20.25.png]]
![[Übung 12.pdf]]![[Bildschirmfoto 2025-12-10 um 23.20.47.png]]