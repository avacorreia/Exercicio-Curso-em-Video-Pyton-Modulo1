import datetime
ano = int(input('Insira o ano: '))
if ano == 0:
    ano = datetime.datetime.now().year
if ano % 400 and ano != 0 and ano % 4 == 0 and ano % 100:
    print(ano)
    print('O ano é bissexto.')
else:
    print(ano)
    print('O ano não é bissexto.')
