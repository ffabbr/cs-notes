Thanks to https://emils.site/docs/lecture_notes/systems_programming/alloc_memory/

## Malloc

Often we want to store memory that is allocated and returned by a function as a result whose size is not known to the caller. 

Initiall content is trash (uninitialized, holds leftover bytes). `n*size` can silently overflow if n is huge. 

Local array: `char arr[x];` lives in the functions own space, can't return that. Also can't solve with pointers since calling the function again overwrites that. 


```c
int *arr = malloc(10 * sizeof(int));   // room for 10 ints (40 bytes on most machines)
if (arr == NULL) {
    return 1;
}

arr[0] = 5;     // no suffix needed, 5 is already an int
arr[1] = 42;

free(arr);
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
