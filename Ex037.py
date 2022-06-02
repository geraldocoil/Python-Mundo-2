n = int(input('Digite um número inteiro:'))
print('''escolha uma das bases para conversão:
[1] para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
escolha = int(input('Sua opcão:'))
if escolha == 1:
    print('{} convertido para BINARIO é igual a {}'.format(n, bin(n)[2:]))
elif escolha == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif escolha == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Opcao inválida, tente novamente')
