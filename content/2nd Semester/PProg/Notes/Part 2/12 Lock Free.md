## Introduction

- **Lock-free**: always deadlock-free, failure of one thread cannot cause failure of another thread. But we can have starvation
- **Wait-freedom**: freedom of starvation. wait freedom => lock freedom


- readSomething() können wir einfach ohne locks machen
- writeSomething() mit CAS
  **Remember ==CAS==** (Compare and Swap): wenn wert im speicher gleich argument old, setze wert im speicher auf argument new. true means change was needed.

```java
do {
	
} while { 
	// if we have meen interleaved, try again
	!atomicReference.compareAndSet(oldObject, newObject)
} 
```


## Execution Timelines

<iframe src="https://cs.rohlik.net/2nd-Semester/PProg/Notes/Part-2/media/execution" width="100%" height="600"></iframe>


## Quiescent consistency

start: invocation
end: return

non-overlapping operations have sequential effect
for overlappint operations we cannot say something

## Sequential consistency



instructions executed in order, write operation instantly visible
we can't swap actions, but we can move actions on the timeline left and right

> !! learn quiescent consistency and sequential and see in the lines


## Linearizability

Instead of a line where things happen, it (the return/chagne of state) happens at a POINT between invocation and return. 

**ABA problem**: CAS suggests that no other thread has written between (a) and (c), but might be deceptive when changed and changed back again by another thread where the value now is the same but changes have been made (?)

**Muster bei Lock Free**: speicher geteilte variable in lokaler variable, am ende überprüfe ob sich geteilte variable geändert hat mit `do {} while (!top.compareAndSet(head, next))` 

## Stack mit Lock Free

```java
public class ConcurrentStack {
    AtomicReference<Node> top = new AtomicReference<Node>();

    public void push(Long item) { ... }
    public Long pop() { ... }
}
```

```java
public Long pop() {
    Node head, next;
    do {
        head = top.get();
        if (head == null) return null;
        next = head.next;
    } while (!top.compareAndSet(head, next));
    return head.item;
}
```

```java
public void push(Long item) {
    Node newi = new Node(item);
    Node head;

    do {
        head = top.get();
        newi.next = head;
    } while (!top.compareAndSet(head, newi));
}
```

## Performance

slow
add exponential backoff (remember [[04 Hardware Locks]])
- threads fight for access to same resource slows down
- solution: **go to sleep with random duration** → less try access at the same time
- double waiting duration each time the resource is not free, reset when accessed

## Linked list

We need double CAS (DCAS), meaning **2 flags**. Java has `AtomicMarkableReference<V>`, pointer with flag bits. with `getReference()` we get the actual pointer, `attemptMark` lets us mark flag with boolean, `compareAndSet`. 

Atomically swing reference or update flag, but remove in 2 steps (marker, redirect pointers).

Delete c: 

1. try to set mark (c.next)
2. `CAS( [b.next.reference, b.next.marked], [c, unmarked], [d, unmarked] )` 

Wenn Zeiger von b noch auf c zeigt UND b selbst nicht markiert ist (`[c, unmarked]`), dann ändere den Zeiger in einer unteilbaren Aktion so, dass er auf d zeigt UND unmarkiert bleibt (`[d, unmarked]`)

Issue: when deleting 2 subsequent nodes, both get marked but only one gets actually removed with the pointer

![[Bildschirmfoto 2026-05-11 um 10.47.58.png]]![[Bildschirmfoto 2026-05-11 um 10.48.10.png]]![[Bildschirmfoto 2026-05-11 um 10.48.19.png]]

## Queue

- 2 pointer (head, tail)
- dummy always-in Placeholder node am Anfang "null" Fall zu verhindern

![[Bildschirmfoto 2026-05-11 um 11.37.28.png]]![[Bildschirmfoto 2026-05-11 um 11.37.36.png]]

## ABA Problem

Beispiel Stack

**ABA problem**: CAS suggests that no other thread has written between (a) and (c), but might be deceptive when changed and changed back again by another thread where the value now is the same but changes have been made. When an activity fails to recognize that a single memory location was modified temporarily by another activity and therefore assumes that the overall state has not changed.

NodePool (stack of not active threads)

https://moodle-app2.let.ethz.ch/pluginfile.php/2560071/mod_resource/content/1/PP-l23-LockFreeProg.pdf
