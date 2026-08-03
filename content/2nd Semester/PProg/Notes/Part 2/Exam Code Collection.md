
## (!!) 03 Software Locks

### Dekker's Lock
Two-process mutual exclusion. Combines interest flags (`wantp`/`wantq`) with a `turn` variable that resolves conflicts: if both want the lock, the one whose turn it is *not* backs off and waits.

```text
volatile boolean wantp = false, wantq = false;  integer turn = 1

// Process P                         // Process Q
loop                                 loop
  non-critical section                 non-critical section
  wantp = true                         wantq = true
  while (wantq) {                      while (wantp) {
    if (turn == 2) {                     if (turn == 1) {
      wantp = false                        wantq = false
      while (turn != 1);                   while (turn != 2);
      wantp = true; }}                     wantq = true; }}
  critical section                      critical section
  turn = 2                              turn = 1
  wantp = false                         wantq = false
```

### Dekker's Lock in Java
Same algorithm with atomics: `want[id]` = interested; if the other wants it and it is the other's `turn`, back off (clear your flag, wait for the turn, re-assert).

```java
AtomicIntegerArray want = new AtomicIntegerArray(2);
AtomicInteger turn = new AtomicInteger(0);

void lock(int id) {
    want.set(id, 1);
    while (want.get(1 - id) == 1) {
        if (turn.get() == (1 - id)) {
            want.set(id, 0);
            while (turn.get() == (1 - id)) { /* wait */ }
            want.set(id, 1);
        }
    }
}

void unlock(int id) {
    turn.set(1 - id);
    want.set(id, 0);
}
```

### Peterson Lock (two processes)
Simplest correct + fair 2-thread lock. Announce interest, then mark yourself the `victim` (let the other go first); busy-wait while the other is interested and you are the victim.

```text
let P=1, Q=2;  volatile boolean flag[1..2] = [false, false];  volatile int victim = 1

// Process P                          // Process Q
loop                                  loop
  non-critical section                  non-critical section
  flag[P] = true                        flag[Q] = true
  victim  = P                           victim  = Q
  while (flag[Q] && victim == P);       while (flag[P] && victim == Q);
  critical section                      critical section
  flag[P] = false                       flag[Q] = false
```

### Peterson Lock — correct Java (atomics)
The fix for the bug above: use `AtomicIntegerArray` for `flag` and `AtomicInteger` for `victim` so the elements are truly atomic/visible (0 = false, 1 = true).

```java
AtomicIntegerArray flag = new AtomicIntegerArray(2);   // 0 = false, 1 = true
AtomicInteger victim = new AtomicInteger();

public void lock(int id) {
    flag.set(id, 1);
    victim.set(id);
    while (flag.get(1 - id) == 1 && victim.get() == id) { /* wait */ }
}

void unlock(int id) {
    flag.set(id, 0);
}
```

### Filter Lock (n processes)
Generalizes Peterson to `n` threads through `n-1` levels. Each level has one `victim` that must let others pass; a thread climbs a level only when no one else is at its level or above.

```text
int[] level(#threads), int[] victim(#threads)

lock(me) {
  for (int i = 1; i < n; ++i) {
    level[me] = i;
    victim[i] = me;
    while (∃k ≠ me: level[k] >= i && victim[i] == me) {};
  }
}

unlock(me) {
  level[me] = 0;
}
```


### Bakery Lock (two processes, simplified)
Ticket-based, fair. Take a number one higher than the other; enter when your number is lowest.

```text
volatile int np = 0, nq = 0

// Process P                     // Process Q
loop                             loop
  non-critical section             non-critical section
  np = nq + 1                       nq = np + 1
  while (nq != 0 && nq < np);       while (np != 0 && np <= nq)
  critical section                  critical section
  np = 0                            nq = 0
```

### Bakery Lock (n processes)
General ticket algorithm. Ties in `label` are broken by thread id via lexicographic order `(k, label[k]) < (me, label[me])`.

```text
integer array[0..n-1] label = [0, ..., 0]
boolean array[0..n-1] flag  = [false, ..., false]

lock(me):
  flag[me]  = true;
  label[me] = max(label[0], ..., label[n-1]) + 1;
  while (∃k ≠ me: flag[k] && (k, label[k]) < (me, label[me])) {};

unlock(me):
  flag[me] = false;

// (k, l_k) < (j, l_j)  ⇔  l_k < l_j  or  (l_k == l_j and k < j)
```


---

## 04 Hardware Locks

### TAS primitive 
if the location is 0, set it to 1 and return true; otherwise return false.

```text
boolean TAS(memref s) {
    if (mem[s] == 0) {
        mem[s] = 1;
        return true;
    }
    return false;
}
```

