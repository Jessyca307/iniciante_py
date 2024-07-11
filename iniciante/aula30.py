"""
Lista em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
conhecimento reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Create read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#         01234
#        -54321
#string = 'ABCDE' #5 caracteres(len)
#print(bool([])) falsy
#print(list, type(lista))


#lista = [123, True, 'luiz', 1.2, []]
#lista[-3] = 'Maria'
#print(lista)
#print(lista[2].upper() , type(lista[2]))
lista = [10, 20, 30, 40]
lista[2] = 300
del lista[2]
lista.append(50)
lista.clear()#limpa a lista
lista.insert(1,5)#adicio um item de acordo com o indice
ultimo_valor = lista.pop() #se o .pop estiver vazio ele elimina o ultimo numero do indice. Se colocar algum valor ele remove aquele valor do indice 
lista.append(60)
print(lista)
print('removido', ultimo_valor )
#print(lista[2])
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)