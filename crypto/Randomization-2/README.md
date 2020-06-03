# Randomization 2
It is a C implementation of java.util.Random (PRNG algorithm).
Analizying the code you will see initRandom function and the next function.
initRandom() exatract a urandom number from /dev/urandom (pseudo random number) that will be the seed.
next() calculates the next value with the formula:
```
next_value = old_value * 0x5DEECE66 + 0xb
```

You have to guess all ten numbers that the program will ask you with the formula written above.