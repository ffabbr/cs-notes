
## Introduction

**Problems with locks**:
- ordering is hard
- can't combine thread safe operations
- locks are pessimistic
- synchronizations and locks are embedded in the code and not portable

Solution:

## Transactional Memory

defined "atomic blocks" and not bother about the HOW

**Ausführung passiert gleichzeitig, sieht für uns aber sequentiell aus.**

Mögliche Ansätze
- Thread erstellt lokale Kopie der Daten ("Snapshot"), macht die Änderungen dort, überprüft auf Konflikte und schreibt dann Änderungen atomar in den shared space, oder wiederholt
- track changes, when a Thread makes a change to a value that is being used by another, abort early 

**Eigenschaften**
- TM ist atomar, aber nicht mutex
- es können z.B. mehrere threads gleichzeitig beginnen
- transactions appear serialized: es muss so aussehen können, als wäre die Ausführung sequentiell
- Sobald eine eine Inkonsistenz zwischen lokaler Version und shared Version erkannt wird, wird abgebrochen (nicht einfach nicht committen)
- TM can be implemented in Hardware or Software. 

**Strong vs weak isolation**
- ==Strong isolation==: Garantiert Sicherheit, selbst wenn ein anderer Thread versucht, die Variable "normal" (ohne Transaktion, also ohne `atomic` block) zu lesen oder zu schreiben
- ==Weak isolation==: Shared state can **only** be read/modified in transactions (z.B. bei DiningPhilosophers muss ich auch bei put down forks atomic block haben)

**Nesting**
Was passiert, wenn eine Transaktion innerhalb einer anderen gestartet wird?
- ==Flat Nesting==: im Grunde nur eine einzige, große Transaktion. Wenn die innere Transaktion scheitert, bricht die komplette (auch die äußere) Transaktion ab.
- ==Closed Nesting==: Die innere Transaktion kann abbrechen und es neu versuchen, ohne dass die äußere Transaktion abgebrochen werden muss.

![[Bildschirmfoto 2026-06-04 um 11.32.23.png]]

Konzept immer: 
```
atomic {
	if (condition) STM.retry();
	do something
}
```

## ScalaSTM

- weak isolation
- closed nesting

**Bank account example**

Callable() when with return value instead of Runnable()

![[Bildschirmfoto 2026-05-27 um 16.36.21.png|350]]
![[Bildschirmfoto 2026-05-27 um 16.36.29.png|350]]
![[Bildschirmfoto 2026-05-27 um 16.37.50.png|350]]
![[Bildschirmfoto 2026-05-27 um 16.38.11.png|350]]

STM Retry: instead of aborting, retry: "wait bis es sich verändert", kein spin wait

![[Bildschirmfoto 2026-05-27 um 16.39.25.png|350]]

### Implementation of STM

- global clock (incremented with compare and set)
- each transaction reads latest value from clock, that's its "birthdate"
- when a transaction commits, the clock is incremented
- thread has "read set" (everything we have read from external) and "write set" (everything we have modified in local copy). each time check if needed Object is in write set already (local copy), if there, use. If not, get from external (check if timestamp of external value is younger as our transaction, if so, put into read set and continue. If not, abort.
- If all works out and we commit, we need to store into actual data. If it was only one object, easy (compare and set), but if multiple objects, needs locks (re-check everything again, then put elements from writeset to global including udpated birthdate)


---

## Message Passing

What if we avoid sharing state by using distributed memory?
Each thread/task has its own private state, they cooperate via message passing.

*Message Passing Interface* for communication: 

- a communicator is a set of threads that can talk about a task
- a thread can be part of multiple communicators
- each thread has a rank (id) within each communicator

![[Bildschirmfoto 2026-06-04 um 11.33.52.png|400]]

How to **SPMD** (Single Program, Multiple Data)

```java
if (rank == 0) {
    // (Master-Prozess) Verteile die Arbeit
} else {
    // Du bist Worker-Prozess, rechne
}
```

**Send:** 

```java
void Comm.Send(
	Object buf, // the data array to be sent
	int offset, // start index of relevant data
	int count,  // number of elements relevant
	Datatype datatype, // type of data
	int dest,  // Rank (id) of destination thread/process
	int tag    // id for this message
)
```


**Receive:** equivalent function similar to `Comm.Send()`, but with `src` instead of `dest`


**Synchronous Send**: send, then wait for recipient to actively receive
**Asynchronous Send**: send, then directly continue, buffer needed

**Blocking**: returns when buffer can be used again, but message transfer might not have been completed

**Non-blocking**: return immediately


![[Bildschirmfoto 2026-06-04 um 11.35.03.png|400]]

- **`Bcast` (Broadcast):** Sends a copy of the same data from one root process to all other processes in the communicator.

- **`Scatter`:** Divides a data array on a root process and sends a distinct, equal-sized chunk to each process.

- **`Gather`:** Collects distinct chunks of data from all processes and concatenates them into a single array on a root process.

- **`Reduce`:** Combines values provided by all processes using a specified mathematical operation (like sum, max, min) and stores the final result on a single root process.

- **`Allreduce`:** Identical to `Reduce`, but distributes the final computed result back to all processes so everyone has the answer.

- **`Barrier`:** A synchronization mechanism that forces all processes to pause; no process can execute past the barrier until every process has reached it.