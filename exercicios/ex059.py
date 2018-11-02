#!/usr/bin/python36
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = ''
while opcao != 5:
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    opcao = int(input('Digite a opção: '))
    if opcao == 1:
        print('\nA soma de {} e {} é {}'.format(n1, n2, n1+n2))
        print('{}'.format('='*30))
    if opcao == 2:
        print('\nA multiplicação entre {} e {} é {}'.format(n1, n2, n1*n2))
        print('{}'.format('='*40))
    if opcao == 3:
        if n1 > n2:
            print('\nO maior número é {}'.format(n1))
        elif n1 == n2:
            print('\nOs números são os mesmos, {}'.format(n1))
        else:
            print('\nO maior número é {}'.format(n2))
        print('{}'.format('='*30))
    if opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    if opcao > 5:
        print('\033[1;31;46m\nOpção incorreta!!! Escolha novamente.\033[m')
print('FIM')

