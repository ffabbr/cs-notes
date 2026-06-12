
> [!info]- Rechenregeln
> - $\log(a \cdot b) = \log(a) + \log(b)$

## Logik

- $\exists!$ es gibt genau eins
- $A \implies B$  A ist hinreichend und B ist notwendig
- $A \implies B$ ist gleichbedeutend zu $¬ B \implies ¬ A$ 

## Mengen

- $\subset$ ist hier gleichbedeutend mit $\subseteq$, die echte Teilmenge ist $\subsetneq$ 
- $X \subset Y$, dann ist das **Komplement** $X^c := \{y \mid y \in Y \wedge y \notin X\}$ 

- $\mathbb{N}=\{1,2,3, \dots\}$  
- $\mathbb{R} = (-\infty, \infty)$ 

## Intervalle

- **Intervall offen** $(a,b)$
- **Intervall abgeschlossen** $[a,b]$ oder $[a, \infty), (-\infty, \infty), \text{etc.}$. 
  das komplement einer offenen menge ist abgeschlossen
- **Intervall halboffen**

- **Intervall beschränkt**: a, b endlich
- **Intervall kompakt**: abgeschlossen und beschränkt

- eine obere (untere) Schranke einer Teilmenge X ist eine Zahl die grösser gleich (kleiner gleich) ist, als alle Zahlen in der Teilmenge. Gibt viele.

- **Supremum** $\text{sup}(X)$: kleinste obere Schranke. Unique if exists.
- **Infimum** $\text{inf}(X)$: grösste untere Schranke. Unique if exists.

- ein Maximum (Minimum) einer Menge ist das grösste bzw. kleinste Element der Menge. Unique if exists.
### Beispiel

$X=[-2,1)$
- Minimum: -2
- Supremum: 1

$X=\{\}$
- Supremum: $-\infty$ 

![[Bildschirmfoto 2026-03-17 um 17.12.33.png]]
![[Bildschirmfoto 2026-03-17 um 17.12.53.png]]



![[Bildschirmfoto 2026-02-17 um 23.11.30.png]]

---

## Axiome

Axiome der Addition und Multiplikation: 
- Assoziativität, neutrales Element, Inverses, Kommutativität

### Ordnungsaxiome
- Reflexivität, Transitivität, antisymmetrie, Totalität
- $\mathbb{R}$ und $\mathbb{Q}$ 

**==Ordnungsvollständigkeit==**:
- Let $A,B \subseteq \mathbb{R}$, nicht leer, und gilt $\forall a \in A, \forall b \in B: a \leq b$. Es gibt ein c: 
	- $\forall a \in A: a \leq c$ 
	- $\forall b \in B: c \leq b$
- gilt für $\mathbb{R}$, **nicht** für $\mathbb{Q}$ 
- Beweis siehe Slides

![[Bildschirmfoto 2026-03-01 um 13.16.01.png]]

## Beweis mit dem Ordnungsvollständigkeitsaxiom

![[2nd Semester/Analysis/Slides/01 Slides.pdf#page=1|01 Slides]]
![[2nd Semester/Analysis/Slides/01 Slides.pdf#page=2|01 Slides]]
![[2nd Semester/Analysis/Slides/01 Slides.pdf#page=3|01 Slides]]
![[2nd Semester/Analysis/Slides/01 Slides.pdf#page=4|01 Slides]]