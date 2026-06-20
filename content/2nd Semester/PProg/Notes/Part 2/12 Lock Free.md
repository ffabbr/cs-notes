## Concepts of Lock Free

- **Lock-free**: always deadlock-free, failure of one thread cannot cause failure of another thread. But we can have starvation
- **Wait-freedom**: freedom of starvation. wait freedom => lock freedom

- readSomething() können wir einfach ohne locks machen
- writeSomething() mit CAS

**Remember ==CAS==** (Compare and Swap): wenn wert im speicher gleich argument old, setze wert im speicher auf argument new. true means change was needed.

```java
do {
	
} while { 
	// if we have been interleaved, try again
	!atomicReference.compareAndSet(oldObject, newObject)
} 
```

### ABA Problem

Beispiel Stack

CAS suggests that no other thread has written between (a) and (c), but might be deceptive when changed and changed back again by another thread where the value now is the same but changes have been made. When an activity fails to recognize that a single memory location was modified temporarily by another activity and therefore assumes that the overall state has not changed.

Remedies: 
- Pointer tagging (use bits as counter)
- hazard pointers 

---

## Lock-Free Programming

**Muster bei Lock Free**: speicher geteilte variable in lokaler variable, am ende überprüfe ob sich geteilte variable geändert hat

```java
do {
      head = top.get();        // 1. lies geteilte Variable lokal
      newi.next = head;        // 2. bereite Änderung vor
  } while (!top.compareAndSet(head, newi));  // 3. war niemand dazwischen? → fertig
```

### Stack mit Lock Free

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

### Performance

slow, weil viele Threads `top` wollen
add exponential backoff (remember [[04 Hardware Locks]])
- threads fight for access to same resource slows down
- solution: **go to sleep with random duration** → less try access at the same time
- double waiting duration each time the resource is not free, reset when accessed

### Linked list

Beim Stack reichte ein CAS. Bei einer verketteten Liste müssen beim Löschen zwei Dinge gleichzeitig passieren:
1. Den Node als "gelöscht" markieren
2. Den Zeiger des Vorgängers umhängen

Ohne Atomarität kann ein anderer Thread zwischen diesen zwei Schritten einfügen

`AtomicMarkableReference<V>`, pointer + flag bit. with `getReference()` we get the actual pointer, `attemptMark` lets us mark flag with boolean, `compareAndSet`. 

Delete c: 

1. try to set mark (c.next)
2. `CAS( [b.next.reference, b.next.marked], [c, unmarked], [d, unmarked] )` 

Wenn Zeiger von b noch auf c zeigt UND b selbst nicht markiert ist (`[c, unmarked]`), dann ändere den Zeiger in einer unteilbaren Aktion so, dass er auf d zeigt UND unmarkiert bleibt (`[d, unmarked]`)

Issue: when deleting 2 subsequent nodes, both get marked but only one gets actually removed with the pointer

![[Bildschirmfoto 2026-05-11 um 10.47.58.png]]![[Bildschirmfoto 2026-05-11 um 10.48.10.png]]![[Bildschirmfoto 2026-05-11 um 10.48.19.png]]

### Queue

- 2 pointer (head, tail)
- dummy always-in Placeholder node am Anfang "null" Fall zu verhindern

![[Bildschirmfoto 2026-05-11 um 11.37.28.png]]![[Bildschirmfoto 2026-05-11 um 11.37.36.png]]


