#!/usr/bin/python36
f = 0
n = c = int(input('Digite um número para calcular o fatorial: '))
while c != 1:
    print(c, end=' ')
    if f == 0:
        f = c * (c-1)
        c = c-2
        print(c+1)
    else:
        f += f * (c-1)
        c = c - 1
print('O fatorial de {} é {}'.format(n, f))

