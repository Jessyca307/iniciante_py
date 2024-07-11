"""
Repetição
while(enquanto)
Executa uma ação enquanto uma cidificação for verdadeira
"""
condicao = True

while condicao:
          nome = input(f'Digite seu nome')
          print(f'Seu nome é {nome}')

          if nome == 'sair':
            break

print('Acabou')

contador = 0

while contador <= 10:
      print(contador)
      contador = contador + 1
print('acabou')
