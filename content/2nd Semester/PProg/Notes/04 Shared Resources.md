→ [[05 Slides.pdf]]

## Terminology and Introduction

![[2nd Semester/PProg/Slides/05 Slides.pdf#page=22|05 Slides]]

## synchronized

Wenn mehrere Objekte von/auf die gleiche Quelle readen/writen, dann ist ja die Reihenfolge random. Mit `synchronized` können wir aber Code-Blöcke festlegen, die definitiv in der Reihenfolge (und nacheinander) ausgeführt werden. 

Während `synchronized` ausgeführt wird, bekommt das einzig **der aktuelle Thread** den Zugriff auf die gemeinsame Quelle. Die Quelle ist ==locked==. Nachdem `synchronized` fertig ist, wird der lock freigegeben und andere Objekte können diesen "aquiren".

*==**locked**: no other thread can lock the object==*

When we perform a write on a thread with shared memory, do so under a lock.

![[2nd Semester/PProg/Slides/05 Slides.pdf#page=16]]
![[2nd Semester/PProg/Slides/05 Slides.pdf#page=17]]
![[2nd Semester/PProg/Slides/05 Slides.pdf#page=18]]

### Code example

![[2nd Semester/PProg/Slides/05 Slides.pdf#page=20]]


## Recursive Locks, Interleavings

> [!info]
> Java locks are reentrant. A thread can request a lock even if it has already and it won't through an error. 

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
#### Example 1

Both T1 and T2 lock on `this`, so they **cannot run at the same time**. One must finish completely before the other starts. This limits the possible interleavings to only two:

$$\underbrace{1 \to 2 \to 3}_{\text{T1 first}} \to \underbrace{4 \to 5 \to 6}_{\text{T2 second}} \quad \text{or} \quad \underbrace{4 \to 5 \to 6}_{\text{T2 first}} \to \underbrace{1 \to 2 \to 3}_{\text{T1 second}}$$

![[2nd Semester/PProg/Slides/05 Slides.pdf#page=27]]

#### Example 2, locking on different objects

Both threads must ==lock on the same object to protect the same shared resource==, so here mutual exclusion doesn't work. 

![[2nd Semester/PProg/Slides/05 Slides.pdf#page=29]]

> [!warning] Es gilt immer
> Exceptions are passed up

## Wait, Notify, NotifyAll

Often one part of the system generates work, another part processes it, buffer stores it for passing it on (f.ex. through a linked list):

$$\underbrace{\text{Producer}}_{\text{generates items}} \longrightarrow \underbrace{\text{Shared Buffer}}_{\text{queue of items}} \longrightarrow \underbrace{\text{Consumer}}_{\text{processes items}}$$

### Problem

Annahme mehrere Consumers machen:

```java
while (buffer.isEmpty()); // spin-wait
performLongRunningComputation(buffer.remove());
```

Dann könnte ein Consumer zwischen dem `.isEmpty()`check und dem removen das letzte Element removen, dann ist `.remove()` ungültig da leer. Selbst wenn nur eine Anweisung; z.B. `.remove()` sind mehrere Anweisungen im Bytecode. 

Synchronize? → ==Deadlock== 

![[2nd Semester/PProg/Slides/05 Slides.pdf#page=38]]

### Lösung

Consumer ==locks buffer== (synchronize). 

- `while(true)` means they constantly try to get access to the buffer
- `synchronize` means the actions in the block are executed in their order. After that block the lock is released and others can aquire it again, f.ex. through `while(true)`
- `buffer.wait()` give up lock mid `synchronize`. Makes Thread sleep until `notification` comes in, then picks up from where it went to `wait()`. But there's no guarantee that Consumer will get the lock after `.notifyAll()`. 

Producer adds an item and calls `notifyAll()`. Wakes up all threads currently sleeping in `wait()`. They all become RUNNABLE again and compete for the lock. Whoever wins re-checks `isEmpty()` via the `while` loop and either proceeds or goes back to sleep.

`notifyAll()` instead of `notify()`: multiple consumers, `notify()` might wake wrong thread,  `notifyAll()` wakes everyone and lets them sort it out. `notify()` wakes up a random thread. 

> [!warning]
> `while(condition){counter.wait()}`, NICHT `if`


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


---


