## Beweissysteme

Beweissystem als Tupel:

$$
\Pi = (\mathcal{S}, \mathcal{P}, \tau, \phi)
$$

| **Symbol**    | **Name**       | **Beschreibung**                                                                                                                                                             |
| ------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| $\mathcal{S}$ | Statements     | Menge der Aussagen                                                                                                                                                           |
| $\mathcal{P}$ | Proofs         | Menge der Beweise                                                                                                                                                            |
| $\tau$        | Truth function | Funktion $\tau$: $\mathcal{S} \rightarrow \{0,1\}$; bestimmt, ob eine Aussage wahr (1) oder falsch (0) ist                                                                   |
| $\phi$        | Verification   | Funktion $\phi: \mathcal{S} \times \mathcal{P} \rightarrow \{0,1\}$; prüft, ob p ein gültiger Beweis für s ist. Wenn $\phi(s,p)=1$ und p gültig ist, gibt $\tau(s)=1$ zurück |

**Wichtige Eigenschaften:**

- Korrekt (**sound**): Es gibt kein Beweis für eine falsche Aussage
$$
\forall s \in \mathcal{S} : (\exists p \in \mathcal{P} \text{ mit } \phi(s,p)=1) \implies \tau(s)=1
$$
- Vollständig (**complete**): Für jede korrekte Aussage existiert ein Beweis
$$
\forall s \in \mathcal{S} : \tau(s)=1 \implies (\exists p \in \mathcal{P} \text{ mit } \phi(s,p)=1)
$$
→ siehe Übung

![[Aufgabe Beweissystem.png]]

---

## Syntax 

- **Alphabet $\Lambda$:** Menge der erlaubten Symbole
- **Formeln $F, G, H$:** Syntaktisch korrekte Zeichenketten

*Erst wenn Syntax korrekt kann die Semantik überprüft werden.*

## Semantik

### Free

Eine Funktion, die alle freien Elemente findet, also die Semantik weist den Formeln Wahrheitswerte zu. Zum Beispiel:

- In $A \land B$ sind $A$ und $B$ frei.
- In $P(x)$ sind $P$ und $x$ frei.
- In $\forall x P(x)$ ist nur $P$ frei. 

### Interpretation und Modell

**Passende Interpretation:** 		jedem freien Element wird ein Wert zugewiesen
**Modell:** 								wahre Interpretaion

**Wahrheitswert einer Formel:** 	$\sigma(\mathcal{A}, F)$ ist 0 oder 1, Schreibweise $\mathcal{A}(F)$
$\mathcal{A}(F)=1 \text{ or } 0$, 							if 1 then A is a model


![[Pasted image 20251202135734.png]]

---

## Relationen

$\models F$ oder $F \models \top$
- Tautologie (gültig), wenn für jede Interpretation wahr

$F \models G$
 - jede Interpretation die ein Modell für $F$ oder $M$ ist, ist auch ein Modell für G (macht wahr)

$F \equiv G \quad \Longleftrightarrow \quad F \models G \text{ und } G \models F$

→ [[Tautologie, Logische Konsequenz.png|siehe Skript]]
## Lemma 6.1

![[Lemma 6.1.png]]
