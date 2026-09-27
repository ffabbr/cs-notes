
## Binary representations

- Unsigned 4: 0100
- Signed 4: 0100
- Signed –4: 1100 (invert `0100` to `1011`, add 1) 

- `0101` evaluates to 4 + 1 = 5.
- `1101` evaluates to -8 + 4 + 1 = -3.

- `~x + 1 = -x`
- `~x + x == 111...111 == -1`

F.ex. on 8 bit

|            |      |                                         |
| ---------- | ---- | --------------------------------------- |
| `01111111` | 127  | Maximum positive (`TMax`)               |
| `00000000` | 0    | Zero                                    |
| `11111111` | -1   | Largest value negative number           |
| `11111110` | -2   |                                         |
| `...`      | ...  |                                         |
| `10000000` | -128 | Smallest value negative number (`TMin`) |

---

## Compile behavior

**General**
- per default signed
- to define unsigned number, add U, f.ex. `938247U`

**Explicit Casting**
when casting using `(int) unsigned-number` or `(unsigned) signed-number` the **bit representation is unchanged**, just differently interpreted. f.ex. looking at `1101` signed, that is –3 (-8 + 4 + 1 = -3), but unsigned `1101` is 13.

**Implicit Casting**
when mixing unsigned and signed in an expression, **signed values** are being cast to **unsigned** (mind that this can go wrong, see point above and image below)

**Resizing Rules**
- Expanding (Short to Wide): 
	- unsigned: propagate with leading `0`
	- signed: propagate the sign bit ("sign-extend")
- Shortening (Wide to Short):
	- unsigned: modulus. removing upper bits is like modulus. keep k bits results in mod $2^k$ 
	- signed: same, but problem is sign bit might result in being different


---

## Logical vs. Bitwise Operators

**Logical** (`&&`, `||`, `!`) 
- 0 is false
- anything else is true
- Example: `00101011 || 00000000 = 00000001`
- Example: use of !! to test if any bit is 1

**Bitwise** (`&`, `|`, `~`, `^`): on each bit position independently
- Example: `00101011 | 10000101 = 10101111`

**Bit Shifting** (`>>`, `<<`): Right-shifting divides by 2 per shift
- unsigned (logical): `10101011 >> 10 = 00101010`
- arithmetic (signed): `10101011 >> 10 = 11101010` (shift by 2, propagate sign bit)

**Bitmasks**
- Test a bit: `input & (1 << i)`
    - Example: `00101011 & 00001000 = 00001000` (Tests the 4th bit).
- Set a bit to 1: `input | (1 << i)`
    - Example: `00101011 | 00000100 = 00101111`.
- Flip a bit: `input ^ (1 << i)`
    - Example: `00101011 ^ 00001000 = 00100011`.


---

## Exercises

→ see Code Expert!!

