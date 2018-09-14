#!/usr/bin/python36
# Exercicio 016

d = int(input('Quantos dias alugados? '))
k = int(input('Quantos Km rodados? '))
dd = 60
km = 0.15
print('O carro foi utilizado por {} dias e rodou {} Km que custou R${:.2f}'.format(d, k, ((d * dd) + (k * km))))
