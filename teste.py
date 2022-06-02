print('=' * 40)
print('{:^40}'.format('BANCO BRASIL'))
print('=' * 40)

valor = int(input('Valor que deseja sacar R$ :'))
total=valor
cedula = 50
totced=0
while True:
    if total>=cedula:
        total-=cedula
        totced+=1
    else:
        if totced>0:
            print(f'Total de {totced} cedulas de R${cedula}')
        if cedula==50:
            cedula=20
        elif cedula==20:
            cedula=10
        elif cedula==10:
            cedula=1
        totced=0
        if valor==0:
            break
print('='*30)
print('Fim do Programa,TENHA UM BOM DIA')
