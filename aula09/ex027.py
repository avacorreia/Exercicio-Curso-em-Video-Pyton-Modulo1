nome = str(input('Insira o nome completo: ')).strip()
lista = nome.split()
print("O nome é {} o apelido é {} ".format(lista[0], lista[len(lista)-1]))
