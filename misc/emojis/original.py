output = "xB^r_En}INc4v"

# e1 = (input[0])
# e2 = (input[1])
# e3 = (input[2])
# e4 = (input[3])
# e5 = (input[4])
# e6 = (input[5])
# e7 = (input[6])
# e8 = (input[7])
# e9 = (input[8])
# e10 = (input[9])
# e11 = (input[10])
# e12 = (input[11])
# e13 = (input[12])

f = open("input_result.txt", "r")

lines = []

for line in f:
    lines.append(int(line.strip("\n")))

e1 = lines[0]
e2 = lines[1]
e3 = lines[2]
e4 = lines[3]
e5 = lines[4]
e6 = lines[5]
e7 = lines[6]
e8 = lines[7]
e9 = lines[8]
e10 = lines[9]
e11 = lines[10]
e12 = lines[11]
e13 = lines[12]
e15 = 0

f.close()

result_t = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13]
result = ""
counter = 1
vett  = []

for v in result_t:
    vett.append(v)
    result = result + chr(v)
    counter = counter+1

print("Vett:")
print(vett)

if e2 != e13:
    e12 = e12 - e1

if e2 != e6:
    e3 = e8

e2 = e2 - e5
e10 = e10 + e7

if e5 != e10:
    e15 = e4
    
e3 = e3 - 8
e4 = e13
e13 = e15
e2 = e2 + e8
e2 = e2 - e4
e1 = e1 + e12
e3 = e3 + 4
e4 = e4 + 2


if e5 != e10:
    e5 = e5 + e10

e12 = e12 + 1
e11 = e11 - 8
e8 = e8 + e9
e6 = e6 - e7

if e11 != 4:
    e7 = e7 + e9

e9 = e9 + 8
e1 = e1 - e3
e5 = e5 - e12
e3 = e3 + e3
e8 = e8 + e12
if e11 != 0:
    e10 = e10 - e2



result_t = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13]
result = ""
counter = 1
vett  = []

for v in result_t:
    vett.append(v)
    result = result + chr(v)
    counter = counter+1

print("Vett:")
print(vett)

print("\nOutput:")

out_vet = []

for val in output:
    out_vet.append((val))

print(out_vet)

print("result: " + result)