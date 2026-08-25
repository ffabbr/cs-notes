## Von Relationen zu Funktionen 

![[Definition einer Funktion durch Relationen.png]]

## Definition

Eine Funktion $f$ ist …

- **injektiv**, falls  
  $\forall a, a' \in A: \; (f(a) = f(a')) \rightarrow (a = a')$
  *es zeigen nie zwei Elemente aus A auf das gleiche b in B*
  *jeder Output ist unique* 

- **surjektiv**, falls  
  $\forall b \in B \; \exists a \in A: \; f(a) = b$
  *jedes b in B wird durch mindestens ein a in A gemapped*

- **bijektiv**, falls $f$ surjektiv und injektiv ist.
  *jedes b in B wird durch genau ein a in A gemapped*

Betrag |$x$| ist nicht injektiv, da zum Beispiel für x = -3 und x = 3 ==beide== auf 3 abgebildet werden. ist aber surjektiv, da die 3 gemapped wurde. 

$f(x)=2x$ ist nicht surjektiv, da z.B. die 3 von keinem x gemapped wird. 

---

**Totaldefiniert**: jedes a aus A wird auf mindestens ein b in B gemapped
**Wohldefiniert**: jedes a aus A mapped maximal auf ein b in B

---

## Kardinalität

- $f: A\to B$ ist injektiv, $|A| \leq |B|$
- $f: A\to B$ ist surjektiv, $|A| \geq |B|$
- $f: A\to B$ ist bijektiv, $|A| = |B|$

Kardinalität ist für unendliche Mengen nicht definiert, geht also nur für endliche Mengen

---

## Schreibweise:  

$g \circ f$ ist Funktion mit $(g \circ f)(a) = g(f(a))$ für Funktionen $f, g$.

> Achtung, ○ hat die verkehrte Bedeutung hier im Vergleich zu Relationen

---

$A^B$ ist die Menge aller Funktionen $f : A \to B$.

---

## Beispiele

### Surjektive Funktion f: $\mathbb{N}$ → $\mathbb{Z}$ 

$f(n) =$ $(-1)^n$ * $\lceil n/2 \rceil$ 

$f(0) = 0$ Wenn abgerundet, dann nicht injektiv, trotzdem surjektiv
$f(1) = -1$
$f(2) = 1$
$f(3) = -2$
$f(4) = 2$

… und so weiter

