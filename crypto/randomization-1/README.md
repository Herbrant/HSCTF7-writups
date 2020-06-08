# Randomization 1

Hear ye, for I have constructed another diversionary exercise taking the form of a competition whose contents consist of the repeated divination of an arbitarily and pseudorandomly generated numeric!

Connect with nc crypto.hsctf.com 6001.

## Solution

Analizying the code you will see initRandom function and the next function.
initRandom() exatract a urandom number from /dev/urandom (pseudo random number) that will be the seed.
next() uses the LCG algorithm to generate the next number as follow:

```
curr = 37 * curr + 65
```

We can see that in the assembly that code does a MOVZX, so it shfts left 8 bit the curr variable and then shifts it right alway by 8.
So only the last 8 bit are taken as result.