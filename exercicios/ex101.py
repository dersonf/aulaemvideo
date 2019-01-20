#!/usr/bin/python36
def voto(ano):
    from datetime import date

    anoatual = date.today().year
    idade = anoatual - nasc
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade <= 17 or idade > 70:
        return f'COM {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'

   
nasc = int(input('Difite o ano de nascimento: ')) 
print(voto(nasc))

