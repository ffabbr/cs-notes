→ siehe [[06 MST Overview]]

**Anfang:** jeder Knoten ist seine eigene Zusammenhangskomponente
Minimale Kante an jeder ZHK hinzufügen ([[06 MST Overview|Schnittprinzip]]) 
Sobald es nur mehr eine ZHK gibt → MST gefunden

## Laufzeit

- die Anzahl der ZHKs halbiert sich pro Iteration
- Iteriert über alle Knoten/Kanten bis nur noch eine ZHK. Pro Iteration $O(|E|+|V|)$. Am Anfang gibt es $|V|$ ZHKs
- $O((|V|+|E|)\cdot \log(|V|))$

>*The runtime of this algorithm can be analyzed as follows: in each iteartion, to find the connected components we may apply DFS. Then, we would go through all edges and check if they connect different connected components. For each connected component, we would find a minimal incident edge. This will take O(n + m). Now we only need to know the number of iterations. in each iteration, the worst case is if every two connected components share the same minimal edge. In this case, we would at least halve the number of connected components each iteration. Since we start off with n connected components, we will need less than log(n) many iterations, with a total runtime of O(n log(n)).*

## Beispiel 

1. **erste Iteration**, Achtung mehrere ZHK 
   ![[Boruvka erste Iteration.jpeg]]

2. **zweite Iteration**
   ![[Boruvka zweite Iteration.jpeg]]

