def reverse_print(val):
    return str(val)[::-1]

def min_print(val):
    return str(val-1)

output = ""

#Good luck reading this lol 
Z = 0
O =1 
output += reverse_print(Z) 
T = 2
L = 5*1 
output += reverse_print(L)

for i in range(0, 3):
    output += reverse_print(O)

output += reverse_print(T)

for i in range(0, 2): 
    reverse_print(O) 

W = L + 1 

output += reverse_print(W) 

N = 13*70

N = N+1

output += reverse_print(N)

output += min_print(1) 
P = 0
K = 0

for i in range(0, 6): 
    P = P+1
    K = K+1


for i in range(0, 8): 
    K = K+1

K = K*P

output += reverse_print(K)
min_print(2)
min_print(2)

L = L-5
output += reverse_print(L)
output += reverse_print(L)

A = 1
T = 1

for i in range(0, 4): 
    P = 2*A
    P = P+1
    T = T+P
    A = A + 1

output += reverse_print(T)

print(output)