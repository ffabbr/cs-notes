Computer können nur endlich viele Zahlen darstellen, alle anderen werden approximiert. Die Abstände zwischen den Maschinenzahlen sind für grosse Zahlen größer . 

- Beim Subtrahieren ähnlich großer Zahlen vergrößert sich der Fehler
- Fehler reduzieren: 
$$
\begin{align*} \sqrt{1+x^2} + x &= \frac{(\sqrt{1+x^2} + x)(\sqrt{1+x^2} - x)}{\sqrt{1+x^2} - x} \\ &= \frac{1}{\sqrt{1+x^2} - x} \end{align*}
$$

- **Mantisse:** $\underbrace{0,1000}_{\text{Mantisse, normalisiert}} \cdot 10^3$
- z.B. $B=10, -1 \leq \exp \leq 4, M=4$ 
	- min: $0,1000 \cdot 10^{-1}$
	- max: $0,9999 \cdot 10^4$ 