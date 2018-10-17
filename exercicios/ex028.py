#!/usr/bin/python36

import random
import time
c = int(random.randint(0, 5))
#print(c)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar')
print('-=-'*20)
p = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
time.sleep(2)
if p == c:
    print('Você acertou')
else:
    print('Errrrrooooou, eu pensei no número {}.'.format(c))
