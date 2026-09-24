## General Overvations

- `#include <stdio.h>` (stdio stands for standard io)
- main is needed
- switch only works with integers
- 0 means false, non-zero means true, so int can be seen as bool

- no support for function overloading
- there are no methods

- goto jumps to a different part, **try not to use**. can be useful for f.ex. breaking out of nested loops (could instead do a bool and break, then in the outer loop check condition of bool)

- arg 1 is always the **filename**

- matrices (2d arrays) are stored linearly, row for row 
- `bool` instead of `boolean`
- instructions looked at in order, so either put method definitions above them being called or "announce" them before with just the signature, call them, then define them.
- use `void greet(void);` for no parameters, else f.ex. `int square(int number);`
- `printf()` for printing

```c
int temperature = -5; // signed
size_t length = 100;  // unsigned
```

For `printf()` the first argument must always be a string. We can "announce" what other type follows though

```c
// example 
printf("number: %d\n", number);   // Insert an int at %d

// other
printf("%d\n", integer);
printf("%f\n", decimal);
printf("%c\n", character);
printf("%s\n", string);
```
## Pointers

- `&value` is the Address of value
- `*pointer` is the Object stored at that address
- never dereference a pointer from NULL to a value

```c
  int value = 10;
  int *pointer = &value;
  *pointer = 25; 
  // value changed to 25 through pointer
```

## Arrays

```c
int numbers[] = {1, 2, 3, 4, 5};
size_t length = sizeof(numbers) / sizeof(numbers[0]);
```

- since `sizeof(numbers)` is the size of "the entire thing" and `sizeof(numbers[0])` is the size of a single int
- the arrays name becomes a pointer to its first element (so `*numbers` is same to `numbers[0]`)
- there is no index out of bounds error, it would just print something unwanted or crash

## Strings

- there is no String, String is an array of chars
- char array for string needs to have end position \0 to indicate ending
- `char name[] = "Fabian";` 
- `strncpy` (copy), arguments: destination, origin, max number of chars to copy
- `strncat` (concatenation)

