import math
ang = float(input('Insira um angulo: '))
rad = math.radians(ang)
sen = math.sin(rad)
cos = math.cos(rad)
tag = math.tan(rad)
print('O valor do angulo {} em: \nsen {:.2f}, \ncos {:.2f} \ntangente é {:.2f} '.format(ang, sen, cos, tag))