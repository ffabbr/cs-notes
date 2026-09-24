
## C Specifics

- per default signed
- to define unsigned number, add U, f.ex. `938247U`
- when casting using `(int) unsigned-number` or `(unsigned) signed-number` the **bit representation doesn't change**, so f.ex. positive and negative might flip. only the interpretation of the bit pattern changes
- when mixing unsigned and signed in an expression, **signed values** are being cast to **unsigned** 

![[Bildschirmfoto 2026-09-23 um 10.31.53.png]]

- convert signed to bigger (wider) signed: propagate the sign bit ("sign-extend)
- make unsigned wider: propagate with leading `0`






## Theory

Unsigned 43: 00101011
Signed 43: 00101011

Signed –43: 11010100 (1st bit is 1, rest is flipped)
because 011111111+1=00000000

`~x + 1 = -x`
`~x + x == 111...111 == -1`

**logical operations**: f.ex. &&, ||, !, etc.
**bitwise operations**: &, |, ~, etc.

`-a == ~a + 1`

so `00101011 || 00000000 = 00000001` as `00101011` is 1 , but `00101011 | 10000101 = 10101111` 

**Shift**

right shift for dividing by 2

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