#!/usr/bin/python36
n = total = 0
c = -1
while n != 999:
   c += 1
   total += n
   n = int(input('Digite um número [999 para parar]: '))
print('Foram digitados {} número(s) e a soma deles é {}'.format(c, total))
print('OBS: Na soma não é contemplado o 999.')

