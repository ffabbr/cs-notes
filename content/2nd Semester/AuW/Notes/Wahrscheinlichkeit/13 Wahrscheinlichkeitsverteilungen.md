
- **Dichtefunktion**: Mit welcher Wahrscheinlichkeit tritt diese Zufallsvariable ein
- **Verteilungsfunktion**: Mit welcher Wahrscheinlichkeit tritt eine kleiner gleiche Zufallsvariable ein (vorherrige aufaddiert)

| **Verteilung / Begriff**         | **Kurzbeschreibung**                                                         |
| -------------------------------- | ---------------------------------------------------------------------------- |
| [[#Bernoulli-Verteilung]]        | Wslkt für Erfolg oder Misserfolg bei einem einzigen Versuch (Ja/Nein)        |
| [[#Binomialverteilung]]          | Wslkt, für Anzahl an Erfolg (k) bei Anzahl an Versuchen (n) mit Zurücklegen  |
| [[#Geometrische Verteilung]]     | Wslkt, dass es erst beim k-ten Mal eintritt                                  |
| [[#Negative Binomialverteilung]] | Wslkt für $n$ Erfolge bei $k$ Versuchen bei Experiment mit 2 Ausgängen       |
| [[#Poisson-Verteilung]]          | Wslkt für die Anzahl von Ereignissen in einem festen Zeitintervall oder Raum |
| **Fakultät**                     | Wie viele Möglichkeiten, n Objekte anzuordnen                                |
| **Binomialkoeffizient**          | Wie viele Möglichkeiten, k Objekte aus n Objekten auszuwählen                |

## Bernoulli-Verteilung

Wslkt für Erfolg oder Misserfolg bei einem einzigen Versuch (Ja/Nein)

Die Zufallsvariable ist 1 (Wslkt p) oder 0 (Wslkt 1-p).

**Beispiel**: Werfen Münze, Variable Kopf; Werfen Würfel, Variable Augenzahl 5. Praktisch: $X^2=X$ hier, da X ja nur 0 oder 1. 

Varianz: $p\cdot(1-p)$
Erwartungswert $p$

## Binomialverteilung

Wslkt, für Anzahl an Erfolg (k) bei Anzahl an Versuchen (n) mit Zurücklegen

$$
\binom{n}{k} \cdot p^k \cdot (1-p)^{n-k}
$$

$E[X] = n \cdot p$
$V[X] = n \cdot p(1-p)$

Bedingungen: 
1. 2 Versuchsausgänge, 
2. Ausgänge gleich wahrscheinlich, 
3. Ausgänge Unabhängig

## Poisson-Verteilung

Seltene Ereignisse modellieren. Bei grossem n ist die genaue Grösse (das n) der Binomialverteilung asymptotisch irrelevant. 

$$
P(X = k) = \frac{\mu^k \cdot e^{-\mu}}{k!}
$$

Annäherung der Binomialverteilung, für grosses n und kleines k. 
- $\lim_{ n \to \infty }\text{Bin}\left( n, \frac{\mu}{n} \right) = \text{Po}(\lambda)$
- $E[X] = Var[X] = \lambda$ 

> [!example]-
> Im Schnitt gibt es pro Jahr 30.000 Erkrankte. Das ist im Schnitt $\mu = \frac{30000}{365} \approx 82$ pro Tag.
> 
> **Wie gross ist die Wahrscheinlichkeit, dass an einem Tag exakt der Durchschnitt von 82 Herzinfarkten eintritt?**
> $$
> P(X = 82) = \frac{82^{82} \cdot e^{-82}}{82!} = 0,044
> $$


## Geometrische Verteilung

Wslkt, dass es erst beim k-ten Mal eintritt

$$
f_X(i) = p \cdot (1 - p)^{i-1}
$$

- $\mathbb{E}[X] = \frac{1}{p}$ (*wie viele Versuche im Schnitt. z.B. Wslkt 1/6 → 6 Versuche im Schnitt*)
- $V[X] = \frac{1-p}{p^2}$

Wslkt, **höchstens** n Versuche

$$
\begin{align}
\sum_{i=1}^{n} \Pr[X=i]
 & = \sum_{i=1}^{n} p \cdot (1-p)^{i-1} \\
 & = p \cdot \sum_{k=0}^{n-1} (1-p)^{k} \\
 & = 1 - (1-p)^n 
\end{align}
$$

 **Gedächtnislosigkeit**: Der Fakt dass ich schon 99 mal Erfolg hatte hat keinen Einfluss darauf, was beim 100. Mal passiert
[[Bildschirmfoto 2026-04-02 um 22.08.14.png|Beweis]] 

## Negative Binomialverteilung

Wslkt beim $k$-ten Wurf den $n$-ten Erfolg bei Experiment mit 2 Ausgängen

Negativ Binomialverteilt mit Ordnung n 

$$
f_X(k) = \begin{cases} \binom{k-1}{n-1} \cdot p^n \cdot (1-p)^{k-n} & \text{für } k=1,2,\dots \\ 0 & \text{sonst} \end{cases}
$$

Beispiel Münzwurf: $Pr[X = k] = \binom{k-1}{n-1} (1-p)^{k-n} p^n$
- letzter Wurf ist Erfolg
- in den $k-1$ Würfen davor $n-1$ Erfolge
- Möglichkeiten, diese $n-1$ Erfolge auf $k-1$ vorherige Würfe zu verteilen: $\binom{k-1}{n-1}$


- $\mathbb{E}[X] = \sum_{i=1}^n \mathbb{E}[X_i] = \sum_{i=1}^n \frac{1}{p} = n \cdot \frac{1}{p} = \frac{n}{p}$

![[Bildschirmfoto 2026-04-02 um 23.40.00.png]]