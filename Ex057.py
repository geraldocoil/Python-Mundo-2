'''sexo=''
while sexo!='M' and sexo!='F':
    sexo = str(input('Sexo (M/F):')).strip().upper()
    if sexo!='M' and sexo!='F':
        print('Elemento Inválido, digite novamente...')
if sexo=='M':
    print('Sexo masculino registrado com sucesso')
if sexo=='F':
    print('Sexo feminino registrado com sucesso')
print('Cadastro completo')'''

sexo=str(input('Informe seu sexo [M/F]:')).strip()
while sexo not in 'MmFf':
    sexo=str(input('Dados inválidos.\nPor favor,informe seu sexo:')).strip()
    if sexo in 'Mm':
        print('Sexo masculino registrado com sucesso')
    if sexo in 'Ff':
        print('Sexo masculino registrado com sucesso')
print('Cadastro completo')
