#!/usr/bin/python36
lista = []
par = []
impar = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
    cont = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if cont == 'N':
        break
print('-='*30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')

