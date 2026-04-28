
> [!info]- Funktion mit Tangente lokal approximieren
> 
> Gleichung der Tangente:
> 
> $$
> \begin{align}
> y & =f'(x_{0})\cdot x + f(x_{0})-f'(x_{0})\cdot x_{0} \\
>  & = f'(x_{0})\cdot x + f(x_{0}) - f'(x_{0})\cdot x_{0}
> \end{align}
> $$
> Also
> $$
> f(x) \approx f(x_{0}) + f'(x_{0})(x-x_{0})
> $$
> 
> Bessere Approximierung mit quadratischer Funktion.
> A,B,C sind Konstanten, sodass die Funktion an $x_{0}$ übereinstimmt mit Approximierung in
> - Funktionswert
> - 1. Ableitung
> - 2. Ableitung
> 
> $$
> P_2(x) = A(x-x_0)^2 + B(x-x_0) + C
> $$
> Durch umformen kommen wir auf A, B, C
> $$
> f(x) \approx f(x_0) + f'(x_0)(x-x_0) + \frac{1}{2}f''(x_0)(x-x_0)^2
> $$

## Taylorpolynom

- Approximierung P
- $deg(P_{n}(x)) \leq n$
- m. Taylorpolynom gibt Polynom von deg m wieder

$$
T_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(x_0)}{k!} (x - x_0)^k
$$

## Taylorreihe

$$
\sum_{k=0}^{\infty} f^{(k)}(a) \frac{1}{k!}(x-a)^k
$$