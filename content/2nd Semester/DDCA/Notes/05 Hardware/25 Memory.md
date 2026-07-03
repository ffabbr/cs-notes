
**Ideal Memory**: zero latency, infinite capacity, zero cost, infinite bandwidth, zero energy

**Reality**: bigger ↔ slower, faster ↔ expensive, bandwidth ↔ expensive, faster ↔ more energy efficient

**Virtual Memory**: what the programmer sees, assume infinite
**Physical memory**: actual size

The system is translating virtual memory addresses to physical.

**Memory Hierarchy**: 
1. CPU Register (Flip-Flop)
2. L1 Cache
3. L2 Cache
4. L3 Cache
5. DRAM
6. Storage (SSD/HDD)

---

## DRAM vs SRAM

### SRAM (Static RAM)

- speichern mit Transistoren (Flip-Flops)
- stabil solange Strom fließt
- sehr schnell 
- geringe Dichte (brauchen viel Platz)
- used for CPU Caches
- teuer

### DRAM (Dynamic RAM)

- speichern in Kondensatoren
- verlieren Ladung über Zeit $\implies$ muss ständig **refreshed** werden
- higher density (viel Speicherplatz auf kleinem Raum)
- used for RAM
- billiger

---

## Memory Banking

Ein großer DRAM-Chip wäre zu langsam, da immer nur eine Anfrage bearbeitet werden kann.

Memory Banking: unterteile in kleinere Banks, auf die unabhängig (und gleichzeitig) zugegriffen werden kann


---

## Locality

One's past is a very good predictor of their near future

- **Temporal**: Wenn ein Programm eine bestimmte Information abruft, ist die Wahrscheinlichkeit sehr hoch, dass es dieselbe Information in naher Zukunft wieder benötigt.
- **Spatial**: Wenn ein Programm eine bestimmte Speicheradresse abruft, ist es sehr wahrscheinlich, dass es als Nächstes die direkt angrenzenden Adressen abrufen wird (da z.B. Liste)

---

## Cache

→ [[26 Cache]]

---

## The DRAM Subsystem

- Wenn wir einen Cache Miss haben, müssen wir in den langsameren Hauptspeicher (DRAM) gehen. 
- Damit das nicht viel zu langsam ist, teilen wir diesen Speicher in kleine Teile auf, die mit Bussen verbunden sind.
- Channe → Dimm → Rank → Chip → Bank → Row/Column

## Latency 

Wie lange dauert ein Speicherzugriff in einem Speicher-Niveau (siehe Memory Hierarchy) im Durchschnitt? 

- $h_{i}$ hit-rate
- $m_{i}$ miss-rate
- $h_{i} + m_{i} = 1$

- $t_{i}$ intrinsic access time, wie lange dauert es, *nur* diesen Cache zu bekommen (schnell)
- $T_{i}$ perceived access time, Durchschnittszeit 

$T_i = h_i \cdot t_i + m_i \cdot (t_i + T_{i+1})$
$T_i = t_i + m_i \cdot T_{i+1}$

Wir schauen immer im Cache nach ($t_{i}$), wenn miss (Wahrscheinlichkeit $m_{i}$), dann müssen wir die Daten aus dem nächst-tieferen Speicher holen ($T_{i+1}$). Die beiden Formeln sind ident (zum Umformen ausmultiplizieren und $h_i + m_i = 1$ nutzen)

$T_i \approx t_i$ desirable

---


> [!info]- Emerging Speichertechnologien
> ### PCM
> Phase Change Memory
> 
> - Speichert Daten durch Ändern des Aggregatzustandes eines Materials durch Stromfluss
> - braucht keinen Strom zum Halten der Daten oder Refresh
> - hohe Datendichte
> - langsamer, braucht mehr Energie
> - Abnutzung des Materials
> 
> ## SST-MRAM
> Spin-Transfer Torque Magnetic RAM
> 
> - speichert 0, 1 durch magnetischen Spin von Elektronen
> - braucht keinen Strom


---

## Other optimizations

### Resource Sharing

Allow a hardware resource be used by multiple contexts

Advantages: 
- improves throughput
- reduces communication latency
- compatible with shared memory programming model

Disadvantages: 
- can reduce performance
- eliminates performance isolation → inconsistent performance

### Shared Caches between cores

Advantages: 
- high effective capacity
- dynamic pertitioning
- easier to maintain coherence

Disadvantages: 
- slower access
- conflict misses due to other cores' accesses
- unfair cache sharing 

### Cache Partitioning

Because Shared Cache might be unfair shared, partitioning solves this