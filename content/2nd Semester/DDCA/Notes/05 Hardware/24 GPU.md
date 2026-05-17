
A GPU is a [[23 SIMD|SIMD]] machine under the hood but is programmed with Threads.

---

## Programming Model vs. Execution Model

**Programming model** 
mental picture of the programmer, Sequential (von Neumann), Data Parallel (SIMD), Dataflow, Multi-threaded, …

**Execution model:**
actual hardware actions, out-of-order, vector-processor, array processor, dataflow processor, multiprocessor, …

---

**SPMD** Programming model (Single Program Multiple Data)
Das gleiche Programm wird auf mehreren Threads ausgeführt mit jeweils unterschiedlichen Daten

**SIMT** Execution model (Single Instruction Multiple Threads)
Wir der SPMD Befehl ausgeführt wird, not visible by programmer; GPU erstellt ==Warp== (32 Threads, die den Befehl auf unterschiedlichen Daten ausführen); Divergenz: es können nicht ein Teil der Threads im Warp die `if` branch und ein anderer Teil die `else` branch ausführen, also nacheinander

### Fine-Grained Multi-Threading (FGMT)

Der Prozessor kann in jedem Taktzyklus schnell zwischen Warps/Threads wechseln. 

Weil die GPU durch das schnelle Wechseln (FGMT) immer einen anderen Warp findet, der gerade arbeitsbereit ist, kann sie Latenzen einfach tolerieren.