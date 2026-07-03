
## QuickSort

1. nehme Sortiertes Array
2. nehme $a_i$ and $a_j$, $i < j$ so $a_i < a_j$

	Wahrscheinlichkeit, dass $a_i$ und $a_j$ verglichen werden
	
	$$I_{ij} = \begin{cases} 1 & a_i, a_j \text{ verglichen} \\ 0 & \text{sonst} \end{cases}$$
	
	Quicksort wählt ein random pivot Element. 
	
3. Betrachte $\{a_i, a_{i+1}, \dots, a_{j-1}, a_j\}$
	- Case 1: Pivot ist genau $a_i$ oder $a_j$ $\Rightarrow a_i$ und $a_j$ werden verglichen
	- Case 2: Pivot ist $a_{i+1} \dots a_{j-1}$: $a_i$ ist im linken Teilarray, $a_j$ im rechten $\Rightarrow$ werden nie verglichen

![[Bildschirmfoto 2026-05-04 um 13.44.34.png]]
![[Bildschirmfoto 2026-05-04 um 13.44.52.png]]

## QuickSelect

![[Bildschirmfoto 2026-05-04 um 13.43.22.png]]