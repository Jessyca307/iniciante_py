"""
Cuidado com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memoria (mutavel)
"""
lista_a = ['luiz', 'maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'qualquer'
print(lista_b)
print(lista_a)

"""
for in com lista
"""
nom = ['maria', 'helena', 'luiz']

for nome in nom:
          print(nome, type(nome))