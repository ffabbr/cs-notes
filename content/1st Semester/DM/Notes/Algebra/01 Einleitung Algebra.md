## Quick Facts

- Eine Algebra besteht aus einer Menge G und einer Operation $*$ die aus G nach G formt. Eine Algebra ist somit unter ihrer Operation $*$ ==abgeschlossen==. 
- $a^n$ heißt hier, dass wir n mal a mit a verknüpfen, also die Operation der Gruppe anwenden
- Wenn nicht genauer definiert nehmen wir als Operation die Addition (modulo something)

- **Monoid**: $〈G,*,e〉$
	- Algebra
	- Operation $*$ ist ==assoziativ== (G1) 
	- gibt ein ==neutrales Element== $e \in G$, $a * e = e * a = a \quad \forall a \in G$ (G2)
	- Beispiel: $〈\mathcal{P}(\mathbb{N}); \cap〉$ ist ein Monoid, da die Union assoziativ ist, neutrales Element ist $\mathbb{N}$
- **Gruppe**: $〈G,*,\hat{},e〉$ 
	- Monoid
	- gibt ein ==inverses Element== für jedes $a \in G$ existiert $\hat{a} \in G$, so dass $a * \hat{a} = \hat{a} * a = e$ (G3)
	- → [[03 Zyklische Gruppen]]
- **Abelsche Gruppe** (Abelian):
	- Gruppe
	- ==Kommutativität==

## Ordnung 

→ siehe [[02 Ordnung]]

## Homomorphism and Isomorphism
### Homomorphism

$\psi(a \circ b) = \psi(a) \ast \psi(b)$

*Es ist egal, ob wir zuerst die Operation und dann das mapping machen, oder zuerst das mappen und dann die Operation.* 

![[Lemma 5.5.png]]
 
### Isomorphismus

Ein Homomorphismus der zusätzlich eine **Bijektion** ist, also: 

- injektiv ($\psi(a) = \psi(b) \;\Rightarrow\; a = b$)
- surjektiv ($\text{für jedes } h \in H \text{ gibt es ein } g \in G \text{ mit } \psi(g) = h$)

Für jedes $n \in \mathbb{Z}^+$ ist jede zyklische Gruppe der Ordnung $n$ isomorph zu $\mathbb{Z}_n$.
Jede unendliche zyklische Gruppe ist isomorph zu $\mathbb{Z}$.

1. Homomorphismus-Eigenschaft: $\phi(g_1 \cdot g_2) = \phi(g_1) \cdot \phi(g_2)$
2. Bijektivität:
    $\phi$ ist eine eineindeutige (injektive) und surjektive (onto) Abbildung.

→ [how to proof an isomorphism](https://discmath.ch/content/ch5/group-theory#steps-to-prove-an-isomorphism)
→ [great Intuition-based explanation](https://discmath.ch/content/ch5/group-theory#homomorphisms--isomorphisms)

## Untergruppen (Subgroups)

Eine Teilmenge (subset) $H \subseteq G$ einer Gruppe ist eine Subgruppe, wenn 

- die binäre **Operation** auf Elemente der Teilmenge (Untergruppe) ist in der Untergruppe **abgeschlossen**
- das **neutrale Element** ist in der Untergruppe
- für alle Elemente in der Untergruppe ist ihre **Inverse auch in der Untergruppe**

2 triviale Teilmengen (Untergruppen) der Gruppe $G$: 

- $\{e\}$
- G selbst

> [!success] Beispiel  
> **Wie viele Untergruppen hat $\langle \mathbb{Z}_4, +\rangle$?**  
>  
> **Schnell, zyklisch (Lagrange)**  
> 1. Da zyklische Gruppe: gibt so viele Untergruppen, wie Teiler der Gruppenordnung.  
> 2. Teiler von 4 sind 1, 2, 4, gibt also 3 Untergruppen.  
>  
> **Manuell (Lagrange)**  
> 1. Lagrange: Ordnung der Untergruppe teilt die Gruppenordnung.  
> 2. Gruppenordnung ist 4, also Ordnung von Untergruppen 1, 2 oder 4.  
>    1. Ordnung 1: {0}  
>    2. Ordnung 2: siehe 2+2=0, also {0,2}  
>    3. Ordnung 4: {0,1,2,3}  
> 3. Inverse muss auch in der Untergruppe sein, also wäre {2} allein nicht erlaubt.

## Direct Product

Aus mehreren Gruppen $G_{1}, G_{2}, \dots, G_{n}$ bauen wir eine neue Gruppe, deren Elemente Toupel $a_{1}, \dots, a_{n}$ sind ($a_{i} \text{ aus } G_{i}$). Erste Komponenten werden mit der Operation von $G_{1}$ verknüpft, die zweiten mit $G_{2}$, etc. 

**Beispiel:** 

$G_{1}$ = $〈\mathbb{R}, +〉$
$G_{2}$ = $〈\mathbb{R_{>0}}, *〉$ 

In $\mathbb{R} \times \mathbb{R}_{>0}$ sieht ein Element so aus $(a, b) \text{ mit } a\in\mathbb{R},\; b\in\mathbb{R}_{>0}$.

**Operation**: $(a, b) \star (c, d) = (a + c,\; b * d)$
**Neutrales Element:** $(0,1)$
**Inverses**: $\left( -a, \frac{1}{b} \right)$ (einmal das Inverse von a in $G_{1}$ und einmal das von a in $G_{2}$)

![[Direct Products of Groups.png]]

![[Übung 8.pdf]]