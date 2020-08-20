dist = int(input('Insira a distancia que pretende viaja: '))
if dist <= 200:
    print('O valor é de: {:.2f}'.format(0.5*dist))
else:
    print('O valor é de: {:.2f}'.format(0.45*dist))
