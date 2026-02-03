## Normalformen

> [!abstract] Literal
> Ein Literal ist eine Formel (oder die negation einer Formel).  

### CNF und DNF

**CNF:** Konjunktion von Disjunktionen von **Literalen**
$$F = (A \lor B) \land (C \lor \neg D)$$
**DNF:** Disjunktion von Konjunktionen von **Literalen**
$$F = (A \land B) \lor (C \land \neg D)$$


**Beispiel**

- $A ∧ ¬ B ∧ ¬C$ ist sowohl in CNF (jede Klausel besteht aus einem Literal) und DNF (alles ist eine Klausel)
- $A \lor (B \lor C)$ ist sowohl in CNF und in DNF, da $A \lor (B \lor C) \equiv A \lor B \lor C$ 


![[Bildschirmfoto 2025-12-10 um 19.15.45.png]]
![[1st Semester/DM/Skript.pdf#page=151|Skript]]