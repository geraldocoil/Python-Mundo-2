maior=homem=mulher=0
while True:
    idade=int(input('Idade :'))
    sexo=' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo [M/F]:'))[0]
    cont=' '
    while cont not in 'SsNn':
        cont = str(input('Deseja continuar [S/N]'))[0]
    if idade>=18:
        maior+=1
    if sexo in 'Mm':
        homem+=1
    if sexo in 'Ff' and idade<20:
        mulher+=1
    print('-=-'*20)
    if cont in 'Nn':
        print('Programa encerrado')
        break
print(f'Foram registrados {maior} pessoas com mais de 18 anos')
if homem==1:
    print(f'Foi registrado {homem} homem')
else:
    print(f'Foram registrados {homem} homens')
if mulher==1:
    print(f'Foi registrado {mulher} mulher com menos de 20 anos')
else:
    print(f'Foram registrados {mulher} mulheres com menos de 20 anos')
