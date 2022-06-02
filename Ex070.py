print('-'*20)
print('{:^10}'.format('Lojas Baratao'))
print('-'*20)
total=menor=caro=prod=0
barato= ''
while True:
    produto=str(input('Nome do Produto :')).strip().capitalize()
    prod+=1
    preco=int(input('Preco R$:'))
    total+=preco#total da compra
    escolha=' '
    while escolha not in 'SsNn':
        escolha = str(input('Deseja continuar [S/N] :'))[0]
    if preco>1000:#produtos mais caros q R$1000
        caro+=1
    if prod==1:
        menor=preco
    else:
        if preco<menor:
            menor=preco
            barato=produto
    if escolha in 'Nn':
        print('-=-'*20)
        print('Fim do programa')
        break
print(f'Total da compra : R${total:.2f}')
print(f'Produtos que custam mais de R$1000 : {caro}')
print(f'Produto mais barato : {barato} que custa R${menor:.2f}')

