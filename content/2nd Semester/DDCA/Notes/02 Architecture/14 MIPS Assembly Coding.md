
## Compute Absolute Value

```python
# we take the sign bit, and replicate it to 32 bits to create our mask
# if the difference is negative, the mask is 0xFFFFFFFF, if positive, then 0x00000000
sra $t3, $t2, 31

# diff XOR mask flips bits if negative, does nothing if positive
xor $t2, $t2, $t3

# if t2 was positive, t3 is 0, so no change
# if t2 was negative, t3 is -1. Subtracting -1 is the same as adding 1, flipping sign
sub $t2, $t2, $t3
```

