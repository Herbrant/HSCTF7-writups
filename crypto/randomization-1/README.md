# Randomization 1

Hear ye, for I have constructed another diversionary exercise taking the form of a competition whose contents consist of the repeated divination of an arbitarily and pseudorandomly generated numeric!

Connect with nc crypto.hsctf.com 6001.

## Solution

Analizying the code you will see "initRandom" function and "next" function.
initRandom() exatract a urandom number from /dev/urandom (pseudo random number) that will be the seed.
next() uses the LCG algorithm to generate the next number as follow:

```
curr = 37 * curr + 65
```

We can see in the assembly that code does a MOVZX on the return of next(), so it shfts left the curr value by 8 bits and then shifts right it always by 8 bits.
In this way, only the last 8 bits are taken as result.

Example:

```
I heard LCGs were cool so I made my own
Since I'm so generous you get a free number: 105
Guess my number:
```

37 * 105 + 65 = 3950 (0x0F6E) ---> 110 (0x6E)

If you answer correctly 10 times, the program will print the flag.

```
flag{l1n34r_c0n6ru3n714l_63n3r470r_f41lur3_4b3bcd43}
```
