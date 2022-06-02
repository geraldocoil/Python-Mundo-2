n = int(input('Primeiro termo:'))
r = int(input('Qual é a razão:'))
a10 = n + (10 - 1) * r
for c in range(n, a10 + r, r):
    print(c, end=' ')

