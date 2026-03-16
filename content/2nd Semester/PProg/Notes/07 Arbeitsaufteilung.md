
Was, wenn ein Thread sehr viel länger braucht als die anderen? Dann funktioniert `fork/join` nicht mehr wirklich effizient. 

## Divide and Conquer

![[08 Slides.pdf#page=35]]

```pseudocode
- if cannot divide:
  - return unitary solution (stop recursion)
- divide problem in two:
  - solve first (recursively)
  - solve second (recursively)
- combine solutions
- return result
```

Code example: [[08 Slides.pdf#page=23|Summing an Array]]

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
> Problem vom Executor Service: [[08 Slides.pdf#page=47|Threads blockieren]]. Daher ==nicht verwenden== für rekursive Probleme. Für flat structures or tasks that can run independently in parallel gut. 


1. Main thread submits task to the Executor Service
2. Main thread immediately gets back a `future` by the Executor Service. The future will later hold the result once the calculation is done. 
3. Executor Service calculates in parallel
4. the Main thread can at any time access the future and see if the result of the calculation is stored there already

### Callable vs Runnable

![[08 Slides.pdf#page=40]]

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


