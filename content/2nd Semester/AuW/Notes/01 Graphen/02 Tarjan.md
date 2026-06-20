
**Kürzeste Wege:** 
immer Weg über Artikulationsknoten finden, das ist der kürzeste Weg. 

## Artikulationsknoten mit DFS finden (Tarjan)

**Zeit in zusammenhängendem Graphen, alle Artikulationsknoten und Brücken finden:** $O(m)$ 

Wir führen DFS aus. Dabei

- definieren wir **Baumkanten** und **Restkanten** 
- Richtung der Restkanten: Richtung "in die wir geschaut haben zum überprüfen".
- **DFS-Wert**: Reihenfolge des Besuches (pre)

- `low[v]`: kleinste dfs Nummer, die man von v aus erreichen kann mit
	- 1) beliebig vielen Baumkanten
	- 2) max. einer Restkante (in der RHF)


**Brücken:** Eine Baumkante $(u,v)$ (mit $v$ Kind von $u$) ist eine Brücke, wenn

$$low[v] > disc[u]$$

Das heißt: der Teilbaum unter $v$ kann über keine Rückwärtskante etwas erreichen, das so früh oder früher entdeckt wurde als $u$ selbst. Es gibt also keinen alternativen Weg.

**Artikulationsknoten:** Zwei Fälle.

Für die **Wurzel** ($A$): Sie ist Artikulationsknoten genau dann, wenn sie im DFS-Baum mehr als ein Kind hat.

Für **alle anderen** Knoten $u$ mit Kind $v$: $u$ ist Artikulationsknoten, wenn

$$low[v] \geq disc[u]$$

Der Unterschied zur Brücke ist nur $\geq$ statt $>$. Der Teilbaum unter $v$ kann höchstens bis $u$ zurück, aber nicht darüber hinaus, also trennt das Entfernen von $u$ den Teilbaum ab.


![[2nd Semester/AuW/Slides/02 Slides.pdf#page=22|02 Slides]]