"""
Introdução ao desempacotamento 
tuples(tuplas) - Uma lista imutável
"""
_, nome2, *resto = ['Maria', 'Helena', 'Luiz']
print(nome2, resto)

nomes = ['Mikassa', 'catoco', 'Hioko']#('Mikassa', 'catoco', 'Hioko')
nomes = tuple(nomes)
nomes = list(nomes)
print(nomes[-1])
print(nomes)