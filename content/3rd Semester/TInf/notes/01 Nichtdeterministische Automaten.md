
Nicht deterministische Automaten können für eine Eingabe keinen, einen, oder mehrere Zielzustände haben. Somit gibt die Übergangsfunktion eine Menge an Zuständen an. Die Akzeptanzbedingung ist, dass es eine Möglichkeit gibt, in einen akzeptierenden Zustand zu kommen. 
$$
L(M) = \{ \omega \in \Sigma^* \mid \hat{\delta}(q_0, \omega) \cap F \neq \emptyset \}
$$

==🟠Zu jedem nicht deterministischen Automaten gibt es einen deterministischen und vice versa. ==

Jeder deterministische Automat ist auch nicht-deterministisch. Diese Richtung ist also offensitlich wahr. Andere Richtung: für jeden NEA gibt es einen EA. Den können wir mit der Potenzmengenkonstruktion bilden.

> [!Note] 
> Für alle $k \in \mathbb{N} \setminus \{0\}$ braucht jeder EA, der $L_k$ akzeptiert, mind. $2^k$ Zustände.
> 
> [[Beweis.png]]

## EA mit Potenzmengenkonstruktion

![[Bildschirmfoto 2026-10-09 um 17.42.01.png]]![[Bildschirmfoto 2026-10-09 um 17.42.09.png]]

## Mindest-Anzahl der Zustände beweisen

Wir verwenden Lemma 3.3.

1. Finde n Wörter $w$, die in unterschiedlichen Zuständen landen (n ist Anzahl minimaler Zustände), z.B. die kürzesten Wege zu jedem Zustand. Das sind unsere Präfixe (unten grün)
2. Erstelle eine Tabelle, in der wir jeden Zustand mit jedem anderen Zustand vergleichen (Tabelle ist symmetrisch, brauchen also nur die eine Hälfte). 
3. Postfix rot ist ein das Wort einmal in der Sprache und einmal nicht.

Beispiel: 
$L = \{\omega \in \{a,b\}^+ \mid |\omega|_b = 1 \pmod 3 \text{ und } \omega \text{ beginnt mit } ab\}$

$$
\begin{array}{l|cccccc}
& \color{blue}{w_1}, \color{green}{\lambda} & \color{blue}{w_2}, \color{green}{a} & \color{blue}{w_3}, \color{green}{b} & \color{blue}{w_4}, \color{green}{ab} & \color{blue}{w_5}, \color{green}{abb} & \color{blue}{w_6}, \color{green}{abbb} \\
\hline
\color{blue}{w_1}, \color{green}{\lambda} & \color{red}{-} & \color{red}{b} & \color{red}{ab} & \color{red}{ab} & \color{red}{ab} & \color{red}{b} \\
\color{blue}{w_2}, \color{green}{a} & \color{red}{-} & \color{red}{-} & \color{red}{b} & \color{red}{\lambda} & \color{red}{bb} & \color{red}{ab} \\
\color{blue}{w_3}, \color{green}{b} & \color{red}{-} & \color{red}{-} & \color{red}{-} & \color{red}{\lambda} & \color{red}{bb} & \color{red}{b} \\
\color{blue}{w_4}, \color{green}{ab} & \color{red}{-} & \color{red}{-} & \color{red}{-} & \color{red}{-} & \color{red}{\lambda} & \color{red}{\lambda} \\
\color{blue}{w_5}, \color{green}{abb} & \color{red}{-} & \color{red}{-} & \color{red}{-} & \color{red}{-} & \color{red}{-} & \color{red}{b} \\
\color{blue}{w_6}, \color{green}{abbb} & \color{red}{-} & \color{red}{-} & \color{red}{-} & \color{red}{-} & \color{red}{-} & \color{red}{-}
\end{array}
$$

![[Bildschirmfoto 2026-10-13 um 00.27.48.png|389]]