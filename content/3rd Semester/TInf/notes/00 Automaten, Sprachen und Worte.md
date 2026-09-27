## Allgemein

> [!success] Allgemein
> - $\Sigma$ **Alphabet**: **endliche, nichtleere** Menge an Zeichen
> - $w$ **Wort**: endliche Folge von Symbolen aus $\Sigma$ 
> - $L$ **Sprache** Menge von Wörtern aus dem Alphabet
> 	- $L^C$ Komplement der Sprache (alle Wörter in $\Sigma$, außer L)

- $\Sigma^*$: Menge aller Wörter aus $\Sigma$
  $\Sigma^+ = \Sigma^* - \{\lambda\}$ 
  z.B. $\Sigma_{\text{bool}}^*=\{\lambda, 0, 1, 00, 01, \ldots\}$

- Konkatination
	- Mit Worten: $w \cdot \lambda = \lambda \cdot w = w$ 
	- Mit Sprachen: 
		- $L_1 \cdot L_2 = \{ w_1 w_2 \mid w_1 \in L_1 \text{ und } w_2 \in L_2 \}$ : zuerst ein Wort aus $L_{1}$, dann ein Wort aus $L_{2}$ 
		- $L \cdot L_{\emptyset} = L\cdot \emptyset= L$ 
		- $L \cdot L_{\lambda} = L\cdot  \lambda = \{\lambda\}$  
- Umkehrung $w^R$

- Potenzen:
	- Wörter
		- $x^0 = \lambda$, 
		- $x^i = xx^{i-1}$
	- Sprachen, z.B. $L=\{aa, b\}$
		- $L^0 = \{ \lambda \}$
		- $L^1 = \{aa, b\}$
		- $L^2=\{aab, baa, aaaa, bb\}$ 

- **Ordnung**: Zuerst nach Wortlänge sortieren, bei gleicher Länge lexikographisch

- $L_{1}L_{2} \cup L_{1}L_{3} = L_{1}(L_{2}\cup L_{3})$ 
- $L_{1}(L_{2}\cap L_{3}) \subseteq L_{1}L_{2}\cap L_{1}L_{3}$  

## Touringmachine

Ein oder mehrere Bänder mit Kästchen und einem Lesekopf. Kann Zeichen lesen, schreiben, Kopf links oder rechts bewegen.
## Automaten

> [!success]
> Band von links nach rechts
> - $M=(Q, \Sigma, \delta, q_{0}, F)$
> - Q Zustände
> - F akzeptierende Zustände
> - $\delta$ Übergangsfunktion, z.B. $\delta(q_{1}, 0)=q_{2}$

**Konfiguration** 
- (aktuelle Position, remaining input) $\vdash_M$ (neue Position, aktualisierter remaining input)
- am ende ist es (Endposition, $\lambda$) 
- $\vdash_M^*$ null, einen oder beliebig viele Schritte

$L(M)$ ... von M akzeptiere Sprachen

> [!Note] Tipps zum Aufstellen von Automaten
> - wenn nur Binär möglich, dann ASCI Darstellung oder z.B. # als Separator verwenden und # kodieren
> - 

**Äquivalenzklassen**
$\text{Kl}[q]$ ... Menge aller Wörter die uns an diesem Zustand landen lassen

## Regularität

> [!success]
> - **regulär:** gibt regular expression, kann mit endlich viel Memory erkennen
> - **nichtregulär:** brauche unbeschränkt viel Memory, z.B. $a^n b^n$ 

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


## Lemmas

### Pumping Lemma

> [!info] Pumping Lemma
> endlicher Automat hat endlich viele Zustände, muss also bei einem langen Wort irgendwann im Kreis laufen (Schleife)

Widerspruch
- Regularität annehmen 
- gibt also Pumping-Länge p
- wähle Wort Länge größer  p
- darf nun in $w = xyz$ zerlegen, gelten muss $\vert{}xy\vert{} \le p$ und $\vert{}y\vert{} \ge 1$ 
- zeige, dass für jede Zerlegung mindestens ein $i$ existiert (z.B. i=0 oder i=2), sodass das aufgepumpte Wort $x y^i z$ nicht in $L$ liegt