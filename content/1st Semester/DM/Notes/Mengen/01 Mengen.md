
eng. Sets

Untermenge: $\subseteq$
Element von: $\in$ 

→ siehe auch [[03 Relationen]] und [[02 Zählbarkeit]]

## 1. Element von (∈)


$$
  3 \in \{1, 2, 3, 4\}
$$

  *3 ist ein Element der Menge {1, 2, 3, 4}.*

---

## 2. Teilmenge (⊆)


$$
  \{1, 2\} \subseteq \{1, 2, 3\}
$$

bedeutet: *Jedes Element von {1, 2} ist auch in {1, 2, 3} enthalten.*

Eine *echte Teilmenge* bedeutet, dass **nicht** die gleichen Elemente enthalten sein können. 

---

## 4. Beispiel zur Veranschaulichung

$$
A = \{1, 2, 3\}, \quad B = \{A, 4\}
$$

Dann gilt:

- $1 \in A$ (weil 1 ein Element von A ist)
- $A \in B$ (weil A selbst ein Element in B ist)
- $A \subseteq A$ (jede Menge ist Teilmenge von sich selbst)
- $A \not\subseteq B$ (weil 1, 2, 3 nicht alle in B enthalten sind)
- $\{1,2\} \subset A$, aber $\{1,2,3\} \not\subset A$


---

## 5. Toupel

Basically eine Menge mit bestimmter Reihenfolge. 

$$
(a,b) \;\overset{\text{def}}{=}\; \text{\{\{a\}, \{a, b\}\}}
$$
#### Beispiele 
- $\{ (\emptyset, \emptyset) \} \subseteq \{\emptyset\} \times \{\emptyset\}$
- $(\emptyset, \emptyset) \in \{\emptyset\} \times \{\emptyset\}$

---

## Sonstiges

### Russells Paradox

Definiere die Menge  
$$
R = \{\, x \mid x \notin x \,\}
$$  
→ \(R\) enthält alle Mengen, die sich **nicht selbst enthalten**.

Frage: Gilt $R \in R$?

- Falls $R \in R$: Dann enthält sich $R$ ja selbst, aber laut Definition dürfen in $R$ ja nur Elemente sein, die sich selbst nicht enthalten.
- Falls : $R \notin R$: Dann enthält $R$ sich nicht selbst, aber laut Definition müsse $R$ ja dann $R$ enthalten.

→ **Widerspruch.**

### Potenzmenge

*(Power Set)*

Die Potenzmenge ist die Menge aller Teilmengen. 

$$\mathcal{P}(A) \;\stackrel{\text{def}}{=}\; \{\, S \mid S \subseteq A \,\}$$
Beispiel: 
$$
\mathcal{P}(\{a, b, c\}) = \{\emptyset, \{a\}, \{b\}, \{c\}, \{a, b\}, \{a, c\}, \{b, c\}, \{a, b, c\}\}.
$$


Eine endliche Menge $A$ enthält $2^{|A|}$ Teilmengen. Wenn $\emptyset$ Teil der Menge ist wird es nicht in $|A|$ mitgezählt. Die Potenzmenge $\mathcal{P}(A \times A)$ beinhaltet $2^{(n^2)}$ Elemente.

### Triviale Teilmengen 

1. Die Menge selbst ist immer eine Teilmenge
2. Die leere Menge $\emptyset$ ist immer eine Teilmenge (aber *nicht* Element jeder Menge)

---

### Das Kartesische Produkt

Die Menge aller Paare, bei denen das erste Element aus $A$ und das zweite Element aus $B$ kommt. 

Definition: 

$$
A \times B = \{ (a, b) \mid a \in A \land b \in B \}
$$

Beispiele: 
- $\emptyset \times A = A \times \emptyset = \emptyset$
- $\{1, 2\} \times \{3, 4\} = \{(1,3), (1,4), (2,3), (2,4)\}$
- $\{ (\emptyset, \emptyset) \} \subseteq \{\emptyset\} \times \{\emptyset\}$
- $(\emptyset, \emptyset) \in \{\emptyset\} \times \{\emptyset\}$

Anzahl Elemente im Kartesischen Produkt: $m\cdot n$ (Produkt der Anzahl der Elemente (Kardinalität) der beiden Mengen)

*Außerdem:*

 $\boxed{|A \times B| = |A| \cdot |B|}$

---

### Sonstiges

Kardinalität = Anzahl der Elemente

---

![[Theorem 3.4.png]]