l1=float(input('valor do primeiro lado:'))
l2=float(input('valor do segundo lado :'))
l3=float(input('valor do terceiro lado :'))
if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
    print('com os lados {}cm,{}cm,{}cm é possível formar um triângulo'.format(l1,l2,l3))
    if l1 == l2 == l3:
        print('O triângulo formado será EQUILÁTERO')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('O triângulo formado será ISÓSCELES')
    elif l1!=l2!=l3!=l1:
        print('O triângulo formado será ESCALENO')
else:
    print('{} É impossivel formar um triângulo com o comprimeto desses lados{}'.format('\033[31m','\033[m'))

