frase=str(input('Digite uma frase:')).upper().strip()
palavras=frase.split()
junto=''.join(palavras)#excluindo os espacos entre as palavras
print('você digitou a frase {}'.format(junto))
inverso=''
#inverso=junto[::-1] #Lendo de trás para a frente
#ou
for letra in range(len(junto)-1,-1,-1): #Lendo de tras para a frente
    inverso=inverso+junto[letra]
print('O inverso de {} é {}'.format(junto,inverso))
if junto==inverso:
    print('TEMOS UM PALINDROMO')
else:
    print('NÃO É PALINDROMO')
