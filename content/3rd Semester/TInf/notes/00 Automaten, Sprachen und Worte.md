## Allgemein

$\Sigma$ Alphabet

> L zeug notieren 

$\Sigma^*$: Menge aller Wörter auf $\Sigma$

$$
\Sigma^+ = \Sigma^* - \{\lambda\}
$$
$$
\Sigma_{\text{bool}}^*
=
\{\lambda, 0, 1, 00, 01, \ldots\}
$$

Umkehrung $w^R$

Potenzen eines Wortes: 
$x^0 = \lambda$, 
$x^i = xx^{i-1}$

Ordnung: Zuerst nach Wortlänge sortieren, bei gleicher Länge lexikographisch

## Regularität

**regulär:** kann mit endlich viel Memory erkennen
**nichtregulär:** brauche unbeschränkt viel Memory, z.B. $a^n b^n$ 

- "teilbar durch k" ist regulär
- Achtung endlich viele Zustände, Angaben die das "merken" von unendlich vielen Stellen benötigen sind nicht regulär

- $\text{endlich} \implies \text{regulär}$ 

$$
\boxed{
L_1,L_2\text{ regulär}
\Longrightarrow
\begin{cases}
L_1\cup L_2 & \text{regulär}\\
L_1\cap L_2 & \text{regulär}\\
L_1\setminus L_2 & \text{regulär}\\
L_1L_2 & \text{regulär}\\
L_1^* & \text{regulär}\\
L_1^+ & \text{regulär}
\end{cases}}
$$

## Touringmachine

Ein oder mehrere Bänder mit Kästchen und einem Lesekopf. Kann Zeichen lesen, schreiben, Kopf links oder rechts bewegen.

## Lemmas

- Pumping Lemma: 
- Kolmogorov: 

