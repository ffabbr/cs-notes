
Separate Namespace of Physical Memory to avoid different programs overwriting themselves. 

**Virtual Memory**: there is a system that sets the namespace (physical memory location), but the programmer still says f.ex. "position 1" but that's a different position 1 than if another program uses "position 1". The programmer sees virtual memory, the system maps virtual memory addresses to physical memory. 

---

**Physical memory is limited in size. What if we don't have enough?** 

Give the program the illusion of infinite physical memory. The programmer doesn't worry about managing physical memory. Hardware and software automatically manage the physical memory space (indirection and mapping).

When physical address space is full, evoice an unlikely to be needed virtual address from physical memory (keep virtual address the same but move to f.ex. disk)


![[Bildschirmfoto 2026-05-30 um 18.20.28.png]]

---

## Pages and Frames

Virtual address space divided into pages
Physical address space divided into frames

We map virtual page to physical frame

---

Physical memory is a cache for pages stored on disk.

![[Bildschirmfoto 2026-05-30 um 18.21.02.png]]

## Address Translation

The address consists of a **location+offset**. 

> [!warning] Offset
> Don't translate the offset (it doesn't change), just the upper bits (position) from the VPN (in virtual address) to the PPN (in physical address)

![[Bildschirmfoto 2026-05-30 um 18.21.37.png]]

### Page Table

A table that translates the gives us the physical address from the virtual address. 

What is the physical address of virtual address `0x5F20`? The last 12 bits are the offset, so `F20`. So the VPN is `5`, meaning we look at the 5th entry in the Page Table. If valid, we get the PPN (physical page number) here, to which we then append the offset. 

Notice how in the image above the phyical memory is smaller than the virtual, and this works by mapping some things to the hard drive instead ("Swap memory")

---

**Page table like this get's ==too large==.** But this table would get very big (f.ex. 52 Bit VPN, so table needs $2^{52}$ entries $\implies 2^{54}$ bytes = 16.000 Terabyte. ). 

Solution: We use multiple page tables. We use a small extra page table that tells us the address of the right page table. When valid set to 0 we let that page table "free", meaning we free the space and use more efficiently. BUT an n-level page table, needs n page table accesses to find the PTE, so more complex/slower.

The VPN contains 
- page Table number (which page table, aka which row in the page table address table)
- page table offset (what row in the actual page table)
- page offset (offset of the physical array)

2-Level Page table: 

![[Bildschirmfoto 2026-05-31 um 20.08.56.png]]


## Translation Lookaside Buffer (TLB)

a cache for the virtual—physical address translation (cache the page table entries to speed up the address translation)

**Hardware Page Table Walker (PTW)** Triggering an OS software exception for every single TLB miss is too slow. Solution: **PTW**. A dedicated hardware state machine that handles the page walk.

* Automatically traverses the n-level page tables in physical memory without OS intervention
* **If valid PTE found in RAM:** PTW loads it directly into the TLB. CPU resumes immediately.
* **If PTE invalid or on disk:** PTW stops and triggers a **Page Fault** exception. The OS software finally takes over to fetch the data from the disk.

## Performing Address Translation 

Virtual memory requires HW+SW support
Job of software OS to populate tables, edit tables, handle memory allocation, etc.

Page size is specified by the ISA, and the Core sends a virtual address to the memory hierarchy, which sends the page table entry back to the core. 

Page table is tag store for physical memory data store
PTE is the tag store entry for a virtual page memory

In case of a fault

1. stall application and checkpoint
2. fetch data from disk OR/AND find free space in physical memory 
3. store the new mapping in the PT

We don't want the CPU to be involved in transfering data from disk to memory (use DMA, direct memory access)

---

**Clock Page Replacement Algorithm** is more efficient than LRU:

- Circular list of physical memory frame (imagine as clock)
- Pointer to last used location
- R-Bit (Reference). 1 means recently used, 0 means longer not used
- R-Bit is set to 1 when used element from RAM. If not in RAM, pointer turns clockwise and searches for a memory location with R=0