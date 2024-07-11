"""
CPF: 746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

ex.: (746824890)
   10  9  8  7  6  5  4  3  2
   7   4  6  8  2  4  8  9  0
   70 36 48 56 12 20 32 27  0

   Somar todos os resultados:
   70+36+48+56+12+20+32+27+0
   Multiplicar o resultado anterior por 10
   301*10 = 3010
   obter o resto da divisão da conta anterior por 11
   3010 % 11 = 7
   se o resultado anterior for maior que 9:
   resultado é 0
   contrario disso:
   Resultado é o valor da conta

O primeiro digito do CPF é 7
"""
import re
import sys

entrada = input('CPF 746.824.890-70:  ')#.replace('.', '').replace('-','')
cpf = re.sub( r'[^0-9]', 
'', 
entrada)
enterr = entrada == entrada[0] * len(entrada)

if enterr:
        print('Você enviou dados sequenciais')
        sys.exit()

nove_digitos = cpf[:9]
contador_r = 10

resultado = 0
for digito_ in nove_digitos:
          resultado += int(digito_) * contador_r
          contador_r -= 1

digito_2 = (resultado * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

dez_digitos = nove_digitos + str(digito_2)
contador_r_2 = 11

resultado_2 = 0
for digito in dez_digitos:
          resultado_2 += int(digito) * contador_r_2
          contador_r_2 -= 1

digito_3 = (resultado_2 * 10) % 11
digito_3 = digito_3 if digito_3 <= 9 else 0
novo_cpf = str(digito_2) + str(digito_3)
digito_final = int(novo_cpf)
print(digito_final)

cpf_gerado_p_c = f'{nove_digitos}{digito_2}{digito_3}'

if cpf == cpf_gerado_p_c:
        print(f'{cpf} é valido')

else: 
        print('CPF invalido')