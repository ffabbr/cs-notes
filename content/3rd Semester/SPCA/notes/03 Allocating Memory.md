Thanks to https://emils.site/docs/lecture_notes/systems_programming/alloc_memory/

## Malloc

Local array: `char arr[x];` lives in the functions own space, can't return that. Also can't solve with pointers since calling the function again overwrites that. 

Malloc `char* arr = malloc(x);`, asks system for memory and can be **freed** with `free(...)`, system returns NULL if no memory for malloc available, so check for that. 

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