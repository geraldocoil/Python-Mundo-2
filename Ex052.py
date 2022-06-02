n=int(input('Digite um número:'))
tot=0
cores={'vermelho':'\033[31m','amarelo':'\033[33m'}
for c in range(1,n+1):
    if n%c==0:
        print('\033[33m',end='')
        tot=tot+1
    else:
        print('\033[31m',end='')
    print('{}'.format(c),end=' ')
print('\n{}O número {} foi divisivel {} vezes'.format('\033[m',n,tot))
if tot==2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele NÃO é Primo')

