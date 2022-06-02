n1=float(input('Primeira nota :'))
n2=float(input('Segunda nota :'))
media=(n1+n2)/2
print('Tirando a media entre {:.1f} e {:.1f} a media do aluno é {:.1f}'.format(n1,n2,media))
if media<=5.0:
    print('sua nota foi {}, menor do que 5.0'.format(media))
    print('{}Você foi reprovado{}'.format('\033[31m','\033[m'))
elif 5.0<media<=6.9:
    print('Sua nota foi {},maior do que 5.0'.format(media))
    print('{}Porém você está em recuperacão{}'.format('\033[33m','\033[m'))
else:
    print('Sua nota foi {}, maior do que 6.9'.format(media))
    print('{}Você foi aprovado{}'.format('\033[32m','\033[m'))
