
==**Arguments**==
- **%rdi**: 1. Argument
- **%rsi**: 2. Argument
- **%rax**: return value
- **%rsp**: Stack pointer

Moving memory to memory location is not possible, need register to temporarily store.

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
The arguments need to be in the right registers (see top) for the new function call. Function arguments can be both on the stack and in registers. 

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
Stack or register with pointer

```C
# int local_variables()
# {
#   int local = 3;
#   return call_me(local, &local);
# }
subq $8, %rsp // Reserve 8 bytes on the stack
movl $3, (%rsp) // Store integer 3 in memory
movl (%rsp), %edi // integer as first argument
movq %rsp, %rsi // variable address as 2nd arg
call call_me // call function
addq $8, %rsp // restore stack pointer
ret
```

==**Loops**==
Coming soon...

==**Condition Codes Register**==
Coming soon...

==**Quicksort**==
Coming soon...

---

[[x86-64-assembly-reference-sheet.pdf]]

![[Bildschirmfoto 2026-10-27 um 19.26.42.png]]![[Bildschirmfoto 2026-10-27 um 19.26.47.png]]![[Bildschirmfoto 2026-10-27 um 19.26.53.png]]