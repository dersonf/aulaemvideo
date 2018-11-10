#!/usr/bin/python36
while True:
    tabuada = int(input('Qual tabuada deve ser exibida: '))
    if tabuada <= 0:
        break
    for c in range(1, 11):
        print(f'{tabuada} x {c} = {tabuada*c}')
print('Programa finalizado!!!')

