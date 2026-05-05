
Barrieren lassen Threads warten, bis alle an einem gemeinsamen Punkt angekommen sind. Erst dann dürfen alle weiterlaufen. Rendezvous der [[06 Semaphores|Semaphoren]] ist wie eine Barriere, erst wenn beide hier sind, können wir post ausführen

![[Bildschirmfoto 2026-04-27 um 11.39.23.png]]
![[Bildschirmfoto 2026-04-29 um 15.49.05.png]]

Alle Threads kommen zum rendezvous Punkt der Semaphore, und erst dann laufen sie weiter. 

**Turnstile**

- acquire, dann gleich release
- schritt für Schritt releasen sich die Threads gegenseitig

---

Beware in implementation 
- count++ is not atomic, need to protect with acquire/release mutex
- barrier needs to be reusable, meaning count 0 at end
- only one thread should trigger release/acquire, not all at once

With [[09 Monitors|Monitor]]:

*reusable*

```java
public class Barrier {
    final int threads;
    
    private int count = 0;
    private int generation = 0;
    
    public Barrier(int threads) {
        this.threads = threads;
    }

    public synchronized void await() throws InterruptedException {
        int myGeneration = generation;
        count++;
        
        if (count == threads) {
            count = 0;
            generation++;
            notifyAll();
        } else {
            while (myGeneration == generation) {
                wait();
            }
        }
    }
}
```

*not reusable*
```java
public class MyBarrier {  
  
    private final int limit;  
    private volatile int count;  
  
    MyBarrier(int n){  
        this.limit = n;  
        this.count = 0;  
    }  
  
    synchronized void await() throws InterruptedException {  
        count++;  
  
        while (count < limit) {  
            wait();  
        }  
        notifyAll();  
  
    }  
}
```

With [[06 Semaphores|Semaphore]]: 

```java
import java.util.concurrent.Semaphore;

public class MyBarrier {
    private final int n;
    private int count = 0;

    private final Semaphore mutex = new Semaphore(1);
    private final Semaphore barrier1 = new Semaphore(0);
    private final Semaphore barrier2 = new Semaphore(1);

    public MyBarrier(int n) {
        this.n = n;
    }

    public void await() throws InterruptedException {
        // Phase 1: wait until all threads arrive
        mutex.acquire();
        count++;

        if (count == n) {
            barrier2.acquire();   // close second turnstile
            barrier1.release();   // open first turnstile
        }

        mutex.release();

        barrier1.acquire();
        barrier1.release();

        // Phase 2: wait until all threads leave phase 1
        mutex.acquire();
        count--;

        if (count == 0) {
            barrier1.acquire();   // close first turnstile
            barrier2.release();   // open second turnstile
        }

        mutex.release();

        barrier2.acquire();
        barrier2.release();
    }
}
```
