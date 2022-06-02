cont = 0
soma = 0
maior = 0
velho=0
menor = 0
novo=0
for pess in range(1, 5):
    print('----------{} PESSOA----------'.format(pess))
    nome = str(input('Nome :')).lower().strip()
    idade = int(input('Idade :'))
    sexo = str(input('Sexo :')).strip()
    soma = soma + idade  # soma todas as idades
    if sexo in 'Ff' and idade < 20:
        cont = cont + 1  # contabiliza as mulheres menores de 20 anos
    if sexo in 'Mm' and pess == 1:
        maior = idade
        velho=nome
        menor = idade
        novo=nome
    elif sexo in 'Mm' and pess!=1:
        if idade > maior:
            maior = idade
            velho=nome
        if idade < menor:
            menor = idade
            novo=nome
media = soma / (pess + 1)
print('A idade média do grupo é de {} anos'.format(media))
if cont>1:
    print('No grupo há {} mulheres menores de 20 anos'.format(cont))
elif cont==0:
    print('No grupo não há mulheres menores de 20 anos')
else:
    print('No grupo há {} mulher menor de 20 anos'.format(cont))
print('O {} é o homem mais velho e tem {} anos'.format(velho,maior))
print('O {} é o homem mais novo e tem {} anos'.format(novo,menor))
