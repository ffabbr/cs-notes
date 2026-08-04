
1. [[#Markov-Ungleichung]]
2. [[#Chebyshev Ungleichung]]
3. [[#Chernoff]]

## Markov Ungleichung:

- **==nicht-negative==** Zufallsvariable X (Achtung, kann man die Zufallsvariable so anpassen, dass sie positiv wird?)
- alle $t > 0$

$$
\Pr[X \ge t] \le \frac{\mathbb{E}[X]}{t}
$$
$$
\Pr \left( X \geq t \cdot \mathbb{E}[X] \right) \leq \frac{1}{t}
$$

Beweis: [[Markov Beweis.png]]

## Chebyshev Ungleichung

- beliebige Zufallsvariable X
- alle $t > 0$
- Varianz gegeben, ev. Umformen zu $\leq$ mit Betrag

$$
\Pr[ |X - E[X]| \ge t ] \le \frac{Var[X]}{t^2}
$$

$$
\Pr\left[ |X - \mathbb{E}[X]| \geq t \cdot \sigma \right] \leq \frac{1}{t^2}
$$
Es ist unwahrscheinlich, dass die Werte von X weiter als t Standardabweichungen vom EW entfernt sind.

![[Bildschirmfoto 2026-04-16 um 20.35.08.png]]

## Chernoff Ungleichung

Für $X_{i}$ unabhängig und **Bernoulli-Verteilt** und $X= \sum X_{i}$ 

![[Bildschirmfoto 2026-04-30 um 16.40.51.png]]

Beispiel aus dem Miniquiz 5: 

Wenn ein probabilistischer Algorithmus mit einer Wahrscheinlichkeit von mindestens $2/3$ eine korrekte JA/NEIN-Antwort liefert und wir ihn unabhängig $n$-mal ausführen, ist die Wahrscheinlichkeit, dass er mehr als $n/2$ Mal eine falsche Antwort gibt, kleiner als $e^{-0.001n}$.

![[Bildschirmfoto 2026-04-30 um 17.08.53.png]]

---

![[Bildschirmfoto 2026-04-16 um 20.35.24.png]]

![[Bildschirmfoto 2026-04-23 um 12.40.50.png]]