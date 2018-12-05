#!/usr/bin/python36
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
coluna = linha = 0
while True:
    matriz[linha][coluna] = int(input(f'Digite o valor para [{linha}, {coluna}]: '))
    if coluna == 2 and linha == 2:
        break
    elif coluna == 2:
        linha += 1
        coluna = 0
    else:
        coluna += 1
print(f'''{matriz[2][0]:^5}{matriz[1][0]:^5}{matriz[0][0]:^5}
{matriz[2][1]:^5}{matriz[1][1]:^5}{matriz[0][1]:^5}
{matriz[2][2]:^5}{matriz[1][2]:^5}{matriz[0][2]:^5}''')

