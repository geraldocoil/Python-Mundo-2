from datetime import date
ano=int(input('Em que ano vc nasceu :'))
data=date.today().year
idade=data-ano
print('Quem nasceu em {} tem {} anos'.format(ano,idade))
if idade<=9:
    print('Classificacao: MIRIM')
elif idade<=14:
    print('Classificacao: INFANTIL')
elif idade<=19:
    print('Classificacao: JUNIOR')
elif idade<=25:
    print('Classificacao: SENIOR')
else:
    print('Classificacao: MASTER')
