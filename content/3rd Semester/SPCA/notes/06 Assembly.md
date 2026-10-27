
==**Arguments**==
- **%rdi**: 1. Argument
- **%rsi**: 2. Argument
- **%rax**: return value
- **%rsp**: Stack pointer

==**Branches**==
```assembly
# int branches(int a)
# {
#   if(a < 12)
#   {
#     return -1;
#  }
#   else{
#     return 1;
#   }
# }

branches:
  cmpq    $12, %rdi
  jl      less
  movq    $1, %rax
  ret
  
less: 
  movq    $-1, %rax
  ret

```

==**Function Calls**==
The arguments need to be in the right registers (see top) for the new function call. 
```assembly
calling_functions:
# int calling_functions(int a, int b)
# {
#   return call_me(b, NULL);
  ret
# }

  movq %rsi, %rdi
  movq $0, %rsi
  call call_me
  ret
```

==**Local Variables**==
```C
# int local_variables()
# {
#   int local = 3;
#   return call_me(local, &local);
# }
```

| `subq $8, %rsp`     | Reserve 8 bytes on the stack                       |
| ------------------- | -------------------------------------------------- |
| `movl $3, (%rsp)`   | Store the integer 3 in memory                      |
| `movl (%rsp), %edi` | Pass the integer value as the first argument       |
| `movq %rsp, %rsi`   | Pass the variable's address as the second argument |
| `call call_me`      | Call the function                                  |
| `addq $8, %rsp`     | Restore the stack pointer                          |
| `ret`               | Return the result in `%rax`                        |


==**Loops**==
Coming soon...

==**Condition Codes Register**==
Coming soon...

![[Bildschirmfoto 2026-10-27 um 19.26.42.png]]![[Bildschirmfoto 2026-10-27 um 19.26.47.png]]![[Bildschirmfoto 2026-10-27 um 19.26.53.png]]