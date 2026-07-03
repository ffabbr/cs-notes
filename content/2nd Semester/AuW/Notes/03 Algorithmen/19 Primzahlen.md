
Introduction
- Zahl $n$ ist Primzahl wenn $gcd(a,n)=1$,  $\forall a \in \{1,2,\dots, n-2\}$  
- Zeuge/Zertifikat: Zahl die zeigt, dass n keine Primzahl ist
- ==Carmichael Zahl==: zusammengesetzte Zahl für die es keine Zeugen gibt
- Pseudoprimzahlbasis a von n: n keine Primzahl aber trotzdem z.B. $a^{n-1} \equiv_{n} 1$

## Euklid (n)

Wähle random a, teste gcd(n,a), wenn $gcd(n,a)=1$, return prime, sonst nicht prime

- korrekt für Primzahlen
- Korrekt mit Wahrscheinlichkeit $\geq 1-O\left( \frac{1}{\sqrt{ n }} \right)$ für NEIN (= nicht-Primzahlen)

## Fermat

Wähle random a, falls p prim, dann $a^{p-1} \equiv_{p} 1$, also return prime, sonst nicht prime. 

- korrekt für Primzahlen
- Korrekt mit Wahrscheinlichkeit $> \frac{1}{2}$ für NEIN (= nicht-Primzahlen) die ==keine Carmichael-Zahl sind==

## Miller-Rabin

Wir finden heraus ob $n$ eine Primzahl ist in $O((\log n)^3)$.

- wenn n prim, ist $\{0, \dots, n-1\}$ ein Körper
- Polynom vom Grad 2 hat höchstens 2 Nullstellen in einem Körper
- $x^2=1$ hat nur Nullstellen $x_{1}=1, x_{2}=-1 \equiv_{n} n-1$
- finden wir noch eine andere Nullstelle, ist n keine Primzahl

