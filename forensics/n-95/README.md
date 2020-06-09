# N-95

QR codes wear masks and so should you.

## Solution

Remove the three mattles of color (red, green, blue), fill the cutted black little squares and add 3 big square in the 3 corners as usual in QR codes using Gimp or Photoshop. You'll obtain this:

![alt text](https://i.imgur.com/ZiqDHpS.png)

It is 25x25, so it is a version 2 code. Knowing this, will help us rebuild it. Version 2 codes follow this structure:

![alt text](https://i.imgur.com/UEdwJAy.png)

Blue lines represent the 15 bits of the Format Informations. All of them follow a pattern depending on the ECC Level + Mask Pattern.

In our image, bit 7 to bit 14 are known as we can see in following image (the line under the upper right big square):

![alt text](https://i.imgur.com/x5YMNxO.png)

So you can easily rebuild the line at the right of the upper left big square:

![alt text](https://i.imgur.com/zX9hydD.png)

If you convert bit 7 to bit 14 to binary string you obtain this: 01001011. We're missing the first 7 significative bits. You can find them searching the last 8 bit we obtained before from the convertion in this page: https://www.thonky.com/qr-code-tutorial/format-version-tables.

Doing this, you'll find out that it is M 3 which has got this string type information bits: 101101101001011.

So you can easily rebuild the first 7 bits of the line under the upper left big square and the 7 bits of the line at the right of the down left big square :

![alt text](https://i.imgur.com/DyZfJiW.png)

![alt text](https://i.imgur.com/5OZ3mUM.png)

After applying these changes, this will be our final QR code:

![alt text](https://i.imgur.com/tMsyGu5.png)

To extract the flag, you can open the image in this [site](https://merricx.github.io/qrazybox/) and we use Extract QR Information in the Tool section.

```
flag{60_dozen_quartz_jars}
```
