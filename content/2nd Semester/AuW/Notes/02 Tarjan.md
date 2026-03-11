
**Kürzeste Wege:** 
immer Weg über Artikulationsknoten finden, das ist der kürzeste Weg. 

## Artikulationsknoten mit DFS finden

**Zeit in zusammenhängendem Graphen, alle Artikulationsknoten und Brücken finden:** $O(m)$ 

Wir führen DFS aus. Dabei

- definieren wir **Baumkanten** und **Restkanten** 
- Richtung der Restkanten: Richtung "in die wir geschaut haben zum überprüfen".
- **DFS-Wert**: Reihenfolge des Besuches (pre)
- `low[v]`: kleinste dfs Nummer, die man von v aus erreichen kann mit
	- 1) beliebig vielen Baumkanten
	- 2) max. einer Restkante (in der RHF)
- Traverse the DFS tree again from top to bottom and check for each vertex v its children w in the DFS tree: if `low[w] < dfs[v]` (meaning we can return above v). 
  
  If for even one of the children this property does not hold, then it means that v is a cut-vertex. 
  
  The first vertex s we start with in DFS has the special property that its subtrees are definitely not connected to one another and would not have had two subtrees. Thus, as soon as s has two children, s is also a cut-vertex. 

![[2nd Semester/AuW/Slides/02 Slides.pdf#page=22|02 Slides]]