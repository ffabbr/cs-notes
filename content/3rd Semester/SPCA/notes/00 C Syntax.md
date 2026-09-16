
## General Overvations

- no support for function overloading
- `const char name[] = "Fabian";` (String is an array of chars)
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