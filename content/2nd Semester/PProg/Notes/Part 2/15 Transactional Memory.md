
## Introduction

**Problems with locks**:
- ordering is hard
- can't combine thread safe operations
- locks are pessimistic
- synchronizations and locks are embedded in the code

Solution: **atomic locks** (transactions)

## Transactional Memory

**Transaktion "sieht konsistente Welt" in der gesamten Ausführungszeit**
Das ist möglich durch 

a. Thread erstellt lokale Kopie der Daten ("Snapshot"), macht die Änderungen dort, überprüft auf Konflikte und schreibt dann Änderungen atomar in den shared space, oder wiederholt

b. track changes, when a Thread makes a change to a value that is being used by another, abort early 

**Eigenschaften**
- TM ist atomar, aber nicht mutex
- es können z.B. mehrere threads gleichzeitig beginnen
- transactions appear serialized: es muss so aussehen können, als wäre die Ausführung sequentiell
- Sobald eine eine Inkonsistenz zwischen lokaler Version und shared Version erkannt wird, wird abgebrochen (nicht einfach nicht committen)
- TM can be implemented in Hardware or Software. 

**Strong vs weak isolation**
- ==Strong isolation==: Garantiert Sicherheit, selbst wenn ein anderer Thread versucht, die Variable "normal" (ohne Transaktion) zu lesen oder zu schreiben
- ==Weak isolation==: not allowed

**Nesting**
Was passiert, wenn eine Transaktion innerhalb einer anderen gestartet wird?
- ==Flat Nesting==: Grunde nur eine einzige, große Transaktion. Wenn die innere Transaktion scheitert, bricht die komplette (auch die äußere) Transaktion ab.
- ==Closed Nesting==: Die innere Transaktion kann abbrechen und es neu versuchen, ohne dass die äußere Transaktion abgebrochen werden muss.

## ScalaSTM


---

## Message Passing

What if we avoid sharing state?
Each thread/task has its own private state, they cooperate via message passing

*Message Passing Interface* for communication: 

- a communicator is a set of threads that can talk about a task
- a thread can be part of multiple communicators
- each thread has a rank (id) within each communicator

How to **SPMD** (Single Program, Multiple Data)

```java
if (rank == 0) {
    // Du bist der Chef (Master-Prozess): Verteile die Arbeit!
} else {
    // Du bist ein Arbeiter (Worker-Prozess): Rechne die Daten durch!
}
```

Send: 

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


**Synchronous Send**: send, then wait for recipient to actively receive
**Asynchronous Send**: send, then directly continue, buffer needed