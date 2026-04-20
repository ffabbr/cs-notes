
> [!success] Critical sections (locks)
> 1. Mutual exclusion (statements not interleaved)
> 2. Freedom from deadlock: a process trying to enter a critical section will eventually succeed
> 3. Freedom from starvation: all processes trying to enter a critical section will eventually succeed

## Mutual Exclusion Problem

### State space diagram

F.ex. state p4 means the next step is p4. 

- **Mutual exclusion**: gibt keinen state mit p3 und q3
- **Keinen Deadlock**: gibt keinen state ohne ausgehendem Pfeil
- **Keinen Livelock**: gibt keinen unendlichen Zyklus, der die Critical Section auslässt 
- **Kein Dead/Livelock**: gibt von jeder Node Pfad zu critical section
- **Freedom from individual starvation**: jeder thread der die critical section haben möchte, bekommt sie irgendwann

![[Bildschirmfoto 2026-04-15 um 17.50.31.png]]
