lösen linearer Gleichungssysteme $Ax = b$.

## Gauß-Elimination

1. Schreibe als Matrix $[A|b]$
2. Pivot: In der ersten Spalte ein Element ungleich Null (meistens das oberste). Falls dort eine Null steht, tausche die Zeilen.
3. Nutze Zeilenoperationen, um alle Zahlen **unterhalb** des Pivot-Elements zu $0$ zu machen
4. Gehe zur nächsten Spalte und eine Zeile tiefer. Wiederhole Schritt 2 und 3, bis eine Dreiecksform entsteht (Nullen unten links).
5. **Rückwärtseinsetzen**

### Beispiel

$$
\begin{aligned} x + y + z &= 6 \\ 2x + 4y + 2z &= 16 \\ -x + 5y - 4z &= -3 \end{aligned}
$$

$$
\begin{bmatrix} 1 & 1 & 1 & 6 \\ 2 & 4 & 2 & 16 \\ -1 & 5 & -4 & -3 \end{bmatrix}
$$

**Nullen in ersten Spalte**

- $Z_2 \rightarrow Z_2 - 2 \cdot Z_1$
- $Z_3 \rightarrow Z_3 + Z_1$
$$
\begin{bmatrix} 1 & 1 & 1 & 6 \\ 0 & 2 & 0 & 4 \\ 0 & 6 & -3 & 3 \end{bmatrix}
$$

**Nullen in zweiten Spalte**

- $Z_3 \rightarrow Z_3 - 3 \cdot Z_2$
$$
\begin{bmatrix} 1 & 1 & 1 & 6 \\ 0 & 2 & 0 & 4 \\ 0 & 0 & -3 & -9 \end{bmatrix}
$$

*Ist Zeilenstufenform, also done*

**4. Rückwärtseinsetzen:**

- Zeile 3: $-3z = -9 \implies \mathbf{z = 3}$
- Zeile 2: $2y + 0z = 4 \implies 2y = 4 \implies \mathbf{y = 2}$
- Zeile 1: $x + 2 + 3 = 6 \implies x + 5 = 6 \implies \mathbf{x = 1}$

Lösung: $(1, 2, 3)$

---

## Gauß-Jordan

1. Gauss-Verfahren, dann normieren, also jede Zeile durch ihr Pivot-Element teilen (oder direkt, geht auch)
2. Rechts unten beginnen, mit Zeilenoperationen alle Zahlen **oberhalb** der führenden 1 zu $0$ machen
3. **Ergebnis:** Links Einheitsmatrix, rechts Lösungen

## Beispiel

**Von oben:**

$$
\begin{bmatrix} 1 & 1 & 1 & 6 \\ 0 & 2 & 0 & 4 \\ 0 & 0 & -3 & -9 \end{bmatrix}
$$

**Normieren**

- $Z_2 \rightarrow Z_2 : 2$
- $Z_3 \rightarrow Z_3 : (-3)$
$$
\begin{bmatrix} 1 & 1 & 1 & 6 \\ 0 & 1 & 0 & 2 \\ 0 & 0 & 1 & 3 \end{bmatrix}
$$

**Rückwärts-Elimination**

- $Z_1 \rightarrow Z_1 - 1 \cdot Z_3$
$$
\begin{bmatrix} 1 & 1 & 0 & 3 \\ 0 & 1 & 0 & 2 \\ 0 & 0 & 1 & 3 \end{bmatrix}
$$
- $Z_1 \rightarrow Z_1 - 1 \cdot Z_2$
$$
\begin{bmatrix} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 2 \\ 0 & 0 & 1 & 3 \end{bmatrix}
$$
Also:

$$
x = 1, \quad y = 2, \quad z = 3
$$
