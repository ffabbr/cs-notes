
*Statt x zu finden, wollen wir eine Funktion bestimmen, die Eigenschaften erfüllt.*

- **Ordnung**: höchste Ableitung
- **homogen**: $s(x)=0$ 
	- gebe alle Terme die die Funktion beinhalten auf eine Seite, und alle Terme die Unabhängig von dieser Funktion sind auf die andere
	- wenn die Seite mit unabhängigen Termen = 0, dann homogen
- **linear**: gesuchte Funktion und alle Ableitungen kommen nur in der ersten Potenz vor und nicht miteinander multipliziert; Koeffizienten linear 
	- $u^2(t)=\ln(t)$ hat $u(t)$ als Koeffizient, daher nicht linear
	- $u^{(5)}(t)=\ln(t)$ ist linear
	- $u^{(5)}(t) = \ln(u)$ ist nicht linear
	- $u''(x)-e^{x}+e^{u}=0$ ist nicht linear, da $u$ im Exponenten
	- $e^t u(t)$ ist linear
- **Randwertproblem**: Informationen an unterschiedlichen Stellen 
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
Wir setzen ein, klammern $e^{\lambda x}$ aus. Da $e^{\lambda x} >0$, muss $a_n \lambda^n + a_{n-1} \lambda^{n-1} + \dots + a_1 \lambda + a_0 = 0$. 

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

---

## nicht-lineare Differenzialgleichung 1. Ordnung

### 1. Trennung der Variablen

Wir schreiben die DGL als $y' = f(x) \cdot g(y)$ und wenden diesen Trick an:

$$
\frac{dy}{dx} = f(x) \cdot g(y) \implies \frac{1}{g(y)} dy = f(x) dx \implies \int \frac{1}{g(y)} dy = \int f(x) dx
$$

Wir befolgen ein genaues Muster für die Lösung

Beispiel: **Löse das AWP** $y' = 3(xy)^2$ mit $y(0) = 1$

1. Differentiale schreiben: $\frac{dy}{dx} = 3(xy)^2$
2. Variablen trennen: $\frac{dy}{dx} = 3x^2 \cdot y^2$
3. Umformung: $\int \frac{1}{y^2} dy = \int 3x^2 dx$
4. Integrieren: $-\frac{1}{y} = x^3 + C$
5. Nach $y(x)$ auflösen: $y(x) = \frac{-1}{x^3 + C}$
6. AWP lösen: $y(0) = \frac{-1}{C} = 1 \implies C = -1$
7. Ergebnis: $y(x) = \frac{-1}{x^3 - 1}$

### 2. Substitutionsmethode

**Löse die DGL:** $y' = (x-y)^2 + 1$

**Lösung:** Der Term $(x-y)$ stört. Wir substituieren..

1. Definition der Substitution: $u(x) = x - y(x)$
2. Ableiten nach x: $u' = 1 - y' \implies y' = 1 - u'$
3. Einsetzen: $1 - u' = u^2 + 1 \implies \frac{du}{dx} = -u^2$
4. Trennung der Variablen: $\int -\frac{1}{u^2} du = \int 1 dx \implies \frac{1}{u} = x + c$
5. Nach u auflösen: $u(x) = \frac{1}{x+c}$
6. Rücksubstitution: $x - y(x) = \frac{1}{x+c}$

**Ergebnis:** $y(x) = x - \frac{1}{x+c}$

### 3. Lineare inhomogene DGL

Falls $y_p(x)$ eine partikuläre Lösung einer solchen DGL ist und $y_h(x)$ die allgemeine Lösung der dazugehörigen homogenen DGL. Dann ist $y(x) = y_p(x) + y_h(x)$ die allgemeine Lösung der inhomogenen DGL.

