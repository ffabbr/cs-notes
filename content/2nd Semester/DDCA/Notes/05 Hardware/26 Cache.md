
## Caching

Caching is about memoizing used data (which works due to locality). We store data in addresses adjacent to recently accessed one in fast memory. 

**We divide memory into blocks**. The Cache contains *block lines/cache line*, which has place for one memory block.

Off-topic: a **Scratchpad** is like a Cache but managed by the programmer, not the hardware.


> [!success] 
> When CPU requests Data, it first checks Cache:
> - **HIT**: data is in cache
> - **MISS**: data is not in cache, bring block from main storage


### Direct mapping

**Direct-mapped**: a givem memory block can be placed in only one possible location in the cache

The CPU sends data request and we quickly check the Cache. The data request contains

- tag of block
- index of block
- byte within block

Ablauf

1. go to position of index in tag store table
2. check if tag of request $=$ tag in tag store at index
3. yes? get block values from data store
4. use MUX to get requested byte of the found block

**Problem**: if 2 things randomly get the same index, they both use the same cache location and overwrite themselves

![[Bildschirmfoto 2026-05-15 um 15.55.32.png]]

### Solution: Memory arrays with associativity

- Der Index zeigt auf ein Set mit N Zeilen (statt auf eine Zeile direkt)
- CPU schaut, welche der Zeilen in dem gegebenen Set frei ist und nutzt diese Zeile
- erst wenn alle Zeilen in dem Set belegt sind, muss eine Zeile überschrieben werden


![[Bildschirmfoto 2026-05-17 um 10.59.06.png]]

Fully Associative: any block can be in any location as everything is in the same set, no index needed, every block can go anywhere in the cache. Flexible, but expensive

![[Bildschirmfoto 2026-05-30 um 15.25.08.png]]

### Associativity

Degree of associativity: how many blocks can map to the same index/set? 

Higher associativity: higher hit rate, slower cache access time, more expensive hardware

### Issues in Set-Associative Caches

Each block has a priority (how important is it to be in the cache)
In a cache set: Insertion, promotion (priority), eviction (replacement)

### Cache  Replacement Policies

We want to keep the most useful data in the cache. If the cache is full and we have a miss, we need to decide which element to replace in the cache.

**LRU**: remove the least recently used. Requires expensive hardware to keep track of order. LRU has a problem of ==Data Trashing==. 

==Data Trashing==: Problem when data is needed in circular order, meaning we have `[A,B,C]`, need D. A was used the longest ago, so A is replaced, `[D,B,C]`, now suppose we need A, we get `[D,A,C]`, etc. so we have Cache misses all the time. ==Trashing== happens when: "program working set" in a set is larger than set associativity. When trashing occurs, random replacement policy is better than LRU (least recently used), hard to implement ordering. 

**Random**: replace randomly

Average hit rate of LRU and random are similar, hybrid combination smart. 

**Belady's OPT**: replace block that it going to be referenced the last in the future of the program

Lower miss rate does not automatically mean faster because overhead could be bigger f.ex. getting the data. 

## Writes 

Dirty bits = modified, change needs to be carried on 

Write-back cache: combine multiple writes to the same block before eviction, BUT need a bit in tag store indivating that block is dirty

Write through cache: simpler design, all levels are up to date and consistent BUT more bandwidth intensive

Do we allocate a cache block on a write miss? 
If the processor writes to an entire block over a small amount of time?

Subblocked (Sectored Caches): Divide a block into subblocks, allocate only a subblock on a request → no need to transfer the entire cache block into the cache, more freedom in transfering subblocks BUT more complex, spatial locallity not epxloited

Instruction vs Data:
Unified: dynamic sharing of cache space → better cache utilization, but instructions can evict/trash each other

Parallel Access of cache levels: parallel → faster if cache miss, but unnecessary access if cache hits already in prev. level

**Cache hierarchy:** 

- Inclusive: a block in an inner level is included in an outer level (simplifies cache coherence)
- Exclusive: a block in an inner level does not exist in an outer level (uses space in entire hierarchy)
- non-inclusive: a block in an inner level may or may not be included in outer level (relaxed)

**Classification of Cache Misses**
- Compulsory miss: first reference to an address block always misses. reduce by prefetching
- Capacity miss: cache too small to hold all data, keep blocks that will be referenced, software management
- Conflict miss: any other miss, reduce by adding associativity
## Cache Performance

- **Cache Size**: bigger is slower, smaller doesn't use temporal locality well 
- **Associativity**: larger means lower miss rate because reduced conflicts but higher hit latency, smaller means lower cost and lower hit latency

![[Bildschirmfoto 2026-05-30 um 16.19.46.png]]

---
![[Bildschirmfoto 2026-05-30 um 16.20.13.png]]

F.ex. when mulitplying 2 matrices, calculate for a sub-part of the matrix that is small enough to fit into the cache (suppose top left) first, then top right, etc. 


MLP: Memory level parallelism, multiple memory accesses in parallel

![[Bildschirmfoto 2026-05-30 um 16.45.09.png]]


## Cache Coherence

Shared memory. Thread 0 writes, Thread 1 then reads, aka they communicate. Need to ensure Thread 1 gets the new value and not a potentionally cached one. 

Broadcast-Based idea: when a processor writes to a cache block it sends to all other processors to invalidate/update their local copy

Directory-Based idea: central directory keeps track of which caches contain every possible cache block