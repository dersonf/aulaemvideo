#!/usr/bin/python36
print('='*30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('='*30)
c = 11
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
t = 0
while c != 0:
    print('{} -> '.format(n), end='')
    n += r
    c -= 1
    t += 1
    if c == 1:
        print('PAUSA')
        c = int(input('Quantos termos você quer mostrar a mais? '))
        if c > 0:
            c = c+1
print('Progressão finalizada com {} termos mostrados'.format(t))

