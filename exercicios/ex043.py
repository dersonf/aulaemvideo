#!/usr/bin/python36
peso = float(input('Qual é o seu peso (Kg)? '))
altura = float(input('Qual é a sua altura? '))
imc = peso / (altura ** 2)
print('Com {}Kg e {}m seu IMC é {:.1f}.'.format(peso, altura, imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal!')
elif imc < 25:
    print('Você está com o PESO IDEAL.')
elif imc < 30:
    print('Você está com SOBREPESO. Fica esperto.')
elif imc < 40:
    print('Você está com OBESIDADE!')
else:
    print('Obesidade Mórbida')

