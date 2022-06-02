maior = 0
menor = 0
for pessoas in range(1, 6):
    peso = float(input('Peso da {} pessoa:'.format(pessoas)))
    if pessoas == 1:#se for o 1 laco
        maior = peso
        menor = peso
    else:#analise dos lacos seguintes
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi {}Kg'.format(maior))
print('O menor peso lido foi {}Kg'.format(menor))
