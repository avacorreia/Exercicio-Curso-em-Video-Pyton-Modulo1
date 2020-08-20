import random
nome1 = input('insira o primeiro nome')
nome2 = input('insira o segundo nome')
nome3 = input('insira o terceiro nome')
nome4 = input('insira o quarto nome')
lista = [nome1, nome2, nome3, nome4]
print('O aluno escoljhido é o {}'.format(random.choice(lista)))
