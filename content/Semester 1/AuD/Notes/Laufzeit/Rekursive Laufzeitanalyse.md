
### Warum $\left( \frac{n}{2} \right)$ zu $\log n$ führt

$$
T(n) \leq a \, T\left(\frac{n}{2}\right) + c \, n^b
$$
#### Rekursive Auflösung

Wenn wir $\frac{n}{2}$ wieder in $T$ einsetzen, erhalten wir:

$$
T\left(\frac{\frac{n}{2}}{2}\right) = T\left(\frac{n}{4}\right)
$$

Somit:

$$
\frac{n}{2} \rightarrow \frac{n}{4} \rightarrow \frac{n}{8} \rightarrow \dots
$$

Die Rekursion endet, wenn:

$$
\frac{n}{2^k} = 1
$$

Daraus folgt:

$$
n = 2^k \quad \Rightarrow \quad k = \log_2(n)
$$