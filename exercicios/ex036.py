#!/usr/bin/python36
a = float(input('Valor da casa: R$'))
b = float(input('Salário do comprador: R$'))
c = int(input('Quantos anos de financiamento? '))
prestacao = a / (c * 12)
print('A prestação é de {:.2f}, 30% do salário é R${:.2f}.'.format(prestacao, b * 0.3))
if prestacao > b * 0.3:
    print('\033[1;31mEmprestimo NEGADO\033[m')
else:
    print('\033[1;32mEmprestimo APROVADO\033[m')
