#!/usr/bin/python36

import math
num = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(num))
cosseno = math.cos(math.radians(num))
tangente = math.tan(math.radians(num))
print('O ângulo de {} tem o SENO de {:.2f}'.format(num, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(num, cosseno))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(num, tangente))
