#!/usr/bin/python36
impar = []
par = []
combinado = [par, impar]
for c in range(1, 8):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
par.sort()
impar.sort()
print(f'Os valores pares digitados foram: {combinado[0]}')
print(f'Os valores impares digitados foram: {combinado[1]}')

