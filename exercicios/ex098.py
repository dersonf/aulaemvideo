#!/usr/bin/python36
from time import sleep

def linha():
    print('-=' *30)

def contador(i, f, p):
    linha()
    if p < 0:
        p = p * (-1)
    if p == 0:
        print('Passo de 0 em 0, tá me zoando? Vai ser de 1 em 1!!!')
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i > f:
        p = p * (-1)
    for c in range(i, f+1, p):
        sleep(0.5)
        print(c, end=' ', flush=True)
    print('FIM!')

#Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
linha()
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)

