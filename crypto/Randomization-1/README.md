Disassemble the code with IDA and checked the next function. It uses the LCG algorithm to generate the next number:
```
 curr = 37 * curr + 65
 ```
 After doing it, we can see that in assembly the code does a movzx, so it shft left 8 bit the curr variable and then it shifts right alway by 8.
 So only the last 8bit are taken as result.
