
Was, wenn ein Thread sehr viel länger braucht als die anderen? Dann funktioniert `fork/join` nicht mehr wirklich effizient. 

## Divide and Conquer

![[2nd Semester/PProg/Slides/08 Slides.pdf#page=35|08 Slides]]

```pseudocode
- if cannot divide:
  - return unitary solution (stop recursion)
- divide problem in two:
  - solve first (recursively)
  - solve second (recursively)
- combine solutions
- return result
```

Code example: [[2nd Semester/PProg/Slides/08 Slides.pdf#page=23|Summing an Array]]

- Wenn ein Thread nicht erstellt werden kann aufgrund mangelnder Ressourcen: **Exception, out of Memory**
- Achtung auf richtige `start/join` Reihenfolge, sonst ist es vielleicht sequentiell
- due to **thread overhead**, sequentially creating a thread for every operation is inefficient. 
	- use a sequential cutoff, f.ex. when summing, around 500-1000
	- do not create two recursive threads; create one and do the other work on the thread that initiates the other thread

## Zuteilung von Task auf Threads

Zur Arbeitsaufteilung, also der Zuteilung von Tasks zu Threads nutzen wir ==Java Frameworks==, z.B.  
 - den [[#Framework Executor Service|Executor Service]], oder
 - das Fork/Join Framework

## Framework: Executor Service

> [!warning]
> Problem vom Executor Service: [[2nd Semester/PProg/Slides/08 Slides.pdf#page=47|Threads blockieren]]. Daher ==nicht verwenden für **rekursive** Probleme==. Für flat structures or tasks that can run independently in parallel gut. 

1. Main thread submits task to the Executor Service
2. Main thread immediately gets back a `future` by the Executor Service. The future will later hold the result once the calculation is done. 
3. Executor Service calculates in parallel
4. the Main thread can at any time access the future and see if the result of the calculation is stored there already

### Callable vs Runnable

![[2nd Semester/PProg/Slides/08 Slides.pdf#page=40]]

```java
.submit(Callable<T> task) → Future<T>
.submit(Runnable task) → Future<?>
```

### Executor Service Syntax (Hello World)

```java
int ntasks = 1000;
ExecutorService exs = Executors.newFixedThreadPool(4);

for (int i = 0; i < ntasks; i++) {
    HelloTask t = new HelloTask("Hello from task " + i);
    exs.submit(t);
}

exs.shutdown(); // initiate shutdown, does not wait, but can't submit more tasks
```

```java
static class HelloTask implements Runnable {

    String msg;

    public HelloTask(String msg) {
        this.msg = msg;
    }

    public void run() {
        long id = Thread.currentThread().getId();
        System.out.println(msg + " from thread: " + id);
    }
}
```


## Fork Join Framework

→ when a task is waiting, it is suspended and other tasks are allowed to run

Wie beim [[#Framework Executor Service]] lesen Threads von der `global queue`. Neu: jeder Thread hat eine `local queue`. 


Jeder Thread arbeitet die `local queue` in LIFO (last in first out) ab. Also stellt man sich die Queue als Röhre vor, kommen neue Aufgaben (bei einer Rekusion also zuerst die grösseren Aufgaben) von links hinein, und werden per LIFO auch von links abgearbeitet. 

Ein Thread kann auch auf die `local queue` von einem anderen Thread zugreiten, in FIFO (also von hinten der local queue des anderen Threads). Eine hintere Aufgabe ist also eine aufwendigere (gut für Lastverteilung).

![[2nd Semester/PProg/Slides/08 Slides.pdf#page=55]]

Instead of 



```java
ForkJoinRecursiveSum left = new ForkJoinRecursiveSum(arr, lo, mid);
ForkJoinRecursiveSum right = new ForkJoinRecursiveSum(arr, mid, hi);

left.fork();
right.fork();

int leftAns = left.join();
int rightAns = right.join();

// Better:
//left.fork();
//int rightAns = right.compute();
//int leftAns = left.join();
```


![[2nd Semester/PProg/Slides/08 Slides.pdf#page=62]]