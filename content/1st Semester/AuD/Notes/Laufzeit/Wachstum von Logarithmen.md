### Wachsen alle Logarithmen gleich schnell?

Wir betrachten zunächst:

$$
\log_3(n^4) = 4 \cdot \log_3(n) = 4 \cdot \frac{\ln(n)}{\ln(3)} = \frac{4}{\ln(3)} \cdot \ln(n)
$$

Die Konstante $\frac{4}{\ln(3)}$ ist **konstant**, daher gilt:

$$
\log_3(n^4) = \Theta(\ln(n))
$$

→ Logarithmen mit unterschiedlichen Basen unterscheiden sich nur um einen konstanten Faktor.
### Achtung Exponenten 

Beispiele:

1.  $$
   \log_7(n^8) = 8 \cdot \log_7(n) = \Theta(\log(n))
   $$

2.  $$
   \log_3(n^{\sqrt{n}}) = \sqrt{n} \cdot \log_3(n) = \Theta(\sqrt{n} \cdot \log(n))
   $$

Hier multipliziert sich der Logarithmus mit einem **nicht-konstanten Faktor** ($\sqrt{n}$).  
Daher gilt: **kein konstanter Faktor!**

![[Logs gleich schnell.png]]