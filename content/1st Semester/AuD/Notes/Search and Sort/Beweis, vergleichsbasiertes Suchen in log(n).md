
*Aus dem Skript, Kapitel 1.2.1*

Die Anzahl der Vergleiche, die ein Algorithmus im schlechtesten Fall ausführt, entspricht exakt der Höhe des Entscheidungsbaums. Diese Höhe ist definiert als die maximale Anzahl von Kanten auf einem Pfad von der Wurzel (dem obersten Knoten) zu einem Blatt (einem Knoten ohne Nachfolger). Wir beobachten, dass ein binärer Baum der Höhe h höchstens 

$$2^0 + 2^1 + 2^2 + \dots + 2^h=2^{h+1}-1 < 2^{h+1}$$

viele Knoten hat. Daraus folgt

$$n+1 \leq \text{Anzahl Knoten im Entscheidungsbaum}<2^{h+1}$$

... was aufgelöst, $h>\log_{2}(n+1)-1=\Omega (\log n)$ ergibt. 

Da die Anzahl der im schlimmsten Fall ausgeführten Vergleiche h beträg und unsere Argumentation für beliebige Entscheidungsbäume gilt, haben wir somit bewiesen, dass jedes vergleichsbasierte Suchverfahren auf einem sortierten Array im schlechtesten Fall mindestens $\Omega(\log(n))$ Vergleiche durchführt.