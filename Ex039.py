from datetime import date
nasc=int(input('Em que ano vc nasceu:'))
data=date.today().year
idade=data-nasc
print('Quem nasceu em {} tem {} anos'.format(nasc,idade))
if idade<18:
    falta=18-idade
    print('Ainda vai se alistar')
    print('Faltam {} anos para poder se alistar'.format(falta))
    ano=nasc+18
    print('O seu alistamento será em {}'.format(ano))
elif idade==18:
    print('Deve se alistar IMEDIATAMENTE')
elif idade>18:
    passou=idade-18
    print('Já deveria ter se alistado')
    print('Se passaram {} anos desde o período que deveria se alistar'.format(passou))
    ano=nasc+18
    print('Seu alistamento foi em {}'.format(ano))
