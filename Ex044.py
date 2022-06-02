print('-=-' * 10)
print('{:=^60}'.format('LOJAS GERAIS'))

preco = int(input('Preco do produto R$:'))
escolha = int(input('''Qual a forma de pagamento?
[1]-A VISTA NO DINHEIRO/CHEQUE
[2]-A VISTA NO CARTÃO
[3]-EM ATÉ 2X NO CARTÃO
[4]-3X OU MAIS NO CARTÃO
Qual a sua opcão?:'''))
if escolha == 1:
    valor = preco - (preco * 10 / 100)
    print('Com 10% de desconto')
elif escolha == 2:
    valor = preco - (preco * 5 / 100)
    print('Com 5% de desconto')
elif escolha == 3:
    valor = preco
    print('Preco formal')
    print('Sua compra será parcelada em 2x de R${}'.format(preco / 2))
elif escolha == 4:
    parcelas = int(input('Quantas parcelas serão:'))
    valor = preco + (preco * 20 / 100)
    print('Com 20% de juros ')
    print('Sua compra de R${} será parcelada em {}x de R${:.1f} com juros de 20%'.format(preco, parcelas,
                                                                                         valor / parcelas))
else:
    valor = preco
    print('Opcao invalida,tente novamente')
print('o produto que custava R${} vai custar R${}'.format(preco, valor))
