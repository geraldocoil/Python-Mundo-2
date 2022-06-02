s=0
cont=0
for c in range(1,7):
    n=int(input('Digite o {} número:'.format(c)))
    if n%2==0:
        cont=cont+1
        s+=n
    if n%2!=0:
        print('O número é impar')
print('A soma dos {} números pares é {}'.format(cont,s))