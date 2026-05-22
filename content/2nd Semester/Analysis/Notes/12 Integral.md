
## Introduction

*Fläche unter der Funktion*

**Untersummen und Obersummen**: wir unterteilen die Funktion in n "Blöcke" und berechnen die Fläche, indem wir die Flächeninhalte der Blöcke (Rechtecke) addieren. Bei der Untersumme $L = \sum_{i=1}^{n} \left( \inf_{x \in [x_{i-1}, x_i]} f(x) \right) \cdot (x_i - x_{i-1})$ nehmen wir immer den kleinsten Funktionswert in dem Abschnitt des Blockes, bei der Obersumme $U = \sum_{i=1}^{n} \left( \sup_{x \in [x_{i-1}, x_i]} f(x) \right) \cdot (x_i - x_{i-1})$ den grössten. Wenn wir n (die Anzahl der Unterteilungen) immer grösser machen ($n \to \infty$) und L und U sich unendlich annähern, können wir das Riemann Integral bestimmen: $\int_{a}^{b} f(x) \, dx = \sup L(f) = \inf U(f)$ 

ist Funktion gerade (symmetrisch), vereinfacht sich die Aufgabe ev. durch Verschieben der Grenzen oder $\cdot 2$, da ja das Integral als Fläche gesehen werden kann.
### Typen der Integrale

1. [[#a. bestimmtes Integral (Riemann)]]
2. [[#b. unbestimmtes Integral (Stammfunktion)]] 

#### a. bestimmtes Integral (Riemann)

*die eigentliche Fläche von bis*

$$
\int_{a}^{b} f(x) \, dx = \sup L(f) = \inf U(f)
$$

Es sei $f : [a,b] \to \mathbb{R}$ stetig und $F : [a,b] \to \mathbb{R}$ eine Stammfunktion von $f$. Dann gilt
$$
\int_{a}^{b} f(x) \, dx = [F(x)]_{a}^{b} = F(b) - F(a)
$$

#### b. unbestimmtes Integral (Stammfunktion)

- die *allgemeine Stammfunktion*, also welche Funktion $F(x)$ abgeleitet $f(x)$ ist
- Füge $+\ C$ an

## Implikationen

$\text{differenzierbar} \implies \text{stetig}$

für Funktionen auf einem kompakten Intervall gilt $f:[a,b] \to \mathbb{R}$ 
- $\text{differenzierbar} \implies \text{stetig}$
- $\text{stetig} \implies \text{integrierbar}$
- $\text{monoton} \implies \text{integrierbar}$

## Integral berechnen

Für einen Term: 
- Potenz +1 
- times $\frac{\text{ehemaliger koeffizient}}{\text{neuer exponent}}$
- $+ \ C$ 


### Integration durch partielle Integration

1. setze u (wird "leichter" beim Ableiten, oft $\ln(x)$) und v' (das andere)
2. berechne u' und v
3. setze $u\cdot v - \int v\cdot u' dx$

![[Bildschirmfoto 2026-05-19 um 15.14.26.png|444]]

Herleitung der regel der partiellen Integration: Produktregel vom Ableiten. Wir wissen $(f \cdot g)' = f' \cdot g + f \cdot g'$, nehmen auf beiden Seiten das Integral $\int \frac{d}{dx}\big(f(x) \cdot g(x)\big) \, dx = \int \big(f'(x) \cdot g(x) + f(x) \cdot g'(x)\big) \, dx$, und auf der linken Seite heben sich Ableitung und Integral auf. Wir haben also $f(x) \cdot g(x) = \int \big(f'(x) \cdot g(x) + f(x) \cdot g'(x)\big) \, dx$, teilen die rechte Seite auf $f(x) \cdot g(x) = \int f'(x) \cdot g(x) \, dx + \int f(x) \cdot g'(x) \, dx$, und bekommen $\int f'(x) \cdot g(x) \, dx = f(x) \cdot g(x) - \int f(x) \cdot g'(x) \, dx$. Jetzt formen wir um und bekommen 
$$
\int \underbrace{g(x)}_{u} \cdot \underbrace{f'(x)}_{v'} \, dx = \underbrace{g(x)}_{u} \cdot \underbrace{f(x)}_{v} - \int \underbrace{f(x)}_{v} \cdot \underbrace{g'(x)}_{u'} \, dx
$$ 


#### Zirkuläres Beispiel

![[Bildschirmfoto 2026-05-19 um 15.15.17.png|444]]

### Integration durch Substitution

wir haben eine Funktion in einer Funktion (vgl. Kettenregel beim Ableiten)
nützlich, wenn ein Teil der Ableitung wieder in der Funktion vorkommt

1. **ersetze** innere Funktion mit u
2. **berechne** $\frac{du}{dx}= u'$ (Ableitung), multipliziere mal $dx$ und forme weiter um, bis wir $dx= \dots$ haben, dann ersetze das $dx$ in der ursprünglichen Gleichung mit der neuen Äquivalenz
3. **neue Gren**zen: setze alte Grenzen in $u(x)$ ein und ersetze

- **bestimmtes Integral**? jetzt normal berechnen, die neuen Grenzen in u einsetzen, etc.
- **unbestimmtes Integral**? berechnen, am Ende wieder $u$ zurück-substituieren

![[Bildschirmfoto 2026-05-20 um 14.58.16.png|482]]


----

## Eigenschaften des bestimmten Integrals

**i) Linearität**
$f, g : [a,b] \to \mathbb{R}$ sind integrierbare Funktionen, dann ist $\alpha f + \beta g$ auch integrierbar mit

$$\int_a^b (\alpha f + \beta g)(x)\, dx = \alpha \int_a^b f(x)\, dx + \beta \int_a^b g(x)\, dx$$

**ii) Monotonie**
$f, g : [a,b] \to \mathbb{R}$ integrierbare Funktionen. Falls $f \leq g$, dann

$$\int_a^b f(x)\, dx \leq \int_a^b g(x)\, dx$$

**iii) Dreiecksungleichung**
$f : [a,b] \to \mathbb{R}$ integrierbar, es gilt

$$\left| \int_a^b f(x)\, dx \right| \leq \int_a^b |f(x)|\, dx$$

**iv) Umkehrung der Integrationsrichtung**
$f : [a,b] \to \mathbb{R}$ integrierbar, es gilt

