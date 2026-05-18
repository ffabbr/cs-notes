
- Potenz +1 
- times $\frac{\text{ehemaliger koeffizient}}{\text{neuer exponent}}$
- Obergrenze minus Untergrenze
- $\int x^n dx = \frac{x^{n+1}}{n+1}$
- $\int \frac{1}{x} dx = \ln|x|$


![[Bildschirmfoto 2026-05-11 um 15.41.40.png|583]]


$$\int (f(x) \pm g(x))\, dx = \int f(x)\, dx \pm \int g(x)\, dx$$

und

$$\int s f(x)\, dx = s \int f(x)\, dx \qquad \text{($s$ eine Konstante)}$$

$$\int k\, dx = kx + C$$

$$\int x^n\, dx = \frac{1}{n+1} x^{n+1} + C, \quad n \neq -1$$

$$\int e^x\, dx = e^x + C, \qquad \int \frac{1}{x}\, dx = \ln(|x|) + C$$

$$\int \sin(x)\, dx = -\cos(x) + C, \qquad \int \cos(x)\, dx = \sin(x) + C$$

$$\int \sinh(x)\, dx = \cosh(x) + C, \qquad \int \cosh(x)\, dx = \sinh(x) + C$$


**Umkehrung der Produktregel**

Wir wissen, dass gilt

$$\int \frac{d}{dx}\bigl(f(x) \cdot g(x)\bigr)\, dx = (f \cdot g)(x) = \int f'(x) \cdot g(x)\, dx + \int f(x) \cdot g'(x)\, dx$$

Oder umformuliert (grüne Terme):

$$\int {\color{green}\underbrace{f'(x)}_{\uparrow}} \cdot {\color{green}\underbrace{g(x)}_{\downarrow}}\, dx = (f \cdot g)(x) - \int f(x) \cdot g'(x)\, dx$$

Diese Regel nennen wir **partielle Integration**.

---

**Umkehrung der Kettenregel**

Hier wissen wir, dass gilt

$${\color{green} f(g(x)) + C} = \int \frac{d}{dx}(f(g(x)))\, dx = \int {\color{green} f'(g(x)) \cdot g'(x)}\, dx = \int \frac{df}{dy} \frac{dy}{dx}\, dx = \int \frac{df}{dy}\, dy$$

Zusammengefasst (grüne Terme):

$$\int {\color{green} f'(g(x)) \cdot g'(x)}\, dx = \int {\color{green} \frac{df}{dy}}\, dy = {\color{green} f(g(x)) + C}$$

Diese Regel nennen wir **Integration durch Substitution**.


**Satz (Eigenschaften des Riemann-Integrals)**

**i) Linearität**
Es seien $f, g : [a,b] \to \mathbb{R}$ zwei (Riemann-)integrierbare Funktionen, und es seien $\alpha, \beta \in \mathbb{R}$. Dann ist auch $\alpha f + \beta g$ integrierbar und es gilt

$$\int_a^b (\alpha f + \beta g)(x)\, dx = \alpha \int_a^b f(x)\, dx + \beta \int_a^b g(x)\, dx$$

**ii) Monotonie**
Es seien $f, g : [a,b] \to \mathbb{R}$ zwei (Riemann-)integrierbare Funktionen. Falls gilt $f \leq g$, so gilt auch

$$\int_a^b f(x)\, dx \leq \int_a^b g(x)\, dx$$

**iii) Dreiecksungleichung**
Es sei $f : [a,b] \to \mathbb{R}$ eine (Riemann-)integrierbare Funktion. Dann gilt

$$\left| \int_a^b f(x)\, dx \right| \leq \int_a^b |f(x)|\, dx$$

**iv) Umkehrung der Integrationsrichtung**
Es sei $f : [a,b] \to \mathbb{R}$ eine (Riemann-)integrierbare Funktion. Dann gilt

$$\int_a^b f(x)\, dx = -\int_b^a f(x)\, dx$$

**v) Aufteilung des Integrationsbereichs**
Es sei $f : [a,b] \to \mathbb{R}$ eine (Riemann-)integrierbare Funktion. Dann gilt

