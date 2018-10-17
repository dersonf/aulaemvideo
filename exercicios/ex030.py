#!/usr/bin/python36
numero = int(input('Me diga um numero qualquer: '))
teste = numero%2
if teste == 0:
    print('O número {} é PAR.'.format(numero))
else:
    print('O número {} é IMPAR.'.format(numero))
