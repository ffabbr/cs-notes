
## Netzwerk

- gerichteter Graph $G?(V,A)$ 
- Source & Target (s, t)
- keine Schlaufen
- jede Kante hat Kapazität c (maximaler Fluss) und Fluss

## Flow

Wir weisen einem Netzwerk einen Fluss zu; geben jeder Kante $f(e)$ 

- $0 \leq f(e) \leq c(e)$
- ausser für s und t, gilt die **Flusserhaltung** (alles was rein fliesst, fliesst auch wieder raus)

- **Fluss**: $\text{val}(f) = \text{netoutflow(s)} = \text{netinflow(t)}$
- **MaxFlow**: maximaler Fluss

- $\text{netoutflow}(v) = \text{Ausfluss}(v) - \text{Zufluss}(v)$
- $\text{netoutflow}(v) = \sum_{(v,u) \in E} f(v,u) - \sum_{(w,v) \in E} f(w,v)$ 

## Schnitt

Partition von V in $(S,T)$
- source ist in S, 
- target ist in T. 

**Kapazität**: Summe aller Arcs, die von S nach T verlaufen ("wie viel überfliessen kann")

$$
\text{cap}(S,T) = \sum_{\underbrace{(u,v) \in (S \times T) \cap A}_{\text{alle Kanten die von } S \text{ zu } T \text{ gehen}}} c(u,v)
$$
$val(f) \leq cap(S,T)$ 

> [!Note]- Beweis
> Intuitiv logisch, alles muss mal rüberfliessen. Mathematisch: $val(f) = \text{netoutflow}(s)$, aber da Flusserhaltung ist netoutflow für Knoten ausser s, t 0, somit $val(f) = \sum_{u \in S} \text{netoutflow}(u)$, also nur relevant wenn wir S verlassen oder nach S kommen, also $val(f) = \sum_{u \in S, v \in T} f(u,v) - \sum_{v \in T, u \in S} f(v,u)$. Es gilt immer $f(u,v) \leq c(u,v)$, also $val(f) \leq \sum_{u \in S, v \in T} c(u,v) - 0$, und $\sum_{u \in S, v \in T} c(u,v)$ ist die Definition von $cap(S,T)$

Fluss maximal $\iff$ Restnetzwerk hat keinen gerichteten s-t-Pfad
Fluss maximal $\implies$ gibt s-t Schnitt mit $val(f)=cap(S,T)$ 

### MaxFlow-Mincut

- **MaxFlow**: maximaler Fluss
- **Mincut**: Schnitt mit kleinster Kapazität
$$
\max_{\text{Fluss } f} \text{val}(f) = \min_{(S,T) \text{ s-t-Schnitt}} \text{cap}(S,T)
$$

## Max-Flow mit Ford-Fulkerson

Kapazitäten ganzzahlig: $O(nmU)$, U = maximale Kapazität

1. Restnetzwerk bilden
2. while gibt (∃) s-t Pfad im Restnetzwerk ("augmentierender Pfad")
3. erhöhe Fluss entlang diesem Pfad um den Bottleneck des augmentierenden Pfades im Restnetzwerk

terminiert ev. nicht

## Restnetzwerk

statt den normalen Kanten, füge Kanten hinzu
- vorwärts: "wie viel mehr man transportieren könnte", und
- rückwerts: "wie viel weniger man transportieren könnte"

Wenn Wert 0, keine Kante

---

## Zuteilungsaufgaben mit Netzwerken

Nehmen an, wir teilen jedem A ein B zu. 

- erstelle Knoten s, t, ein Knoten pro A und ein Knoten pro B
- verbinde alle s mit allen aus A, und alle aus B mit t
- verbinde die aus A, je nach Kompatibilität mit denen aus B

Lässt es sich zuteilen? Ist maxFlow = Anzahl Elemente? 

![[Bildschirmfoto 2026-05-07 um 20.51.01.png]]