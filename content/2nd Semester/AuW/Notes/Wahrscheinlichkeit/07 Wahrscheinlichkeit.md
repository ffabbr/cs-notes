## Gymi thoughts

- Versuche als Baum darstellen, multiplizieren oder addieren
- Günstige durch Mögliche
- bei [[08 Bedingte Wahrscheinlichkeit|bedingter Wahrscheinlichkeit]] eine Tabelle machen
- $P(E_1 | E_2) = \frac{P(E_1 \wedge E_2)}{P(E_2)}$ 
- $P(E_1 \wedge E_2) = P(E_1) \cdot P(E_2 | E_1)$
- Einander ausschliessende Ereignisse (disjunkt): [[#Vereinigung von Ereignissen]]: $P(E_1 \vee E_2) = P(E_1) + P(E_2)$
- Unabhängigkeit prüfen $P(E_1 \wedge E_2) = P(E_1) \cdot P(E_2)$
- [[#Laplace]]: alles gleich Wahrscheinlich
- wenn z.B. "mindestens", nutze Gegenwahrscheinlichkeit

## Introduction

Ein **diskreter Wahrscheinlichkeitsraum** hat eine ==Ergebnismenge== $\Omega$ von Elementareineignissen $\omega_{i}$ mit je einer Wahrscheinlichkeit $P[\omega_{i}]$. Alle Wahrscheinlichkeiten addieren sich zu 1 auf. 

Ein **Ereignis** E, oder oft $A_{i}$ ist eine Teilmenge von der Ergebnismenge. Die Wahrscheinlichkeit ist die Summe aller Wahrscheinlichkeiten aller Elementarereignisse die Teil des Ereignisses sind. Vgl. Komplementärereignis $\overline{E} = \Omega \setminus E$. 

$$
\Pr[\overline{A} \cap B] = \Pr[B] - \Pr[A \cap B]
$$

$$
Pr[B] = Pr[B|A] \cdot Pr[A] + Pr[B|\bar{A}] \cdot Pr[\bar{A}]
$$

Out-of-context fun fact: 
$$
1-x \approx e^{-x}
$$

**Für Ereignisse A, B gilt:**

1. $\text{Pr}[\emptyset] = 0, \text{Pr}[\Omega] = 1$.
2. $\text{Pr}[\bar{A}] = 1 - \text{Pr}[A]$.
3. Wenn $A \subseteq B$, dann $Pr[A] \leq Pr[B]$

> [!info]- Binomialkoeffizient, Formel
> $$
> \binom{n}{k} = \frac{n!}{k! \cdot (n - k)!}
> $$

## Laplace

In einem **Laplace-Raum** sind alle Elementarereignisse gleich wahrscheinlich. Somit 
$$
\Pr[E]=\frac{|E|}{|\Omega|}
$$

$\Omega$ berechnen: z.B. 3 Mal Münze werfen: $2^3$. (Anzahl der möglichen Outcomes)

## Vereinigung von Ereignissen

Wenn die Ereignisse $A_1, \dots, A_n$ **paarweise disjunkt** sind, gilt. 
$$ \text{Pr}\left[\bigcup_{i=1}^{n} A_i\right] = \sum_{i=1}^{n} \text{Pr}[A_i]. $$
Das geht analog genauso auch für eine unendliche Menge von disjunkten Ereignissen. 

Wenn sie **nicht disjunkt sind**, dann Siebformel. 

$$
\begin{align}
Pr[A \cup B]  & = Pr[A] + Pr[B] - Pr[A \cap B] \\
 &  \leq Pr[A] + Pr[B]
\end{align}
$$

![[Bildschirmfoto 2026-03-18 um 11.39.23.png]]

![[Bildschirmfoto 2026-03-17 um 15.53.41.png]]

## Siebformel

![[Bildschirmfoto 2026-03-23 um 09.58.22.png]]


### Beweis für die Siebformel

> [!info] Allgemeine Binomische Formel
> $$
> (x-y)^k = x^k - k \cdot x^{k-1} \cdot y + \binom{k}{2} \cdot x^{k-2} \cdot y^2 - \binom{k}{3} x^{k-3} \cdot y^3 + \dots (-1)^k \binom{k}{k} y^k
> $$

![[Quick sheets - Seite 31.svg]]

### Beispiel, Kartendeck

> [!abstract]- Einleitung
> Wir mischen ein Kartenspiel und geben Spieler 1 und Spieler 2 jeweils 5 Karten. **Wahrscheinlichkeit: Spieler 1 hat 4 Asse.** $\Omega = \{ (X,Y) : X, Y \subseteq C, X \cap Y = \emptyset, |X| = |Y| = 5 \}$. Günstige durch Mögliche: 
> $$
> Pr[A] = \frac{48 \cdot \binom{47}{5}}{\binom{52}{5} \cdot \binom{47}{5}}
> $$

Wir mischen ein Deck von n Karten. 

![[Bildschirmfoto 2026-03-23 um 10.26.23.png]]
