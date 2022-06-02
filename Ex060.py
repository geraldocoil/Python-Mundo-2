
from math import factorial
n=int(input('Digite um número para calcular seu fatorial:'))

#CALCULANDO FATORIAL COM (MODULO)
'''f=factorial(n)
print('O fatorial de {} é {}'.format(n,f))'''

c=n
f=1

#CALCULANDO FATORIAL COM (WHILE)
'''print('Calculando o fatoral de {}! ='.format(n),end='')
while c>0:
    print('{}'.format(c),end='')
    print(' x ' if c>1 else ' = ',end='')
    f=f*c
    c=c-1
print(f)'''


#CALCULANDO FATORAL COM (FOR)
print('Calculando o fatorial de {}! = '.format(n),end='')
for c in range(n,0,-1):
    print('{}'.format(c),end='')
    print(' * ' if c>1 else ' = ',end='')
    f=f*c
print(f)
