valor = int(input('Insira o numer entre 0 a 9999: '))
u = valor // 1 % 10
d = valor // 10 % 10
c = valor // 100 % 10
m = valor // 1000 % 10
print(u)
print('unidade:  {}'.format(u))
print('dezena:   {}'.format(d))
print('centena:  {}'.format(c))
print('milhares: {}'.format(m))
