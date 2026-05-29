## Einleitung

- **ungerade**: $\forall x \in \mathbb{R} f(-x) = -f(x)$
- **gerade**: $\forall x \in \mathbb{R} f(-x) = f(x)$
- $\sin^2 + \cos^2=1$ 

- **Injektiv**: nie 2 inputs zu gleichem output
- **Surjektiv**: jeder output hat einen input
- **Bijektiv**: injektiv und surjektiv, 1 to 1 
	
- Jede streng monotone Funktion ist injektiv.
- Falls bijkeitv, existiert eine Umkehrfunktion. 
- Wenn $f$ streng monoton ist, ist auch die Umkehrfunktion $f^{-1}$ streng monoton

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

**konvex**: linksgekrümmt (konv$e^x$)
**konkav**: rechtsgekrümmt

siehe [[09 Differenzialrechnung#Krümmung]]

## Stetigkeit

Eine Funktion ist stetig, wenn an jedem Punkt stetig, aka keinen Sprung. Vorstellung Zoom: Hab ich z.B. einen Spitz, dann kann ich beliebig nahe ran-zoomen und komme dem Spitz immer näher, somit stetig. 

==Ich darf annehmen, dass Polynome, sin(x), log, etc. stetisch sind.== 

> [!info] Rechenregeln Stetigkeit
> $f, g : D \subset \mathbb{R} \to \mathbb{R}$ stetig. Es gilt:
> - $f + g$ ist stetig
> - $f - g$ ist stetig
> - $c \cdot f$, respektive $c \cdot g$, ist für jede beliebige Konstante $c \in \mathbb{R}$ stetig
> - $f \cdot g$ ist stetig
> - $\frac{f}{g}$ ist stetig, wenn $g \neq 0$
> - Verknüpfung stetiger Funktionen wieder stetig, Grenzwert ist Grenzwert der inneren Funktion ausgewertet auf die äussere Funktion. [[2nd Semester/Analysis/Slides/06 Slides.pdf#page=19|Beweis]]
>   $$
>   \lim_{n \to \infty} f(x_n) = f\left(\lim_{n \to \infty} x_n\right)
>   $$
> - Umkehrfunktion einer stetigen Funktion ist auch stetig


Stetigkeit zeigen: 

- [[#Definition]]
- [[#Links- und rechtsseitiger Limes]]
- [[#Folgenstetigkeit]]

### Definition

Wenn der **Abstand des x-Wertes** zu unserem Startpunkt $x_0$ **kleiner als Delta** ist dann ist auch der **Abstand der Funktionswerte kleiner als Epsilon**. 

Eine Funktion ist an Stelle $x_0$ stetig, wenn wir
1. für jeden beliebig vorgegebenen $\varepsilon$-Bereich (y-Achse) um $f(x_0)$
2. einen $\delta$-Bereich (x-Achse) um $x_0$ finden, sodass
3. alle $x$-Werte aus diesem $\delta$-Bereich Funktionswerte liefern, die in den $\varepsilon$-Bereich fallen

$$
\forall \varepsilon > 0 \exists \delta > 0 \text{ s.d. } \forall x \in I \left( |x - x_0| < \delta \Rightarrow |f(x) - f(x_0)| < \varepsilon \right)
$$

**Vorgehen**

1. Forme um, bis $|x-x_{0}|$ als eigener Faktor vorkommt. 
2. Schätze den Rest so lange nach oben ab, bis **kein** $x$ vorkommt ($x_{0}$ darf vorkommen). Jetzt haben wir Form $< |x - x_0| \cdot R$ 
3. nutze $\frac{\varepsilon}{R}$. 
4. $\delta$ ist minimum von allen $|x-2| <$ Abschätzungen

![[Bildschirmfoto 2026-04-13 um 17.15.58.png]]
![[Bildschirmfoto 2026-04-14 um 15.21.57.png]]


### Links- und rechtsseitiger Limes

Stetigkeit an Stelle zeigen, indem **linksseitiger limes gleich rechtsseitiger limes**. 
$$
\lim_{x \to x_0^-} f(x) = \lim_{x \to x_0^+} f(x) = f(x_0)
$$
 
 ![[Bildschirmfoto 2026-04-13 um 17.38.58.png]]
 
### Folgenstetigkeit

$f$ an der Stelle $x_0$ genau dann stetig, wenn 
- für jede Folge $(x_n)_{n \in \mathbb{N}_0}$ mit $\lim_{ n \to \infty }x_{n}=x_{0}$ 
- die Folge der Funktionswerte $(f(x_n))_{n \in \mathbb{N}_0}$ gegen $f(x_0)$ konvergiert.

![[Bildschirmfoto 2026-04-13 um 17.16.28.png]]

### Zwischenwertsatz

Eine stetige Funktion kann keine Werte überspringen. ==Achtung==, um zu Verwenden, zuerst **Stetigkeit** zeigen, muss auch am Rand gelten.

> Es sei $f : [a, b] \to \mathbb{R}$ eine stetige Funktion und es sei $c$ eine Zahl zwischen $f(a)$ und $f(b)$. Dann gibt es ein $x \in [a, b]$ mit $f(x) = c$.

Also: 
Es sei $f : I \subset \mathbb{R} \to \mathbb{R}$ eine stetige Funktion, und es seinen $a, b \in I$ mit $f(a) < 0$ und $f(b) > 0$. Dann hat $f$ mindestens eine Nullstelle zwischen $a$ und $b$.

Eine stetige Funktion, die auf einem abgeschlossenen und beschränkten Intervall definiert ist, nimmt dort immer einen konkreten maximalen und minimalen Wert an.

### Stetig fortsetzbar

Wenn man einen **==endlichen==** Wert für eine Stelle finden kann, die nicht definiert ist, kann man eine Funktion "stetisch forsetzen".

==Achtung==, z.B. $f(x)=\frac{1}{x}$ ist nicht stetisch fortsetzbar. Auch $f(x)=\ln(x^2)$ **nicht**, da der gesuchte Wert **nicht endlich** ist. 

![[Pasted image 20260413180021.png]]

---

## Extremwertsatz

Funktion 

- stetig
- Definitionsbereich ist kompaktes Intervall (kann als $[a,b]$ mit $a,b \in \mathbb{R}$ schreiben)

hat minimum und maximum. 

Wenn $(a,b)$ dann können wir nur unendlich nah an Max und Min ran.

---

## Ableitung

→ siehe [[09 Differenzialrechnung]]
