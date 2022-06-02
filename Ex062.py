'''n1=int(input('Primeiro termo: '))
r=int(input('Razão: '))
termo=n1
cont=1

while cont<=10:
    print('{}'.format(termo),end='')
    print(' > 'if cont<10 else ' PAUSA',end='')
    termo=termo+r
    cont=cont+1
    if cont>10:
        novos=int(input('\nDeseja adicionar quantos novos termos? :'))
        while novos!=0:
            print('{}'.format(termo),end='')
            print(' > ' if novos>1 else ' PAUSA',end='')
            termo=termo+r
            novos=novos-1
            if novos==0:
                novos=int(input('\nDeseja adicionar quantos novos termos? :'))

print('Fim')'''

#Gerador de PA,calculando o número total de termos
print('GERADOR DE PA')
print('-=-' * 10)
n1 = int(input('Primeiro termo da PA:'))
razao = int(input('Razao da PA: '))
cont = 1
termo = n1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} > '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Deseja adicionar quantos termos? :'))
print('Fim')
print('Progresão finalizada com {} termos'.format(total))
