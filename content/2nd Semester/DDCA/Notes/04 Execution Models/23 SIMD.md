single instruction multiple data

[[21 Dataflow|Dataflow]]: concurrency because different operations in parallel
SIMD: concurrency because same operation concurrently applied to different pieces of data (f.ex. dot product of vectors)

## Vector processor

SIMD/Vector machines do performance improvement by vectorizability. Check [[07 Scalability#Amdahl's Law|Amdahl's Law]] 

A vector processor is one whose instructions operate on vectors rather than scalar (single data) values

Advantages: 
- no dependencies within a vector
- regular memory access pattern
- high workload per instruction

Disadvantages: 
- parallelism needs to be regular to function properly
- memory becomes a bottleneck

### Memory banking

Problem: Memory speed can't keep up with CPU
Solution: Memory banking

- divide Memory into independent banks (they share address and data bus)
- each bank has its own MAR (memory address register) and MDR (memory data register)
- result: we can fetch from memory in parallel (N concurrent accesses if they go to N different banks)

The CPU gives the memory the base (starting address in memory) and a stride (distance between the elements to be fetched). So `Next address = Previous address + Stride`

For maximum throughput (1 element per cycle) we need
- stride = 1
- consecutive elements on different banks
- number of banks >= bank latency

Loop vectorizable if iterations independent from one another

## Masked Instructions

At times we only want to compute part of the vector. The mask tells us which part. 

Simple Implementation: execute everything, but don't write back where mask = 0

Advanced Implementation: check mask and only calculate where needed

## Stride number

As mentioned, stride = 1 is optimal, as guaranteed that each bank will be used. At times though, we have operations with stride > 1. 

Then, stride coprime to bank amount means every bank will be hit before looping back to the beginning. 

Memory interleaving uses mod to assign addresses to banks. 

So with 16 memory banks 
- stide=3: banks 0, 3, 6, 9, 12, 15, 2, 5, 8, 11, 14, 1, 4, 7, 10, 13
- stride=4: banks 0, 4, 8, 12

Remember $\mathbb{Z}_7^*=\{1,2,3,4,5,6\}$ 

Avoiding bank conflicts: 
- more banks
- more ports per bank
- better data layout