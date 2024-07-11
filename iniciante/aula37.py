"""
split e join com list e str
split - divide uma string
join - une uma string
"""
frase = '   Olha so que  , coisa interessante    '
lista_f_c = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_f_c):
          lista_frases.append(lista_f_c[i].strip())

print(lista_f_c)
print(lista_frases)
frase_unidas = '-'.join(lista_frases)
print(frase_unidas)

