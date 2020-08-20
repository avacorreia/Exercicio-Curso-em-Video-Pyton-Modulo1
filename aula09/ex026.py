frase = str(input('Insira uma frase: ')).strip()
print('Existe {} "A" '.format(frase.count('a')))
print('A posição que ela aparece a primeira vez, é na posição: {}'.format(frase.upper().find('A')+1))
print('A posição que ela aparece a última vez, é na posição: {}'.format(frase.upper().rfind('A')+1))
