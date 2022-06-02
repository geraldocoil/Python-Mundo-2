from random import randint
print('-=-'*20)
print('VOU ESCOLHER UM NÚMERO ENTRE 0 E 10, E VAMOS JOGAR PAR OU IMPAR!!!!')
print('-=-'*20)
computador= randint(0,10)
vitorias=0
while True:
    jogador=int(input('Escolha um número :'))
    escolha = str(input('Par ou Impar [P/I]:'))
    if escolha not in 'PpIi':
        escolha = str(input('Par ou Impar [P/I]:'))
    total=computador+jogador
    print('-=-' * 20)
    if total%2==0:
        if escolha in 'Pp':
            print('O jogador ganhou')
            print(f'O jogador jogou {jogador} e o computador jogou {computador}, e o total foi {total}, deu PAR')
            vitorias+=1
        if escolha in 'Ii':
            print('O computador ganhou,GAME OVER')
            print(f'O jogador jogou {jogador} e o computador {computador} e o total foi {total},deu PAR')
            break
    if total%2!=0:
        if escolha in 'Ii':
            print('O jogador ganhou')
            print(f'O jogador jogou {jogador} e o computador {computador} o total foi {total}, deu IMPAR')
            vitorias += 1
        if escolha in 'Pp':
            print('O computador ganhou,GAME OVER')
            print(f'O jogador jogou {jogador} e o computador {computador} e o total foi {total}, deu IMPAR')
            break
    print('-=-'*20)
    computador = randint(0, 10)
print('O jogo acabou')
print(f'Você venceu {vitorias} vezes seguidas')
