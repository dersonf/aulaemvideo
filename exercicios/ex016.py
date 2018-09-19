#!/usr/bin/python36

from math import trunc
num = float(input('Digite um número qualquer: '))
print('O número inteiro do número {} é {}'.format(num, trunc(num)))
print('O número inteiro do número {} é {:.0f}'.format(num, num))
