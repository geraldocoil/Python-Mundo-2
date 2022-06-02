from datetime import date
menor=0
maior=0
hj = date.today().year
for pessoas in range(1,8):
    ano=int(input('Ano de nascimento da {} pessoa:'.format(pessoas)))
    idade=hj-ano
    print(idade,'anos')
    if idade>=21:
        maior=maior+1
    else:
        menor=menor+1
print('das {} pessoas, {} são MAIORES DE IDADE'.format(pessoas,maior))
print('e, {} sao MENORES DE IDADE'.format(menor))
