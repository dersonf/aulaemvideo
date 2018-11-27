#!/usr/bin/python36
valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {c}: ')))
print(f'Você digitou os valores {valores}')
mm = ('maior', max(valores), 'menor', min(valores))
for p, f in enumerate(mm):
    if p % 2 == 0:
        print(f'O {f} valor digitado foi {mm[p+1]} na(s) posiçõe(s)', end = ' ')
        for pos, v in enumerate(valores):
            if v == mm[p+1]:
                print(f'{pos}...', end = ' ')
        print()

