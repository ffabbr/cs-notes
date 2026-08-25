---
draft: "true"
---

- Assume $(i)$. Every decrease in $c(e)$ decreases $\text{flow}(N)$, so decreasing $c(e)$ also decreases capacity of min cut (per maxflow mincut theorem). This obviously only works when $e$ is part of min cut. So given $(i)$, $e$ must be part of a min cut ($(i) \implies (iii)$) 
    
- Assume $(iii)$. $e$ is part of a min cut as forward edge, net flow of this cut = max cap (Max-Flow Min-Cut Theorem). This is only possible if all forward edges within the cut are fully utilized (maximal value). So $f(e) = c(e)$ and $(iii) \implies (v)$ holds.
    
- Assume $(v)$, meaning $f(e) = c(e)$. If $c(e)$ is decreased, every flow must satisfy the equation $f(e)=c(e)$ for the new c(e), and thus decrease $f(e)$. If we didn't have to decrease f, then that would mean that before the decrease of c we had $f(e) < c(e)$, which would be a contradiction. Thus $(v) \implies (i)$ 
- Combining these we have $(i) \iff (iii) \iff (v)$ by transitivity of implication

---

- Assume $(iv)$, every minimum cut contains $e$, so $c(e)$ is a Summand in $cap(S,T)$. Suppose $c(e)$ increases. $\implies$ cap of mincut also increases. Because all previous minimum cuts now have a higher capacity (and the other cuts that weren't minimum had a larger capacity anyways),  $\text{flow}(N)$ increases and thus $(iv) \implies (ii)$ 
    
- Assume $(ii)$. Every increase of $c(e)$ increases $\text{flow}(N)$, so increasing $c(e)$ increases the capacity of the global min cut. This only occurs if $e$ is part of every min cut. If there existed a minimum cut not containing $e$, its capacity wouldn't change when increasing $c(e)$, meaning min cap S,T and thus $\text{flow}(N)$ wouldn't increase. So $e$ must is part of every minimum cut, $(ii) \implies (iv)$ holds.
    
- Combined, $(ii) \iff (iv)$ 

---

- Assume $(iv)$. Every min cut contains $e$, so there exists "a" min cut that contains e. $(iv) \implies (iii)$
