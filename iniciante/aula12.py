"""

Interpolação basica de strings
s - string
d e i - int
f - float
x e x - hexadecimal(ABCDEF123456789)
"""
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' %(nome, preco)
print(variavel)
print('O hexadecimal de %d é %04X' %(1500, 1500))