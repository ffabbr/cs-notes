
A macro is a text replacement rule. 

```c
#define SIZE 100              
#define SQUARE(x) ((x) * (x)) 

int arr[SIZE];                // becomes: int arr[100];
int y = SQUARE(5);            // becomes: int y = ((5) * (5));
```

```c
#include<stdio.h>
#define SQUARE(x) x*x

int main(void) {
  int a = 3;
  printf("%d\n", SQUARE(a + 1));
  # output: 7
  # a+1*a+1 = 3+1*3+1 = 7
  return 0;
}
```



![[Pasted image 20261007131033.png]]

**1. `#` turns an argument into a string (stringification).** `#val` takes whatever text you passed as `val` and wraps it in quotes. If you pass `s1.c[0]`, then `#val` becomes `"s1.c[0]"`.

**2. Adjacent string literals are glued together.** C automatically joins string literals that sit next to each other

