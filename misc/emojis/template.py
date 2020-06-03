import itertools
import string

input = "xB^r_En}INc4v"

e1 = ord(input[0])
e2 = ord(input[1])
e3 = ord(input[2])
e4 = ord(input[3])
e5 = ord(input[4])
e6 = ord(input[5])
e7 = ord(input[6])
e8 = ord(input[7])
e9 = ord(input[8])
e10 = ord(input[9])
e11 = ord(input[10])
e12 = ord(input[11])
e13 = ord(input[12])
e15 = 0

if e11 != 0:
    e10 = e10 - e2

e8 = e8 - e12
e3 = e3 + e3
e5 = e5 - e12
e1 = e1 - e3
e9 = e9 + 8

if e11 != 4:
    e7 = e7 + e9

e6 = e6 - e7
e8 = e8 + e9
e11 = e11 - 8
e12 = e12 + 1

if e5 != e10:
    e5 = e5 + e10

e4 = e4 + 2
e3 = e3 + 4
e1 = e1 + e12
e2 = e2 - e4
e2 = e2 + e8
e13 = e15
e4 = e13
e3 = e3 - 8

if e5 != e10:
    e15 = e4
e10 = e10 + e7
e2 = e2 - e5

if e2 != e6:
    e3 = e8



result_t = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13]
result = ""

for v in result_t:
    result = result + chr(v)

print(result)
