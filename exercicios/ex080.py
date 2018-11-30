#!/usr/bin/python36
lista = []
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num >= lista[-1]:
        lista.append(num)
        print('Adicionado no final')
    elif num <= lista[0]:
        lista.insert(0, num)
        print('Adicionado no inicio da lista.')
    else:
        for pos, valor in enumerate(lista):
            if num <= valor:
                lista.insert(pos, num)
                print(f'Adicionado na posição {pos}.')
                break
print(lista)

