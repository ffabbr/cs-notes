
*Deadlock detection: Directed Graph describing relation or Threads and Locks has a cycle.* 

Bank Account, Transfer from A to B
- non-overlapping smaller critical sections means money is gone for a short time, so no atomarity
- one global lock, bad performance
- Solution: global orderung: 
  ![[Bildschirmfoto 2026-04-21 um 13.52.52.png]]

