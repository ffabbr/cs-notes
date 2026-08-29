## Introduction

Ableitungen der Form
$$
F \vdash G
$$

Oder:
$$
\{F_1, \dots, F_k\} \vdash G
$$
## Ableitung
$\vdash_R$ soll $\vDash$ imitieren nach festen Regeln R
$$
F \vdash_R G
$$
z.B.
$$
\{F, G\} \vdash_R (F \land G)
$$

- **Schrittweise** mehr Formeln aus einer Menge $M$ von gegebenen Formeln ableiten
- **Kalkül** ist eine (endliche) Menge von **Regeln**.

## Schreibweise

$$
M \vdash_K F
$$

## Eigenschaften

**==Sound==** (man kann nur Wahres ableiten)
$$
M \vdash_K F \implies M \models F
$$

**==Vollständig==** (Completeness):
$$
M \models F \implies M \vdash_K F
$$

### Beispiele für **Sound**

$$
\{F, ¬ F \} \vdash_R G
$$
(die LHS ist immer falsch, also gilt die logische Implikation immer)
$$
\{F \lor G, ¬ G\} \vdash_R F \lor H
$$
$$
\emptyset \vdash_R (F \to G) \lor (G \to F)
$$
---

## Resolutionskalkül

> [!abstract] Clause
> A clause is a set of literals.

**Quick-Facts**
- Ziel: leere Menge herleiten, somit gezeigt, dass Formel unerfüllbar
- $\text{F ist unerfüllbar} \Longleftrightarrow K(F) \vdash_{\text{res}} \emptyset$ 
- Resolutionskalkül ist korrekt

**Aufgabe – Beweise dass F unerfüllbar ist**
1. Bringe F in CNF
2. Wandle $F_{\text{CNF}}$ in Mengen um (jede Klausel ist eine Menge)
3. Resolutionsschritt so lange ausführen bis wir $\{\}$ hergeleitet haben

**Logische Folgerung zeigen**

![[Bildschirmfoto 2025-12-16 um 15.25.13.png]]

![[Lemma 6.3.png]]

![[Resolutionskalkül Schritt.png]]


![[Übung 11.pdf#page=6|Übung]] 