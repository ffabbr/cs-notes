**Leibniz-Formel**

- → siehe [[05 Kofaktoren]] 
- Möglichkeit, mit [[Gauss and Gauss-Jordan|Gauss-Elimination]] in eine triangular Matrix umzustellen und dann det einfach zu berechnen. Die Determinante ändert sich nicht bei row operations, ausser beim swappen ändert sich das Vorzeichen der det.
- Sonst (Def.7.2.3): 
$$\det(A) = \sum_{\sigma \in \Pi_n} \text{sgn}(\sigma) \prod_{i=1}^{n} A_{i, \sigma(i)}$$
$\Pi_n$: Menge aller Permutationen ("alle Möglichkeiten, die Zahlen $1$ bis $n$ durcheinanderzuwürfeln")
$\prod_{i=1}^{n} A_{i, \sigma(i)}$: pro Zeile wählen wir einen Eintrag, bestimmt von $\sigma$.

> [!abstract]- Logik bei einer $3 \times 3$ Matrix
> Nehmen wir an, wir haben eine Permutation $\sigma$, die $(1, 2, 3)$ zu $(2, 3, 1)$ vertauscht. Das heißt:
> - $\sigma(1) = 2$
> - $\sigma(2) = 3$
> - $\sigma(3) = 1$
> 
> Wenn wir das in deine Formel ($\prod_{i=1}^{3} A_{i, \sigma(i)}$) einsetzen
> 
> 1. $i=1$: Wir sind in Zeile 1. Die Permutation sagt Spalte 2 ($\sigma(1)=2$). Element: $A_{1,2}$
> 2. $i=2$: Wir sind in Zeile 2. Die Permutation sagt Spalte 3 ($\sigma(2)=3$). Element: $A_{2,3}$
> 3. $i=3$: Wir sind in Zeile 3. Die Permutation sagt Spalte 1 ($\sigma(3)=1$). Element: $A_{3,1}$
> 
> Das Produkt für diese spezielle Permutation ist also: $A_{1,2} \cdot A_{2,3} \cdot A_{3,1}$.

Skript: 

![[Pasted image 20251206162216.png]]

### Permutationsfunktion Sigma

$\sigma(a)=b$ nimmt das a-te Element und ersetzt es mit b, wobei b ein anderes Element in der Reihe ist (nicht irgendein Element). Kann nur swapen. 

z.B. 

1 | 2 | 3 | 4 | 5
1 | 3 | 2 | 5 | 4

$\sigma(1)=1$, $\sigma(2)=3$, etc.

Es gibt also immer Paare die sich geändert haben. 

### Signum

**Wozu?** Vorzeichen bei Formel für Determinante richtig behalten, pro swap ändert sich ja das Vorzeichen. Siehe oben. Signum keeps track of that:

$\text{sgn}(\sigma)$ = 1 wenn ***gerade* Anzahl an Paaren** geändert wurden.
$\text{sgn}(\sigma)$ = -1 wenn ***ungerade* Anzahl an Paaren** geändert wurden.

Gegeben Permutationsmatrix mit Permutation $\sigma$, dann $\det(a)=\text{sgn}(\sigma)$. Beispiel: 

$\begin{bmatrix}1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0\end{bmatrix} \implies \text{sgn}(\sigma)=-1 \implies \det=-1$ 

![[Proposition 7.2.4.png]]
