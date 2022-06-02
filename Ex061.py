print('Gerador de PA')
print('-=-'*10)
a1=int(input('Primeiro termo: '))
r=int(input('Razão da PA: '))
termo=a1
cont=1
while cont<=10:
    print('{} > '.format(termo),end='')
    termo=termo+r
    cont=cont+1
print('Fim')