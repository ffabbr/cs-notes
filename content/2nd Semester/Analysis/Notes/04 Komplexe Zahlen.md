
$$
i^2=-1
$$
$$
\mathbb{C}=\{a+ib\mid a,b\in\mathbb{R}\}
$$

![[Screenshot Übung.png]]
![[Bildschirmfoto 2026-03-01 um 20.50.49.png]]
![[2nd Semester/Analysis/Slides/01 Slides.pdf#page=13]] 

> [!warning] Wichtig
> $lm(z)$ enthält ==NICHT== das i

### Grundrechenarten

![[2nd Semester/Analysis/Slides/01 Slides.pdf#page=17]] 

---
## Gausssche Zahlenebene 

Komplexe Zahlen können wir in der Ebene darstellen, indem wir auf der horizontalen Achse den Realteil und auf der vertikalen Achse den Imaginärteil abtragen.

![[2nd Semester/Analysis/Slides/01 Slides.pdf#page=18]] 

Richtungsvektor vom Ursprung zu diesem Punkt, Länge davon ist Betrag der komplexen Zahl. 

Allternative Beschreibung von komplexen Zahlen in der Ebene:

## Polarform

### Polarkoordinaten

![[2nd Semester/Analysis/Slides/01 Slides.pdf#page=21|01 Slides]]

### Eulersche Formel

![[2nd Semester/Analysis/Slides/02 Slides.pdf#page=1|02 Slides]]
![[2nd Semester/Analysis/Slides/02 Slides.pdf#page=2]]
![[2nd Semester/Analysis/Slides/02 Slides.pdf#page=3]]
![[2nd Semester/Analysis/Slides/02 Slides.pdf#page=4]]


### Umrechnen

![[2nd Semester/Analysis/Slides/02 Slides.pdf#page=5]]
![[2nd Semester/Analysis/Slides/02 Slides.pdf#page=6]]

## Potenzen komplexer Zahlen

![[2nd Semester/Analysis/Slides/02 Slides.pdf#page=7]]
![[2nd Semester/Analysis/Slides/02 Slides.pdf#page=8]]

→ [check that out again](https://claude.ai/share/ea0e079e-969d-4fd4-821a-a03830832dc5)
![[Pasted image 20260301205329.png]]

## Wurzeln komplexer Zahlen

> [!success] Anzahl Wurzeln
> Höchte Potenz ist Anzahl Wurzeln 

![[2nd Semester/Analysis/Slides/02 Slides.pdf#page=9]]
![[2nd Semester/Analysis/Slides/02 Slides.pdf#page=10]]

## Funamentalsatz der Algebra

Jedes (nicht konstante) Polynom von $deg(n)$
1. kann in n Linearfaktoren faktorisiert werden
	- hat somit n Nullstellen (inkl. Vielfachheit)
	- hat maximal n verschiedene Nullstellen
2. hat mindestens eine komplexe Nullstelle

> [!success] Wann nicht max. Anzahl?


![[2nd Semester/Analysis/Slides/02 Slides.pdf#page=11]]
![[2nd Semester/Analysis/Slides/02 Slides.pdf#page=12]]
![[2nd Semester/Analysis/Slides/02 Slides.pdf#page=13]]

## Nullstellen berechnen

z.B. 

$p(z)=z^4 - 6z^3 + 23z^2-34z+26$

Gegeben: $1+i$ ist eine Nullstelle von $p(z)$

1. $1+i$ (gegeben)
2. $1-i$ (komplex konjugiert)

$(z-(1+i)) \cdot (z-(1-i))=z^2-2z+2$, jetzt Polynomdivision: 
   $(z^4 - 6z^3 + 23z^2 - 34z + 26) : (z^2 - 2z + 2) = z^2 - 4z + 13$. 0 Rest. Aus dem Fundamentalsatz der Algebra wissen wir, dass das Polynom die Funktion teilt, somit muss 0R. Lösungen der quadratischen Gleichung: $2 \pm 3i$

3. $2 + 3i$
4. $2 - 3i$

---

> [!success] 
> $\sqrt{i}$ berechnen: $z^2=i$

---

→ [[05 Winkelfunktionen]]
