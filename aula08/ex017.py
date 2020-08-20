from math import hypot
from urllib.response import addbase

oposto = float(input('Insira o comprimento do cateto oposto: '))
adjacente = float(input('Insira o comprimento do cateto adjacente: '))
print('O valor da hipotonusa é: {:.2f}'.format(hypot(oposto, adjacente)))
