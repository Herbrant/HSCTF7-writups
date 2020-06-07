# Mad Libs

We all know that officer speeches are just mad libs, anyway.

## Solution

Analyzing the image with binwalk you will see:

```
> binwalk Mad_Libs.png

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 1089 x 544, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, compressed
```

So one is the image and other is zlib compressed.

Decode it with this steganography tool [Link](https://stylesuxx.github.io/steganography/)