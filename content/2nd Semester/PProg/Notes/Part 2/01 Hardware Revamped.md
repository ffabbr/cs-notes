
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

*Welche Garantien über die Ausführungsreihenfolge habe ich?* 

| Abbreviation | Full Term                 |
| :----------- | :------------------------ |
| **JMM**      | Java Memory Model         |
| **PO**       | Program Order             |
| **SA**       | Synchronization Action(s) |
| **SO**       | Synchronization Order     |
| **SW**       | Synchronizes-with         |
| **HB**       | Happens-Before            |

Your code runs in [[#Program Order]] when seen a single thread in isolation. Because the CPU reorders things, [[#Synchronization Actions]] create a [[#Synchronization Order]]. When threads interact with these actions, they create a [[#Synchronizes-with]] handshake. This handshake establishes a [[#Happens-Before]] relationship, which is the only way to guarantee that Thread B actually sees what Thread A just did.

> [!warning]
> Rescheduling on a single Thread can only happen in a way that the programmer doesn't notice. 

### Program Order

The order of statement execution on a singal thread. The JMM can re-order though, this is about the order of execution.
**Total order on one thread, but not across threads** (partial order on thread==s==). 

### Synchronizes-with

Two threads "touch" the same point on that master timeline through a Synchronization Action (like reading and writing the same `volatile` variable), creating a **handshake**.

A write to a `volatile` variable `V` _synchronizes-with_ every subsequent read of `volatile` variable `V` by any thread.

#### Synchronization Actions

**Critical actions that need a fixed order.**

- Read/write of **volatile variable**
- Lock/Unlock [[09 Monitors|monitor]] (what is a monitor?)
- First/last action of a thread (synthetic)
- First/last action, starting, or terminating a thread

### Synchronization Order

Global order of all [[#Synchronization Actions]].

- **Total Order:** every thread in the application agrees on this order
- **Consistency:** If you look at the SO, ==read/write of a `volatile` var will make sure all variables that were updated before this statement are up to date.== 

### Happens-Before

- transitive closure of program order and synchronizes-with order (rote Linie durch den ganzen code)
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