#!/usr/bin/python36
from datetime import date
maior = 0
menor = 0
ano = date.today().year
for c in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = ano - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
if maior > 0:
    print('Tivemos {} pessoa(s) maior(es) de idade'.format(maior))
if menor > 0:
    print('Tivemos {} pessoa(s) menor(es) de idade'.format(menor))

