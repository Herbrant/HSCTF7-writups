# Bank Robbing

dont do it dont do it dont rob the bank

## Solution

The challenge gives you a file from which you have to extract the flag. If you analyze it with an hex editor you can see that it is a RIFF file (0x00000000/03 - RIFF), a file container format for multimedia such as audio and video.

Delete (trim) the hex values from 0x00000000 to 0x000006FF. You'll obtain a new file from which you have to extract the hidden audio file using [fmod_extractors](https://zenhax.com/viewtopic.php?t=1901). Just drag and drop it on fsb_aud_extr.exe and you'll get "bankfiles.wav" which will tell you the flag.

```
flag{sh4m3_0n_y0u_4_r0bbing_th15_b4nk}
```