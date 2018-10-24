#!/usr/bin/python36
tabuada = int(input('Digiteum número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(tabuada, c, tabuada * c))

