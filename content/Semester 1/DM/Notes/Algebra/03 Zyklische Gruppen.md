Es gibt ein einziges Element, aus dem durch wiederholtes Anwenden der Gruppenoperation **alle** Elemente der Gruppe entstehen.

> [!success] Number of Generators  
> The number of generators for the cyclic group $\mathbb{Z}_{49}$ is $\varphi(49)=42$. The number of generators of $\mathbb{Z}_{49}^*$ is $\varphi(42)=12$. An element is a generator, if the gcd of the Gruppenordnung and the element is 1.

> [!example] Number of Subgroups  
> Die Anzahl der Untergruppen entspricht also der Anzahl der Teiler von $\varphi(m)$.
> 
> Beispiel $\mathbb{Z}_{49}^*$
> 1. Ordnung der Gruppe $n = \varphi(49) = 42$
> 2. Finde die Teiler von 42: $\{1, 2, 3, 6, 7, 14, 21, 42\}$
> 3. Es gibt insgesamt **8 Teiler**
> 4. **Ergebnis:** $\mathbb{Z}_{49}^*$ hat genau **8 Untergruppen**
>

## Beispiele

$\mathbb{Z}$ = $〈1〉$
$\mathbb{Z}_{7}^{*}$ = $〈3〉$, also {3,2,6,4,5,1} (mit 3 hoch steigendem n kommt man mod 7 auf alle Restklassen)

- **Lagrange:**
	- H ist eine Untergruppe von G (endlich). |H| teilt |G|.
	- $g^{|G|}=e$ für alle $g \in G$. 
- Die Ordnung des Generators muss gleich der Gruppenordnung sein (bei endlichen Gruppen)
- ord(a) divides |G| for every a ∈ G

- Unter Addition modulo 8 muss für einen Generator $\gcd(k,8) = 1$ gelten.
- Gruppe G ist zyklisch, wenn $g \in G$ existiert mit $〈g〉=G$. Somit $\text{ord(g)}=|G|$. 
- A cyclic group of order n is isomorphic to〈$\mathbb{Z}_{n}$; ⊕〉, [siehe Vorlesung](https://video.ethz.ch/lectures/d-infk/2025/autumn/252-0025-01L/v/EJh3HgV3BDe?t=45m55s)

![[Lagrange.png]]

![[Page 102.png]]
![[Pasted image 20251117194631.png]]

Weiter mit → [[04 Euler]]

![[Übung 9.pdf]]