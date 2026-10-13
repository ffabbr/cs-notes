Thanks to https://emils.site/docs/lecture_notes/systems_programming/alloc_memory/
There is metadata (length and availability) stored in a block to the left of the first block and to the right of the last block. Needed to combine region with other free blocks when freeing a block. We also keep 2 linked-lists, a list for allocated and free blocks. 

## Malloc

Often we want to store memory that is allocated and returned by a function as a result whose size is not known to the caller. 

Initial content is trash (uninitialized, holds leftover bytes). `n*size` can silently overflow if n is huge. 

Local array: `char arr[x];` lives in the functions own space, can't return that. Also can't solve with pointers since calling the function again overwrites that. 


```c
int *arr = malloc(10 * sizeof(int));   // room for 10 ints 
if (arr == NULL) {
    return 1;
}

arr[0] = 5;
arr[1] = 42;

free(arr);
// there's also realloc to change size
```

## Calloc

Like Malloc but initialized to zero
can not overflow (returns NULL)

```c
void *calloc(size_t count, size_t size);
```

2 Parameters: 
- count (how many elements)
- size (how many bytes per element)

(with malloc we need to multiply it ourselves, with calloc that is done automatically)
## Structs

copied on assignment and pass-by-value

```c
struct person {
    int age;
    int height;
};

struct person tom = {24, 180}
struct person* p = &tom;

tom.age = 25;
p->height = 182; // same as (*p).height
```

## Unions

**Unions** only ever hold one of the values declared in it. They only have one memory space for all the values (which means they will override each other).

```c
union fandi {
    float f;
    int i;
};

union fandi u;
u.i = 10;
// u.i = 10 and u.f = 0.0
u.f = 0.5;
// u.i = 1056964608 and u.f = 0.5
```

---


**Memory Structure**

```
high addresses (0xfff...)
┌─────────────────────────┐
│ stack                   │  local vars, function calls
│   ↓ grows down          │  (done automatically)
│                         │
│   (free space)          │
│                         │
│   ↑ grows up            │
│ heap                    │  malloc / free (manually)
├─────────────────────────┤
│ read-only data          │  string literals like
├─────────────────────────┤
│ unmapped                │  address 0 = NULL lives here
└─────────────────────────┘
low addresses (0)
```

---

