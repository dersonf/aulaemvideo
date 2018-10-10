#!/usr/bin/python36
n1 = float(input('Insira a PRIMEIRA nota: '))
n2 = float(input('Insira a SEGUNDA nota: '))
media = float((n1 + n2) /2)
if media >= 7:
    print('Sua média foi {:.1f}, você foi \033[1;32;44mAPROVADO\033[m!'.format(media))
elif media >= 5:
    print('Sua média foi {:.1f}, voce está de RECUPERAÇÃO!'.format(media))
else:
    print('Sua média foi {:.1f}, você foi \033[1;31;44mREPROVADO\033[m!'.format(media))
