#!/usr/bin/python36
from sys import exit
print('{:=^40}'.format(' LOJAS FERNEDA '))
valor = float(input('Valor da compra: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
pagamento = int(input('Qual é a opção? '))
if pagamento == 1:
    vt = valor * 0.90
elif pagamento == 2:
    vt = valor * 0.95
elif pagamento == 3:
    vt = valor
elif pagamento == 4:
    vt = valor * 1.2
    parcelas = int(input('Quantas parcelas: '))
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas, vt / parcelas))
else:
    print('Opção incorreta, escolha entre as opção oferecidas.')
    exit()
print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(valor, vt))

