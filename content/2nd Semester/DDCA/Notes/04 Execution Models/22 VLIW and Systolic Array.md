
## VLIW

Very long instruction word

[[19 Superscalar Execution|Superscalar]]: Hardware fetches instructions and checks dependencies

**VLIW**: Software bundles independent instructions to be fetched and executed concurrently in a single VLIW instruction. Hardware no need for dependence checking. 

Simpler hardware (no scheduling or dependency check needed), but compiler more complex with possible NOPs.

If any operation in a VLIW instruction stalls, all concurrent operations stall. 

### Superblocks

single entry, multiple exit (output)
Superblock Formation: we separate the common path from the rarely used path by duplicating the lower nodes after the rarely used point

![[Bildschirmfoto 2026-05-03 um 19.47.34.png]]

## Systolic Array 

- execution model different from [[09 Von Neumann|von neumann]], [[21 Dataflow|dataflow]]
- separate task to many PE (processing elements). A piece of data that is taken from memory is done some processing with by PE1, then passed on to PE2 for further processing, and so on. But by the time that this data reaches PE2, PE1 can already start fetching and processing the next memory element, finally, it is stored back to memory. In [[15 Pipelining|pipelining]] we pipeline instructions, here we are working with individual PEs. 

- The PEs and this pipeline can be specialized
- but then they aren't generally applicable for all computations

![[Bildschirmfoto 2026-05-03 um 20.40.22.png]]
- 