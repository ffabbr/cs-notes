
Parallel output order changes between runs, because ==console access is random==. 

## Single-Core

- A single-core CPU can execute one instruction at a time, meaning sequentially. 
- processes share CPU, but **each process has own memory space**
- während wir auf Nutzereingabe warten, ist CPU auf **idle**, was man vermeiden möchte
- die OS scheduler sind für die Arbeitsverwaltung zuständig
- der **CPU scheduler** verteilt CPU zwischen Prozessen (zwischen Prozessen wechseln)

![[Bildschirmfoto 2026-04-05 um 01.05.47.png]]

### Every process needs context (PCB)

- **hardware** context
- **memory** context
- **os-level** context

- changing to another process requires a context switch, resulting in large overhead
- swap memory (green) is a lot slower

![[2nd Semester/PProg/Slides/01 Slides.pdf#page=12]]

### OS manages processes

- starts processes
- ends processes
- controls resource usage
- schedules cpu time
- allows inter-process communication

### Context switching

1. P1 is executing
2. capture PCB(1)
3. load PCB(2)
4. P2 is executing

## Prallelism and Concurrency

- ==concurrency==: multiple processes are being worked on, not necessarily simultaneously
- ==parallelism==: multiple processes execute simulatneously on different CPU cores

![[2nd Semester/PProg/Slides/01 Slides.pdf#page=17]]

## Threads

- independent sequences of execution on the same process
- Context switching between threads is ***efficient*** 

- share memory space
- have own execution stack 
- have own instruction screen 

![[2nd Semester/PProg/Slides/01 Slides.pdf#page=23]] 
![[2nd Semester/PProg/Slides/01 Slides.pdf#page=25]] 

#### Thread Attributes

- id
- name
- priority
- status (new, runnable, blocked, waiting, terminated, etc.)

### Threads in Java

- the console is shared between all threads, internal mechanisms make sure only one thread read/writes at the same time. who gets access is ==random==
- Threads can **continue to run even if main() returns** already

![[2nd Semester/PProg/Slides/01 Slides.pdf#page=36]] 

#### Option 1

Override run method and call `.start` to create the thread. 

```java
class ConcurrWriter extends Thread { 
	public void run() {
		// if multiple threads started -> concurrent execution
	}
}
ConcurrWriter writerThread = new ConcurrWriter();
writerThread.start(); // calls ConcurrWriter.run()
```

#### Option 2

```java
public class ConcurrWriter implements Runnable {
	public void run() { ...
		// if multiple threads started -> concurrent execution
	}
}

ConcurrWriter writerTask = new ConcurrWriter(); // task
Thread t = new Thread(writerTask); // executor
t.start(); // calls ConcurrWriter.run()
```


