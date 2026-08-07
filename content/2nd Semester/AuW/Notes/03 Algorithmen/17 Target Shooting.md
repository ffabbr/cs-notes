
- Es gibt ein Subset S vom Universum U.
- Wir haben eine Teilmenge (Stichprobe) des Universums. 
- Wir wollen $\frac{|S|}{|U|}$ abschätzen

Wir schauen uns den Prozentsatz von der Stichprobe an, und schauen, wie sehr sich das auf die grosse Menge verallgemeinern lässt.

Algorithmus: 
1. Wir ziehen $N$ zufällige Elemente aus der Gesamtmenge (Stichprobe)
2. Berechne Prozentteil in der Stichprobe:
	1. Nehme Anzahl Elemente in Stichprobe die Teil von S sind 
	2. Teile durch N für Prozentsatz 

$$
Y=\frac{1}{N} \cdot  \sum_{i=1}^N I_{s}(u_{i})
$$
Wie gross muss N sein damit Ausgabe aussagekräftig? 

Sei 

$$
N \geq 3 \frac{|U|}{|S|} \cdot \varepsilon^{-2} \ln\left(\frac{2}{\delta}\right)
$$

für $\varepsilon, \delta > 0$. Dann ist die Ausgabe des Algorithmus mit Wahrscheinlichkeit $\geq 1-\delta$ im Intervall 

$$
\left[(1-\varepsilon)\frac{|S|}{|U|}, (1+\varepsilon)\frac{|S|}{|U|}\right]
$$
richtig

---

![[Bildschirmfoto 2026-04-23 um 16.30.18.png]]
