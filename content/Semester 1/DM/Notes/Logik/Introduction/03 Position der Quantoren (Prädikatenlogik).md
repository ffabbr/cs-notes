In der Prädikatenlogik kann es einen entscheidenden Unterschied machen, ob ein Existenzquantor $\exists$ **innerhalb** oder **außerhalb** einer Implikation steht.

---

### Formel C:
$$
\forall x\;\bigl(P(x)\rightarrow \exists y\,Q(x,y)\bigr)
$$

**Bedeutung:**  
Für jedes $x$ gilt: Wenn $P(x)$ wahr ist, dann gibt es ein $y$, sodass $Q(x,y)$ gilt.  
Das $y$ darf also von $x$ abhängen und muss nur existieren, wenn $P(x)$ tatsächlich gilt.

**Beispiel:**  
- $P(x):\ \text{``x ist Student.''}$  
- $Q(x,y):\ \text{``x hat die E-Mail-Adresse }y\text{.''}$  
Formal bedeutet die Aussage:
$$
\forall x\;\bigl(P(x)\rightarrow \exists y\,Q(x,y)\bigr)
$$
Dass jeder Student mindestens eine E-Mail-Adresse besitzt.

---

### Formel D:
$$
\forall x\;\exists y\;\bigl(P(x)\rightarrow Q(x,y)\bigr)
$$

**Bedeutung:**  
Für jedes $x$ gibt es ein $y$, sodass gilt: Wenn $P(x)$ wahr ist, dann $Q(x,y)$.  
Hier wird das $y$ unabhängig davon gewählt, ob $P(x)$ gilt oder nicht.

**Beispiel:**  
Mit denselben Prädikaten heißt die Formel:
$$
\forall x\;\exists y\;\bigl(P(x)\rightarrow Q(x,y)\bigr)
$$
Dass für jede Person $x$ ein $y$ existiert, sodass: falls $x$ Student ist, dann hat $x$ die E-Mail-Adresse $y$.  
Da die Implikation für Nicht-Studenten immer wahr ist, können für Nicht-Studenten beliebige $y$ gewählt werden; die Formel kann also wahr sein, obwohl tatsächlich niemand eine E-Mail-Adresse hat.

---

### Vergleich

| Formel                                             | Struktur                                      | Bedeutung                                          |
| -------------------------------------------------- | --------------------------------------------- | -------------------------------------------------- |
| $\forall x\,(P(x)\rightarrow \exists y\,Q(x,y))$ | Existenzquantor **innerhalb** der Implikation | relevant nur, wenn $P(x)$ gilt                   |
| $\forall x\;\exists y\;(P(x)\rightarrow Q(x,y))$ | Existenzquantor **außerhalb** der Implikation | gilt für alle $x$, auch wenn $P(x)$ nicht gilt |

---

### Also

Die beiden Formeln sind nicht äquivalent:
$$
\forall x\,(P(x)\rightarrow \exists y\,Q(x,y)) \;\not\equiv\; \forall x\;\exists y\;(P(x)\rightarrow Q(x,y))
$$

In der ersten Formel muss ein $y$ nur existieren, wenn $P(x)$ gilt.  
In der zweiten Formel muss es für jedes $x$ ein $y$ geben, auch wenn $P(x)$ nicht gilt.  
Der Unterschied liegt im Geltungsbereich (Scope) des Existenzquantors.
