#!/usr/bin/python36
salario = float(input('Qual é o salário do funcionário? R$'))
if salario >= 1250:
    print('Quem ganhava \033[1;32;44mR${:.2f}\033[m passa a ganhar \033[1;32;44mR${:.2f}\033[m agora.'.format(salario, salario * 1.10))
else:
    print('Quem ganhava \033[1;32;44mR${:.2f}\033[m passa a ganhar \033[1;32;44mR${:.2f}\033[m.'.format(salario, salario * 1.15))
