
## Markov-Ungleichung:

- **nicht-negative** Zufallsvariable X
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
$$
\Pr[ |X - E[X]| \ge t ] \le \frac{Var[X]}{t^2}
$$
$$
\Pr\left[ |X - \mathbb{E}[X]| \geq t \cdot \sigma \right] \leq \frac{1}{t^2}
$$
