→ [[05 Slides.pdf]]

## Terminology and Introduction

| **Begriff**          | **Beschreibung**                                                                                                                                                                                       |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Data Race**        | Ein Thread schreibt, während ein anderer Thread gleichzeitig denselben Ort liest oder beschreibt.                                                                                                      |
| **Deadlock**         | Mehrere Threads warten darauf, dass der jeweils andere eine Ressource freigibt. Zyklische Abhängigkeit ($\infty$ wenn aufgemalt). Directed Graph describing relation or Threads and Locks has a cycle. |
| **Livelock**         | In Livelocks the system makes no progress, although the threads execute statements/use CPU time. In deadlocks, no statements are executed.                                                             |
| **Bad Interleaving** | Die zeitliche Abfolge der Schritte verschiedener Threads führt zu falschem Endergebnis, selbst wenn die einzelnen Schritte an sich korrekt sind.                                                       |
| **Critical Section** | Ein sensibler „Einer-nach-dem-Anderen“-Bereich im Code, in dem auf gemeinsam genutzte Daten zugegriffen wird.                                                                                          |
| **Mutual Exclusion** | Ein 2. Thread kann keinen kritischen Abschnitt betreten, bevor der aktuelle Thread ihn verlassen hat. Synchronize blocks create mutual exclusion.                                                      |
| **Atomicity**        | Eine Gruppe von Operationen, die unteilbar ausgeführt werden. Kein anderer Thread kann die Daten in einem halbfertigen Zustand sehen.                                                                  |

## synchronized

> [!warning]
> NIE synchronized auf einen Boxed type wie z.B. `Integer`. Problem ist, bei `x+=1` erstellt Java ein neues Objekt

Wenn mehrere Objekte von/auf die gleiche Quelle readen/writen, dann ist ja die Reihenfolge random. Mit `synchronized` können wir aber Code-Blöcke festlegen, die definitiv in der Reihenfolge (und nacheinander) ausgeführt werden. 

Während `synchronized` ausgeführt wird, bekommt einzig **der aktuelle Thread** den Zugriff auf die gemeinsame Quelle. Die Quelle ist ==locked==. Nachdem `synchronized` fertig ist, wird der lock freigegeben und andere Objekte können diesen "aquiren".

When we perform a write on a thread with shared memory, do so under a lock.

Wenn wir `public synchronized run() {}` zur Methode schreiben synchronisieren wir auf `this`. Wenn wir auf ein anderes Objekt synchronisieren wollen, schreiben wir 

```java
public void run(){
	synchronized (x) {
		// code
	}
}
```

### Code example

![[2nd Semester/PProg/Slides/05 Slides.pdf#page=20]]


## Recursive Locks, Interleavings

- If a thread tries to acquire a lock that is already taken, it becomes blocked and must wait until woken up. See the [[2nd Semester/PProg/Slides/01 Slides.pdf#page=36|Life cycle of a thread]] for reference.
- Java locks are reentrant. A thread can request a lock even if it has already and it won't throw an error. It will increase the **lock count, and we will have to release the lock twice too**.

### Recursive Locks

==The lock belongs to the thread, not to the method==. This means that **the thread carries the lock with it** as it moves through method calls, rather than the lock being tied to a specific method. 

So methods can pass around the lock without releasing it. 

```java
public class Foo {
    public synchronized void f() { … }
    public synchronized void g() { … f(); … }
}
```

### Interleavings

Without `synchronized`, all instructions are shuffeled ("interleaved") in each other. With `synchronized` we can control the possible interleavings.

Both threads must ==lock on the same object to protect the same shared resource==
#### Example

Both T1 and T2 lock on `this`, so they **cannot run at the same time**. One must finish completely before the other starts. This limits the possible interleavings to only two:

$$
\underbrace{1 \to 2 \to 3}_{\text{T1 first}} \to \underbrace{4 \to 5 \to 6}_{\text{T2 second}} \quad \text{or} \quad \underbrace{4 \to 5 \to 6}_{\text{T2 first}} \to \underbrace{1 \to 2 \to 3}_{\text{T1 second}}
$$

![[2nd Semester/PProg/Slides/05 Slides.pdf#page=27]]

## Wait, Notify, NotifyAll

Example: each runner can start after the previous runner finished (except the first one)

![[Bildschirmfoto 2026-03-18 um 17.23.31.png]]

![[Bildschirmfoto 2026-04-06 um 22.14.38.png]]

> [!warning]
> NIE synchronized auf einen Boxed type wie z.B. `Integer`. Problem ist, bei `x+=1` erstellt Java ein neues Objekt! 


### Producer-Consumer

Often one part of the system generates work, another part processes it, buffer stores it for passing it on (f.ex. through a linked list):

$$
\underbrace{\text{Producer}}_{\text{generates items}} \longrightarrow \underbrace{\text{Shared Buffer}}_{\text{queue of items}} \longrightarrow \underbrace{\text{Consumer}}_{\text{processes items}}
$$


Annahme mehrere Consumers machen:

```java
while (buffer.isEmpty()); // spin-wait
	buffer.remove();
```

Dann könnte ein Consumer zwischen dem `.isEmpty()`check und dem removen das letzte Element removen, dann ist `.remove()` ungültig da leer. Selbst wenn nur eine Anweisung; z.B. `.remove()` sind **mehrere Anweisungen im Bytecode**. 

Synchronize? → ==Deadlock== 

![[2nd Semester/PProg/Slides/05 Slides.pdf#page=38]]

Stattdessen (richtig): 

- `while(true)` means they constantly try to get access to the buffer
- `synchronize` means the actions in the block are executed in their order. After that block the lock is released and others can aquire it again, f.ex. through `while(true)`
- `buffer.wait()` give up lock mid `synchronize`. Makes Thread sleep until `notification` comes in, then picks up from where it went to `wait()`. But there's no guarantee that Consumer will get the lock after `.notifyAll()`. 

Producer adds an item and calls `notifyAll()`. Wakes up all threads currently sleeping in `wait()`. They all become RUNNABLE again and compete for the lock. Whoever wins re-checks `isEmpty()` via the `while` loop and either proceeds or goes back to sleep.

`notifyAll()` instead of `notify()`: multiple consumers, `notify()` might wake wrong thread,  `notifyAll()` wakes everyone and lets them sort it out. `notify()` wakes up a random thread. 

> [!warning]
> `while(condition) { counter.wait() }`, NICHT `if`. 
> This is because sometimes **Threads get woken up randomly**. 


![[2nd Semester/PProg/Slides/05 Slides.pdf#page=39]]

![[2nd Semester/PProg/Slides/05 Slides.pdf#page=40]]

![[2nd Semester/PProg/Slides/05 Slides.pdf#page=44]]


---

#### wait vs join

|                             | `wait()`                                | `join()`                        |
| --------------------------- | --------------------------------------- | ------------------------------- |
| Called on                   | any object (the lock)                   | a `Thread` object               |
| Purpose                     | wait for a **condition** to become true | wait for a **thread to finish** |
| Woken up by                 | `notify()` / `notifyAll()`              | the thread terminating          |
| Releases lock?              | **Yes**                                 | No                              |
| Used inside `synchronized`? | Yes, required                           | No                              |


