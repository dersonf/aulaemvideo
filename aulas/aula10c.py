#!/usr/bin/python36
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('Sua nota foi {:.1f}.'.format(m))
if m >= 6:
    print('Você passou de ano!')
else:
    print('Você foi reprovado!')
