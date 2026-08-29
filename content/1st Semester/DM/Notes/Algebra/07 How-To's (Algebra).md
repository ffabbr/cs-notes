
## Untergruppen

- Die Untergruppen erben die Operationen von der parent Gruppe

### Liste Untergruppen

Liste alle Untergruppen von $\langle \mathbb{Z}_{14}, \oplus_{14} \rangle$. 

1. $\mathbb{Z}_{14}$ hat 14 Elemente (0–13)
2. Langrange: Ordnung der Untergruppe teilt die Gruppenordnung
3. 14 wird geteilt durch 1, 2, 7, 14
4. 2 Möglichkeiten
	1. **Option A**: wir rechnen für jeden dieser Teiler $a$, $\frac{14}{a}$ und bekommen somit 4 Generatoren für die 4 Untergruppen, müssen die nur mehr notieren. Also $\langle 14 \rangle=$ {0}, $\langle 7 \rangle=$ {0,7}, $\langle 2 \rangle=$ {0,2,4,6,8,10,12}, $\langle 1 \rangle=\mathbb{Z}_{14}$. Achtung modulo. 
	2. **Option B**: Die trivialen Untermengen sind {e}, also hier {0}, und die Gruppe selbst, also $\mathbb{Z}_{14}$. Es fehlen noch zwei Gruppen, per Lagrange, einmal mit 2 Elementen, einmal mit 7. Neutr. Element 0 muss immer Teil sein, dann anschauen, z.B. nur gerade Zahlen, Teiler 7, etc.

### Anzahl Untergruppen

Wie viele Untergruppen hat $\langle \mathbb{Z}_{4}, \oplus_{4} \rangle$?

- **Wenn Zyklisch** (schneller)
	1. Gibt so viele Untergruppen, wie Teiler der Gruppenordnung 
	2. Teiler von 4 sind 1,2,4, gibt also 3 Untergruppen
- **Manuell (Lagrange)**
	1. Lagrange: Ordnung der Untergruppe teilt die Gruppenordnung. 
	2. Gruppenordnung ist 4, also Ordnung von Untergruppen 1, 2, oder 4
		1. Ordnung 1: {0} (trivial)
		2. Ordnung 2: siehe 2+2=0, also {0,2} (jede Gruppe muss das neutrale Element enthalten, abgeschlossen)
		3. Ordnung 4: {0,1,2,3} (trivial)
	3. Inverse muss auch in der Untergruppe sein, also z.B. {2}
## Polynome

### Liste Nullteiler 

Liste alle Nullteiler von $R = \text{GF}(3)[x]_{x^2+2x}$:

1. m(x) Faktorisieren: $m(x) = x \cdot (x+2)$
2. Vielfache bilden: Da $m(x)$ Grad 2 hat, suchen wir nur Nullteiler mit Grad 1. Wir multiplizieren also nur mit Konstanten, nicht mit $x$, da wir sonst den Grad 2 überschreiten würden.
	- **ausgehend von $x$:**
	    1. $1 \cdot x = \mathbf{x}$
	    2. $2 \cdot x = \mathbf{2x}$
	- **ausgehend von $(x+2)$:**
	    1. $1 \cdot (x+2) = \mathbf{x+2}$
	    2. $2 \cdot (x+2) = 2x + 4 \quad \xrightarrow{\text{mod } 3} \quad \mathbf{2x+1}$
3. Also, unsere Nullteiler sind $\{x, \, 2x, \, x+2, \, 2x+1\}$


### Elemente von A

Determine all elements of $\text{GF}(3)[x]_{x^2+2}$ 

1. Grad muss $\leq$ 1 sein, da kleiner als $x^2$, Koeffizienten müssen sein 0,1,2, da $\mathbb{Z_{3}}$ 
2. Grad muss also $-\infty$, 0 oder 1 sein. 
3. Alle Kombinationen, auf modulo achten: 0, 1, 2, x, 2x, x+1, x+2, 2x+1, 2x+2

### Elemente von A*

Determine all elements of $\text{GF}(3)[x]_{x^2+2}^*$

- Erst mal nur A berechnen, so wie oben. Wir bekommen 0, 1, 2, x, 2x, 2x+1, 2x+2
- A* bedeutet teilerfremd, also zerlegen wir $m(x)=x^2+2$ in $(x+2)(x+1)$, und streichen alle Vielfache der Faktoren davon aus der Liste oben (achtung modulo). 0 ist nie Teil von A*. Übrig bleiben die teilerfremden Elemente (keine gemeinsamen Faktoren). Auf modulo achten!
- Wir bekommen 1, 2, x, 2x

### Inverse berechnen

Berechne die Inverse von $x+4$ in $R^* = \mathbb{Z}_5[x]^*_{x^2+1}$.

1. Wir suchen ein Polynom in der Form $(ax+b)$, sodass $(x+4)(ax+b)=1$
2. $(x+4)(ax+b)=ax^2+bx+4ax+4b=ax^2 + (4a+b)x + 4b$
3. Wir müssen das $x^2$ wegbringen. In dem Ring gilt $x^2+1 = 0$. Ginge mit Polynomdivision, aber einfacher $a \cdot (x^2+1)$ abziehen:
$$
\begin{align}
[ax^2 + (4a+b)x + 4b] - [ax^2 + a]  \\
= \underbrace{(ax^2 - ax^2)}_{0} + (4a+b)x + (4b - a) \\
=(4a+b)x + (4b-a)
\end{align}
$$
4. $(4a+b)x + (4b-a)$ soll ja 1 ergeben, also $0x+1$ also muss gelten $4a + b = 0$ und $4b - a = 1$. Das Gleichungssystem kann man ja einfach lösen (Achtung modulo, negative Zahlen also immer umdrehen)
5. Lösung: $2x + 2$

