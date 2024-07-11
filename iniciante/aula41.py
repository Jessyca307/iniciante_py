"""
Operação ternária(condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""
condicao = 10 == 11
variavel = 'valor' if condicao else 'outro valos'
print(variavel)

digito = 9 # > 9 = 0
novo_digito = digito if digito <= 9 else 0
novo_digito_2 = 0 if digito > 9 else digito
print(novo_digito_2)
print('valor' if False else 'Outro_valor' if False else 'Fim')