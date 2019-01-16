#!/usr/bin/python36
def maior(* numeros):
    print('-=' * 20)
    print('Analisando os valores')
    for i in numeros:
        print(i, end=' ')
    print(f'\nO maior número é {max(numeros)}.')

maior(4, 5, 15)
maior(9, 3, 6, 3, 2)
