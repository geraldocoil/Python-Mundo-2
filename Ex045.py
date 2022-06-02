from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
jogador = int(input('''Suas opcões:
[0] PEDRA
[1] PAPEL
[2] TESOURA
Qual é a sua jogada?'''))
if jogador > 2:
    print('JOGADA INVÁLIDA')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!!')
    print('-=-' * 10)
    print('O computador jogou {}'.format(itens[computador]))
    print('O jogador jogou {}'.format(itens[jogador]))
    print('-=-' * 10)
    # Primeiro forma
    # if jogador==0 and computador==1 or jogador==1 and computador==2 or jogador==2 and computador==0:
    #    print('{}O COMPUTADOR ganhou{}'.format('\033[31m','\033[m'))
    # elif jogador==0 and computador==2 or jogador==1 and computador==0 or jogador==2 and computador==1:
    #   print('{}O JOGADOR ganhou{}'.format('\033[32m','\033[m'))
    # else:
    #    print('Empate')

    # Segunda forma
    if computador == 0:  # Computador jogou PEDRA
        if jogador == 0:
            print('empate'.upper())
        elif jogador == 1:
            print('jogador ganhou'.upper())
        elif jogador == 2:
            print('computador ganhou'.upper())

    elif computador == 1:  # Computador jogou PAPEL
        if jogador == 0:
            print('computador ganhou'.upper())
        elif jogador == 1:
            print('empate'.upper())
        elif jogador == 2:
            print('jogador ganhou'.upper())

    elif computador == 2:  # Computador jogou TESOURA
        if jogador == 0:
            print('jogador ganhou'.upper())
        elif jogador == 1:
            print('computador ganhou'.upper())
        elif jogador == 2:
            print('empate'.upper())
