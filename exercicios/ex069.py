#!/usr/bin/python36
pm18a = qtth = mm20a = 0
while True:
    idade = int(input('Digite a idade: '))
    if idade > 18:
        pm18a += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo:[M/F] ')).upper().strip()[0]
    if sexo == 'M':
        qtth += 1
    if sexo == 'F' and idade < 20:
        mm20a += 1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Continua:[S/N] ')).upper().strip()[0]
    if cont == 'N':
        break
if pm18a > 0:
    print(f'Foram cadastradas {pm18a} pessoa(s) maiores de 18 anos.')
if qtth > 0:
    print(f'Foram cadastrados {qtth} homen(s).')
if mm20a > 0:
    print(f'Foram cadastradas {mm20a} mulher(es) com menos de 20 anos.')

