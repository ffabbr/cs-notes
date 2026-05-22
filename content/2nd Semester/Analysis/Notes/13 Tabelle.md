
> [!error]
> DON'T FORGETT `+C` at the Stammfunktion!!

### 1. Allgemeine Rechenregeln

| **Funktion**    | **Ableitung             | **Stammfunktion**                |
| --------------- | ----------------------- | -------------------------------- |
| $k \cdot f(x)$  | $k \cdot f'(x)$         | $k \cdot F(x)$                   |
| $f(x) \pm g(x)$ | $f'(x) \pm g'(x)$       | $F(x) \pm G(x)$                  |
| $f(k \cdot x)$  | $k \cdot f'(k \cdot x)$ | $\frac{1}{k} \cdot F(k \cdot x)$ |

### 2. Polynome und Potenzfunktionen

| **Funktion f(x)**         | **Ableitung f′(x)**       | **Stammfunktion F(x)**                     |
| ------------------------- | ------------------------- | ------------------------------------------ |
| $k$                       | $0$                       | $k \cdot x$                                |
| $mx + b$                  | $m$                       | $\frac{1}{2}mx^2 + bx$                     |
| $x^n$                     | $n \cdot x^{n-1}$         | $\frac{x^{n+1}}{n+1}$ _(für $n \neq -1$)_  |
| $a \cdot x^p$             | $a \cdot p \cdot x^{p-1}$ | $\frac{a}{p+1}x^{p+1}$ _(für $p \neq -1$)_ |
| $\frac{1}{x}$ ($=x^{-1}$) | $-\frac{1}{x^2}$          | $\ln(\left\vert x \right\vert)$            |
| $\frac{a}{x}$             | $-\frac{a}{x^2}$          | $a \cdot \ln(\left\vert x \right\vert)$    |
| $\sqrt{x}$                | $\frac{1}{2\sqrt{x}}$     | $\frac{2}{3}x\sqrt{x}$                     |


### 3. Exponential- und Logarithmusfunktionen

|**Funktion f(x)**|**Ableitung f′(x)**|**Stammfunktion F(x)**|
|---|---|---|
|$e^x$|$e^x$|$e^x$|
|$2e^x$|$2e^x$|$2e^x$|
|$a^x$|$\ln(a)\cdot a^x$|$\frac{a^x}{\ln(a)}$|
|$e^{u(x)}$|$u'(x)\cdot e^{u(x)}$|$\int e^{u(x)} dx$|
|$\ln(x)$|$\frac{1}{x}$|$x\ln(x) - x$|
|$\log_a(x)$|$\frac{1}{x\ln(a)}$|$\frac{x\ln(x) - x}{\ln(a)}$|
|$x^x$|$x^x(\ln(x)+1)$|$\int x^x dx$|

### 4. Trigonometrische und Hyperbelfunktionen

| **Funktion f(x)**          | **Ableitung f′(x)**                   | **Stammfunktion F(x)**                               |
| -------------------------- | ------------------------------------- | ---------------------------------------------------- |
| $\sin(x)$                  | $\cos(x)$                             | $-\cos(x)$                                           |
| $\cos(x)$                  | $-\sin(x)$                            | $\sin(x)$                                            |
| $\tan(x)$                  | $\frac{1}{\cos^2(x)} = 1+\tan^2(x)$   | $-\ln(\left\vert \cos(x) \right\vert)$               |
| $\cot(x)$                  | $-\frac{1}{\sin^2(x)}$                | $\ln(\left\vert \sin(x) \right\vert)$                |
| $\sinh(x)$                 | $\cosh(x)$                            | $\cosh(x)$                                           |
| $\cosh(x)$                 | $\sinh(x)$                            | $\sinh(x)$                                           |
| $\tanh(x)$                 | $\frac{1}{\cosh^2(x)} = 1-\tanh^2(x)$ | $\ln(\cosh(x))$                                      |
| $\coth(x)$                 | $1-\coth^2(x)$                        | $\ln(\left\vert \sinh(x) \right\vert)$               |
| $\arcsin(x)$               | $\frac{1}{\sqrt{1-x^2}}$              | $x \arcsin(x) + \sqrt{1-x^2}$                        |
| $\arccos(x)$               | $-\frac{1}{\sqrt{1-x^2}}$             | $x \arccos(x) - \sqrt{1-x^2}$                        |
| $\arctan(x)$               | $\frac{1}{1+x^2}$                     | $x \arctan(x) - \frac{1}{2}\ln(1+x^2)$               |
| $\text{arccot}(x)$         | $-\frac{1}{1+x^2}$                    | $x \text{arccot}(x) + \frac{1}{2}\ln(1+x^2)$         |
| $\operatorname{arsinh}(x)$ | $\frac{1}{\sqrt{1+x^2}}$              | $x \operatorname{arsinh}(x) - \sqrt{x^2+1}$          |
| $\operatorname{arcosh}(x)$ | $\frac{1}{\sqrt{x^2-1}}$              | $x \operatorname{arcosh}(x) - \sqrt{x^2-1}$          |
| $\operatorname{artanh}(x)$ | $\frac{1}{1-x^2}$                     | $x \operatorname{artanh}(x) + \frac{1}{2}\ln(1-x^2)$ |
