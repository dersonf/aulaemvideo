#!/usr/bin/python36

import math
import emoji
n = int(input('Digite um número: '))
raiz = math.sqrt(n)
print('A raiz de {} é igual a {}'.format(n, raiz))
print('A raiz de {} é igual a {}'.format(n, math.ceil(raiz)))
print('A raiz de {} é igual a {}'.format(n, math.floor(raiz)))
print(emoji.emojize('Python é :smile:'))
