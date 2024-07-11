nome = 'Jessyca Diniz'
altura = 1.77
peso = 64
imc = peso/ (altura * altura) #peso / altura ** 2

#f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'{imc:.2f}'
print(linha_1)
print ('peso', peso, 'quilo e seu IMC é', linha_2 )