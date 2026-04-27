
==Atomic hardware operations== 
- **Test and Set** (set 1 if currently 0)
- **Compare-and-Swap** (wenn wert im speicher gleich argument alt, setze wert im speicher auf neuen wert)
- Load Linked / Store-Conditional (ARM). 

Time per thread rises with number of threads

## Locks with TAS

- both threads try TAS in while loop, only one sets it to 1 the other gets 0, needs only one memory location
- problem, all threads spam TAS in while loop
- Backoff
	- threads fight for access to same resource slows down
	- solution: **go to sleep with random duration** → less try access at the same time
	- double waiting duration each time the resource is not free, reset when accessed

### TATAS 

- TAS with Backoff still slow
- TATAS also

- **Solution**: add flag, read flag if lock is free (fast)
- only if free, start TAS, else go to sleep (backoff)

![[Bildschirmfoto 2026-04-21 um 13.48.34.png]]