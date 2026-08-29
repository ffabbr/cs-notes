Das **Master Theorem** hilft, die asymptotische Laufzeit von rekursiven Algorithmen der Form  

$$
T(n) = aT\left(\frac{n}{b}\right) + Cn^d
$$
zu bestimmen, wobei  
- $a \ge 1$: Anzahl der Teilprobleme  
- $b > 1$: Verkleinerungsfaktor  
- $d \ge 0$: Arbeit außerhalb der Rekursion  

### Fälle

1. **Fall 1:** $d > \log_b a$
$$
T(n) \leq O(n^d)
$$

2. **Fall 2:** $d = \log_b a$
$$
T(n) \leq O(n^d \log n)
$$
3. **Fall 3:** $d < \log_b a$
$$
T(n) \leq O(n^{\log_b a})
$$