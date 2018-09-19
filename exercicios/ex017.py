#!/usr/bin/python36

import math
c_oposto = float(input('Digite o cateto oposto: '))
c_adjacente = float(input('Digite o cateto adjacente: '))
print('A hipotenusa é {:.2f}.'.format(math.hypot(c_oposto, c_adjacente)))
