#!/usr/bin/python36
total = prod1000 = valorprodbarato = 0
prodbarato = ' '
while True:
    prod = str(input('Nome do Produto: '))
    valor = int(input('Preço: R$'))
    total += valor
    if valor > 1000:
        prod1000 += 1
    if valorprodbarato == 0 and prodbarato == ' ':
        prodbarato = prod
        valorprodbarato = valor
    elif valor < valorprodbarato:
        prodbarato = prod
        valorprodbarato = valor
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Contiuar? [S/N] ')).upper().strip()[0]
    if cont == 'N':
        break
print(f'O total da compra foi R${total}')
print(f'Temos {prod1000} produto(s) que custa(m) mais de R$1.000,00')
print(f'O produto mais barato foi {prodbarato} que custou {valorprodbarato}')

