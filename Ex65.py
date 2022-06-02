n=1
soma=0
total=0
r='S'
maior=0
menor=0
while r in 'Ss':
    n=int(input('Digite um número:'))
    total=total+1
    soma=soma+n
    if total==1:
        maior=n
        menor=n
    if n>maior:
        maior=n
    if n<menor:
        menor=n
    r=str(input('Dejesa continuar [S/N]: '))
    if r not in 'SsNn':
        r=str(input('Resposta invalida, tente novamente [S/N]: '))
media=soma/total
print('A soma dos {} números digitados foi {}'.format(total,soma))
print('A média entre eles foi {}'.format(media))
print('O maior valor foi {}{}{} e o menor {}{}{}'.format('\033[32m',maior,'\033[m','\033[31m',menor,'\033[m'))
