
| $x$         | $-\sqrt{3}$       | $-1$              | $-\dfrac{\sqrt{3}}{2}$ | $-\dfrac{\sqrt{2}}{2}$ | $-\dfrac{1}{\sqrt{3}}$ | $-\dfrac{1}{2}$   | $0$              | $\dfrac{1}{2}$   | $\dfrac{1}{\sqrt{3}}$ | $\dfrac{\sqrt{2}}{2}$ | $\dfrac{\sqrt{3}}{2}$ | $1$              | $\sqrt{3}$       |
| ----------- | ----------------- | ----------------- | ---------------------- | ---------------------- | ---------------------- | ----------------- | ---------------- | ---------------- | --------------------- | --------------------- | --------------------- | ---------------- | ---------------- |
| $\arccos x$ | undef.            | $\pi$             | $\dfrac{5\pi}{6}$      | $\dfrac{3\pi}{4}$      | —                      | $\dfrac{2\pi}{3}$ | $\dfrac{\pi}{2}$ | $\dfrac{\pi}{3}$ | —                     | $\dfrac{\pi}{4}$      | $\dfrac{\pi}{6}$      | $0$              | undef.           |
| $\arcsin x$ | undef.            | $-\dfrac{\pi}{2}$ | $-\dfrac{\pi}{3}$      | $-\dfrac{\pi}{4}$      | —                      | $-\dfrac{\pi}{6}$ | $0$              | $\dfrac{\pi}{6}$ | —                     | $\dfrac{\pi}{4}$      | $\dfrac{\pi}{3}$      | $\dfrac{\pi}{2}$ | undef.           |
| $\arctan x$ | $-\dfrac{\pi}{3}$ | $-\dfrac{\pi}{4}$ | —                      | —                      | $-\dfrac{\pi}{6}$      | —                 | $0$              | —                | $\dfrac{\pi}{6}$      | —                     | —                     | $\dfrac{\pi}{4}$ | $\dfrac{\pi}{3}$ |

| $\varphi$     | $0$ | $\dfrac{\pi}{6}$      | $\dfrac{\pi}{4}$      | $\dfrac{\pi}{3}$      | $\dfrac{\pi}{2}$ | $\pi$ | $\dfrac{3\pi}{2}$ | $2\pi$ |
| ------------- | --- | --------------------- | --------------------- | --------------------- | ---------------- | ----- | ----------------- | ------ |
| $\cos\varphi$ | $1$ | $\dfrac{\sqrt{3}}{2}$ | $\dfrac{\sqrt{2}}{2}$ | $\dfrac{1}{2}$        | $0$              | $-1$  | $0$               | $1$    |
| $\sin\varphi$ | $0$ | $\dfrac{1}{2}$        | $\dfrac{\sqrt{2}}{2}$ | $\dfrac{\sqrt{3}}{2}$ | $1$              | $0$   | $-1$              | $0$    |
| $\tan\varphi$ | $0$ | $\dfrac{1}{\sqrt{3}}$ | $1$                   | $\sqrt{3}$            | undef.           | $0$   | undef.            | $0$    |

## Negative Winkel

$\cos(-\varphi)=\cos(\varphi)$  
$\sin(-\varphi)=-\sin(\varphi)$

![[Pasted image 20260427162909.png]]
![[2nd Semester/Analysis/Slides/02 Slides.pdf#page=3]]

## Additionstheoreme

$$
 \tan(x + y) = \frac{\tan(x) + \tan(y)}{1 - \tan(x)\cdot \tan(y)} 
 $$
$$
 \tan(x - y) = \frac{\tan(x) - \tan(y)}{1 + \tan(x)\cdot \tan(y)} 
 $$

$$
 \sin(x + y) = \sin(x)\cos(y) + \cos(x)\sin(y) 
 $$
$$
 \sin(x - y) = \sin(x)\cos(y) - \cos(x)\sin(y) 
 $$

$$
 \cos(x + y) = \cos(x)\cos(y) - \sin(x)\sin(y) 
 $$
$$
 \cos(x - y) = \cos(x)\cos(y) + \sin(x)\sin(y) 
 $$

## Hyperbolicus

$$
\sinh(x) = \frac{e^x - e^{-x}}{2}
$$

$$
\cosh(x) = \frac{e^x + e^{-x}}{2}
$$

$$
\tanh(x) = \frac{\sinh(x)}{\cosh(x)} = \frac{e^x - e^{-x}}{e^x + e^{-x}}
$$

Da Hyperbelfunktionen keine periodischen Kreiswinkel abbilden, gibt es keine klassische $\pi$\-Tabelle. Wichtig sind die Werte an der Stelle $0$:

$$
\sinh(0) = 0
$$

$$
\cosh(0) = 1
$$

$$
\tanh(0) = 0
$$

### Symmetrie (Negative Argumente)

$$
\cosh(-\varphi) = \cosh(\varphi)
$$

$$
\sinh(-\varphi) = -\sinh(\varphi)
$$

$$
\tanh(-\varphi) = -\tanh(\varphi)
$$

### Fundamentalbeziehung (Trigonometrischer Pythagoras für Hyperbeln)

$$
\cosh^2(x) - \sinh^2(x) = 1
$$

### Additionstheoreme

$$
\sinh(x + y) = \sinh(x)\cosh(y) + \cosh(x)\sinh(y)
$$

$$
\sinh(x - y) = \sinh(x)\cosh(y) - \cosh(x)\sinh(y)
$$

$$
\cosh(x + y) = \cosh(x)\cosh(y) + \sinh(x)\sinh(y)
$$

$$
\cosh(x - y) = \cosh(x)\cosh(y) - \sinh(x)\sinh(y)
$$

$$
\tanh(x + y) = \frac{\tanh(x) + \tanh(y)}{1 + \tanh(x)\cdot \tanh(y)}
$$

$$
\tanh(x - y) = \frac{\tanh(x) - \tanh(y)}{1 - \tanh(x)\cdot \tanh(y)}
$$

