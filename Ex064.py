n=0
total=0
soma=0
while n!=999:
    n=int(input('Digite um número [999 para parar]:'))
    if n!=999:
        total=total+1
        soma+=n
print('A somas de todos os {} números que vc digitou foi {}'.format(total,soma))