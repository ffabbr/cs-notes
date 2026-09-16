

Unsigned 43: 00101011
Signed 43: 00101011
Signed –43: 11010100 (1st bit is 1, rest is flipped)

because 011111111+1=00000000

logical operations: f.ex. &&, ||, !, etc.
bitwise operations: &, |, ~, etc.

f.ex. `00101011 || 00000000 = 00000001` as `00101011` is 1 , but `00101011 | 10000101 = 10101111` 

**Shift**

- right shift for dividing by 2

unsigned (logical): `10101011 >> 10 = 00101010`
arithmetic (signed): `10101011 >> 10 = 11101010` (shift by 2 but propagate sign bit instead of always 0)

**Bit masks**

**testing for i-th bit**
`input & (1<<i)` 
f.ex. `00101011 & 00001000 = 00001000` 

**flip i-th bit with xor**
`(input ^ (1 << i))` 
f.ex. `00101011 ^ 00001000) = 00100011`

**setting**
`(input | (1 << i))`
f.ex. `00101011 | 00000100 = 00101111`