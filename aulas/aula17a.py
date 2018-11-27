#!/usr/bin/python36
num = [2, 5, 9, 1]
print(num)
num[2] = 3
print(num)
num.append(8)
print(num)
for p, v in enumerate(num):
    print(f'Na posição {p} contém o valor {v}!')

