
Eine Speicherlocation ist mindestens eines von 

- Thread-local 
- Immutable
- Synchonized

## Guidelines

1. **Keine Data Races** (nicht mehrere Threads können den gleichen Speicherort lesen/schreiben)
2. Nutze **locks** wenn synchronisation needed, either
	1. Coarse grained: more objects per lock, fewer locks
	2. Fine grained: more locks, fewer objects per lock
3. **keine teuren Berechnungen in critical sections**
4. think, what **operations need to be atomic** (and create locks that way)

