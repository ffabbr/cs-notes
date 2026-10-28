
Structs and unions in C are custom data types that allow to group multiple variables of different types under a single name, but they manage memory differently.

## Alignment

- Primitive data types of K bytes are K-byte aligned
- Integers are 4 byte aligned, so we can only put them in sp+0, sp+4, etc. so we might need padding so that that works. See [[00 C Syntax#Data types|Data types and sizes]].

## Union

The size of the union is determined strictly by the largest member.
It uses a single, shared memory block for all of its members (might overwrite)

## Sruct

- A struct allocates separate memory space for every member it contains. 
- Padding added such that every element’s alignment fulfilled. 
- Padding at the end of struct added such that it’s length is a multiple of K (largest of all elements alignment requirements)

![[Bildschirmfoto 2026-10-28 um 13.03.50.png]]