#!/usr/bin/python36
from random import sample
numeros = tuple(sample(range(1,11), k=5))
print('O valores sorteados foram: ', end = '')
for c in (numeros):
    print(c,end = ' ')
print(f'\nO maior número sorteado foi {sorted(numeros)[-1]}')
print(f'O menor número sorteado foi {sorted(numeros)[0]}')

