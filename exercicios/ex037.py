#!/usr/bin/python36
print('='*20)
print('Conversor binário, octal, hexadecimal')
print('='*20)
numero = int(input('Digite um número inteiro: '))
print('''Digite 1 para converter em binário.
Digite 2 para converter em octal.
Digite 3 para converter em hexadecimal''')
opcao = int(input('Digite a opção desejada: '))
if opcao == 1:
    print('O número {} em binário é {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('O número {} em octal é {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('O número {} em hexadecimal é {}'.format(numero, hex(numero)[2:].upper()))
else:
    print('O animal, é pra escolher entre 1 e 3, não sabe ler?')
