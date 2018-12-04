#!/usr/bin/python36
pessoa = list()
pessoas = list()
pesado = leve = contador = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(int(input('Peso: ')))
    if contador == 0:
        leve = pesado = pessoa[1]
    elif pessoa[1] < leve:
        leve = pessoa[1]
    elif pessoa[1] > pesado:
         pesado = pessoa[1]
    contador +=1
    pessoas.append(pessoa[:])
    pessoa.clear()
    cont = str(input('Continua: [S/N]')).upper().strip()[0]
    if cont == 'N':
        break
print('-=' * 30)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso é {pesado}Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == pesado:
        print(f'{p[0]}', end=' ')
print()
print(f'O menor peso é {leve}Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == leve:
        print(f'{p[0]}', end=' ')
print()

