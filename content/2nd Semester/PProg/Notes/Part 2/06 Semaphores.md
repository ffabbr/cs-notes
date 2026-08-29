
Semaphoren erlauben mehreren Threads Zugriff bis zu einer festen Grenze. Sie funktionieren wie ein Zähler für verfügbare Plätze.

Locks haben entweder 0 oder 1 Thread in der CS. Semaphoren haben bis zu `s` Threads in der CS.

Vgl. Parkhaus mit Kapazität s

- `acquire(S)` to `dec(S)` counter
- `release(S)` to `inc(S)` counter

## Beispiel

1. Thread A führt aus
2. Thread A macht `release(S)`, also erhöht sich der counter
3. Thread B führt aus
4. Thread B stösst auf `acquire(S)`. Wenn Thread A noch nicht `release` ausgeführt hat ist der counter 0, somit wird B schlafengelegt. So wartet B mit der letzten Operation bis A fertig ist. Wenn A schneller war ist der counter bereits erhöht, somit kann B den counter decrementen und fortfahren.

![[Bildschirmfoto 2026-04-27 um 10.57.34.png]]


```java
public class MySemaphore {  
    private int count;  
    public MySemaphore(int maxCount) {  
        count = maxCount;  
    }  
  
    public void acquire() throws InterruptedException {  
        synchronized (this) {  
            while (count == 0) this.wait();  
            count--;  
        }  
    }  
  
    public void release() {  
        synchronized (this) {  
            count++;  
            this.notify();  
        }  
    }  
}
```
