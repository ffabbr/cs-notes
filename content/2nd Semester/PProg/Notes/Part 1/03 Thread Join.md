
**Busy waiting**: Main thread überprüft laufend ob das Resultat der worker-Threads schon da sind. Braucht CPU Zeit.

## Java Join

- instead of constantly checking, let main thread go to sleep and wake up when results ready
- join produces overhead, so if worker threads are quick, busy waiting might be better

- f.ex. in the main thread, call `worker.join()` to make main sleep until worker finishes
- `thread.join()` may throw an Exception, so put in try catch 

## Exceptions

- In a sequential program an exception terminates the program, if not caught. 
- if a worker thread throws exception
	- exception is shown on console
	- `thread.join()` is unaffected
	- main thread may not be aware

![[2nd Semester/PProg/Slides/01 Slides.pdf#page=58|01 Slides]]


## Interrupt Threads

Threads können sich immer nur selbst interrupten. Aber möglich ist ein Interrupt flag, dass der andere Thread lesen und reagieren kann. 

```java
public class InterruptDemo {

    static class MyTask implements Runnable {
        public void run() {
            while (!Thread.currentThread().isInterrupted()) {
                // keep running
            }
            System.out.println("Stopped!");
        }
    }

    public static void main(String[] args) throws InterruptedException {

        Thread t = new Thread(new MyTask());
        t.start();

        Thread.sleep(100); 
        t.interrupt();     // set interrupt flag
    }
}
```
