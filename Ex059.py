n1=int(input('Digite um número: '))
n2=int(input('Digite outro número: '))
menu=0
while menu!=5:
    menu=int(input('''Escolha sua operacão:
[1]-somar
[2]-multiplicar
[3]-maior
[4]-novos números
[5]-sair do programa
>>>'''))
    if menu>5:
        print('Operacao inválida')
    if menu==1:
        soma=n1+n2
        print('A soma de {} e {} é {}'.format(n1,n2,soma))
    elif menu==2:
        mult=n1*n2
        print('O produto de {} e {} é {}'.format(n1,n2,mult))
    elif menu==3:
        if n1>n2:
            print('{}>{}'.format(n1,n2))
            print('{} é maior q {}'.format(n1,n2))
        elif n2>n1:
            print('{}>{}'.format(n2,n1))
            print('{} é maior q {}'.format(n2,n1))
        else:
            print('Ambos os valores são iguais a {}'.format(n1 or n2))
    elif menu==4:
        print('Informe os valores novamente')
        n1=int(input('Digite um novo valor:'))
        n2=int(input('Digite um outro novo valor:'))
    print('-=-'*10)
print('Fim do programa')