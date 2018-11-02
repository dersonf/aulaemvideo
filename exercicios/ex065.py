#!/usr/bin/python36
maior = c = total = 0
cont = 'S'
while cont == 'S':
    n = int(input('Digite um número: '))
    if c == 0:
        menor = n
    elif n < menor:
        menor = n
    if n > maior:
        maior = n
    c += 1
    total += n
    cont = input('Continua? [S/N]').strip().upper()
    while cont not in 'SN':
        print('Valor incorreto, digite S ou N')
        cont = input('Continua? [S/N]').strip().upper()
media = total/n
print('Você digitou {} número(s), a média foi {}'.format(c, media))
print('O maior valor foi {} e o menor {}'.format(maior, menor))

