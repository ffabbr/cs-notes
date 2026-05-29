
Gegeben eine Punktmenge, finde kleinsten Kreis der alle Punkte umschliesst. Die smallest enclosing disk ist eindeutig. 

Die smallest enclosing disk lässt sich mit 3 Punkten bestimmen. 

> [!success] Notation
> - $C(P)$: Randlinie
> - $C^\bullet(P)$: Kreisfläche

## Brute-Force Algorithmus

$O(n^4)$

for all subsets von P mit 3 Elementen ($\binom{n}{3} \leq O(n^3)$)
	1. bestimme $C(Q)$ ($O(1)$)
	2. wenn alle Punkte aus P in der Kreisfläche $C^\bullet(Q)$ sind ($O(n)$, return $C(Q)$

## Randomised Algorithmus

$O(n \log n)$
Las-Vegas

1. Kopiere P
2. wiederhole
	1. wähle 11 Punkte at random ($O(n)$)
	2. determine C dieser Punkte ($O(1)$)
	3. if $P \subseteq$ diese Punkte ($O(n)$), return, sonst ==verdopple die Punkte ausserhalb von C==


![[Lemma328.png]]

→ [[Bildschirmfoto 2026-05-28 um 20.49.30.png|Beweis]]
