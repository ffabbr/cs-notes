## Grenzwerte

z.B. 2 dimensional—teste beide dimensionen, $\left( \frac{1}{k}, 0 \right)$ und $\left( 0, \frac{1}{k} \right)$ und prüfe, ob Wert gleich
## Stetigkeit

**Folgenkriterium**
stetig $\iff \text{für jede Folge } (x_k)_{k \in \mathbb{N}_0} \subset \mathbb{R}^n \text{ mit } x_k \to x \text{ konvergiert } (f(x_k))_{k \in \mathbb{N}_0} \text{ gegen } f(x)$

**Epsilon-Delta Kriterium**
stetig $\iff \forall x \in X : \forall \varepsilon > 0 \ \exists \delta > 0 \text{ sodass } (\vert{}\vert{}x - x'\vert{}\vert{} < \delta \Rightarrow \vert{}\vert{}f(x) - f(x')\vert{}\vert{} < \varepsilon)$

>Beispiel Epsilon-Delta Kriterium für die Stetigkeit an dem Punkt 0,0: $f(x,y) = \frac{x^3}{x^2+y^2}$ für $(x,y)\neq(0,0)$ und $f(0,0)=0$. $|f(x,y) - f(0,0)| = |x| \cdot \underbrace{\frac{x^2}{x^2+y^2}}_{\le 1} \le |x| \to_{(x,y)\to(0,0)}0$. Findet man eine Abschätzung $|f(x') - f(x)| \le C \cdot \|x' - x\|$ (hier mit $C = 1$), dann funktioniert immer $\delta = \varepsilon / C$. Hier: Wähle $\delta := \varepsilon$. $|f(x,y) - f(0,0)| \le \|(x,y) - (0,0)\| < \delta = \varepsilon. \;✓$, also $\|(x,y) - (0,0)\| < \delta \;\Rightarrow\; |f(x,y) - f(0,0)| < \varepsilon$, daher stetig.

Der Bruch ist immer höchstens 1, weil der Zähler ein Teil des Nenners ist. Übrig bleibt $|x|$, und das geht gegen 0, wenn $(x,y)\to(0,0)$.

z.B. bei einem kritischen Punkt der eine spezielle Festlegung in der Definition der Funktion benötigt, nutze Folgenkriterium. 
## Kompaktheit

von $K \subset \mathbb{R}^n$

- $\iff$ abgeschlossen und beschränkt
- $\iff$ jede Folge $(x_s)_{s \in \mathbb{N}_0} \subset K$ in $K$ eine in $K$ konvergente Teilfolge hat

> eine stetige Funktion hat in jedem kompakten $K \subset \mathbb{R}^n$ ein minimum und maximum


---

## Graphen lesen

![[Bildschirmfoto 2026-10-06 um 15.34.57.png]]![[Bildschirmfoto 2026-10-06 um 15.35.45.png]]

Niveaulinien verbinden inputs die alle den selben Wert (notiert auf der Linie) haben. $f_x$ ist die Änderungsrate wenn y fixiert ist und x erhöht wird. Hier geht es zu höheren Niveaus (z.B. bis 10 ganz rechts). Der Abstand zwischen den Linien ist, wie "steil" es ist. $f_{xx}$ sagt, ob die Steigung in x-Richtung zu oder abnimmt (die Linien werden immer näher, es wird also steiler.)