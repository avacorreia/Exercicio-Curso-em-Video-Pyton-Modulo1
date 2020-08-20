a = int(input('Insira a 1ª reta: '))
b = int(input('Insira a 2ª reta: '))
c = int(input('Insira a 3ª reta: '))
if (abs(b - c) < a < (b + c)) and (abs(a - c) < b < (a + c)) and (abs(a - b) < c < (a + b)):
    print('As retas a, b e c podem formar um triangulo')
else:
    print('As reta a, b, e c não podem formar um triangulo')

