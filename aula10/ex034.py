salario = float(input('Qual o seu salário: '))
if salario >= 1250:
    print('Teve um aumento de 10%, o seu salario atual é de: {}'.format(salario+(salario*10/100)))
else:
    print('Teve um aumento de 15%, o seu salario atual é de: {}'.format(salario+(salario*15/100)))
