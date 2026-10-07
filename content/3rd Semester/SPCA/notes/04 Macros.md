
A macro is a text replacement rule. 

```c
#define SIZE 100              
#define SQUARE(x) ((x) * (x)) 

int arr[SIZE];                // becomes: int arr[100];
int y = SQUARE(5);            // becomes: int y = ((5) * (5));
```


![[Pasted image 20261007131033.png]]

**1. `#` turns an argument into a string (stringification).** `#val` takes whatever text you passed as `val` and wraps it in quotes. If you pass `s1.c[0]`, then `#val` becomes `"s1.c[0]"`.

**2. Adjacent string literals are glued together.** C automatically joins string literals that sit next to each other

