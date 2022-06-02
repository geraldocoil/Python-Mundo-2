casa = float(input('Valor da casa R$:'))
s = float(input('Sálario do comprador R$:'))
anos = int(input('Em quantos anos de finaciamento :'))

valor=casa/(anos*12)
print('para financiar uma casa de R${} em {} meses é necessário pagar um valor de R${:.1f} por mês'.format(casa,anos*12,valor))
if valor>=(s*30/100):
    print('a prestacão mensal ultrapassou o limite ')
    print('Seu emprestimo foi {}Negado{}'.format('\033[1;31m','\033[m'))
else:
    print('Seu empréstimo foi {}concedido{}'.format('\033[32m','\033[m'))
print('Volte sempre')

