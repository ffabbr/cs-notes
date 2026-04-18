
## Markov-Ungleichung:

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

## Chernoff

Für $X_{i}$ unabhängig und **Bernoulli-Verteilt** und $X= \sum X_{i}$ 

![[Bildschirmfoto 2026-04-16 um 17.25.42.png]]
![[Bildschirmfoto 2026-04-16 um 20.35.24.png]]

