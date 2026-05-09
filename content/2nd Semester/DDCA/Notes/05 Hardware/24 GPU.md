
## Overview

- Instruction pipeline is like a [[23 SIMD|SIMD]] pipeline
- Programming is done using threads, not SIMD instructions

---

## Programming Model vs. Execution Model

- **Programming model:** Sequential (von Neumann), Data Parallel (SIMD), Dataflow, Multi-threaded, …
- **Execution model (hardware):** out-of-order, vector-processor, array processor, dataflow processor, multiprocessor, …

> [!important]
> The execution model can be different from the programming model.

---

## Key Paradigms

- **SPMD** (Single Program Multiple Data) — e.g. adding two arrays `C = A + B` on a MIMD machine with 1 thread per entry
- **SIMT** (Single Instruction Multiple Threads) — multiple instruction streams of scalar instructions; each thread is independent → behaves like MIMD

---

## GPU Architecture: SIMD Hardware, Thread Programming

> [!note]
> A GPU is a **SIMD machine** under the hood, but it is **programmed with threads**.

- Each thread has its own context and executes the same code on a different piece of data
- The hardware groups threads executing the same instruction into a **warp** → a warp is essentially a SIMD operation formed by hardware

### Warp

- Set of threads with the same instruction on different data elements
- **Not exposed to programmers** — handled entirely by hardware

### Fine-Grained Multi-Threading (FGMT)

- One instruction per thread in the pipeline at a time
- Warp execution is interleaved to hide latencies
- Enables a simple pipeline with long latency tolerance
