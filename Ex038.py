n1=int(input('Digite um número :'))
n2=int(input('Digite outro número :'))
if n1>n2:
    print('O PRIMEIRO número {} é o {}maior{}'.format(n1,'\033[4;32m','\033[m'))
elif n2>n1:
    print('O SEGUNDO número {} é o {}maior{}'.format(n2,'\033[4;32m','\033[m'))
elif n1==n2:
    print('Ambos os valores são {}iguais'.format('\033[4;33m'))


