
##### Code-Expert Tipps
- Index Search in an almost sorted Array
	- Ähnlich wie Aufgabe 4.4 
- Ticket Shop: 
	- DP
	- Laufzeit hat jeden Parameter aus der Angabe einmal → Teilproblem mit der vollständigen Parameterisierung
- Zum debuggen ev. temporär Arrays importieren und deepToString verwenden


## Allgemein

### Schritte

1. Dimension 
2. Teilproblem 
3. Rekursionsformel (Elemente in der DP Table berechnen aus vorherigen Einträgen)
4. Berechnungsreihenfolge
5. Anzahl und Laufzeit (Ziel der Laufzeit pro Element ist $O(1)$)

### Bekannte Probleme und Takeways

| **Problem**                       | **Takeway** | Rekursionsformel | Laufzeit |
| --------------------------------- | ----------- | ---------------- | -------- |
| [[#Jump-Game]]                    |             |                  |          |
| [[#Something]]                    |             |                  |          |
| [[#Coin Conversion]]              |             |                  |          |
| [[#Editierdistanz]]               |             |                  |          |
| [[#Teilsummenproblem]]            |             |                  |          |
| [[#Rucksackproblem]]              |             |                  |          |
| [[#Längste gemeinsame Teilfolge]] |             |                  |          |
| [[#Ticket Shop]]                  |             |                  |          |
| [[#Coffee & Tea]]                 |             |                  |          |
|                                   |             |                  |          |


### Sonstiges

- Memoization
- DP braucht Rekursionsformel, dann ist Bottom-up und Memoization beides möglich. Siehe [[Bottom-up vs Memoization.jpg]] 
- DP Tabelle durch Rückverfolgung 

```java
// erlaubt
Integer.MAX_VALUE
Math.min()
```

## Bekannte Probleme

### Jump-Game

*(Definition 2.1)*

Zahl im Array gibt erlaubte maximale Anzahl an Sprüngen an, Ziel ist, mit möglichst wenigen Schritten an das letzte Element zu kommen. 

1. **Teilproblem:** DP(i): min. Anzahl Sprünge um Position i zu erreichen. *i ... Parametrisierung*
2. **Dimension:** DP(1...n), nur ein Parameter, also nur eine Dimension
3. **Rekursionsformel:** 
   
   Base Case: DP(1)=0 
   *wir starten mit Position 1, und um die zu erreichen braucht man also 0 Schritte*
   
   DP(i) = min{ DP(j)+1 **|** j+$a_{j} \geq$ i, 1 $\leq j<i$ }

4. **Berechnungsreihenfolge:** *aufsteigend*
   
``` java
   for i=1...n: 
	   Compute DP(i)
```

5. **Lösung Extrahieren:** DP(n)
6. **Anzahl Einträge in der DP-Tabelle:** n
   **Laufzeit pro Eintrag:** O(n)
   Gesamtlaufzeit: $n \cdot O(n)=O(n^2)$

#### Something

DP(i) = Max. erreichbarer Index in i Sprüngen

DP(0)=1
DP(i)=max{k+A(k) | DP(i-2) $\leq$ k $\leq$ DP(i-1)}

### Coin Conversion

Siehe [[1st Semester/AuD/Exercises/06 Sheet.pdf|06 Sheet]]

### Längste gemeinsame Teilfolge

*Definition 2.2, zweidimensional*

1. **Teilproblem:** L(i,j) = Länge einer LGT von ($a_{1}, \dots a_{i}$ und $b_{1},\dots,b_{j}$) 
   *hier wieder basically Parameterisierung*
2. **Rekursionformel:**$$
L[i,j] = 
\begin{cases}
0, & \text{falls } i = 0 \text{ oder } j = 0 \text{ ist}, \\[6pt]
1 + L[i-1, j-1], & \text{falls } i > 0 \text{ und } j > 0 \text{ und } a_i = b_j \text{ ist}, \\[6pt]
\max\{L[i, j-1], L[i-1, j]\}, & \text{falls } i > 0 \text{ und } j > 0 \text{ und } a_i \neq b_j \text{ ist}.
\end{cases}$$

### Editierdistanz

1. **Teilproblem:** ED(i,j) = Editierdistanz von ($a_{1}, \dots a_{i}$) und ($b_{1}, \dots, b_{j}$)
2. **Rekursionsformel:** (und zusätzlich ==Base Case nicht vergessen==) $$
ED(i,j) = \min \begin{cases}
ED(i-1, j) + 1, \\[6pt]
ED(i, j-1) + 1, \\[6pt]
ED(i-1, j-1) + 
\begin{cases}
1, & \text{falls } a_i \neq b_j \text{ ist}, \\[4pt]
0, & \text{falls } a_i = b_j \text{ ist}.
\end{cases}
\end{cases}
$$
### Teilsummenproblem

*Definition 2.4, Rückgabe, ob eine Teilmenge möglich ist (1) oder nicht (0)*

1. **Teilproblem:** siehe Skript [[4_Dynamische Programmierung.pdf]], S. 24
2. **Rekursion:** T(0,s)=1 $\Leftrightarrow$ s=0 $$T(i, s) = \begin{cases}
1 & \text{falls es eine Teilmenge } I \subseteq \{1, \ldots, i\} \text{ gibt mit } \sum_{j \in I} A[j] = s, \\
0 & \text{sonst.}
\end{cases}$$
DP-Tabelle rückverfolgen (siehe Notizen der Übung)

### Rucksackproblem

![](https://youtu.be/nLmhmB6NzcM?si=Ck1fcwG-6j4O4CbP)

### Längste aufsteigende Teilfolge

### Ticket Shop

### Coffee & Tea