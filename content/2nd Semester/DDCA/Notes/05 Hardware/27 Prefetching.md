
Memory latency is high. We reduce it using prefetching. We want to predict which address will be needed in the future and fetch before needed. 

Works if programs have predictable miss address patterns. We want to reduce both miss rate and miss latency. 

A misprediction in prefetching does not affect correctness. So no need for state recovery. 

Prefetching is usually done at the cache block granularity. 

Can be done with Software or Hardware

Performance Metrics: Accuracy, Coverage, Timeliness, Bandwidth consumption, don't want to pollute Cache

## Stride Prefetcher

Record stride between consecutive memory access, if stable use it to predict next memory accesses. 

Useful when pattern is simple.

---

Real systems use hybrid prefetchers (a combination of multiple). This makes it more complex and bandwidth intensive, etc. but better coverage and timeliness.

---

## Execution Based Prefetchers

Pre-execute a piece of the program just to prefetch data
Thread-Based Pre-Exeuction (spin up separate side-threads)

---

## Runahead Execution

Problem: out of order execution requires large instruction windows to tolerate memory latencies. As memory latency increases, instruction window size should also increase. Building large instruction window is challenging (expensive, power, cycle time, etc.)

Runahead Execution: memory-level parallelism benefits of a large instruction window. 

When we have a miss, instead of stalling, we use that time to enter runahead mode and speculatively pre-execute isntructions (prefetches) such that we then in a later miss don't need to stall again. When we exit runahead mode we restore the processor to the state of before. These prefetches are accurate because we are executing the actual program.

![[Bildschirmfoto 2026-05-30 um 17.58.31.png]]

Advantages: 
- accurate
- simple
- no waste of hardware 
- no need for special thread for prefetching

Disadvantages: 
- extra executed instructions
- cannot prefetch dependent cache misses
- limited by MLP (memory level parallelism)
- prefetch distance limited by memory latency