import numpy as np
n1 = 990
n2 = 33
table = []
for i in range(n1):
    table.append([])
    for j in range(n2):
        table[i].append(0)

def combination(a1, a2):
    if a2 == 1:
        return a1
    elif a1 == a2:
        return 1
    elif table[a1-1][a2-1] != 0:
        return table[a1-1][a2-1]
    else:
        c = combination(a1-1, a2) + combination(a1-1, a2-1)
        table[a1-1][a2-1] = c
        return c

print(combination(n1, n2))

