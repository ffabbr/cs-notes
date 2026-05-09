
1. [[#Zufallsvariable]]
2. [[#Erwartungswert]]
3. [[#Varianz]]

## Zufallsvariable

Weist Versuchsausgängen eine Zahl zu. z.B. Anzahl Kopf bei Münzwurf. 

---

## Erwartungswert

wahrscheinlichkeits-gewichteter Durchschnitt basically

- $E[X] + E[Y] = E[X+Y]$
- $\lambda E[X] = E[\lambda X]$
- $E[x+b] = E[x] + E[b] = E[x] + b$

### Formeln

#### Formel 1 Erwartungswert: 

$$
\mathbb{E}[X] = \sum_{\omega \in \Omega} X(\omega) \cdot \Pr[\omega]
$$

#### Formel 2 (äquivalent):

$$
\mathbb{E}[X] := \sum_{\alpha \in W_X} \alpha \cdot \Pr[X = \alpha]
$$
Bedingt: 
$$
E[X|A] = \sum_{\alpha \in W_x} \alpha \cdot Pr[X=\alpha | A]
$$

> [!example]- Proof
> **Beweis der Äquivalenz**: 
> 
> ![[Bildschirmfoto 2026-03-27 um 15.07.07.png]]

> [!example]- Vergleich Formel 1 und 2
> Zweifacher Münzwurf
> 
> Wir werfen zwei faire Münzen. $X$ sei die Anzahl der Köpfe ($K$).
> 
> - $\Omega = \{ (K,K), (K,Z), (Z,K), (Z,Z) \}$ mit jeweils $\Pr[\omega] = \frac{1}{4}$.
> - $W_X = \{0, 1, 2\}$.
> 
> **Berechnung nach Formel 1 (jedes Ereignis einzeln):**
> 
> $$\mathbb{E}[X] = X(K,K) \cdot \frac{1}{4} + X(K,Z) \cdot \frac{1}{4} + X(Z,K) \cdot \frac{1}{4} + X(Z,Z) \cdot \frac{1}{4}$$
> 
> $$\mathbb{E}[X] = 2 \cdot \frac{1}{4} + 1 \cdot \frac{1}{4} + 1 \cdot \frac{1}{4} + 0 \cdot \frac{1}{4} = 1$$
> 
> **Berechnung nach Formel 2 (Werte gruppiert):**
> 
> - $\Pr[X=0] = \Pr[(Z,Z)] = \frac{1}{4}$
> - $\Pr[X=1] = \Pr[(K,Z), (Z,K)] = \frac{2}{4}$
> - $\Pr[X=2] = \Pr[(K,K)] = \frac{1}{4}$
> 
> $$\mathbb{E}[X] = 0 \cdot \frac{1}{4} + 1 \cdot \frac{2}{4} + 2 \cdot \frac{1}{4} = 1$$

#### Formel 2 mit Indikatorvariable

$$
\mathbb{E}[X_A] = \Pr[A] = 0 \cdot \Pr[X_A = 0] + 1 \cdot \Pr[X_A = 1]
$$

#### Tail Sum Formula

==Bedingung:==  Wertebereich von $X$ ist $\subseteq \mathbb{N}_{0}$.

$$
\mathbb{E}[X] = \sum_{i=1}^{\infty} \Pr[X \ge i]
$$

"mindestens" einfacher als genauen Wert zu bestimmen, aka Gegenwahrscheinlichkeit. Remember, $\Pr[X \geq i] = 1 - \Pr[X \leq i-1]$

> [!info]- Beweis
> [[Bildschirmfoto 2026-03-27 um 15.23.51.png|Beweis]]
> Wir beginnen mit der klassischen Definition von dem Erwartungswert. 
> 1. Orange: Statt $\Pr[X=i]$  mal $i$ zurechnen, notieren wir es als $i$ mal addiert
> 2. Rot: Wir schreiben die Summe aller Paare $(i,j)$ mit $j \leq i$ um
> 3. Grün: wir vereinfachen mit $X \geq j$

**Beispiel für Formel 3**

![[Bildschirmfoto 2026-03-27 um 16.07.06.png]]


![[08 Bedingte Wahrscheinlichkeit#Bedingte Zufallsvariable]]

## Varianz

Quadratische Abweichung einer Zufallsvariable vom Erwartungswert. $\mu = \mathbb{E}[X]$. Die Standardabweichung ist die Wurzel der Varianz $\sigma = \sqrt{V(X)}$.

$$
\text{Var}[X] = \mathbb{E}[X^2] - (\mathbb{E}[X])^2
$$

$$
\text{Var}[X] = \mathbb{E}\left[(X - \mathbb{E}[X])^2\right]
$$

> [!info]- Herleitung
> $$
> \begin{align}
> \sigma^2 &= \mathbb{E}\left[(X - \mu)^2\right] \\
> &= \mathbb{E}\left[X^2 - 2X\mu + \mu^2\right] \\
> &= \mathbb{E}[X^2] - \mathbb{E}[2X\mu] + \mathbb{E}[\mu^2] \\
> &= \mathbb{E}[X^2] - 2\mu \mathbb{E}[X] + \mu^2 \\
> &= \mathbb{E}[X^2] - 2\mu^2 + \mu^2 \\
> &= \mathbb{E}[X^2] - \mu^2
> \end{align}
> $$


- $\text{Var}[a \cdot X + b]$ ist unabhängig von $b$
- $\text{Var}[a \cdot X] = a^2 \cdot \text{Var}[X]$
- $\text{Var}[X + Y] = \text{Var}[X] + \text{Var}[Y]$  ==wenn unabhängig==

## Momente

![[Bildschirmfoto 2026-04-02 um 17.47.40.png]]