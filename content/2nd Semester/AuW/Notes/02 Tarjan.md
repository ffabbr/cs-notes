
**Kürzeste Wege:** 
immer Weg über Artikulationsknoten finden, das ist der kürzeste Weg. 

## Artikulationsknoten mit DFS finden

**Zeit in zusammenhängendem Graphen, alle Artikulationsknoten und Brücken finden:** $O(m)$ 

Wir führen DFS aus. Dabei

- definieren wir Baumkanten und Restkanten 
- Richtung der Restkanten: Richtung "in die wir geschaut haben zum überprüfen".
- DFS-Wert: Reihenfolge des Besuches
- low\[v\]: kleinste dfs Nummer, die man von v aus erreichen kann mit
	- 1) beliebig vielen Baumkanten
	- 2) max. einer Restkante (in der RHF)
- Angepasste DFS berechnet alle Artikulationsknoten und Brücken in $O(m)$. 

![[2nd Semester/AuW/Slides/02 Slides.pdf#page=22|02 Slides]]