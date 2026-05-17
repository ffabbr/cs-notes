Single Instruction Multiple Data — same operation applied concurrently to different pieces of data (e.g. dot product of vectors).

Contrast with [[21 Dataflow|Dataflow]]: concurrency comes from different operations running in parallel, whereas SIMD parallelizes the *same* operation across data.

e.g. summing 2 arrays: fully parallelizable, so the programmer or compiler generates a SIMD instruction → forms a vector instruction → executes on a SIMD processor.

---

## Vector Processor

A vector processor is one whose instructions operate on vectors rather than scalar values. Same operation in the same space, different operations at different times.

> [!warning] Performance ceiling
> SIMD/Vector performance improvement is limited by the vectorizability of the code. Check [[07 Scalability#Amdahl's Law|Amdahl's Law]] (!!)

**Advantages:**
- No dependencies within a vector
- Regular memory access pattern
- High workload per instruction

**Disadvantages:**
- Parallelism needs to be regular to function properly
- Memory becomes a bottleneck

A loop is vectorizable if its iterations are independent from one another.

### Memory Banking

**Problem:** Memory speed can't keep up with the CPU.  
**Solution:** Divide memory into independent banks (sharing address and data bus), each with its own [[09 Von Neumann|MAR and MDR]] → enables N concurrent accesses if they go to N different banks.

The CPU provides a **base** (starting address) and a **stride** (distance between elements): `next address = previous address + stride`

For maximum throughput (1 element per cycle):
- stride = 1
- consecutive elements on different banks
- number of banks ≥ bank latency

### Stride & Bank Conflicts

Stride = 1 is optimal. For stride > 1, stride **coprime to the number of banks** ensures every bank is hit before cycling back.

Memory interleaving assigns addresses to banks via modulo. With 16 banks:
- stride = 3 → banks 0, 3, 6, 9, 12, 15, 2, 5, 8, 11, 14, 1, 4, 7, 10, 13
- stride = 4 → banks 0, 4, 8, 12 (conflict!)

> [!tip] Recall $\mathbb{Z}_7^* = \{1,2,3,4,5,6\}$

Avoiding bank conflicts:
- More banks
- More ports per bank
- Better data layout

---

## Masked Instructions

Sometimes only part of a vector needs to be computed — the **mask** specifies which elements.

- **Simple:** execute everything, don't write back where mask = 0
- **Advanced:** check mask first and only compute where needed
