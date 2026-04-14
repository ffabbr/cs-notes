
## Introduction

- 2 threads with k statements each: $2k \choose k$ possible interleavings (ziehen ohne zurücklegen)
- showing that something isn't possible by showing what needs to happen before something and through transitivity find a contradiction (a circle when drawn)
- parallel threads interacting via shared memory depends on **hardware, runtime system, and programming language**.
- Compiler, CPU and memory reorder for better performance (works sequentially, might break in parallel)
- possible solutions for bugs caused by cpu based memory optimizations
	- synchronized (slow)
	- volatile (slow)

- Architekturen heutzutage (x86, AMD64, ARM, etc.) sind **nicht ==sequentiell konsistent==**. Umordnung kann also vorkommen. Als Lösung: 

## Java Memory Model (JMM)

Legt valide und nicht valide Ausführungsreihenfolgen fest.

| Abbreviation | Full Term                 |
| :----------- | :------------------------ |
| **JMM**      | Java Memory Model         |
| **PO**       | Program Order             |
| **SA**       | Synchronization Action(s) |
| **SO**       | Synchronization Order     |
| **SW**       | Synchronizes-with         |
| **HB**       | Happens-Before            |

Your code runs in [[#Program Order]] when seen a single thread in isolation. Because the CPU reorders things, [[#Synchronization Actions]] create a [[#Synchronization Order]]. When threads interact with these actions, they create a [[#Synchronizes-with]] handshake. This handshake establishes a [[#Happens-Before]] relationship, which is the only way to guarantee that Thread B actually sees what Thread A just did.

### Program Order

Order of statements exactly as they are written in the source code. How things happen in isolation. Single thread in isolation is always correct in program order. 

**Total order on one thread, but not across threads** (partial order on thread==s==). 

### Synchronization Actions and Order

Synchronization Actions (SA) form the Synchronization Order (SO). 
#### Synchronization Order

Total, global order of all [[#Synchronization Actions]], to prevent CPU reordering from breaking the program.

- **Total Order:** Every single thread in the application agrees on the exact sequence of these specific actions.
- **Consistency:** If you look at the SO, a `volatile` read of variable `X` will always see the value written by the most recent `volatile` write to `X` in that order.

#### Synchronization Actions

**Critical actions that need a fixed order.**

- Read/write of **volatile variable**
- Lock/Unlock monitor (what is a monitor?)
- First/last action of a thread (synthetic)
- First/last action, starting, or terminating a thread

### Synchronizes-with

Two threads "touch" the same point on that master timeline (like reading and writing the same `volatile` variable), creating a **handshake**.

A write to a `volatile` variable `V` _synchronizes-with_ every subsequent read of `volatile` variable `V` by any thread.

### Happens-Before

- combining Program Order and Synchronizes-With rules
- everything Thread A did before the handshake is guaranteed to be visible to Thread B.

**HB Consistent**

Read
- The **most recent write** in its happens-before chain, **OR**
- Any **unordered write** (a write with no HB relationship to the read).

**HB Inconsistent**

Read
- An **outdated write** (one already overwritten by a newer write in the HB chain), **OR**
- A **future write** (one that happens-before the read)

![[Bild.jpeg]]