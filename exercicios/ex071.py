#!/usr/bin/python36
nota50 = nota20 = nota10 = nota1 = 0
valor = int(input('Que valor quer sacar? R$'))
while True:
    if valor >= 50:
       nota50 += 1
       valor = valor - 50
    elif valor >= 20:
       nota20 += 1
       valor = valor - 20
    elif valor >= 10:
       nota10 += 1
       valor = valor -10
    elif valor >= 1:
       nota1 +=1
       valor = valor -1
    else:
       break
print('='*30)
print(f'Total de {nota50} cédulas de R$50')
print(f'Total de {nota20} cédulas de R$20')
print(f'Total de {nota10} cédulas de R$10')
print(f'Total de {nota1} cédulas de R$1')

