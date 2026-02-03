
Ein Paar (A,$\preceq$) nennt man **poset** (partially ordered set).

### Beispiel

$A = \mathbb{Z}, \ \preceq = \le$

- **Reflexiv:** $a \le a$
- **Antisymmetrisch:** $a \le b \ \text{und} \ b \le a \Rightarrow a = b$
- **Transitiv:** $a \le b \ \text{und} \ b \le c \Rightarrow a \le c$

(siehe [[03 Relationen#Wichtige Eigenschaften|Relationseigenschaften]])

(totally ordered bedeutet zusätzlich $\forall a,b \in A:\ a \le b \ \text{or}\ b \le a$)

Also ist $(\mathbb{Z}, \le)$ ein Poset. 

$\preceq = <$ wäre **nicht reflexiv**, also würde das nicht gelten. 

### Beispiel Lexografische Ordnung

Wie im Wörterbuch (wie bei „abc“ < „abd“).

Formal:

$$
(a_1, b_1) \le_{\mathrm{lex}} (a_2, b_2)
\;\;\Longleftrightarrow\;\;
(a_1 \prec a_2)
\;\text{ oder }\;
(a_1 = a_2 \;\text{ und }\; b_1 \sqsubseteq b_2)$$
- Erst nach dem **ersten Element** vergleichen.  
- Nur wenn das gleich ist, entscheidet das zweite.

Eigenschaften
- Reflexiv 
- Antisymmetrisch
- Transitiv  

Also → Lexikographische Ordnung ist ein Poset

### Deckung

**Definition 3.26** In a poset (A; ≼) an element b is said to cover an element a if a ≺ b and there exists no c with a ≺ c and c ≺ b (i.e., between a and b). 

**Example 3.41** In a hierarchy (say of a company), if a ≺ b means that b is superior to a, then b covers a means that b is the direct superior of a.

### Geordnet

- In einem Poset (A; ≼) sind 2 Elemente a and b vergleichbar, wenn a ≼ b oder b ≼ a
- Totalgeordnet, wenn alle Elemente in (A; ≼) vergleichbar sind

**Example 3.39**. (Z; ≤) and (Z; ≥) are totally ordered posets (or simply totally ordered sets), and so is any subset of Z with respect to ≤ or ≥. For instance, ({2, 5, 7, 10}; ≤) is a totally ordered set. 

**Example 3.40.** The poset (P(A); ⊆) is not totally ordered if |A| ≥ 2, nor is the poset (N; |).

**Definition 3.30** A poset (A; ≼) is well-ordered if it is totally ordered and if every non-empty subset of A has a least element.

### Hasse-Diagramme

Siehe [[06 Hasse Diagramme]]

---

## Sonstiges

![[Relations-Beweis mit Widerspruch.png]]