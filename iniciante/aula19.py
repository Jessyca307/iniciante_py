"""
Faça um programa que peça ao usuário para digitar um número,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
entrada = input('Digite  um numero:')

if entrada.isdigit():
          entrada_int = int(entrada)
          par_impar = entrada_int % 2 == 0
          par_impar_texto = 'impar'

          if par_impar:
                  par_impar_texto = 'par'
          print(f'O númro {entrada_int} é {par_impar_texto}')
else:
        print('Você não digitou um número inteiro')



try:
          entrada_int = int(entrada)
          par_impar = entrada_int % 2 == 0
          par_impar_texto = 'impar'

          if par_impar:
                  par_impar_texto = 'par'
          print(f'O númro {entrada_int} é {par_impar_texto}')
except:
        print('Você não digitou um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseado-se no horário 
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
time = input('Digite a hora em números inteiros. ')
try:
          hora = int(entrada)

          if hora >= 0 and hora <= 11:
                    print('Bom dia!')
          elif hora >= 12 and hora <= 17:
                    print('Boa tarde!')
          elif hora >= 18 and hora <= 23:
                    print('Boa noite!')
except:
        print('Não conheço essa hora!')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver
4 letras ou menos escreva "Seu nofme é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva " Seu nome é muito grande".
"""
nome = input('Digite seu nome: ')
tamanho = len(nome)

if tamanho > 1:
          if tamanho <= 4:
                print('Seu nome e muito curto!')
          elif tamanho >= 5 and tamanho <= 6:
                  print('Seu nome é normal!')
          else:
                  print('Seu nome e muito grande!')
else:
        print('Digite mais de uma letra!')
