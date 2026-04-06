## External Locks
![[2nd Semester/PProg/Slides/10 Slides.pdf#page=19]]![[2nd Semester/PProg/Slides/10 Slides.pdf#page=27]]

## Race Conditions

Race Condition: Berechnungsergebnis hängt von Ausführungsreihenfolge ab. 

**Low-level race conditions: ==data races==**
- fehlerhaftes Programm, da mehrere Threads auf geteilte Ressource zugreifen (lesen/schreiben) → error
- [[2nd Semester/PProg/Slides/10 Slides.pdf#page=32]]

**High-level race conditions: ==bad interleavings==**
- fehlerhaftes Programm, da falsche Ausfühungsreihenfolge trotz guter Synchronisation von Ressourcen
- [[2nd Semester/PProg/Slides/10 Slides.pdf#page=33]]
## Peek

Looks at the top element of a stack without changing anything (`pop`, then `push`). `Push` and `pop` are synchronized in java, but our peek function per default is not → bad interleavings possible. 

Solution: `synchronize` entire `peek` function. 

```java
class Stack<E> {
    ...
    synchronized E peek() {
        E ans = pop();
        push(ans);
        return ans;
    }
}
```