- nehme ein $a \in \{2, \dots, n-1\}$
	- falls $a^{n-1} \not\equiv_{n} 1$, keine Primzahl ([[#Fermat]])
	- else if (kann Wurzel ziehen)
		- falls $\sqrt{a^{n-1}} \not\in \{1, n-1\}$, n sicher keine Primzahl, da weitere Nullstelle gefunden
		- falls $\sqrt{a^{n-1}} \equiv_{n} n-1$ geht nicht weiter, abbruch (können nicht Wurzel von $-1$ ziehen)
		- falls $\sqrt{a^{n-1}} \equiv_n 1$ repeat Wurzel ziehen (else if branch)

> [!note]- Miller Rabin Java Code
> ```java
> import algorithms.*;
>
> // Main class required by Java.
> // The online judge / framework will run the main method inside this class.
> class Main {
>
>     public static void main(String[] args) {
>
>         // These lines are commented out.
>         // They are useful when testing locally with input/output files.
>         //
>         // In.open("public/sample.in");
>         // would make the program read input from public/sample.in.
>         //
>         // Out.compareTo("public/sample.out");
>         // would compare the program output against public/sample.out.
>         //
>         // In.open("public/sample.in");
>         // Out.compareTo("public/sample.out");
>
>         // Read the number of test cases.
>         // Each test case will contain one number n,
>         // and we will decide whether n is probably prime.
>         int t = In.readInt();
>
>         // Run testCase() exactly t times.
>         for (int i = 0; i < t; i++) {
>             testCase();
>         }
>
>         // This would close the input file if In.open(...) had been used.
>         // It is not needed for normal standard input.
>         //
>         // In.close();
>     }
>
>     public static void testCase() {
>
>         // Read the number we want to test for primality.
>         long n = In.readLong();
>
>         // This variable stores the final answer.
>         // It starts as false, and we update it based on the Miller-Rabin test.
>         boolean isPrime = false;
>
>         // Number of random Miller-Rabin rounds.
>         //
>         // More iterations reduce the probability of a composite number
>         // being incorrectly classified as prime.
>         //
>         // This implementation is probabilistic because it uses random bases.
>         int iterations = 20;
>
>         // Handle the two smallest prime numbers directly.
>         //
>         // Miller-Rabin is usually written for odd n > 3,
>         // so we treat 2 and 3 as special cases.
>         if (n == 2 || n == 3) {
>             isPrime = true;
>
>         // Handle all clearly non-prime cases:
>         //
>         // n <= 1:
>         //   0, 1, and negative numbers are not prime.
>         //
>         // n % 2 == 0:
>         //   Any even number greater than 2 is composite.
>         } else if (n <= 1 || n % 2 == 0) {
>             isPrime = false;
>
>         } else {
>
>             // At this point, n is odd and greater than 3.
>             //
>             // We assume n is prime unless a Miller-Rabin witness proves
>             // that it is composite.
>             isPrime = true;
>
>             // Miller-Rabin writes n - 1 in this form:
>             //
>             //     n - 1 = d * 2^k
>             //
>             // where d is odd.
>             //
>             // We start with d = n - 1 and repeatedly divide out factors of 2.
>             long d = n - 1;
>
>             // k counts how many factors of 2 were removed from n - 1.
>             int k = 0;
>
>             // Keep dividing d by 2 while it is even.
>             //
>             // Example:
>             // If n = 21, then n - 1 = 20.
>             // 20 = 5 * 2^2, so d becomes 5 and k becomes 2.
>             while (d % 2 == 0) {
>                 d /= 2;
>                 k++;
>             }
>
>             // Perform the Miller-Rabin test several times,
>             // each time using a different random base a.
>             for (int iteration = 0; iteration < iterations; iteration++) {
>
>                 // Pick a random base a in the range [2, n - 2].
>                 //
>                 // Math.random() gives a double in [0.0, 1.0).
>                 //
>                 // Math.random() * (n - 3) gives a value in [0, n - 3).
>                 //
>                 // Casting to long truncates the decimal part.
>                 //
>                 // Adding 2 shifts the range to approximately [2, n - 2].
>                 long a = (long) (Math.random() * (n - 3)) + 2;
>
>                 // Compute:
>                 //
>                 //     x = a^d mod n
>                 //
>                 // This is the first Miller-Rabin check.
>                 long x = powMod(a, d, n);
>
>                 // If x is 1 or n - 1, then this base a does not prove
>                 // that n is composite.
>                 //
>                 // We continue to the next random base (loop iteration).
>                 if (x == 1 || x == n - 1) {
>                     continue;
>                 }
>
>                 // At this point, x was neither 1 nor n - 1.
>                 //
>                 // We assume this base is a witness that n is composite,
>                 // unless the repeated squaring step reaches n - 1.
>                 boolean witnessSaysComposite = true;
>
>                 // Repeatedly square x:
>                 //
>                 //     x = x^2 mod n
>                 //
>                 // We do this up to k - 1 times.
>                 //
>                 // This checks the sequence:
>                 //
>                 //     a^d, a^(2d), a^(4d), ..., a^(2^(k-1)d) mod n
>                 //
>                 // For a prime n, one of these values should become n - 1
>                 // unless the first value was already 1.
>                 for (int i = 0; i < k - 1; i++) {
>
>                     // Square x modulo n without overflowing long.
>                     //
>                     // Instead of using:
>                     //
>                     //     x = (x * x) % n;
>                     //
>                     // we call mulMod because x * x may overflow
>                     // if x is large.
>                     x = mulMod(x, x, n);
>
>                     // If x becomes n - 1, this base a does not prove
>                     // that n is composite.
>                     //
>                     // The current Miller-Rabin round passes.
>                     if (x == n - 1) {
>                         witnessSaysComposite = false;
>                         break;
>                     }
>
>                     // If x becomes 1 before reaching n - 1,
>                     // this is bad for primality.
>                     //
>                     // For a prime number, the square root behavior modulo n
>                     // should not produce this kind of early 1 in this sequence.
>                     //
>                     // We break and leave witnessSaysComposite as true.
>                     if (x == 1) {
>                         break;
>                     }
>                 }
>
>                 // If this random base proved n is composite,
>                 // then n is definitely not prime.
>                 //
>                 // We can stop immediately; no more rounds are needed.
>                 if (witnessSaysComposite) {
>                     isPrime = false;
>                     break;
>                 }
>             }
>         }
>
>         // Print the final answer for this test case.
>         //
>         // "yes" means n is probably prime.
>         // "no" means n is definitely composite.
>         //
>         // Because this version uses random bases, "yes" is probabilistic.
>         Out.println(isPrime ? "yes" : "no");
>     }
>
>     public static long powMod(long a, long d, long n) {
>
>         // This function computes:
>         //
>         //     a^d mod n
>         //
>         // efficiently using binary exponentiation.
>         //
>         // Instead of multiplying a by itself d times,
>         // it processes the binary representation of d.
>
>         // result stores the accumulated answer.
>         //
>         // We start with 1 because 1 is the multiplicative identity.
>         long result = 1;
>
>         // Reduce a modulo n first.
>         //
>         // This keeps a smaller and does not change the final result because:
>         //
>         //     a^d mod n == (a mod n)^d mod n
>         a = a % n;
>
>         // Continue until all bits of d have been processed.
>         while (d > 0) {
>
>             // If d is odd, then the current power of a contributes
>             // to the final answer.
>             //
>             // In binary exponentiation, this corresponds to a 1-bit
>             // in the binary form of d.
>             if (d % 2 == 1) {
>
>                 // Multiply result by a modulo n.
>                 //
>                 // We use mulMod instead of direct multiplication
>                 // to avoid overflow when result and a are large.
>                 result = mulMod(result, a, n);
>             }
>
>             // Square a modulo n.
>             //
>             // This moves to the next power:
>             //
>             //     a, a^2, a^4, a^8, ...
>             //
>             // Again, mulMod avoids overflow.
>             a = mulMod(a, a, n);
>
>             // Divide d by 2.
>             //
>             // This shifts the binary representation of d right by one bit.
>             d = d / 2;
>         }
>
>         // Return a^d mod n.
>         //
>         // Note: by this point, the original d has been reduced to 0,
>         // but result contains the answer.
>         return result;
>     }
>
>     private static long mulMod(long a, long b, long mod) {
>
>         // This function computes:
>         //
>         //     (a * b) mod mod
>         //
>         // without directly calculating a * b.
>         //
>         // Direct multiplication can overflow long if a and b are large.
>         //
>         // Instead, this uses repeated doubling, similar to binary multiplication.
>
>         // res stores the accumulated modular product.
>         long res = 0;
>
>         // Reduce a modulo mod first.
>         //
>         // This keeps numbers smaller and does not change the final result.
>         a %= mod;
>
>         // Process b bit by bit.
>         while (b > 0) {
>
>             // If b is odd, add the current value of a to the result.
>             //
>             // This corresponds to a 1-bit in the binary representation of b.
>             if (b % 2 == 1) {
>
>                 // Add a to res, then reduce modulo mod.
>                 //
>                 // This keeps res in the range [0, mod - 1].
>                 res = (res + a) % mod;
>             }
>
>             // Double a modulo mod.
>             //
>             // This prepares a for the next binary digit of b.
>             //
>             // Conceptually:
>             //
>             //     a, 2a, 4a, 8a, ...
>             a = (a * 2) % mod;
>
>             // Divide b by 2.
>             //
>             // This moves to the next bit of b.
>             b /= 2;
>         }
>
>         // Return (original a * original b) mod mod.
>         return res;
>     }
> }
> ```

l