## Einleitung

- **ungerade**: $\forall x \in \mathbb{R} f(-x) = -f(x)$
- **gerade**: $\forall x \in \mathbb{R} f(-x) = f(x)$

- **Injektiv**: nie 2 inputs zu gleichem output
- **Surjektiv**: jeder output hat einen input
- **Bijektiv**: injektiv und surjektiv, 1 to 1 

- Jede streng monotone Funktion ist injektiv.
- Falls bijkeitv, existiert eine Umkehrfunktion. 

==Achtung==, multiple choice, bspw. "ist das eine injektive Funktion" → überprüfen, ob überhaupt eine Funktion #exam 

> [!warning]- Definitionsbereiche
> |**Typ**|**Funktion f(x)**|**Definitionsbereich D**|
> |---|---|---|
> |**Grundfunktion**|$x$|$\mathbb{R}$|
> |**Polynom**|$x^2$|$\mathbb{R}$|
> |**Bruchfunktion**|$\frac{1}{x}$|$x \neq 0$|
> |**Wurzelfunktion**|$\sqrt{x}$|$x \geq 0$|
> |**Logarithmus**|$\ln(x)$|$x > 0$|
> |**Exponentialfunktion**|$e^x$|$\mathbb{R}$|
> |**Sinus**|$\sin(x)$|$\mathbb{R}$|
> |**Kosinus**|$\cos(x)$|$\mathbb{R}$|
> |**Tangens**|$\tan(x)$|$x \neq \frac{\pi}{2} + k\pi, k \in \mathbb{Z}$|
> |**Arkussinus**|$\arcsin(x)$|$-1 \leq x \leq 1$|
> |**Arkuskosinus**|$\arccos(x)$|$-1 \leq x \leq 1$|
> |**Arkustangens**|$\arctan(x)$|$\mathbb{R}$|

## Grenzwerte 

$$
x \in \mathbb{D}(f) \cap (x_0 - \delta, x_0 + \delta) \implies |f(x) - L| < \varepsilon
$$

- **Grenzwerte im Unendlichen**: $x \to -\infty$ oder $x \to \infty$ hat Grenzwerte
- **Uneigentlicher Grenzwert**: der Grenzwert ist $\infty$ oder $- \infty$, eigentlich divergiert also

### Folgenkriterium für Grenzwerte 

$$
\lim_{x \to x_0} f(x) = L \iff \forall (x_n) \subset \mathbb{D}(f) \text{ mit } x_n \to x_0: \lim_{n \to \infty} f(x_n) = L
$$

hat an der Stelle $x_0$ den Grenzwert $L$ genau dann, wenn jede Folge $(x_n)$, die gegen $x_0$ konvergiert, dazu führt, dass $(f(x_n))$ gegen $L$ konvergiert.

### Einseitige Grenzwerte

man nähert sich von links oder von rechts
Unterscheide zwischen 2 Versionen von einseitigen Grenzwerten. 

#### Einseitige Grenzwerte, Version 1

Wenn der Grenzwert existiert und die Funktion an dieser Stelle definiert ist, muss der Grenzwert der Funktionswert sein. Also ist $x_{0}$ ein "Mitstreiter". Gibt es bspw. eine Sprungstelle an $x_{0}$ der nicht in das Konvergenzverhalten passt, dann haben wir keinen Grenzwert. 

Wenn
$$ x \in \mathbb{D}(f) \cap [x_0, x_0 + \delta) \implies |f(x) - L| < \epsilon $$
hat $f$ in $x_0$ den **rechtsseitigen Grenzwert L**
#### Einseitige Grenzwerte, Version 2

Wir schliessen $x_{0}$ aus. In dem Beispiel mit der Sprungstelle wäre die Sprungstelle ($x_{0}$) ausgeschlossen und wir könnten einen Grenzwert haben mit der Stelle, OBWOHL die Funktion an der Stelle definiert ist. 

Wenn
$$ x \in \mathbb{D}(f) \cap (x_0, x_0 + \delta) \Rightarrow |f(x) - L| < \epsilon $$
hat $f$ in $x_0$ den **rechtsseitigen Grenzwert L**

### Grenzwert im Unendlichen

Wenn
$$ x \in \mathbb{D}(f) \cap (M, \infty) \Rightarrow |f(x) - L| < \epsilon $$
hat $f$ für $x$ gegen unendlich den Grenzwert L


> [!info]
> Es gelte $\lim_{x \to c} f(x) = K(\neq \pm\infty)$, $\lim_{x \to c} g(x) = L(\neq \pm\infty)$ und $A$ sei eine beliebige feste Zahl.
> Dann gilt:
> 1.  $\lim_{x \to c}(f(x) + g(x)) = K + L$
> 2.  $\lim_{x \to c}(f(x) - g(x)) = K - L$
> 3.  $\lim_{x \to c}(f(x) \cdot g(x)) = K \cdot L$
> 4.  $\lim_{x \to c}(A \cdot f(x)) = A \cdot K$
> 5.  Falls $L \neq 0$, haben wir $\lim_{x \to c}(f(x)/g(x)) = K/L$

## Einschränkung

Gleiche Zuordnung, aber nur an bestimmten x-Stellen (durch $D'$) festgelegt

$$f|_{D'} : D' \to \mathbb{R} \text{ mit } f|_{D'}(x) = f(x) \forall x \in D'$$

## Krümmung

**konvex**: linksgekrümmt
**konkav**: rechtsgekrümmt

## Stetigkeit

Eine Funktion ist stetig, wenn an jedem Punkt stetig, aka keinen Sprung.

Eine Funktion ist an der Stelle $x_0$ **stetig**, wenn zu jedem $\varepsilon$ um den Funktionswert $f(x_0)$ ein Bereich $\delta$ um $x_0$ existiert, sodass alle $x$-Werte aus diesem Bereich Funktionswerte liefern, die weniger als $\varepsilon$ von $f(x_0)$ abweichen.

$$
\forall \varepsilon > 0 \exists \delta > 0 \text{ s.d. } \forall x \in I \left( |x - x_0| < \delta \Rightarrow |f(x) - f(x_0)| < \varepsilon \right)
$$

Hab ich z.B. einen Spitz, dann kann ich beliebig nahe ran-zoomen und komme dem Spitz immer näher, somit stetig.

> [!info] Rechenregeln Stetigkeit
> Wir gehen von zwei stetigen Funktionen $f, g : D \subset \mathbb{R} \to \mathbb{R}$ aus. Dann gilt:
> - $f + g$ ist stetig
> - $f - g$ ist stetig
> - $c \cdot f$, respektive $c \cdot g$, ist für jede beliebige Konstante $c \in \mathbb{R}$ stetig
> - $f \cdot g$ ist stetig
> - $\frac{f}{g}$ ist stetig, sofern $g \neq 0$
> - Verknüpfung stetiger Funktionen wieder stetig, Grenzwert ist Grenzwert der inneren Funktion ausgewertet auf die äussere Funktion

### Folgenstetigkeit

$f$ an der Stelle $x_0$ genau dann stetig, wenn für jede Folge $(x_n)_{n \in \mathbb{N}_0}$ mit $x_n \to x_0$ die Folge $(f(x_n))_{n \in \mathbb{N}_0}$ gegen $f(x_0)$ konvergiert

ODER

Folge genau dann stetig

---

