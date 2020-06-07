# Randomization 1

Hear ye, for I have constructed another diversionary exercise taking the form of a competition whose contents consist of the repeated divination of an arbitarily and pseudorandomly generated numeric!

Connect with nc crypto.hsctf.com 6001.

## Solution

Disassemble the code with IDA and checked the next function. It uses the LCG algorithm to generate the next number:

```
curr = 37 * curr + 65
```

After doing it, we can see that in assembly the code does a movzx, so it shft left 8 bit the curr variable and then it shifts right alway by 8.
So only the last 8bit are taken as result.
