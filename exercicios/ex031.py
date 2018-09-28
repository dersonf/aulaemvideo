#!/usr/bin/python36
distancia = int(input('Qual é a distância da sua viagem? '))
if distancia <= 200:
    print('Você viajou {}Km e será cobrado R${:.2f} nessa viagem.'.format(distancia, distancia * 0.50))
else:
    print('\033[4;34mAndou muito e ganhou desconto!\nVocê viajou {}Km, seu custo foi R${:.2f}.\033[m'.format(distancia, distancia * 0.45))
