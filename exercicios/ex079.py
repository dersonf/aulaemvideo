#!/usr/bin/python36
lista = []
while True:
    num = int(input('Digite um valor: '))
    if num in lista:
        print('Número repetido na lista...')
    else:
        lista.append(num)
    cont = str(input('Continua[S/N]: ')).upper().strip()
    while cont not in 'SN':
        cont = str(input('Continua[S/N]: ')).upper().strip()
    if cont == 'N':
        break
print('='*30)
lista.sort()
print(f'Você digitou os valores {lista}')
