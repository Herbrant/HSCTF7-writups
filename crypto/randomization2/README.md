# Randomization 2

I was tired of writing verbose descriptions so I went and drank some coffee. Now I'm coding in Java. Darn it.

The C implementation implements the PRNG used in java.util.Random, but outputs all 64 bits instead of the top 32.

Connect with nc crypto.hsctf.com 6002.

## Solution

It is a C implementation of java.util.Random (PRNG algorithm).
Analizying the code you will see initRandom function and the next function.
initRandom() exatract a urandom number from /dev/urandom (pseudo random number) that will be the seed.
next() calculates the next value with the formula:

```
next_value = old_value * 0x5DEECE66 + 0xb
```

You have to guess all ten numbers that the program will ask you with the formula written above.