print('-' * 20)
print('Sequencia de Fibonacci')
print('-' * 20)
termos = int(input('Quantos termos deseja mostrar? :'))
t1 = 0
t2 = 1
print('#'*50)
print('{} > {}'.format(t1, t2), end='')
cont = 3
while cont <= termos:
    t3 = t1 + t2  # t1=0 ; t2=1 ; t3=1
    print(' > {} '.format(t3), end='')
    cont = cont + 1
    t1 = t2  # t1 RECEBE t2
    t2 = t3  # t2 RECEBE t3
print('\nFim')
