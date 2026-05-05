
Wir unterscheiden jetzt das Konzept der *intrinsic built-in locks* eines Objekts und der external locks. Ein Monitor ist eine Verallgemeinerung des Konzepts der *intrinsic (synchronized) locks* in Java. Es ist eine Datenstruktur mit `wait / notify / notifyAll`. 

Wie schon früher bekannt, gilt immer noch, es gibt 
- ein Entry set of threads:
  tries to acquire the lock. One thread succeeds. The thread can go to the 
- wait set (sleep state):
  by releasing the lock, then it can be woken up with notify by an active thread. Once woken up, it competes with the threads from entry set to get access of the lock, to become the 
- owner of the lock. 
- Release and exit removes the thread from the pool. If all threads are in waiting state, we have a [[05 Deadlocks|deadlock]]. 

Wir können das wait set unterteilen, um nur z.B. eine bestimmte Kategorie von Threads zu wecken. Wir verwenden das [[#Condition interface of Monitors|Condition Interface]]. F.ex. in a [[08 Producer Consumer]] setup we create 2 wait sets.

> [!success]- Arten, Locks weiterzureichen (irrelevant)
> Es gibt unterschiedliche Varianten, wie ein Lock weitergereicht werden kann (irrelevant)
> 
> **signal and continue (java)**
> 1. signaling process continues running
> 2. signaling process moves signaled process from wait set to entry set
> 
> **signal and wait**
> 1. signaling process gives lock to signaled process
> 2. signaling process exits monitor and **goes waiting entry queue**
> 
> **signal and exit**
> 1. signaling process gives lock to signaled process
> 2. signaling process exits monitor entirely

![[Bildschirmfoto 2026-04-29 um 15.06.56.png]]

![[Bildschirmfoto 2026-04-29 um 15.20.07.png]]


---

## Condition interface of Monitors

Wenn wir manuell ein lock erstellt haben, können wir die conditions verwenden um Gruppierungen zu erstellen. Es ist immer noch nur ==ein Lock==, aber Gruppierungen in der waiting queue. 

Mehr flexibilität haben wir mit reentrant locks. `final Lock lock = new ReentrantLock();`

```java
final Lock lock = new ReentrantLock();
Condition notFull = lock.newCondition();
```

Jedes Java objekt hat `.wait()`, also hat man die wait, notify und notifyAll methoden umbenannt hier, um zu unterscheiden.

- `.await()`
- `.signal()`
- `.signalAll()`

### PC with Lock (Monitors)

F.ex. in Producer / Consumer we have notFull and notEmpty conditions. Wir verwenden nicht mehr intrinsic lock, also kein synchronized sondern muss manuell `lock.lock()` mit `try { } finally { unlock }`

![[Bildschirmfoto 2026-04-29 um 15.26.21.png]]

---
