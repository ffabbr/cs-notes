
**Ziel**: Möglichst grosse stabile Menge (menge an Knoten, die keine direkte Kante zwischen ihnen haben) finden. 

**Long story short**: jeder Knoten tritt mit Wahrscheinlichkeit p bei, somit haben wir $|V|\cdot p$ Knoten dabei. Es kann Konfliktkanten geben (mit 2 Knoten an den Enden die dabei sind), das sind $|E|\cdot p^2$ viele, in diesem Fall entfernen wir einfach einen der 2 Knoten. Wir suchen p sodass $E(|S|)$ maximiert ist, indem wir $|V|\cdot p - |E|\cdot p^2$ als Funktion betrachten, nach p ableiten und auf $p=$ umstellen. Dann setzen wir zurück ein und bekommen $E(|S|)\geq \frac{n^2}{4m}$ als Antwort. 

## Algorithmus

Jeder Knoten $v$ entscheidet sich unabhängig mit Wahrscheinlichkeit $p$, Teil der Menge zu sein ($s_v = 1$). Mit Wahrscheinlichkeit $1-p$ wählt er sich nicht ($s_v = 0$).

Wenn zwei Knoten, die durch eine Kante verbunden sind, _beide_ im ersten Schritt gewählt haben ($s_u = s_v = 1$), entferne einen Knoten aus der Menge, behalte den anderen.

## Erwartungswert der Grösse

- $X$: Die Anzahl der Knoten, die nach Schritt 1 (der zufälligen Auswahl) den Wert $1$ haben.
- $Y$: Die Anzahl der "Konfliktkanten" (also Kanten, bei denen _beide_ Endknoten in Schritt 1 den Wert $1$ bekommen haben).

$$
|S| \ge X - Y
$$

> [!info]-
> Wir haben $X$ ausgewählte Knoten, $Y$ Kanten verletzen die Eigenschaft der stabilen Menge. Im schlechtesten Fall müssen wir für jede dieser $Y$ Konfliktkanten genau einen Knoten aus unserer bisherigen Menge entfernen. Ziehen wir also für jeden Konflikt ($Y$) einen Knoten ab, haben wir eine untere Schranke für die Größe der Menge $S$.

[[10 Zufallsvariable, Erwartungswert, Varianz#Linearität des Erwartungswerts|Linearität des Erwartungswertes]]  

$$
\mathbb{E}[|S|] \ge \mathbb{E}[X] - \mathbb{E}[Y]
$$

### Berechnung von $\mathbb{E}[X]$: 

[[10 Zufallsvariable, Erwartungswert, Varianz#Formel 2 mit Indikatorvariable|Indikatorvariable]]

Da jeder Knoten mit Wahrscheinlichkeit $p$ gewählt wird, ist der Erwartungswert für einen einzelnen Knoten: $\mathbb{E}[X_v] = p$.

Für alle $n$ Knoten also:
$$
\mathbb{E}[X] = n \cdot p
$$


### Berechnung von $\mathbb{E}[Y]$: 

[[10 Zufallsvariable, Erwartungswert, Varianz#Formel 2 mit Indikatorvariable|Indikatorvariable]]

Sei $Y_e$ eine Indikatorvariable, die $1$ ist, wenn die Kante $e = \{u, v\}$ ein Konflikt ist (also wenn sowohl $u$ als auch $v$ gewählt wurden).

Da die Knoten unabhängig entschieden, multiplizieren sich Wahrscheinlichkeiten. Die Wahrscheinlichkeit, dass beide Enden der Kante den Wert $1$ haben, ist

$\Pr[s_u = 1 \text{ und } s_v = 1] = \Pr[s_u = 1] \cdot \Pr[s_v = 1] = p \cdot p = p^2$

Der Erwartungswert für eine Kante ist also $\mathbb{E}[Y_e] = p^2$.

Für alle $m$ Kanten im Graphen ergibt sich

$$
\mathbb{E}[Y] = m \cdot p^2
$$

### Together

$$
\mathbb{E}[|S|] \ge n \cdot p - m \cdot p^2
$$

## Optimale Wahl von p

Um eine möglichst große stabile Menge zu erhalten, wollen wir den Term $n \cdot p - m \cdot p^2$ maximieren.

Das ist eine nach unten geöffnete Parabel. Um das Maximum zu finden, leitet man die Funktion nach $p$ ab und setzt sie gleich null:

$$
n - 2 \cdot m \cdot p = 0 \implies p = \frac{n}{2m}
$$

Setzt man dieses optimale $p$ wieder in die Ungleichung ein, erhält man

$$
\mathbb{E}[|S|] \geq \frac{n^2}{4m}
$$

Wenn d-regulär, lässt sich die Gesamtzahl der Kanten $m$ berechnen als $m = \frac{d \cdot n}{2}$ (jeder der $n$ Knoten steuert $d$ Kantenenden bei, da jede Kante zwei Enden hat, wird durch 2 geteilt).

$$
\mathbb{E}[|S|] \ge \frac{n^2}{4 \left(\frac{d \cdot n}{2}\right)} = \frac{n^2}{2 \cdot d \cdot n} = \frac{n}{2d}
$$
