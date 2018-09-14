#!/usr/bin/python36

m = float(input('Digite a quantidade em metros: '))
print('A medida de {}m corresponde a:'.format(m))
print('{}km'.format(m/1000))
print('{}hm'.format(m/100))
print('{}dam'.format(m/10))
print('{:.0f}dm'.format(m*10))
print('{:.0f}cm'.format(m*100))
print('{:.0f}mm'.format(m*1000))
