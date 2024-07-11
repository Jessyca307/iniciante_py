"""
lista de listas e seus índices
"""
sala = [
          #0       1
          ['Maria', 'Helena'],# 0
          #0
          ['Elaine',], # 1
          # 0         1      2
          ['Luiz', 'João', 'Eduardo', (0, 10, 20, 30)], # 2
]

for salas in sala:
          print(f'para cada sala {salas}')
          for alunos in salas:
                  print(alunos)