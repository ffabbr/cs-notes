
## Take-aways

- z.B. $\mathbb{N}$ oder $\mathbb{Q}$ abzählbar, weil du beginnen könntest, alle Elemente aufzuzählen. Bei $\mathbb{R}$ z.B. geht das nicht.
- Unendliche Mengen
	- **Equinumerous**, wenn es eine **[[07 Funktionen|Bijektion]]** gibt, Zeichen $\sim$ 
		- A und B sind **gleich mächtig**
	- B dominiert A, wenn es eine **[[07 Funktionen|Injektion]]** von A nach B gibt, Zeichen $\preceq$ 
	- *countable*, wenn equinumerous zu $\mathbb{N}$ 
	- $\sim$ ist eine Äquivalenzrelation
- Endliche Mengen
	- $A \sim B$, wenn $|A|=|B|$
	- Endliche Mengen sind immer countable

## Quick-Checks

- $\mathbb{N} \times \{1, 2, 3\}^\infty$, **nicht abzählbar**
- $P(\mathbb{N})$, **nicht abzählbar**
- $\{1\}^\infty$, abzählbar

---

## Arten von Mengen:

1. Endliche Mengen {1,2}
2. Unendliche abzählbare Mengen ($\mathbb{N}, \space \mathbb{Z}$, $\mathbb{N} \times \mathbb{N}$, endliche Bitstrings: $\{0,1\}^*$ )
3. Unendliche überabzählbare Mengen: $\{0,1\}^{\infty}$, $[0,1]$ und $\mathbb{R}$

$\{0,1\}^*$ ist abzählbar, damit gemeint sind alle endlichen Folgen aus 0 und 1, also *0, 1, 01, 10, 001, 1110*
$\{0,1\}^{\infty}$ ist unabzählbar, damit gemeint sind alle unendlichen Folgen aus 0 uns 1, also *0101010101…* unendlich halt

---

## Beweise

### Beweis, Abzählbarkeit der Menge S:

* Finde abzählbare Menge A, z.B. $\mathbb{N}$
* Muss mit Lemma begründet werden z.B. $\mathbb{N} \times \mathbb{N}$ ist abzählbar
* Finde injektive Funktion $f: S \rightarrow A$
* Beweise, dass f injektiv ist
* Beweise, dass $f(s) \in A$ gilt für alle $s \in S.$

### Beweis, dass S überabzählbar ist:

* Finde überabzählbare Menge B, z.B. $\{0,1\}^\infty$ (vom TA empfohlen)
* Finde injektive Funktion $f: B \rightarrow S$
* Beweise, dass f injektiv ist
* Beweise, $f(b) \in S$ für alle $b \in B$

### Beweise equinumerity (Gleichmächtigkeit): A ~ B

* Finde bijektive Funktion $f: A \rightarrow B$
* Beweise, dass f injektiv und surjektiv ist

	→ Aufgabe *Zig* aus der Übung (scroll down)

![[Übung 6.pdf]]


---


## Überabzählbarkeit

Cantors Diagonalisierung

![](https://youtu.be/renajBmw-Y0?si=MjwHxVtpDM_zg2Oy&t=413)