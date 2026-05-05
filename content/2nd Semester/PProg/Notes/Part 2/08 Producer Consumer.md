
- T0 rechnet x aus und gibt es an T1 weiter
- x muss nicht synchronisiert werden da immer nur ein Thread zugreift, müssen nur Zugriff managen
- Queue mit pointern für `out` und `in` position und **==wrap-around Semantik==** (das lineare array springt nach dem Ende an den Anfang (position mod länge))

Voll und leer erkennen: 
- Queue leer: in und out pointer gleich
- Queue voll: wenn ich noch ein Element einfüge, ist in gleich out. Wir definieren also die Queue als "voll", wenn noch genau ein Platz frei ist

![[Bildschirmfoto 2026-04-29 um 14.39.54.png]]![[Bildschirmfoto 2026-04-29 um 14.40.16.png]]

---

## PC with Semaphores

2 Semaphoren zählen, ob der Puffer **nicht leer** oder **nicht voll** ist, sodass Consumer nur bei vorhandenen Elementen und Producer nur bei freiem Platz weiterlaufen.

Ein zusätzlicher binärer Semaphore schützt den gemeinsamen Puffer, damit immer nur ein Thread gleichzeitig `buf`, `in` und `out` verändert.

![[Bildschirmfoto 2026-04-29 um 15.00.13.png]]![[Bildschirmfoto 2026-04-29 um 15.00.26.png]]

## PC with Lock

ein gemeinsamer Lock schützt den Puffer, damit nur ein Thread gleichzeitig `buf`, `in` und `out` verändert

2 **Conditions**: Producer warten auf `notFull`, wenn der Puffer voll ist, und Consumer warten auf `notEmpty`, wenn der Puffer leer ist.

![[09 Monitors#PC with Lock (Monitors)]] 


## PC with Sleeping Barber

- Will nicht notFull und notEmpty nicht senden obwohl keine threads warten
- Idee Barber checks waiting room, sleeps. Client either enqueues or wakes barber. Achtung, wenn barber und client gleichzeitig schauen deadlock

Lösung

- add counters for clients and barbers. 
- m <= 0: buffer full, -m clients waiting
- n <= 0, buffer empty, -n barbers waiting

![[Bildschirmfoto 2026-05-04 um 10.38.49.png]]