#!/usr/bin/python36
r = 0
n = int(input('Digite um número: '))
for c in range(1, n+1):
    if n % c == 0:
        r += 1
if r == 2:
    print('O número {} é PRIMO!'.format(n))
else:
    print('O número {} NÃO É PRIMO'.format(n))