| **Rechts der DGL / Störfunktion**                                               | **Ansatz für partikuläre Lösung**                          |
| ------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **Polynom**<br>$s(t) = a_0 + a_1t + \dots + a_nt^n$                             | <br>$y(t) = C_0 + C_1t + \dots + C_nt^n$                   |
| Spezialfall: $0$ ist eine m-fache Nullst. des charakteristischen Polynoms       | $y(t) = (C_0 + C_1t + \dots + C_nt^n)t^m$                  |
| <br><br>**Exponentialfunktion**<br>$s(t) = Ae^{kt}$                             | <br><br><br>$y(t) = Ce^{kt}$                               |
| Spezialfall: $k$ ist eine m-fache Nullst. des charakteristischen Polynoms       | <br>$y(t) = (Ce^{kt})t^m$                                  |
| <br><br>**Schwingung**<br>$s(t) = A\sin(\omega t) + B\cos(\omega t)$            | <br><br><br>$y(t) = C_1\sin(\omega t) + C_2\cos(\omega t)$ |
| Spezialfall: $i\omega$ ist eine m-fache Nullst. des charakteristischen Polynoms | <br>$y(t) = (C_1\sin(\omega t) + C_2\cos(\omega t))t^m$    |

**Löse die DGL:** $y' - 2y = 4e^{2x}$

1. Homogene Lösung: $y' - 2y = 0 \implies \lambda - 2 = 0 \implies \lambda = 2$
   Somit ist $y_h(x) = C \cdot e^{2x}$ die homogene Lösung.
2. Partikulärer Ansatz: Da $e^{2x}$ schon in der homogenen Lösung steckt, versuchen wir $y_p(x) = A \cdot x \cdot e^{2x}$
3. $y_p(x)$ ableiten: $y_p'(x) = A \cdot e^{2x} + 2A \cdot x \cdot e^{2x}$
4. Einsetzen: $(A \cdot e^{2x} + 2A \cdot x \cdot e^{2x}) - 2 \cdot (A \cdot x \cdot e^{2x}) = 4 \cdot e^{2x}$
    $\implies A \cdot e^{2x} = 4 \cdot e^{2x} \implies A = 4 \implies y_p(x) = 4x \cdot e^{2x}$
5. **Ergebnis:** $y(x) = y_h(x) + y_p(x) = C \cdot e^{2x} + 4x \cdot e^{2x}$

### 4. Variation der Konstante

Dies können wir bei linearen inhomogenen DGL 1. Ordnung anwenden. Falls wir die homogene Lösung $y_h(x) = K \cdot e^x$ gefunden haben, dann versuchen wir den Ansatz $y_p(x) = K(x) \cdot e^x$ und setzen ein.

**Löse DGL:** $y' - 2y = \frac{e^{2x}}{x}$

**Lösung:** Die homogene Lösung haben wir schon gefunden.

1. Homogene Lösung: $y_h(x) = K \cdot e^{2x}$
2. Variation Konstante: $y_p(x) = K(x) \cdot e^{2x}$
3. Ableitung von $y_p(x)$: $y_p'(x) = K'(x) \cdot e^{2x} + 2 \cdot K(x) \cdot e^{2x}$
4. Einsetzen: $(K'(x) \cdot e^{2x} + 2 \cdot K(x) \cdot e^{2x}) - 2 \cdot (K(x) \cdot e^{2x}) = \frac{e^{2x}}{x}$
    $\implies(x) \cdot e^{2x} = \frac{e^{2x}}{x} \implies K'(x) = \frac{1}{x}$
5. Integrieren: $K(x) = \int K'(x) dx = \int \frac{1}{x} dx = \ln(|x|) + D$
6. Partikuläre Lösung: $y_p(x) = (\ln(|x|) + D) \cdot e^{2x}$
7. **Ergebnis:** $y(x) = y_h(x) + y_p(x) = \ln(|x|) \cdot e^{2x} + D \cdot e^{2x} + K \cdot e^{2x} = \ln(|x|)e^{2x} + C \cdot e^{2x}$