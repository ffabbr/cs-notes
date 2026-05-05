
## Introduction

- **Lock-free**: always deadlock-free, failure of one thread cannot cause failure of another thread. But we can have starvation
- **Wait-freedom**: freedom of starvation

Remember CAS (Compare and Swap): wenn wert im speicher gleich argument old, setze wert im speicher auf argument new. true means change was needed.

ABA problem: CAS suggests that no other thread has written between (a) and (c), but might be deceptive when changed and changed back again by another thread where the value now is the same but changes have been made (?)

Muster bei Lock Free: speicher geteilte variable in lokaler variable, am ende überprüfe ob sich geteilte variable geändert hat mit `do {} while (!top.compareAndSet(head, next))` 
## Kellerspeicher (Stack) mit Lock Free

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


We need double CAS, meaning 2 flags. Java has `AtomicMarkableReference<V>`, pointer with flag bits. with `getReference()` we get the actual pointer, `attemptMark` lets us mark flag with boolean, `compareAndSet`. 