$$\int_a^b f(x)\, dx = -\int_b^a f(x)\, dx$$

**v) Aufteilung des Integrationsbereichs**
$f : [a,b] \to \mathbb{R}$ integrierbar, es gilt

$$\int_a^c f(x) \, dx = \int_a^b f(x) \, dx + \int_b^c f(x) \, dx, \quad a \leq b \leq c$$

**vi) Punktweise Sachen**
$(f_n)_{n \in \mathbb{N}_0}$ konvergiert punktweise auf $D$ gegen $f$, falls für jedes $x \in D$ gilt:

$$\lim_{n \to \infty} f_n(x) = f(x)$$

**vii) Etwas**
$(f_n)_{n \in \mathbb{N}_0}$ konvergiert gleichmässig auf $D$ gegen $f$, falls für jedes $\varepsilon > 0$ ein $N$ existiert, sodass für alle $n \geq N$ und alle $x \in D$ gilt:

$$|f_n(x) - f(x)| < \varepsilon$$
**viii) Stetigkeit**
Es sei $D \subset \mathbb{R}$ und $(f_n)_{n \in \mathbb{N}_0}$ eine Folge stetiger Funktionen $f_n : D \subset \mathbb{R} \to \mathbb{R}$, welche gleichmässig gegen $f : D \subset \mathbb{R} \to \mathbb{R}$ konvergiert. Dann ist $f$ stetig.

**ix) Unterteilung in Blöcke für Flächeninhalt**
Es sei $(f_n)_{n \in \mathbb{N}_0}$ eine Folge integrierbarer Funktionen $f_n : [a,b] \to \mathbb{R}$, welche gleichmässig gegen $f : [a,b] \to \mathbb{R}$ konvergiert. Dann ist auch $f$ integrierbar, und es gilt

$$\int_a^b f\, dx = \lim_{n \to \infty} \int_a^b f_n\, dx$$

**x) Mittelwertsatz**
Falls der Integrand $f(x)$ auf dem betrachteten Intervall $[a,b]$ stetig ist, gilt für ein $c \in [a,b]$ 

$$f(c) = \frac{1}{b-a} \int_a^b f(x)\, dx$$

Der Ausdruck $\dfrac{1}{b-a} \int_a^b f(x)\, dx$ ist der **Mittelwert** von $f$ über $[a,b]$.

**xi) Logische Addition**
Es sei $F : [a,b] \to \mathbb{R}$ stetig differenzierbar. Dann gilt für alle $x \in [a,b]$

$$F(x) = F(a) + \int_a^x F'(t)\, dt$$


---


## Tabelle zum Integrieren

![[13 Tabelle]]






