#!/usr/bin/python36
abre = fecha = 0
expr = str(input('Digite a expressão: '))
for p in expr:
    if p == '(':
        abre += 1
    elif p == ')':
        fecha += 1
if abre == fecha:
    print('A expressão está correta')
else:
    print('A expressão está INCORRETA')

