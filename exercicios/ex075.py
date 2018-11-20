#!/usr/bin/python36
num = (int(input('Digite o 1 valor de 4: ')),
    int(input('Digite o 2 valor de 4: ')),
    int(input('Digite o 3 valor de 4: ')),
    int(input('Digite 0 último valor: ')))
print(f'O número 9 apareceu {num.count(9)} veze(s).')
if 3 in num:
    print(f'O número 3 aparece a primeira vez na posição {num.index(3)}.')
else:
    print('O número 3 não apareceu :(')
print('Os números pares foram: ',end = '')
for c in num:
    if c % 2 == 0:
        print(c,end = ' ')
print()
