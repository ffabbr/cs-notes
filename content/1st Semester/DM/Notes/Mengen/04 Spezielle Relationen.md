
1. [[#Äquivalenzrelationen]] (reflexiv, symmetrisch, transitiv)
2. [[#Ordnungsrelationen]] (reflexiv, antisymmetrisch, transitiv)
3. [[05 Posets]]

## Äquivalenzrelationen

1. reflexiv
2. symmetrisch
3. transitiv

(siehe [[03 Relationen#Wichtige Eigenschaften|Relationseigenschaften]])

z.B: $id_{A}$, $\equiv_{m}$

Der Schnitt einer Äquivalenzrelation ist wieder eine Äquivalenzrelation, z.B: $\equiv_{3} \cap \equiv_{5} \; = \; \equiv_{15}$ 

Beweise, z.B: 

![[Beweis einer Äquivalenzrelation.png]]

## Äquivalenzklassen

Eine **Äquivalenzklasse** entsteht, wenn man eine Menge von Dingen (z. B. Zahlen, Personen, Objekten) nach einer bestimmten Regel (**Äquivalenzrelation**) in Gruppen einteilt. Zwei Elemente gehören **zur selben Klasse**, wenn sie nach dieser Regel „gleich“ sind. 

z.B. 
$$[0]_{\equiv_{3}}=\{\dots, -6, -3, 0, 3, 6, \dots\}$$
### Partitionen

Sie bilden eine Partition, da 

1. Jedes Element gehört genau zu einer dieser Klassen.
2. Zwei Äquivalenzklassen sind entweder identisch oder disjunkt.
3. Wenn man alle Klassen zusammenfasst, hat man wieder die Menge.

$$[a]_\Theta = \{\, b \in A \mid b \,\Theta\, a \,\}$$

Bsp.: $A = \mathbb{Z}$, $\Theta = \equiv_5$, $[0]_\Theta = \{0, -5, 5, -10, 10, \ldots\}$, $[2]_\Theta = \{2, -3, 7, -8, 12, \ldots\}$, $[5]_\Theta = [0]_\Theta$


### Quotientenmenge 

Die Quotientenmenge A/θ ist die Menge **aller Äquivalenzklassen**.

Beispiel:

$$\mathbb{Z}/\equiv_{3}=\{[0],[1],[2]\}$$

Definittion: Die Menge aller Äquivalenzklassen (Quotientenmenge) einer Äquivalenzrelation $\theta$ ist
$$A / \theta \overset{\text{def}}{=} \{ [a]_\theta \mid a \in A \}$$

## Ordnungsrelationen

*partial order relation*

1. reflexiv
2. antisymmetrisch
3. transitiv

(siehe [[03 Relationen#Wichtige Eigenschaften|Relationseigenschaften]])

*z.B. bei Teilbarkeits-Hasse-Diagrammen, siehe [[Hasse, Teilbarkeit.png]], teilt ein oberes Element ja nicht das untere, somit nicht symmetrisch. Da das überall gilt, also antisymmetrisch und somit eine Ordnungsrelation.*

## Posets

siehe [[05 Posets]]