
*Deadlock detection: Directed Graph describing relation or Threads and Locks has a cycle. Suppose A waits for B, B waits for C, C waits for A.* 

- `java.util.concurrent.atomic.AtomicBoolean`
- `boolean set();`
- `boolean get():`
- `boolean compareAndSet(boolean expect, boolean update`
- `boolean getAndSet(boolean newValue)`

Bank Account, Transfer from A to B
- non-overlapping smaller critical sections means money is gone for a short time, so no atomarity
- one global lock, bad performance
- Solution: global ordering: 
  ![[Bildschirmfoto 2026-04-21 um 13.52.52.png]]

