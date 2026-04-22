
Atomic hardware operations
- Test and Set (set 1 if currently 0)
- Compare-and-Swap (wenn wert im speicher gleich argument alt, setze wert im speicher auf neuen wert)
- Load Linked / Store-Conditional (ARM). 

Time per thread rises with number of threads

![[Bildschirmfoto 2026-04-21 um 13.46.08.png]]

## Java
### TAS in Java

- lock: loop setting boolean to true
- unlock: set boolean to false

### TTAS (test and test and set)

- komplex, thus don't use

### TATAS with backoff

- threads fight for access to same resource slows down
- solution: go to sleep with random duration → less try access at the same time
- increase expected duration each time the resource is not free

![[Bildschirmfoto 2026-04-21 um 13.48.34.png]]