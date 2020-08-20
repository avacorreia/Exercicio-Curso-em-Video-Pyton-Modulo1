dias = int(input('Quantos dias: '))
km = float(input('Quantos km: '))
preco = dias * 60 + km * 0.15
if(dias == 0){
print('O valor a pagar é de : {:.2f} '.format(preco))
}

