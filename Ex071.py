# SIMULACAO DE UM CAIXA ELETRONICO:
'''print('-'*50)
print('{:^50}'.format('CAIXA ELETRONICO'))
print('-'*50)

n = int(input('Digite um valor R$:'))
unidade = n // 1 % 10 * 1
dezena = n // 10 % 10 * 10
centena = n // 100 % 10 * 100
milhar = n // 1000 % 10 * 1000
um = dez = vinte = cinquenta =0
print(unidade)
print(dezena)
print(centena)
print(milhar)
while True:
    um = unidade / 1
    if dezena / 10 % 2 == 0:
        vinte = dezena / 20
    else:
        dez = dezena / 10
    cinquenta = centena / 50+milhar / 50
    break
print('-'*50)
if um>0:
    print(f'Total de {um} notas de R$ 1')
if dez>0:
    print(f'Total de {dez} notas de R$ 10')
if vinte>0:
    print(f'Total de {vinte} notas de R$ 20')
if cinquenta>0:
    print(f'Total de {cinquenta} notas de R$ 50')'''
# OU

print('=' * 30)
print('{:^30}'.format('BANCO DO BRASIL'))
print('=' * 30)

valor = int(input('Valor a ser sacado R$:'))
ced = 50
nced = 0
while True:
    if valor >= ced:  # a cada ciclo retira o valor da cedula do valor total, até ser menor
        valor = valor - ced
        nced = nced + 1
    else:  # caso o valor lido seja menor doque o valor atual da cédula
        if nced > 0:
            print(f'{nced} de R${ced}')
        if ced == 50:  # se a cedula autal for de 50>20
            ced = 20
        elif ced == 20:  # se a cedula autal for de 20>10
            ced = 10
        elif ced == 10:  # se a cedula autal for de 10>1
            ced = 1
        nced = 0
        if valor == 0:
            break
print('=' * 30)
print('ACABOU,VOLTE SEMPRE')
