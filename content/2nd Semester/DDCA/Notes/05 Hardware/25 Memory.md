
**Ideal Memory**: zero latency, infinite capacity, zero cost, infinite bandwidth, zero energy

**Reality**: bigger ↔ slower, faster ↔ expensive, handwidth ↔ expensive, faster ↔ more energy efficient

**Virtual Memory**: what the programmer sees, assume infinite
**Physical memory**: actual size

The system is translating virtual memory addresses to physical.

**Memory Hierarchy**: 
1. CPU Register (Flip-Flop)
2. L1 Cache, L2 Cache (SRAM)
3. DRAM
4. Storage (SSD/HDD)

---

## DRAM vs SRAM

### SRAM (Static RAM)

- speichern mit Transistoren (Flip-Flops)
- stabil solange Stron fließt
- sehr schnell 
- geringe Dichte (viele Transistoren brauchen viel Platz)
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

## Caching

Caching is about memoizing used data (which works due to locality). We store data in addresses adjacent to recently accessed one in fast memory. 

**We divide memory into blocks**. The Cache contains *block lines/cache line*, which has place for one memory block.

Off-topic: a **Scratchpad** is like a Cache but managed by the programmer, not the hardware.


> [!success] 
> When CPU requests Data, it first checks Cache:
> - HIT: data is in cache
> - MISS: data is not in cache, bring block from main storage


The CPU sends data request and we quickly check the Cache. The data request contains

- tag of block
- index of block
- byte within block

Ablauf

1. go to position of index in tag store table
2. check if tag of request $=$ tag in tag store at index
3. yes? get block values from data store
4. use MUX to get requested byte of the found block

**Problem**: if 2 things randomly get the same index, they both use the same cache location and overwrite themselves

![[Bildschirmfoto 2026-05-15 um 15.55.32.png]]

**Solution**: Memory arrays

- Der Index zeigt auf ein Set mit N Zeilen (statt auf eine Zeile direkt)
- CPU schaut, welche der Zeilen in dem gegebenen Set frei ist und nutzt diese Zeile
- erst wenn alle Zeilen in dem Set belegt sind, muss eine Zeile überschrieben werden


![[Bildschirmfoto 2026-05-17 um 10.59.06.png]]



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
> - braucht keinen Stron zum Halten der Daten oder Refresh
> - hohe Datendchte
> - langsamer, braucht mehr Energie
> - Abnutzung des Materials
> 
> ## SST-MRAM
> Spin-Transfer Torque Magnetic RAM
> 
> - speichert 0, 1 durch magnetischen Spin von Elektronen
> - braucht keinen Strom
