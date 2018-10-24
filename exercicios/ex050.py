#!/usr/bin/python36
soma = 0
count = 0
for n in range(1, 7):
    numero = int(input('Digite o valor {}/6: '.format(n)))
    if numero % 2 == 0:
        soma += numero
        count += 1
print('A soma dos {} números PARES é {}'.format(count, soma))