### CAS primitive
if equal, write `new`. Returns the old value (Java's `compareAndSet` instead returns a boolean success flag).

```text
int CAS(memref a, int expected, int new) {
    oldValue = mem[a];
    if (oldValue == expected) {
        mem[a] = new;
    }
    return oldValue;
}
```

### TAS Lock (Test-and-Set)
Simplest spin lock: keep doing `getAndSet(true)` until it returns `false` (you flipped it from free to taken). Needs one memory location. Downside: every thread hammers the same location with atomic writes.

```java
class TASLock {
    AtomicBoolean state = new AtomicBoolean(false);

    public void lock() {
        while (state.getAndSet(true)) {}   // spin until we flip false -> true
    }

    public void unlock() {
        state.set(false);
    }
}
```

### TATAS Lock (Test-and-Test-and-Set)
Reduces bus traffic: first spin on a cheap read (`get()`); only attempt the expensive atomic `getAndSet` when the lock looks free.

```java
class TATASLock {
    AtomicBoolean state = new AtomicBoolean(false);

    public void lock() {
        while (true) {
            while (state.get()) {};          // test: spin on cheap read only
            if (!state.getAndSet(true))      // tas only when it looks free
                return;
        }
    }

    public void unlock() {
        state.set(false);
    }
}
```

### CAS Lock (spinlock)
Spin on `compareAndSet(false, true)`: only the thread that flips it from free to taken enters. Equivalent guarantees to the TAS lock (deadlock-free, but neither fair nor starvation-free).

```java
AtomicBoolean inCS = new AtomicBoolean(false);

public void lock() {
    while (!inCS.compareAndSet(false, true));
}

public void unlock() {
    inCS.set(false);
}
```

### Lock with Backoff (TTAS + exponential backoff)
Spin reading the flag cheaply (TTAS); only attempt the atomic `getAndSet` when it looks free; on failure back off for a growing random delay.

```java
public void lock() {
    Backoff backoff = null;
    while (true) {
        while (state.get()) {};              // spin reading only (TTAS)
        if (!state.getAndSet(true))          // try to acquire, returns previous value
            return;
        else {                               // backoff on failure
            try {
                if (backoff == null)         // allocate only on demand
                    backoff = new Backoff(MIN_DELAY, MAX_DELAY);
                backoff.backoff();
            } catch (InterruptedException ex) {}
        }
    }
}
```

---

## 05 Deadlocks

### Bank transfer — global ordering of locks
Avoids deadlock by always acquiring the two account locks in a fixed global order (by account number), so no cycle of waits can form.

```java
class BankAccount {
    ...
    void transferTo(int amount, BankAccount to) {
        if (to.accountNr < this.accountNr)
            synchronized (this) {
                synchronized (to) {
                    withdraw(amount);
                    to.deposit(amount);
                }}
        else
            synchronized (to) {
                synchronized (this) {
                    withdraw(amount);
                    to.deposit(amount);
                }}
    }
}
```

---

## 06 Semaphores

### Semaphore built from a monitor
A counting semaphore implemented with `synchronized` + `wait`/`notify`. `acquire` blocks while the count is 0; `release` increments and wakes a waiter.

```java
public class MySemaphore {
    private int count;

    public MySemaphore(int maxCount) {
        count = maxCount;
    }

    public void acquire() throws InterruptedException {
        synchronized (this) {
            while (count == 0) this.wait();
            count--;
        }
    }

    public void release() {
        synchronized (this) {
            count++;
            this.notify();
        }
    }
}
```

### Rendezvous (two threads meet)
Each thread signals its own arrival then waits for the other; neither proceeds past the rendezvous until both have arrived.

```text
// init:  P_Arrived = 0,  Q_Arrived = 0

// Thread P                 // Thread Q
...                         ...
release(P_Arrived)          release(Q_Arrived)
acquire(Q_Arrived)          acquire(P_Arrived)
...                         ...
```

---

## 07 Barrier

### Barrier with a Monitor — reusable (double-door / draining)
Threads gather; the last one flips `draining` to release everyone, and the barrier resets so it can be reused.

```java
synchronized void await() throws InterruptedException {
    while (draining) {
        wait();
    }
    i++;
    while (i < n && !draining) {
        wait();
    }
    if (i-- == n) {
        draining = true;
        notifyAll();
    }
    if (i == 0) {
        draining = false;
        notifyAll();
    }
}
```

### Barrier with a Monitor — reusable (generation counter)
Reusable barrier that tags each round with a `generation` number so waiters from one round are not woken by the next.

```java
public class Barrier {
    final int threads;
    private int count = 0;
    private int generation = 0;

    public Barrier(int threads) {
        this.threads = threads;
    }

    public synchronized void await() throws InterruptedException {
        int myGeneration = generation;
        count++;
        if (count == threads) {
            count = 0;
            generation++;
            notifyAll();
        } else {
            while (myGeneration == generation) {
                wait();
            }
        }
    }
}
```

### (!!) Two-Phase Barrier with Semaphores (pseudocode)
Two turnstiles guarantee reusability: phase 1 waits for all to arrive, phase 2 waits for all to leave, so a fast thread cannot lap a slow one.

```text
init:  mutex=1; barrier1=0; barrier2=1; count=0

barrier:
  acquire(mutex)
    count++;
    if (count == n) {
        acquire(barrier2); release(barrier1)}
  release(mutex)

  acquire(barrier1); release(barrier1);
  // barrier1 = 1 for all processes, barrier2 = 0 for all processes

  acquire(mutex)
    count--;
    if (count == 0) {
        acquire(barrier1); release(barrier2) }
  release(mutex)

  acquire(barrier2); release(barrier2)
  // barrier1 = 0 for all processes, barrier2 = 1 for all processes
```

### (!!) Two-Phase Barrier with Semaphores (Java)

```java
import java.util.concurrent.Semaphore;

public class MyBarrier {
    private final int n;
    private int count = 0;

    private final Semaphore mutex    = new Semaphore(1);
    private final Semaphore barrier1 = new Semaphore(0);
    private final Semaphore barrier2 = new Semaphore(1);

    public MyBarrier(int n) { this.n = n; }

    public void await() throws InterruptedException {
        // Phase 1: wait until all threads arrive
        mutex.acquire();
        count++;
        if (count == n) {
            barrier2.acquire();   // close second turnstile
            barrier1.release();   // open first turnstile
        }
        mutex.release();

        barrier1.acquire();
        barrier1.release();

        // Phase 2: wait until all threads leave phase 1
        mutex.acquire();
        count--;
        if (count == 0) {
            barrier1.acquire();   // close first turnstile
            barrier2.release();   // open second turnstile
        }
        mutex.release();

        barrier2.acquire();
        barrier2.release();
    }
}
```

---

## (!!) 08 Producer / Consumer

### Circular buffer — full / empty tests
With one slot deliberately left unused, empty vs full can be told apart from the `in`/`out` pointers alone — no counter needed.

```java
public boolean isFull() {
    return (in + 1) % size == out;
}

public boolean isEmpty() {
    return in == out;
}
```

### Producer/Consumer queue with Semaphores — fields
`nonEmpty`/`nonFull` are counting semaphores tracking used/free slots; `manipulation` is a binary semaphore protecting the shared buffer.

```java
import java.util.concurrent.Semaphore;

class Queue {
    int in, out, size;
    long buf[];
    Semaphore nonEmpty, nonFull, manipulation;

    Queue(int s) {
        size = s;
        buf = new long[size];
        in = out = 0;
        nonEmpty     = new Semaphore(0);     // use the counting feature
        nonFull      = new Semaphore(size);  // use the counting feature
        manipulation = new Semaphore(1);     // binary semaphore
    }
}
```

### Producer/Consumer with Semaphores — enqueue / dequeue
Acquire the resource semaphore, then the mutex, mutate the buffer in `try`, and release in `finally` (mutex first, then the opposite counting semaphore).

```java
void enqueue(long x) {
    try {
        nonFull.acquire();
        manipulation.acquire();
        buf[in] = x;
        in = next(in);
    } catch (InterruptedException ex) {}
    finally {
        manipulation.release();
        nonEmpty.release();
    }
}

long dequeue() {
    long x = 0;
    try {
        nonEmpty.acquire();
        manipulation.acquire();
        x = buf[out];
        out = next(out);
    } catch (InterruptedException ex) {}
    finally {
        manipulation.release();
        nonFull.release();
    }
    return x;
}
```

### Producer/Consumer with a Lock (explicit conditions)
One `lock` plus two `Condition`s: producers `await` on `notFull`, consumers on `notEmpty`; each signals the other after mutating.

```java
void enqueue(long x) {
    lock.lock();
    while (isFull())
        try { notFull.await(); }
        catch (InterruptedException e) {}
    doEnqueue(x);
    notEmpty.signal();
    lock.unlock();
}

long dequeue() {
    long x;
    lock.lock();
    while (isEmpty())
        try { notEmpty.await(); }
        catch (InterruptedException e) {}
    x = doDequeue();
    notFull.signal();
    lock.unlock();
    return x;
}
```

### Producer/Consumer with a Monitor (intrinsic lock)
Same logic using `synchronized` methods and `wait`/`notifyAll` on the object's built-in monitor. `while` (not `if`) re-checks after waking; `notifyAll` (not `notify`) avoids waking the wrong kind of thread.

```java
class Queue {
    int in, out, size;
    long buf[];

    Queue(int s) {
        size = s;
        buf = new long[size];
        in = out = 0;
    }
}

synchronized void enqueue(long x) {
    while (isFull())
        try { wait(); }
        catch (InterruptedException e) {}
    doEnqueue(x);
    notifyAll();
}

synchronized long dequeue() {
    long x;
    while (isEmpty())
        try { wait(); }
        catch (InterruptedException e) {}
    x = doDequeue();
    notifyAll();
    return x;
}
```

### Producer/Consumer — Sleeping Barber
Counters `m` (clients) and `n` (barbers) avoid signalling when nobody waits. `m<0` ⇒ `-m` clients waiting; `n<0` ⇒ `-n` barbers waiting. Only signal when a counterpart is actually blocked.

```java
void enqueue(long x) {              long dequeue() {
    lock.lock();                        long x;
    m--; 
	if (m < 0)                          lock.lock();
        while (isFull())                n--; 
                                        if (n < 0)
            try { notFull.await(); }        while (isEmpty())
            catch (...) {}                      try { notEmpty.await(); }
    doEnqueue(x);                               catch (...) {}
    n++;                                x = doDequeue();
    if (n <= 0) notEmpty.signal();      m++;
    lock.unlock();                      if (m <= 0) notFull.signal();
}                                       lock.unlock();
                                        return x;
                                    }
```

---

## 09 Monitors

### Condition interface — creating conditions on a manual Lock
With a `ReentrantLock` you create named condition groups; it is still one lock but with separate wait sets. `wait/notify/notifyAll` become `await/signal/signalAll`.

```java
final Lock lock = new ReentrantLock();
Condition notFull = lock.newCondition();
// use with: lock.lock(); try { ... } finally { lock.unlock(); }
// notFull.await();  notFull.signal();  notFull.signalAll();
```


---

## (!!) 10 Reader/Writer Locks

### Fair(er) Reader/Writer Lock
Separates read-locking from write-locking with the invariant `writers * readers == 0`. Fairness: when a writer finishes it sets `writersWait = readersWaiting`, letting exactly the currently-waiting readers through before writers are blocked again — so writers can't be starved by a stream of new readers.

Counters: `writers` = # writers in CS; `readers` = # readers in CS; `writersWaiting` = # writers trying to enter; `readersWaiting` = # readers trying to enter; `writersWait` = # readers the writers still have to wait for.

```java
class RWLock {
    int writers = 0;        int readers = 0;
    int writersWaiting = 0; int readersWaiting = 0;
    int writersWait = 0;

    synchronized void acquire_read() {
        readersWaiting++;
        while (writers > 0 ||
               (writersWaiting > 0 && writersWait <= 0))   // writers waiting & readers lost priority
            try { wait(); }
            catch (InterruptedException e) {}
        readersWaiting--;
        writersWait--;
        readers++;
    }

    synchronized void release_read() {
        readers--;
        notifyAll();
    }

    synchronized void acquire_write() {
        writersWaiting++;
        while (writers > 0 || readers > 0 || writersWait > 0)  // wait for waiting readers to finish
            try { wait(); }
            catch (InterruptedException e) {}
        writersWaiting--;
        writers++;
    }

    synchronized void release_write() {
        writers--;
        writersWait = readersWaiting;   // let currently-waiting readers pass
        notifyAll();
    }
}
```

---

## (!!) 11 Lock Granularity

### Fine-grained: Hand-over-hand (lock coupling) — remove
Each node has its own lock. Traverse holding two locks at a time (`pred` and `curr`): lock the next node **before** releasing the previous one, so no thread can overtake you. Sentinels at front and end avoid null checks.

```java
public boolean remove(T item) {
    Node pred = null, curr = null;
    int key = item.hashCode();
    head.lock();
    try {
        pred = head;
        curr = pred.next;
        curr.lock();
        try {
            while (curr.key < key) {
                pred.unlock();
                pred = curr;            // pred still locked
                curr = curr.next;
                curr.lock();            // lock hand over hand
            }
            if (curr.key == key) {
                pred.next = curr.next;  // delete
                return true;
            }
            return false;
        } finally { curr.unlock(); }
    } finally { pred.unlock(); }
}
```

### Fine-grained: Hand-over-hand — add / remove / contains (compact)
All three methods use the same two-lock traversal.

```java
public boolean add(T item) {
    int key = item.hashCode();
    head.lock();
    Node pred = head;
    Node curr = pred.next;
    curr.lock();
    try {
        while (curr.key < key) {
            pred.unlock();
            pred = curr;
            curr = curr.next;
            curr.lock();
        }
        if (curr.key == key) {
            return false;
        }
        Node newNode = new Node(item);
        newNode.next = curr;
        pred.next = newNode;
        return true;
    } finally {
        curr.unlock(); pred.unlock();
    }
}

public boolean remove(T item) {
    Node pred = null, curr = null;
    int key = item.hashCode();
    head.lock();
    try {
        pred = head;
        curr = pred.next;
        curr.lock();
        try {
            while (curr.key < key) {
                pred.unlock();
                pred = curr;
                curr = curr.next;
                curr.lock();
            }
            if (curr.key == key) {
                pred.next = curr.next;
                return true;
            }
            return false;
        } finally { curr.unlock(); }
    } finally { pred.unlock(); }
}

public boolean contains(T item) {
    Node pred = null, curr = null;
    int key = item.hashCode();
    head.lock();
    try {
        pred = head;
        curr = pred.next;
        curr.lock();
        try {
            while (curr.key < key) {
                pred.unlock();
                pred = curr;
                curr = curr.next;
                curr.lock();
            }
            return (curr.key == key);
        } finally { curr.unlock(); }
    } finally { pred.unlock(); }
}
```

### Optimistic synchronization — add / remove / contains
Traverse **without** locks; then lock `pred` and `curr`; then `validate` that nothing changed in between; retry the whole thing on validation failure. `contains` needs only `pred.lock()`.

```java
@Override
public boolean add(T item) {
    int key = item.hashCode();
    while (true) {
        Node pred = this.head;
        Node curr = pred.next;
        while (curr.key < key) { pred = curr; curr = curr.next; }
        pred.lock();
        curr.lock();
        try {
            if (validate(pred, curr)) {
                if (curr.key == key) {          // present
                    return false;
                } else {                        // not present
                    Node entry = new Node(item);
                    entry.next = curr;
                    pred.next = entry;
                    return true;
                }
            }
        } finally {
            pred.unlock(); curr.unlock();
        }
    }
}

@Override
public boolean remove(T item) {
    int key = item.hashCode();
    while (true) {
        Node pred = this.head;
        Node curr = pred.next;
        while (curr.key < key) { pred = curr; curr = curr.next; }
        pred.lock();
        curr.lock();
        try {
            if (validate(pred, curr)) {
                if (curr.key == key) {
                    pred.next = curr.next;
                    return true;
                } else {
                    return false;
                }
            }
        } finally {
            pred.unlock(); curr.unlock();
        }
    }
}

@Override
public boolean contains(T item) {
    int key = item.hashCode();
    while (true) {
        Node pred = this.head;
        Node curr = pred.next;
        while (curr.key < key) { pred = curr; curr = curr.next; }
        try {
            pred.lock();
            // curr.lock();   // not needed for contains
            if (validate(pred, curr)) {
                return (curr.key == key);
            }
        } finally {
            pred.unlock();
            // curr.unlock();
        }
    }
}
```

### Optimistic — validate()
After locking, re-scan from `head` to confirm `pred` is still reachable and still points to `curr` (nothing changed between the lock-free read and acquiring the locks).

```java
private boolean validate(Node pred, Node curr) {
    Node entry = head;
    while (entry.key <= pred.key) {     // reachable?
        if (entry == pred)
            return pred.next == curr;   // connected?
        entry = entry.next;
    }
    return false;
}
```

### Lazy synchronization — add / remove / contains / validate
Improvement over optimistic: each node has a `marked` bit. Deletion is split into **logical** (set `marked = true`) and **physical** (unlink). Every method traverses the list **once without locks**; `validate` no longer rescans from head — it just checks the marks and the link. `contains` is fully wait-free (no locks at all).

```java
public boolean add(T item) {
    int key = item.hashCode();
    while (true) {
        Node pred = head;
        Node curr = head.next;
        while (curr.key < key) {           // find nodes WITHOUT locking
            pred = curr; curr = curr.next;
        }
        pred.lock();
        try {
            curr.lock();
            try {
                if (validate(pred, curr)) {
                    if (curr.key == key) {     // already exists
                        return false;
                    } else {
                        Node node = new Node(item);
                        node.next = curr;
                        pred.next = node;
                        return true;
                    }
                }
            } finally { curr.unlock(); }
        } finally { pred.unlock(); }
    }
}

public boolean remove(T item) {
    int key = item.hashCode();
    while (true) {
        Node pred = head;
        Node curr = head.next;
        while (curr.key < key) {           // find nodes WITHOUT locking
            pred = curr; curr = curr.next;
        }
        pred.lock();
        try {
            curr.lock();
            try {
                if (validate(pred, curr)) {
                    if (curr.key != key) {
                        return false;
                    } else {
                        curr.marked = true;      // LOGICAL remove
                        pred.next = curr.next;   // PHYSICAL remove
                        return true;
                    }
                }
            } finally { curr.unlock(); }
        } finally { pred.unlock(); }
    }
}

public boolean contains(T item) {
    int key = item.hashCode();
    Node curr = head;
    while (curr.key < key)                 // search WITHOUT locking
        curr = curr.next;
    return curr.key == key && !curr.marked;  // check WITHOUT locking
}

// marked == true  -> node has been logically removed
// marked == false -> node is still in the list
private boolean validate(Node pred, Node curr) {
    return !pred.marked && !curr.marked && pred.next == curr;
}
```

---

## 12 Lock Free

### CAS retry pattern
The core lock-free loop: read shared into a local, prepare the change, commit with `compareAndSet`; if someone interleaved, the CAS fails and you retry.

```java
do {
    head = top.get();        // 1. read shared variable locally
    newi.next = head;        // 2. prepare the change
} while (!top.compareAndSet(head, newi));  // 3. nobody in between? -> done
```

### Lock-free Stack
`push`/`pop` both CAS the `top` reference. `pop` reads head + next then swings `top`; `push` links the new node then swings `top`.

```java
public class ConcurrentStack {
    AtomicReference<Node> top = new AtomicReference<Node>();

    public void push(Long item) {
        Node newi = new Node(item);
        Node head;
        do {
            head = top.get();
            newi.next = head;
        } while (!top.compareAndSet(head, newi));
    }

    public Long pop() {
        Node head, next;
        do {
            head = top.get();
            if (head == null) return null;
            next = head.next;
        } while (!top.compareAndSet(head, next));
        return head.item;
    }
}
```

### Lock-free linked list — find (window)
Traverses looking for `key`, and along the way physically unlinks any nodes whose mark bit is set (using `compareAndSet` on pointer+mark); restarts from head if a deletion CAS fails.

```java
public Window find(Node head, int key) {
    Node pred = null, curr = null, succ = null;
    boolean[] marked = {false}; boolean snip;
    while (true) {
        pred = head;
        curr = pred.next.getReference();
        boolean done = false;
        while (!done) {
            marked = curr.next.get(marked);          // get bit array
            succ = marked[1:n];                      // pseudo-code: next ptr
            while (marked[0] && !done) {             // marked[0] is the mark bit
                if (pred.next.compareAndSet(curr, succ, false, false)) {
                    curr = succ;
                    marked = curr.next.get(marked);
                    succ = marked[1:n];
                }
                else done = true;
            }
            if (!done && curr.key >= key)
                return new Window(pred, curr);
            pred = curr;
            curr = succ;
        }
    }
}

class Window {
    public Node pred;
    public Node curr;
    Window(Node pred, Node curr) {
        this.pred = pred;
        this.curr = curr;
    }
}
```

### Lock-free linked list — remove
Find the node; logically delete it with `attemptMark` (set mark bit); then try to physically unlink with `compareAndSet` (result ignored — a later `find` cleans up). Retry from the top if marking fails.

```java
public boolean remove(T item) {
    Boolean snip;
    while (true) {
        Window window = find(head, key);
        Node pred = window.pred, curr = window.curr;
        if (curr.key != key) {
            return false;                                  // no such element
        } else {
            Node succ = curr.next.getReference();
            snip = curr.next.attemptMark(succ, true);      // logical delete (mark)
            if (!snip) continue;                           // failed -> restart
            pred.next.compareAndSet(curr, succ, false, false); // physical delete
            return true;
        }
    }
}
```

### Lock-free linked list — add
Find the insertion window; if the key exists return false; otherwise build the node pointing at `curr` and CAS `pred.next` from `curr` to the new node. Retry on failure.

```java
public boolean add(T item) {
    boolean splice;
    while (true) {
        Window window = find(head, key);
        Node pred = window.pred, curr = window.curr;
        if (curr.key == key) {
            return false;                                  // already exists
        } else {
            Node node = new Node(item);
            node.next = new AtomicMarkableRef(curr, false);
            if (pred.next.compareAndSet(curr, node, false, false))
                return true;                               // inserted
        }
    }
}
```

### Lock-free Queue — enqueue
Read `tail` (`last`) and `last.next`. If `next == null`, CAS `last.next` from null to the new node, then try to swing `tail`. If `next != null`, another thread is mid-enqueue, so help by advancing `tail` and retry.

```java
public void enqueue(T item) {
    Node node = new Node(item);
    while (true) {
        Node last = tail.get();
        Node next = last.next.get();
        if (next == null) {
            if (last.next.compareAndSet(null, node)) {
                tail.compareAndSet(last, node);
                return;
            }
        }
        else
            tail.compareAndSet(last, next);   // help other threads make progress
    }
}
```

### Lock-free Queue — dequeue
Read `head`/`tail`/`first.next`. If `first == last` the queue looks empty (return null) or `tail` is lagging (advance it). Otherwise read the value and CAS `head` forward.

```java
public T dequeue() {
    while (true) {
        Node first = head.get();
        Node last  = tail.get();
        Node next  = first.next.get();
        if (first == last) {
            if (next == null) return null;            // really empty
            else tail.compareAndSet(last, next);      // advance lagging tail
        }
        else {
            T value = next.item;
            if (head.compareAndSet(first, next))
                return value;
        }
    }
}
```

---

## 14 Consensus

### Binary ⇄ general consensus (equivalence)
Shows each can be built from the other using a boolean↔int conversion, so binary consensus is as powerful as general consensus.

```java
// general consensus  ->  binary consensus
boolean binary_decide(boolean b) {
    return int_decide(b ? 1 : 0) == 1;
}

// binary consensus  ->  general consensus
int int_decide(int d) {
    values[id] = d;
    int index = binary_decide(id == 1) ? 1 : 0;
    return values[index];
}
```

### 2-thread consensus with Test-and-Set
Announce your value, then race via TAS: the winner (`TAS()==0`) returns its own value; the loser reads the winner's announced value. Consensus number of TAS is 2.

```java
// Step 1: announce own value to shared memory immediately
proposed[thread_id] = own_value;

// Step 2: attempt to win the consensus race
if (TAS() == 0) {
    return own_value;                      // I won
} else {
    int other_thread_id = 1 - thread_id;   // I lost -> read winner's value
    return proposed[other_thread_id];
}
```

### n-thread consensus with Compare-and-Swap
A single `AtomicReference`: the first thread's `compareAndSet(null, proposal)` succeeds and fixes the decision; everyone returns `decision.get()`. CAS has consensus number n.

```java
public class NThreadConsensus<T> {
    private final AtomicReference<T> decision = new AtomicReference<>(null);

    public T decide(T proposal) {
        decision.compareAndSet(null, proposal);   // only the first thread sets it
        return decision.get();                     // all return the first value
    }
}
```

### Consensus with a Queue (enqueue/dequeue) — consensus number 2
A FIFO pre-filled with `{0, 1}`: announce your value, then dequeue. Whoever dequeues `0` won (was first) and returns its own value; the loser returns the winner's value. Proves a queue has consensus number ≥ 2.

```java
int shared[2];
fifo q = {0, 1};   // initialize the queue with two distinct values

int decide(int proposed, int thread_id) {
    shared[thread_id] = proposed;
    if (q.dequeue() == 0)
        return shared[thread_id];              // I won: first to dequeue
    else
        return shared[(thread_id + 1) % 2];    // I lost: return other's value
}
```

### Consensus with a Queue supporting peek — consensus number ∞
With `peek`, every thread can see who enqueued first; enqueue your id, then return the value of the first enqueuer. A queue with peek solves consensus for any n.

```java
int shared[N];
fifo q = {};   // initialize the queue as empty

int decide(int proposed, int thread_id) {
    shared[thread_id] = proposed;
    q.enqueue(thread_id);
    return shared[q.peek()];   // value of the first enqueuer
}
```

---

## 15 Transactional Memory

### ScalaSTM — creating transactional state
How to declare variables/arrays used inside transactions. Use `Ref`/`TArray` for shared transactional state; plain Java variables are fine if only used *inside* one transaction.

```java
// variable / array used and modified across transactions
Ref.View<Integer> a_stm = STM.newRef(0);       // single ref
TArray.View<Integer> items = STM.newTArray(10);  // transactional array

int a = 0;                   // plain: only used inside one transaction
int[] arr = new int[10];     // plain: not shared across transactions

// declaring a transaction:
STM.atomic(new Runnable() { ... });          // no return value
STM.atomic(new Callable<T>() { ... });       // with return value
```

### ScalaSTM — Account fields
An STM-managed account; `balance` is a transactional reference (`Ref.View`) created with `STM.newRef`.

```java
class AccountSTM {
    private final Integer id;                 // account id
    private final Ref.View<Integer> balance;

    AccountSTM(int id, int balance) {
        this.id      = new Integer(id);
        this.balance = STM.newRef(balance);
    }
}
```

### ScalaSTM — withdraw / deposit (atomic blocks)
Each mutation runs inside `STM.atomic(Runnable)`; read the balance and write the new value; the STM makes it appear atomic and serialized.

```java
void withdraw(final int amount) {
    // assume that there are always sufficient funds...
    STM.atomic(new Runnable() { public void run() {
        int old_val = balance.get();
        balance.set(old_val - amount);
    }});
}

void deposit(final int amount) {
    STM.atomic(new Runnable() { public void run() {
        int old_val = balance.get();
        balance.set(old_val + amount);
    }});
}
```

### ScalaSTM — getBalance (Callable with return value)
When a transaction must return a value, use `Callable<T>` instead of `Runnable`.

```java
public int getBalance() {
    int result = STM.atomic(
        new Callable<Integer>() {
            public Integer call() {
                int result = balance.get();
                return result;
            }
        });
    return result;
}
```

### ScalaSTM — transfer (composed transaction)
Two account operations composed into one atomic block — the thing locks make hard is trivial here.

```java
static void transfer(final AccountSTM a,
                     final AccountSTM b,
                     final int amount) {
    STM.atomic(new Runnable() { public void run() {
        a.withdraw(amount);
        b.deposit(amount);
    }});
}
```

### ScalaSTM — transfer with retry
`STM.retry()` blocks the transaction until a read value changes, then re-runs — no busy spin-wait.

```java
static void transfer_retry(final AccountSTM a,
                           final AccountSTM b,
                           final int amount) {
    atomic {   // for brevity
        if (a.balance.get() < amount) STM.retry();
        a.withdraw(amount);
        b.deposit(amount);
    }
}
```

### Transactional Memory — general pattern

```text
atomic {
    if (condition) STM.retry();
    do something
}
```

### ScalaSTM — CircularBuffer (bounded queue)
A full producer/consumer buffer in STM: `count`/`tail` are `Ref`s, `items` is a `TArray`. `enq` calls `STM.retry()` when full (blocks until state changes, no spin), then updates the array and increments the count — all atomically.

```java
public class CircularBufferSTM<T> {
    private final Ref.View<Integer> count = STM.newRef(0);
    private final Ref.View<Integer> tail  = STM.newRef(0);
    private TArray.View<T> items;

    public CircularBufferSTM(int capacity) {
        items = STM.newTArray(capacity);
    }

    public void enq(final T x) {
        STM.atomic(new Runnable() {
            public void run() {
                if (count.get() == items.length()) {
                    STM.retry();                       // full: wait for change
                }
                items.update(tail.get(), x);
                tail.set((tail.get() + 1) % items.length());
                STM.increment(count, 1);
            }
        });
    }
}
```

---

## 15 Message Passing / MPI

### MPI — SPMD skeleton
Single Program Multiple Data: all processes run the same code and branch on their `rank`.

```java
if (rank == 0) {
    // (Master process) distribute the work
} else {
    // Worker process: compute
}
```

### MPI — Send signature
Sends `count` elements from `buf` (starting at `offset`) to process `dest`, tagged with `tag`. `Recv` is the mirror image with `src` instead of `dest`.

```java
void Comm.Send(
    Object buf,        // the data array to be sent
    int offset,        // start index of relevant data
    int count,         // number of elements relevant
    Datatype datatype, // type of data
    int dest,          // rank (id) of destination process
    int tag            // id for this message
)
```

### MPI — Recv signature
Mirror of `Send` with `source` instead of `dest`. The receiver can accept a message without knowing the exact sender/tag by passing `MPI_ANY_SOURCE` / `MPI_ANY_TAG`.

```java
void Comm.Recv(
    Object buf,        // buffer to receive into
    int offset,        // start index in the buffer
    int count,         // number of elements
    Datatype datatype, // type of data
    int source,        // rank of source process, or MPI_ANY_SOURCE
    int tag            // message id, or MPI_ANY_TAG
)
```

### MPI — avoiding send/receive deadlock
Three fixes for the classic `Send;Recv` deadlock (unsafe because it relies on system buffering).

```text
// Fix 1: order operations carefully
Process 0        Process 1
Send(1)          Recv(0)
Recv(1)          Send(0)

// Fix 2: combined send+receive
Process 0        Process 1
Sendrecv(1)      Sendrecv(0)

// Fix 3: non-blocking operations
Process 0        Process 1
Isend(1)         Isend(0)
Irecv(1)         Irecv(0)
Waitall          Waitall
```

### MPI — common functions
`MPI_INIT` (first call), `MPI_COMM_SIZE`, `MPI_COMM_RANK`, `MPI_SEND`, `MPI_RECV`, `MPI_FINALIZE` (last call).


- **`Bcast` (Broadcast):** Sends a copy of the same data from one root process to all other processes in the communicator.
- **`Scatter`:** Divides a data array on a root process and sends a distinct, equal-sized chunk to each process.
- **`Gather`:** Collects distinct chunks of data from all processes and concatenates them into a single array on a root process.
- **`Reduce`:** Combines values provided by all processes using a specified mathematical operation (like sum, max, min) and stores the final result on a single root process.
- **`Allreduce`:** Identical to `Reduce`, but distributes the final computed result back to all processes so everyone has the answer.
- **`Barrier`:** A synchronization mechanism that forces all processes to pause; no process can execute past the barrier until every process has reached it.