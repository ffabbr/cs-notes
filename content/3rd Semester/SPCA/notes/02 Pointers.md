Thanks to https://emils.site/docs/lecture_notes/systems_programming/pointers/

**pointer**: variable that stores a memory location
**dereference**: get the value of that location

- `&` means "address of."
- `*` in a declaration means "this is a pointer." 
- `*` in an expression means "go to the address." This is called dereferencing.
- Each extra `*` is one more hop. 

```c
int value = 10; // normal variable
int *ptr = &value; // ptr holds ADDRESS of value
*ptr = 20; // go to address, store 20 -> value is now 20

int **ptr_to_ptr = &ptr; // ADDRESS of the pointer
**ptr_to_ptr = 30; // follow the arrows, set x to 7
```

If we add or subtract to a pointer, it will **not** simply add or subtract the number. It will add or subtract as many bytes as the value takes up times that number. So if there were multiple values with the same type in an array, adding one to a pointer would jump to the next one.

```c
int* ip = (int*) 4;
char* cp = (char*) 4;

ip += 1; // int is 4 bytes, so now 8
cp += 4; // char is 1 byte so now 8

// ip now holds the same value as cp
```

You can add an integer n to a pointer p. p now points to n objects further on.
## Arrays

An array name is like a pointer to the first element. 

```c
int arr[3] = {2, 3, 4}; // array
int *p1 = &arr[0]; // pointer to first element
int *p2 = arr; // same as line 2
```

![[Bildschirmfoto 2026-10-07 um 11.59.11.png]]
## Function Arguments

Function arguments in C are **pass-by-value**. This means the entire argument will get copied and modifying it inside the function will not change the original one. We can use pointers to **pass-by-reference**.

```c
#include <stdio.h>

void mod1(int x)   { 
	x = 1; 
}
void mod2(int* x)  { 
	*x = 1; 
}
void mod3(int x[]) { 
	x[0] = 1; 
}

int main(void) {
    int x = 0;
    int a[1] = {0};

    mod1(x);   
    // x is still 0
    mod2(&x);  
    // we passed the address, so now x is 1
    mod3(a);   
    // array names decay into a pointer to first element, so a[0] is now 1
    return 0;
}
```

```c
values[0]     // same as *values
values[2]     // same as *(values + 2)
```

## Function Pointers

```c
#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

int main(void) {
    int (*func)(int, int) = add;  
    // (*func) is a pointer to a function with 2 arguments returning an int
    
    int x = 0;
    int y = 1;
    
    int z = func(x, y); 
    // calls add through the pointer

    printf("%d\n", z); // prints 1
    return 0;
}
```


---

## Array Tasks (hard)

`sizeof` array is number of elements times size of an element

`char name[100] = "test";` creats array of 100 chars, initiallized with 0 and added

```
index:  0    1    2    3    4    5   ...  89   90  ...  99
       't'  'e'  's'  't'  \0   \0  ...  \0   \0  ...  \0
```


But 

`char *test = "I love SPCA";` is a pointer. The text is a string literal placed in a read-only section of the program. Test holds the address. `char c = test[0];` is fine because it's just `*(test + 0)`, but `test[0] = 'X';` doesn't work because it's read only. 


`p && *p`: "p is not null (it points somewhere) and the thing it points at is not zero". f.ex. `if (name && *name) {...} // name is not NULL and not ""`. (because if empty then first character would be `\0`) 

**Memory Structure**

```
high addresses (0xfff...)
┌─────────────────────────┐
│ stack                   │  local variables, function calls
│   ↓ grows down          │  (done automatically)
│                         │
│   (free space)          │
│                         │
│   ↑ grows up            │
│ heap                    │  malloc / free (manually)
├─────────────────────────┤
│ read-only data          │  string literals like "I love SPCA"
├─────────────────────────┤
│ unmapped                │  address 0 = NULL lives here
└─────────────────────────┘
low addresses (0)
```


```c
#include
int main() {
    int a = 0;
    int *b = malloc(sizeof(int));
    if ((&a) > b) {
        printf("Trick!\n"); // <-- THIS (see graphic above)
    } else {
        printf("Treat!\n");
    }
    return 0;
}
```

---

```c
void copy(char *to, char *from) { 
	while ((*to++ = *from++) != ’\0’) ; 
}
```

copies character by character from `from` to `to` and after each time move the pointers forward to the next characters. Compare the copied character with `\0`, which means end of string.

**Task**


![[Pasted image 20261007125856.png]]

#### Line 1: `**++cpp`

1. `++cpp`: `cpp` moves forward, so now `cpp → cp[1]` 
2. `*` gives value of  `cp[1]`, which is `c+2`
3. `*` gives `c[2]`, which is `"POINT"`.
#### Line 2: `*--*++cpp+3`

1. `++cpp`: `cpp` moves again, so now `cpp → cp[2]` (permanently).
2. `*` gives `cp[2]`, which is `c+1`.
3. `--` decrements **`cp[2]` itself**, so `cp[2]` is now `c+0`. This changes the `cp` array.
4. `*` gives `c[0]`, which is `"ENTER"`.
5. `+3` skips 3 characters of `"ENTER"`, leaving `"ER"`.
#### Line 3: `*cpp[-2]+3`

1. `cpp[-2]` is `*(cpp - 2)`. Since `cpp` is at `cp[2]`, two back is `cp[0]`, which is `c+3`. Indexing doesn't move `cpp`.
2. `*` gives `c[3]`, which is `"FIRST"`.
3. `+3` skips `"FIR"`, leaving `"ST"`.
#### Line 4: `cpp[-1][-1]+1`

1. `cpp[-1]` is one back from `cp[2]`, so `cp[1]`, which is `c+2`. This one was never changed.
2. `[-1]` on that is `*(c+2 - 1)`, so `c[1]`, which is `"NEW"`.
3. `+1` skips `"N"`, leaving `"EW"`.
