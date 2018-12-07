#!/usr/bin/python36
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
tc = par = coluna = linha = 0
while True:
    matriz[linha][coluna] = int(input(f'Digite o valor para [{linha}, {coluna}]: '))
    if matriz[linha][coluna] % 2 == 0:
        par += matriz[linha][coluna]
    if coluna == 2:
        tc += matriz[linha][coluna]
    if coluna == 0 and linha == 1:
        maior =  matriz[linha][coluna]
    elif linha == 1 and matriz[linha][coluna] > maior:
        maior = matriz[linha][coluna] 
    if coluna == 2 and linha == 2:
        break
    elif coluna == 2:
        linha += 1
        coluna = 0
    else:
        coluna += 1
print('-='*30)
print(f'''{matriz[0][0]:^5}{matriz[0][1]:^5}{matriz[0][2]:^5}
{matriz[1][0]:^5}{matriz[1][1]:^5}{matriz[1][2]:^5}
{matriz[2][0]:^5}{matriz[2][1]:^5}{matriz[2][2]:^5}''')
print('-='*30)
print(f'A soma dos valors pares é {par}.')
print(f'A soma dos valores da terceira coluna é {tc}.')
print(f'O maior valor da segunda linha é {maior}.')

