#!/usr/bin/python36
print('='*30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('='*30)
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for c in range(0, 10):
    print('{} -> '.format(n), end = '')
    n += r
print('ACABOU')

