## Unabhängigkeit 

Ereignisse $A_1, \dots, A_n$ sind unabhängig  $\iff$ Indikatorvariablen $I_{A_1}, \dots, I_{A_n}$ sind unabhängig

$$
\Pr[I_{A_1} = \alpha_1, \dots, I_{A_n} = \alpha_n] = \Pr[I_{A_1} = \alpha_1] \cdot \ ...\ \cdot \Pr[I_{A_n} = \alpha_n]
$$

### Unabhängigkeit mit Mengen

 $X_{i}$ unabhängige Zufallsvariablen, $S_{i}$ beliebige Mengen
$$
\Pr[X_1 \in S_1, \dots, X_n \in S_n] = \Pr[X_1 \in S_1] \cdot \dots \cdot \Pr[X_n \in S_n]
$$
Die Wahrscheinlichkeit, dass $X_1$ in einer bestimmten Menge $S_1$ landet **und** $X_2$ in einer Menge $S_2$ landet, ist genau das Produkt der Wahrscheinlichkeiten, dass jedes $X$ in seiner jeweiligen Menge landet.

> [!example]- Proof
> **Erklärung**
> 1. Wahrscheinlichkeit, dass unsere Variablen in den Mengen $S_1$ bis $S_n$ landen. Alle möglichen Kombinationen von konkreten Werten ($\alpha_1, \dots, \alpha_n$), die in diesen Mengen liegen, und addiert deren Wslkt auf:  $\sum_{\alpha_1 \in S_1} \dots \sum_{\alpha_n \in S_n} \Pr[X_1 = \alpha_1, \dots, X_n = \alpha_n]$
> 2. Voraussetung Unabhängigkeit
> 3. Distributivgesetz (Umsortieren/Ausklammern)
> 4. Summe der Wahrscheinlichkeiten der Einzelwerte, die in $S_1$ liegen, aufaddiert, ist Gesamtwslkt, dass $X_1$ in $S_1$ 
> 
> ![[Bildschirmfoto 2026-04-12 um 09.41.51.png|Beweis]]

### Teilmengen von unabhängigen Zufallsvariablen sind unabhängig

> [!example]- Proof
> Sei $S_i = \begin{cases} \{\alpha_i\} & \text{falls } i \in I \\ \text{gesamter Wertebereich} & \text{sonst} \end{cases}$. 
> 
> 1. Wahrscheinlichkeit, dass Teilmenge genau die vorgegebenen Werte annimmt: $\Pr[X_{i_1} = \alpha_{i_1}, \ldots, X_{i_k} = \alpha_{i_k}]$
> 2. Um die restlichen Variablen (nicht in I) erweitern. Die nehmen mit 100% einen Wert aus $S_{i}$ (da Definition). $\Pr[X_1 \in S_1, \ldots, X_n \in S_n]$
> 3. Unabhängigkeit: $\Pr[X_1 \in S_1] \cdot \ldots \cdot \Pr[X_n \in S_n]$
> 4. Für alle Variablen, die nicht in $I$ sind, ist Wslkt 1, Faktoren fallen also weg. Für die Variablen, die in $I$ sind, ist $S_i = \{\alpha_i\}$, aus $\Pr[X_i \in S_i]$ also $\Pr[X_i = \alpha_i]$.
> 
> ![[Bildschirmfoto 2026-04-12 um 09.42.20.png|Beweis]]

## Summe von Zufallsvariablen

Berechnung der Wahrscheinlichkeitsfunktion der Summe zweier unabhängiger, diskreter Zufallsvariablen

$Z := X + Y$
$$
f_Z(\alpha) = \sum_{\beta \in W_X} f_X(\beta) \cdot f_Y(\alpha - \beta)
$$

$f$: Wahrscheinlichkeit, dass $\alpha = Z$, und $Z=X+Y$. Wir summieren über alle Kombinationen, sodass $\alpha = Z$ rauskommt. Wslkt, dass X eine Zahl ist und Y dann auffüllt sodass insgesamt $Z$ rauskommt. 

> [!example]- Proof
> **Beweis**: 
> 
> 1. $f_Z(\alpha) = \Pr[X+Y = \alpha]$ (Definition Z)
> 2. $= \sum_{\beta \in W_X} \Pr[X = \beta \text{ und } Y = \alpha - \beta]$ (Satz von der totalen Wahrscheinlichkeit)
> 3. $= \sum_{\beta \in W_X} \Pr[X = \beta] \cdot \Pr[Y = \alpha - \beta]$ (Unabhängigkeit X und Y)
> 4. Umwandeln zurück in Funktionsschreibweise $f_X(\beta)$ und $f_Y(\alpha - \beta)$. 

**Beispiel**
X, Y unabhängig. Wenn $X \sim \text{Po}(\lambda)$ ([[13 Verteilungen#Poisson-Verteilung|Poisson-Verteilung]]) und $Y \sim \text{Po}(\mu)$, dann gilt $X + Y \sim \text{Po}(\lambda + \mu)$ 

## Rechenregeln bei mehreren Zufallsvariablen

- $\mathbb{E}[X \cdot Y] = \mathbb{E}[X] \cdot \mathbb{E}[Y]$ ==wenn unabhängig==
- $\mathbb{E}[X + Y] = \mathbb{E}[X] + \mathbb{E}[Y]$ (immer)
- $\text{Var}[X + Y] = \text{Var}[X] + \text{Var}[Y]$  ==wenn unabhängig==
- Var multipliziert gilt nicht

> [!example]- Proofs
> 
> **Multiplikativität des Erwartungswerts wenn Unabhängigkeit**
> 
> ![[Bildschirmfoto 2026-04-12 um 11.34.10.png]]
> 
> **Additivität der Varianz wenn Unabhängigkeit**
> 
> Nutze Formel $\text{Var}[X] = \mathbb{E}[X^2] - (\mathbb{E}[X])^2$ (siehe [[10 Zufallsvariable, Erwartungswert, Varianz#Varianz|Varianz]]) wiederholt
> 
> ![[Bildschirmfoto 2026-04-12 um 11.41.15.png]]


---

## Waldsche Identität

N und X **unabhängige** Zufallsvariablen. 

- N ist die Anzahl
- X ist ein Experiment, dass wir N mal machen

Wir wollen den EW für Z (Gesamtzahl der geworfenen "Köpfe") $Z := \sum_{i=1}^{N} X_i$

$$
\mathbb{E}[Z] = \mathbb{E}[N] \cdot \mathbb{E}[X]
$$

> [!example]- Proofs
> Beweis mit dem [[08 Bedingte Wahrscheinlichkeit#Gesetz des totalen Erwartungswerts|Erwartungswert bei bedingter Wahrscheinlichkeit]]:  
> 
> ![[Bildschirmfoto 2026-04-15 um 15.48.19.png]]

