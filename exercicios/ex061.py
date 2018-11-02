#!/usr/bin/python36
print('='*30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('='*30)
c = 10
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
while c != 0:
    print('{} -> '.format(n), end='')
    n += r
    c -= 1
print('ACABOU')

