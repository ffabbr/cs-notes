
1. [[#Einleitung]]
2. [[#Rechenregeln]]
3. [[#Grenzwert berechnen]]
4. [[#Absolute und Bedingte Konvergenz]]
5. [[#Kriterien]]

## Einleitung

- eine Reihe ist die **Summe der Glieder einer Folge**
- darf NICHT umgeordnet werden

eine Reihe konvergiert, wenn die Folge der Teilsummen konvergiert: 

- **Teilsummen**: Summe der ersten $n$ Glieder der Reihe ($s_{1} = a_{1}, s_{2} = a_{1} + a_{2}, \dots$)
- $s_1, s_2, s_3, \dots$ bilden eine neue Folge

---

Reihe konvergiert $\implies$ Grenzwert der Summanden (Folge) ist 0
Grenzwert der Summanden ist nicht 0 $\implies$ Reihe divergiert

==ACHTUNG== auf Implikationsrichtung. z.B. $\sum_{n=1}^{\infty} \frac{1}{n}$ divergiert, $\sum_{n=1}^{\infty} \frac{1}{n^2}$ konvergiert


> [!info]
> - Wenn $a_n \geq 0$ für alle n (nur nicht-negative Glieder): 
>   Die Folge der Teilsummen $s_1, s_2, s_3, \dots$, $s_{n} = \sum_{k=0}^{n} a_{k}$ ist monoton wachsend. 


## Rechenregeln

$$
\sum_{n=0}^{\infty} C \cdot a_n = C \cdot \sum_{n=0}^{\infty} a_n \quad (C \in \mathbb{R})
$$

$$
\sum_{n=0}^{\infty} (a_n + b_n) = \sum_{n=0}^{\infty} a_n + \sum_{n=0}^{\infty} b_n
$$

Das Konvergenzverhalten ändert sich nicht durch Weglassen endlicher Glieder. Somit gilt $\sum_{n=0}^{\infty} a_n \text{ konvergent} \iff \sum_{n=N}^{\infty} a_n \text{ konvergent}$, also:

$$
\underbrace{\sum_{n=0}^{\infty} a_n}_{\text{Gesamt}} = \underbrace{\sum_{n=0}^{N-1} a_n}_{\text{Endlicher Anfang}} + \underbrace{\sum_{n=N}^{\infty} a_n}_{\text{Unendlicher Rest}}
$$

## Grenzwert berechnen

Es gibt nur 2 Reihen, bei denen wir das können. Die geometrische Reihe und die teleskope Reihe. Also wenn etwas keine geometrische Reihe ist, dann muss es durch Teleskopieren lösbar sein. 

### Geometrische Reihe

konvergiert bei $q < 1$, divergiert bei $q > 1$.

$$\sum_{n=k}^{\infty} a \cdot q^n = a\cdot \frac{q^k}{1-q} \quad \text{für } |q| 
< 1$$
oder (einfachere) Formel ==ab 0== verwenden $\sum_{n=0}^{\infty} a\cdot q^n = a\cdot \frac{1}{1-q}$ und wenn z.B. ab 2, dann für 0, 1 abziehen. 

### Teleskope Reihe

Aufteilung finden, Beispiel
$$
\begin{align}
 & \frac{1}{n(n+1)} = \frac{A}{n} + \frac{B}{n+1} \\
 \implies  & 1 = A(n+1) + Bn
\end{align}
$$

Jetzt finde Werte für A und B, sodass B und A respektive "verschwinden", durch ein Gleichungssystem. 

Hier: $n=0, n=-1$. Jetzt können wir in eine teleskope Summe umschreiben:
$$
\frac{1}{n(n+1)} = \frac{1}{n} - \frac{1}{n+1}
$$
![[IMG_8452.jpg]]

## Beispiele

**Harmonische Reihe**, konvergiert bei $s > 1$, divergiert bei $s \leq 1$

$$\sum_{k=1}^{\infty} \frac{1}{k^s}$$


**Beispiel**

Konvergiert für $s > 1$ und divergiert für $s \leq 1$:

$$\sum_{k=1}^{\infty} \frac{1}{k^s} = \sum_{k=1}^{\infty} k^{-s}$$

**Beispiel**

- Reihe: $a \sum_{n=0}^{\infty} q^n$
- Partialsumme: $s_n = a + aq + aq^2 + \dots + aq^{n-1} = a \cdot \frac{1 - q^n}{1 - q}$
- Falls $|q| < 1$, konvergiert: $s = \lim_{n \to \infty} s_n = a \sum_{n=0}^{\infty} q^n = a \frac{1}{1 - q}$

## Absolute und Bedingte Konvergenz

**Absolut konvergent**:
- $\sum_{n=0}^{\infty} |a_n|$ (Reihe der Absolutbeträge) konvergiert
- Absolute Konvergenz $\implies$ Konvergenz

**Bedingt konvergent**: 
- Reihe konvergiert
- $\sum_{n=0}^{\infty} |a_n|$ geht gegen unendlich (sie **divergiert ==nicht== absolut**).


## Riemannscher Umordnungssatz 

Wir können **die Summanden einer ==bedingt konvergenten Reihe== so vertauschen**, sodass jeder Wert $L$ herauskommen kann, oder sogar divergiert ($\infty$). Dabei addieren wir z.B. alle positiven Werte bis wir L überschreiten, dann alle negativen Werte bis wir L unterschreiten, usw. 

$$
L = \sum_{n=0}^{\infty} a_{\varphi(n)}
$$
Für **==absolut konvergente Reihen==** gilt das nicht. Beim Vertauschen konvergiert die Reihe weiterhin absolut zum selben Wert, Ergebnis der Summe bleibt gleich. 

## Dreiecksungleichung

Jede **absolut konvergente Reihe konvergiert** und es gilt die verallgemeinerte Dreiecksungleichung

$$
\left| \sum_{n=0}^{\infty} a_n \right| \le \sum_{n=0}^{\infty} |a_n| 
$$

## Kriterien

1. [[#Vergleichskriterium]]
2. [[#Leibnitz-Kriterium]]
3. [[#Cauchy-Kriterium]]
4. [[#Wurzelkriterium]]
5. [[#Quotientenkriterium]]

### Vergleichskriterium

vgl. ähnlich wie [[06 Folgen#Sandwich Theorem|Sandwich-Theorem]] 

- Reihe $\sum_{n=0}^{\infty} b_n$, alle Glieder $\geq 0$
- ==2 Vergleichsreihen== mit $c_n \leq b_n \leq a_n$

**Majorantenkriterium**
"größere" Reihe $\sum_{n=0}^{\infty} a_n$ konvergiert (nimmt endlichen Wert an) $\implies$ "kleinere" Reihe $\sum_{n=0}^{\infty} b_n$ konvergiert

**Minorantenkriterium**
"kleinere" Reihe $\sum_{n=0}^{\infty} c_n$ divergiert (wächst gegen unendlich) $\implies$  "größere" Reihe $\sum_{n=0}^{\infty} b_n$ divergiert

![[Bildschirmfoto 2026-03-18 um 14.35.14.png|700]]

### Leibnitz-Kriterium

Nehme Folge
- hat nur positive Zahlen
- ist monoton fallend
- konvergiert ==nach 0== 

Erstelle Reihe
- füge Faktor $(-1)^n$ bei

Reihe konvergiert gegen endlichen Grenzwert. 

$$
\sum_{n=0}^{2m+1} (-1)^n a_n \le \sum_{n=0}^{\infty} (-1)^n a_n \le \sum_{n=0}^{2m} (-1)^n a_n, \quad \forall m \in \mathbb{N}_0. 
$$

![[Bildschirmfoto 2026-03-24 um 18.02.29.png]]

### Cauchy-Kriterium

Eine Reihe konvergiert $\iff$ Summe eines beliebigen "Blocks" von Gliedern, der weit hinten in der Reihe liegt, ist klein

$$
\left| \sum_{k=m+1}^{n} a_k \right| \le \varepsilon
$$


### Wurzelkriterium

Indiz: oben und unten im Bruch steht hoch n. 

Man vergleicht die zu prüfende Reihe mit der bekannten geometrischen Reihe $\sum q^n$. Bei einer geometrischen Reihe wissen wir, dass sie konvergiert, wenn der Faktor $q$ kleiner als 1 ist.

$$
\rho = \limsup_{n \to \infty} (|a_n|)^{1/n} = \begin{cases} < 1 & \text{(absolut) konvergent} \\ > 1 & \text{divergent} \\ = 1 & \text{keine Aussage} \end{cases}
$$

[Beispiel](https://youtu.be/4_3RuskBREM?si=POt9i_CLmfKjMr7c&t=89)

### Quotientenkriterium

→ Wachstumsfaktor
Indiz: Bruch mit Faktorial

Indiz: Fakultät

$$
\lim_{k \to \infty} \left| \frac{a_{k+1}}{a_k} \right| = \begin{cases} < 1 & \text{(absolut) konvergent} \\ > 1 & \text{divergent} \\ = 1 & \text{keine Aussage} \end{cases}
$$

[Beispiel](https://youtu.be/p3BPRuk0Wwk?si=cO3VWkrH7vFr3FT1&t=420)

## Potenzreihen

→ Polynom mit unendlich vielen Gliedern

$$
\sum_{k=0}^{\infty} c_k(x-a)^k
$$