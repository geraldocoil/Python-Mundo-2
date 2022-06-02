from random import randint

print('EU VOU PENSAR EM UM NÚMERO entre 0 e 10, TENTE ADIVINHAR!!!!')
#jogador = 0
jg = 0
computador = randint(0, 10)
print(computador)

'''while jogador != computador:
    jogador = int(input('Seu palpite? :'))
    if jogador >computador:
        print('Menos...')
    if jogador<computador:
        print('Mais...')
    if jogador != computador:
        print('Vc errou, TENTE NOVAMENTE!!!')
        jg = jg + 1
    if jogador == computador:
        print('O jogador GANHOU')
        jg=jg+1'''

acertou=False
while not acertou:
    jogador=int(input('Qual o seu palpite...:'))
    if jogador==computador:
        acertou=True
        jg=jg+1
    if jogador!=computador:
        jg=jg+1
        if jogador>computador:
            print('Menos....')
        if jogador<computador:
            print('Mais')
        print('Voce ERROU,Tente novamente')
if jg==1:
    print('VC ACERTOU DE PRIMEIRA')
print('Parabens você acertou mas foram necessários {} tentativas para acertar'.format(jg))



