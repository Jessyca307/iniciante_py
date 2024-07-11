"""
Formatação basica de strings
s - string
d - int
f - float
.<numero de digitos>f
x ou X - hexadecimal
(Caractere)(><^)(quantidade)
> - esqueda
< - direita
^ - centro
= - Força o numero aparecer antes dos zeros
Sinal - + ou -
ex.: 0>-100,.1f
conversion flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.6378923937:0=+10,.1f}')
print(f'hexadecimal de 1500 é {1500:08x}')
print(f'{variavel!r}')