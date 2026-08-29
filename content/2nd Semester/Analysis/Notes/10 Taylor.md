
Einleitung

- suppose we want to approximate $\cos(x)$ at $x=0$ with a polynomial of deg 2
- we take $P(x)=c_{o}+c_{1}x+c_{2}x^2$, and get the values for $c_{i}$ by making sure the function matches $\cos(x)$ in it's value, first, and second derivative at $x=0$
- we get $P(x)=1+\left( -\frac{1}{2} \right)x^2$ 
- wir sehen, dass der teil-term mit deg n, die n-te ableitung übereinstimmen lässt. bspw., der Teil mit $c_{2}x^2$ ist für die Übereinstimmung der 2. Abeleitung zuständig. Wir können in diesem Beispiel $c_{2}$ so ausrechnen, dass wir $P(x)$ 2 mal ableiten: $P''(x)=2\cdot 1\cdot c_{2}$, und da $\cos''(0)=-\cos(0)=-1$, wollen wir $2\cdot 1\cdot c_{2}=-1$, also $2!\cdot c_{2} = -1$, somit $c_{2}=\frac{-1}{2!}$. Hier kommt also die Fakultät her

## Taylorpolynom

$$
T_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(x_0)}{k!} (x - x_0)^k
$$

## Taylorreihe

$$
\sum_{k=0}^{\infty} \frac{f^{(k)}(a)}{k!}(x-a)^k
$$

Bei diesen Funktionen dürfen wir annehmen, dass die Taylor Reihe gleich der Funktion ist. Andernfalls gilt nicht allgemein, dass wenn eine Taylorreihe konvergiert, dass sie gegen den Funktionswert konvergiert. Gegenbeispiel $e^{-\frac{1}{x}}$ ist nicht gleich ihrer Taylorreihe. 

Tylorreihe existiert nur bei ==glatten Funktionen (unendlich ableitbar)==. **NICHT** jede glatte Funktion konvergiert gegen ihre Taylorreihe. 

![[Bildschirmfoto 2026-05-02 um 16.17.46.png]]![[Bildschirmfoto 2026-05-02 um 16.17.52.png]]

## Konvergenz von Funktionenfolgen

gleichmässige Konvergenz $\implies$ punktweise Konvergenz

- **Punktweise Konvergenz:** Zu jedem $x$ und jedem $\varepsilon > 0$ gibt es ein passendes $N$, sodass $\forall n \geq N$ die Differenz von der Funktionenfolge zu dem Funktionswert kleiner als $\varepsilon$. 
  
  Fixiere beliebiges x und zeige, dass Grenzwert für $n \to \infty$ existiert. Definiere $f(x)$ die Grenzfunktion, mit den Grenzwerten; kann abhängig von x sein. 
  
- **Gleichmässige Konvergenz:** Zu jedem $\epsilon > 0$ gibt es ein $N$, das für _alle_ $x$ gleichzeitig funktioniert. 
  Zeige 

$$
\lim_{n \to \infty} \left( \sup_{x \in D} |f_n(x) - f(x)| \right) = 0
$$
   

![[Bildschirmfoto 2026-05-04 um 17.38.17.png]]![[Bildschirmfoto 2026-05-04 um 17.48.19.png]]![[Bildschirmfoto 2026-05-04 um 17.49.43.png]]