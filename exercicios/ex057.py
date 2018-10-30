#!/usr/bin/python36
sexo = input('Sexo [M/F]: ').upper().strip()
while sexo not in 'MF':
    print('ERRO! Digite o sexo corretamente.')
    sexo = input('Sexo [M/F]: ').upper().strip()
if sexo == 'M':
    print('É um menino.')
else:
    print('É uma menina.')

