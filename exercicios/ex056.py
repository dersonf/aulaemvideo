#!/usr/bin/python36
totidade = 0
velho='wsaqe'
idadevelho = 0
mulmenor20 = 0
mulher = 0
for c in range(1, 5):
    n = str(input('Nome da {}ª pessoa: '.format(c)))
    i = int(input('Idade: '))
    s = str(input('Sexo(M/F): ')).upper()
    totidade += i
    if s == 'M' and velho == 'wsaqe':
        velho = n
        idadevelho = i
    if s == 'M' and i > idadevelho:
        velho = n
        idadevelho = i
    if s == 'F' and i < 20:
        mulmenor20 += 1
    if s == 'F':
        mulher += 1
print('A média de idade do grupo é {:.1f}'.format(totidade / 4))
if velho != 'wsaqe':
    print('O homem mais velho chama-se {} e possui {} anos'.format(velho, idadevelho))
else:
    print('Não há homens cadastrados!!!')
if mulmenor20 != 0:
    print('No grupo há {} mulher(es) com menos de 20 anos.'.format(mulmenor20))
elif mulher > 0:
    print('Só tem mulherão.')
else:
    print('Grupinho sem vergonha, não tem uma mulher')

