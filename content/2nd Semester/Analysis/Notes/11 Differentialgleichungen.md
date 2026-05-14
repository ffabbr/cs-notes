
*Statt x zu finden, wollen wir eine Funktion bestimmen, die Eigenschaften erfüllt.*

- **Ordnung**: höchste Ableitung
- **homogen**: $s(x)=0$ 
	- gebe alle Terme die die Funktion beinhalten auf eine Seite, und alle Terme die Unabhängig von dieser Funktion sind auf die andere
	- wenn die Seite mit unabhängigen Termen = 0, dann homogen
- **linear**: gesuchte Funktion und alle Abelitungen kommen nur in der ersten Potenz vor und nicht miteinander multipliziert; Koeffizienten linear 
	- $u^2(t)=\ln(t)$ hat $u(t)$ als Koeffizient, daher nicht linear
	- $u^{(5)}(t)=\ln(t)$ ist linear
	- $u^{(5)}(t) = \ln(u)$ ist nicht linear
	- $u''(x)-e^{x}+e^{u}=0$ ist nicht linear, da $u$ im Exponenten
	- $e^t u(t)$ ist linear
- **Randwertproblem**: Informationen an unterschiedlichen Stellen gegeben
- **Anfangswertproblem**: Informationen an selben Stelle gegeben 
## homogen-lineare Gleichungen lösen

**Superpositionsprinzip**: Linearkombination von Lösungen wieder eine Lösung. Es gibt n Lösungen $y_{1}(x), \dots, y_{n}(x)$, allgemeine Lösung: $y(x) = C_1y_1(x) + \dots + C_ny_n(x)$

$$
a_n u^{(n)}(x) + a_{n-1} u^{(n-1)}(x) \dots + a_1 u'(x) + a_0 u(x) = 0
$$

Wir raten Form der Lösung als 
$$
u(x) = e^{\lambda x}
$$
Wir setzen ein mitden Ableitungen, klammern $e^{\lambda x}$ aus. Da $e^{\lambda x} >0$, muss $a_n \lambda^n + a_{n-1} \lambda^{n-1} + \dots + a_1 \lambda + a_0 = 0$. 

Wir nennen 
$$
p(\lambda) = a_n\lambda^n + a_{n-1}\lambda^{n-1} + \dots + a_1\lambda + a_0
$$
das charakteristische Polynom.

### Nullstellen des charakteristischen Polynoms

**Case 1**: reelle Nullstellen $\lambda$: Lösungen haben Form $u(x) = e^{\lambda x}$
- z.B. allgemeine Form bei 2 verschiedenen: $u(x) = C_1 \cdot e^{\lambda_1 x} + C_2 \cdot e^{\lambda_2 x}$ 

**Case 2**: komplex konjugierte Nullstelle $\lambda$
- Wurzel aus negativer Zahl (z.B. Mitternachtsformel $\lambda_{1,2} = a \pm ib$) 
- Realteil a und Imaginärteil b
- $u_1(x) = e^{ax} \sin(bx) \quad \text{und} \quad u_2(x) = e^{ax} \cos(bx)$

**Case 3**: mehrfache Nullstellen die gleich sind (höhere Multiplizität)
- für jede Wiederholung der Nullstelle multiplizieren wir die Lösung mit weiterem $x$
- Multiplizität $s \implies$ s verschiedene Lösungen
- $e^{\lambda x}, \quad x \cdot e^{\lambda x}, \quad x^2 \cdot e^{\lambda x}, \quad \dots \quad \text{bis} \quad x^{s-1} e^{\lambda x}$ 