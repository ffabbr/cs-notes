
Seien $A$ und $B$ Ereignisse mit $\Pr[B] > 0$.
Die bedingte Wahrscheinlichkeit $\Pr[A|B]$von $A$ gegeben $B$ ist definiert durch

$$
\Pr[A|B] := \frac{Pr[A \cap B]}{Pr[B]}
$$

> [!success] Allgemein
> - $\Pr[A|\Omega] = \Pr[A]$
> - $\Pr[A|A] = 1$
> - $\Pr[A|\bar{A}] = 0$
> - $\Pr[A \cap B] = \Pr[A|B] \cdot \Pr[B] = \Pr[B|A] \cdot \Pr[A]$

> [!example]- 2-Kinder-Problem
> Familie hat 2 Kinder, mindestens ein Kind ist ein Mädchen. Was ist die Wahrscheinlichkeit, dass das andere Kind auch ein Mädchen ist. 
> 
> $\Omega = \{mm, mw, wm, ww\}$
>
> Ergeignis A: Beide Mädchen {ww}. $\Pr[A] = \frac{1}{4}$
> Ereignis B: Mindestens 1 Mädchen. $\Pr[B] = \frac{3}{4}$
>
> $\Pr[A|B] = \frac{1/4}{3/4} = \frac{1}{3}$


## Multiplikationssatz 

Wahrscheinlichkeit, dass mehrere Ereignisse zusammen (oder nacheinander) eintreten:

1. Wie wahrscheinlich ist das erste Ereignis?
2. Wie wahrscheinlich ist das zweite, **unter der Bedingung**, dass das erste schon passiert ist?
3. Wie wahrscheinlich ist das dritte, wenn die ersten beiden schon passiert sind? ... und so weiter.

![[Bildschirmfoto 2026-03-23 um 11.27.38.png]]

> [!example] Geburtstagsproblem
> Wahrscheinlichkeit, dass mindestens 2 Personen von m gleichen Geburtstag haben. Gegenwahrscheinlichkeit, alle haben unterschiedlichen Geburtstag. Erste Person hat $\frac{365}{365}$ Möglichkeiten, 2. hat $\frac{364}{365}$ Möglichkeiten, usw., somit
> $$
> P(\text{mindestens 2 gleichen Geb})=1-\prod_{k=0}^{m-1} \frac{365-k}{365}
> $$
> **Alternative Vorstellung**
> Jeder Ball wird zufällig in einen der 365 Körbe geworfen. *Was ist die Wahrscheinlichkeit, dass 2 Bälle im gleichen Korb landen?*, bzw. ==Komplementärereignis==: *Was ist die W'keit, dass alle Bälle in unterschiedlichen Körben landen?*
> - Bälle ($m$): Personen im Raum
> - Körbe ($n$): möglichen Geburtstage (365)
> 
> ![[Bildschirmfoto 2026-03-23 um 11.33.38.png]]
>
> **Vereinfachen**:
> $$
> \begin{aligned}
> \left(1 - \frac{1}{n}\right) \left(1 - \frac{2}{n}\right) \dots \left(1 - \frac{m-1}{n}\right) &\approx e^{-\frac{1}{n}} \cdot e^{-\frac{2}{n}} \dots e^{-\frac{m-1}{n}} \\
> &\approx e^{-\frac{1}{n} (1 + 2 + \dots + (m-1))} \\
> &= e^{-\frac{(m-1) \cdot m}{2n}}
> \end{aligned}
> $$


## Satz der totalen Wahrscheinlichkeit

Wir haben ein Ereignis $B$, dass sich mit den $A_{i}$ überschneidet. Wir addieren alle Unionen mit den $A_{i}$.

$$
\Pr[B] = \sum_{i=1}^{n} \Pr[B|A_i] \cdot \Pr[A_i]=\sum_{i=1}^{n} \Pr[B \cap A_i]
$$

> [!example]- Proof
> **Beweis:** 
> 1. $B$ in nicht-überlappende Stücke aufteilen $B = (B \cap A_1) \cup \dots \cup (B \cap A_n)$.
> 2. Da sich diese Stücke nicht überlappen, ist die Gesamtwahrscheinlichkeit von $B$ einfach die Summe der Wahrscheinlichkeiten dieser Stücke: $\Pr[B] = \sum \Pr[B \cap A_i]$.
> 3. Umformen: Die Definition der bedingten Wahrscheinlichkeit besagt, dass $\Pr[B \cap A_i] = \Pr[B|A_i] \cdot \Pr[A_i]$ ist. Setzt man dies in die Summe ein, erhält man die finale Formel.

## Satz von Bayes

Im Prinzip einfach Günstige durch Mögliche. Oben hat man den "richtigen" Weg zum Ereignis B, und unten hat man alle möglichen Wege zum Ereignis B, addiert. Die Addition geht ja nur wenn disjunkt, also müssen $A_{1}, \dots, A_{n}$ paarweise disjunkt sein, und $B \subseteq A_{1} \cup \dots \cup A_{n}$ ein Ereignis mit $\Pr[B] > 0$. 

$$
\text{Pr}[A_i|B] = \frac{\text{Pr}[B|A_i] \cdot \text{Pr}[A_i]}{\sum_{j=1}^{n} \text{Pr}[B|A_j] \cdot \text{Pr}[A_j]} = \frac{\Pr(B \cap A_i)} {\sum_{j=1}^{n} \Pr(B \cap A_j)}
$$

> [!example]- Proof
> **Beweis**: siehe Bedingte Wahrscheinlichkeit und Satz der totalen Wahrscheinlichkeit
> 
> - $\Pr[B] = \sum_{i=1}^{n} \Pr[B|A_i] \cdot \Pr[A_i]$  
> - $\Pr[A|B] := \frac{Pr[A \cap B]}{Pr[B]}$.

Hat man ein Gesundheitsexperiment und möchte auf falsch positive, etc. überprüfen, hat man oben den "richtigen Weg", also krank und positiv, unten dann alle möglichen Wege die der Test positiv sein könnte. 

![[2nd Semester/AuW/Slides/08 Slides.pdf#page=5]]

### Bedingte Zufallsvariable

$$
Pr[ (X|A) = \alpha ] := Pr[ X = \alpha \mid A ]
$$

$$
Pr[X ≤ x | A] = \frac{Pr[\{\omega \in A \mid X(\omega) \leq x\}]}{Pr[A]}
$$


Bedingter Erwartungswert: 
$$
E[X|A] = \sum_{\alpha \in W_x} \alpha \cdot Pr[X=\alpha | A]
$$

**Gesetz des totalen Erwartungswerts**

X Zufallsvariable, $A_{i}$ disjunkt mit $A_{1} \cup \dots \cup A_{n}=\Omega$ und Wahrscheinlichkeiten $> 0$.
$$
\mathbb{E}[X] = \sum_{i=1}^{n} \mathbb{E}[X|A_i] \cdot \Pr[A_i]
$$

> [!example]- Proof
> 
> Beweis mit dem [[08 Bedingte Wahrscheinlichkeit#Satz d. totalen Wahrscheinlichkeit|Satz der totalen Wslkt]] ($\Pr[B] = \sum_{i=1}^{n} \Pr[B|A_i] \cdot \Pr[A_i]$)
> 
> ![[Bildschirmfoto 2026-04-15 um 14.44.32.png]]


