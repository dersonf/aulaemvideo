#!/usr/bin/python36
#import binary_repr
print('='*20)
print('Conversor binário, octal, hexadecimal')
print('='*20)
numero = int(input('Digite um número inteiro: '))
print('Digite 1 para converter em binário.')
print('Digite 2 para converter em octal.')
print('Digite 3 para converter em hexadecimal')
opcao = int(input('Digite a opção desejada: '))
if opcao == 1:
#    binary_repr(15)
    binario = bin(numero)
    print('O número {} em binário é {}'.format(numero, binario[2:]))
else:
    print('Ainda em contrução :(')
