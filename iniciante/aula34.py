"""
Exercicio
Exiba os índices da lista
0-Maria
1-helena
2-luiz
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

lista_enumerada = enumerate(lista)

for i, nome in enumerate(lista):
        print(i, nome, lista[i])

print('#' * 10)

for item in lista_enumerada:
          print(item)

print('#' * 10)

for item in enumerate(lista):
        indice, nome = item
        print(indice, nome)

print('#' * 10)


for tupla_enumerada in enumerate(lista):
        print('For da tupla:')
        for valor in tupla_enumerada:
                print(f'\t{valor}')

#indices = range(len(lista))

#for indice in indices:
#          print(indice, lista[indice], type(lista[indice]))


