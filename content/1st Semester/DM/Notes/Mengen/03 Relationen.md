
→ siehe auch 
- [[01 Mengen]] 
- [[04 Spezielle Relationen]]
- [[06 Hasse Diagramme]]
- [[#Wichtige Eigenschaften]]

## Allgemein

- Eine **Relation** ρ zwischen zwei Mengen A und B ist eine Teilmenge von A×B:  
  $ρ ⊆ A × B$
- $a\ ρ\ b$ bedeutet $(a,b) ∈ ρ$.
- $\rho^{*} \stackrel{\mathrm{def}}{=} \cup \ P_{\rho} \quad\text{mit}\quad P_{\rho} = \{ \rho, \rho^{2}, \rho^{3}, \ldots \}$
- [[04 Spezielle Relationen]]

---

## Identitätsrelation

- $id_A = \{(a,a) \mid a ∈ A\}$
- Bedeutung: Jedes Element steht nur zu sich selbst in Relation.  
- Beispiel: $id_{\mathbb{Z}} = \{(0,0), (1,1), (2,2), ...\}$
- Enthalten in jeder reflexiven Relation:  
  $id_A ⊆ ρ$

---

## Inverse

- Definition:  
  $\hat{ρ} = \{(b,a) \mid (a,b) ∈ ρ\}$
- Die Richtung der Paare wird vertauscht.  
- $a\,ρ\,b \iff b\,\hat{ρ}\,a$ 
- Bspw. von „ist Elternteil von“ zu „ist Kind von“
- $\hat{≤} = ≥$

---

## Komposition von Relationen

- Definition: $ρ \circ σ = \{(a,c) \mid ∃b\,((a,b)∈ρ ∧ (b,c)∈σ)\}$
- Bedeutung: Verbindung zweier Relationen über ein Zwischenelement b.
- Achtung, Kreis hat verkehrte Bedeutung als z.B. bei Funktionen. ==Achtung== LLM's machen das oft umgekehrt, also aufpassen
- Bspw.
  - $ρ$: „ist Elternteil von“  
    $σ$: „ist Elternteil von“  
    → $ρ∘σ$: „ist Großelternteil von“
  - Wenn $a ≤ b$ und $b ≤ c$, dann $a ≤ c$  
    → $≤ ∘ ≤ = ≤$

> [!info]
> Kompositionen von Relationen sind **assoziativ** und **nicht kommutativ**

---

## Wichtige Eigenschaften

| Eigenschaft     | Formel             | Bedeutung                                         | Beispiel                                                |
| --------------- | ------------------ | ------------------------------------------------- | ------------------------------------------------------- |
| reflexiv        | $id ⊆ ρ$           | Jedes a steht zu sich selbst                      | $a \leq a$                                              |
| irreflexiv      | $id ∩ ρ = ∅$       | Kein a steht zu sich selbst (z.B. <)              |                                                         |
| symmetrisch     | $ρ = \hat{ρ}$      | Wenn a ρ b, dann b ρ a                            | "verheiratet mit"                                       |
| antisymmetrisch | $ρ ∩ \hat{ρ} ⊆ id$ | Beide Richtungen nur, wenn gleich                 | $a\leq b$ und $b\leq a \Rightarrow a=b$                 |
| transitiv       | $ρ∘ρ ⊆ ρ$          | Wenn a ρ b und b ρ c, dann a ρ c (z.B. <, $\leq$) | $a \le b \ \text{und} \ b \le c \ \Rightarrow\ a \le c$ |

Kann **symmetrisch** und **antisymmetrisch** gleichzeitig sein, z.B. = in $\mathbb{Z}$ 

→ siehe auch [[06 Hasse Diagramme]], inkl. [[06 Hasse Diagramme#Transitive Closure|Transitive Closure]] 

---

## Kongruenz modulo m
	 
  $3 ≡_7 10$, weil $\frac{10}{7}$ hat gleich viel Rest wie $\frac{3}{7}$ 

---


![[Relationseigenschaften.png]]

---

![[Übung 5.pdf]]