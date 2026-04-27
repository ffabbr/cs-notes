
- locks haben entweder 0 oder 1 Thread in der CS
- Semaphoren haben bis zu `s` Threads in der CS
- `acquire(S)` to `dec(S)` counter
- `release(S)` to `inc(S)` counter
- `release(S)` so oft aufrufen bis `s` richtige Zahl

**acquire(S)** *(atomic)*

```java
{ if S > 0 then
    dec(S)
  else
    put(Q_s, self)
    block(self)
  end }
```

**release(S)** *(atomic)*

```java
{ if Q_s == Ø then
    inc(S)
  else
    get(Q_s, p)
    unblock(p)
  end }
```


Beispiel: 

1. Thread A führt aus
2. Thread A macht `release(S)`, also erhöht sich der counter
3. Thread B führt aus
4. Thread B stösst auf `acquire(S)`. Wenn Thread A noch nicht `release` ausgeführt hat ist der counter 0, somit wird B schlafengelegt. So wartet B mit der letzten Operation bis A fertig ist. Wenn A schneller war ist der counter bereits erhöht, somit kann B den counter decrementen und fortfahren.

![[Bildschirmfoto 2026-04-27 um 10.57.34.png]]


## Phases

![[Bildschirmfoto 2026-04-27 um 11.39.23.png]]


## Barrier

Alle Threads kommen zum rendezvous Punkt, und erst dann laufen sie weiter. 
**Turnstile**: acquire, dann gleich release. Schritt für Schritt "releasen sich die Threads nacheinander".

