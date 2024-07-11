"""
Calculadora com while
"""

while True:
          
        numer_1 = input('Digite um numero: ')
        numer_2 = input('Digite outro numero: ')
        operador = input('Digite o operador (+-/*): ')
        numeros_validos = None

        numero_1_float = float(numer_1)
        numero_2_float = float(numer_2)
          
        try:
                  numero_1_float = float(numer_1)
                  numero_2_float = float(numer_2)
                  numeros_validos = True
        except:
                  numeros_validos = None


        if numeros_validos is None:
                  print('um ou ambos os numeros digitados são inválidos.')
                  continue

        operadores_permitidos = '+-/*'

        if operador not in operadores_permitidos:
                  print('Operador invalido.')
                  continue

        if len(operador) > 1:
                  print('Digite apenas um operador.')
                  continue

        print('Realizando sua conta. Confira o resultado abaixo:')

        if operador == '+':
                 print(f'{numero_1_float} + {numero_2_float}=', numero_1_float + numero_2_float)
        elif operador == '-':
                 print(f'{numero_1_float} - {numero_2_float}=', numero_1_float - numero_2_float)
        elif operador == '/':
                 print(f'{numero_1_float} / {numero_2_float}=', numero_1_float / numero_2_float)
        elif operador == '*':
                 print(f'{numero_1_float} * {numero_2_float}=', numero_1_float * numero_2_float)
        else:
                  print('Nunca deveria chegar aqui.')
                  
        sair = input('Quer sair? [s]sim: ').lower().startswith('s')
          

        if sair is True:
                  break