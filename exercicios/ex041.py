#!/usr/bin/python36
from datetime import date
nasc = int(input('Ano de nascimento: '))
ano = date.today().year
idade = int(ano - nasc)
print('O atleta possui {} anos.'.format(idade))
if idade <= 9:
    print('Está na categoria MIRIM.')
elif idade <= 14:
    print('Está na categoria INFANTIL.')
elif idade <= 19:
    print('Está na categoria JÚNIOR.')
elif idade <= 25:
    print('Está na categoria SÊNIOR.')
else:
    print('Está na categoria MASTER.')

