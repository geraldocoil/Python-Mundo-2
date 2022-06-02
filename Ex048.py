soma = 0
cont=0
for c in range(1, 501, 2):
    if c % 3 == 0:
    #cont=cont+1 #conta todos os números impares
        cont=cont+1 #conta somentes os números impares, que sao divisiveis por 3
        soma=soma+c
print('A soma entre todos os {} números impares e \n multiplos de 3 é igual a {}'.format(cont,soma))