$$\int_a^b f(x)\, dx = \int_a^c f(x)\, dx + \int_c^b f(x)\, dx, \quad a \leq c \leq b$$

---

**Satz**
Jede monotone Funktion $f : [a,b] \to \mathbb{R}$ ist Riemann-integrierbar.

---

**Satz**
Jede stetige Funktion $f : [a,b] \to \mathbb{R}$ ist Riemann-integrierbar.

---

**Definition**
Es sei $D \subset \mathbb{R}$, $(f_n)_{n \in \mathbb{N}_0}$ eine Folge von Funktionen $f_n : D \subset \mathbb{R} \to \mathbb{R}$ und $f : D \subset \mathbb{R} \to \mathbb{R}$ eine weitere Funktion.
Dann **konvergiert die Folge $(f_n)_{n \in \mathbb{N}_0}$ punktweise gegen $f$**, falls für jedes $x \in D$ die reelle Folge $(f_n(x))_{n \in \mathbb{N}_0}$ gegen $f(x)$ konvergiert. $f$ heisst dann auch **punktweiser Grenzwert** der Folge $(f_n)_{n \in \mathbb{N}_0}$.

---

**Definition**
Es sei $D \subset \mathbb{R}$, $(f_n)_{n \in \mathbb{N}_0}$ eine Folge von Funktionen $f_n : D \subset \mathbb{R} \to \mathbb{R}$ und $f : D \subset \mathbb{R} \to \mathbb{R}$ eine weitere Funktion.
Dann **konvergiert die Folge $(f_n)_{n \in \mathbb{N}_0}$ gleichmässig gegen $f$**, falls für jedes $\varepsilon > 0$ ein Index $N$ existiert, sodass für alle $n \geq N$ und für alle $x \in D$ gilt

$$|f_n(x) - f(x)| < \varepsilon$$

---

**Satz**
Es sei $D \subset \mathbb{R}$ und $(f_n)_{n \in \mathbb{N}_0}$ eine Folge stetiger Funktionen $f_n : D \subset \mathbb{R} \to \mathbb{R}$, welche gleichmässig gegen $f : D \subset \mathbb{R} \to \mathbb{R}$ konvergiert. Dann ist $f$ stetig.

---

**Satz**
Es sei $(f_n)_{n \in \mathbb{N}_0}$ eine Folge integrierbarer Funktionen $f_n : [a,b] \to \mathbb{R}$, welche gleichmässig gegen $f : [a,b] \to \mathbb{R}$ konvergiert. Dann ist auch $f$ integrierbar, und es gilt

$$\int_a^b f\, dx = \lim_{n \to \infty} \int_a^b f_n\, dx$$

---

**Satz (Mittelwertsatz der Integralrechnung)**
Falls der Integrand $f(x)$ auf dem betrachteten Intervall $[a,b]$ stetig ist, gilt für ein $c \in [a,b]$

$$f(c) = \frac{1}{b-a} \int_a^b f(x)\, dx$$

Der Ausdruck $\dfrac{1}{b-a} \int_a^b f(x)\, dx$ ist der **Mittelwert** von $f$ über $[a,b]$.

---

**Satz (Hauptsatz der Integral- und Differentialrechnung)**
Es sei $f : [a,b] \to \mathbb{R}$ stetig. Dann ist für alle $C \in \mathbb{R}$ die folgende Funktion $F : [a,b] \to \mathbb{R}$ eine Stammfunktion von $f$

$$F(x) := \int_a^x f(y)\, dy + C$$

Ausserdem ist jede Stammfunktion von der obigen Form.

---

**Korollar**
Es sei $F : [a,b] \to \mathbb{R}$ stetig differenzierbar. Dann gilt für alle $x \in [a,b]$

$$F(x) = F(a) + \int_a^x F'(t)\, dt$$

---

**Korollar**
Es sei $f : [a,b] \to \mathbb{R}$ stetig und $F : [a,b] \to \mathbb{R}$ eine Stammfunktion von $f$. Dann gilt

$$\int_a^b f(t)\, dt = F(x)\Big|_a^b = F(b) - F(a)$$
