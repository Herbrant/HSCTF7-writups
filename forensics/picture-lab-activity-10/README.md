# Picture Lab: Activity 10

Dear APCSA students,

You thought you were done with Picture Lab.

Unfortunately, you were wrong.

We're sorry. We should not have pushed this challenge out, it was irresponsible for us to deploy a meme challenge in the middle of a very serious "Catch-The-Flag" competition. We originally wrote this challenge as a joke, hoping that it would poke fun at Collegeboard's APCSA "Picture Lab"; however, we now realize that this decision was insensitive and outright disrespectful to all those who have to solve the challenge. In the future, we promise that our challenges will not make you suffer as much as this trivial challenge does. We apologize in advance to all those who will suffer at the hands of this beginner-level challenge. I hope you are able to forgive us.

Sincerely,

AC/PMP/JC

## Solution

The challenge gives you a damaged PNG file which has to be recovered. Open the file with an hex editor and fix damaged lines.

Magic Number

```
0x00000000 00 00 00 00 ---> 89 50 4E 47 ("PNG" in ASCII)
```

Chunks

```
0x0000000C 00 48 00 52 ---> 49 48 44 52 ("IHDR" in ASCII)
0x00000025 49 00 41 00 ---> AB 44 45 54 ("IDAT" in ASCII)
0x0003DD2D 49 00 00 00 ---> 49 45 4E 44 ("IEND" in ASCII)
```

You'll get the flag in the recovered image:

```
flag{and_y0u_th0ught_p1ctur3_l4b_was_h4rd}
```