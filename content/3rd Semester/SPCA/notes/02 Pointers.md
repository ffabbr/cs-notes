Thanks to https://emils.site/docs/lecture_notes/systems_programming/pointers/

**pointer**: variable that stores a memory location
**dereference**: get the value of that location

```c
int x = 10;
int* p = &x; // pointer to address of x
*p = 5; // set x to 5 by dereferencing p

int** q = &p; // pointer to a pointer to the address of x
**q = 7; // set x to 7
```

If we add or subtract to a pointer, it will **not** simply add or subtract the number. It will add or subtract as many bytes as the value takes up times that number. So if there were multiple values with the same type in an array, adding one to a pointer would jump to the next one.

```c
int* ip = (int*) 4;
char* cp = (char*) 4;

ip += 1; // int is 4 bytes, so now 8
cp += 4; // char is 1 byte so now 8

// ip now holds the same value as cp
```


## Arrays

```c
int arr[10]; // array
int (*pa)[] = &arr; // pointer to an array
int* pi = &arr[0]; // pointer to first element
```

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

    printf("%d %d\n", x, a[0]);  // prints "1 1"
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
