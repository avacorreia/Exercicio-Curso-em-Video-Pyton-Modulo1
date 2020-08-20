import random
from time import sleep
print('-=-' * 20)
num = int(input('Pense num numero de 0 a 5: '))
print('processando...')
sleep(3)
if 0 < num > 6:
    print('O numero inserrido está fora do intervalo')
else:
    x = random.randint(0, 5)
    print('acertou' if num == x else 'Não acerto, o numero sorteado é o {}'.format(x))
print('Terminou o programa!')
print('-=-' * 20)
