
Imaging 2 Threads propose 2 differnet numbers through a finite number of steps (wait free, independent), and they agree on a number and return.

1. **Valid** (the agreed number needs to be computed by either)
2. **Consistent** (both threads agree on same value)
3. **Wait-free** (one thread can return even though other thread kills, finite number of steps, no no wait loop on other thread)

We implement by agreeing on first value (value of faster Thread).
### Consensus Hierarchy

|                                 | **Consensus number** <br>(how many threaded sonsensus can we create) |
| ------------------------------- | -------------------------------------------------------------------- |
| **Atomic** read/write registers | 1                                                                    |
| **Test and Set**                | 2                                                                    |
| **Compare and Set**             | n (beliebig)                                                         |


---

## Binary Consensus

a binary consensus is the equivalent to a normal consensus. 

In the proof we use the ternary operator to convert a boolean to `1`and `0`, and vice versa.

**Proof:**

We can create a binary consensus when we have a normal consensus: 

```java
boolean binary_decide(boolean b) {
    return int_decide(b ? 1 : 0) == 1;
}
```

We can create a normal consensus when we have a binary consensus: 
```java
int int_decide(int d) {
    values[id] = d; 
    int index = binary_decide(id == 1) ? 1 : 0;
    return values[index];
}
```

---

## Consensus in the State Space Diagram

*binary tree*

- 2 children because 2 Threads
- no loop (because needs to be wait-free)
- each state contains: shared variables, local variables and program counter (the state contains both of A and B threads but Thread B doesn't see local variables and program counter of A), so from the perspective from one Thread the states look the same unless shared variables change

Begriffe

- **bivalent**: not yet decided if 0 or 1, both outcomes possible, start state is bivalent
- **univalent**: both children have same value, threads agreed already
- **critical**: diese Stelle ist gerade bivalent, aber entscheided was output ist, also ichkann nicht tiefer gehen und es ist immer noch nicht entschieden, bivalent with 2 univalent children

**Lemma**: Every consensus protocol has a critical state. *Proof*: In our State Space diagram we can only move down (no loop because wait-free), so at some point we reach an univalent state. 

---
## Java Implementation

### 2 Threaded

We use TAS, because this is not possible with volatile variables (see table above or proof below).

```java
// Step 1: Announce own value to shared memory immediately
proposed[thread_id] = own_value;

// Step 2: Attempt to win the consensus race
if (TAS() == 0) {
    // I won. The decision is my value.
    return own_value;
} else {
    // I lost. The other thread won, so its value is the decision.
    // Read from shared memory AFTER losing.
    int other_thread_id = 1 - thread_id;
    return proposed[other_thread_id];
}
```

### n-Threaded

We use CAS, not possible with TAS (see table above)

```java
// single reference to one object
public class NThreadConsensus<T> {
    private final AtomicReference<T> decision = new AtomicReference<>(null);
    
	// every thread brings his proposal
    public T decide(T proposal) {
		// only for the first thread is decision empty, so he puts his proposal in. all others don't
        decision.compareAndSet(null, proposal);
        // we return the first threads' value
        return decision.get();
    }
}
```


---

## Proof: We cannot do wait-free Consensus with only atomic registers 

**Proof** 
We cover all options. 

Assume we are at a cricital state (there always is a critical state). Now, either Thread A or B needs to do something first. Wlog. we reduce to the following options for the next steps.

First action: 
- A: `r1.read()`
- A: `r1.write()

Second action: 
- B: `r1.read()`
- B: `r2.read()`
- B: `r1.write()`
- B: `r2.write()`

> If B is first, output 1, if A is first, output 0.

**Case** first action is A: `r1.read()`: 
- Thread A takes the first step, so our output needs to be 0. A pulls data to own private memory, but doesn't change shared memory. 
- Suppose, Thread A is now paused, Thread B continues itself (B can't wait for A because wait-free, so B must decide on its own). 
- But for Thread B the current situation (A read, now B's turn) is identical to as if B executed directly from the critical state, so it wouldn't know that it would need to output A's preference; Thread B would have to output 2 different values on the 2 branches. So now we have both A and B branches identical, thus the top node isn't critical $\implies$ contradiction.
- ![[Bildschirmfoto 2026-05-20 um 20.01.52.png|280]]

**Case** first action is A: `r1.write()`and second action is B `read()`
- Same situation as above. 

**Case** A and B write to different registers
- Path left from critical node: 
	- Thread A does `r1.write()`, so output must be 0
	- Thread B does `r2.write()`
- Path right from critical node: 
	- Thread B does `r2.write()`, output must be 1
	- Thread A does `r1.write()`
- both paths lead to the same state, the registers have the same values, so no critical node

**Case** first action A: `r1.write()`, B: `r1.write()`
- Same as Case 1, 2

---

