#!/usr/bin/python36
def escreva(msg):
    print('~' * (len(msg)+4))
    print(f'  {msg}')
    print('~' * (len(msg)+4))


mensagem = str(input('Digite uma mensagem: '))
escreva(mensagem)

